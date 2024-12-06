
# Pystats results

- benchmark: sympy
- fork: brandtbucher
- ref: justin-cold-17
- commit hash: 06d5d2f
- commit date: 2024-12-05T14:57:01-08:00

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
<td align="left">LOAD_FAST</td>
<td align="right">594,167,039</td>
<td align="right">16.3%</td>
<td align="right">16.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">202,438,162</td>
<td align="right">5.6%</td>
<td align="right">21.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">182,152,988</td>
<td align="right">5.0%</td>
<td align="right">26.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">171,651,567</td>
<td align="right">4.7%</td>
<td align="right">31.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">170,412,369</td>
<td align="right">4.7%</td>
<td align="right">36.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">158,148,159</td>
<td align="right">4.3%</td>
<td align="right">40.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">140,520,149</td>
<td align="right">3.9%</td>
<td align="right">44.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">114,620,224</td>
<td align="right">3.1%</td>
<td align="right">47.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">103,799,735</td>
<td align="right">2.9%</td>
<td align="right">50.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">98,038,508</td>
<td align="right">2.7%</td>
<td align="right">53.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">84,786,410</td>
<td align="right">2.3%</td>
<td align="right">55.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">71,616,659</td>
<td align="right">2.0%</td>
<td align="right">57.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">60,711,996</td>
<td align="right">1.7%</td>
<td align="right">59.1%</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">60,398,260</td>
<td align="right">1.7%</td>
<td align="right">60.8%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">60,055,004</td>
<td align="right">1.6%</td>
<td align="right">62.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">55,854,628</td>
<td align="right">1.5%</td>
<td align="right">64.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">54,276,941</td>
<td align="right">1.5%</td>
<td align="right">65.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">49,757,996</td>
<td align="right">1.4%</td>
<td align="right">66.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">43,971,060</td>
<td align="right">1.2%</td>
<td align="right">68.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">43,425,894</td>
<td align="right">1.2%</td>
<td align="right">69.2%</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">42,951,342</td>
<td align="right">1.2%</td>
<td align="right">70.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">42,392,738</td>
<td align="right">1.2%</td>
<td align="right">71.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">41,904,838</td>
<td align="right">1.2%</td>
<td align="right">72.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,133,026</td>
<td align="right">1.1%</td>
<td align="right">73.9%</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">39,264,093</td>
<td align="right">1.1%</td>
<td align="right">74.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,907,981</td>
<td align="right">1.0%</td>
<td align="right">75.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,612,330</td>
<td align="right">0.9%</td>
<td align="right">76.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,847,964</td>
<td align="right">0.9%</td>
<td align="right">77.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">30,250,718</td>
<td align="right">0.8%</td>
<td align="right">78.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">29,881,107</td>
<td align="right">0.8%</td>
<td align="right">79.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">29,764,915</td>
<td align="right">0.8%</td>
<td align="right">80.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,280,192</td>
<td align="right">0.7%</td>
<td align="right">80.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">25,975,164</td>
<td align="right">0.7%</td>
<td align="right">81.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">24,002,293</td>
<td align="right">0.7%</td>
<td align="right">82.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">22,308,091</td>
<td align="right">0.6%</td>
<td align="right">82.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">21,976,856</td>
<td align="right">0.6%</td>
<td align="right">83.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">21,740,608</td>
<td align="right">0.6%</td>
<td align="right">84.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,093,627</td>
<td align="right">0.6%</td>
<td align="right">84.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">20,337,202</td>
<td align="right">0.6%</td>
<td align="right">85.3%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">19,843,110</td>
<td align="right">0.5%</td>
<td align="right">85.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">18,697,178</td>
<td align="right">0.5%</td>
<td align="right">86.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">18,591,646</td>
<td align="right">0.5%</td>
<td align="right">86.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,922,788</td>
<td align="right">0.5%</td>
<td align="right">87.3%</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,838,662</td>
<td align="right">0.5%</td>
<td align="right">87.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">17,717,083</td>
<td align="right">0.5%</td>
<td align="right">88.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">17,532,527</td>
<td align="right">0.5%</td>
<td align="right">88.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">17,508,411</td>
<td align="right">0.5%</td>
<td align="right">89.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">16,299,324</td>
<td align="right">0.4%</td>
<td align="right">89.7%</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">15,950,813</td>
<td align="right">0.4%</td>
<td align="right">90.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">15,912,013</td>
<td align="right">0.4%</td>
<td align="right">90.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">15,909,429</td>
<td align="right">0.4%</td>
<td align="right">91.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,567,699</td>
<td align="right">0.4%</td>
<td align="right">91.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">15,511,628</td>
<td align="right">0.4%</td>
<td align="right">91.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">15,281,559</td>
<td align="right">0.4%</td>
<td align="right">92.3%</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">15,113,147</td>
<td align="right">0.4%</td>
<td align="right">92.7%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">12,947,822</td>
<td align="right">0.4%</td>
<td align="right">93.1%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">12,797,310</td>
<td align="right">0.4%</td>
<td align="right">93.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">12,121,673</td>
<td align="right">0.3%</td>
<td align="right">93.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,106,796</td>
<td align="right">0.3%</td>
<td align="right">94.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,876,982</td>
<td align="right">0.3%</td>
<td align="right">94.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,856,974</td>
<td align="right">0.3%</td>
<td align="right">94.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,500,393</td>
<td align="right">0.3%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,938,980</td>
<td align="right">0.3%</td>
<td align="right">95.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">7,555,511</td>
<td align="right">0.2%</td>
<td align="right">95.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">7,516,861</td>
<td align="right">0.2%</td>
<td align="right">95.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,744,250</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,642,819</td>
<td align="right">0.2%</td>
<td align="right">96.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,622,531</td>
<td align="right">0.2%</td>
<td align="right">96.2%</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">6,589,483</td>
<td align="right">0.2%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,227,978</td>
<td align="right">0.2%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,035,326</td>
<td align="right">0.2%</td>
<td align="right">96.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,752,970</td>
<td align="right">0.2%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">5,567,157</td>
<td align="right">0.2%</td>
<td align="right">97.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,075,362</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,046,165</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,952,092</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,609,853</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,588,113</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,587,451</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,497,182</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,469,386</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,181,630</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,728,179</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,550,078</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,438,886</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,431,368</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,431,183</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,703,686</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,675,966</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,588,170</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,281,101</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,199,903</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,195,132</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,069,667</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,966,484</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,787,313</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,758,866</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,754,443</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,521,722</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,389,693</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,323,166</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,288,053</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,244,520</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,222,092</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,036,043</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,028,972</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,028,367</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,593</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">881,038</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">746,307</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">745,901</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">655,055</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">655,055</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">655,055</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">642,624</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">642,608</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">597,612</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">493,601</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">456,491</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">427,555</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">389,890</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">389,282</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">372,870</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">338,565</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">270,096</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">178,536</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">178,534</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">175,266</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">172,018</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,655</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">147,596</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">141,391</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">133,724</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">89,010</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">83,093</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">78,656</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">40,227</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">36,459</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">20,682</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">18,052</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">17,016</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">14,629</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">9,212</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">8,958</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,941</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">8,858</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,742</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,961</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,645</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,679</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,455</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,444</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,055</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">591</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">447</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">394</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">255</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">133</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">127</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">102</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">92</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">1</td>
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
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">116,642,252</td>
<td align="right">3.2%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">110,121,834</td>
<td align="right">3.0%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">80,832,316</td>
<td align="right">2.2%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">77,326,896</td>
<td align="right">2.1%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">74,394,626</td>
<td align="right">2.0%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">69,687,748</td>
<td align="right">1.9%</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">68,455,138</td>
<td align="right">1.9%</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_SLOT</td>
<td align="right">58,977,388</td>
<td align="right">1.6%</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">50,732,282</td>
<td align="right">1.4%</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">41,112,626</td>
<td align="right">1.1%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN</td>
<td align="right">40,754,922</td>
<td align="right">1.1%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">40,190,175</td>
<td align="right">1.1%</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">38,980,634</td>
<td align="right">1.1%</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">38,672,330</td>
<td align="right">1.1%</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST_IMMORTAL</td>
<td align="right">38,345,469</td>
<td align="right">1.1%</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR RETURN_VALUE</td>
<td align="right">37,159,480</td>
<td align="right">1.0%</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">34,110,212</td>
<td align="right">0.9%</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST RETURN_VALUE</td>
<td align="right">33,836,571</td>
<td align="right">0.9%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">32,582,254</td>
<td align="right">0.9%</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT TO_BOOL_BOOL</td>
<td align="right">32,086,712</td>
<td align="right">0.9%</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">31,499,253</td>
<td align="right">0.9%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">31,343,612</td>
<td align="right">0.9%</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">31,277,429</td>
<td align="right">0.9%</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">27,643,607</td>
<td align="right">0.8%</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER</td>
<td align="right">26,256,840</td>
<td align="right">0.7%</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL RETURN_VALUE</td>
<td align="right">25,695,830</td>
<td align="right">0.7%</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST</td>
<td align="right">25,486,214</td>
<td align="right">0.7%</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">24,191,736</td>
<td align="right">0.7%</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE CALL_ISINSTANCE</td>
<td align="right">24,187,524</td>
<td align="right">0.7%</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">22,776,232</td>
<td align="right">0.6%</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">22,540,513</td>
<td align="right">0.6%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">IS_OP POP_JUMP_IF_FALSE</td>
<td align="right">22,274,168</td>
<td align="right">0.6%</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST GET_ITER</td>
<td align="right">21,940,083</td>
<td align="right">0.6%</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR STORE_FAST</td>
<td align="right">21,817,561</td>
<td align="right">0.6%</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR</td>
<td align="right">21,709,363</td>
<td align="right">0.6%</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST</td>
<td align="right">21,651,147</td>
<td align="right">0.6%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_LEN</td>
<td align="right">21,070,375</td>
<td align="right">0.6%</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP STORE_FAST</td>
<td align="right">19,398,563</td>
<td align="right">0.5%</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_PROPERTY</td>
<td align="right">19,281,481</td>
<td align="right">0.5%</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL CALL_BUILTIN_FAST</td>
<td align="right">18,759,833</td>
<td align="right">0.5%</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST</td>
<td align="right">18,567,565</td>
<td align="right">0.5%</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">18,383,968</td>
<td align="right">0.5%</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT STORE_FAST</td>
<td align="right">17,917,188</td>
<td align="right">0.5%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">17,612,868</td>
<td align="right">0.5%</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_CONST_IMMORTAL</td>
<td align="right">17,329,370</td>
<td align="right">0.5%</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE INTERPRETER_EXIT</td>
<td align="right">17,205,805</td>
<td align="right">0.5%</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST COMPARE_OP</td>
<td align="right">16,904,907</td>
<td align="right">0.5%</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_CONST_IMMORTAL</td>
<td align="right">16,794,779</td>
<td align="right">0.5%</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST</td>
<td align="right">16,725,115</td>
<td align="right">0.5%</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,642,069</td>
<td align="right">0.5%</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT</td>
<td align="right">16,498,968</td>
<td align="right">0.5%</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS</td>
<td align="right">16,247,156</td>
<td align="right">0.4%</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">15,560,422</td>
<td align="right">0.4%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE RETURN_VALUE</td>
<td align="right">15,304,086</td>
<td align="right">0.4%</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">POP_TOP ENTER_EXECUTOR</td>
<td align="right">15,085,268</td>
<td align="right">0.4%</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_SUBSCR_LIST_INT</td>
<td align="right">14,829,318</td>
<td align="right">0.4%</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT RETURN_VALUE</td>
<td align="right">14,580,345</td>
<td align="right">0.4%</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_INT</td>
<td align="right">14,566,206</td>
<td align="right">0.4%</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_BOOL</td>
<td align="right">14,490,852</td>
<td align="right">0.4%</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS RESUME_CHECK</td>
<td align="right">14,416,969</td>
<td align="right">0.4%</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST BUILD_TUPLE</td>
<td align="right">14,302,600</td>
<td align="right">0.4%</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK NOP</td>
<td align="right">14,214,376</td>
<td align="right">0.4%</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,953,796</td>
<td align="right">0.4%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE</td>
<td align="right">12,894,402</td>
<td align="right">0.4%</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE CALL_FUNCTION_EX</td>
<td align="right">12,797,310</td>
<td align="right">0.4%</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP LOAD_FAST</td>
<td align="right">12,727,219</td>
<td align="right">0.3%</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST DICT_MERGE</td>
<td align="right">12,699,302</td>
<td align="right">0.3%</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST LOAD_FAST</td>
<td align="right">12,166,601</td>
<td align="right">0.3%</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">12,096,082</td>
<td align="right">0.3%</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT COMPARE_OP_INT</td>
<td align="right">11,940,092</td>
<td align="right">0.3%</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">11,825,375</td>
<td align="right">0.3%</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_LIST_APPEND</td>
<td align="right">11,820,234</td>
<td align="right">0.3%</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">11,767,607</td>
<td align="right">0.3%</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK POP_TOP</td>
<td align="right">11,709,937</td>
<td align="right">0.3%</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">11,589,478</td>
<td align="right">0.3%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP POP_JUMP_IF_FALSE</td>
<td align="right">11,489,771</td>
<td align="right">0.3%</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">11,348,644</td>
<td align="right">0.3%</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND ENTER_EXECUTOR</td>
<td align="right">11,309,133</td>
<td align="right">0.3%</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR IS_OP</td>
<td align="right">11,266,895</td>
<td align="right">0.3%</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">POP_TOP RESUME_CHECK</td>
<td align="right">11,113,871</td>
<td align="right">0.3%</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST TO_BOOL_BOOL</td>
<td align="right">10,921,035</td>
<td align="right">0.3%</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST</td>
<td align="right">10,857,868</td>
<td align="right">0.3%</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_TYPE_1</td>
<td align="right">10,809,286</td>
<td align="right">0.3%</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">CACHE POP_TOP</td>
<td align="right">10,788,894</td>
<td align="right">0.3%</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST_IMMORTAL</td>
<td align="right">10,775,096</td>
<td align="right">0.3%</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">10,644,731</td>
<td align="right">0.3%</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR POP_JUMP_IF_FALSE</td>
<td align="right">10,459,006</td>
<td align="right">0.3%</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS RESUME_CHECK</td>
<td align="right">10,346,614</td>
<td align="right">0.3%</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL STORE_FAST</td>
<td align="right">10,327,961</td>
<td align="right">0.3%</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST LOAD_FAST</td>
<td align="right">10,232,875</td>
<td align="right">0.3%</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">IS_OP YIELD_VALUE</td>
<td align="right">10,202,901</td>
<td align="right">0.3%</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST IS_OP</td>
<td align="right">10,199,498</td>
<td align="right">0.3%</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE STORE_FAST</td>
<td align="right">10,137,717</td>
<td align="right">0.3%</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS GET_ITER</td>
<td align="right">9,958,665</td>
<td align="right">0.3%</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX STORE_FAST</td>
<td align="right">9,906,438</td>
<td align="right">0.3%</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">CACHE COPY_FREE_VARS</td>
<td align="right">9,861,399</td>
<td align="right">0.3%</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_BUILTIN_FAST</td>
<td align="right">9,648,804</td>
<td align="right">0.3%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BUILD_MAP</td>
<td align="right">9,581,782</td>
<td align="right">0.3%</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">9,574,730</td>
<td align="right">0.3%</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_FAST</td>
<td align="right">9,389,160</td>
<td align="right">0.3%</td>
<td align="right">65.1%</td>
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
<td align="right">5,135</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,151</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">316</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">256</td>
<td align="right">2.9%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">3,291</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,611</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,144</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">704</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">528</td>
<td align="right">6.0%</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">591</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">591</td>
<td align="right">100.0%</td>
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
<td align="right">68,455,138</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">10,788,894</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">9,861,399</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">7,932,728</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,153,160</td>
<td align="right">1.2%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

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
<td align="left">LOAD_DEREF</td>
<td align="right">2,869,113</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,385,948</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,209,544</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">541,515</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">312,415</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">2,661,638</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,064,998</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,061,630</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">736,081</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">510,905</td>
<td align="right">6.8%</td>
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
<td align="right">491,072</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">110,887</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">51,764</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,295</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">37</td>
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
<td align="right">654,927</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">128</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">960</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">95</td>
<td align="right">9.0%</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">960</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">92</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3</td>
<td align="right">0.3%</td>
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
<td align="right">17,016</td>
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
<td align="left">POP_TOP</td>
<td align="right">17,016</td>
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
<td align="right">237,680</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">127,962</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">7,228</td>
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
<td align="left">POP_TOP</td>
<td align="right">372,870</td>
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
<td align="right">642,608</td>
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
<td align="right">642,608</td>
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
<td align="right">178,534</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
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
<td align="left">BUILD_STRING</td>
<td align="right">88,881</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">86,248</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,406</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">21,940,083</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">9,958,665</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">7,314,748</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,514,732</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,304,024</td>
<td align="right">5.9%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">26,256,840</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">8,361,632</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">8,092,557</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">6,514,732</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,064,196</td>
<td align="right">7.3%</td>
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
<td align="right">247,965</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">141,545</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">376</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">389,890</td>
<td align="right">100.0%</td>
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
<td align="right">80,832,316</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">17,205,805</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">387</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">4,952,092</td>
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
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,430,211</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">714,630</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">497,583</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">287,613</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,282</td>
<td align="right">0.1%</td>
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
<td align="right">14,214,376</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,305,253</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,752,193</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,133,046</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,064,488</td>
<td align="right">4.8%</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">8,168,311</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,103,586</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,073,637</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">696,770</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">694,674</td>
<td align="right">3.1%</td>
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
<td align="left">SWAP</td>
<td align="right">323,774</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">237,026</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">92,498</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,551</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">128</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">323,774</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">120,283</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">109,451</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">63,281</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">35,747</td>
<td align="right">5.5%</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">11,709,937</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">10,788,894</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">7,723,862</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,307,099</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,594,056</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">15,085,268</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">11,113,871</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,211,269</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,258,359</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4,024,734</td>
<td align="right">7.4%</td>
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
<td align="left">BINARY_SUBSCR</td>
<td align="right">249,464</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">162,998</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">80,232</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">63,905</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">42,126</td>
<td align="right">6.4%</td>
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
<td align="right">573,220</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">80,408</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,295</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">132</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">9,270,937</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,086,759</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,549,908</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,034,833</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">942,593</td>
<td align="right">3.9%</td>
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
<td align="right">18,383,968</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,757,488</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">716,430</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">101,924</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">13,447</td>
<td align="right">0.1%</td>
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
<td align="left">COPY_FREE_VARS</td>
<td align="right">3,053,370</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,804,754</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">130,501</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">81,114</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">5,066</td>
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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,265,762</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">706,534</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">624,963</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">247,965</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">127,991</td>
<td align="right">2.5%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">37,159,480</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">33,836,571</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">25,695,830</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">15,304,086</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">14,580,345</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">80,832,316</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">31,277,429</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">15,560,422</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">11,589,478</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,307,099</td>
<td align="right">4.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">856,399</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,011</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">4,660</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,463</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,135</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">847,133</td>
<td align="right">96.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">22,111</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,735</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,811</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,320</td>
<td align="right">0.1%</td>
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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">8,230,028</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,466,401</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">94,633</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">62,398</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">17,819</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">9,574,730</td>
<td align="right">96.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">278,834</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">65,861</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">8,673</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,303</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">144,867</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">93,950</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">85,473</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">85,003</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">40,391</td>
<td align="right">8.8%</td>
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
<td align="right">105,269</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">90,190</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">85,640</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">84,943</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">45,872</td>
<td align="right">10.0%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">2,703,801</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">890,925</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">521,035</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">65,861</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">8</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">2,768,473</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">703,169</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">587,854</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">63,269</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">54,394</td>
<td align="right">1.3%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,383,399</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">5,084,091</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,998,315</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">3,724,751</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,343,487</td>
<td align="right">4.9%</td>
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
<td align="right">19,398,563</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,469,638</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">831,843</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">680,230</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">598,115</td>
<td align="right">2.2%</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,262,356</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,032,224</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,769,892</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,493,010</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,241,508</td>
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
<td align="left">STORE_FAST</td>
<td align="right">9,180,341</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,769,892</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,549,052</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,073,396</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">593,840</td>
<td align="right">3.7%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">9,581,782</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,824,100</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,730,398</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">988,851</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">703,112</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">12,727,219</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,730,398</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,621,501</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,244,666</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">587,982</td>
<td align="right">2.8%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">25,721</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">14,442</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">64</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">25,721</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">14,442</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">64</td>
<td align="right">0.2%</td>
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
<td align="right">88,881</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">129</td>
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
<td align="right">84,943</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,451</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">800</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">800</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">15</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">14,302,600</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,492,758</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,991,076</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,990,910</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,931,693</td>
<td align="right">5.9%</td>
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
<td align="right">15,304,086</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">3,824,100</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,724,741</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,429,212</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,554,036</td>
<td align="right">7.8%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">17,173</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,497</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,228</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,475</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,364</td>
<td align="right">3.7%</td>
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
<td align="right">6,321</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,091</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,227</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,207</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,479</td>
<td align="right">4.1%</td>
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
<td align="left">DICT_MERGE</td>
<td align="right">12,797,310</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,159,324</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,157,186</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">958,440</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">587,982</td>
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
<td align="left">STORE_FAST</td>
<td align="right">9,906,438</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">9,242,531</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,244,327</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">510,706</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">336,075</td>
<td align="right">1.5%</td>
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
<td align="right">1,028,306</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">53</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">8</td>
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
<td align="right">958,440</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">69,874</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">53</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">1,444</td>
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
<td align="left">CALL_KW_PY</td>
<td align="right">620</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">403</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">84</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">59</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">50</td>
<td align="right">3.5%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">16,904,907</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,421,324</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,223,110</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">923,125</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">505,401</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,489,771</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,998,315</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,998,311</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">2,703,801</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,542,997</td>
<td align="right">5.9%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,859,189</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,003,902</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">476,696</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">100,038</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">87,235</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,561,694</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">20,113</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,818</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">132</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">88,570</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">88,139</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,806</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">FORMAT_SIMPLE</td>
<td align="right">178,534</td>
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
<td align="left">COPY</td>
<td align="right">899,476</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">892,261</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">644,488</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">420,037</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">174,694</td>
<td align="right">4.9%</td>
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
<td align="right">950,257</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">899,476</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">894,714</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">669,164</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">43,071</td>
<td align="right">1.2%</td>
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
<td align="left">CACHE</td>
<td align="right">9,861,399</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,496,820</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,682,815</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">901,155</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">200,176</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">14,416,969</td>
<td align="right">82.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,053,370</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">62,080</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">108</td>
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
<td align="left">FOR_ITER</td>
<td align="right">1,022,618</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">12,586</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">704</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7</td>
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
<td align="right">512,003</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">511,309</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,593</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">10</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">12,699,302</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">98,008</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">12,797,310</td>
<td align="right">100.0%</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,819,009</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,354,406</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,890,741</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,758,358</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,368,109</td>
<td align="right">11.3%</td>
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
<td align="right">5,060,452</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,694,603</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,394,078</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,032,506</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">511,301</td>
<td align="right">4.2%</td>
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
<td align="left">GET_ITER</td>
<td align="right">26,256,840</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">7,003,548</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">297,367</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">37,887</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">6,946</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">22,540,513</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,231,867</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,970,941</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,653,321</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,634,815</td>
<td align="right">4.9%</td>
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
<td align="right">5,752,894</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">689,613</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">145,549</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">127</td>
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
<td align="right">4,925,473</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,661,980</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,903</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">127</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">5,752,947</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
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
<td align="left">IMPORT_FROM</td>
<td align="right">5,752,894</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">53</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">11,266,895</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">10,199,498</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,429,514</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,739,884</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">84,943</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">22,274,168</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">10,202,901</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,404,403</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">12,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,456</td>
<td align="right">0.0%</td>
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
<td align="right">3,423,470</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,377,368</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">3,011,300</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,394,078</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,450,859</td>
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
<td align="left">FOR_ITER</td>
<td align="right">7,003,548</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,202,652</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,278,843</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,354,406</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">964,059</td>
<td align="right">5.2%</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">625,123</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">109,451</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">11,319</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">8</td>
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
<td align="left">SEND_GEN</td>
<td align="right">487,031</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">138,100</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">85,117</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">20,139</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,542</td>
<td align="right">1.8%</td>
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
<td align="right">3,370,173</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">495,801</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">192,735</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">153,540</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">114,492</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">3,175,075</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">488,680</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">346,237</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">327,403</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">94,695</td>
<td align="right">2.1%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,144,638</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">605,287</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">291,358</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">51,220</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">30,468</td>
<td align="right">1.4%</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,159,177</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,040,478</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">8</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,027,720</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">666</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">394</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,028,306</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">527</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">34,110,212</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,709,363</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,883,802</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,829,090</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">221,897</td>
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
<td align="right">21,817,561</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">11,266,895</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">10,857,868</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,549,908</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,493,822</td>
<td align="right">4.2%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,305,250</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">5,753,482</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,429,212</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">694,674</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">595,533</td>
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
<td align="left">CALL_KW_PY</td>
<td align="right">7,516,220</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,752,947</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,952,092</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">597,209</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">312,415</td>
<td align="right">1.6%</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">8,747,718</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">8,168,311</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,543,264</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,920,073</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,869,113</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">9,270,937</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,885,511</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,352,597</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,869,113</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,729,031</td>
<td align="right">7.0%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">116,642,252</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">110,121,834</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">74,394,626</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">69,687,748</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">25,486,214</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">58,977,388</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">50,732,282</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">41,112,626</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">38,980,634</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">38,345,469</td>
<td align="right">6.5%</td>
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
<td align="right">6,514,732</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">5,362,246</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
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
<td align="left">SWAP</td>
<td align="right">6,514,728</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">5,362,246</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">8</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,239,909</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,456</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,028</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">320</td>
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
<td align="right">1,239,905</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,708</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,160</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">864</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">368</td>
<td align="right">0.0%</td>
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
<td align="right">27,643,607</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">18,567,565</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">16,725,115</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">11,825,375</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">9,231,790</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">16,904,907</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">16,498,968</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">14,829,318</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">14,302,600</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">9,648,804</td>
<td align="right">6.9%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,483</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,983</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,580</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,635</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">875</td>
<td align="right">4.8%</td>
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
<td align="right">8,832</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,685</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,992</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">710</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">494</td>
<td align="right">2.7%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,425,609</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,751,964</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">5,354,115</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,451,769</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,771,054</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">11,940,092</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,307,616</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,670,928</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,753,482</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,598,963</td>
<td align="right">6.1%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">54</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">6</td>
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
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">25</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">16</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">5</td>
<td align="right">8.3%</td>
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
<td align="right">1,782,087</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">1,153,160</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">541,541</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">491,118</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">407,390</td>
<td align="right">9.1%</td>
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
<td align="right">2,714,801</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,782,087</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">266</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">4</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,725,601</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,561</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">575</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">95</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,432,935</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">295,227</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">17</td>
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
<td align="right">77,326,896</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">22,274,168</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">17,612,868</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">11,489,771</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,459,006</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">74,394,626</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">40,754,922</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">16,725,115</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">10,775,096</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,425,609</td>
<td align="right">4.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">3,115,594</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,061,630</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">861,752</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">5,333</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">768</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,834,754</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,064,986</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">865,205</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">643,291</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">473,932</td>
<td align="right">9.4%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">16,642,069</td>
<td align="right">95.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">717,799</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">142,480</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,945</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,663</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">9,323,530</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,305,553</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,398,977</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,014,836</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">222,245</td>
<td align="right">1.3%</td>
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
<td align="right">32,582,254</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">7,127,969</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,038,970</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,404,403</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,542,997</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">25,486,214</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,271,572</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,526,067</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,377,368</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,305,253</td>
<td align="right">6.6%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">81,778</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,294</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">13</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">8</td>
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
<td align="left">PUSH_EXC_INFO</td>
<td align="right">80,232</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,423</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">128</td>
<td align="right">0.2%</td>
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
<td align="right">1,551</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">128</td>
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
<td align="left">PUSH_EXC_INFO</td>
<td align="right">256</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">128</td>
<td align="right">33.3%</td>
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
<td align="right">138,100</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">130,888</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">836</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">272</td>
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
<td align="right">132,407</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">127,962</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,689</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,928</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">836</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">12,947</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,680</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">14,629</td>
<td align="right">100.0%</td>
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
<td align="right">3,430,211</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,157</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">3,023,180</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">229,563</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">81,201</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">32,013</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">26,087</td>
<td align="right">0.8%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">164,910</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,825</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,552</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">979</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">80,522</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">80,401</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,503</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,763</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,153</td>
<td align="right">0.7%</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,023,628</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,661,980</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,195,204</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">188,974</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">81,201</td>
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
<td align="right">3,023,383</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,516,431</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,026,425</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">336,987</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">145,549</td>
<td align="right">2.3%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">31,277,429</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">21,817,561</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">19,398,563</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">17,917,188</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">10,327,961</td>
<td align="right">5.1%</td>
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
<td align="right">116,642,252</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">27,643,607</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">24,191,736</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,689,170</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,236,018</td>
<td align="right">2.1%</td>
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
<td align="right">1,321,181</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">430,347</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">19,596</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">16,189</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,204,468</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">218,036</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">197,526</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">101,805</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">18,592</td>
<td align="right">1.0%</td>
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
<td align="right">38,672,330</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,560,928</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,132,561</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">605,665</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">330,550</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">12,166,601</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,825,375</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">8,747,718</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,661,288</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">910,377</td>
<td align="right">2.1%</td>
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
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,099</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,903</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,086</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,080</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">947</td>
<td align="right">10.3%</td>
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
<td align="right">2,301</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,093</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,300</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,086</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,044</td>
<td align="right">11.3%</td>
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
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,391,698</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">6,514,728</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,733,601</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">3,730,398</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,769,892</td>
<td align="right">9.2%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,391,829</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,514,732</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,594,056</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">3,730,398</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,769,892</td>
<td align="right">9.2%</td>
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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,590</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,561</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,512</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,159</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">502</td>
<td align="right">5.6%</td>
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
<td align="right">4,744</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,895</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,476</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">376</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">313</td>
<td align="right">3.5%</td>
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
<td align="left">IS_OP</td>
<td align="right">10,202,901</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,232,966</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,289,673</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">873,319</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">502,533</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">17,205,805</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">502,533</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">128,122</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">156</td>
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
<td align="right">1,218</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">570</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">436</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">266</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">198</td>
<td align="right">6.7%</td>
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
<td align="right">1,027</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">549</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">487</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">322</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">185</td>
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
<td align="right">2,598,963</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">402,022</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">311,496</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">62,861</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">34,608</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,230,980</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">923,132</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">774,989</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">159,987</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">110,025</td>
<td align="right">3.2%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">336,283</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">31,720</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">16,888</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,350</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,293</td>
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
<td align="right">352,154</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">33,419</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,556</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">455</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">336</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,327,207</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">579,264</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">213,836</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">74,692</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">129</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,827,693</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">144,958</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">137,000</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">59,760</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">19,981</td>
<td align="right">0.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">383</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">64</td>
<td align="right">14.3%</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">254</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">193</td>
<td align="right">43.2%</td>
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
<td align="right">1,114,170</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">476,383</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">144,956</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,556</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,619</td>
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
<td align="left">SWAP</td>
<td align="right">791,041</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">553,327</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">247,485</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">121,990</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">10,705</td>
<td align="right">0.6%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

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
<td align="right">930,687</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">721,980</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">511,732</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">328,260</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">93,047</td>
<td align="right">3.6%</td>
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
<td align="right">693,004</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">642,507</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">311,496</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">296,436</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">254,570</td>
<td align="right">9.8%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

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
<td align="right">10,425</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,024</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,984</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,744</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,449</td>
<td align="right">7.0%</td>
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
<td align="left">MAKE_CELL</td>
<td align="right">20,682</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

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
<td align="right">16,498,968</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">894,714</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">815,000</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">223,068</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">149,529</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,398,193</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">7,391,698</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,238,440</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">894,690</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">360,442</td>
<td align="right">1.9%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

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
<td align="right">944</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">510</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">944</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">511</td>
<td align="right">35.1%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

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
<td align="right">6,670,928</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">72,495</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">63</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">3,414,530</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,406,328</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,241,508</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">257,286</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">164,636</td>
<td align="right">2.4%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">634,972</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,318</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">114</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">50</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">642,615</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">9</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">10,644,731</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">923,132</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">384,407</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">66,011</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">65,873</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">10,346,614</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">901,155</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">491,118</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">367,436</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">442</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">165,507</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">158,709</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">6,946</td>
<td align="right">4.2%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">2,117,784</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,534,043</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">513,129</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">454,458</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">452,832</td>
<td align="right">6.8%</td>
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
<td align="right">2,487,029</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,534,043</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,359,820</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">223,068</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">190,305</td>
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
<td align="right">18,759,833</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,648,804</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,023,174</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">334,582</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">62,752</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">10,921,035</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,299,224</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">8,230,028</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,143,012</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,034,833</td>
<td align="right">3.5%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,864,918</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">195,164</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">189,260</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">98,842</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">96,098</td>
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
<td align="left">CALL_TUPLE_1</td>
<td align="right">3,724,741</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">200,991</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">137,311</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">111,507</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">97,034</td>
<td align="right">2.2%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">4,353,332</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,691,266</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,265,762</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,730,927</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,368,217</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">8,279,614</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,071,693</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,792,750</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,062,886</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">39,686</td>
<td align="right">0.2%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">24,187,524</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">12,894,402</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,729,031</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,060,193</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">826,702</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">40,190,175</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">2,289,673</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">420,037</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">45,066</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,451</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">372</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">22</td>
<td align="right">5.6%</td>
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
<td align="right">394</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">597,209</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">403</td>
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
<td align="left">POP_TOP</td>
<td align="right">555,411</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,710</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">8,644</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,611</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,088</td>
<td align="right">1.0%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">7,516,220</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">21</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">7,358,194</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">147,776</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">5,800</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,066</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">21</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">21,070,375</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">469,468</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">141,545</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">29,040</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">11,743</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">8,164,561</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,664,693</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">5,354,115</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">452,832</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">66,789</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">11,820,234</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,554,036</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,406,328</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,239,905</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">447,808</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">11,309,133</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,011,300</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,758,358</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,318,739</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">164,929</td>
<td align="right">0.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">8,233,784</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,177,422</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,662,775</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,549,052</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,244,666</td>
<td align="right">6.9%</td>
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
<td align="right">10,232,875</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,680,134</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,483,064</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,222,072</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">583,843</td>
<td align="right">3.3%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,165</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">894</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">580</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6</td>
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
<td align="left">STORE_FAST</td>
<td align="right">633</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">591</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">574</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">527</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">191</td>
<td align="right">7.2%</td>
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
<td align="right">11,348,644</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,836,128</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">96,180</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">515</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">92</td>
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
<td align="right">9,958,665</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,864,918</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,142,752</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">105,081</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">96,180</td>
<td align="right">0.6%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,634,872</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">717,874</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">203,030</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">76,720</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">31,975</td>
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
<td align="left">POP_TOP</td>
<td align="right">1,911,907</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">717,690</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">31,720</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">7,930</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,734</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,502,971</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,530,444</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">1,827,693</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,246,857</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,046,128</td>
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
<td align="left">GET_ITER</td>
<td align="right">7,314,748</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,241,207</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,443,829</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">447,808</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">81,778</td>
<td align="right">0.5%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">16,247,156</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,767,607</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,720,073</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">4,064,196</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,204,805</td>
<td align="right">2.9%</td>
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
<td align="right">31,499,253</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,496,820</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,615,517</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,804,754</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">541,541</td>
<td align="right">1.3%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,740,791</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,167,655</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">130,842</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">126,010</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">64,036</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">2,598,018</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">407,390</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">156,225</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">146,417</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">130,501</td>
<td align="right">3.8%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">116,491</td>
<td align="right">87.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">10,803</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,401</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">29</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">127,257</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,503</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">759</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">92</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">63</td>
<td align="right">0.0%</td>
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
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,724,741</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">782,538</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">71,622</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,226</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,035</td>
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
<td align="left">BINARY_OP</td>
<td align="right">3,724,751</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">328,260</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">275,331</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">145,208</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">36,519</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">10,809,286</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">47,522</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">92</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">74</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,472,852</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,421,324</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,883,802</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,735</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,170</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">392,951</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">19,745</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">14,710</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">92</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">16</td>
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
<td align="right">426,415</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,119</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">21</td>
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
<td align="right">11,940,092</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">8,164,561</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,468,617</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4,100,284</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">741,904</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">17,612,868</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,084,091</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,817,361</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,368,109</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,266,726</td>
<td align="right">4.3%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,104,206</td>
<td align="right">77.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,241,184</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">152,112</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">126</td>
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
<td align="right">10,459,006</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">37,958</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">703</td>
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
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,162,916</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,824,730</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,536,816</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">31,831</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,437</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,038,970</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,527,459</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">636</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">92</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">62,408</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">7,558</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,166</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,335</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">632</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">66,071</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,738</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,553</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,294</td>
<td align="right">1.6%</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">76,988</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">70,603</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">76,822</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">70,475</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">256</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">43</td>
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
<td align="left">GET_ITER</td>
<td align="right">8,092,557</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">4,202,652</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,694,603</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">118,818</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,733</td>
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
<td align="right">8,730,834</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,135,349</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,951,081</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,321,181</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">529,092</td>
<td align="right">3.5%</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">964,059</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">594,237</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">511,301</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,842,881</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">140,739</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">58,765</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,596</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,141</td>
<td align="right">0.2%</td>
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
<td align="left">GET_ITER</td>
<td align="right">8,361,632</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,278,843</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,032,506</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">265,765</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">7,847</td>
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
<td align="right">10,137,717</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">857,728</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">462,666</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">430,347</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">406,601</td>
<td align="right">3.1%</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,366,133</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">22,683</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">845</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">18</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,362,574</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">21,522</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,164</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,111</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">316</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,540,083</td>
<td align="right">93.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">131,884</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">28,253</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">1,585</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,540</td>
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
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,162,916</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">239,618</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">124,768</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">62,398</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">61,775</td>
<td align="right">2.3%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">3,360,113</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">766,903</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">763,716</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">669,164</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">449,351</td>
<td align="right">7.4%</td>
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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,023,174</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">924,697</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">781,153</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">766,903</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">717,799</td>
<td align="right">11.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">50,732,282</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,663,065</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,483,064</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,558,509</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">924,697</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">22,776,232</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">16,247,156</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">11,348,644</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,626,523</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,086,655</td>
<td align="right">3.5%</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">8,885,511</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,728,953</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,672,159</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">106,211</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">101,805</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">7,993,480</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,836,128</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,484,244</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">186,872</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">5,718</td>
<td align="right">0.0%</td>
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
<td align="right">490,840</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,055</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">379</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">277</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">50</td>
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
<td align="right">418,969</td>
<td align="right">84.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">62,828</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,860</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,145</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,055</td>
<td align="right">0.4%</td>
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
<td align="right">38,980,634</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,480,781</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">980,907</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">271,092</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">197,526</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">32,086,712</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">4,353,332</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,990,910</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,455,350</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">1,327,207</td>
<td align="right">3.1%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">671,266</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">335,613</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">200,438</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,159</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">3,754</td>
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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">334,582</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">334,582</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">289,828</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">95,544</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">84,961</td>
<td align="right">7.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">19,281,481</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">505,685</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">218,036</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">135,185</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">51,585</td>
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
<td align="right">9,356,687</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,131,199</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,682,815</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,533,352</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">534,221</td>
<td align="right">2.6%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">58,977,388</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,273,114</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">327,978</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">54,311</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">50,403</td>
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
<td align="right">17,917,188</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">14,580,345</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,034,164</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,991,076</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,771,054</td>
<td align="right">6.2%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">38,345,469</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">17,329,370</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">16,794,779</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,775,096</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,247,526</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">25,695,830</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">18,759,833</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">17,329,370</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,327,961</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">8,429,514</td>
<td align="right">8.1%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">40,754,922</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">31,343,612</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">24,191,736</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,953,796</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">8,661,288</td>
<td align="right">5.5%</td>
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
<td align="right">110,121,834</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">18,567,565</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">12,894,402</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,799,726</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,422,193</td>
<td align="right">1.5%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">41,112,626</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">12,096,082</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,689,170</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">6,999,976</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,073,637</td>
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
<td align="left">CALL_ISINSTANCE</td>
<td align="right">24,187,524</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">21,709,363</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,651,147</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,540,083</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,423,508</td>
<td align="right">2.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">880,688</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">61,900</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">942,593</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,323,141</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">25</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,204,805</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">113,236</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,229</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">878</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">16</td>
<td align="right">0.0%</td>
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
<td align="left">CACHE</td>
<td align="right">68,455,138</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">31,499,253</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">14,416,969</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">11,113,871</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">10,346,614</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">69,687,748</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">31,343,612</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">16,794,779</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">14,214,376</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">12,096,082</td>
<td align="right">7.1%</td>
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
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">487,031</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">259,002</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">274</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">479,824</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">251,772</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">7,228</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">7,211</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">272</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,408,900</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">669,164</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">194,533</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,223</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">280</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">799,234</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">754,164</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">334,677</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">334,585</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">35,803</td>
<td align="right">1.6%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,510,794</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,082,032</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">29,650</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">55</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">3,480,395</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,612,946</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,380,610</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">106,215</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">29,650</td>
<td align="right">0.4%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,250,962</td>
<td align="right">71.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">280,702</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">145,208</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">63,312</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">11,699</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">950,566</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">536,336</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">155,559</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">102,034</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,494</td>
<td align="right">0.5%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">14,829,318</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">894,714</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">89,080</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">79,653</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">16,636</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,864,919</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,887,913</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,013,501</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">109,962</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">16,957</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">169,796</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,134</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,022</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">66</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">167,092</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,790</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,134</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2</td>
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
<td align="right">40,190,175</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">32,086,712</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">14,490,852</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">10,921,035</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,429,710</td>
<td align="right">5.6%</td>
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
<td align="right">77,326,896</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">32,582,254</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,819,009</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">890,925</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,140</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">14,566,206</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">565,178</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">360,442</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">50,130</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">19,745</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,439,359</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,127,969</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">342</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,484,839</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">31,678</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,258</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,998</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">439</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">596,993</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">521,035</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">372,124</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">29,542</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,875</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,364,033</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">333,257</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">207,170</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">37,495</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,312</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,465,836</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">485,380</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">12,133</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,513</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,216</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">334,582</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,183</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">560</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">226</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8</td>
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
<td align="right">336,001</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,564</td>
<td align="right">0.8%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">93,991</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">39,255</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,245</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,534</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,534</td>
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
<td align="left">STORE_FAST</td>
<td align="right">89,723</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">51,668</td>
<td align="right">36.5%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">697,033</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">526,161</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">63,736</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">376</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">257</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,132,561</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">123,496</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">31,868</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2</td>
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
<td align="right">22,540,513</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">15,560,422</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,951,081</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,238,440</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">462,666</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">38,672,330</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">3,023,628</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">203,830</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,503</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

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
<td align="right">15,085,268</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">11,309,133</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">7,932,728</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">6,887,913</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">6,271,572</td>
<td align="right">8.8%</td>
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
<td align="right">37,159,480</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,723,862</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">6,159,324</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,177,422</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">3,232,966</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">254</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1</td>
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
<td align="right">255</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">101</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">102</td>
<td align="right">100.0%</td>
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
<td align="right">111</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">21</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">133</td>
<td align="right">100.0%</td>
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
<td align="right">127</td>
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
<td align="right">127</td>
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
<td align="left">DELETE_NAME</td>
<td align="right">4</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1</td>
<td align="right">16.7%</td>
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
<td align="left">DELETE_NAME</td>
<td align="right">4</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1</td>
<td align="right">16.7%</td>
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
<td align="left">BUILD_MAP</td>
<td align="right">1</td>
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
<td align="right">1</td>
<td align="right">100.0%</td>
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
<td align="left">STORE_NAME</td>
<td align="right">2,301</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">2,160</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,800</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">900</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">360</td>
<td align="right">4.0%</td>
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
<td align="right">2,160</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,796</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,130</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">917</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">901</td>
<td align="right">10.1%</td>
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
<td align="right">1,871</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,871</td>
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
<td align="right">1,871</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">901</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">878</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">92</td>
<td align="right">2.5%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

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
<td align="right">2</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1</td>
<td align="right">33.3%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">92</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">92</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1</td>
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
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1</td>
<td align="right">100.0%</td>
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
<td align="right">27,259,408</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,386,375</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">126</td>
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
<td align="right">1,270</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">19,514</td>
<td align="right">93.9%</td>
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
<td align="left">subtract other</td>
<td align="right">3,221</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">2,896</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">2,592</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">2,225</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,291</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">1,215</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,086</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,010</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">982</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">716</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">702</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">569</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">363</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">211</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">189</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">155</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">91</td>
<td align="right">0.5%</td>
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
<td align="right">8,858</td>
<td align="right">100.0%</td>
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
<td align="right">7,549,707</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,765,552</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,754</td>
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
<td align="right">982</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,022</td>
<td align="right">83.6%</td>
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
<td align="right">3,488</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">689</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">422</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">274</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">148</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">1</td>
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
<td align="right">20,200</td>
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
<td align="right">13,673</td>
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
<td align="right">296,117,245</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,918,584</td>
<td align="right">7.8%</td>
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
<td align="right">486,791</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">536</td>
<td align="right">0.1%</td>
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
<td align="left">out of versions</td>
<td align="right">536</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">536</td>
<td align="right">100.0%</td>
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
<td align="right">399</td>
<td align="right">9.4%</td>
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
<td align="right">66.0%</td>
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
<td align="right">25,937,667</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">51,028,529</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">409,664</td>
<td align="right">0.5%</td>
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
<td align="right">8,834</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">36,336</td>
<td align="right">80.4%</td>
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
<td align="left">big int</td>
<td align="right">14,102</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,480</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,400</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">4,262</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,159</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">409</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">138</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">136</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">115</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">91</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">44</td>
<td align="right">0.1%</td>
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
<td align="right">4,584,173</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,499,525</td>
<td align="right">83.7%</td>
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
<td align="right">122</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,818</td>
<td align="right">96.9%</td>
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
<td align="right">1,909</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,473</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">299</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">137</td>
<td align="right">3.6%</td>
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
<td align="right">33,563,788</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,587,111</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">691,121</td>
<td align="right">1.1%</td>
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
<td align="right">13,668</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">47,838</td>
<td align="right">77.8%</td>
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
<td align="left">dict items</td>
<td align="right">38,915</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,885</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">2,710</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,335</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">758</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">557</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">382</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">243</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">29</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">24</td>
<td align="right">0.1%</td>
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
<td align="right">59,994,788</td>
<td align="right">18.4%</td>
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
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">222,237,671</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">42,943,142</td>
<td align="right">13.2%</td>
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
<td align="right">823,039</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,042</td>
<td align="right">5.2%</td>
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
<td align="left">mutable class</td>
<td align="right">21,175</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">6,812</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">4,069</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">3,164</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">3,098</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,008</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,327</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">211</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">148</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
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
<td align="right">4,535</td>
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
<td align="right">244,301,519</td>
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
<td align="right">1,294</td>
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
<td align="right">13,565</td>
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
<td align="right">30</td>
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
<td align="right">2,265,759</td>
<td align="right">100.0%</td>
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
<td align="right">30</td>
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
<td align="right">268,986</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">731,596</td>
<td align="right">72.0%</td>
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
<td align="right">274</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,108</td>
<td align="right">80.2%</td>
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
<td align="right">1,108</td>
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
<td align="right">173,952</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,327,822</td>
<td align="right">80.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,575,810</td>
<td align="right">17.4%</td>
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
<td align="right">29,986</td>
<td align="right">96.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">979</td>
<td align="right">3.2%</td>
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
<td align="left">class attr simple</td>
<td align="right">518</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">300</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">158</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3</td>
<td align="right">0.3%</td>
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
<td align="right">591</td>
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
<td align="right">879,327</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,739,808</td>
<td align="right">95.3%</td>
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
<td align="right">576</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,135</td>
<td align="right">66.3%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">1,135</td>
<td align="right">100.0%</td>
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
<td align="right">9,919,526</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">153,557,973</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">442,445</td>
<td align="right">0.3%</td>
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
<td align="right">15,469</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">11,787</td>
<td align="right">43.2%</td>
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
<td align="left">tuple</td>
<td align="right">6,214</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,899</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">1,254</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">883</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">730</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">721</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">84</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2</td>
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
<td align="right">6,260</td>
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
<td align="right">83,919,063</td>
<td align="right">100.0%</td>
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
<td align="right">2,392</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">306</td>
<td align="right">11.3%</td>
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
<td align="right">263</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">43</td>
<td align="right">14.1%</td>
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
<td align="right">2,148,784,626</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">170,406,116</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,250,521,377</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">71,011,738</td>
<td align="right">2.0%</td>
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
<td align="right">59,994,788</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,563,788</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,259,408</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">25,937,667</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,919,526</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">7,549,707</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,584,173</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">879,327</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">268,986</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">173,952</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">20,396,520</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">11,804,534</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,491,516</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,158,036</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,113,388</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,102,552</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,166,122</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,103,567</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,575,031</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">464,671</td>
<td align="right">0.7%</td>
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
<td align="right">98,192,924</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">112,593,363</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">98,192,924</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">75,631,172</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">22,561,752</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">652</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">75,630,387</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,490,733</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">9,331,939</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">41,334,882</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">950,135</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">187,979,598</td>
<td align="right">89.2%</td>
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
<td align="right">281,751,058</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">281,782,457</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">232,971,449</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">232,194,423</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">768,396</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,630</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">245,617,881</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">866,164</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,647,587,053</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,005,258,552</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,674,980,875</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,771,878,866</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">441,403,827</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">705,659,116</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,179,750,921</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,282,453,946</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (str subclass)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">147,661,469</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,227,766</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,039,194</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">265,707,825</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">813,083</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">17,970</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">6,892</td>
<td align="right">38.4%</td>
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
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">11,068</td>
<td align="right">61.6%</td>
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
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">11,078</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">185</td>
<td align="right">1.0%</td>
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
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">172</td>
<td align="right">1.0%</td>
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
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">141,762,764</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,728,310,036</td>
<td align="right">1,924.6%</td>
</tr>
</tbody>
</table>

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
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">6,892</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">6,804</td>
<td align="right">98.7%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">937</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,161</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">2,601</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,496</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">676</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">0.3%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">133</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,020</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,506</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">3,033</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,022</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">90</td>
<td align="right">1.3%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
<th align="right">Miss ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">_SET_IP</td>
<td align="right">282,084,271</td>
<td align="right">10.3%</td>
<td align="right">10.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">231,204,259</td>
<td align="right">8.5%</td>
<td align="right">18.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">184,396,283</td>
<td align="right">6.8%</td>
<td align="right">25.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">141,762,764</td>
<td align="right">5.2%</td>
<td align="right">30.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">133,838,302</td>
<td align="right">4.9%</td>
<td align="right">35.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">127,502,775</td>
<td align="right">4.7%</td>
<td align="right">40.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">68,998,784</td>
<td align="right">2.5%</td>
<td align="right">42.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">66,629,603</td>
<td align="right">2.4%</td>
<td align="right">45.3%</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">65,314,933</td>
<td align="right">2.4%</td>
<td align="right">47.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">58,252,901</td>
<td align="right">2.1%</td>
<td align="right">49.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">51,901,479</td>
<td align="right">1.9%</td>
<td align="right">51.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">48,659,123</td>
<td align="right">1.8%</td>
<td align="right">53.5%</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">43,670,943</td>
<td align="right">1.6%</td>
<td align="right">55.1%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">42,747,608</td>
<td align="right">1.6%</td>
<td align="right">56.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">42,633,519</td>
<td align="right">1.6%</td>
<td align="right">58.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40,584,781</td>
<td align="right">1.5%</td>
<td align="right">59.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">39,353,728</td>
<td align="right">1.4%</td>
<td align="right">61.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">38,430,072</td>
<td align="right">1.4%</td>
<td align="right">62.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">34,424,255</td>
<td align="right">1.3%</td>
<td align="right">63.9%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">33,225,751</td>
<td align="right">1.2%</td>
<td align="right">65.1%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">32,199,704</td>
<td align="right">1.2%</td>
<td align="right">66.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">28,336,640</td>
<td align="right">1.0%</td>
<td align="right">67.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">28,301,061</td>
<td align="right">1.0%</td>
<td align="right">68.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">27,749,075</td>
<td align="right">1.0%</td>
<td align="right">69.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">27,708,238</td>
<td align="right">1.0%</td>
<td align="right">70.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">27,342,376</td>
<td align="right">1.0%</td>
<td align="right">71.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">26,667,880</td>
<td align="right">1.0%</td>
<td align="right">72.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">24,715,237</td>
<td align="right">0.9%</td>
<td align="right">73.3%</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">22,931,327</td>
<td align="right">0.8%</td>
<td align="right">74.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">20,291,576</td>
<td align="right">0.7%</td>
<td align="right">74.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">20,291,576</td>
<td align="right">0.7%</td>
<td align="right">75.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">19,429,197</td>
<td align="right">0.7%</td>
<td align="right">76.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">19,148,911</td>
<td align="right">0.7%</td>
<td align="right">77.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">18,780,339</td>
<td align="right">0.7%</td>
<td align="right">77.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">18,419,385</td>
<td align="right">0.7%</td>
<td align="right">78.4%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">18,218,463</td>
<td align="right">0.7%</td>
<td align="right">79.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">18,200,952</td>
<td align="right">0.7%</td>
<td align="right">79.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">18,123,721</td>
<td align="right">0.7%</td>
<td align="right">80.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">17,854,732</td>
<td align="right">0.7%</td>
<td align="right">81.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">15,789,022</td>
<td align="right">0.6%</td>
<td align="right">81.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">14,994,935</td>
<td align="right">0.5%</td>
<td align="right">82.1%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">14,684,327</td>
<td align="right">0.5%</td>
<td align="right">82.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">14,672,499</td>
<td align="right">0.5%</td>
<td align="right">83.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">14,220,964</td>
<td align="right">0.5%</td>
<td align="right">83.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">14,217,344</td>
<td align="right">0.5%</td>
<td align="right">84.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">14,064,012</td>
<td align="right">0.5%</td>
<td align="right">84.8%</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">13,923,415</td>
<td align="right">0.5%</td>
<td align="right">85.3%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">13,313,079</td>
<td align="right">0.5%</td>
<td align="right">85.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">13,313,079</td>
<td align="right">0.5%</td>
<td align="right">86.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,082,077</td>
<td align="right">0.5%</td>
<td align="right">86.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">12,863,248</td>
<td align="right">0.5%</td>
<td align="right">87.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">12,404,829</td>
<td align="right">0.5%</td>
<td align="right">87.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">12,247,367</td>
<td align="right">0.4%</td>
<td align="right">88.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">12,024,793</td>
<td align="right">0.4%</td>
<td align="right">88.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">11,732,700</td>
<td align="right">0.4%</td>
<td align="right">89.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,557,180</td>
<td align="right">0.4%</td>
<td align="right">89.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">11,164,677</td>
<td align="right">0.4%</td>
<td align="right">89.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">10,329,095</td>
<td align="right">0.4%</td>
<td align="right">90.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,045,538</td>
<td align="right">0.4%</td>
<td align="right">90.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">9,162,885</td>
<td align="right">0.3%</td>
<td align="right">90.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">8,935,094</td>
<td align="right">0.3%</td>
<td align="right">91.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">8,862,018</td>
<td align="right">0.3%</td>
<td align="right">91.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">8,862,018</td>
<td align="right">0.3%</td>
<td align="right">91.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,861,390</td>
<td align="right">0.3%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">8,831,531</td>
<td align="right">0.3%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">8,509,277</td>
<td align="right">0.3%</td>
<td align="right">92.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">8,475,805</td>
<td align="right">0.3%</td>
<td align="right">93.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">8,245,687</td>
<td align="right">0.3%</td>
<td align="right">93.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,844,260</td>
<td align="right">0.3%</td>
<td align="right">93.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">7,817,618</td>
<td align="right">0.3%</td>
<td align="right">94.0%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">7,225,469</td>
<td align="right">0.3%</td>
<td align="right">94.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">6,908,572</td>
<td align="right">0.3%</td>
<td align="right">94.5%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">6,908,572</td>
<td align="right">0.3%</td>
<td align="right">94.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">6,788,230</td>
<td align="right">0.2%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">6,746,736</td>
<td align="right">0.2%</td>
<td align="right">95.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">6,585,329</td>
<td align="right">0.2%</td>
<td align="right">95.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,558,784</td>
<td align="right">0.2%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,525,101</td>
<td align="right">0.2%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">6,525,101</td>
<td align="right">0.2%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">6,504,124</td>
<td align="right">0.2%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">6,074,232</td>
<td align="right">0.2%</td>
<td align="right">96.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">6,074,232</td>
<td align="right">0.2%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">6,040,002</td>
<td align="right">0.2%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">5,636,603</td>
<td align="right">0.2%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,516,652</td>
<td align="right">0.2%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">5,185,974</td>
<td align="right">0.2%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">4,947,749</td>
<td align="right">0.2%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,801,283</td>
<td align="right">0.2%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">4,671,758</td>
<td align="right">0.2%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">4,549,561</td>
<td align="right">0.2%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">3,264,972</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">3,163,771</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,587,941</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,513,694</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">2,451,931</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,380,046</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,262,649</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">2,092,783</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">1,852,084</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,828,463</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">1,703,683</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,498,208</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,498,208</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,382,796</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">1,368,244</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">1,368,244</td>
<td align="right">0.1%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,360,727</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,285,622</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,032,560</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">651,739</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">630,363</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">563,070</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">559,113</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">416,235</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">416,235</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">389,868</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">320,400</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">245,074</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">188,210</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">174,242</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">159,560</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">144,184</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">105,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">73,352</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">52,447</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">42,126</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">28,820</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">26,932</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">24,402</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">24,402</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,228</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">5,166</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">744</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">628</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">519</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
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


</details>

### Unsupported opcodes

<details>
<summary> unsupported opcodes </summary>

<table>
<thead>
<tr>
<th align="left">Opcode</th>
<th align="right">Count</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,792</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">926</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">21</td>
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
<td align="right">0</td>
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
<td align="right">0</td>
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
<td align="right">84</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-12-06
