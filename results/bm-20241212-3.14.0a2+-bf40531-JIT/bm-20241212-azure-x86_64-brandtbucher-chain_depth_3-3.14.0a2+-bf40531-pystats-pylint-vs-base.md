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
<td align="left">CALL_TUPLE_1</td>
<td align="right">86,119</td>
<td align="right">194,210</td>
<td align="right">125.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">2,225,769</td>
<td align="right">2,811,512</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">69,578</td>
<td align="right">85,427</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">420,797</td>
<td align="right">356,883</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">714,080</td>
<td align="right">650,166</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">12,406,225</td>
<td align="right">11,355,602</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,671,181</td>
<td align="right">2,836,543</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">11,257,194</td>
<td align="right">11,810,810</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,123,028</td>
<td align="right">1,073,838</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,680,657</td>
<td align="right">3,533,086</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,015,951</td>
<td align="right">1,939,629</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,122,766</td>
<td align="right">3,980,045</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">6,889,781</td>
<td align="right">7,108,237</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,034,235</td>
<td align="right">1,065,933</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">51,911,513</td>
<td align="right">53,203,919</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,838,591</td>
<td align="right">3,755,037</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,761,831</td>
<td align="right">3,682,180</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,240,839</td>
<td align="right">2,193,921</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">17,153,369</td>
<td align="right">17,491,504</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">27,013,124</td>
<td align="right">26,509,772</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">15,027,742</td>
<td align="right">14,749,520</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,969,303</td>
<td align="right">2,920,113</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">38,411,365</td>
<td align="right">39,037,333</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">14,825,838</td>
<td align="right">14,584,639</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">7,677,373</td>
<td align="right">7,562,485</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">3,042,164</td>
<td align="right">3,002,208</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,394,711</td>
<td align="right">2,363,704</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,453,516</td>
<td align="right">6,375,986</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">45,328,572</td>
<td align="right">45,841,159</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,992,462</td>
<td align="right">4,036,924</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,004,538</td>
<td align="right">1,982,563</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,713,248</td>
<td align="right">5,772,789</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">29,491,097</td>
<td align="right">29,212,460</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,507,125</td>
<td align="right">3,538,832</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,895,854</td>
<td align="right">4,853,969</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,555,136</td>
<td align="right">3,524,770</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">42,939,069</td>
<td align="right">42,578,396</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,717,707</td>
<td align="right">6,771,947</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">7,934,866</td>
<td align="right">7,997,890</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,775,641</td>
<td align="right">9,699,408</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,188,596</td>
<td align="right">2,171,588</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">25,419,920</td>
<td align="right">25,233,091</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">26,712,343</td>
<td align="right">26,522,988</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,559,014</td>
<td align="right">4,528,648</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,843,602</td>
<td align="right">8,891,167</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,466,397</td>
<td align="right">2,477,986</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,010,141</td>
<td align="right">4,027,544</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">29,365,154</td>
<td align="right">29,482,653</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">29,623,012</td>
<td align="right">29,507,119</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">987,182</td>
<td align="right">983,397</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42,351,479</td>
<td align="right">42,499,705</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,931,395</td>
<td align="right">1,927,672</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">9,479,266</td>
<td align="right">9,496,306</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,501,914</td>
<td align="right">2,497,510</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">16,566,235</td>
<td align="right">16,584,867</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">173,127,995</td>
<td align="right">172,934,349</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">31,389,859</td>
<td align="right">31,360,226</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,607,809</td>
<td align="right">5,611,913</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,502,920</td>
<td align="right">4,500,463</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,985,116</td>
<td align="right">1,984,104</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,993,679</td>
<td align="right">1,992,683</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,332,352</td>
<td align="right">9,327,958</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">15,363,878</td>
<td align="right">15,370,915</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,695,466</td>
<td align="right">6,698,215</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,131,022</td>
<td align="right">1,131,332</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">50,226</td>
<td align="right">50,235</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,562,908</td>
<td align="right">1,562,635</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">4,697,000</td>
<td align="right">4,697,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">916,476</td>
<td align="right">916,364</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,583,509</td>
<td align="right">11,582,195</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,613,976</td>
<td align="right">2,613,934</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,575,146</td>
<td align="right">2,575,178</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">959,393</td>
<td align="right">959,402</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">46,187,485</td>
<td align="right">46,187,212</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,909,979</td>
<td align="right">8,910,011</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9,612,652</td>
<td align="right">9,612,642</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">11,705,171</td>
<td align="right">11,705,171</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,220,127</td>
<td align="right">11,220,127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">10,019,530</td>
<td align="right">10,019,530</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,152,860</td>
<td align="right">8,152,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">8,096,363</td>
<td align="right">8,096,363</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">7,099,887</td>
<td align="right">7,099,887</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,493,719</td>
<td align="right">6,493,719</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,643,637</td>
<td align="right">5,643,637</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">5,334,244</td>
<td align="right">5,334,244</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,673,341</td>
<td align="right">4,673,341</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">4,314,479</td>
<td align="right">4,314,479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,856,172</td>
<td align="right">2,856,172</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,649,454</td>
<td align="right">2,649,454</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,943,825</td>
<td align="right">1,943,825</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,806,037</td>
<td align="right">1,806,037</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,798,448</td>
<td align="right">1,798,448</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,746,732</td>
<td align="right">1,746,732</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,705,703</td>
<td align="right">1,705,703</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,640,793</td>
<td align="right">1,640,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,623,476</td>
<td align="right">1,623,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,548,261</td>
<td align="right">1,548,261</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,499,255</td>
<td align="right">1,499,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,424,440</td>
<td align="right">1,424,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,221,836</td>
<td align="right">1,221,836</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,149,140</td>
<td align="right">1,149,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,045,207</td>
<td align="right">1,045,207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">998,490</td>
<td align="right">998,490</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">974,050</td>
<td align="right">974,050</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">849,921</td>
<td align="right">849,921</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">822,988</td>
<td align="right">822,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">735,098</td>
<td align="right">735,098</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">703,475</td>
<td align="right">703,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">690,199</td>
<td align="right">690,199</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">667,298</td>
<td align="right">667,298</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">663,236</td>
<td align="right">663,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">657,616</td>
<td align="right">657,616</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">615,293</td>
<td align="right">615,293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">615,293</td>
<td align="right">615,293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">582,464</td>
<td align="right">582,464</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">581,571</td>
<td align="right">581,571</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">579,568</td>
<td align="right">579,568</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">555,773</td>
<td align="right">555,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">514,769</td>
<td align="right">514,769</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">465,880</td>
<td align="right">465,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">446,275</td>
<td align="right">446,275</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">438,777</td>
<td align="right">438,777</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">353,669</td>
<td align="right">353,669</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">307,447</td>
<td align="right">307,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">296,815</td>
<td align="right">296,815</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">281,324</td>
<td align="right">281,324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">280,898</td>
<td align="right">280,898</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">266,985</td>
<td align="right">266,985</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">258,617</td>
<td align="right">258,617</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">253,967</td>
<td align="right">253,967</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">225,565</td>
<td align="right">225,565</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">165,604</td>
<td align="right">165,604</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">163,174</td>
<td align="right">163,174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">136,378</td>
<td align="right">136,378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">127,250</td>
<td align="right">127,250</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">122,558</td>
<td align="right">122,558</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">108,792</td>
<td align="right">108,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,224</td>
<td align="right">98,224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">84,680</td>
<td align="right">84,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">84,374</td>
<td align="right">84,374</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">82,706</td>
<td align="right">82,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">76,258</td>
<td align="right">76,258</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,426</td>
<td align="right">72,426</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">63,916</td>
<td align="right">63,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,672</td>
<td align="right">56,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">55,564</td>
<td align="right">55,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">43,007</td>
<td align="right">43,007</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">42,343</td>
<td align="right">42,343</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">31,479</td>
<td align="right">31,479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">23,352</td>
<td align="right">23,352</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">19,679</td>
<td align="right">19,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">19,071</td>
<td align="right">19,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">10,977</td>
<td align="right">10,977</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,655</td>
<td align="right">5,655</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">5,547</td>
<td align="right">5,547</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,039</td>
<td align="right">3,039</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,949</td>
<td align="right">2,949</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,428</td>
<td align="right">2,428</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,305</td>
<td align="right">1,305</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,133</td>
<td align="right">1,133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,081</td>
<td align="right">1,081</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">954</td>
<td align="right">954</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">893</td>
<td align="right">893</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">777</td>
<td align="right">777</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">723</td>
<td align="right">723</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">589</td>
<td align="right">589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">235</td>
<td align="right">235</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">214</td>
<td align="right">214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">33</td>
<td align="right">33</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">25</td>
<td align="right">25</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">18</td>
<td align="right">18</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">15</td>
<td align="right">15</td>
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
<td align="right">732,280</td>
<td align="right">10.8%</td>
<td align="right">732,280</td>
<td align="right">10.8%</td>
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
<td align="right">6,066,088</td>
<td align="right">89.2%</td>
<td align="right">6,066,088</td>
<td align="right">89.2%</td>
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
<td align="right">480</td>
<td align="right">17.0%</td>
<td align="right">480</td>
<td align="right">17.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,338</td>
<td align="right">83.0%</td>
<td align="right">2,338</td>
<td align="right">83.0%</td>
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
<td align="left">add other</td>
<td align="right">998</td>
<td align="right">42.7%</td>
<td align="right">998</td>
<td align="right">42.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">232</td>
<td align="right">9.9%</td>
<td align="right">232</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">210</td>
<td align="right">9.0%</td>
<td align="right">210</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">173</td>
<td align="right">7.4%</td>
<td align="right">173</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">160</td>
<td align="right">6.8%</td>
<td align="right">160</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">156</td>
<td align="right">6.7%</td>
<td align="right">156</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">148</td>
<td align="right">6.3%</td>
<td align="right">148</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">120</td>
<td align="right">5.1%</td>
<td align="right">120</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">2.8%</td>
<td align="right">66</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">36</td>
<td align="right">1.5%</td>
<td align="right">36</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">21</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">10</td>
<td align="right">0.4%</td>
<td align="right">10</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">446,275</td>
<td align="right">100.0%</td>
<td align="right">446,275</td>
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
<td align="right">2,008,649</td>
<td align="right">14.6%</td>
<td align="right">1,932,350</td>
<td align="right">14.2%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,644,779</td>
<td align="right">84.9%</td>
<td align="right">11,644,797</td>
<td align="right">85.3%</td>
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
<td align="right">62,806</td>
<td align="right">0.5%</td>
<td align="right">62,806</td>
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
<td align="right">5,876</td>
<td align="right">69.3%</td>
<td align="right">5,853</td>
<td align="right">69.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,599</td>
<td align="right">30.7%</td>
<td align="right">2,599</td>
<td align="right">30.8%</td>
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
<td align="right">802</td>
<td align="right">13.6%</td>
<td align="right">779</td>
<td align="right">13.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,690</td>
<td align="right">45.8%</td>
<td align="right">2,690</td>
<td align="right">46.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">845</td>
<td align="right">14.4%</td>
<td align="right">845</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">782</td>
<td align="right">13.3%</td>
<td align="right">782</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">690</td>
<td align="right">11.7%</td>
<td align="right">690</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">32</td>
<td align="right">0.5%</td>
<td align="right">32</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">13</td>
<td align="right">0.2%</td>
<td align="right">13</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
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
<td align="right">7,813,333</td>
<td align="right">11.5%</td>
<td align="right">7,787,394</td>
<td align="right">11.4%</td>
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
<td align="right">60,154,368</td>
<td align="right">88.2%</td>
<td align="right">60,192,137</td>
<td align="right">88.2%</td>
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
<td align="right">246,709</td>
<td align="right">0.4%</td>
<td align="right">246,709</td>
<td align="right">0.4%</td>
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
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">8,513</td>
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
<td align="right">179,687</td>
<td align="right">99.8%</td>
<td align="right">179,222</td>
<td align="right">99.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">308</td>
<td align="right">0.2%</td>
<td align="right">308</td>
<td align="right">0.2%</td>
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
<td align="left">out of versions</td>
<td align="right">308</td>
<td align="right">100.0%</td>
<td align="right">308</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">308</td>
<td align="right">100.0%</td>
<td align="right">308</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">62</td>
<td align="right">20.1%</td>
<td align="right">62</td>
<td align="right">20.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">21</td>
<td align="right">6.8%</td>
<td align="right">21</td>
<td align="right">6.8%</td>
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
<td align="right">568</td>
<td align="right">0.1%</td>
<td align="right">568</td>
<td align="right">0.1%</td>
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
<td align="right">573,498</td>
<td align="right">99.6%</td>
<td align="right">573,498</td>
<td align="right">99.6%</td>
<td align="right">0.0%</td>
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
<td align="right">1,030,181</td>
<td align="right">5.6%</td>
<td align="right">1,061,879</td>
<td align="right">5.8%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,217,365</td>
<td align="right">94.3%</td>
<td align="right">17,217,374</td>
<td align="right">94.2%</td>
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
<td align="right">3,370</td>
<td align="right">0.0%</td>
<td align="right">3,370</td>
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
<td align="right">1,538</td>
<td align="right">37.3%</td>
<td align="right">1,538</td>
<td align="right">37.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,583</td>
<td align="right">62.7%</td>
<td align="right">2,583</td>
<td align="right">62.7%</td>
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
<td align="left">different types</td>
<td align="right">1,109</td>
<td align="right">42.9%</td>
<td align="right">1,109</td>
<td align="right">42.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">657</td>
<td align="right">25.4%</td>
<td align="right">657</td>
<td align="right">25.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">244</td>
<td align="right">9.4%</td>
<td align="right">244</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">212</td>
<td align="right">8.2%</td>
<td align="right">212</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">155</td>
<td align="right">6.0%</td>
<td align="right">155</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">90</td>
<td align="right">3.5%</td>
<td align="right">90</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">51</td>
<td align="right">2.0%</td>
<td align="right">51</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">2,494,967</td>
<td align="right">37.6%</td>
<td align="right">2,490,564</td>
<td align="right">37.6%</td>
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
<td align="right">4,103,534</td>
<td align="right">61.9%</td>
<td align="right">4,103,534</td>
<td align="right">61.9%</td>
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
<td align="right">26,561</td>
<td align="right">0.4%</td>
<td align="right">26,561</td>
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
<td align="right">6,232</td>
<td align="right">83.6%</td>
<td align="right">6,231</td>
<td align="right">83.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,226</td>
<td align="right">16.4%</td>
<td align="right">1,226</td>
<td align="right">16.4%</td>
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
<td align="right">3,249</td>
<td align="right">52.1%</td>
<td align="right">3,248</td>
<td align="right">52.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,241</td>
<td align="right">19.9%</td>
<td align="right">1,241</td>
<td align="right">19.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,213</td>
<td align="right">19.5%</td>
<td align="right">1,213</td>
<td align="right">19.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">529</td>
<td align="right">8.5%</td>
<td align="right">529</td>
<td align="right">8.5%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">227,535</td>
<td align="right">0.8%</td>
<td align="right">224,728</td>
<td align="right">0.8%</td>
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
<td align="right">3,982,691</td>
<td align="right">14.6%</td>
<td align="right">4,027,154</td>
<td align="right">14.7%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,055,344</td>
<td align="right">84.5%</td>
<td align="right">23,058,064</td>
<td align="right">84.4%</td>
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
<td align="right">5,431</td>
<td align="right">38.6%</td>
<td align="right">5,368</td>
<td align="right">38.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,638</td>
<td align="right">61.4%</td>
<td align="right">8,637</td>
<td align="right">61.7%</td>
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
<td align="right">4,244</td>
<td align="right">49.1%</td>
<td align="right">4,243</td>
<td align="right">49.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,408</td>
<td align="right">16.3%</td>
<td align="right">1,408</td>
<td align="right">16.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,189</td>
<td align="right">13.8%</td>
<td align="right">1,189</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">604</td>
<td align="right">7.0%</td>
<td align="right">604</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">306</td>
<td align="right">3.5%</td>
<td align="right">306</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">276</td>
<td align="right">3.2%</td>
<td align="right">276</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">253</td>
<td align="right">2.9%</td>
<td align="right">253</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">97</td>
<td align="right">1.1%</td>
<td align="right">97</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">44</td>
<td align="right">0.5%</td>
<td align="right">44</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">17</td>
<td align="right">0.2%</td>
<td align="right">17</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">7</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">81,484,608</td>
<td align="right">65.3%</td>
<td align="right">81,187,300</td>
<td align="right">65.2%</td>
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
<td align="right">33,615,521</td>
<td align="right">27.0%</td>
<td align="right">33,714,486</td>
<td align="right">27.1%</td>
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
<td align="right">9,532,457</td>
<td align="right">7.6%</td>
<td align="right">9,532,447</td>
<td align="right">7.7%</td>
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
<td align="right">207,304</td>
<td align="right">0.2%</td>
<td align="right">207,304</td>
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
<td align="right">693,832</td>
<td align="right">97.7%</td>
<td align="right">695,736</td>
<td align="right">97.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">16,283</td>
<td align="right">2.3%</td>
<td align="right">16,283</td>
<td align="right">2.3%</td>
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
<td align="right">5,331</td>
<td align="right">32.7%</td>
<td align="right">5,331</td>
<td align="right">32.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,652</td>
<td align="right">22.4%</td>
<td align="right">3,652</td>
<td align="right">22.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,573</td>
<td align="right">9.7%</td>
<td align="right">1,573</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,339</td>
<td align="right">8.2%</td>
<td align="right">1,339</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">989</td>
<td align="right">6.1%</td>
<td align="right">989</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">836</td>
<td align="right">5.1%</td>
<td align="right">836</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">392</td>
<td align="right">2.4%</td>
<td align="right">392</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">318</td>
<td align="right">2.0%</td>
<td align="right">318</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">1.4%</td>
<td align="right">235</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">204</td>
<td align="right">1.3%</td>
<td align="right">204</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">102</td>
<td align="right">0.6%</td>
<td align="right">102</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">64</td>
<td align="right">0.4%</td>
<td align="right">64</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">56,368,516</td>
<td align="right">99.9%</td>
<td align="right">55,982,663</td>
<td align="right">99.9%</td>
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
<td align="right">5,290</td>
<td align="right">0.0%</td>
<td align="right">5,290</td>
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
<td align="right">550</td>
<td align="right">0.0%</td>
<td align="right">550</td>
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
<td align="right">9,762</td>
<td align="right">0.0%</td>
<td align="right">9,762</td>
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
<td align="right">18,197</td>
<td align="right">100.0%</td>
<td align="right">18,197</td>
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
<td align="right">138</td>
<td align="right">0.0%</td>
<td align="right">138</td>
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
<td align="right">721,377</td>
<td align="right">99.9%</td>
<td align="right">721,377</td>
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
<td align="right">451</td>
<td align="right">100.0%</td>
<td align="right">451</td>
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
<td align="right">6,490,754</td>
<td align="right">54.9%</td>
<td align="right">6,490,754</td>
<td align="right">54.9%</td>
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
<td align="right">5,334,244</td>
<td align="right">45.1%</td>
<td align="right">5,334,244</td>
<td align="right">45.1%</td>
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
<td align="right">104</td>
<td align="right">3.5%</td>
<td align="right">104</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,861</td>
<td align="right">96.5%</td>
<td align="right">2,861</td>
<td align="right">96.5%</td>
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
<td align="right">2,058</td>
<td align="right">71.9%</td>
<td align="right">2,058</td>
<td align="right">71.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">51</td>
<td align="right">1.8%</td>
<td align="right">51</td>
<td align="right">1.8%</td>
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
<td align="right">1,214,555</td>
<td align="right">8.7%</td>
<td align="right">1,214,555</td>
<td align="right">8.7%</td>
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
<td align="right">10,785,358</td>
<td align="right">77.1%</td>
<td align="right">10,785,358</td>
<td align="right">77.1%</td>
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
<td align="right">1,977,237</td>
<td align="right">14.1%</td>
<td align="right">1,977,237</td>
<td align="right">14.1%</td>
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
<td align="right">41,804</td>
<td align="right">94.0%</td>
<td align="right">41,804</td>
<td align="right">94.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,659</td>
<td align="right">6.0%</td>
<td align="right">2,659</td>
<td align="right">6.0%</td>
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
<td align="left">not managed dict</td>
<td align="right">1,397</td>
<td align="right">52.5%</td>
<td align="right">1,397</td>
<td align="right">52.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">440</td>
<td align="right">16.5%</td>
<td align="right">440</td>
<td align="right">16.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">284</td>
<td align="right">10.7%</td>
<td align="right">284</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">230</td>
<td align="right">8.6%</td>
<td align="right">230</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">129</td>
<td align="right">4.9%</td>
<td align="right">129</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">107</td>
<td align="right">4.0%</td>
<td align="right">107</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">39</td>
<td align="right">1.5%</td>
<td align="right">39</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">8</td>
<td align="right">0.3%</td>
<td align="right">8</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">25</td>
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
<td align="right">83,907</td>
<td align="right">3.1%</td>
<td align="right">83,907</td>
<td align="right">3.1%</td>
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
<td align="right">2,586,148</td>
<td align="right">96.8%</td>
<td align="right">2,586,148</td>
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
<td align="right">343</td>
<td align="right">44.4%</td>
<td align="right">343</td>
<td align="right">44.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">430</td>
<td align="right">55.6%</td>
<td align="right">430</td>
<td align="right">55.6%</td>
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
<td align="right">240</td>
<td align="right">55.8%</td>
<td align="right">240</td>
<td align="right">55.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">92</td>
<td align="right">21.4%</td>
<td align="right">92</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">47</td>
<td align="right">10.9%</td>
<td align="right">47</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">25</td>
<td align="right">5.8%</td>
<td align="right">25</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">18</td>
<td align="right">4.2%</td>
<td align="right">18</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">8</td>
<td align="right">1.9%</td>
<td align="right">8</td>
<td align="right">1.9%</td>
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
<td align="right">3,097,804</td>
<td align="right">7.3%</td>
<td align="right">3,013,123</td>
<td align="right">7.1%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">39,030,141</td>
<td align="right">91.4%</td>
<td align="right">39,018,118</td>
<td align="right">91.6%</td>
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
<td align="right">565,572</td>
<td align="right">1.3%</td>
<td align="right">565,572</td>
<td align="right">1.3%</td>
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
<td align="right">65,474</td>
<td align="right">88.4%</td>
<td align="right">63,874</td>
<td align="right">88.1%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,596</td>
<td align="right">11.6%</td>
<td align="right">8,596</td>
<td align="right">11.9%</td>
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
<td align="right">5,830</td>
<td align="right">67.8%</td>
<td align="right">5,830</td>
<td align="right">67.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">804</td>
<td align="right">9.4%</td>
<td align="right">804</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">665</td>
<td align="right">7.7%</td>
<td align="right">665</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">564</td>
<td align="right">6.6%</td>
<td align="right">564</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">345</td>
<td align="right">4.0%</td>
<td align="right">345</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">317</td>
<td align="right">3.7%</td>
<td align="right">317</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">50</td>
<td align="right">0.6%</td>
<td align="right">50</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">21</td>
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
<td align="right">7,969,895</td>
<td align="right">90.4%</td>
<td align="right">7,965,501</td>
<td align="right">90.4%</td>
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
<td align="right">848,870</td>
<td align="right">9.6%</td>
<td align="right">848,870</td>
<td align="right">9.6%</td>
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
<td align="right">805</td>
<td align="right">76.6%</td>
<td align="right">805</td>
<td align="right">76.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">246</td>
<td align="right">23.4%</td>
<td align="right">246</td>
<td align="right">23.4%</td>
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
<td align="right">222</td>
<td align="right">90.2%</td>
<td align="right">222</td>
<td align="right">90.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">24</td>
<td align="right">9.8%</td>
<td align="right">24</td>
<td align="right">9.8%</td>
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
<td align="right">406,232,359</td>
<td align="right">37.4%</td>
<td align="right">407,065,014</td>
<td align="right">37.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">601,405,894</td>
<td align="right">55.4%</td>
<td align="right">600,951,432</td>
<td align="right">55.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">47,408,441</td>
<td align="right">4.4%</td>
<td align="right">47,393,685</td>
<td align="right">4.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">29,863,693</td>
<td align="right">2.8%</td>
<td align="right">29,859,117</td>
<td align="right">2.8%</td>
<td align="right">-0.0%</td>
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
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,008,649</td>
<td align="right">6.8%</td>
<td align="right">1,932,350</td>
<td align="right">6.5%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,030,181</td>
<td align="right">3.5%</td>
<td align="right">1,061,879</td>
<td align="right">3.6%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,982,691</td>
<td align="right">13.4%</td>
<td align="right">4,027,154</td>
<td align="right">13.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,494,967</td>
<td align="right">8.4%</td>
<td align="right">2,490,564</td>
<td align="right">8.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9,532,457</td>
<td align="right">32.1%</td>
<td align="right">9,532,447</td>
<td align="right">32.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,490,754</td>
<td align="right">21.9%</td>
<td align="right">6,490,754</td>
<td align="right">21.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,214,555</td>
<td align="right">4.1%</td>
<td align="right">1,214,555</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">848,870</td>
<td align="right">2.9%</td>
<td align="right">848,870</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">732,280</td>
<td align="right">2.5%</td>
<td align="right">732,280</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">565,572</td>
<td align="right">1.9%</td>
<td align="right">565,572</td>
<td align="right">1.9%</td>
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
<td align="right">983,486</td>
<td align="right">2.1%</td>
<td align="right">918,283</td>
<td align="right">1.9%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,377,291</td>
<td align="right">2.9%</td>
<td align="right">1,332,130</td>
<td align="right">2.8%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">5,364,890</td>
<td align="right">11.3%</td>
<td align="right">5,534,955</td>
<td align="right">11.7%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,673,640</td>
<td align="right">5.6%</td>
<td align="right">2,601,827</td>
<td align="right">5.5%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,206,524</td>
<td align="right">6.8%</td>
<td align="right">3,137,155</td>
<td align="right">6.6%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,880,151</td>
<td align="right">16.6%</td>
<td align="right">7,942,403</td>
<td align="right">16.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,617,607</td>
<td align="right">11.8%</td>
<td align="right">5,653,842</td>
<td align="right">11.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">16,114,368</td>
<td align="right">34.0%</td>
<td align="right">16,115,896</td>
<td align="right">34.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,977,052</td>
<td align="right">4.2%</td>
<td align="right">1,977,052</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">533,301</td>
<td align="right">1.1%</td>
<td align="right">533,301</td>
<td align="right">1.1%</td>
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
<td align="left">Frame objects created</td>
<td align="right">1,218,028</td>
<td align="right">1.8%</td>
<td align="right">1,103,968</td>
<td align="right">1.6%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">5,427,088</td>
<td align="right">7.8%</td>
<td align="right">5,361,851</td>
<td align="right">7.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">11,985,227</td>
<td align="right">17.3%</td>
<td align="right">11,919,999</td>
<td align="right">17.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">11,985,227</td>
<td align="right">17.3%</td>
<td align="right">11,919,999</td>
<td align="right">17.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">57,320,815</td>
<td align="right">82.7%</td>
<td align="right">57,322,147</td>
<td align="right">82.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">388,602</td>
<td align="right">0.6%</td>
<td align="right">388,611</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,557,033</td>
<td align="right">9.5%</td>
<td align="right">6,557,042</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,558,139</td>
<td align="right">9.5%</td>
<td align="right">6,558,148</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">47,793,301</td>
<td align="right">69.0%</td>
<td align="right">47,793,319</td>
<td align="right">69.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">213</td>
<td align="right">0.0%</td>
<td align="right">213</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">893</td>
<td align="right">0.0%</td>
<td align="right">893</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">453,513</td>
<td align="right">0.7%</td>
<td align="right">453,513</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,161,490</td>
<td align="right">1.7%</td>
<td align="right">1,161,490</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">24</td>
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
<td align="right">285,311</td>
<td align="right"></td>
<td align="right">444,148</td>
<td align="right"></td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,924,410</td>
<td align="right"></td>
<td align="right">2,197,814</td>
<td align="right"></td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,640,979</td>
<td align="right"></td>
<td align="right">1,755,614</td>
<td align="right"></td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">327,308,482</td>
<td align="right">26.8%</td>
<td align="right">323,090,637</td>
<td align="right">26.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">351,156,235</td>
<td align="right">31.9%</td>
<td align="right">347,656,358</td>
<td align="right">31.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">28,726,127</td>
<td align="right"></td>
<td align="right">28,529,277</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">182,930,667</td>
<td align="right">15.0%</td>
<td align="right">181,776,516</td>
<td align="right">15.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">427,299,228</td>
<td align="right">38.8%</td>
<td align="right">425,270,378</td>
<td align="right">38.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">66,283,756</td>
<td align="right"></td>
<td align="right">66,019,985</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">52,388,745</td>
<td align="right"></td>
<td align="right">52,595,021</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">67,299,129</td>
<td align="right">70.3%</td>
<td align="right">67,039,170</td>
<td align="right">70.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">67,651,734</td>
<td align="right">70.7%</td>
<td align="right">67,391,683</td>
<td align="right">70.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">532,635,895</td>
<td align="right">43.6%</td>
<td align="right">531,071,096</td>
<td align="right">43.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">121,198,746</td>
<td align="right">11.0%</td>
<td align="right">120,849,325</td>
<td align="right">11.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">177,407,344</td>
<td align="right">14.5%</td>
<td align="right">177,795,647</td>
<td align="right">14.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">202,278,843</td>
<td align="right">18.4%</td>
<td align="right">202,598,905</td>
<td align="right">18.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">313,937</td>
<td align="right">0.3%</td>
<td align="right">313,845</td>
<td align="right">0.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">28,074,330</td>
<td align="right">29.3%</td>
<td align="right">28,074,394</td>
<td align="right">29.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">28,093,095</td>
<td align="right"></td>
<td align="right">28,093,159</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">38,668</td>
<td align="right">0.0%</td>
<td align="right">38,668</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,109,929</td>
<td align="right"></td>
<td align="right">1,109,929</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">99,223</td>
<td align="right">8.9%</td>
<td align="right">99,223</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">5,005</td>
<td align="right">0.5%</td>
<td align="right">5,005</td>
<td align="right">0.5%</td>
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
<td align="right">1,326</td>
<td align="right">28,109</td>
<td align="right">72,528,681</td>
<td align="right">11,497,490</td>
<td align="right">1,927,156</td>
<td align="right">1,326</td>
<td align="right">28,109</td>
<td align="right">72,511,491</td>
<td align="right">11,497,707</td>
<td align="right">1,925,338</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,547</td>
<td align="right">35.6%</td>
<td align="right">1,202</td>
<td align="right">29.2%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">30,678,266</td>
<td align="right"></td>
<td align="right">26,015,157</td>
<td align="right"></td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,340</td>
<td align="right">30.8%</td>
<td align="right">1,176</td>
<td align="right">28.6%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">4,350</td>
<td align="right"></td>
<td align="right">4,116</td>
<td align="right"></td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">378,467,463</td>
<td align="right">1,233.7%</td>
<td align="right">361,578,752</td>
<td align="right">1,389.9%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,803</td>
<td align="right">64.4%</td>
<td align="right">2,914</td>
<td align="right">70.8%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">85</td>
<td align="right">2.0%</td>
<td align="right">84</td>
<td align="right">2.0%</td>
<td align="right">-1.2%</td>
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
<td align="right">2,739</td>
<td align="right">97.7%</td>
<td align="right">2,850</td>
<td align="right">97.8%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,803</td>
<td align="right"></td>
<td align="right">2,914</td>
<td align="right"></td>
<td align="right">4.0%</td>
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
<td align="right">176</td>
<td align="right">6.3%</td>
<td align="right">263</td>
<td align="right">9.0%</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">600</td>
<td align="right">21.4%</td>
<td align="right">714</td>
<td align="right">24.5%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">984</td>
<td align="right">35.1%</td>
<td align="right">877</td>
<td align="right">30.1%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">745</td>
<td align="right">26.6%</td>
<td align="right">783</td>
<td align="right">26.9%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">234</td>
<td align="right">8.3%</td>
<td align="right">213</td>
<td align="right">7.3%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">64</td>
<td align="right">2.3%</td>
<td align="right">64</td>
<td align="right">2.2%</td>
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
<td align="right">130</td>
<td align="right">4.6%</td>
<td align="right">237</td>
<td align="right">8.1%</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">571</td>
<td align="right">20.4%</td>
<td align="right">587</td>
<td align="right">20.1%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">337</td>
<td align="right">12.0%</td>
<td align="right">350</td>
<td align="right">12.0%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">994</td>
<td align="right">35.5%</td>
<td align="right">968</td>
<td align="right">33.2%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">644</td>
<td align="right">23.0%</td>
<td align="right">645</td>
<td align="right">22.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">63</td>
<td align="right">2.2%</td>
<td align="right">63</td>
<td align="right">2.2%</td>
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
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">19,778</td>
<td align="right">45,755</td>
<td align="right">131.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">183,080</td>
<td align="right">395,928</td>
<td align="right">116.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">162,828</td>
<td align="right">349,699</td>
<td align="right">114.8%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">15,905</td>
<td align="right">56</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">149,065</td>
<td align="right">291,786</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">33,952</td>
<td align="right">2,254</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">35</td>
<td align="right">3</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">35</td>
<td align="right">3</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">193,913</td>
<td align="right">28,551</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">287,521</td>
<td align="right">528,720</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">129,448</td>
<td align="right">21,357</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">178,240</td>
<td align="right">325,811</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">65,958</td>
<td align="right">115,148</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,143</td>
<td align="right">8,883</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">788,567</td>
<td align="right">232,958</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">698,158</td>
<td align="right">213,935</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,170</td>
<td align="right">749</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">164,409</td>
<td align="right">57,330</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">368,661</td>
<td align="right">597,028</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">369,028</td>
<td align="right">585,135</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">86,622</td>
<td align="right">135,812</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">154,126</td>
<td align="right">240,156</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">390,446</td>
<td align="right">580,074</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">395,577</td>
<td align="right">583,695</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">669,916</td>
<td align="right">948,147</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">376,037</td>
<td align="right">522,560</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">93,543</td>
<td align="right">128,388</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">768,484</td>
<td align="right">1,018,460</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">456,592</td>
<td align="right">600,178</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">15,031,196</td>
<td align="right">10,863,401</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,091,211</td>
<td align="right">1,392,684</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">5,440,627</td>
<td align="right">4,001,449</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">301,565</td>
<td align="right">377,864</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">205,136</td>
<td align="right">255,657</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">207,765</td>
<td align="right">258,188</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">3,468,843</td>
<td align="right">2,703,434</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">323,710</td>
<td align="right">260,686</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">25,162,886</td>
<td align="right">20,718,954</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,309,563</td>
<td align="right">2,671,801</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">30,678,266</td>
<td align="right">26,015,157</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,079,029</td>
<td align="right">917,456</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">481,341</td>
<td align="right">414,035</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,248,944</td>
<td align="right">1,421,219</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">35,430,022</td>
<td align="right">30,787,932</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">991,694</td>
<td align="right">1,120,827</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">964,216</td>
<td align="right">1,079,104</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,096,202</td>
<td align="right">1,850,277</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">434,397</td>
<td align="right">386,850</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,868,617</td>
<td align="right">2,072,771</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">364,045</td>
<td align="right">403,812</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">374,326</td>
<td align="right">414,282</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">799,472</td>
<td align="right">876,448</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">1,295,823</td>
<td align="right">1,415,990</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">832,821</td>
<td align="right">902,334</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">3,648,101</td>
<td align="right">3,937,647</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,538,058</td>
<td align="right">2,736,573</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">392,477</td>
<td align="right">362,242</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,257,078</td>
<td align="right">1,333,141</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">3,706,130</td>
<td align="right">3,485,823</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,954,945</td>
<td align="right">1,841,225</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,483,402</td>
<td align="right">2,605,254</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,043,881</td>
<td align="right">6,337,492</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,466,619</td>
<td align="right">4,258,985</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">232,052</td>
<td align="right">242,324</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,023,096</td>
<td align="right">4,182,027</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,034,039</td>
<td align="right">4,882,168</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">20,741,478</td>
<td align="right">20,139,360</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">34,961</td>
<td align="right">35,973</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">5,266,091</td>
<td align="right">5,124,492</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">637,412</td>
<td align="right">654,420</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">663,305</td>
<td align="right">680,313</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,814,579</td>
<td align="right">1,770,116</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,365,911</td>
<td align="right">2,420,242</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,128,192</td>
<td align="right">2,080,549</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,669,798</td>
<td align="right">1,635,069</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">571,419</td>
<td align="right">559,839</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,015,666</td>
<td align="right">2,955,414</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">32,626,185</td>
<td align="right">33,263,521</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,729,660</td>
<td align="right">1,697,962</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">24,618,523</td>
<td align="right">25,066,498</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,863,473</td>
<td align="right">1,831,679</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">7,362,515</td>
<td align="right">7,243,100</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">254,875</td>
<td align="right">258,598</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">13,678,469</td>
<td align="right">13,877,281</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,796,803</td>
<td align="right">2,760,983</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">332,451</td>
<td align="right">328,356</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">4,986,328</td>
<td align="right">4,926,787</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,604,014</td>
<td align="right">4,645,899</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">123,923</td>
<td align="right">124,919</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">357,037</td>
<td align="right">354,297</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,055,572</td>
<td align="right">1,047,904</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,306,158</td>
<td align="right">3,328,657</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">5,549,547</td>
<td align="right">5,585,729</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">49,916</td>
<td align="right">49,606</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,303,018</td>
<td align="right">4,328,990</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">7,769,341</td>
<td align="right">7,811,754</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">4,291,372</td>
<td align="right">4,311,739</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,521,727</td>
<td align="right">6,492,337</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,751,756</td>
<td align="right">4,772,775</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,390,761</td>
<td align="right">1,384,623</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,901,632</td>
<td align="right">2,889,475</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,513,594</td>
<td align="right">6,492,216</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,452,529</td>
<td align="right">1,449,789</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">3,895,710</td>
<td align="right">3,902,105</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">226,535</td>
<td align="right">226,826</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">229,244</td>
<td align="right">229,535</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">226,784</td>
<td align="right">226,826</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,541,564</td>
<td align="right">2,541,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,227,755</td>
<td align="right">2,227,755</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,207,290</td>
<td align="right">1,207,290</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,164,555</td>
<td align="right">1,164,555</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,041,083</td>
<td align="right">1,041,083</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">975,423</td>
<td align="right">975,423</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">908,841</td>
<td align="right">908,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">651,252</td>
<td align="right">651,252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">635,166</td>
<td align="right">635,166</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">592,788</td>
<td align="right">592,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">572,124</td>
<td align="right">572,124</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">374,208</td>
<td align="right">374,208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">207,135</td>
<td align="right">207,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">173,254</td>
<td align="right">173,254</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">170,545</td>
<td align="right">170,545</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">139,200</td>
<td align="right">139,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">128,793</td>
<td align="right">128,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">63,042</td>
<td align="right">63,042</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">54,240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">39,816</td>
<td align="right">39,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">33,075</td>
<td align="right">33,075</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">27,237</td>
<td align="right">27,237</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">2,709</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">121</td>
<td align="right">121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">121</td>
<td align="right">121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">115</td>
<td align="right">115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">115</td>
<td align="right">115</td>
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
<td align="left">CALL</td>
<td align="right">21</td>
<td align="right">89</td>
<td align="right">323.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">488</td>
<td align="right">429</td>
<td align="right">-12.1%</td>
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
<td align="right">37</td>
<td align="right">37</td>
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
<td align="right">8</td>
<td align="right">8</td>
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
<td align="right">8</td>
<td align="right">8</td>
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
Stats gathered on: 2024-12-13
