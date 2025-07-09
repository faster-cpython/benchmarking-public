
# Pystats results

- benchmark: sqlglot_v2_transpile
- fork: python
- ref: c419af9e277bea7dd78f4defefc752fe93b0b8ec
- commit hash: c419af9
- commit date: 2025-06-28T00:18:44+08:00

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
<td align="right">140,478,302</td>
<td align="right">21.2%</td>
<td align="right">21.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">60,554,624</td>
<td align="right">9.2%</td>
<td align="right">30.4%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">36,651,058</td>
<td align="right">5.5%</td>
<td align="right">36.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">31,606,869</td>
<td align="right">4.8%</td>
<td align="right">40.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">31,077,963</td>
<td align="right">4.7%</td>
<td align="right">45.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">24,906,742</td>
<td align="right">3.8%</td>
<td align="right">49.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">22,934,046</td>
<td align="right">3.5%</td>
<td align="right">52.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,726,907</td>
<td align="right">3.0%</td>
<td align="right">55.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">18,181,616</td>
<td align="right">2.8%</td>
<td align="right">58.4%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">17,307,463</td>
<td align="right">2.6%</td>
<td align="right">61.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">16,190,587</td>
<td align="right">2.4%</td>
<td align="right">63.5%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,868,475</td>
<td align="right">2.1%</td>
<td align="right">65.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">13,076,222</td>
<td align="right">2.0%</td>
<td align="right">67.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,068,133</td>
<td align="right">2.0%</td>
<td align="right">69.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,779,117</td>
<td align="right">1.8%</td>
<td align="right">71.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">10,427,571</td>
<td align="right">1.6%</td>
<td align="right">72.9%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">9,345,289</td>
<td align="right">1.4%</td>
<td align="right">74.3%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,584,749</td>
<td align="right">1.3%</td>
<td align="right">75.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,772,181</td>
<td align="right">1.2%</td>
<td align="right">76.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7,015,962</td>
<td align="right">1.1%</td>
<td align="right">77.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,539,564</td>
<td align="right">1.0%</td>
<td align="right">78.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">6,061,671</td>
<td align="right">0.9%</td>
<td align="right">79.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">5,411,112</td>
<td align="right">0.8%</td>
<td align="right">80.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,959,717</td>
<td align="right">0.8%</td>
<td align="right">81.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,828,845</td>
<td align="right">0.7%</td>
<td align="right">82.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,745,613</td>
<td align="right">0.7%</td>
<td align="right">82.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,704,743</td>
<td align="right">0.7%</td>
<td align="right">83.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,701,748</td>
<td align="right">0.7%</td>
<td align="right">84.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,688,115</td>
<td align="right">0.7%</td>
<td align="right">84.9%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">4,607,195</td>
<td align="right">0.7%</td>
<td align="right">85.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,431,210</td>
<td align="right">0.7%</td>
<td align="right">86.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,267,747</td>
<td align="right">0.6%</td>
<td align="right">86.9%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,144,980</td>
<td align="right">0.6%</td>
<td align="right">87.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,558,408</td>
<td align="right">0.5%</td>
<td align="right">88.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,539,012</td>
<td align="right">0.5%</td>
<td align="right">88.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,313,366</td>
<td align="right">0.5%</td>
<td align="right">89.1%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">3,207,498</td>
<td align="right">0.5%</td>
<td align="right">89.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">3,070,560</td>
<td align="right">0.5%</td>
<td align="right">90.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,973,243</td>
<td align="right">0.4%</td>
<td align="right">90.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,973,039</td>
<td align="right">0.4%</td>
<td align="right">91.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,931,977</td>
<td align="right">0.4%</td>
<td align="right">91.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,801,622</td>
<td align="right">0.4%</td>
<td align="right">91.8%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,706,948</td>
<td align="right">0.4%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,621,199</td>
<td align="right">0.4%</td>
<td align="right">92.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,558,944</td>
<td align="right">0.4%</td>
<td align="right">93.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,514,168</td>
<td align="right">0.4%</td>
<td align="right">93.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,472,781</td>
<td align="right">0.4%</td>
<td align="right">93.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,469,768</td>
<td align="right">0.4%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,332,520</td>
<td align="right">0.4%</td>
<td align="right">94.5%</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,227,818</td>
<td align="right">0.3%</td>
<td align="right">94.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,213,538</td>
<td align="right">0.3%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,838,340</td>
<td align="right">0.3%</td>
<td align="right">95.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,740,483</td>
<td align="right">0.3%</td>
<td align="right">95.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,527,504</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,510,269</td>
<td align="right">0.2%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,429,155</td>
<td align="right">0.2%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,388,205</td>
<td align="right">0.2%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,318,098</td>
<td align="right">0.2%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,281,609</td>
<td align="right">0.2%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,279,817</td>
<td align="right">0.2%</td>
<td align="right">97.2%</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,070,425</td>
<td align="right">0.2%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,013,376</td>
<td align="right">0.2%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">937,755</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">920,672</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">911,169</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">860,055</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">809,619</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">777,231</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">752,745</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">700,314</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">634,662</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">630,441</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">620,985</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">565,089</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">565,089</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">565,089</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">548,730</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">541,569</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">511,119</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">462,873</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">450,450</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">401,310</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">357,446</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">335,859</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">261,933</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">237,411</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">200,655</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">192,534</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">184,149</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">135,114</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">124,824</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">118,755</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">114,597</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">91,354</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">83,399</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">81,837</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">69,684</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">65,589</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">53,130</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">49,138</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">49,098</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">45,045</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">45,045</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">45,045</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,802</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">32,829</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">32,760</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">32,739</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">28,665</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">28,623</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">24,609</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">24,570</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">24,570</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">24,555</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">20,544</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">18,816</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">12,354</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">12,285</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">11,429</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">9,576</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">8,190</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">8,169</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,164</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">4,143</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">4,095</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">4,095</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">4,095</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">4,095</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">4,074</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">4,074</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">4,071</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,247</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,806</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,008</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">462</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">252</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">48</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">42</td>
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
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_SLOT</td>
<td align="right">48,208,860</td>
<td align="right">7.3%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_FAST_BORROW</td>
<td align="right">22,893,591</td>
<td align="right">3.5%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_BORROW</td>
<td align="right">20,722,713</td>
<td align="right">3.1%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_BORROW</td>
<td align="right">19,712,244</td>
<td align="right">3.0%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">17,749,259</td>
<td align="right">2.7%</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">15,206,898</td>
<td align="right">2.3%</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST RETURN_VALUE</td>
<td align="right">13,915,773</td>
<td align="right">2.1%</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST_BORROW</td>
<td align="right">11,090,077</td>
<td align="right">1.7%</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">9,988,892</td>
<td align="right">1.5%</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW</td>
<td align="right">9,864,698</td>
<td align="right">1.5%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_BORROW</td>
<td align="right">9,443,275</td>
<td align="right">1.4%</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_FAST_BORROW</td>
<td align="right">8,969,541</td>
<td align="right">1.4%</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW STORE_ATTR_SLOT</td>
<td align="right">8,956,248</td>
<td align="right">1.4%</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">8,331,842</td>
<td align="right">1.3%</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE</td>
<td align="right">8,095,296</td>
<td align="right">1.2%</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE POP_JUMP_IF_FALSE</td>
<td align="right">7,752,385</td>
<td align="right">1.2%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST</td>
<td align="right">7,726,929</td>
<td align="right">1.2%</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_ATTR_SLOT</td>
<td align="right">7,172,062</td>
<td align="right">1.1%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT TO_BOOL_ALWAYS_TRUE</td>
<td align="right">7,016,878</td>
<td align="right">1.1%</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR</td>
<td align="right">6,850,914</td>
<td align="right">1.0%</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP POP_JUMP_IF_FALSE</td>
<td align="right">6,066,060</td>
<td align="right">0.9%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE TO_BOOL_NONE</td>
<td align="right">5,595,422</td>
<td align="right">0.8%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_GLOBAL_MODULE</td>
<td align="right">5,507,964</td>
<td align="right">0.8%</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">5,307,168</td>
<td align="right">0.8%</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL RESUME_CHECK</td>
<td align="right">4,659,627</td>
<td align="right">0.7%</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW COMPARE_OP</td>
<td align="right">4,545,534</td>
<td align="right">0.7%</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">4,538,223</td>
<td align="right">0.7%</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">4,397,909</td>
<td align="right">0.7%</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">4,324,988</td>
<td align="right">0.7%</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR CALL_PY_EXACT_ARGS</td>
<td align="right">4,300,716</td>
<td align="right">0.7%</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">4,246,395</td>
<td align="right">0.6%</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">4,128,117</td>
<td align="right">0.6%</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">4,114,968</td>
<td align="right">0.6%</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">4,026,603</td>
<td align="right">0.6%</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">4,016,565</td>
<td align="right">0.6%</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,927,058</td>
<td align="right">0.6%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_CONST</td>
<td align="right">3,923,556</td>
<td align="right">0.6%</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW TO_BOOL_NONE</td>
<td align="right">3,905,877</td>
<td align="right">0.6%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_ADD_INT</td>
<td align="right">3,780,357</td>
<td align="right">0.6%</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_SMALL_INT</td>
<td align="right">3,693,984</td>
<td align="right">0.6%</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW STORE_ATTR_SLOT</td>
<td align="right">3,575,021</td>
<td align="right">0.5%</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT POP_JUMP_IF_FALSE</td>
<td align="right">3,526,779</td>
<td align="right">0.5%</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW COPY</td>
<td align="right">3,502,065</td>
<td align="right">0.5%</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT SWAP</td>
<td align="right">3,501,981</td>
<td align="right">0.5%</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">COPY LOAD_ATTR_SLOT</td>
<td align="right">3,501,897</td>
<td align="right">0.5%</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">SWAP STORE_ATTR_SLOT</td>
<td align="right">3,501,897</td>
<td align="right">0.5%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,402,525</td>
<td align="right">0.5%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT COMPARE_OP_INT</td>
<td align="right">3,211,194</td>
<td align="right">0.5%</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW TO_BOOL_STR</td>
<td align="right">3,156,197</td>
<td align="right">0.5%</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,133,017</td>
<td align="right">0.5%</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST STORE_FAST</td>
<td align="right">3,088,570</td>
<td align="right">0.5%</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW RETURN_VALUE</td>
<td align="right">3,087,699</td>
<td align="right">0.5%</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_MODULE</td>
<td align="right">3,083,959</td>
<td align="right">0.5%</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS</td>
<td align="right">3,073,245</td>
<td align="right">0.5%</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,964,886</td>
<td align="right">0.4%</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_BORROW</td>
<td align="right">2,873,142</td>
<td align="right">0.4%</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,801,082</td>
<td align="right">0.4%</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT LOAD_FAST_BORROW</td>
<td align="right">2,765,259</td>
<td align="right">0.4%</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O RETURN_VALUE</td>
<td align="right">2,751,840</td>
<td align="right">0.4%</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE CALL_BUILTIN_O</td>
<td align="right">2,751,840</td>
<td align="right">0.4%</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,706,633</td>
<td align="right">0.4%</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW TO_BOOL_BOOL</td>
<td align="right">2,665,982</td>
<td align="right">0.4%</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">2,513,004</td>
<td align="right">0.4%</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">2,472,781</td>
<td align="right">0.4%</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE POP_JUMP_IF_TRUE</td>
<td align="right">2,438,046</td>
<td align="right">0.4%</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,403,975</td>
<td align="right">0.4%</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST STORE_FAST</td>
<td align="right">2,383,497</td>
<td align="right">0.4%</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_CONST</td>
<td align="right">2,252,457</td>
<td align="right">0.3%</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE</td>
<td align="right">2,228,584</td>
<td align="right">0.3%</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT COMPARE_OP_INT</td>
<td align="right">2,179,359</td>
<td align="right">0.3%</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR POP_JUMP_IF_TRUE</td>
<td align="right">2,175,732</td>
<td align="right">0.3%</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT CALL_PY_GENERAL</td>
<td align="right">2,157,855</td>
<td align="right">0.3%</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,155,986</td>
<td align="right">0.3%</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE LOAD_FAST_BORROW</td>
<td align="right">2,150,904</td>
<td align="right">0.3%</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER</td>
<td align="right">2,118,123</td>
<td align="right">0.3%</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK NOP</td>
<td align="right">2,108,862</td>
<td align="right">0.3%</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_CONST</td>
<td align="right">2,096,868</td>
<td align="right">0.3%</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR POP_JUMP_IF_FALSE</td>
<td align="right">2,084,124</td>
<td align="right">0.3%</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,076,470</td>
<td align="right">0.3%</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_SMALL_INT</td>
<td align="right">2,065,020</td>
<td align="right">0.3%</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_FAST</td>
<td align="right">1,994,265</td>
<td align="right">0.3%</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,968,021</td>
<td align="right">0.3%</td>
<td align="right">71.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,966,141</td>
<td align="right">0.3%</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,949,874</td>
<td align="right">0.3%</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,893,969</td>
<td align="right">0.3%</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,878,346</td>
<td align="right">0.3%</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST_BORROW</td>
<td align="right">1,857,723</td>
<td align="right">0.3%</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY RESUME_CHECK</td>
<td align="right">1,838,340</td>
<td align="right">0.3%</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST_BORROW</td>
<td align="right">1,826,853</td>
<td align="right">0.3%</td>
<td align="right">73.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,801,589</td>
<td align="right">0.3%</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_FAST_BORROW</td>
<td align="right">1,769,040</td>
<td align="right">0.3%</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CONTAINS_OP_DICT</td>
<td align="right">1,764,585</td>
<td align="right">0.3%</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">1,748,367</td>
<td align="right">0.3%</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,727,964</td>
<td align="right">0.3%</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,719,900</td>
<td align="right">0.3%</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,716,771</td>
<td align="right">0.3%</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT RETURN_VALUE</td>
<td align="right">1,711,668</td>
<td align="right">0.3%</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT CALL_PY_EXACT_ARGS</td>
<td align="right">1,706,985</td>
<td align="right">0.3%</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT LOAD_FAST_BORROW</td>
<td align="right">1,638,000</td>
<td align="right">0.2%</td>
<td align="right">75.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT TO_BOOL_BOOL</td>
<td align="right">1,627,194</td>
<td align="right">0.2%</td>
<td align="right">76.2%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,429,134</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">1,429,155</td>
<td align="right">100.0%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,073,226</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">990,360</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">397,131</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">28,665</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,285</td>
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
<td align="left">FOR_ITER</td>
<td align="right">2,118,123</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">371,511</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">12,264</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">12,222</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48</td>
<td align="right">0.0%</td>
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
<td align="right">4,246,395</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">184,338</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">546</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">442,218</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">99,309</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">42</td>
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
<td align="right">442,239</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">99,330</td>
<td align="right">18.3%</td>
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
<td align="right">450,450</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">12,285</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">138</td>
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
<td align="right">389,025</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">49,140</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">12,312</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4,095</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,053</td>
<td align="right">0.9%</td>
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
<td align="right">45,003</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">42</td>
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
<td align="right">45,045</td>
<td align="right">100.0%</td>
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
<td align="right">12,285</td>
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
<td align="right">12,285</td>
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
<td align="right">4,095</td>
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
<td align="right">4,095</td>
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
<td align="right">565,089</td>
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
<td align="right">565,089</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">601,944</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">397,215</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">331,695</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">49,098</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">8,190</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">819,000</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">315,315</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">253,890</td>
<td align="right">18.3%</td>
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
<td align="right">4,095</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">4,095</td>
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
<td align="right">4,128,117</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">303,093</td>
<td align="right">6.8%</td>
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
<td align="right">192,534</td>
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
<td align="right">159,705</td>
<td align="right">82.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">32,829</td>
<td align="right">17.1%</td>
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
<td align="right">2,108,862</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">310,422</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">209,622</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">172,011</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">171,990</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,719,900</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">925,539</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">327,600</td>
<td align="right">11.0%</td>
</tr>
</tbody>
</table>


</details>

### NOT_TAKEN

<details>
<summary> Successors and predecessors for NOT_TAKEN </summary>

<table>
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
<td align="right">357,383</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">286,146</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">37,742</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,356</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,752</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">4,725</td>
<td align="right">1.3%</td>
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
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">32,739</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">12,285</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">45,045</td>
<td align="right">100.0%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,430,589</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">388,359</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">371,841</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">12,285</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">10,311</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">864,045</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">653,343</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">442,260</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">192,402</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">24,570</td>
<td align="right">1.1%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">4,538,223</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">561,015</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">561,015</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">462,735</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">372,498</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">2,096,868</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,826,853</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">602,112</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">561,015</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">561,015</td>
<td align="right">8.0%</td>
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
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">32,739</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">12,285</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">44,961</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">84</td>
<td align="right">0.2%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,380,222</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">601,923</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">237,480</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">135,135</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">32,991</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">888,753</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">493,112</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">429,975</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">400,350</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">188,439</td>
<td align="right">7.6%</td>
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
<td align="right">159,642</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,570</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">12,222</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,074</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">126</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">184,065</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,285</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">4,095</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">210</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">13,915,773</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,307,168</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,087,699</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,751,840</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,711,668</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,595,422</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,307,168</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,538,223</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,128,117</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,114,968</td>
<td align="right">13.0%</td>
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
<td align="left">CALL</td>
<td align="right">63</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">63</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">42</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">42</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">42</td>
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
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">126</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">63</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">21</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21</td>
<td align="right">8.3%</td>
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
<td align="right">72,303</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,292</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,961</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">651</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">504</td>
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
<td align="right">72,540</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,628</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,100</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,512</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">630</td>
<td align="right">0.8%</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">24,549</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">21</td>
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
<td align="left">COPY</td>
<td align="right">24,570</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">89,565</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">546</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">294</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">274</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">210</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">89,439</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">274</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">213</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">168</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">168</td>
<td align="right">0.2%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">579,474</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">159,705</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">32,760</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">32,697</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">24,570</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">461,280</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">147,336</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">97,650</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">49,140</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">45,045</td>
<td align="right">4.9%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">442,260</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">32,760</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">28,644</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,285</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,190</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">413,595</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">65,520</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">28,623</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">16,380</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">12,285</td>
<td align="right">2.2%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">622,440</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">315,315</td>
<td align="right">33.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">601,965</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">290,745</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">32,760</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,190</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,095</td>
<td align="right">0.4%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,150,764</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">81,249</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">61,404</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,190</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,190</td>
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
<td align="left">SWAP</td>
<td align="right">561,015</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">450,450</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">142,611</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">57,330</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">49,125</td>
<td align="right">3.7%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">6,300</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,108</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,940</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,722</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">714</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,460</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,326</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,974</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,050</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">651</td>
<td align="right">3.5%</td>
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
<td align="left">LIST_APPEND</td>
<td align="right">12,285</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">69</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">12,285</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">69</td>
<td align="right">0.6%</td>
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
<td align="right">1,806</td>
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
<td align="right">756</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">399</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">210</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">147</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">126</td>
<td align="right">7.0%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,545,534</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,528,422</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">461,280</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,488</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">252</td>
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
<td align="right">6,066,060</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">461,280</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,190</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,488</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">294</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">32,949</td>
<td align="right">87.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,095</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">317</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">252</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">84</td>
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
<td align="right">37,107</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">317</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">168</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">147</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,502,065</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">745,269</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">241,605</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">208,803</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">94,185</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">3,501,897</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">629,559</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">540,662</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">77,010</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">53,866</td>
<td align="right">1.1%</td>
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
<td align="right">47,190</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,941</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,074</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">1,237</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">147</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">40,935</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">24,570</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">84</td>
<td align="right">0.1%</td>
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
<td align="right">405,405</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">28,665</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">8,190</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">8,190</td>
<td align="right">1.8%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">450,450</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,190</td>
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
<td align="left">DICT_MERGE</td>
<td align="right">8,190</td>
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
<td align="right">904,793</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">860,055</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">602,112</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">209,068</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">45,045</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,113,966</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">860,076</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">634,809</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,285</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">63</td>
<td align="right">0.0%</td>
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
<td align="right">2,118,123</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">811,450</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,404</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,461,205</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,079,274</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">388,359</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,404</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">357</td>
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
<td align="right">4,095</td>
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
<td align="left">STORE_FAST</td>
<td align="right">4,095</td>
<td align="right">100.0%</td>
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
<td align="left">CALL_TYPE_1</td>
<td align="right">241,584</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">90,090</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,095</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">69</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">COPY</td>
<td align="right">241,605</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">94,185</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">69</td>
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
<td align="right">315</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">231</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">126</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">84</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">84</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,008</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">28,644</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">21</td>
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
<td align="left">SEND_GEN</td>
<td align="right">28,644</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">21</td>
<td align="right">0.1%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">585,585</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">556,899</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">253,959</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">45,045</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">32,760</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">749,454</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">651,105</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">61,425</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">32,718</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">12,285</td>
<td align="right">0.8%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">114,660</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">4,095</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">102,375</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">12,285</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">4,074</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">21</td>
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
<td align="left">STORE_FAST</td>
<td align="right">20,475</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">69</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">20,475</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">69</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,850,914</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">833,517</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">36,792</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">22,335</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">10,500</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,300,716</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,528,422</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">781,872</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">360,150</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">339,759</td>
<td align="right">4.4%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,726,929</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,923,556</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,252,457</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,096,868</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,310,538</td>
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
<td align="right">13,915,773</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,383,497</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,769,040</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,291,695</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">622,440</td>
<td align="right">2.7%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">974,610</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">503,685</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">384,810</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">106,470</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">102,312</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,893,969</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">155,400</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">81,816</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">69,531</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">10,500</td>
<td align="right">0.5%</td>
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
<td align="right">1,330,335</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">794,430</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">746,676</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">712,467</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">442,239</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,994,265</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">990,360</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">446,229</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">352,044</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">327,558</td>
<td align="right">6.9%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">20,412</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,095</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">4,095</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">4,074</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">63</td>
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
<td align="left">SWAP</td>
<td align="right">28,665</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">4,095</td>
<td align="right">12.5%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">22,893,591</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">20,722,713</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">19,712,244</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">11,090,077</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">9,988,892</td>
<td align="right">7.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">48,208,860</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">15,206,898</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">8,956,248</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,545,534</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,324,988</td>
<td align="right">3.1%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">2,155,986</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,949,874</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,801,589</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,719,900</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,408,596</td>
<td align="right">10.8%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,575,021</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,727,964</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,716,771</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,199,751</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">844,347</td>
<td align="right">6.5%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">24,570</td>
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
<td align="right">24,528</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">42</td>
<td align="right">0.2%</td>
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
<td align="left">BUILD_STRING</td>
<td align="right">4,095</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">48</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">21</td>
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
<td align="left">COPY</td>
<td align="right">4,095</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">42</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">27</td>
<td align="right">0.6%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">2,331</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,953</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,176</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">987</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">756</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,423</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,856</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,365</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,218</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">210</td>
<td align="right">2.2%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,693,984</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,065,020</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">880,929</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">565,137</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">565,089</td>
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
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,403,975</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,179,359</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,638,000</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,179,192</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">569,274</td>
<td align="right">6.6%</td>
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
<td align="right">294,840</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">213,178</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">89,705</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">73,500</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">28,650</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">405,306</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">294,840</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">168</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,095</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">4,074</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">21</td>
<td align="right">0.5%</td>
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
<td align="right">8,331,842</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">7,752,385</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,066,060</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,026,603</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">3,526,779</td>
<td align="right">9.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">19,712,244</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,726,929</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,949,874</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,878,346</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">974,610</td>
<td align="right">2.7%</td>
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
<td align="right">600,510</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">16,380</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">4,074</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">588,225</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">28,623</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,095</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">42</td>
<td align="right">0.0%</td>
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
<td align="right">805,524</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,074</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">651,105</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">81,228</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">32,760</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">24,570</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">19,845</td>
<td align="right">2.5%</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">8,095,296</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,513,004</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,438,046</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,175,732</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">860,076</td>
<td align="right">5.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">11,090,077</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,577,325</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,519,203</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">868,140</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">746,676</td>
<td align="right">4.3%</td>
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
<td align="right">21</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">21</td>
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
<td align="left">POP_TOP</td>
<td align="right">21</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">21</td>
<td align="right">50.0%</td>
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
<td align="right">32,829</td>
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
<td align="right">24,570</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,148</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">69</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">42</td>
<td align="right">0.1%</td>
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
<td align="right">1,239</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">798</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">168</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">42</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,302</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">315</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">210</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">189</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">84</td>
<td align="right">3.7%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">69,615</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">48</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">69,615</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">69</td>
<td align="right">0.1%</td>
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
<td align="right">4,114,968</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,088,570</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,383,497</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,994,265</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,079,274</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,988,892</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,252,457</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,155,986</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,968,021</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,330,335</td>
<td align="right">6.7%</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">124,803</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">TO_BOOL_STR</td>
<td align="right">124,782</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">42</td>
<td align="right">0.0%</td>
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
<td align="right">2,472,781</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">85,953</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">210</td>
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
<td align="right">1,571,688</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">804,199</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">96,978</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">85,995</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">84</td>
<td align="right">0.0%</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,501,981</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">561,015</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">28,665</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">24,570</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">24,570</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,501,897</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">561,015</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">28,665</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">24,570</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">24,570</td>
<td align="right">0.6%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">252</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">84</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">42</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">42</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">42</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">210</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">168</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">63</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21</td>
<td align="right">4.5%</td>
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
<td align="right">229,320</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">85,995</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">57,330</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">28,665</td>
<td align="right">7.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">303,093</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">57,246</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">28,665</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,264</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">42</td>
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
<td align="left">CALL</td>
<td align="right">1,974</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">546</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">525</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">168</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">168</td>
<td align="right">4.4%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">2,520</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">378</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">189</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">189</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">147</td>
<td align="right">3.9%</td>
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
<td align="right">4,050</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21</td>
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
<td align="left">STORE_FAST</td>
<td align="right">4,071</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,780,357</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,179,192</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">168</td>
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
<td align="right">3,501,981</td>
<td align="right">70.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">888,552</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">569,163</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">21</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">359,667</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">311,094</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">61,383</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">28,623</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,148</td>
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
<td align="right">560,322</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">81,879</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">36,813</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">32,739</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">28,644</td>
<td align="right">3.7%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">8,148</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21</td>
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
<td align="right">8,169</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,727,964</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,159</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">234</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">1,711,668</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">12,285</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,074</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,074</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,074</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_OP_SUBSCR_LIST_SLICE

<details>
<summary> Successors and predecessors for BINARY_OP_SUBSCR_LIST_SLICE </summary>

<table>
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
<td align="right">4,053</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21</td>
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
<td align="right">4,074</td>
<td align="right">100.0%</td>
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
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,384,488</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,380,729</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">442,218</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,765,259</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">442,239</td>
<td align="right">13.8%</td>
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
<td align="right">27</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21</td>
<td align="right">43.8%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">48</td>
<td align="right">100.0%</td>
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
<td align="right">4,053</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">4,050</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">24</td>
<td align="right">0.6%</td>
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
<td align="right">2,403,975</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">565,068</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,053</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">147</td>
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
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,384,488</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">577,269</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">565,089</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">442,239</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,053</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">565,068</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="right">565,089</td>
<td align="right">100.0%</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">493,112</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">378,592</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,581</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,008</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,106</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">805,472</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">89,705</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">12,941</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,029</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">525</td>
<td align="right">0.1%</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">7,228</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,053</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">127</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">21</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">10,085</td>
<td align="right">88.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,237</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">107</td>
<td align="right">0.9%</td>
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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">16,338</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,080</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">4,053</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">84</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">16,359</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">4,122</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,074</td>
<td align="right">16.6%</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,199,751</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">49,056</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">28,623</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">4,053</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">634,641</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">601,923</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">28,644</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">16,338</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">42</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">565,068</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">565,089</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,751,840</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">761,460</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">32,718</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,243</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">147</td>
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
<td align="right">2,751,840</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">606,018</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">65,394</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">61,404</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">61,383</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,228,584</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,122,223</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">904,491</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">180,138</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">142,611</td>
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
<td align="right">4,397,909</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">208,803</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">483</td>
<td align="right">0.0%</td>
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
<td align="right">261,786</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">147</td>
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
<td align="right">257,859</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">4,074</td>
<td align="right">1.6%</td>
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
<td align="right">510,363</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">756</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">433,545</td>
<td align="right">84.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">73,500</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,074</td>
<td align="right">0.8%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">622,146</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">4,053</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,053</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">189</td>
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
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">565,068</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">32,697</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">16,359</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">8,106</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,074</td>
<td align="right">0.6%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">573,174</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">179,445</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">565,089</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">151,473</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">28,644</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,074</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,465</td>
<td align="right">0.5%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,966,141</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,495,011</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">417,606</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">392,826</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">335,706</td>
<td align="right">7.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">3,088,570</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,236,606</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">237,426</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">106,428</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">20,412</td>
<td align="right">0.4%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">24,528</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">24,528</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">42</td>
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
<td align="left">JUMP_FORWARD</td>
<td align="right">24,549</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">24,549</td>
<td align="right">50.0%</td>
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
<td align="right">2,706,633</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">315</td>
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
<td align="right">1,073,226</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">646,968</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">573,174</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">327,558</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">57,288</td>
<td align="right">2.1%</td>
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
<td align="left">RETURN_GENERATOR</td>
<td align="right">184,065</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">49,125</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,053</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">168</td>
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
<td align="right">167,811</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">49,167</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,359</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,074</td>
<td align="right">1.7%</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">16,266</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,148</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">168</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">27</td>
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
<td align="right">16,317</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,074</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,074</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">48</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">48</td>
<td align="right">0.2%</td>
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
<td align="right">4,324,988</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,300,716</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,073,245</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,706,985</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,291,695</td>
<td align="right">7.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">17,749,259</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">213,178</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">159,642</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">47,190</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,008</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,157,855</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,236,606</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">707,973</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">339,759</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">155,400</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">4,659,627</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">28,650</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,222</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,074</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">149</td>
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
<td align="right">28,581</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">42</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">28,623</td>
<td align="right">100.0%</td>
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
<td align="right">634,599</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">IS_OP</td>
<td align="right">241,584</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">241,563</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">151,494</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,211,194</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,179,359</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">8,106</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">8,106</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,053</td>
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
<td align="right">4,026,603</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,384,509</td>
<td align="right">25.6%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">671,496</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">160,524</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">148,407</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">32,718</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">231</td>
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
<td align="right">1,013,376</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,764,585</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,557,318</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">712,954</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">646,968</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">6,143</td>
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
<td align="right">3,526,779</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">712,975</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">442,239</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">6,122</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">683,613</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">438,441</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">151,473</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,122</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">168</td>
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
<td align="right">1,265,505</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,169</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,143</td>
<td align="right">0.5%</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">69,552</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,222</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">63</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">69,552</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">12,222</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">63</td>
<td align="right">0.1%</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">698,557</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">371,511</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">357</td>
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
<td align="right">698,584</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">371,841</td>
<td align="right">34.7%</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">4,074</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">48</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21</td>
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
<td align="left">STORE_FAST</td>
<td align="right">4,074</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">69</td>
<td align="right">1.7%</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">122,829</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,264</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">124,803</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">10,311</td>
<td align="right">7.6%</td>
</tr>
</tbody>
</table>


</details>

### JUMP_BACKWARD_JIT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_JIT </summary>

<table>
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
<td align="right">740,439</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">634,809</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">469,265</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">360,318</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">278,376</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,175,434</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">811,450</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">698,557</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">172,011</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">122,829</td>
<td align="right">4.0%</td>
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
<td align="right">28,581</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">20,349</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,179</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">32,718</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,095</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,074</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,053</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,053</td>
<td align="right">7.6%</td>
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
<td align="right">2,801,082</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">450</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">27</td>
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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,751,840</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">16,380</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">16,380</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">16,380</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">450</td>
<td align="right">0.0%</td>
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
<td align="right">15,206,898</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,927,058</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,893,969</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,224,657</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">929,838</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,443,275</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,507,964</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,073,245</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,706,633</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,157,855</td>
<td align="right">8.7%</td>
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
<td align="right">3,133,017</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">155,400</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,663</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,133</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">4,053</td>
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
<td align="right">2,873,142</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">319,200</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">53,172</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">28,455</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">20,391</td>
<td align="right">0.6%</td>
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
<td align="right">1,505,250</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,074</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">945</td>
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
<td align="left">CALL_ISINSTANCE</td>
<td align="right">904,491</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">237,480</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">171,864</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">122,640</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">36,792</td>
<td align="right">2.4%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,016,565</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,716,771</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">327,558</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">777</td>
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
<td align="right">1,706,985</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,557,318</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,224,657</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">683,613</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">560,994</td>
<td align="right">9.3%</td>
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
<td align="right">1,491,882</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">426,034</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">387,573</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">26,590</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">420</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">929,838</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">712,954</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">601,944</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">36,666</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">26,590</td>
<td align="right">1.1%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,473,696</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">327,558</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">32,718</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,053</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">315</td>
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
<td align="right">1,838,340</td>
<td align="right">100.0%</td>
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
<td align="right">48,208,860</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,172,062</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,501,897</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">844,347</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">446,229</td>
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
<td align="right">22,893,591</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,172,062</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">7,016,878</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,927,058</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,693,984</td>
<td align="right">6.1%</td>
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
<td align="right">3,402,525</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,964,886</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,968,021</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,878,346</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,519,203</td>
<td align="right">11.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">9,864,698</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,228,584</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,408,596</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">178,857</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">81,249</td>
<td align="right">0.6%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,507,964</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,083,959</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,748,367</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">708,225</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">671,370</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">6,850,914</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,857,723</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,505,250</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,285,773</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,122,223</td>
<td align="right">8.6%</td>
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
<td align="right">17,749,259</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,659,627</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">4,246,395</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,838,340</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">805,472</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">20,722,713</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,402,525</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,108,862</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,748,367</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,302,147</td>
<td align="right">4.2%</td>
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
<td align="right">28,644</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,074</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">21</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">28,665</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,074</td>
<td align="right">12.4%</td>
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
<td align="right">8,956,248</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,575,021</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,501,897</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">101,426</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">50,619</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,969,541</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,923,556</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,801,589</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">573,174</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">438,101</td>
<td align="right">2.7%</td>
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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">65,394</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">61,383</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">53,193</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,053</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">126</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">61,383</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">53,214</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">36,792</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">32,739</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,016,878</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,076,470</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">165,897</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">53,866</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">16,934</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,095,296</td>
<td align="right">86.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,218,149</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">16,934</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">14,910</td>
<td align="right">0.2%</td>
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
<td align="right">4,397,909</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,665,982</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,627,194</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">634,641</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">629,559</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,331,842</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,513,004</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">904,793</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">24,549</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,929</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">860,034</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
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
<td align="left">EXTENDED_ARG</td>
<td align="right">860,055</td>
<td align="right">100.0%</td>
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
<td align="right">28,364</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">20,391</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">320</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">63</td>
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
<td align="right">45,405</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,392</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">341</td>
<td align="right">0.7%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">5,595,422</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,905,877</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">540,662</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">194,820</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">111,563</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,752,385</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,438,046</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">209,068</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">14,929</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">7,892</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,156,197</td>
<td align="right">74.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">856,275</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">124,782</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">77,010</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">44,961</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,175,732</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,084,124</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">7,891</td>
<td align="right">0.2%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">57,288</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">57,246</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">63</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">85,953</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">28,644</td>
<td align="right">25.0%</td>
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
<td align="right">1,461,205</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,011,381</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27</td>
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
<td align="right">2,472,781</td>
<td align="right">100.0%</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,577,325</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">629,937</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">438,101</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">370,174</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">328,566</td>
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
<td align="left">POP_ITER</td>
<td align="right">1,430,589</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">387,573</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">357,383</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">310,422</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">296,473</td>
<td align="right">8.4%</td>
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
<td align="right">90,303</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,374,960</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,565</td>
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
<td align="right">1,053</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">232</td>
<td align="right">18.1%</td>
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
<td align="left">out of range</td>
<td align="right">231</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1</td>
<td align="right">0.4%</td>
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
<td align="right">1,429,155</td>
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
<td align="right">1,287,942</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">45,839,545</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,303,082</td>
<td align="right">2.8%</td>
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
<td align="right">33,956</td>
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
<td align="right">903</td>
<td align="right">50.0%</td>
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
<td align="right">903</td>
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
<td align="right">6,535,551</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,901,180</td>
<td align="right">69.5%</td>
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
<td align="right">525</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,488</td>
<td align="right">86.9%</td>
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
<td align="left">baseobject</td>
<td align="right">3,172</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">316</td>
<td align="right">9.1%</td>
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
<td align="right">37,170</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,092,449</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">650,861</td>
<td align="right">8.4%</td>
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
<td align="right">12,580</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">317</td>
<td align="right">2.5%</td>
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
<td align="right">190</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">127</td>
<td align="right">40.1%</td>
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
<td align="right">2,929,111</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,291,519</td>
<td align="right">30.6%</td>
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
<td align="right">462</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,404</td>
<td align="right">83.9%</td>
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
<td align="right">1,138</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">464</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">400</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">380</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">22</td>
<td align="right">0.9%</td>
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
<td align="left">other</td>
<td align="right">1,142,574</td>
<td align="right">1,142,574 / 0 !!</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">1,003,275</td>
<td align="right">1,003,275 / 0 !!</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">389,025</td>
<td align="right">389,025 / 0 !!</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">376,740</td>
<td align="right">376,740 / 0 !!</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">12,285</td>
<td align="right">12,285 / 0 !!</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,285</td>
<td align="right">12,285 / 0 !!</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">8,190</td>
<td align="right">8,190 / 0 !!</td>
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
<td align="right">7,737,561</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">506,772</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">158,872,692</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,517,371</td>
<td align="right">2.6%</td>
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
<td align="right">98,556</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">21,138</td>
<td align="right">17.7%</td>
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
<td align="right">16,996</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,042</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">697</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">127</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">127</td>
<td align="right">0.6%</td>
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
<td align="right">4,788</td>
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
<td align="right">26,932,156</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,452</td>
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
<td align="right">4,872</td>
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
<td align="right">21</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,739</td>
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
<td align="right">21</td>
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
<td align="right">945</td>
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
<td align="right">36,591,399</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,684,280</td>
<td align="right">6.8%</td>
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
<td align="right">51,921</td>
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
<td align="right">126</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">184,149</td>
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
<td align="right">126</td>
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
<td align="right">78,315</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,327,137</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,894,870</td>
<td align="right">9.7%</td>
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
<td align="right">77,676</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">485</td>
<td align="right">0.6%</td>
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
<td align="right">231</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">127</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">127</td>
<td align="right">26.2%</td>
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
<td align="right">231</td>
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
<td align="right">4,148,073</td>
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
<td align="right">231</td>
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
<td align="right">346,600,246</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">21,432,801</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">279,977,494</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">13,067,549</td>
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
<td align="right">7,737,561</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,535,551</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,929,111</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,429,155</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,287,942</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">90,303</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">78,315</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,170</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">945</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,684,280</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,517,391</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,691,950</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,501,950</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,410,027</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">650,565</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">638,542</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">565,310</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">418,900</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">325,579</td>
<td align="right">2.5%</td>
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
<td align="right">4,431,279</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">31,359,504</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">4,431,279</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">3,943,911</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">487,368</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">3,943,911</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">450,471</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">12,354</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,752,155</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">45,045</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">35,753,907</td>
<td align="right">99.9%</td>
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
<td align="right">22,674,904</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">22,675,234</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">15,116,774</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,087,579</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">29,090</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">14,780,649</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">683,865</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">169,697,792</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">204,487,833</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">132,786,796</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">132,149,217</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">12,395,927</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">14,843,057</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">101,497,224</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">85,291,222</td>
<td align="right">19.5%</td>
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
<td align="right">27,163,044</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,056,461</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,162,668</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">11,231,503</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">109,224</td>
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
<td align="right">661</td>
<td align="right">1,115,397</td>
<td align="right">12,638,821</td>
<td align="right">773,445</td>
<td align="right">1,254,936</td>
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
<td align="right">1,191</td>
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
<td align="right">635</td>
<td align="right">53.3%</td>
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
<td align="right">384</td>
<td align="right">32.2%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">21</td>
<td align="right">1.8%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">172</td>
<td align="right">14.4%</td>
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
<td align="right">4,445,961</td>
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
<td align="right">750,305,899</td>
<td align="right">16,876.1%</td>
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
<td align="right">635</td>
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
<td align="right">530</td>
<td align="right">83.5%</td>
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

### JIT memory stats

<details>
<summary> JIT memory stats </summary>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Size (bytes)</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">7,438,336</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">6,154,816</td>
<td align="right">82.7%</td>
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
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">159,376</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">1,124,144</td>
<td align="right">15.1%</td>
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
<th align="left">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 4,096</td>
<td align="left">107</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">148</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">170</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">42</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">63</td>
<td align="right">11.9%</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 16</td>
<td align="right">22</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">149</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">128</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">147</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">168</td>
<td align="right">26.5%</td>
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
<td align="left"><= 16</td>
<td align="right">86</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">150</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">168</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">42</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">84</td>
<td align="right">13.2%</td>
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
<th align="right">Count</th>
<th align="right">Self</th>
<th align="right">Cumulative</th>
<th align="right">Miss ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">_SET_IP</td>
<td align="right">145,398,833</td>
<td align="right">19.4%</td>
<td align="right">19.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">140,857,015</td>
<td align="right">18.8%</td>
<td align="right">38.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">75,909,852</td>
<td align="right">10.1%</td>
<td align="right">48.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">57,413,543</td>
<td align="right">7.7%</td>
<td align="right">55.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">23,085,092</td>
<td align="right">3.1%</td>
<td align="right">59.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">20,357,169</td>
<td align="right">2.7%</td>
<td align="right">61.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">16,550,777</td>
<td align="right">2.2%</td>
<td align="right">63.9%</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">16,214,184</td>
<td align="right">2.2%</td>
<td align="right">66.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">13,459,112</td>
<td align="right">1.8%</td>
<td align="right">67.9%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">13,156,677</td>
<td align="right">1.8%</td>
<td align="right">69.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">12,629,843</td>
<td align="right">1.7%</td>
<td align="right">71.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,143,535</td>
<td align="right">1.2%</td>
<td align="right">72.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,121,853</td>
<td align="right">1.2%</td>
<td align="right">73.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">8,776,899</td>
<td align="right">1.2%</td>
<td align="right">74.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">8,476,356</td>
<td align="right">1.1%</td>
<td align="right">76.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">8,196,279</td>
<td align="right">1.1%</td>
<td align="right">77.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">8,107,260</td>
<td align="right">1.1%</td>
<td align="right">78.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">8,107,260</td>
<td align="right">1.1%</td>
<td align="right">79.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">8,107,260</td>
<td align="right">1.1%</td>
<td align="right">80.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">8,106,924</td>
<td align="right">1.1%</td>
<td align="right">81.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">7,648,811</td>
<td align="right">1.0%</td>
<td align="right">82.5%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">6,930,483</td>
<td align="right">0.9%</td>
<td align="right">83.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">5,653,474</td>
<td align="right">0.8%</td>
<td align="right">84.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">5,323,313</td>
<td align="right">0.7%</td>
<td align="right">84.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,042,900</td>
<td align="right">0.7%</td>
<td align="right">85.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,697,574</td>
<td align="right">0.6%</td>
<td align="right">86.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">4,508,364</td>
<td align="right">0.6%</td>
<td align="right">86.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">4,508,364</td>
<td align="right">0.6%</td>
<td align="right">87.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">4,508,364</td>
<td align="right">0.6%</td>
<td align="right">88.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">4,508,364</td>
<td align="right">0.6%</td>
<td align="right">88.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">4,508,364</td>
<td align="right">0.6%</td>
<td align="right">89.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,495,055</td>
<td align="right">0.6%</td>
<td align="right">89.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,445,961</td>
<td align="right">0.6%</td>
<td align="right">90.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,445,961</td>
<td align="right">0.6%</td>
<td align="right">90.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">4,147,038</td>
<td align="right">0.6%</td>
<td align="right">91.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,053,630</td>
<td align="right">0.5%</td>
<td align="right">92.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">4,053,630</td>
<td align="right">0.5%</td>
<td align="right">92.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">4,053,294</td>
<td align="right">0.5%</td>
<td align="right">93.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">3,856,835</td>
<td align="right">0.5%</td>
<td align="right">93.6%</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,771,407</td>
<td align="right">0.5%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">3,716,828</td>
<td align="right">0.5%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">3,384,575</td>
<td align="right">0.5%</td>
<td align="right">95.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,836,004</td>
<td align="right">0.4%</td>
<td align="right">95.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">2,834,334</td>
<td align="right">0.4%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">2,718,954</td>
<td align="right">0.4%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,604,236</td>
<td align="right">0.3%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,550,637</td>
<td align="right">0.3%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,357,859</td>
<td align="right">0.3%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,778,549</td>
<td align="right">0.2%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">1,775,378</td>
<td align="right">0.2%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,611,752</td>
<td align="right">0.2%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">1,560,695</td>
<td align="right">0.2%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,560,695</td>
<td align="right">0.2%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">1,302,819</td>
<td align="right">0.2%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,294,435</td>
<td align="right">0.2%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">928,720</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">695,357</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">595,502</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">525,525</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">484,470</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">471,534</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">471,534</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">471,534</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">471,534</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">471,534</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">454,734</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">430,206</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">425,481</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">370,671</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">365,715</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">359,390</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">356,265</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">356,265</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">280,413</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">169,890</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">127,050</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">127,050</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">127,050</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">98,469</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">89,019</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">82,551</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">59,438</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">59,438</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">54,665</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">16,380</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">16,380</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">14,406</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">10,905</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">9,450</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">9,450</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">6,180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">4,725</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">4,725</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">4,725</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">2,910</td>
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
<td align="right">21</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-09
