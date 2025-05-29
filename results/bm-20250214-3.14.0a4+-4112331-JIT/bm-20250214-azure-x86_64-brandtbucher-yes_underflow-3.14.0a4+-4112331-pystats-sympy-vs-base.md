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
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,913,267</td>
<td align="right">4,048,324</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">18,581,120</td>
<td align="right">6,728,929</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,745</td>
<td align="right">1,646,121</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,587,587</td>
<td align="right">1,763,331</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,740,695</td>
<td align="right">9,046,966</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">26,538,682</td>
<td align="right">16,942,826</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,568,791</td>
<td align="right">10,197,967</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,044,578</td>
<td align="right">11,206,129</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">1,509,971</td>
<td align="right">1,942,495</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,610,164</td>
<td align="right">3,383,710</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">140,847,549</td>
<td align="right">104,039,119</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">29,770,273</td>
<td align="right">22,042,255</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">43,367,952</td>
<td align="right">32,340,889</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">159,492,593</td>
<td align="right">120,722,184</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">30,248,391</td>
<td align="right">23,444,066</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">69,106,539</td>
<td align="right">53,635,781</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">43,865,081</td>
<td align="right">34,962,624</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">182,024,731</td>
<td align="right">150,029,811</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">18,671,756</td>
<td align="right">21,865,572</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,772,434</td>
<td align="right">14,793,880</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">41,798,271</td>
<td align="right">34,887,488</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">17,693,490</td>
<td align="right">14,864,293</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">60,489,301</td>
<td align="right">51,467,763</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">15,282,072</td>
<td align="right">13,015,039</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,202,159</td>
<td align="right">2,512,526</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">15,301,267</td>
<td align="right">17,293,696</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,676,056</td>
<td align="right">3,022,984</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">203,144,933</td>
<td align="right">178,544,614</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">46,300,451</td>
<td align="right">41,238,090</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">115,456,174</td>
<td align="right">102,976,300</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,467,593</td>
<td align="right">29,918,216</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">15,421,888</td>
<td align="right">13,869,187</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">13,400,323</td>
<td align="right">14,728,689</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">25,985,847</td>
<td align="right">23,509,155</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">172,511,324</td>
<td align="right">156,622,856</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,158,478</td>
<td align="right">37,433,750</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">50,271,845</td>
<td align="right">45,954,768</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,788,563</td>
<td align="right">1,941,458</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">24,419,840</td>
<td align="right">26,494,532</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">55,882,379</td>
<td align="right">51,522,066</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">597,619,604</td>
<td align="right">551,385,526</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,343,501</td>
<td align="right">8,926,537</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,588,586</td>
<td align="right">2,440,880</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">61,545,763</td>
<td align="right">64,875,391</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">18,417,587</td>
<td align="right">19,358,446</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,806,990</td>
<td align="right">31,132,333</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">85,008,613</td>
<td align="right">80,876,145</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,439,534</td>
<td align="right">3,601,342</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">20,337,578</td>
<td align="right">19,404,930</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,818,089</td>
<td align="right">2,932,100</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">23,299,081</td>
<td align="right">24,203,381</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,950,675</td>
<td align="right">10,528,887</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,877,524</td>
<td align="right">12,310,380</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,580,806</td>
<td align="right">4,415,217</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">5,033,617</td>
<td align="right">5,202,223</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,156,842</td>
<td align="right">5,288,964</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,228,328</td>
<td align="right">6,383,183</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">39,981,536</td>
<td align="right">40,942,208</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">171,244,002</td>
<td align="right">174,485,567</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,524</td>
<td align="right">6,617,568</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,027,201</td>
<td align="right">16,303,828</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">61</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,842,387</td>
<td align="right">34,311,478</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">60,256,764</td>
<td align="right">61,130,696</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">865,933</td>
<td align="right">876,678</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,677,994</td>
<td align="right">5,744,508</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">17,488,274</td>
<td align="right">17,286,327</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,836,343</td>
<td align="right">17,671,246</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">19,920,484</td>
<td align="right">20,086,991</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">104,358,485</td>
<td align="right">105,213,667</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">919</td>
<td align="right">926</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9,068</td>
<td align="right">9,004</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,966</td>
<td align="right">2,984</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,047</td>
<td align="right">18,154</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">26,542,643</td>
<td align="right">26,697,380</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">42,396,285</td>
<td align="right">42,162,805</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,057,720</td>
<td align="right">5,032,946</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">12,801,976</td>
<td align="right">12,740,746</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">15,197,612</td>
<td align="right">15,259,226</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,944</td>
<td align="right">10,985</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">133,724</td>
<td align="right">133,225</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">43,430,910</td>
<td align="right">43,270,931</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,421</td>
<td align="right">653,043</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,419,768</td>
<td align="right">3,431,712</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,168</td>
<td align="right">24,250</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,440</td>
<td align="right">1,444</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,377</td>
<td align="right">40,290</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">16,296,599</td>
<td align="right">16,272,924</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,098,462</td>
<td align="right">21,070,003</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">171,773</td>
<td align="right">171,970</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,623,621</td>
<td align="right">6,616,769</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,220,686</td>
<td align="right">1,221,800</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">20,694</td>
<td align="right">20,682</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">17,035</td>
<td align="right">17,028</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,141</td>
<td align="right">83,111</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">147,660</td>
<td align="right">147,617</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,356</td>
<td align="right">175,309</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">78,686</td>
<td align="right">78,665</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">97,964,604</td>
<td align="right">97,939,871</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,725</td>
<td align="right">165,765</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">493,781</td>
<td align="right">493,877</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">745,688</td>
<td align="right">745,818</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,028,611</td>
<td align="right">1,028,457</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,029,207</td>
<td align="right">1,029,053</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">30,306,765</td>
<td align="right">30,302,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,521,902</td>
<td align="right">1,521,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">654,472</td>
<td align="right">654,384</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">654,488</td>
<td align="right">654,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,498,006</td>
<td align="right">4,497,418</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,350</td>
<td align="right">1,288,506</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,421</td>
<td align="right">655,343</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,421</td>
<td align="right">655,343</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,517,534</td>
<td align="right">7,516,666</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,966,818</td>
<td align="right">1,966,611</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,759,196</td>
<td align="right">1,759,361</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,919</td>
<td align="right">389,883</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,025,462</td>
<td align="right">6,024,929</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,950</td>
<td align="right">745,889</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,590,858</td>
<td align="right">6,590,359</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,376</td>
<td align="right">2,281,221</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,754,061</td>
<td align="right">5,753,690</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,408</td>
<td align="right">141,399</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,107,083</td>
<td align="right">12,106,468</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,644,040</td>
<td align="right">6,643,703</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,418,698</td>
<td align="right">2,418,581</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,336</td>
<td align="right">746,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,681</td>
<td align="right">942,638</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,069,746</td>
<td align="right">2,069,653</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,951</td>
<td align="right">1,389,889</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,548</td>
<td align="right">427,530</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,728,249</td>
<td align="right">3,728,108</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,163</td>
<td align="right">2,195,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">456,578</td>
<td align="right">456,590</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,977,790</td>
<td align="right">21,977,227</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,917,389</td>
<td align="right">10,917,125</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,431,709</td>
<td align="right">3,431,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,826</td>
<td align="right">4,181,761</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,175</td>
<td align="right">1,323,193</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,456</td>
<td align="right">1,754,471</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">597,627</td>
<td align="right">597,632</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,939,359</td>
<td align="right">9,939,276</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,550,227</td>
<td align="right">3,550,198</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,538</td>
<td align="right">1,244,529</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,036,043</td>
<td align="right">1,036,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">389,282</td>
<td align="right">389,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">372,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">339,309</td>
<td align="right">339,309</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">270,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">178,536</td>
<td align="right">178,536</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">178,534</td>
<td align="right">178,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">89,010</td>
<td align="right">89,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">14,629</td>
<td align="right">14,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">9,212</td>
<td align="right">9,212</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,941</td>
<td align="right">8,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">8,858</td>
<td align="right">8,858</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,742</td>
<td align="right">3,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,645</td>
<td align="right">2,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,679</td>
<td align="right">1,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,455</td>
<td align="right">1,455</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,055</td>
<td align="right">1,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">591</td>
<td align="right">591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">447</td>
<td align="right">447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">394</td>
<td align="right">394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">255</td>
<td align="right">255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">133</td>
<td align="right">133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">102</td>
<td align="right">102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">92</td>
<td align="right">92</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">26,515,822</td>
<td align="right">63.6%</td>
<td align="right">16,922,264</td>
<td align="right">52.8%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,925</td>
<td align="right">0.1%</td>
<td align="right">49,913</td>
<td align="right">0.2%</td>
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
<td align="right">15,083,736</td>
<td align="right">36.2%</td>
<td align="right">15,083,169</td>
<td align="right">47.0%</td>
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
<td align="right">21,549</td>
<td align="right">90.5%</td>
<td align="right">19,211</td>
<td align="right">89.3%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,256</td>
<td align="right">9.5%</td>
<td align="right">2,296</td>
<td align="right">10.7%</td>
<td align="right">1.8%</td>
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
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">10.3%</td>
<td align="right">1,521</td>
<td align="right">7.9%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">14.9%</td>
<td align="right">2,219</td>
<td align="right">11.6%</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,899</td>
<td align="right">13.5%</td>
<td align="right">2,219</td>
<td align="right">11.6%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,226</td>
<td align="right">10.3%</td>
<td align="right">2,303</td>
<td align="right">12.0%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">213</td>
<td align="right">1.0%</td>
<td align="right">207</td>
<td align="right">1.1%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">716</td>
<td align="right">3.3%</td>
<td align="right">701</td>
<td align="right">3.6%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.7%</td>
<td align="right">367</td>
<td align="right">1.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.4%</td>
<td align="right">92</td>
<td align="right">0.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">4.6%</td>
<td align="right">989</td>
<td align="right">5.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,893</td>
<td align="right">18.1%</td>
<td align="right">3,869</td>
<td align="right">20.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">702</td>
<td align="right">3.3%</td>
<td align="right">699</td>
<td align="right">3.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,212</td>
<td align="right">5.6%</td>
<td align="right">1,216</td>
<td align="right">6.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">567</td>
<td align="right">2.6%</td>
<td align="right">568</td>
<td align="right">3.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">998</td>
<td align="right">4.6%</td>
<td align="right">999</td>
<td align="right">5.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">5.0%</td>
<td align="right">1,086</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.7%</td>
<td align="right">155</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">8,858</td>
<td align="right">100.0%</td>
<td align="right">8,858</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,337,491</td>
<td align="right">20.3%</td>
<td align="right">8,920,397</td>
<td align="right">21.4%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,778</td>
<td align="right">0.0%</td>
<td align="right">10,767</td>
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
<td align="right">32,742,701</td>
<td align="right">79.7%</td>
<td align="right">32,742,681</td>
<td align="right">78.6%</td>
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
<td align="right">5,228</td>
<td align="right">84.2%</td>
<td align="right">5,353</td>
<td align="right">84.4%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">982</td>
<td align="right">15.8%</td>
<td align="right">987</td>
<td align="right">15.6%</td>
<td align="right">0.5%</td>
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
<td align="right">3,698</td>
<td align="right">70.7%</td>
<td align="right">3,817</td>
<td align="right">71.3%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">271</td>
<td align="right">5.2%</td>
<td align="right">275</td>
<td align="right">5.1%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">688</td>
<td align="right">13.2%</td>
<td align="right">690</td>
<td align="right">12.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">8.1%</td>
<td align="right">422</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">148</td>
<td align="right">2.8%</td>
<td align="right">148</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">24,850,786</td>
<td align="right">7.7%</td>
<td align="right">23,809,537</td>
<td align="right">7.4%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">24,390,497</td>
<td align="right">7.6%</td>
<td align="right">23,368,926</td>
<td align="right">7.3%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">295,926,844</td>
<td align="right">92.2%</td>
<td align="right">297,052,709</td>
<td align="right">92.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">13,673</td>
<td align="right">0.0%</td>
<td align="right">13,673</td>
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
<td align="right">484,457</td>
<td align="right">100.0%</td>
<td align="right">464,861</td>
<td align="right">100.0%</td>
<td align="right">-4.0%</td>
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
<td align="right">3,183</td>
<td align="right">75.0%</td>
<td align="right">3,185</td>
<td align="right">75.0%</td>
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
<td align="right">2,805</td>
<td align="right">66.1%</td>
<td align="right">2,805</td>
<td align="right">66.0%</td>
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
<td align="right">1,062</td>
<td align="right">100.0%</td>
<td align="right">1,064</td>
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
<td align="right">409,659</td>
<td align="right">0.5%</td>
<td align="right">115,391</td>
<td align="right">0.2%</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">25,948,371</td>
<td align="right">33.5%</td>
<td align="right">23,485,963</td>
<td align="right">31.6%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,031,298</td>
<td align="right">65.9%</td>
<td align="right">50,702,450</td>
<td align="right">68.2%</td>
<td align="right">-0.6%</td>
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
<td align="right">8,834</td>
<td align="right">19.6%</td>
<td align="right">3,287</td>
<td align="right">13.0%</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">36,315</td>
<td align="right">80.4%</td>
<td align="right">22,026</td>
<td align="right">87.0%</td>
<td align="right">-39.3%</td>
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
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">20.6%</td>
<td align="right">1,188</td>
<td align="right">5.4%</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">14,100</td>
<td align="right">38.8%</td>
<td align="right">6,588</td>
<td align="right">29.9%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,149</td>
<td align="right">8.7%</td>
<td align="right">2,697</td>
<td align="right">12.2%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">134</td>
<td align="right">0.4%</td>
<td align="right">137</td>
<td align="right">0.6%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">413</td>
<td align="right">1.1%</td>
<td align="right">408</td>
<td align="right">1.9%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,412</td>
<td align="right">17.7%</td>
<td align="right">6,345</td>
<td align="right">28.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">115</td>
<td align="right">0.3%</td>
<td align="right">116</td>
<td align="right">0.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,239</td>
<td align="right">11.7%</td>
<td align="right">4,274</td>
<td align="right">19.4%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">138</td>
<td align="right">0.4%</td>
<td align="right">138</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.3%</td>
<td align="right">91</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">44</td>
<td align="right">0.1%</td>
<td align="right">44</td>
<td align="right">0.2%</td>
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
<td align="right">4,576,871</td>
<td align="right">16.3%</td>
<td align="right">4,411,300</td>
<td align="right">15.8%</td>
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
<td align="right">23,499,995</td>
<td align="right">83.7%</td>
<td align="right">23,499,394</td>
<td align="right">84.2%</td>
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
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">1,020</td>
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
<td align="right">3,813</td>
<td align="right">96.9%</td>
<td align="right">3,795</td>
<td align="right">96.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">122</td>
<td align="right">3.1%</td>
<td align="right">122</td>
<td align="right">3.1%</td>
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
<td align="right">1,906</td>
<td align="right">50.0%</td>
<td align="right">1,887</td>
<td align="right">49.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,471</td>
<td align="right">38.6%</td>
<td align="right">1,472</td>
<td align="right">38.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">7.8%</td>
<td align="right">299</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">137</td>
<td align="right">3.6%</td>
<td align="right">137</td>
<td align="right">3.6%</td>
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
<td align="right">33,419,388</td>
<td align="right">50.5%</td>
<td align="right">29,870,627</td>
<td align="right">46.2%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,018,700</td>
<td align="right">48.4%</td>
<td align="right">34,072,798</td>
<td align="right">52.7%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">697,585</td>
<td align="right">1.1%</td>
<td align="right">697,394</td>
<td align="right">1.1%</td>
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
<td align="right">47,497</td>
<td align="right">77.5%</td>
<td align="right">46,871</td>
<td align="right">77.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,791</td>
<td align="right">22.5%</td>
<td align="right">13,802</td>
<td align="right">22.7%</td>
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
<td align="left">zip</td>
<td align="right">2,709</td>
<td align="right">5.7%</td>
<td align="right">1,516</td>
<td align="right">3.2%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,859</td>
<td align="right">6.0%</td>
<td align="right">2,813</td>
<td align="right">6.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">38,602</td>
<td align="right">81.3%</td>
<td align="right">39,221</td>
<td align="right">83.7%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,334</td>
<td align="right">2.8%</td>
<td align="right">1,328</td>
<td align="right">2.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.6%</td>
<td align="right">758</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">557</td>
<td align="right">1.2%</td>
<td align="right">557</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.8%</td>
<td align="right">382</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">29</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.1%</td>
<td align="right">24</td>
<td align="right">0.1%</td>
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
<td align="right">43,142,112</td>
<td align="right">13.3%</td>
<td align="right">47,911,233</td>
<td align="right">14.8%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">221,806,745</td>
<td align="right">68.2%</td>
<td align="right">214,404,619</td>
<td align="right">66.3%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">60,196,420</td>
<td align="right">18.5%</td>
<td align="right">61,070,117</td>
<td align="right">18.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,588</td>
<td align="right">0.0%</td>
<td align="right">18,588</td>
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
<td align="right">824,727</td>
<td align="right">94.8%</td>
<td align="right">914,713</td>
<td align="right">95.3%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,176</td>
<td align="right">5.2%</td>
<td align="right">45,386</td>
<td align="right">4.7%</td>
<td align="right">0.5%</td>
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
<td align="right">243</td>
<td align="right">0.5%</td>
<td align="right">271</td>
<td align="right">0.6%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,359</td>
<td align="right">5.2%</td>
<td align="right">2,387</td>
<td align="right">5.3%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,160</td>
<td align="right">46.8%</td>
<td align="right">21,334</td>
<td align="right">47.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,157</td>
<td align="right">7.0%</td>
<td align="right">3,147</td>
<td align="right">6.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,067</td>
<td align="right">9.0%</td>
<td align="right">4,059</td>
<td align="right">8.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,101</td>
<td align="right">6.9%</td>
<td align="right">3,096</td>
<td align="right">6.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,999</td>
<td align="right">6.6%</td>
<td align="right">3,000</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,812</td>
<td align="right">15.1%</td>
<td align="right">6,812</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">148</td>
<td align="right">0.3%</td>
<td align="right">148</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">46</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
<td align="right">0.0%</td>
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
<td align="right">245,775,367</td>
<td align="right">100.0%</td>
<td align="right">202,748,949</td>
<td align="right">100.0%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,529</td>
<td align="right">0.0%</td>
<td align="right">4,595</td>
<td align="right">0.0%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,294</td>
<td align="right">0.0%</td>
<td align="right">1,294</td>
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
<td align="right">13,566</td>
<td align="right">100.0%</td>
<td align="right">13,607</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">30</td>
<td align="right">0.0%</td>
<td align="right">31</td>
<td align="right">0.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,265,856</td>
<td align="right">100.0%</td>
<td align="right">2,265,831</td>
<td align="right">100.0%</td>
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
<td align="right">30</td>
<td align="right">100.0%</td>
<td align="right">30</td>
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
<td align="right">731,625</td>
<td align="right">72.0%</td>
<td align="right">731,589</td>
<td align="right">72.0%</td>
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
<td align="right">268,986</td>
<td align="right">26.5%</td>
<td align="right">268,986</td>
<td align="right">26.5%</td>
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
<td align="right">14,711</td>
<td align="right">1.4%</td>
<td align="right">14,711</td>
<td align="right">1.4%</td>
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
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">274</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
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
<td align="right">1,108</td>
<td align="right">100.0%</td>
<td align="right">1,108</td>
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
<td align="right">1,578,029</td>
<td align="right">17.4%</td>
<td align="right">1,576,428</td>
<td align="right">17.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">174,053</td>
<td align="right">1.9%</td>
<td align="right">174,004</td>
<td align="right">1.9%</td>
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
<td align="right">7,326,968</td>
<td align="right">80.7%</td>
<td align="right">7,328,242</td>
<td align="right">80.7%</td>
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
<td align="right">967</td>
<td align="right">3.1%</td>
<td align="right">969</td>
<td align="right">3.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,031</td>
<td align="right">96.9%</td>
<td align="right">29,994</td>
<td align="right">96.9%</td>
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
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">53.6%</td>
<td align="right">518</td>
<td align="right">53.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">292</td>
<td align="right">30.2%</td>
<td align="right">292</td>
<td align="right">30.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">102</td>
<td align="right">10.5%</td>
<td align="right">102</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3</td>
<td align="right">0.3%</td>
<td align="right">3</td>
<td align="right">0.3%</td>
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
<td align="right">591</td>
<td align="right">100.0%</td>
<td align="right">591</td>
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
<td align="right">864,225</td>
<td align="right">4.6%</td>
<td align="right">874,967</td>
<td align="right">4.7%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,741,075</td>
<td align="right">95.3%</td>
<td align="right">17,738,893</td>
<td align="right">95.3%</td>
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
<td align="right">1,132</td>
<td align="right">66.3%</td>
<td align="right">1,135</td>
<td align="right">66.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">576</td>
<td align="right">33.7%</td>
<td align="right">576</td>
<td align="right">33.7%</td>
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
<td align="right">1,132</td>
<td align="right">100.0%</td>
<td align="right">1,135</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="right">153,540,957</td>
<td align="right">93.7%</td>
<td align="right">152,105,299</td>
<td align="right">93.6%</td>
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
<td align="right">442,680</td>
<td align="right">0.3%</td>
<td align="right">442,595</td>
<td align="right">0.3%</td>
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
<td align="right">9,919,941</td>
<td align="right">6.1%</td>
<td align="right">9,919,832</td>
<td align="right">6.1%</td>
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
<td align="right">15,444</td>
<td align="right">56.7%</td>
<td align="right">15,471</td>
<td align="right">56.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">11,778</td>
<td align="right">43.3%</td>
<td align="right">11,776</td>
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
<td align="left">other</td>
<td align="right">1,901</td>
<td align="right">16.1%</td>
<td align="right">1,868</td>
<td align="right">15.9%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">6,203</td>
<td align="right">52.7%</td>
<td align="right">6,242</td>
<td align="right">53.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,267</td>
<td align="right">10.8%</td>
<td align="right">1,261</td>
<td align="right">10.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">715</td>
<td align="right">6.1%</td>
<td align="right">713</td>
<td align="right">6.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">7.5%</td>
<td align="right">883</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">723</td>
<td align="right">6.1%</td>
<td align="right">723</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.7%</td>
<td align="right">84</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">83,682,333</td>
<td align="right">100.0%</td>
<td align="right">80,850,418</td>
<td align="right">100.0%</td>
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
<td align="right">6,374</td>
<td align="right">0.0%</td>
<td align="right">6,308</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">302</td>
<td align="right">11.2%</td>
<td align="right">296</td>
<td align="right">11.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,392</td>
<td align="right">88.8%</td>
<td align="right">2,400</td>
<td align="right">89.0%</td>
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
<td align="left">sequence</td>
<td align="right">259</td>
<td align="right">85.8%</td>
<td align="right">253</td>
<td align="right">85.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.2%</td>
<td align="right">43</td>
<td align="right">14.5%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,300,644,367</td>
<td align="right">35.3%</td>
<td align="right">1,156,039,808</td>
<td align="right">34.8%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,137,813,562</td>
<td align="right">58.1%</td>
<td align="right">1,938,815,943</td>
<td align="right">58.3%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">170,486,169</td>
<td align="right">4.6%</td>
<td align="right">156,166,368</td>
<td align="right">4.7%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">71,201,701</td>
<td align="right">1.9%</td>
<td align="right">74,633,482</td>
<td align="right">2.2%</td>
<td align="right">4.8%</td>
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
<td align="right">26,515,822</td>
<td align="right">13.6%</td>
<td align="right">16,922,264</td>
<td align="right">9.4%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,419,388</td>
<td align="right">17.2%</td>
<td align="right">29,870,627</td>
<td align="right">16.7%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">25,948,371</td>
<td align="right">13.3%</td>
<td align="right">23,485,963</td>
<td align="right">13.1%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,337,491</td>
<td align="right">4.3%</td>
<td align="right">8,920,397</td>
<td align="right">5.0%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,390,497</td>
<td align="right">12.5%</td>
<td align="right">23,368,926</td>
<td align="right">13.0%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,576,871</td>
<td align="right">2.4%</td>
<td align="right">4,411,300</td>
<td align="right">2.5%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">60,196,420</td>
<td align="right">30.9%</td>
<td align="right">61,070,117</td>
<td align="right">34.1%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">864,225</td>
<td align="right">0.4%</td>
<td align="right">874,967</td>
<td align="right">0.5%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,919,941</td>
<td align="right">5.1%</td>
<td align="right">9,919,832</td>
<td align="right">5.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.1%</td>
<td align="right">268,986</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">20,591,850</td>
<td align="right">28.9%</td>
<td align="right">26,953,985</td>
<td align="right">36.1%</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,159,240</td>
<td align="right">10.1%</td>
<td align="right">5,220,274</td>
<td align="right">7.0%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,113,865</td>
<td align="right">8.6%</td>
<td align="right">5,128,833</td>
<td align="right">6.9%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">11,809,388</td>
<td align="right">16.6%</td>
<td align="right">12,114,566</td>
<td align="right">16.2%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,165,891</td>
<td align="right">4.4%</td>
<td align="right">3,204,849</td>
<td align="right">4.3%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">470,009</td>
<td align="right">0.7%</td>
<td align="right">465,649</td>
<td align="right">0.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,423,119</td>
<td align="right">16.0%</td>
<td align="right">11,367,025</td>
<td align="right">15.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,577,250</td>
<td align="right">2.2%</td>
<td align="right">1,575,649</td>
<td align="right">2.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,620</td>
<td align="right">7.2%</td>
<td align="right">5,102,529</td>
<td align="right">6.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,595</td>
<td align="right">3.0%</td>
<td align="right">2,103,583</td>
<td align="right">2.8%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,495,999</td>
<td align="right">10.7%</td>
<td align="right">22,440,207</td>
<td align="right">10.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,436,702</td>
<td align="right">53.4%</td>
<td align="right">112,550,871</td>
<td align="right">53.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,826,557</td>
<td align="right">89.2%</td>
<td align="right">187,971,778</td>
<td align="right">89.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,337,633</td>
<td align="right">19.6%</td>
<td align="right">41,369,573</td>
<td align="right">19.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,622,236</td>
<td align="right">35.9%</td>
<td align="right">75,653,297</td>
<td align="right">35.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,623,021</td>
<td align="right">35.9%</td>
<td align="right">75,654,082</td>
<td align="right">35.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">98,119,020</td>
<td align="right">46.6%</td>
<td align="right">98,094,289</td>
<td align="right">46.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">98,119,020</td>
<td align="right">46.6%</td>
<td align="right">98,094,289</td>
<td align="right">46.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,491,053</td>
<td align="right">8.8%</td>
<td align="right">18,490,506</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,332,199</td>
<td align="right">4.4%</td>
<td align="right">9,332,043</td>
<td align="right">4.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,381</td>
<td align="right">0.5%</td>
<td align="right">950,383</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">652</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">348</td>
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
<td align="right">1,019,341</td>
<td align="right"></td>
<td align="right">839,474</td>
<td align="right"></td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">443,408,791</td>
<td align="right">9.1%</td>
<td align="right">379,093,269</td>
<td align="right">7.8%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">707,552,600</td>
<td align="right">12.3%</td>
<td align="right">616,377,096</td>
<td align="right">10.7%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,661,753,899</td>
<td align="right">34.1%</td>
<td align="right">1,829,581,557</td>
<td align="right">37.5%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,758,092,135</td>
<td align="right">30.6%</td>
<td align="right">1,925,354,739</td>
<td align="right">33.4%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,651,624,861</td>
<td align="right">33.9%</td>
<td align="right">1,497,288,648</td>
<td align="right">30.7%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,009,694,525</td>
<td align="right">34.9%</td>
<td align="right">1,858,896,448</td>
<td align="right">32.3%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,275,866,820</td>
<td align="right">22.2%</td>
<td align="right">1,360,927,373</td>
<td align="right">23.6%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,118,802,316</td>
<td align="right">22.9%</td>
<td align="right">1,177,054,520</td>
<td align="right">24.1%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,345,286</td>
<td align="right"></td>
<td align="right">3,171,977</td>
<td align="right"></td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">147,769,476</td>
<td align="right"></td>
<td align="right">155,352,571</td>
<td align="right"></td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">764,180</td>
<td align="right">0.1%</td>
<td align="right">775,219</td>
<td align="right">0.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,904</td>
<td align="right">0.0%</td>
<td align="right">9,025</td>
<td align="right">0.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">339,786,817</td>
<td align="right">66.0%</td>
<td align="right">342,743,293</td>
<td align="right">66.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">339,821,462</td>
<td align="right"></td>
<td align="right">342,777,945</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,327,390</td>
<td align="right"></td>
<td align="right">2,333,987</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">265,057,837</td>
<td align="right"></td>
<td align="right">265,676,744</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,370</td>
<td align="right"></td>
<td align="right">866,220</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">174,772,838</td>
<td align="right">34.0%</td>
<td align="right">174,796,854</td>
<td align="right">33.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">187,416,784</td>
<td align="right"></td>
<td align="right">187,440,165</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">173,999,754</td>
<td align="right">33.8%</td>
<td align="right">174,012,610</td>
<td align="right">33.6%</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">10,394</td>
<td align="right">59.6%</td>
<td align="right">2,093</td>
<td align="right">17.3%</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">10,458</td>
<td align="right">60.0%</td>
<td align="right">2,476</td>
<td align="right">20.4%</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">7,032</td>
<td align="right">40.4%</td>
<td align="right">10,028</td>
<td align="right">82.7%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">223</td>
<td align="right">1.3%</td>
<td align="right">294</td>
<td align="right">2.4%</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">17,426</td>
<td align="right"></td>
<td align="right">12,121</td>
<td align="right"></td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,908,257,276</td>
<td align="right">2,111.8%</td>
<td align="right">3,673,246,641</td>
<td align="right">2,363.5%</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">236</td>
<td align="right">1.4%</td>
<td align="right">293</td>
<td align="right">2.4%</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">137,714,606</td>
<td align="right"></td>
<td align="right">155,415,647</td>
<td align="right"></td>
<td align="right">12.9%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">7,032</td>
<td align="right"></td>
<td align="right">10,028</td>
<td align="right"></td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">6,944</td>
<td align="right">98.7%</td>
<td align="right">9,622</td>
<td align="right">96.0%</td>
<td align="right">38.6%</td>
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
<td align="right">1,030</td>
<td align="right">14.6%</td>
<td align="right">458</td>
<td align="right">4.6%</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,132</td>
<td align="right">16.1%</td>
<td align="right">2,369</td>
<td align="right">23.6%</td>
<td align="right">109.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,644</td>
<td align="right">37.6%</td>
<td align="right">3,841</td>
<td align="right">38.3%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,384</td>
<td align="right">19.7%</td>
<td align="right">2,229</td>
<td align="right">22.2%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">821</td>
<td align="right">11.7%</td>
<td align="right">1,022</td>
<td align="right">10.2%</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">109</td>
<td align="right">1.1%</td>
<td align="right">419.0%</td>
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
<td align="right">273</td>
<td align="right">3.9%</td>
<td align="right">329</td>
<td align="right">3.3%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">863</td>
<td align="right">12.3%</td>
<td align="right">985</td>
<td align="right">9.8%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,098</td>
<td align="right">15.6%</td>
<td align="right">1,901</td>
<td align="right">19.0%</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">3,330</td>
<td align="right">47.4%</td>
<td align="right">4,407</td>
<td align="right">43.9%</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,194</td>
<td align="right">17.0%</td>
<td align="right">1,652</td>
<td align="right">16.5%</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">165</td>
<td align="right">2.3%</td>
<td align="right">327</td>
<td align="right">3.3%</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.2%</td>
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
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">73,352</td>
<td align="right">11,936,098</td>
<td align="right">16,172.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">501</td>
<td align="right">62,491</td>
<td align="right">12,373.3%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">2,851,038</td>
<td align="right">10,486.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">245,074</td>
<td align="right">12,938,447</td>
<td align="right">5,179.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">174,242</td>
<td align="right">5,545,555</td>
<td align="right">3,082.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">651,739</td>
<td align="right">10,245,336</td>
<td align="right">1,472.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,302,956</td>
<td align="right">14,384,349</td>
<td align="right">524.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">28,820</td>
<td align="right">176,394</td>
<td align="right">512.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,405,419</td>
<td align="right">6,243,175</td>
<td align="right">344.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,405,419</td>
<td align="right">6,243,175</td>
<td align="right">344.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">14,126,229</td>
<td align="right">53,987,687</td>
<td align="right">282.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,788,280</td>
<td align="right">16,640,866</td>
<td align="right">247.5%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,384,614</td>
<td align="right">4,213,638</td>
<td align="right">204.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">159,560</td>
<td align="right">410,966</td>
<td align="right">157.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">8,869,661</td>
<td align="right">21,481,665</td>
<td align="right">142.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">12,443,610</td>
<td align="right">29,056,491</td>
<td align="right">133.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">5,190,276</td>
<td align="right">11,992,699</td>
<td align="right">131.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">11,215,951</td>
<td align="right">25,536,635</td>
<td align="right">127.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">8,748,911</td>
<td align="right">19,774,368</td>
<td align="right">126.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,169,966</td>
<td align="right">4,429,918</td>
<td align="right">104.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">8,974,324</td>
<td align="right">18,167,787</td>
<td align="right">102.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,961,696</td>
<td align="right">26,657,715</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">26,390,399</td>
<td align="right">48,296,136</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,844,545</td>
<td align="right">14,217,139</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">42,814,179</td>
<td align="right">74,781,114</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">4,389,851</td>
<td align="right">7,621,430</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,042,190</td>
<td align="right">17,080,347</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">10,325,747</td>
<td align="right">17,492,873</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">8,281,857</td>
<td align="right">13,972,473</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,382,788</td>
<td align="right">2,319,988</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">49,323,631</td>
<td align="right">78,772,500</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">18,574,721</td>
<td align="right">29,618,674</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,692,503</td>
<td align="right">728,643</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">28,200,297</td>
<td align="right">43,757,758</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">630,363</td>
<td align="right">283,368</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">98,773</td>
<td align="right">44,746</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,452,030</td>
<td align="right">17,622,806</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">8,383,881</td>
<td align="right">12,759,514</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">64,714,377</td>
<td align="right">93,863,714</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">39,513</td>
<td align="right">55,382</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">6,479,537</td>
<td align="right">8,749,273</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">371,728,901</td>
<td align="right">497,624,085</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,285,622</td>
<td align="right">852,328</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">12,156,187</td>
<td align="right">16,179,279</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">43,862,074</td>
<td align="right">58,167,506</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">117,540,498</td>
<td align="right">154,892,730</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">389,868</td>
<td align="right">270,458</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">915,823</td>
<td align="right">638,587</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">563,070</td>
<td align="right">401,126</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">559,107</td>
<td align="right">403,989</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">22,839,912</td>
<td align="right">29,038,383</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">28,050,414</td>
<td align="right">35,525,472</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">18,589,594</td>
<td align="right">23,150,758</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">1,759,295</td>
<td align="right">2,180,410</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">13,032,205</td>
<td align="right">16,136,513</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">316,688,620</td>
<td align="right">391,322,140</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">13,843,909</td>
<td align="right">10,626,892</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">20,094,669</td>
<td align="right">24,726,888</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">20,094,669</td>
<td align="right">24,726,888</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">18,027,718</td>
<td align="right">21,938,233</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">6,788,888</td>
<td align="right">8,106,052</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">2,451,958</td>
<td align="right">2,927,330</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,733,239</td>
<td align="right">10,381,400</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">8,733,867</td>
<td align="right">10,382,028</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">8,733,867</td>
<td align="right">10,382,028</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">27,420,704</td>
<td align="right">32,530,842</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">123,548,363</td>
<td align="right">101,310,087</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">19,151,985</td>
<td align="right">22,422,909</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,827,746</td>
<td align="right">1,517,088</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">6,317,028</td>
<td align="right">5,377,685</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">12,007,267</td>
<td align="right">13,708,763</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">37,779,596</td>
<td align="right">43,079,393</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">137,714,606</td>
<td align="right">155,415,647</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">57,982,381</td>
<td align="right">64,453,340</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">17,935,872</td>
<td align="right">19,883,825</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40,454,304</td>
<td align="right">44,533,025</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,275,455</td>
<td align="right">1,151,914</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,275,455</td>
<td align="right">1,151,914</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">179,408,142</td>
<td align="right">196,439,467</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">26,525,482</td>
<td align="right">24,335,196</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">39,326,374</td>
<td align="right">42,418,565</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">48,672,185</td>
<td align="right">52,194,210</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">131,021,499</td>
<td align="right">140,315,763</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">13,288,554</td>
<td align="right">12,421,357</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">32,913,322</td>
<td align="right">31,047,278</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">4,855,984</td>
<td align="right">5,125,548</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">17,454,824</td>
<td align="right">16,527,706</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">33,643,489</td>
<td align="right">31,885,600</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">3,163,769</td>
<td align="right">3,328,387</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">7,657,122</td>
<td align="right">8,044,014</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">27,069,055</td>
<td align="right">26,013,158</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">5,968,440</td>
<td align="right">5,801,836</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">5,968,440</td>
<td align="right">5,801,836</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">10,042,103</td>
<td align="right">9,782,655</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">12,721,071</td>
<td align="right">13,035,051</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">5,934,210</td>
<td align="right">5,804,113</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">24,402</td>
<td align="right">24,901</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">24,402</td>
<td align="right">24,901</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">48,722,842</td>
<td align="right">47,874,531</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">41,693,536</td>
<td align="right">41,023,820</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">42,616,759</td>
<td align="right">42,109,366</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,512,344</td>
<td align="right">5,573,358</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">52,034,747</td>
<td align="right">51,459,289</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">13,501,802</td>
<td align="right">13,364,761</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">13,198,993</td>
<td align="right">13,084,862</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">13,198,993</td>
<td align="right">13,084,862</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,042,776</td>
<td align="right">7,984,857</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">1,719,044</td>
<td align="right">1,708,348</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">11,820,470</td>
<td align="right">11,759,713</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">12,350,016</td>
<td align="right">12,412,084</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">5,632,295</td>
<td align="right">5,660,431</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">17,744,335</td>
<td align="right">17,677,241</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">6,747,321</td>
<td align="right">6,728,253</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">4,658,755</td>
<td align="right">4,649,042</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">2,841,410</td>
<td align="right">2,844,283</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,797,188</td>
<td align="right">15,792,721</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">6,909,183</td>
<td align="right">6,908,098</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">6,909,183</td>
<td align="right">6,908,098</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">6,504,709</td>
<td align="right">6,503,691</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,559,369</td>
<td align="right">6,558,351</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,513,982</td>
<td align="right">2,513,592</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,525,686</td>
<td align="right">6,525,013</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,525,686</td>
<td align="right">6,525,013</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">188,307</td>
<td align="right">188,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">320,573</td>
<td align="right">320,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">144,184</td>
<td align="right">144,184</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">52,447</td>
<td align="right">52,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,228</td>
<td align="right">18,228</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,166</td>
<td align="right">5,166</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">628</td>
<td align="right">628</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">32,137,818</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">2,923,814</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">2,923,039</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">2,823,607</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">1,435,165</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">126,674</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">6,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right"></td>
<td align="right">2,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">499</td>
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
<td align="right">1,792</td>
<td align="right">1,882</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">815</td>
<td align="right">845</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">21</td>
<td align="right">21</td>
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
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-05-05
