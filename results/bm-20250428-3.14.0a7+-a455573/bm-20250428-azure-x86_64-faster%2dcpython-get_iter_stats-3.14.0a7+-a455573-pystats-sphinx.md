
# Pystats results

- benchmark: sphinx
- fork: faster-cpython
- ref: get-iter-stats
- commit hash: a455573
- commit date: 2025-04-28T18:14:38+01:00

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
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
<th align="right">Miss ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">641,147,060</td>
<td align="right">16.6%</td>
<td align="right">16.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">179,606,134</td>
<td align="right">4.6%</td>
<td align="right">21.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">171,216,259</td>
<td align="right">4.4%</td>
<td align="right">25.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">166,722,051</td>
<td align="right">4.3%</td>
<td align="right">29.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,117,752</td>
<td align="right">4.0%</td>
<td align="right">33.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">145,319,070</td>
<td align="right">3.8%</td>
<td align="right">37.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">140,867,683</td>
<td align="right">3.6%</td>
<td align="right">41.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">137,431,775</td>
<td align="right">3.5%</td>
<td align="right">44.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">125,750,591</td>
<td align="right">3.2%</td>
<td align="right">48.1%</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">115,978,879</td>
<td align="right">3.0%</td>
<td align="right">51.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">101,047,411</td>
<td align="right">2.6%</td>
<td align="right">53.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">100,140,366</td>
<td align="right">2.6%</td>
<td align="right">56.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">89,884,364</td>
<td align="right">2.3%</td>
<td align="right">58.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">87,171,399</td>
<td align="right">2.3%</td>
<td align="right">60.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">87,037,228</td>
<td align="right">2.2%</td>
<td align="right">63.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">84,060,459</td>
<td align="right">2.2%</td>
<td align="right">65.3%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">78,131,393</td>
<td align="right">2.0%</td>
<td align="right">67.3%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">74,884,478</td>
<td align="right">1.9%</td>
<td align="right">69.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">74,107,210</td>
<td align="right">1.9%</td>
<td align="right">71.2%</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">61,068,650</td>
<td align="right">1.6%</td>
<td align="right">72.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">55,116,703</td>
<td align="right">1.4%</td>
<td align="right">74.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">50,199,633</td>
<td align="right">1.3%</td>
<td align="right">75.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">49,020,848</td>
<td align="right">1.3%</td>
<td align="right">76.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">39,973,551</td>
<td align="right">1.0%</td>
<td align="right">77.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,529,008</td>
<td align="right">1.0%</td>
<td align="right">78.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,888,512</td>
<td align="right">1.0%</td>
<td align="right">79.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">38,348,023</td>
<td align="right">1.0%</td>
<td align="right">80.8%</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,031,560</td>
<td align="right">1.0%</td>
<td align="right">81.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">35,916,152</td>
<td align="right">0.9%</td>
<td align="right">82.7%</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">30,039,927</td>
<td align="right">0.8%</td>
<td align="right">83.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">28,727,438</td>
<td align="right">0.7%</td>
<td align="right">84.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">25,341,559</td>
<td align="right">0.7%</td>
<td align="right">84.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">23,611,786</td>
<td align="right">0.6%</td>
<td align="right">85.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,681,571</td>
<td align="right">0.6%</td>
<td align="right">86.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">21,490,121</td>
<td align="right">0.6%</td>
<td align="right">86.6%</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">20,873,441</td>
<td align="right">0.5%</td>
<td align="right">87.2%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">18,586,735</td>
<td align="right">0.5%</td>
<td align="right">87.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,981,385</td>
<td align="right">0.5%</td>
<td align="right">88.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">17,777,171</td>
<td align="right">0.5%</td>
<td align="right">88.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">17,570,044</td>
<td align="right">0.5%</td>
<td align="right">89.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,335,149</td>
<td align="right">0.4%</td>
<td align="right">89.5%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">16,964,671</td>
<td align="right">0.4%</td>
<td align="right">89.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,962,767</td>
<td align="right">0.4%</td>
<td align="right">90.3%</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">16,492,163</td>
<td align="right">0.4%</td>
<td align="right">90.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15,344,709</td>
<td align="right">0.4%</td>
<td align="right">91.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">14,190,345</td>
<td align="right">0.4%</td>
<td align="right">91.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">14,055,848</td>
<td align="right">0.4%</td>
<td align="right">91.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">13,602,656</td>
<td align="right">0.4%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,948,139</td>
<td align="right">0.3%</td>
<td align="right">92.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">11,745,417</td>
<td align="right">0.3%</td>
<td align="right">92.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,350,686</td>
<td align="right">0.3%</td>
<td align="right">93.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">11,074,517</td>
<td align="right">0.3%</td>
<td align="right">93.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">11,030,981</td>
<td align="right">0.3%</td>
<td align="right">93.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">10,991,106</td>
<td align="right">0.3%</td>
<td align="right">94.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">10,092,363</td>
<td align="right">0.3%</td>
<td align="right">94.3%</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,050,197</td>
<td align="right">0.3%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">9,666,210</td>
<td align="right">0.2%</td>
<td align="right">94.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,738,496</td>
<td align="right">0.2%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">8,427,790</td>
<td align="right">0.2%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">7,682,466</td>
<td align="right">0.2%</td>
<td align="right">95.4%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,308,781</td>
<td align="right">0.2%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,747,743</td>
<td align="right">0.2%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,559,408</td>
<td align="right">0.2%</td>
<td align="right">96.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,948,305</td>
<td align="right">0.2%</td>
<td align="right">96.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,699,834</td>
<td align="right">0.1%</td>
<td align="right">96.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,682,839</td>
<td align="right">0.1%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,677,194</td>
<td align="right">0.1%</td>
<td align="right">96.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">5,568,615</td>
<td align="right">0.1%</td>
<td align="right">96.7%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">5,090,547</td>
<td align="right">0.1%</td>
<td align="right">96.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,981,790</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,777,355</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,643,467</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,584,696</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,540,429</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,485,293</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,469,827</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,264,351</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,115,342</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3,533,727</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,508,317</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,487,582</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">3,356,559</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,276,986</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,050,951</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,973,842</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,953,118</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,941,148</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">2,687,394</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,687,005</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,581,290</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,505,941</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,499,272</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">2,019,447</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,834,952</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,795,183</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,741,585</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,671,167</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,671,167</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,670,029</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,625,964</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,578,480</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,511,872</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,391,566</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,355,264</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,341,773</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,280,595</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,271,684</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,267,606</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,133,536</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,103,527</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,091,630</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">893,087</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">833,578</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">771,482</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">743,884</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">728,729</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">703,057</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">641,072</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">598,928</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">554,681</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">501,734</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">481,177</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">346,302</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,744</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">266,633</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">256,363</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">247,953</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">196,240</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">192,011</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">170,348</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">158,405</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">152,839</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">149,588</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">146,469</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">129,078</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">118,994</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">85,331</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">84,414</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">79,858</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">76,983</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">53,610</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">38,142</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,575</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">32,076</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">28,959</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">26,349</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">25,178</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">24,500</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">23,610</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">23,179</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,621</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">21,431</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,384</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,467</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,810</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">10,427</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,253</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,706</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,706</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4,541</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,013</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,560</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,049</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1,337</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">488</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">346</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">285</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">259</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">129</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">117</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">98</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">10</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
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

<table>
<thead>
<tr>
<th align="left">Pair</th>
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">118,286,842</td>
<td align="right">3.1%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">107,544,622</td>
<td align="right">2.8%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_BORROW</td>
<td align="right">101,515,223</td>
<td align="right">2.6%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">98,280,448</td>
<td align="right">2.5%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">86,129,304</td>
<td align="right">2.2%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL RETURN_VALUE</td>
<td align="right">79,085,358</td>
<td align="right">2.0%</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW</td>
<td align="right">67,476,382</td>
<td align="right">1.7%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">64,868,232</td>
<td align="right">1.7%</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">57,934,521</td>
<td align="right">1.5%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">57,718,693</td>
<td align="right">1.5%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_BORROW</td>
<td align="right">55,327,694</td>
<td align="right">1.4%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_BORROW</td>
<td align="right">50,340,530</td>
<td align="right">1.3%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">48,704,530</td>
<td align="right">1.3%</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">43,293,050</td>
<td align="right">1.1%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_LIST</td>
<td align="right">40,697,833</td>
<td align="right">1.1%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">39,661,152</td>
<td align="right">1.0%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">POP_TOP RESUME_CHECK</td>
<td align="right">39,527,035</td>
<td align="right">1.0%</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST</td>
<td align="right">39,436,013</td>
<td align="right">1.0%</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN POP_TOP</td>
<td align="right">39,273,624</td>
<td align="right">1.0%</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR GET_ITER</td>
<td align="right">39,046,977</td>
<td align="right">1.0%</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_GEN</td>
<td align="right">38,924,834</td>
<td align="right">1.0%</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">END_FOR POP_ITER</td>
<td align="right">38,888,512</td>
<td align="right">1.0%</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE END_FOR</td>
<td align="right">38,888,512</td>
<td align="right">1.0%</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">POP_ITER JUMP_BACKWARD_NO_JIT</td>
<td align="right">37,845,660</td>
<td align="right">1.0%</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">37,532,039</td>
<td align="right">1.0%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_CONST_IMMORTAL</td>
<td align="right">37,483,272</td>
<td align="right">1.0%</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW CALL_ISINSTANCE</td>
<td align="right">36,815,682</td>
<td align="right">1.0%</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,792,458</td>
<td align="right">0.9%</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RETURN_GENERATOR</td>
<td align="right">34,928,973</td>
<td align="right">0.9%</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW TO_BOOL_BOOL</td>
<td align="right">34,001,460</td>
<td align="right">0.9%</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_LIST</td>
<td align="right">33,070,543</td>
<td align="right">0.9%</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST POP_ITER</td>
<td align="right">31,852,054</td>
<td align="right">0.8%</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST_BORROW</td>
<td align="right">30,487,666</td>
<td align="right">0.8%</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR</td>
<td align="right">28,724,470</td>
<td align="right">0.7%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_MODULE</td>
<td align="right">28,281,603</td>
<td align="right">0.7%</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">27,583,977</td>
<td align="right">0.7%</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW</td>
<td align="right">27,538,801</td>
<td align="right">0.7%</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_TUPLE</td>
<td align="right">23,156,118</td>
<td align="right">0.6%</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">22,471,669</td>
<td align="right">0.6%</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST_BORROW</td>
<td align="right">22,395,519</td>
<td align="right">0.6%</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW YIELD_VALUE</td>
<td align="right">22,183,241</td>
<td align="right">0.6%</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK POP_TOP</td>
<td align="right">22,087,729</td>
<td align="right">0.6%</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">22,048,018</td>
<td align="right">0.6%</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN</td>
<td align="right">22,038,266</td>
<td align="right">0.6%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">POP_TOP JUMP_BACKWARD_NO_JIT</td>
<td align="right">21,839,126</td>
<td align="right">0.6%</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN RESUME_CHECK</td>
<td align="right">21,795,002</td>
<td align="right">0.6%</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE STORE_FAST</td>
<td align="right">21,702,379</td>
<td align="right">0.6%</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">21,447,053</td>
<td align="right">0.6%</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_GEN</td>
<td align="right">20,256,628</td>
<td align="right">0.5%</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES GET_ITER</td>
<td align="right">19,783,872</td>
<td align="right">0.5%</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE STORE_FAST</td>
<td align="right">19,236,280</td>
<td align="right">0.5%</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_BUILTIN</td>
<td align="right">19,064,916</td>
<td align="right">0.5%</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK NOP</td>
<td align="right">18,665,753</td>
<td align="right">0.5%</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE</td>
<td align="right">17,886,054</td>
<td align="right">0.5%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE CALL_ISINSTANCE</td>
<td align="right">17,835,075</td>
<td align="right">0.5%</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_BORROW</td>
<td align="right">17,759,557</td>
<td align="right">0.5%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">17,401,625</td>
<td align="right">0.4%</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_CONST_IMMORTAL</td>
<td align="right">16,762,598</td>
<td align="right">0.4%</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE JUMP_BACKWARD_NO_JIT</td>
<td align="right">16,467,493</td>
<td align="right">0.4%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_CONST_IMMORTAL</td>
<td align="right">15,545,048</td>
<td align="right">0.4%</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL RESUME_CHECK</td>
<td align="right">15,495,088</td>
<td align="right">0.4%</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE GET_ITER</td>
<td align="right">15,088,687</td>
<td align="right">0.4%</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_CONST_IMMORTAL</td>
<td align="right">14,817,331</td>
<td align="right">0.4%</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE POP_JUMP_IF_TRUE</td>
<td align="right">14,808,762</td>
<td align="right">0.4%</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">14,107,645</td>
<td align="right">0.4%</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST_BORROW</td>
<td align="right">13,927,166</td>
<td align="right">0.4%</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,605,274</td>
<td align="right">0.4%</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST_BORROW</td>
<td align="right">13,513,594</td>
<td align="right">0.3%</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST_IMMORTAL</td>
<td align="right">13,489,930</td>
<td align="right">0.3%</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">12,877,818</td>
<td align="right">0.3%</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE POP_ITER</td>
<td align="right">12,850,110</td>
<td align="right">0.3%</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_SLOT</td>
<td align="right">12,556,565</td>
<td align="right">0.3%</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_TUPLE</td>
<td align="right">12,495,115</td>
<td align="right">0.3%</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW POP_JUMP_IF_NOT_NONE</td>
<td align="right">12,471,371</td>
<td align="right">0.3%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">12,418,662</td>
<td align="right">0.3%</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">COPY TO_BOOL_NONE</td>
<td align="right">12,050,872</td>
<td align="right">0.3%</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST_BORROW</td>
<td align="right">11,646,268</td>
<td align="right">0.3%</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL LOAD_FAST_BORROW</td>
<td align="right">11,525,446</td>
<td align="right">0.3%</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST_BORROW</td>
<td align="right">11,452,431</td>
<td align="right">0.3%</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">11,407,091</td>
<td align="right">0.3%</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,071,120</td>
<td align="right">0.3%</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_NON_PY_GENERAL</td>
<td align="right">10,961,735</td>
<td align="right">0.3%</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">10,670,873</td>
<td align="right">0.3%</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">10,297,552</td>
<td align="right">0.3%</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE POP_TOP</td>
<td align="right">9,821,207</td>
<td align="right">0.3%</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_FAST_BORROW</td>
<td align="right">9,652,390</td>
<td align="right">0.2%</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">9,633,564</td>
<td align="right">0.2%</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">9,611,944</td>
<td align="right">0.2%</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW PUSH_NULL</td>
<td align="right">9,588,754</td>
<td align="right">0.2%</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER</td>
<td align="right">9,514,599</td>
<td align="right">0.2%</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR STORE_FAST</td>
<td align="right">9,308,093</td>
<td align="right">0.2%</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_ATTR</td>
<td align="right">8,982,787</td>
<td align="right">0.2%</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_FAST_BORROW</td>
<td align="right">8,900,077</td>
<td align="right">0.2%</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_SUBSCR_DICT</td>
<td align="right">8,883,434</td>
<td align="right">0.2%</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT RETURN_VALUE</td>
<td align="right">8,777,413</td>
<td align="right">0.2%</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW</td>
<td align="right">8,769,667</td>
<td align="right">0.2%</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">8,696,996</td>
<td align="right">0.2%</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST JUMP_BACKWARD_NO_JIT</td>
<td align="right">8,608,505</td>
<td align="right">0.2%</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW POP_JUMP_IF_NONE</td>
<td align="right">8,565,052</td>
<td align="right">0.2%</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_PY_GENERAL</td>
<td align="right">8,490,755</td>
<td align="right">0.2%</td>
<td align="right">71.4%</td>
</tr>
</tbody>
</table>


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each Tier 1 opcode. </summary>


This does not include the unspecialized instructions that occur after a
specialized instruction deoptimizes.

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,012,993</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">679,339</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">395,197</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">209,276</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">148,665</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">800,817</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">676,124</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">407,616</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">313,911</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">227,840</td>
<td align="right">6.5%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">82,559</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">73,742</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">39,936</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">196,155</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,046,977</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">19,783,872</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,088,687</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,368,284</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,725,747</td>
<td align="right">1.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">38,924,834</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">33,070,543</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">12,495,115</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,785,777</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">943,698</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">39,661,152</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">245,912</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">237,557</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">6,912</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,522</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,552,380</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,267,286</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">154,176</td>
<td align="right">5.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,272,279</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">721,088</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">496,764</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">270,680</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">104,167</td>
<td align="right">3.5%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">137,152</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">49,484</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">32,082</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">28,349</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">817</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">133,944</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">50,869</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">48,115</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,752</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,688</td>
<td align="right">1.1%</td>
</tr>
</tbody>
</table>


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,590,513</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">22,455</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">12,929</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">52</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,625,964</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">117,056</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">16,512</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,284</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">6,589</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">108</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">96,832</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">34,717</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">16,404</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,216</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">303</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">38,888,512</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_ITER</td>
<td align="right">38,888,512</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,552</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">1,154</td>
<td align="right">13.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,706</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">554,681</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">554,681</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,682,839</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">150,270</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">70,032</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">12,859</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,415</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">2,813,889</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,732,140</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">347,936</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">32,399</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,854</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### FORMAT_WITH_SPEC

<details>
<summary> Successors and predecessors for FORMAT_WITH_SPEC </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">2,559</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">2,559</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">7,551</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,152</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,701</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">37,532,039</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">498,171</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,350</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,103</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">128</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">75</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">18</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,337</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">245,635</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,728</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">119,095</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">71,035</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">55,767</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,099</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">2,330</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">18,665,753</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,605,295</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">6,348,677</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">5,121,096</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,989,647</td>
<td align="right">7.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">30,487,666</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,218,913</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,116,147</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,498,830</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,097,979</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,197,850</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">327,684</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">115,769</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">18,633</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">7,398</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,119,030</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">327,684</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">115,769</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">87,261</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">12,269</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>


</details>

### POP_ITER

<details>
<summary> Successors and predecessors for POP_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,888,512</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">31,852,054</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">12,850,110</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,308,597</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">270,205</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">37,845,660</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">37,483,272</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,229,933</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,924,109</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,808,456</td>
<td align="right">2.1%</td>
</tr>
</tbody>
</table>


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,273,624</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">22,087,729</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,048,018</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,821,207</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,365,167</td>
<td align="right">2.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">39,527,035</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">22,395,519</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">21,839,126</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4,773,765</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,843,915</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">889,877</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">203,084</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">158,659</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">113,128</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">99,840</td>
<td align="right">6.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,599,199</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">49,921</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,854</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">159</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">11,407,091</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,588,754</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,001,417</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,523,635</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">219,710</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,927,166</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">5,064,941</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,606,217</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,552,380</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">908,793</td>
<td align="right">3.6%</td>
</tr>
</tbody>
</table>


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">34,928,973</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,723,002</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">837,259</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">18,562</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,546</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">39,046,977</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">207,553</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">205,824</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">25,169</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">17,860</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">79,085,358</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,418,662</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">8,777,413</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">6,725,984</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">6,617,443</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,888,512</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">37,532,039</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">22,048,018</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,107,645</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,418,662</td>
<td align="right">8.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">809,220</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">454,023</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">194,588</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">186,351</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,685</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">856,645</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">507,819</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">185,242</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">79,846</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">15,746</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">7,363,073</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,194,441</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,148,741</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">913,664</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">894,954</td>
<td align="right">5.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">12,877,818</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,276,497</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">74,057</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">70,563</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">19,603</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,080</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">387</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">11,461</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">72,055</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">4,927</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">66,814</td>
<td align="right">86.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,928</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,926</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">311</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">47,678</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">19,204</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,226</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,532</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">218</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">47,395</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">31,730</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">512</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">218</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">3,451,727</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,630,891</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,939,994</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">894,777</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">602,376</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,656,840</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,725,747</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,673,668</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,333,931</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">924,325</td>
<td align="right">8.1%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,532,051</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,390,520</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">892,947</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">831,734</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">792,069</td>
<td align="right">7.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,035,168</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,051,563</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">831,734</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">577,474</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">348,928</td>
<td align="right">3.2%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">874,651</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">842,298</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">695,185</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">643,276</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">375,905</td>
<td align="right">8.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,715,201</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,131,831</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">321,545</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">154,176</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">111,964</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,399</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">8,766</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">135</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">126</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">126</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">14,398</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,783</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">168</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">126</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">90</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">68,751</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">50,240</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">117,056</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,938</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">2,732,140</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">196,512</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">12,414</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">82</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,558,511</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">224,902</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">75,136</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">27,345</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">23,997</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">8,364,475</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,881,438</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,989,747</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,750,843</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">577,474</td>
<td align="right">3.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,725,984</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">5,691,158</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,043,189</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">895,591</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">712,490</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">6,631</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,289</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,586</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4,402</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,379</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,815</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">6,836</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">5,643</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,594</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,477</td>
<td align="right">3.9%</td>
</tr>
</tbody>
</table>


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,270,233</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,344</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">88</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">874,651</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">219,710</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">175,862</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,344</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">87</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,730</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">319</td>
<td align="right">15.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,355</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">374</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">117</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">47</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">41</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">297,327</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">186,062</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">67,713</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">28,502</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">14,399</td>
<td align="right">2.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">524,714</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">91,653</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">20,800</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,527</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">695</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,150,643</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">727,349</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">512,241</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">497,381</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">425,020</td>
<td align="right">9.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,458,713</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">845,615</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">150,702</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,538</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,039</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,765,751</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,691,849</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60,860</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">60,543</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">60,543</td>
<td align="right">1.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,682,839</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,669,132</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">5,239,967</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,116,644</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">957,208</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">589,963</td>
<td align="right">3.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">12,050,872</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,148,741</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">929,178</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">868,071</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">231,361</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">259,953</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">237,557</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">111,951</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,934</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">19,990</td>
<td align="right">2.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">721,288</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">18,562</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,970</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,384</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">10,880</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,440</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">63</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,240</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,280</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">640</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">320</td>
<td align="right">14.3%</td>
</tr>
</tbody>
</table>


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,260,906</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,648</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,687</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">43</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,267,286</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">259</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">64</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">22</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">243</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">65</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">24</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">8</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,856,495</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">377,064</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">310,794</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">256,698</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">97,096</td>
<td align="right">2.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,861,928</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">673,594</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">392,445</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">295,849</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">95,347</td>
<td align="right">2.7%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">9,514,599</td>
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,785,777</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">295,849</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,422</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,495,600</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,791,180</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">3,308,597</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,422</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">458</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">20,821</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">10,115</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,139</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,267</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">10,115</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">2,566</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">128</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">15,038</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">9,267</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,044</td>
<td align="right">7.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">20,821</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,930</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">577</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">14</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">5</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,116,597</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">984,870</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">906,924</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">895,740</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">42,497</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,839,705</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,801,517</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">297,428</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">39,871</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,017</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">165</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">124</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">38</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">36</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">35</td>
<td align="right">7.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">488</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">12,269</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">10,096</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,590</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">20,900</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">3,335</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">3,259</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">644</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">609</td>
<td align="right">2.1%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">851,701</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">570,844</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">405,107</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">153,664</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">152,658</td>
<td align="right">6.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,311,220</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">373,770</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">221,590</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">220,069</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">206,534</td>
<td align="right">8.3%</td>
</tr>
</tbody>
</table>


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,109,792</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">741,591</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">712,490</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">639,935</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">407,616</td>
<td align="right">9.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,099,335</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,512</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">6,444</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">248</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,270,072</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,512</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,279</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">249</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,270,233</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,511</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,280</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">28,724,470</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,982,787</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,677,147</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,376,319</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,231,751</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">11,452,431</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">9,308,093</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,237,759</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,715,103</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">2,691,849</td>
<td align="right">5.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_COMMON_CONSTANT

<details>
<summary> Successors and predecessors for LOAD_COMMON_CONSTANT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">25,178</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">IS_OP</td>
<td align="right">25,178</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">14,396</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,462</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,876</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,205</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,099</td>
<td align="right">7.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">10,728</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,768</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,876</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,318</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">5,064</td>
<td align="right">9.4%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">430,946</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">281,542</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">165,769</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">151,100</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">121,170</td>
<td align="right">8.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">404,837</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">289,457</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">165,769</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">149,674</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">107,837</td>
<td align="right">7.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,996,900</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,843,915</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,498,830</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,084,475</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,449,119</td>
<td align="right">10.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,881,438</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,680,976</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,053,503</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,077,082</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,025,881</td>
<td align="right">8.6%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">943,698</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">147,932</td>
<td align="right">13.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">943,698</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">147,932</td>
<td align="right">13.6%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_BORROW

<details>
<summary> Successors and predecessors for LOAD_FAST_BORROW </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">101,515,223</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">98,280,448</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">67,476,382</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">55,327,694</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">50,340,530</td>
<td align="right">7.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">107,544,622</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">64,868,232</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">57,718,693</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,792,458</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">34,001,460</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_BORROW_LOAD_FAST_BORROW

<details>
<summary> Successors and predecessors for LOAD_FAST_BORROW_LOAD_FAST_BORROW </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">43,293,050</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,071,120</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">9,633,564</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,464,246</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,764,247</td>
<td align="right">5.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">36,815,682</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">10,670,873</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,900,077</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,696,996</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,364,475</td>
<td align="right">7.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">59,776</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">13,696</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,085</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,111</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,481</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">62,075</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,736</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,971</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,240</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,239</td>
<td align="right">1.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,036,872</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,876,807</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">189,632</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">89,818</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">88,643</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,996,900</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">3,876,228</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">189,630</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">143,678</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">132,992</td>
<td align="right">1.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,388</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,634</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,031</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,632</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,581</td>
<td align="right">7.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,537</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,303</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">831</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">825</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">414</td>
<td align="right">1.9%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">6,444</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">3,781</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">2,939</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,554</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,058</td>
<td align="right">8.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">8,418</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">2,939</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">2,212</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,110</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,945</td>
<td align="right">7.9%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SMALL_INT

<details>
<summary> Successors and predecessors for LOAD_SMALL_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,803,118</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,698,273</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">750,835</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">640,848</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">584,060</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,185,747</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">2,492,066</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,323,968</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,795,139</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">874,272</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SPECIAL

<details>
<summary> Successors and predecessors for LOAD_SPECIAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">173,151</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">173,151</td>
<td align="right">50.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SWAP</td>
<td align="right">173,151</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">86,369</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">80,885</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,486</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">411</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">255</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4</td>
<td align="right">1.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">179</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">30</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">19</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">9</td>
<td align="right">3.5%</td>
</tr>
</tbody>
</table>


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">231,087</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">110,943</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">84,657</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">43,706</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">15,062</td>
<td align="right">3.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">263,331</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">231,087</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">6,912</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">404</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">557,926</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">20,864</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">13,255</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,558</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,919</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">594,078</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,298</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,196</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">259</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">72</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">118,286,842</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,877,818</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,978,789</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,836,663</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,834,969</td>
<td align="right">2.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">101,515,223</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">22,038,266</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">13,489,930</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">8,464,246</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,421,623</td>
<td align="right">5.1%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,565,052</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,791,826</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,327,085</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">39,247</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">7,423</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,036,519</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,790,184</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,108,878</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">352,396</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">147,009</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,471,371</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,507,368</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">764,256</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">610,368</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">77,566</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">11,646,268</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,515,745</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">733,989</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">667,502</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">572,481</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">22,471,669</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">14,808,762</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,014,332</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,458,719</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,276,497</td>
<td align="right">4.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">16,467,493</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,513,594</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,821,207</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,105,540</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4,075,372</td>
<td align="right">7.4%</td>
</tr>
</tbody>
</table>


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">82,743</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20,286</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">8,831</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,296</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,220</td>
<td align="right">3.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">65,649</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">60,612</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,279</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">115,769</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">49,921</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,017</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,344</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,280</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">113,128</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">54,515</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,344</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,335</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,154</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">47</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">3,332</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,154</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">47</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">4</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">119,095</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">33,744</td>
<td align="right">22.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">100,596</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">33,744</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">10,398</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">3,529</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">3,514</td>
<td align="right">2.3%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,597,180</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,395,161</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">38,658</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">9,504</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,620</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,213,485</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,284,713</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">349,915</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">81,508</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">40,746</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,768</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,529</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,693</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,486</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,408</td>
<td align="right">6.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,469</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,407</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">3,154</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,353</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,280</td>
<td align="right">6.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">39,436,013</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">21,702,379</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">19,236,280</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">14,107,645</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9,308,093</td>
<td align="right">5.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">98,280,448</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">17,401,625</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">9,633,564</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">8,608,505</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,470,980</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,847,633</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">715,324</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">12,529</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,224</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,558</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">741,803</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">724,606</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">610,368</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">240,506</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">201,666</td>
<td align="right">7.8%</td>
</tr>
</tbody>
</table>


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">10,297,552</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3,507,781</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">368,210</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">8,959</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,320</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">7,162,708</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,212,197</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,404,848</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,104,507</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">578,781</td>
<td align="right">4.1%</td>
</tr>
</tbody>
</table>


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,064</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,514</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">2,566</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,330</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,947</td>
<td align="right">8.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,462</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">3,781</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,506</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,427</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,139</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">943,698</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">831,734</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">688,183</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">501,065</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">370,660</td>
<td align="right">8.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">943,698</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">929,136</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">831,734</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">501,067</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">388,884</td>
<td align="right">8.7%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">295,682</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">383</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">323</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">97</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">295,693</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">555</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">268</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">97</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">22,183,241</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">456,300</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">11,583</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,737</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">5,502</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,702,379</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">498,171</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">451,006</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">21,497</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5,112</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CACHE</td>
<td align="right">1,522</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">671</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">404</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">160</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">64</td>
<td align="right">2.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,210</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">690</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">351</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">281</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">188</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,185,747</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">609,460</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">307,452</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">136,892</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">16,057</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,041,585</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">688,183</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">616,842</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">307,455</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">209,276</td>
<td align="right">4.9%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,837,752</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,199,444</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">309,876</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">86,021</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">36,963</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,170,012</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">211,135</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">49,484</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">35,117</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">25,149</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_EXTEND

<details>
<summary> Successors and predecessors for BINARY_OP_EXTEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">934,275</td>
<td align="right">84.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">147,214</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,461</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,835</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">789</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">894,905</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">147,679</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">53,000</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,830</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">510</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">7,422</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,349</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,288</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">318</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">27</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">7,422</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,349</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">682</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">319</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">303</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,883,434</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,691,158</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,029,230</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">642,554</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">401,336</td>
<td align="right">2.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,777,413</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,134,034</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,557,950</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">639,935</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">591,367</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_GETITEM </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">901,012</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">587,450</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">264,319</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">164,674</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">92,020</td>
<td align="right">4.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,999,810</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,927</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,793</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,890</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,741</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_LIST_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,611,944</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">275,457</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">90,869</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">42,770</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">37,734</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,382,480</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">863,605</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">268,211</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">99,840</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">93,996</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_STR_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,492,066</td>
<td align="right">74.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">684,789</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">76,792</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">49,726</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">49,726</td>
<td align="right">1.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,774,078</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,327,842</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">157,304</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">67,006</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">18,185</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_TUPLE_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,795,139</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">43</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">721,086</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">721,086</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">157,138</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">75,771</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">47,001</td>
<td align="right">2.6%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">42</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21</td>
<td align="right">33.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">63</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">874,272</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">383,743</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">235,452</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">146,046</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">93,107</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">821,812</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">264,612</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">152,506</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">146,047</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">90,869</td>
<td align="right">5.2%</td>
</tr>
</tbody>
</table>


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">398,085</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">355,918</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">82,885</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">15,550</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,576</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">534,759</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">313,874</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">19,990</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,751</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">6,355</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,897,072</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">95,974</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">24,831</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">11,702</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,510</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,839,063</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">110,943</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">95,934</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,980</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">27</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BOUND_METHOD_GENERAL

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">126</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">129</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">342,318</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">216,602</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">48,171</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">37,700</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">21,819</td>
<td align="right">2.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">377,362</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">198,228</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">65,276</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">37,700</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">22,706</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">5,918,827</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,876,228</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,558,396</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">194,199</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">169,264</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,601,281</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,412,104</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">299,740</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">209,975</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">176,811</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,041,900</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">303,711</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">146,046</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">26,750</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,218</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">768,421</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">598,645</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">158,659</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">15,793</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">8,191</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,483,858</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,987</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">3,533</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,420</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,395</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,250,605</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">642,554</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">405,823</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">73,407</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">41,934</td>
<td align="right">1.7%</td>
</tr>
</tbody>
</table>


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">36,815,682</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">17,886,054</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,835,075</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,820,421</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,684,715</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">86,129,304</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">905,413</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">199</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW_BOUND_METHOD

<details>
<summary> Successors and predecessors for CALL_KW_BOUND_METHOD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">97</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">64</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">34</td>
<td align="right">34.7%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW_NON_PY

<details>
<summary> Successors and predecessors for CALL_KW_NON_PY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">480,803</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">374</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">201,545</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">195,057</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">71,871</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,947</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,171</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW_PY

<details>
<summary> Successors and predecessors for CALL_KW_PY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">4,642,112</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,355</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,723,002</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">890,559</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">15,062</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">14,843</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,367,432</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,666,313</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,547,859</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">49,842</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">39,754</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,516,115</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">754,088</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">750,835</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">552,428</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">383,743</td>
<td align="right">5.7%</td>
</tr>
</tbody>
</table>


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,225,775</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">721,086</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">265,607</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">127,804</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">101,249</td>
<td align="right">1.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,254,016</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,381,605</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">411,236</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">298,920</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">107,253</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,612,957</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,342,710</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,533,618</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,433,091</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">550,634</td>
<td align="right">5.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,340,107</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,527,224</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">747,787</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">741,591</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">464,470</td>
<td align="right">4.8%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,302,667</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,790,843</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,774,078</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,340,179</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">234,000</td>
<td align="right">3.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,241,163</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,658,354</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,055,098</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">304,162</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">225,916</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,908,802</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">32,698</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">5,486</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,567</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,472</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,364,026</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">781,200</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">295,678</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">227,902</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">78,745</td>
<td align="right">2.7%</td>
</tr>
</tbody>
</table>


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,658,354</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,115,440</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">180,633</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">93,877</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">80,203</td>
<td align="right">2.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,726,981</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">748,038</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">360,877</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">266,302</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">93,521</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>


</details>

### CALL_NON_PY_GENERAL

<details>
<summary> Successors and predecessors for CALL_NON_PY_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">10,961,735</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,634,531</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,272,969</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">894,905</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">500,457</td>
<td align="right">2.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,617,443</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,647,055</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,563,964</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,279,514</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">462,685</td>
<td align="right">2.6%</td>
</tr>
</tbody>
</table>


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">57,718,693</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">8,696,996</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,154,295</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,053,503</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,209,539</td>
<td align="right">2.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">48,704,530</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">34,928,973</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">259,953</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">84,657</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">56,576</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### CALL_PY_GENERAL

<details>
<summary> Successors and predecessors for CALL_PY_GENERAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,490,755</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,656,840</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,558,511</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">796,058</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">632,883</td>
<td align="right">3.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">15,495,088</td>
<td align="right">94.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">837,259</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">111,951</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">43,706</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,328</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">819,290</td>
<td align="right">72.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">277,311</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,590</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,373</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">638</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">324,538</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">295,995</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">295,678</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">107,834</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">60,543</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">32,061</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,160</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">383</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">293</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">190</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">32,063</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,578</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">799</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">431</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">293</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,627,010</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">676,104</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,313</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">70</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">5,680,985</td>
<td align="right">77.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">894,915</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">710,899</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">7,899</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,782</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">146,046</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">421</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">146,468</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,323,968</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,120,764</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">548,227</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">342,391</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">335,857</td>
<td align="right">6.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,692,519</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,128,946</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">109,130</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">82,630</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">65,342</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,940,838</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">585,150</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">333,679</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">295,678</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">266,604</td>
<td align="right">4.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,502,179</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,602,731</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">589,963</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,139</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">361</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP_DICT

<details>
<summary> Successors and predecessors for CONTAINS_OP_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,467,598</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,822,495</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">263,616</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">202,042</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">105,352</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,014,332</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,836,663</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,169,057</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,834</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,513</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP_SET

<details>
<summary> Successors and predecessors for CONTAINS_OP_SET </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">620,599</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">36,351</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">28,120</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,888</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,558</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">692,078</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,402</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,587</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">990</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">38,924,834</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">20,256,628</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,861,928</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">25,169</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">91</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">39,273,624</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">21,795,002</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">24</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">40,697,833</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">33,070,543</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">264,363</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">74,013</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">458</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">39,436,013</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">31,852,054</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,847,633</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">677,280</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">264,363</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,546,308</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">287,333</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,278</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">849,423</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">715,324</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">270,205</td>
<td align="right">14.7%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">23,156,118</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,495,115</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">264,363</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">65</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,236,280</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">12,850,110</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,548,258</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">264,363</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">12,529</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD_NO_JIT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_JIT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_ITER</td>
<td align="right">37,845,660</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">21,839,126</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">16,467,493</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,608,505</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">4,254,016</td>
<td align="right">4.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">40,697,833</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">23,156,118</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">20,256,628</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,514,599</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,019,971</td>
<td align="right">3.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,053,212</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">204,576</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">186,177</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">120,838</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">3,000</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,001,417</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,689,042</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,336,982</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">202,042</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">80,638</td>
<td align="right">1.4%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_CLASS_WITH_METACLASS_CHECK

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS_WITH_METACLASS_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,685,219</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,342</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">107</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">101</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">894,976</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">894,954</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">894,909</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,349</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">107,544,622</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,670,873</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,886,093</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,077,082</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">929,178</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">27,538,801</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">15,088,687</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,669,132</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,659,766</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,677,147</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">146,545</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">45,430</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">88,443</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">38,909</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">32,698</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">30,078</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,603</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">21,447,053</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,786,760</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,854,285</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,259,151</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,098,770</td>
<td align="right">2.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">17,759,557</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,071,120</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,610,848</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,908,802</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,342,710</td>
<td align="right">5.9%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">64,868,232</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,237,759</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,680,976</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,509,691</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">788,305</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">55,327,694</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,154,295</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">5,440,824</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,084,475</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,058,552</td>
<td align="right">3.9%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">27,583,977</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">954,040</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">168,042</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">12,418</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,418</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">11,407,091</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">6,820,421</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,136,172</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,989,747</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">954,040</td>
<td align="right">3.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,002</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,154</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">65</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">31</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,045</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,855</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,855</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">404</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">42</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">35,792,458</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,062,346</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,030,482</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">202,368</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">171,002</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">19,783,872</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,239,967</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,040,866</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,572,782</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,547,859</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,659,766</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,699,902</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,570,011</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">440,014</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">225,089</td>
<td align="right">1.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,606,544</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,855,951</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,231,751</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">913,664</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">889,877</td>
<td align="right">5.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,556,565</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,777,058</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,036,110</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">584,371</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">189,630</td>
<td align="right">1.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,982,787</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,684,715</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,597,393</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">894,913</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">584,444</td>
<td align="right">3.4%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,680,521</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">313,153</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">284,460</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">119,979</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">116,524</td>
<td align="right">4.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,195,881</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">414,910</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">278,710</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">225,119</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">135,705</td>
<td align="right">5.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_CONST_IMMORTAL

<details>
<summary> Successors and predecessors for LOAD_CONST_IMMORTAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_ITER</td>
<td align="right">37,483,272</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,762,598</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">15,545,048</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">14,817,331</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">13,489,930</td>
<td align="right">9.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">79,085,358</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">15,545,048</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,652,390</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,755,756</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">5,918,827</td>
<td align="right">4.1%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_CONST_MORTAL

<details>
<summary> Successors and predecessors for LOAD_CONST_MORTAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">5,628,346</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,440,824</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,064,941</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">2,813,889</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,659,613</td>
<td align="right">8.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">11,525,446</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,642,112</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,451,727</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,875,007</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,194,656</td>
<td align="right">4.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">57,934,521</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">22,038,266</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">19,064,916</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,401,625</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,686,815</td>
<td align="right">4.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">67,476,382</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">43,293,050</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">17,886,054</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,876,807</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,590,513</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">28,281,603</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,470,980</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,421,623</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,764,272</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">6,218,913</td>
<td align="right">8.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">27,583,977</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">17,835,075</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,764,247</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,918,358</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,686,815</td>
<td align="right">7.6%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">158,375</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">30</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">157,893</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">512</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">246,234</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,220</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">179</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">118,233</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">48,271</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,070</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">33,343</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,222</td>
<td align="right">7.6%</td>
</tr>
</tbody>
</table>


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">48,704,530</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">39,661,152</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">39,527,035</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">21,795,002</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">15,495,088</td>
<td align="right">8.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">57,934,521</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">50,340,530</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">22,087,729</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">18,665,753</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">14,817,331</td>
<td align="right">8.2%</td>
</tr>
</tbody>
</table>


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,547</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,259</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,548</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,260</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,605,274</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,556,798</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">929,136</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">179,598</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">155,900</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,769,667</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,121,096</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,773,370</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,533,784</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,342,957</td>
<td align="right">6.2%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">483,664</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">337,059</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,419</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">52</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">295,887</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">250,981</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">174,921</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">59,200</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">39,805</td>
<td align="right">4.8%</td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">663,582</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">638,713</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,550</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,198</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,428</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">687,386</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">618,866</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">19,510</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">11,240</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,918</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,982,502</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,246,782</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">721,086</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">295,995</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">56,144</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,987,590</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,631,498</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">720,030</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">71,488</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,633</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">670,302</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">40,124</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,550</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,742</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">11</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">452,964</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">196,478</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">69,503</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,255</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,529</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,269,240</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">86,017</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">18,155</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">9,811</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">6,902</td>
<td align="right">0.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">689,110</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">605,265</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">86,737</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">9,749</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">384</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">86,129,304</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">34,001,460</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">5,412,104</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,882,624</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,409,759</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">118,286,842</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">22,471,669</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">97,096</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">11,226</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">384</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">3,516,115</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,250,605</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">231,361</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">201,843</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">138,362</td>
<td align="right">2.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,834,969</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,751,631</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">88,193</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">1,532</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">552</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">655,370</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">323,020</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">265,861</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">94,109</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">10,024</td>
<td align="right">0.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,143,005</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">186,891</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">21,373</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,756</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">218</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">COPY</td>
<td align="right">12,050,872</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,814,860</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,786,184</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">460,914</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">253,767</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">14,808,762</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,978,789</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">69,826</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">9,811</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">3,836</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,159,422</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">596,396</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">464,470</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">183,191</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">146,080</td>
<td align="right">3.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,458,719</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,200,070</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">67,007</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">47,678</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,817</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">83,388</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">704</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">320</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">75,135</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">8,959</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">320</td>
<td align="right">0.4%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,557,950</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">791,889</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">87,480</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">29,884</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">27,898</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,507,781</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">23,487</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,177</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">254</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">28</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,791,180</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,548,258</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,100,776</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">677,280</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">451,006</td>
<td align="right">4.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">10,297,552</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">498,971</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">194,230</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">251</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">102</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_LOCALS

<details>
<summary> Successors and predecessors for LOAD_LOCALS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">285</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">285</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### SETUP_ANNOTATIONS

<details>
<summary> Successors and predecessors for SETUP_ANNOTATIONS </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">107</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">10</td>
<td align="right">8.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">110</td>
<td align="right">94.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">6</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1</td>
<td align="right">0.9%</td>
</tr>
</tbody>
</table>


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">16</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">16</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### DELETE_NAME

<details>
<summary> Successors and predecessors for DELETE_NAME </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">4</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">3</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1</td>
<td align="right">11.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">3</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1</td>
<td align="right">11.1%</td>
</tr>
</tbody>
</table>


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">66</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">60</td>
<td align="right">47.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">66</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">59</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">7</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1</td>
<td align="right">10.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1</td>
<td align="right">10.0%</td>
</tr>
</tbody>
</table>


</details>


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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">11,335,199</td>
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
<td align="right">52,169,713</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,366,802</td>
<td align="right">3.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">46,337</td>
<td align="right">77.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">13,658</td>
<td align="right">22.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">remainder</td>
<td align="right">3,402</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,632</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,349</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,492</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">746</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">698</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">535</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">272</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">254</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">243</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">196</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">120</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">116</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">92</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">88</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">66</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">46</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">1</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">3,508,317</td>
<td align="right">100.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">1,863,669</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">239,481,195</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,885,023</td>
<td align="right">0.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">59,496</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">init not simple</td>
<td align="right">424</td>
<td align="right">424 / 0 !!</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">24</td>
<td align="right">24 / 0 !!</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">383</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">64</td>
<td align="right">3.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">1,730</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">637,200</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,928,794</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,056</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">1,345</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,658</td>
<td align="right">66.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">different types</td>
<td align="right">1,802</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">259</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">256</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">155</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">97</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">43</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">23</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">21</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">4,479,727</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,734,038</td>
<td align="right">72.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">527</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,039</td>
<td align="right">90.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">str</td>
<td align="right">2,193</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,493</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">731</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">622</td>
<td align="right">12.3%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">13,595,587</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">144,903,381</td>
<td align="right">77.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,023,583</td>
<td align="right">15.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">529,373</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,422</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">seq iter</td>
<td align="right">1,788</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,652</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">794</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">592</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">468</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">351</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">297</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">272</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">97</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">51</td>
<td align="right">0.8%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">generator</td>
<td align="right">39,447,686</td>
<td align="right">39,447,686 / 0 !!</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">24,403,667</td>
<td align="right">24,403,667 / 0 !!</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">21,180,766</td>
<td align="right">21,180,766 / 0 !!</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,653,723</td>
<td align="right">3,653,723 / 0 !!</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">926,862</td>
<td align="right">926,862 / 0 !!</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">149,321</td>
<td align="right">149,321 / 0 !!</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">87,710</td>
<td align="right">87,710 / 0 !!</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">32,900</td>
<td align="right">32,900 / 0 !!</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,729</td>
<td align="right">1,729 / 0 !!</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">48,435,478</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">64,390</td>
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
<td align="right">215,534,471</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">140,838,719</td>
<td align="right">34.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">2,660,388</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">181,758</td>
<td align="right">6.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">method</td>
<td align="right">3,246</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,852</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,314</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">993</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">764</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">646</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">323</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">129</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">71</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">66</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">2</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">2,781</td>
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
<td align="right">51</td>
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
<td align="right">212,304,364</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">11,889</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">19,273</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">50</td>
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
<td align="right">425,038</td>
<td align="right">99.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">209</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">4,490</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,810</td>
<td align="right">70.4%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">4</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">47</td>
<td align="right">92.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">list</td>
<td align="right">47</td>
<td align="right">100.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">10,035,248</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,055,521</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,609,951</td>
<td align="right">28.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">185,983</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,803</td>
<td align="right">5.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">other</td>
<td align="right">170,810</td>
<td align="right">1,742.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">5,037</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,626</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">643</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">311</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">290</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">119</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">1</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">196,240</td>
<td align="right">100.0%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">1,666,035</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,156,519</td>
<td align="right">84.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">473</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,521</td>
<td align="right">88.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">py simple</td>
<td align="right">2,961</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">341</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">113</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">59</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">47</td>
<td align="right">1.3%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">15,193,122</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">168,591,152</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,516,611</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">107,951</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">147,642</td>
<td align="right">57.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">number</td>
<td align="right">134,241</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,949</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,081</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">902</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">244</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">118</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">107</td>
<td align="right">0.1%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">296,267</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,609,247</td>
<td align="right">98.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">380</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97</td>
<td align="right">20.3%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sequence</td>
<td align="right">74</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">23</td>
<td align="right">23.7%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
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
<td align="right">1,903,920,269</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">200,117,767</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,579,441,202</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">188,262,431</td>
<td align="right">4.9%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">48,435,478</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15,193,122</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">13,595,587</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,335,199</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10,035,248</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,479,727</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,508,317</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,863,669</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,666,035</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">637,200</td>
<td align="right">0.6%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">55,576,202</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">42,021,198</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">23,518,033</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">14,012,245</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">14,011,338</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">10,348,677</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,554,980</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,690,802</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,462,159</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,342,046</td>
<td align="right">1.2%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,155,749</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">178,983,750</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,155,749</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,612,411</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">543,338</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">376</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,610,698</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">1,337</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">10,485,106</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">502,495</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">18,548,165</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">250</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">6,759,105</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,071,412</td>
<td align="right">72.1%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">154,046,034</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">154,020,563</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">131,826,011</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">130,344,963</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,419,037</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">62,011</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">142,710,777</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,079,888</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">867,864,405</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,258,659,297</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">885,863,450</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">748,034,289</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">126,462,747</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">87,495,860</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">625,414,755</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">540,265,318</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">997,135</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">98,881</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (str subclass)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">198,804,351</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">8,543,004</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">10,023,705</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">156,302,933</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,482,447</td>
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
<th align="right">Collections</th>
<th align="right">Objects collected</th>
<th align="right">Object visits</th>
<th align="right">Reachable from roots</th>
<th align="right">Not reachable from roots</th>
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
</tr>
<tr>
<td align="right">1</td>
<td align="right">6,259</td>
<td align="right">13,097,598</td>
<td align="right">263,600,020</td>
<td align="right">16,204,341</td>
<td align="right">23,962,624</td>
</tr>
<tr>
<td align="right">2</td>
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
<th align="right">Count</th>
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
<td align="right">22,592</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">22</td>
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
</tr>
<tr>
<td align="left">
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">23</td>
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
<th align="right">Count</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Number of data files</td>
<td align="right">21</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-28
