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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,276,352</td>
<td align="right">6,886,572</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">8,672,745</td>
<td align="right">7,604,874</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">383,859</td>
<td align="right">429,786</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">91,371</td>
<td align="right">100,695</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">642,747</td>
<td align="right">602,742</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,397,214</td>
<td align="right">1,317,204</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,446,853</td>
<td align="right">4,197,553</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,393,286</td>
<td align="right">2,273,271</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">144,186</td>
<td align="right">137,109</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">23,029,521</td>
<td align="right">21,908,679</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">885,339</td>
<td align="right">845,334</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,962,298</td>
<td align="right">4,739,803</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">82,995,434</td>
<td align="right">80,436,170</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">68,756,854</td>
<td align="right">66,696,934</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">13,231,497</td>
<td align="right">12,948,669</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,811,763</td>
<td align="right">3,730,742</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">26,826,180</td>
<td align="right">26,292,042</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">96,322,462</td>
<td align="right">94,486,201</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">30,016,831</td>
<td align="right">29,531,605</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">532,434</td>
<td align="right">524,664</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,718,741</td>
<td align="right">5,635,308</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,837,310</td>
<td align="right">2,797,305</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">33,822,317</td>
<td align="right">33,347,660</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,843,001</td>
<td align="right">2,882,607</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,816,604</td>
<td align="right">5,738,805</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,791,737</td>
<td align="right">3,837,790</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">6,804,717</td>
<td align="right">6,726,918</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">64,145,280</td>
<td align="right">63,442,443</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,963,835</td>
<td align="right">2,995,335</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,846,586</td>
<td align="right">8,754,795</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">81,606</td>
<td align="right">80,766</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,789,956</td>
<td align="right">1,772,505</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">5,357,988</td>
<td align="right">5,308,632</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">4,287,549</td>
<td align="right">4,251,498</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,790,329</td>
<td align="right">8,723,921</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">18,958,644</td>
<td align="right">19,100,643</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">65,141,995</td>
<td align="right">64,656,385</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">7,051,433</td>
<td align="right">7,002,104</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">70,431,340</td>
<td align="right">69,955,465</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">8,203,228</td>
<td align="right">8,154,193</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">66,046,907</td>
<td align="right">65,685,026</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">349,346,496</td>
<td align="right">347,547,129</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">20,405,990</td>
<td align="right">20,314,871</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">20,559,164</td>
<td align="right">20,470,208</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,079,748</td>
<td align="right">10,038,147</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">8,236,620</td>
<td align="right">8,269,716</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,288,668</td>
<td align="right">2,280,892</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">7,900,710</td>
<td align="right">7,876,071</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">3,944,598</td>
<td align="right">3,932,817</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">29,985,326</td>
<td align="right">30,072,053</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,853,013</td>
<td align="right">4,839,773</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">32,705,632</td>
<td align="right">32,630,017</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,265,917</td>
<td align="right">4,274,590</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">12,914,790</td>
<td align="right">12,891,228</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">27,294,876</td>
<td align="right">27,254,871</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,541,753</td>
<td align="right">5,533,983</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">52,500</td>
<td align="right">52,437</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">51,065,388</td>
<td align="right">51,011,586</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">32,486,244</td>
<td align="right">32,465,685</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">14,999,629</td>
<td align="right">14,993,230</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">111,379,442</td>
<td align="right">111,335,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,769,119</td>
<td align="right">5,771,273</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">32,002,934</td>
<td align="right">31,991,153</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,611,203</td>
<td align="right">2,610,363</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">53,604,111</td>
<td align="right">53,587,731</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">101,608,068</td>
<td align="right">101,623,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">164,052</td>
<td align="right">164,037</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,345,699</td>
<td align="right">16,344,850</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">983,466</td>
<td align="right">983,457</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,324,853</td>
<td align="right">2,324,832</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">98,927,053</td>
<td align="right">98,926,183</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,781,184</td>
<td align="right">1,781,178</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">27,380,147</td>
<td align="right">27,380,132</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">42,157,893</td>
<td align="right">42,157,893</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">32,927,142</td>
<td align="right">32,927,142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">25,268,733</td>
<td align="right">25,268,733</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">16,452,870</td>
<td align="right">16,452,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">15,379,999</td>
<td align="right">15,379,999</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">15,090,844</td>
<td align="right">15,090,844</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">13,413,813</td>
<td align="right">13,413,813</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">12,973,059</td>
<td align="right">12,973,059</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,650,463</td>
<td align="right">12,650,463</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,626,968</td>
<td align="right">8,626,968</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">8,512,224</td>
<td align="right">8,512,224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,496,663</td>
<td align="right">8,496,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">7,779,889</td>
<td align="right">7,779,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">7,541,035</td>
<td align="right">7,541,035</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,275,429</td>
<td align="right">7,275,429</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">6,826,812</td>
<td align="right">6,826,812</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,825,525</td>
<td align="right">6,825,525</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">6,727,369</td>
<td align="right">6,727,369</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">6,334,163</td>
<td align="right">6,334,163</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">6,065,283</td>
<td align="right">6,065,283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">5,622,288</td>
<td align="right">5,622,288</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">5,476,359</td>
<td align="right">5,476,359</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,663,155</td>
<td align="right">4,663,155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">4,414,534</td>
<td align="right">4,414,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,203,255</td>
<td align="right">4,203,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,110,874</td>
<td align="right">4,110,874</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,036,200</td>
<td align="right">4,036,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,687,180</td>
<td align="right">3,687,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,366,023</td>
<td align="right">3,366,023</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">3,323,628</td>
<td align="right">3,323,628</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">3,285,093</td>
<td align="right">3,285,093</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">2,564,982</td>
<td align="right">2,564,982</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,433,417</td>
<td align="right">2,433,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,327,892</td>
<td align="right">2,327,892</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,180,430</td>
<td align="right">2,180,430</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,993,593</td>
<td align="right">1,993,593</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,693,671</td>
<td align="right">1,693,671</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,480,101</td>
<td align="right">1,480,101</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,441,440</td>
<td align="right">1,441,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,427,055</td>
<td align="right">1,427,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,347,927</td>
<td align="right">1,347,927</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,325,394</td>
<td align="right">1,325,394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,320,606</td>
<td align="right">1,320,606</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,280,790</td>
<td align="right">1,280,790</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,273,755</td>
<td align="right">1,273,755</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,236,438</td>
<td align="right">1,236,438</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,231,820</td>
<td align="right">1,231,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,195,194</td>
<td align="right">1,195,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,195,194</td>
<td align="right">1,195,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">902,538</td>
<td align="right">902,538</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">878,031</td>
<td align="right">878,031</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">845,187</td>
<td align="right">845,187</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">828,723</td>
<td align="right">828,723</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">737,562</td>
<td align="right">737,562</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">735,838</td>
<td align="right">735,838</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">700,791</td>
<td align="right">700,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">536,256</td>
<td align="right">536,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">504,126</td>
<td align="right">504,126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">490,308</td>
<td align="right">490,308</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">465,927</td>
<td align="right">465,927</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">455,448</td>
<td align="right">455,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">452,928</td>
<td align="right">452,928</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">451,731</td>
<td align="right">451,731</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">422,163</td>
<td align="right">422,163</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">333,543</td>
<td align="right">333,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">326,676</td>
<td align="right">326,676</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">285,327</td>
<td align="right">285,327</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">254,352</td>
<td align="right">254,352</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">245,763</td>
<td align="right">245,763</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">243,789</td>
<td align="right">243,789</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">241,731</td>
<td align="right">241,731</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">212,394</td>
<td align="right">212,394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">209,244</td>
<td align="right">209,244</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">203,574</td>
<td align="right">203,574</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">195,615</td>
<td align="right">195,615</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">138,957</td>
<td align="right">138,957</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">128,205</td>
<td align="right">128,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">127,596</td>
<td align="right">127,596</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">120,267</td>
<td align="right">120,267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">110,460</td>
<td align="right">110,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">80,094</td>
<td align="right">80,094</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">79,674</td>
<td align="right">79,674</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">74,319</td>
<td align="right">74,319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,135</td>
<td align="right">72,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">65,373</td>
<td align="right">65,373</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">60,816</td>
<td align="right">60,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">56,952</td>
<td align="right">56,952</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">30,156</td>
<td align="right">30,156</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">28,140</td>
<td align="right">28,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">21,294</td>
<td align="right">21,294</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">20,706</td>
<td align="right">20,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">20,475</td>
<td align="right">20,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">18,207</td>
<td align="right">18,207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">14,049</td>
<td align="right">14,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">13,881</td>
<td align="right">13,881</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">10,395</td>
<td align="right">10,395</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,972</td>
<td align="right">6,972</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">5,985</td>
<td align="right">5,985</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,502</td>
<td align="right">5,502</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">4,242</td>
<td align="right">4,242</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">4,011</td>
<td align="right">4,011</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,465</td>
<td align="right">3,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,638</td>
<td align="right">1,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,239</td>
<td align="right">1,239</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">609</td>
<td align="right">609</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">315</td>
<td align="right">315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">210</td>
<td align="right">210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">94,378</td>
<td align="right">0.3%</td>
<td align="right">98,830</td>
<td align="right">0.3%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,928,383</td>
<td align="right">14.0%</td>
<td align="right">4,706,224</td>
<td align="right">13.5%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">30,104,040</td>
<td align="right">85.6%</td>
<td align="right">30,139,527</td>
<td align="right">86.2%</td>
<td align="right">0.1%</td>
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
<td align="right">20,622</td>
<td align="right">57.9%</td>
<td align="right">20,286</td>
<td align="right">57.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">14,973</td>
<td align="right">42.1%</td>
<td align="right">15,057</td>
<td align="right">42.6%</td>
<td align="right">0.6%</td>
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
<td align="right">5,229</td>
<td align="right">25.4%</td>
<td align="right">4,935</td>
<td align="right">24.3%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">588</td>
<td align="right">2.9%</td>
<td align="right">567</td>
<td align="right">2.8%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,381</td>
<td align="right">16.4%</td>
<td align="right">3,360</td>
<td align="right">16.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">2,961</td>
<td align="right">14.4%</td>
<td align="right">2,961</td>
<td align="right">14.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">2,310</td>
<td align="right">11.2%</td>
<td align="right">2,310</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,289</td>
<td align="right">11.1%</td>
<td align="right">2,289</td>
<td align="right">11.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">777</td>
<td align="right">3.8%</td>
<td align="right">777</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">756</td>
<td align="right">3.7%</td>
<td align="right">756</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">336</td>
<td align="right">1.6%</td>
<td align="right">336</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">336</td>
<td align="right">1.6%</td>
<td align="right">336</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">210</td>
<td align="right">1.0%</td>
<td align="right">210</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">210</td>
<td align="right">1.0%</td>
<td align="right">210</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">189</td>
<td align="right">0.9%</td>
<td align="right">189</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">147</td>
<td align="right">0.7%</td>
<td align="right">147</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">105</td>
<td align="right">0.5%</td>
<td align="right">105</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
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
<td align="right">737,562</td>
<td align="right">100.0%</td>
<td align="right">737,562</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,686,096</td>
<td align="right">10.0%</td>
<td align="right">12,644,012</td>
<td align="right">10.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,588,255</td>
<td align="right">9.9%</td>
<td align="right">12,546,948</td>
<td align="right">9.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">113,966,774</td>
<td align="right">89.8%</td>
<td align="right">114,010,349</td>
<td align="right">89.8%</td>
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
<td align="right">6,720</td>
<td align="right">0.0%</td>
<td align="right">6,720</td>
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
<td align="right">339,572</td>
<td align="right">100.0%</td>
<td align="right">338,795</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">483</td>
<td align="right">483 / 0 !!</td>
<td align="right">483</td>
<td align="right">483 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">636,615</td>
<td align="right">96.7%</td>
<td align="right">636,615</td>
<td align="right">96.7%</td>
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
<td align="right">637,287</td>
<td align="right">96.8%</td>
<td align="right">637,287</td>
<td align="right">96.8%</td>
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
<td align="right">21,966</td>
<td align="right">100.0%</td>
<td align="right">21,966</td>
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
<td align="right">4,830,246</td>
<td align="right">11.5%</td>
<td align="right">4,817,007</td>
<td align="right">11.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">37,036,929</td>
<td align="right">88.4%</td>
<td align="right">37,036,923</td>
<td align="right">88.4%</td>
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
<td align="right">29,484</td>
<td align="right">0.1%</td>
<td align="right">29,484</td>
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
<td align="right">11,028</td>
<td align="right">47.3%</td>
<td align="right">11,027</td>
<td align="right">47.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,285</td>
<td align="right">52.7%</td>
<td align="right">12,285</td>
<td align="right">52.7%</td>
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
<td align="right">360</td>
<td align="right">3.3%</td>
<td align="right">359</td>
<td align="right">3.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">4,305</td>
<td align="right">39.0%</td>
<td align="right">4,305</td>
<td align="right">39.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">3,591</td>
<td align="right">32.6%</td>
<td align="right">3,591</td>
<td align="right">32.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">882</td>
<td align="right">8.0%</td>
<td align="right">882</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">882</td>
<td align="right">8.0%</td>
<td align="right">882</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">420</td>
<td align="right">3.8%</td>
<td align="right">420</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">210</td>
<td align="right">1.9%</td>
<td align="right">210</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">168</td>
<td align="right">1.5%</td>
<td align="right">168</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">168</td>
<td align="right">1.5%</td>
<td align="right">168</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">21</td>
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
<td align="right">3,789,050</td>
<td align="right">33.5%</td>
<td align="right">3,708,050</td>
<td align="right">33.0%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,475,830</td>
<td align="right">66.1%</td>
<td align="right">7,475,830</td>
<td align="right">66.6%</td>
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
<td align="right">26,439</td>
<td align="right">0.2%</td>
<td align="right">26,439</td>
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
<td align="left">Failure</td>
<td align="right">18,345</td>
<td align="right">79.1%</td>
<td align="right">18,324</td>
<td align="right">79.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,851</td>
<td align="right">20.9%</td>
<td align="right">4,851</td>
<td align="right">20.9%</td>
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
<td align="right">3,738</td>
<td align="right">20.4%</td>
<td align="right">3,717</td>
<td align="right">20.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,181</td>
<td align="right">44.6%</td>
<td align="right">8,181</td>
<td align="right">44.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">4,179</td>
<td align="right">22.8%</td>
<td align="right">4,179</td>
<td align="right">22.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,247</td>
<td align="right">12.2%</td>
<td align="right">2,247</td>
<td align="right">12.3%</td>
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
<td align="right">5,681,445</td>
<td align="right">11.4%</td>
<td align="right">5,598,033</td>
<td align="right">11.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">43,849,585</td>
<td align="right">88.1%</td>
<td align="right">43,942,549</td>
<td align="right">88.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">231,084</td>
<td align="right">0.5%</td>
<td align="right">231,084</td>
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
<td align="left">Failure</td>
<td align="right">22,134</td>
<td align="right">53.2%</td>
<td align="right">22,113</td>
<td align="right">53.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">19,488</td>
<td align="right">46.8%</td>
<td align="right">19,488</td>
<td align="right">46.8%</td>
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
<td align="right">4,704</td>
<td align="right">21.3%</td>
<td align="right">4,683</td>
<td align="right">21.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,174</td>
<td align="right">27.9%</td>
<td align="right">6,174</td>
<td align="right">27.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">4,872</td>
<td align="right">22.0%</td>
<td align="right">4,872</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,953</td>
<td align="right">8.8%</td>
<td align="right">1,953</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">1,155</td>
<td align="right">5.2%</td>
<td align="right">1,155</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">924</td>
<td align="right">4.2%</td>
<td align="right">924</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">630</td>
<td align="right">2.8%</td>
<td align="right">630</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">630</td>
<td align="right">2.8%</td>
<td align="right">630</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">525</td>
<td align="right">2.4%</td>
<td align="right">525</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">231</td>
<td align="right">1.0%</td>
<td align="right">231</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">189</td>
<td align="right">0.9%</td>
<td align="right">189</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
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
<td align="left">list</td>
<td align="right">9,144,742</td>
<td align="right">9,144,742 / 0 !!</td>
<td align="right">9,144,742</td>
<td align="right">9,144,742 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">5,551,014</td>
<td align="right">5,551,014 / 0 !!</td>
<td align="right">5,551,014</td>
<td align="right">5,551,014 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,654,292</td>
<td align="right">3,654,292 / 0 !!</td>
<td align="right">3,654,292</td>
<td align="right">3,654,292 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">858,081</td>
<td align="right">858,081 / 0 !!</td>
<td align="right">858,081</td>
<td align="right">858,081 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">728,469</td>
<td align="right">728,469 / 0 !!</td>
<td align="right">728,469</td>
<td align="right">728,469 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">363,510</td>
<td align="right">363,510 / 0 !!</td>
<td align="right">363,510</td>
<td align="right">363,510 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">243,705</td>
<td align="right">243,705 / 0 !!</td>
<td align="right">243,705</td>
<td align="right">243,705 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">13,713</td>
<td align="right">13,713 / 0 !!</td>
<td align="right">13,713</td>
<td align="right">13,713 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">6,804</td>
<td align="right">6,804 / 0 !!</td>
<td align="right">6,804</td>
<td align="right">6,804 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
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
<td align="right">45,969,578</td>
<td align="right">19.0%</td>
<td align="right">43,666,807</td>
<td align="right">18.3%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">163,331,331</td>
<td align="right">67.6%</td>
<td align="right">162,660,448</td>
<td align="right">68.1%</td>
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
<td align="right">31,994,361</td>
<td align="right">13.2%</td>
<td align="right">31,977,876</td>
<td align="right">13.4%</td>
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
<td align="right">341,082</td>
<td align="right">0.1%</td>
<td align="right">341,082</td>
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
<td align="right">985,488</td>
<td align="right">84.1%</td>
<td align="right">942,018</td>
<td align="right">83.7%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">186,858</td>
<td align="right">15.9%</td>
<td align="right">182,784</td>
<td align="right">16.3%</td>
<td align="right">-2.2%</td>
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
<td align="right">21,063</td>
<td align="right">11.3%</td>
<td align="right">21,063</td>
<td align="right">11.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">18,942</td>
<td align="right">10.1%</td>
<td align="right">18,942</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">15,603</td>
<td align="right">8.4%</td>
<td align="right">15,603</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">4,536</td>
<td align="right">2.4%</td>
<td align="right">4,536</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,591</td>
<td align="right">1.9%</td>
<td align="right">3,591</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">1,869</td>
<td align="right">1.0%</td>
<td align="right">1,869</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">1,806</td>
<td align="right">1.0%</td>
<td align="right">1,806</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,092</td>
<td align="right">0.6%</td>
<td align="right">1,092</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">840</td>
<td align="right">0.4%</td>
<td align="right">840</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">756</td>
<td align="right">0.4%</td>
<td align="right">756</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">609</td>
<td align="right">0.3%</td>
<td align="right">609</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">546</td>
<td align="right">0.3%</td>
<td align="right">546</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">105</td>
<td align="right">0.1%</td>
<td align="right">105</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
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
<td align="right">129,246,115</td>
<td align="right">99.8%</td>
<td align="right">128,057,668</td>
<td align="right">99.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">103,509</td>
<td align="right">0.1%</td>
<td align="right">103,509</td>
<td align="right">0.1%</td>
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
<td align="right">1,134</td>
<td align="right">0.0%</td>
<td align="right">1,134</td>
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
<td align="right">41,160</td>
<td align="right">0.0%</td>
<td align="right">41,160</td>
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
<td align="right">100,611</td>
<td align="right">100.0%</td>
<td align="right">100,611</td>
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
<td align="right">2,121</td>
<td align="right">0.1%</td>
<td align="right">2,121</td>
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
<td align="right">3,578,417</td>
<td align="right">99.9%</td>
<td align="right">3,578,417</td>
<td align="right">99.9%</td>
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
<td align="right">2,121</td>
<td align="right">100.0%</td>
<td align="right">2,121</td>
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
<td align="right">6,815,697</td>
<td align="right">55.4%</td>
<td align="right">6,815,697</td>
<td align="right">55.4%</td>
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
<td align="right">5,476,359</td>
<td align="right">44.5%</td>
<td align="right">5,476,359</td>
<td align="right">44.5%</td>
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
<td align="right">9.2%</td>
<td align="right">903</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,925</td>
<td align="right">90.8%</td>
<td align="right">8,925</td>
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
<td align="left">list</td>
<td align="right">6,594</td>
<td align="right">73.9%</td>
<td align="right">6,594</td>
<td align="right">73.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,121</td>
<td align="right">23.8%</td>
<td align="right">2,121</td>
<td align="right">23.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">210</td>
<td align="right">2.4%</td>
<td align="right">210</td>
<td align="right">2.4%</td>
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
<td align="right">3,657,780</td>
<td align="right">8.1%</td>
<td align="right">3,657,780</td>
<td align="right">8.1%</td>
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
<td align="right">27,757,992</td>
<td align="right">61.5%</td>
<td align="right">27,757,992</td>
<td align="right">61.5%</td>
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
<td align="right">13,699,581</td>
<td align="right">30.3%</td>
<td align="right">13,699,581</td>
<td align="right">30.3%</td>
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
<td align="right">271,047</td>
<td align="right">94.3%</td>
<td align="right">271,047</td>
<td align="right">94.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">16,422</td>
<td align="right">5.7%</td>
<td align="right">16,422</td>
<td align="right">5.7%</td>
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
<td align="right">111,573</td>
<td align="right">679.4%</td>
<td align="right">107,499</td>
<td align="right">654.6%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">7,539</td>
<td align="right">45.9%</td>
<td align="right">7,539</td>
<td align="right">45.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">3,360</td>
<td align="right">20.5%</td>
<td align="right">3,360</td>
<td align="right">20.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">1,869</td>
<td align="right">11.4%</td>
<td align="right">1,869</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,092</td>
<td align="right">6.6%</td>
<td align="right">1,092</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">630</td>
<td align="right">3.8%</td>
<td align="right">630</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">609</td>
<td align="right">3.7%</td>
<td align="right">609</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">441</td>
<td align="right">2.7%</td>
<td align="right">441</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">210</td>
<td align="right">1.3%</td>
<td align="right">210</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">168</td>
<td align="right">1.0%</td>
<td align="right">168</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">42</td>
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
<td align="right">609</td>
<td align="right">100.0%</td>
<td align="right">609</td>
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
<td align="right">239,757</td>
<td align="right">6.2%</td>
<td align="right">239,757</td>
<td align="right">6.2%</td>
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
<td align="right">3,629,178</td>
<td align="right">93.7%</td>
<td align="right">3,629,178</td>
<td align="right">93.7%</td>
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
<td align="right">2,121</td>
<td align="right">52.6%</td>
<td align="right">2,121</td>
<td align="right">52.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,911</td>
<td align="right">47.4%</td>
<td align="right">1,911</td>
<td align="right">47.4%</td>
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
<td align="right">819</td>
<td align="right">42.9%</td>
<td align="right">819</td>
<td align="right">42.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">441</td>
<td align="right">23.1%</td>
<td align="right">441</td>
<td align="right">23.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">252</td>
<td align="right">13.2%</td>
<td align="right">252</td>
<td align="right">13.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">168</td>
<td align="right">8.8%</td>
<td align="right">168</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">126</td>
<td align="right">6.6%</td>
<td align="right">126</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">105</td>
<td align="right">5.5%</td>
<td align="right">105</td>
<td align="right">5.5%</td>
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
<td align="right">7,126,959</td>
<td align="right">6.8%</td>
<td align="right">6,177,234</td>
<td align="right">6.0%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">96,776,930</td>
<td align="right">92.3%</td>
<td align="right">96,239,957</td>
<td align="right">93.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">917,463</td>
<td align="right">0.9%</td>
<td align="right">917,454</td>
<td align="right">0.9%</td>
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
<td align="right">182,364</td>
<td align="right">91.6%</td>
<td align="right">164,451</td>
<td align="right">90.8%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">16,758</td>
<td align="right">8.4%</td>
<td align="right">16,758</td>
<td align="right">9.2%</td>
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
<td align="right">10,626</td>
<td align="right">63.4%</td>
<td align="right">10,626</td>
<td align="right">63.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,617</td>
<td align="right">9.6%</td>
<td align="right">1,617</td>
<td align="right">9.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,239</td>
<td align="right">7.4%</td>
<td align="right">1,239</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,113</td>
<td align="right">6.6%</td>
<td align="right">1,113</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">1,050</td>
<td align="right">6.3%</td>
<td align="right">1,050</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">756</td>
<td align="right">4.5%</td>
<td align="right">756</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">210</td>
<td align="right">1.3%</td>
<td align="right">210</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">147</td>
<td align="right">0.9%</td>
<td align="right">147</td>
<td align="right">0.9%</td>
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
<td align="right">25,422,204</td>
<td align="right">96.8%</td>
<td align="right">25,424,415</td>
<td align="right">96.8%</td>
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
<td align="right">839,874</td>
<td align="right">3.2%</td>
<td align="right">839,874</td>
<td align="right">3.2%</td>
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
<td align="right">4,410</td>
<td align="right">83.0%</td>
<td align="right">4,410</td>
<td align="right">83.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">903</td>
<td align="right">17.0%</td>
<td align="right">903</td>
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
<td align="left">sequence</td>
<td align="right">819</td>
<td align="right">90.7%</td>
<td align="right">819</td>
<td align="right">90.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">84</td>
<td align="right">9.3%</td>
<td align="right">84</td>
<td align="right">9.3%</td>
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
<td align="right">80,545,006</td>
<td align="right">3.6%</td>
<td align="right">77,255,192</td>
<td align="right">3.5%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,257,772,899</td>
<td align="right">56.6%</td>
<td align="right">1,248,571,434</td>
<td align="right">56.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">86,185,382</td>
<td align="right">3.9%</td>
<td align="right">85,675,669</td>
<td align="right">3.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">796,806,118</td>
<td align="right">35.9%</td>
<td align="right">792,562,350</td>
<td align="right">36.0%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">4,928,383</td>
<td align="right">6.3%</td>
<td align="right">4,706,224</td>
<td align="right">6.1%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,789,050</td>
<td align="right">4.9%</td>
<td align="right">3,708,050</td>
<td align="right">4.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,681,445</td>
<td align="right">7.3%</td>
<td align="right">5,598,033</td>
<td align="right">7.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">12,588,255</td>
<td align="right">16.2%</td>
<td align="right">12,546,948</td>
<td align="right">16.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,830,246</td>
<td align="right">6.2%</td>
<td align="right">4,817,007</td>
<td align="right">6.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">31,994,361</td>
<td align="right">41.1%</td>
<td align="right">31,977,876</td>
<td align="right">41.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">917,463</td>
<td align="right">1.2%</td>
<td align="right">917,454</td>
<td align="right">1.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,815,697</td>
<td align="right">8.8%</td>
<td align="right">6,815,697</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,657,780</td>
<td align="right">4.7%</td>
<td align="right">3,657,780</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">839,874</td>
<td align="right">1.1%</td>
<td align="right">839,874</td>
<td align="right">1.1%</td>
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
<td align="right">918,729</td>
<td align="right">1.1%</td>
<td align="right">731,745</td>
<td align="right">0.9%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,624,654</td>
<td align="right">11.9%</td>
<td align="right">8,183,004</td>
<td align="right">10.6%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">5,974,563</td>
<td align="right">7.4%</td>
<td align="right">5,211,822</td>
<td align="right">6.7%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">8,953,980</td>
<td align="right">11.1%</td>
<td align="right">8,093,211</td>
<td align="right">10.5%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,981,205</td>
<td align="right">11.2%</td>
<td align="right">8,931,330</td>
<td align="right">11.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,020,471</td>
<td align="right">2.5%</td>
<td align="right">2,028,262</td>
<td align="right">2.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">18,348,918</td>
<td align="right">22.8%</td>
<td align="right">18,348,918</td>
<td align="right">23.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,699,539</td>
<td align="right">17.0%</td>
<td align="right">13,699,539</td>
<td align="right">17.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">5,267,178</td>
<td align="right">6.5%</td>
<td align="right">5,267,178</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,664,899</td>
<td align="right">4.5%</td>
<td align="right">3,664,899</td>
<td align="right">4.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">561,607</td>
<td align="right">0.5%</td>
<td align="right">561,592</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">24,758,780</td>
<td align="right">19.9%</td>
<td align="right">24,758,765</td>
<td align="right">19.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">24,772,850</td>
<td align="right">19.9%</td>
<td align="right">24,772,835</td>
<td align="right">19.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">27,746,303</td>
<td align="right">22.3%</td>
<td align="right">27,746,288</td>
<td align="right">22.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">27,746,303</td>
<td align="right">22.3%</td>
<td align="right">27,746,288</td>
<td align="right">22.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">100,759,345</td>
<td align="right">81.0%</td>
<td align="right">100,759,315</td>
<td align="right">81.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">96,655,218</td>
<td align="right">77.7%</td>
<td align="right">96,655,203</td>
<td align="right">77.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">2,973,453</td>
<td align="right">2.4%</td>
<td align="right">2,973,453</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,675</td>
<td align="right">0.0%</td>
<td align="right">3,675</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">10,395</td>
<td align="right">0.0%</td>
<td align="right">10,395</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">682,689</td>
<td align="right">0.5%</td>
<td align="right">682,689</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">4,325,471</td>
<td align="right">3.5%</td>
<td align="right">4,325,471</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">1,449</td>
<td align="right">0.0%</td>
<td align="right">1,449</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">1,677,753</td>
<td align="right">1.3%</td>
<td align="right">1,677,753</td>
<td align="right">1.3%</td>
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
<td align="right">2,883,063</td>
<td align="right"></td>
<td align="right">3,036,135</td>
<td align="right"></td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,468,122</td>
<td align="right"></td>
<td align="right">3,619,790</td>
<td align="right"></td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">693,857,497</td>
<td align="right">44.4%</td>
<td align="right">687,404,991</td>
<td align="right">44.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">496,554,148</td>
<td align="right">31.8%</td>
<td align="right">500,763,026</td>
<td align="right">32.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">554,032,049</td>
<td align="right">35.5%</td>
<td align="right">549,926,335</td>
<td align="right">35.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">518,267,957</td>
<td align="right">33.2%</td>
<td align="right">520,129,085</td>
<td align="right">33.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">489,153</td>
<td align="right">0.3%</td>
<td align="right">490,161</td>
<td align="right">0.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">613,393</td>
<td align="right"></td>
<td align="right">612,315</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">35,694,637</td>
<td align="right">2.3%</td>
<td align="right">35,641,393</td>
<td align="right">2.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">335,681,062</td>
<td align="right">21.5%</td>
<td align="right">336,058,025</td>
<td align="right">21.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">419,080,665</td>
<td align="right">26.8%</td>
<td align="right">419,365,012</td>
<td align="right">26.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">69,635,385</td>
<td align="right">4.5%</td>
<td align="right">69,595,302</td>
<td align="right">4.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">227,094</td>
<td align="right">0.1%</td>
<td align="right">227,199</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">54,906,045</td>
<td align="right"></td>
<td align="right">54,921,037</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">112,889,807</td>
<td align="right"></td>
<td align="right">112,878,096</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">86,975,847</td>
<td align="right"></td>
<td align="right">86,980,259</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">99,119,847</td>
<td align="right">56.9%</td>
<td align="right">99,123,161</td>
<td align="right">56.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">98,403,600</td>
<td align="right">56.5%</td>
<td align="right">98,405,801</td>
<td align="right">56.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">75,004,552</td>
<td align="right">43.1%</td>
<td align="right">75,004,777</td>
<td align="right">43.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">75,045,042</td>
<td align="right"></td>
<td align="right">75,045,267</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,978,070</td>
<td align="right"></td>
<td align="right">3,978,070</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">366,114</td>
<td align="right">9.2%</td>
<td align="right">366,114</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">37,632</td>
<td align="right">0.9%</td>
<td align="right">37,632</td>
<td align="right">0.9%</td>
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
<td align="right">4,872</td>
<td align="right">65,289</td>
<td align="right">154,165,480</td>
<td align="right">19,090,094</td>
<td align="right">7,314,923</td>
<td align="right">4,872</td>
<td align="right">65,289</td>
<td align="right">154,164,327</td>
<td align="right">19,089,946</td>
<td align="right">7,316,128</td>
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
<td align="right">42</td>
<td align="right">0.7%</td>
<td align="right">231</td>
<td align="right">2.2%</td>
<td align="right">450.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">21</td>
<td align="right">1.4%</td>
<td align="right">84</td>
<td align="right">3.1%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">336</td>
<td align="right">5.2%</td>
<td align="right">945</td>
<td align="right">8.8%</td>
<td align="right">181.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,008</td>
<td align="right">15.7%</td>
<td align="right">2,646</td>
<td align="right">24.8%</td>
<td align="right">162.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,449</td>
<td align="right">22.6%</td>
<td align="right">2,667</td>
<td align="right">25.0%</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">6,405</td>
<td align="right"></td>
<td align="right">10,689</td>
<td align="right"></td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">24,926,433</td>
<td align="right"></td>
<td align="right">36,152,340</td>
<td align="right"></td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">3,612</td>
<td align="right">56.4%</td>
<td align="right">4,431</td>
<td align="right">41.5%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">842,112,789</td>
<td align="right">3,378.4%</td>
<td align="right">922,981,311</td>
<td align="right">2,553.0%</td>
<td align="right">9.6%</td>
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
<td align="right">1,386</td>
<td align="right">95.7%</td>
<td align="right">2,604</td>
<td align="right">97.6%</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,449</td>
<td align="right"></td>
<td align="right">2,667</td>
<td align="right"></td>
<td align="right">84.1%</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">86,016</td>
<td align="right">0.6%</td>
<td align="right">172,032</td>
<td align="right">0.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">308,616</td>
<td align="right">2.2%</td>
<td align="right">545,160</td>
<td align="right">2.2%</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">10,774,680</td>
<td align="right">75.9%</td>
<td align="right">18,539,367</td>
<td align="right">76.2%</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">14,192,640</td>
<td align="right"></td>
<td align="right">24,342,528</td>
<td align="right"></td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">3,109,344</td>
<td align="right">21.9%</td>
<td align="right">5,258,001</td>
<td align="right">21.6%</td>
<td align="right">69.1%</td>
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
<td align="left">273</td>
<td align="right">19.7%</td>
<td align="left">777</td>
<td align="right">29.8%</td>
<td align="right">184.6%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">693</td>
<td align="right">50.0%</td>
<td align="left">1,134</td>
<td align="right">43.5%</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">294</td>
<td align="right">21.2%</td>
<td align="left">462</td>
<td align="right">17.7%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">105</td>
<td align="right">7.6%</td>
<td align="left">210</td>
<td align="right">8.1%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">21</td>
<td align="right">1.5%</td>
<td align="left">21</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
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
<td align="right">21</td>
<td align="right">1.4%</td>
<td align="right">84</td>
<td align="right">3.1%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">84</td>
<td align="right">5.8%</td>
<td align="right">147</td>
<td align="right">5.5%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">378</td>
<td align="right">26.1%</td>
<td align="right">672</td>
<td align="right">25.2%</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">546</td>
<td align="right">37.7%</td>
<td align="right">1,029</td>
<td align="right">38.6%</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">294</td>
<td align="right">20.3%</td>
<td align="right">567</td>
<td align="right">21.3%</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">105</td>
<td align="right">7.2%</td>
<td align="right">147</td>
<td align="right">5.5%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">21</td>
<td align="right">1.4%</td>
<td align="right">21</td>
<td align="right">0.8%</td>
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
<td align="left"><= 8</td>
<td align="right">42</td>
<td align="right">2.9%</td>
<td align="right">105</td>
<td align="right">3.9%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">168</td>
<td align="right">11.6%</td>
<td align="right">546</td>
<td align="right">20.5%</td>
<td align="right">225.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">651</td>
<td align="right">44.9%</td>
<td align="right">966</td>
<td align="right">36.2%</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">336</td>
<td align="right">23.2%</td>
<td align="right">630</td>
<td align="right">23.6%</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">147</td>
<td align="right">10.1%</td>
<td align="right">273</td>
<td align="right">10.2%</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">42</td>
<td align="right">2.9%</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">63</td>
<td align="right">2.4%</td>
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
<td align="left">_GET_ITER</td>
<td align="right">5,229</td>
<td align="right">94,185</td>
<td align="right">1,701.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">12,810</td>
<td align="right">61,530</td>
<td align="right">380.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">119,154</td>
<td align="right">497,112</td>
<td align="right">317.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">14,238</td>
<td align="right">58,632</td>
<td align="right">311.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">14,238</td>
<td align="right">57,750</td>
<td align="right">305.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">16,002</td>
<td align="right">57,582</td>
<td align="right">259.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">668,661</td>
<td align="right">2,236,500</td>
<td align="right">234.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">19,866</td>
<td align="right">64,218</td>
<td align="right">223.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">19,866</td>
<td align="right">64,218</td>
<td align="right">223.3%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">19,866</td>
<td align="right">64,218</td>
<td align="right">223.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">19,866</td>
<td align="right">64,218</td>
<td align="right">223.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">19,866</td>
<td align="right">64,218</td>
<td align="right">223.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">754,005</td>
<td align="right">2,214,828</td>
<td align="right">193.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">139,608</td>
<td align="right">348,558</td>
<td align="right">149.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,071,504</td>
<td align="right">2,560,530</td>
<td align="right">139.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">383,124</td>
<td align="right">849,597</td>
<td align="right">121.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,037,063</td>
<td align="right">4,502,064</td>
<td align="right">121.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">418,026</td>
<td align="right">892,668</td>
<td align="right">113.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">61,110</td>
<td align="right">15,183</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">61,110</td>
<td align="right">15,183</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">10,164</td>
<td align="right">17,241</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">69,930</td>
<td align="right">23,877</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">20,307</td>
<td align="right">33,537</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,759,023</td>
<td align="right">2,867,088</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">758,205</td>
<td align="right">1,134,273</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,038,050</td>
<td align="right">3,028,158</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">24,926,433</td>
<td align="right">36,152,340</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">24,168,228</td>
<td align="right">35,018,067</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,356,516</td>
<td align="right">855,708</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">12,762,624</td>
<td align="right">17,334,555</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,227,658</td>
<td align="right">4,353,237</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">576,576</td>
<td align="right">776,601</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,012,661</td>
<td align="right">2,553,033</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">42,968,478</td>
<td align="right">54,064,962</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">383,376</td>
<td align="right">482,097</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">194,481</td>
<td align="right">243,495</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">126,378</td>
<td align="right">94,878</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">126,378</td>
<td align="right">94,878</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">238,014</td>
<td align="right">287,343</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">277,683</td>
<td align="right">326,718</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">277,683</td>
<td align="right">326,718</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">391,608</td>
<td align="right">458,010</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5,628</td>
<td align="right">6,468</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">5,628</td>
<td align="right">6,468</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">5,628</td>
<td align="right">6,468</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">5,628</td>
<td align="right">6,468</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">5,628</td>
<td align="right">6,468</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">979,965</td>
<td align="right">855,708</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,429,721</td>
<td align="right">2,693,985</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,116,003</td>
<td align="right">1,236,018</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,592,889</td>
<td align="right">5,058,396</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">24,090,087</td>
<td align="right">26,502,840</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">160,916,259</td>
<td align="right">176,901,648</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">85,029</td>
<td align="right">92,799</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">923,202</td>
<td align="right">1,006,425</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,695,540</td>
<td align="right">1,840,188</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,067,304</td>
<td align="right">1,150,716</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">588,483</td>
<td align="right">633,507</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">553,014</td>
<td align="right">593,019</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,137,864</td>
<td align="right">1,217,874</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,033</td>
<td align="right">12,873</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">252,756</td>
<td align="right">270,207</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,076,145</td>
<td align="right">1,149,834</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">584,850</td>
<td align="right">624,855</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">729,246</td>
<td align="right">778,596</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">1,501,122</td>
<td align="right">1,598,289</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">625,674</td>
<td align="right">665,679</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">689,346</td>
<td align="right">729,351</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">697,620</td>
<td align="right">737,625</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">24,409,497</td>
<td align="right">25,706,184</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">1,527,036</td>
<td align="right">1,604,799</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,187,445</td>
<td align="right">1,247,547</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">805,770</td>
<td align="right">845,775</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,853,649</td>
<td align="right">1,944,642</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">1,302</td>
<td align="right">1,365</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">368,361</td>
<td align="right">385,812</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">136,247,076</td>
<td align="right">142,150,449</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">2,834,391</td>
<td align="right">2,948,484</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,679,349</td>
<td align="right">1,737,603</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,628,760</td>
<td align="right">1,681,995</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">18,504,717</td>
<td align="right">19,101,999</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,424,850</td>
<td align="right">1,470,084</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">1,499,190</td>
<td align="right">1,544,214</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">21,005,628</td>
<td align="right">21,610,512</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">19,277,055</td>
<td align="right">19,754,112</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,174,509</td>
<td align="right">1,199,142</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">38,094,903</td>
<td align="right">38,542,098</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">18,042,045</td>
<td align="right">17,912,622</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">21,682,542</td>
<td align="right">21,542,745</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">21,682,542</td>
<td align="right">21,542,745</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,020,411</td>
<td align="right">1,014,489</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">20,486,949</td>
<td align="right">20,388,774</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">19,471,410</td>
<td align="right">19,551,420</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">19,471,410</td>
<td align="right">19,551,420</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">19,001,514</td>
<td align="right">19,075,371</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">43,305,696</td>
<td align="right">43,358,973</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">16,135,875</td>
<td align="right">16,137,093</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">19,067,181</td>
<td align="right">19,068,042</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">16,344,636</td>
<td align="right">16,344,699</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">754,005</td>
<td align="right">754,005</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">382,725</td>
<td align="right">382,725</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">171,339</td>
<td align="right">171,339</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">168,861</td>
<td align="right">168,861</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">106,302</td>
<td align="right">106,302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">78,624</td>
<td align="right">78,624</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">63,672</td>
<td align="right">63,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">33,642</td>
<td align="right">33,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">31,836</td>
<td align="right">31,836</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">31,836</td>
<td align="right">31,836</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">31,836</td>
<td align="right">31,836</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">31,836</td>
<td align="right">31,836</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">29,316</td>
<td align="right">29,316</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">29,316</td>
<td align="right">29,316</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">6,405</td>
<td align="right">6,405</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">4,788</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,793</td>
<td align="right">2,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right"></td>
<td align="right">91,791</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right"></td>
<td align="right">91,119</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right"></td>
<td align="right">50,379</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">40,005</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right"></td>
<td align="right">23,562</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right"></td>
<td align="right">17,451</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">11,781</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">7,770</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right"></td>
<td align="right">7,770</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right"></td>
<td align="right">7,770</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right"></td>
<td align="right">7,770</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">7,224</td>
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
<td align="right">336</td>
<td align="right">945</td>
<td align="right">181.2%</td>
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
<td align="right">252</td>
<td align="right">252</td>
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
<td align="right">252</td>
<td align="right">252</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">21</td>
<td align="right">21</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-01
