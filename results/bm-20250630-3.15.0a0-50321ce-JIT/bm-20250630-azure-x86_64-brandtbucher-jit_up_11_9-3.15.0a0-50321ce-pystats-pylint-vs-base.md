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
<td align="left">NOT_TAKEN</td>
<td align="right">91,371</td>
<td align="right">235,935</td>
<td align="right">158.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">845,187</td>
<td align="right">457,989</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">144,186</td>
<td align="right">100,779</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">243,789</td>
<td align="right">177,366</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">642,747</td>
<td align="right">498,372</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,397,214</td>
<td align="right">1,092,840</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,789,956</td>
<td align="right">1,413,657</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,276,352</td>
<td align="right">6,543,760</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">885,339</td>
<td align="right">725,340</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,393,286</td>
<td align="right">1,994,031</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">6,804,717</td>
<td align="right">5,736,204</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">465,927</td>
<td align="right">396,018</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">7,900,710</td>
<td align="right">6,730,551</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,811,763</td>
<td align="right">3,318,426</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,816,604</td>
<td align="right">5,135,625</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">4,287,549</td>
<td align="right">3,791,757</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,718,741</td>
<td align="right">5,105,142</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,441,440</td>
<td align="right">1,291,168</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">13,231,497</td>
<td align="right">11,968,386</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">8,672,745</td>
<td align="right">7,896,018</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,265,917</td>
<td align="right">4,613,551</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">8,236,620</td>
<td align="right">7,600,761</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">737,562</td>
<td align="right">680,883</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">383,859</td>
<td align="right">355,131</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">81,606</td>
<td align="right">87,234</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,963,835</td>
<td align="right">2,777,838</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">30,016,831</td>
<td align="right">28,184,161</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">532,434</td>
<td align="right">501,438</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,962,298</td>
<td align="right">4,687,765</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">878,031</td>
<td align="right">835,716</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">3,285,093</td>
<td align="right">3,151,260</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">23,029,521</td>
<td align="right">22,110,819</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">82,995,434</td>
<td align="right">79,846,058</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">15,379,999</td>
<td align="right">15,956,625</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,446,853</td>
<td align="right">4,282,289</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">5,357,988</td>
<td align="right">5,159,814</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,843,001</td>
<td align="right">2,740,143</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">96,322,462</td>
<td align="right">92,901,914</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">65,141,995</td>
<td align="right">62,919,341</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,769,119</td>
<td align="right">5,594,174</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">828,723</td>
<td align="right">804,287</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">68,756,854</td>
<td align="right">66,819,997</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">29,985,326</td>
<td align="right">29,143,028</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">32,705,632</td>
<td align="right">31,866,336</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">26,826,180</td>
<td align="right">26,162,172</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,790,329</td>
<td align="right">8,601,269</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">66,046,907</td>
<td align="right">64,634,915</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">490,308</td>
<td align="right">480,354</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,079,748</td>
<td align="right">9,884,154</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">18,958,644</td>
<td align="right">18,597,258</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,180,430</td>
<td align="right">2,140,656</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,781,184</td>
<td align="right">1,748,742</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">254,352</td>
<td align="right">249,946</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">33,822,317</td>
<td align="right">33,329,213</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">3,791,737</td>
<td align="right">3,736,591</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,853,013</td>
<td align="right">4,783,245</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,288,668</td>
<td align="right">2,256,457</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">7,051,433</td>
<td align="right">6,967,055</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">70,431,340</td>
<td align="right">69,606,898</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">64,145,280</td>
<td align="right">63,420,690</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,846,586</td>
<td align="right">8,753,472</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,837,310</td>
<td align="right">2,809,737</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">3,944,598</td>
<td align="right">3,906,630</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">349,346,496</td>
<td align="right">346,115,862</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">20,559,164</td>
<td align="right">20,376,779</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,541,753</td>
<td align="right">5,494,293</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">27,294,876</td>
<td align="right">27,071,247</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,611,203</td>
<td align="right">2,590,665</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">14,999,629</td>
<td align="right">14,885,923</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">51,065,388</td>
<td align="right">50,702,256</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">20,405,990</td>
<td align="right">20,261,510</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">8,203,228</td>
<td align="right">8,146,486</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,275,429</td>
<td align="right">7,226,478</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,110,874</td>
<td align="right">4,084,897</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">12,914,790</td>
<td align="right">12,838,854</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">32,486,244</td>
<td align="right">32,326,812</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">53,604,111</td>
<td align="right">53,399,957</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">7,541,035</td>
<td align="right">7,515,058</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,345,699</td>
<td align="right">16,295,377</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">32,002,934</td>
<td align="right">31,919,753</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">15,090,844</td>
<td align="right">15,061,801</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">101,608,068</td>
<td align="right">101,433,718</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">6,826,812</td>
<td align="right">6,837,438</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">12,973,059</td>
<td align="right">12,957,435</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">111,379,442</td>
<td align="right">111,389,201</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">98,927,053</td>
<td align="right">98,922,574</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">164,052</td>
<td align="right">164,049</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">983,466</td>
<td align="right">983,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">27,380,147</td>
<td align="right">27,380,144</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">13,413,813</td>
<td align="right">13,413,813</td>
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
<td align="left">CALL_LEN</td>
<td align="right">2,324,853</td>
<td align="right">2,324,853</td>
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
<td align="left">RAISE_VARARGS</td>
<td align="right">245,763</td>
<td align="right">245,763</td>
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
<td align="left">SET_ADD</td>
<td align="right">52,500</td>
<td align="right">52,500</td>
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
<td align="right">72,118</td>
<td align="right">0.2%</td>
<td align="right">-23.6%</td>
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
<td align="right">4,654,396</td>
<td align="right">13.3%</td>
<td align="right">-5.6%</td>
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
<td align="right">30,108,399</td>
<td align="right">86.3%</td>
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
<td align="right">14,973</td>
<td align="right">42.1%</td>
<td align="right">14,553</td>
<td align="right">42.0%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20,622</td>
<td align="right">57.9%</td>
<td align="right">20,076</td>
<td align="right">58.0%</td>
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
<td align="left">out of range</td>
<td align="right">5,229</td>
<td align="right">25.4%</td>
<td align="right">4,725</td>
<td align="right">23.5%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">756</td>
<td align="right">3.7%</td>
<td align="right">714</td>
<td align="right">3.6%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,381</td>
<td align="right">16.4%</td>
<td align="right">3,381</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">2,961</td>
<td align="right">14.4%</td>
<td align="right">2,961</td>
<td align="right">14.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">2,310</td>
<td align="right">11.2%</td>
<td align="right">2,310</td>
<td align="right">11.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,289</td>
<td align="right">11.1%</td>
<td align="right">2,289</td>
<td align="right">11.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">777</td>
<td align="right">3.8%</td>
<td align="right">777</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">588</td>
<td align="right">2.9%</td>
<td align="right">588</td>
<td align="right">2.9%</td>
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
<td align="right">680,883</td>
<td align="right">100.0%</td>
<td align="right">-7.7%</td>
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
<td align="right">113,966,774</td>
<td align="right">89.8%</td>
<td align="right">113,630,984</td>
<td align="right">89.8%</td>
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
<td align="right">12,686,096</td>
<td align="right">10.0%</td>
<td align="right">12,702,623</td>
<td align="right">10.0%</td>
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
<td align="right">12,588,255</td>
<td align="right">9.9%</td>
<td align="right">12,604,446</td>
<td align="right">10.0%</td>
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
<td align="right">339,908</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
<td align="right">4,760,478</td>
<td align="right">11.4%</td>
<td align="right">-1.4%</td>
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
<td align="right">37,036,932</td>
<td align="right">88.5%</td>
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
<td align="left">Success</td>
<td align="right">12,285</td>
<td align="right">52.7%</td>
<td align="right">12,285</td>
<td align="right">52.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">11,028</td>
<td align="right">47.3%</td>
<td align="right">11,028</td>
<td align="right">47.3%</td>
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
<td align="left">tuple</td>
<td align="right">360</td>
<td align="right">3.3%</td>
<td align="right">360</td>
<td align="right">3.3%</td>
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
<td align="right">3,295,821</td>
<td align="right">30.5%</td>
<td align="right">-13.0%</td>
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
<td align="right">18,237</td>
<td align="right">79.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,851</td>
<td align="right">20.9%</td>
<td align="right">4,851</td>
<td align="right">21.0%</td>
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
<td align="right">2,247</td>
<td align="right">12.2%</td>
<td align="right">2,226</td>
<td align="right">12.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,738</td>
<td align="right">20.4%</td>
<td align="right">3,717</td>
<td align="right">20.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">8,181</td>
<td align="right">44.6%</td>
<td align="right">8,136</td>
<td align="right">44.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">4,179</td>
<td align="right">22.8%</td>
<td align="right">4,158</td>
<td align="right">22.8%</td>
<td align="right">-0.5%</td>
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
<td align="right">5,067,972</td>
<td align="right">10.4%</td>
<td align="right">-10.8%</td>
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
<td align="right">43,361,548</td>
<td align="right">89.0%</td>
<td align="right">-1.1%</td>
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
<td align="right">22,008</td>
<td align="right">53.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">19,488</td>
<td align="right">46.8%</td>
<td align="right">19,488</td>
<td align="right">47.0%</td>
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
<td align="right">4,599</td>
<td align="right">20.9%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">4,872</td>
<td align="right">22.0%</td>
<td align="right">4,851</td>
<td align="right">22.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,174</td>
<td align="right">27.9%</td>
<td align="right">6,174</td>
<td align="right">28.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,953</td>
<td align="right">8.8%</td>
<td align="right">1,953</td>
<td align="right">8.9%</td>
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
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">630</td>
<td align="right">2.8%</td>
<td align="right">630</td>
<td align="right">2.9%</td>
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
<td align="right">44,223,322</td>
<td align="right">18.7%</td>
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
<td align="right">163,331,331</td>
<td align="right">67.6%</td>
<td align="right">160,471,504</td>
<td align="right">67.7%</td>
<td align="right">-1.8%</td>
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
<td align="right">31,838,310</td>
<td align="right">13.4%</td>
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
<td align="right">952,497</td>
<td align="right">83.8%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">186,858</td>
<td align="right">15.9%</td>
<td align="right">183,477</td>
<td align="right">16.2%</td>
<td align="right">-1.8%</td>
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
<td align="right">15,603</td>
<td align="right">8.4%</td>
<td align="right">15,561</td>
<td align="right">8.5%</td>
<td align="right">-0.3%</td>
</tr>
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
<td align="right">10.3%</td>
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
<td align="right">126,298,871</td>
<td align="right">99.8%</td>
<td align="right">-2.3%</td>
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
<td align="right">108,234</td>
<td align="right">659.1%</td>
<td align="right">-3.0%</td>
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
<td align="right">173,334</td>
<td align="right">4.6%</td>
<td align="right">-27.7%</td>
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
<td align="right">95.3%</td>
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
<td align="right">6,481,461</td>
<td align="right">6.2%</td>
<td align="right">-9.1%</td>
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
<td align="right">96,251,201</td>
<td align="right">92.8%</td>
<td align="right">-0.5%</td>
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
<td align="right">917,457</td>
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
<td align="right">170,184</td>
<td align="right">91.0%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">16,758</td>
<td align="right">8.4%</td>
<td align="right">16,758</td>
<td align="right">9.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">839,874</td>
<td align="right">3.2%</td>
<td align="right">452,802</td>
<td align="right">1.7%</td>
<td align="right">-46.1%</td>
</tr>
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
<td align="right">25,423,476</td>
<td align="right">98.2%</td>
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
<td align="right">903</td>
<td align="right">17.0%</td>
<td align="right">777</td>
<td align="right">15.0%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,410</td>
<td align="right">83.0%</td>
<td align="right">4,410</td>
<td align="right">85.0%</td>
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
<td align="right">693</td>
<td align="right">89.2%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">84</td>
<td align="right">9.3%</td>
<td align="right">84</td>
<td align="right">10.8%</td>
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
<td align="right">78,147,804</td>
<td align="right">3.6%</td>
<td align="right">-3.0%</td>
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
<td align="right">83,882,022</td>
<td align="right">3.8%</td>
<td align="right">-2.7%</td>
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
<td align="right">782,844,731</td>
<td align="right">35.8%</td>
<td align="right">-1.8%</td>
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
<td align="right">1,239,285,993</td>
<td align="right">56.7%</td>
<td align="right">-1.5%</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">3,789,050</td>
<td align="right">4.9%</td>
<td align="right">3,295,821</td>
<td align="right">4.4%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,681,445</td>
<td align="right">7.3%</td>
<td align="right">5,067,972</td>
<td align="right">6.7%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,928,383</td>
<td align="right">6.3%</td>
<td align="right">4,654,396</td>
<td align="right">6.2%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,830,246</td>
<td align="right">6.2%</td>
<td align="right">4,760,478</td>
<td align="right">6.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">31,994,361</td>
<td align="right">41.1%</td>
<td align="right">31,838,310</td>
<td align="right">42.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">12,588,255</td>
<td align="right">16.2%</td>
<td align="right">12,604,446</td>
<td align="right">16.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">917,463</td>
<td align="right">1.2%</td>
<td align="right">917,457</td>
<td align="right">1.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,815,697</td>
<td align="right">8.8%</td>
<td align="right">6,815,697</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,657,780</td>
<td align="right">4.7%</td>
<td align="right">3,657,780</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">839,874</td>
<td align="right">1.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">680,883</td>
<td align="right">0.9%</td>
<td align="right"></td>
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
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,020,471</td>
<td align="right">2.5%</td>
<td align="right">2,342,128</td>
<td align="right">3.0%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">918,729</td>
<td align="right">1.1%</td>
<td align="right">790,083</td>
<td align="right">1.0%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,624,654</td>
<td align="right">11.9%</td>
<td align="right">8,513,649</td>
<td align="right">10.9%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">5,974,563</td>
<td align="right">7.4%</td>
<td align="right">5,457,711</td>
<td align="right">7.0%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">8,953,980</td>
<td align="right">11.1%</td>
<td align="right">8,319,213</td>
<td align="right">10.6%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,981,205</td>
<td align="right">11.2%</td>
<td align="right">8,661,606</td>
<td align="right">11.1%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">18,348,918</td>
<td align="right">22.8%</td>
<td align="right">18,348,918</td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,699,539</td>
<td align="right">17.0%</td>
<td align="right">13,699,539</td>
<td align="right">17.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">5,267,178</td>
<td align="right">6.5%</td>
<td align="right">5,267,178</td>
<td align="right">6.7%</td>
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
<td align="right">561,604</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">24,758,780</td>
<td align="right">19.9%</td>
<td align="right">24,758,777</td>
<td align="right">19.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">24,772,850</td>
<td align="right">19.9%</td>
<td align="right">24,772,847</td>
<td align="right">19.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">27,746,303</td>
<td align="right">22.3%</td>
<td align="right">27,746,300</td>
<td align="right">22.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">27,746,303</td>
<td align="right">22.3%</td>
<td align="right">27,746,300</td>
<td align="right">22.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">100,759,345</td>
<td align="right">81.0%</td>
<td align="right">100,759,339</td>
<td align="right">81.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">96,655,218</td>
<td align="right">77.7%</td>
<td align="right">96,655,215</td>
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
<td align="left">Mortal decrefs</td>
<td align="right">496,554,148</td>
<td align="right">31.8%</td>
<td align="right">505,901,183</td>
<td align="right">32.4%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">693,857,497</td>
<td align="right">44.4%</td>
<td align="right">681,226,312</td>
<td align="right">43.7%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">554,032,049</td>
<td align="right">35.5%</td>
<td align="right">546,749,956</td>
<td align="right">35.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">112,889,807</td>
<td align="right"></td>
<td align="right">113,860,420</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">518,267,957</td>
<td align="right">33.2%</td>
<td align="right">522,265,813</td>
<td align="right">33.5%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">35,694,637</td>
<td align="right">2.3%</td>
<td align="right">35,480,494</td>
<td align="right">2.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">419,080,665</td>
<td align="right">26.8%</td>
<td align="right">420,833,082</td>
<td align="right">27.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">335,681,062</td>
<td align="right">21.5%</td>
<td align="right">336,915,628</td>
<td align="right">21.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">69,635,385</td>
<td align="right">4.5%</td>
<td align="right">69,420,909</td>
<td align="right">4.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,883,063</td>
<td align="right"></td>
<td align="right">2,891,363</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">3,468,122</td>
<td align="right"></td>
<td align="right">3,477,580</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">489,153</td>
<td align="right">0.3%</td>
<td align="right">490,485</td>
<td align="right">0.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">613,393</td>
<td align="right"></td>
<td align="right">614,946</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">227,094</td>
<td align="right">0.1%</td>
<td align="right">227,157</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">54,906,045</td>
<td align="right"></td>
<td align="right">54,916,792</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">86,975,847</td>
<td align="right"></td>
<td align="right">86,978,271</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">99,119,847</td>
<td align="right">56.9%</td>
<td align="right">99,122,481</td>
<td align="right">56.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">98,403,600</td>
<td align="right">56.5%</td>
<td align="right">98,404,839</td>
<td align="right">56.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">75,004,552</td>
<td align="right">43.1%</td>
<td align="right">75,004,807</td>
<td align="right">43.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">75,045,042</td>
<td align="right"></td>
<td align="right">75,045,297</td>
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
<td align="right">154,240,955</td>
<td align="right">19,077,295</td>
<td align="right">7,330,400</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,449</td>
<td align="right">22.6%</td>
<td align="right">3,012</td>
<td align="right">30.2%</td>
<td align="right">107.9%</td>
</tr>
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
<td align="right">84</td>
<td align="right">0.8%</td>
<td align="right">100.0%</td>
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
<td align="right">1,638</td>
<td align="right">16.4%</td>
<td align="right">62.5%</td>
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
<td align="right">9,963</td>
<td align="right"></td>
<td align="right">55.6%</td>
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
<td align="right">36,797,230</td>
<td align="right"></td>
<td align="right">47.6%</td>
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
<td align="right">4,872</td>
<td align="right">48.9%</td>
<td align="right">34.9%</td>
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
<td align="right">441</td>
<td align="right">4.4%</td>
<td align="right">31.2%</td>
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
<td align="right">972,715,477</td>
<td align="right">2,643.4%</td>
<td align="right">15.5%</td>
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
<td align="right">105</td>
<td align="right">1.1%</td>
<td align="right">105 / 0 !!</td>
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
<td align="right">21</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
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
<td align="right">2,886</td>
<td align="right">95.8%</td>
<td align="right">108.2%</td>
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
<td align="right">3,012</td>
<td align="right"></td>
<td align="right">107.9%</td>
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
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">3,109,344</td>
<td align="right">21.9%</td>
<td align="right">6,381,906</td>
<td align="right">22.7%</td>
<td align="right">105.2%</td>
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
<td align="right">617,232</td>
<td align="right">2.2%</td>
<td align="right">100.0%</td>
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
<td align="right">28,065,792</td>
<td align="right"></td>
<td align="right">97.7%</td>
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
<td align="right">21,066,654</td>
<td align="right">75.1%</td>
<td align="right">95.5%</td>
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
<td align="right">86,016</td>
<td align="right">0.6%</td>
<td align="right">86,016</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
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
<td align="left">609</td>
<td align="right">21.1%</td>
<td align="right">123.1%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">693</td>
<td align="right">50.0%</td>
<td align="left">1,281</td>
<td align="right">44.4%</td>
<td align="right">84.8%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">294</td>
<td align="right">21.2%</td>
<td align="left">870</td>
<td align="right">30.1%</td>
<td align="right">195.9%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">105</td>
<td align="right">7.6%</td>
<td align="left">126</td>
<td align="right">4.4%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">21</td>
<td align="right">1.5%</td>
<td align="left"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">126</td>
<td align="right">4.2%</td>
<td align="right">500.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">84</td>
<td align="right">5.8%</td>
<td align="right">147</td>
<td align="right">4.9%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">378</td>
<td align="right">26.1%</td>
<td align="right">546</td>
<td align="right">18.1%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">546</td>
<td align="right">37.7%</td>
<td align="right">1,101</td>
<td align="right">36.6%</td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">294</td>
<td align="right">20.3%</td>
<td align="right">882</td>
<td align="right">29.3%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">105</td>
<td align="right">7.2%</td>
<td align="right">210</td>
<td align="right">7.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">21</td>
<td align="right">1.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">84</td>
<td align="right">2.8%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">168</td>
<td align="right">11.6%</td>
<td align="right">336</td>
<td align="right">11.2%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">651</td>
<td align="right">44.9%</td>
<td align="right">1,155</td>
<td align="right">38.3%</td>
<td align="right">77.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">336</td>
<td align="right">23.2%</td>
<td align="right">996</td>
<td align="right">33.1%</td>
<td align="right">196.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">147</td>
<td align="right">10.1%</td>
<td align="right">252</td>
<td align="right">8.4%</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">42</td>
<td align="right">2.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">63</td>
<td align="right">2.1%</td>
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
<td align="right">187,614</td>
<td align="right">3,488.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,793</td>
<td align="right">31,962</td>
<td align="right">1,044.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">12,810</td>
<td align="right">135,849</td>
<td align="right">960.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">139,608</td>
<td align="right">1,223,763</td>
<td align="right">776.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">16,002</td>
<td align="right">118,230</td>
<td align="right">638.8%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">10,164</td>
<td align="right">53,571</td>
<td align="right">427.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">119,154</td>
<td align="right">586,173</td>
<td align="right">391.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">20,307</td>
<td align="right">90,069</td>
<td align="right">343.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">6,405</td>
<td align="right">22,869</td>
<td align="right">257.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">5,628</td>
<td align="right">19,551</td>
<td align="right">247.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,033</td>
<td align="right">32,571</td>
<td align="right">170.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">33,642</td>
<td align="right">90,321</td>
<td align="right">168.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">126,378</td>
<td align="right">312,375</td>
<td align="right">147.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">126,378</td>
<td align="right">312,375</td>
<td align="right">147.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,037,063</td>
<td align="right">4,922,148</td>
<td align="right">141.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">383,124</td>
<td align="right">918,069</td>
<td align="right">139.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">4,788</td>
<td align="right">11,130</td>
<td align="right">132.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">106,302</td>
<td align="right">240,135</td>
<td align="right">125.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">31,836</td>
<td align="right">71,610</td>
<td align="right">124.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">29,316</td>
<td align="right">64,785</td>
<td align="right">121.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">85,029</td>
<td align="right">186,084</td>
<td align="right">118.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">418,026</td>
<td align="right">911,127</td>
<td align="right">118.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,071,504</td>
<td align="right">2,316,963</td>
<td align="right">116.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">252,756</td>
<td align="right">522,711</td>
<td align="right">106.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">368,361</td>
<td align="right">744,660</td>
<td align="right">102.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">382,725</td>
<td align="right">769,797</td>
<td align="right">101.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">168,861</td>
<td align="right">339,486</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,174,509</td>
<td align="right">2,344,671</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">29,316</td>
<td align="right">58,359</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">14,238</td>
<td align="right">147</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">588,483</td>
<td align="right">1,150,422</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,424,850</td>
<td align="right">65,121</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">12,762,624</td>
<td align="right">24,534,873</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">171,339</td>
<td align="right">321,611</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,628,760</td>
<td align="right">2,969,085</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">1,527,036</td>
<td align="right">2,756,179</td>
<td align="right">80.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,038,050</td>
<td align="right">3,658,935</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5,628</td>
<td align="right">10,101</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">69,930</td>
<td align="right">125,076</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">5,628</td>
<td align="right">9,954</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">31,836</td>
<td align="right">56,272</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,012,661</td>
<td align="right">3,463,946</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">63,672</td>
<td align="right">105,987</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,695,540</td>
<td align="right">2,788,152</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">78,624</td>
<td align="right">127,575</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,592,889</td>
<td align="right">7,356,719</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,067,304</td>
<td align="right">1,680,777</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,020,411</td>
<td align="right">1,593,627</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">31,836</td>
<td align="right">49,623</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">923,202</td>
<td align="right">1,417,713</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">383,376</td>
<td align="right">580,692</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">576,576</td>
<td align="right">870,219</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">1,501,122</td>
<td align="right">2,253,237</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">805,770</td>
<td align="right">1,208,193</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">24,168,228</td>
<td align="right">36,198,562</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">19,866</td>
<td align="right">10,101</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">19,866</td>
<td align="right">10,101</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">19,866</td>
<td align="right">10,101</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">19,866</td>
<td align="right">10,101</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">19,866</td>
<td align="right">10,101</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">31,836</td>
<td align="right">47,460</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">391,608</td>
<td align="right">580,671</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">24,926,433</td>
<td align="right">36,797,230</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">61,110</td>
<td align="right">89,838</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">61,110</td>
<td align="right">89,838</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">2,834,391</td>
<td align="right">3,979,773</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,429,721</td>
<td align="right">3,379,609</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,227,658</td>
<td align="right">4,460,298</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,187,445</td>
<td align="right">1,634,871</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,076,145</td>
<td align="right">689,223</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,116,003</td>
<td align="right">1,515,258</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">238,014</td>
<td align="right">322,392</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">697,620</td>
<td align="right">938,448</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">689,346</td>
<td align="right">912,975</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">625,674</td>
<td align="right">817,110</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">42,968,478</td>
<td align="right">55,804,500</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">14,238</td>
<td align="right">10,101</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,679,349</td>
<td align="right">2,155,062</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,853,649</td>
<td align="right">2,361,437</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">584,850</td>
<td align="right">744,849</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">729,246</td>
<td align="right">927,423</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">1,499,190</td>
<td align="right">1,093,347</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,137,864</td>
<td align="right">1,442,238</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">553,014</td>
<td align="right">697,389</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">277,683</td>
<td align="right">349,608</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">758,205</td>
<td align="right">598,668</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">277,683</td>
<td align="right">334,425</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">160,916,259</td>
<td align="right">187,255,022</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">668,661</td>
<td align="right">760,959</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">18,504,717</td>
<td align="right">20,660,090</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,356,516</td>
<td align="right">1,199,478</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">136,247,076</td>
<td align="right">151,451,169</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">194,481</td>
<td align="right">179,991</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">19,277,055</td>
<td align="right">20,334,660</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">18,042,045</td>
<td align="right">19,007,270</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">24,090,087</td>
<td align="right">25,167,474</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">38,094,903</td>
<td align="right">39,503,166</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">19,471,410</td>
<td align="right">20,153,661</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">19,471,410</td>
<td align="right">20,153,661</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">43,305,696</td>
<td align="right">44,710,069</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,759,023</td>
<td align="right">1,815,030</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">979,965</td>
<td align="right">956,781</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">19,001,514</td>
<td align="right">19,430,082</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">16,135,875</td>
<td align="right">16,467,213</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">21,682,542</td>
<td align="right">22,045,194</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">21,682,542</td>
<td align="right">22,045,194</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">20,486,949</td>
<td align="right">20,792,922</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">21,005,628</td>
<td align="right">21,288,910</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">16,344,636</td>
<td align="right">16,535,823</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">24,409,497</td>
<td align="right">24,685,116</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">19,067,181</td>
<td align="right">19,210,863</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">754,005</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">754,005</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">5,628</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">5,628</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">1,302</td>
<td align="right">1,302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right"></td>
<td align="right">160,041</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right"></td>
<td align="right">144,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right"></td>
<td align="right">93,114</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right"></td>
<td align="right">75,936</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right"></td>
<td align="right">69,909</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right"></td>
<td align="right">69,909</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right"></td>
<td align="right">66,423</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">66,423</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">37,968</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">36,666</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right"></td>
<td align="right">32,214</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right"></td>
<td align="right">32,214</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right"></td>
<td align="right">32,214</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">30,996</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">27,573</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">25,977</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right"></td>
<td align="right">25,977</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right"></td>
<td align="right">25,977</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right"></td>
<td align="right">11,907</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">9,954</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">4,406</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">4,406</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">3,321</td>
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
<td align="right">441</td>
<td align="right">31.2%</td>
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
