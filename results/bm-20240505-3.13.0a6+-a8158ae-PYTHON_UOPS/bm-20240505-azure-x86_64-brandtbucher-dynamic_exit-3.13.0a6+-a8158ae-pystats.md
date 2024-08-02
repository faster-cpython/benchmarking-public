
# Pystats results

- benchmark: all
- fork: brandtbucher
- ref: dynamic-exit
- commit hash: a8158ae
- commit date: 2024-05-05T13:51:13-07:00

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
<td align="right">17,307,563,944</td>
<td align="right">17.8%</td>
<td align="right">17.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,041,305,193</td>
<td align="right">5.2%</td>
<td align="right">23.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,905,779,904</td>
<td align="right">5.1%</td>
<td align="right">28.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,692,459,908</td>
<td align="right">4.8%</td>
<td align="right">32.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,151,649,084</td>
<td align="right">4.3%</td>
<td align="right">37.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,939,170,286</td>
<td align="right">4.1%</td>
<td align="right">41.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,619,660,525</td>
<td align="right">3.7%</td>
<td align="right">44.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,305,695,718</td>
<td align="right">3.4%</td>
<td align="right">48.3%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,985,007,468</td>
<td align="right">3.1%</td>
<td align="right">51.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,824,339,145</td>
<td align="right">2.9%</td>
<td align="right">54.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,736,578,091</td>
<td align="right">2.8%</td>
<td align="right">57.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,327,553,600</td>
<td align="right">2.4%</td>
<td align="right">59.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,196,857,139</td>
<td align="right">2.3%</td>
<td align="right">61.8%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,194,878,674</td>
<td align="right">2.3%</td>
<td align="right">64.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,980,990,894</td>
<td align="right">2.0%</td>
<td align="right">66.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,629,929,687</td>
<td align="right">1.7%</td>
<td align="right">67.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,342,520,079</td>
<td align="right">1.4%</td>
<td align="right">69.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,258,281,214</td>
<td align="right">1.3%</td>
<td align="right">70.5%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,091,154,684</td>
<td align="right">1.1%</td>
<td align="right">71.6%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,076,369,883</td>
<td align="right">1.1%</td>
<td align="right">72.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,074,280,640</td>
<td align="right">1.1%</td>
<td align="right">73.8%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">988,414,034</td>
<td align="right">1.0%</td>
<td align="right">74.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">908,293,003</td>
<td align="right">0.9%</td>
<td align="right">75.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">855,729,080</td>
<td align="right">0.9%</td>
<td align="right">76.6%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">788,040,979</td>
<td align="right">0.8%</td>
<td align="right">77.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,863,593</td>
<td align="right">0.8%</td>
<td align="right">78.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">649,598,041</td>
<td align="right">0.7%</td>
<td align="right">78.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">604,802,039</td>
<td align="right">0.6%</td>
<td align="right">79.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">600,487,090</td>
<td align="right">0.6%</td>
<td align="right">80.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">556,283,044</td>
<td align="right">0.6%</td>
<td align="right">80.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">533,939,892</td>
<td align="right">0.5%</td>
<td align="right">81.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">524,605,789</td>
<td align="right">0.5%</td>
<td align="right">81.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">487,133,612</td>
<td align="right">0.5%</td>
<td align="right">82.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">483,216,810</td>
<td align="right">0.5%</td>
<td align="right">82.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">451,081,901</td>
<td align="right">0.5%</td>
<td align="right">83.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">447,801,390</td>
<td align="right">0.5%</td>
<td align="right">83.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,573,918</td>
<td align="right">0.4%</td>
<td align="right">84.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">398,860,671</td>
<td align="right">0.4%</td>
<td align="right">84.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">393,344,161</td>
<td align="right">0.4%</td>
<td align="right">85.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">378,228,187</td>
<td align="right">0.4%</td>
<td align="right">85.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">366,265,703</td>
<td align="right">0.4%</td>
<td align="right">85.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">364,490,184</td>
<td align="right">0.4%</td>
<td align="right">86.1%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">358,131,973</td>
<td align="right">0.4%</td>
<td align="right">86.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">354,837,720</td>
<td align="right">0.4%</td>
<td align="right">86.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">351,639,265</td>
<td align="right">0.4%</td>
<td align="right">87.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">349,590,739</td>
<td align="right">0.4%</td>
<td align="right">87.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">342,846,488</td>
<td align="right">0.4%</td>
<td align="right">87.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">326,755,390</td>
<td align="right">0.3%</td>
<td align="right">88.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">325,796,652</td>
<td align="right">0.3%</td>
<td align="right">88.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">306,487,764</td>
<td align="right">0.3%</td>
<td align="right">88.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">300,764,996</td>
<td align="right">0.3%</td>
<td align="right">89.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">295,041,407</td>
<td align="right">0.3%</td>
<td align="right">89.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">294,335,591</td>
<td align="right">0.3%</td>
<td align="right">89.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">294,334,179</td>
<td align="right">0.3%</td>
<td align="right">90.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">286,950,890</td>
<td align="right">0.3%</td>
<td align="right">90.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">280,299,737</td>
<td align="right">0.3%</td>
<td align="right">90.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">277,074,725</td>
<td align="right">0.3%</td>
<td align="right">91.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">276,267,353</td>
<td align="right">0.3%</td>
<td align="right">91.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">271,495,986</td>
<td align="right">0.3%</td>
<td align="right">91.6%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">253,372,652</td>
<td align="right">0.3%</td>
<td align="right">91.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">239,839,131</td>
<td align="right">0.2%</td>
<td align="right">92.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">231,492,853</td>
<td align="right">0.2%</td>
<td align="right">92.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">229,143,926</td>
<td align="right">0.2%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">228,725,864</td>
<td align="right">0.2%</td>
<td align="right">92.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">225,802,269</td>
<td align="right">0.2%</td>
<td align="right">93.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">218,428,286</td>
<td align="right">0.2%</td>
<td align="right">93.2%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">213,013,013</td>
<td align="right">0.2%</td>
<td align="right">93.5%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">208,197,642</td>
<td align="right">0.2%</td>
<td align="right">93.7%</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">202,650,957</td>
<td align="right">0.2%</td>
<td align="right">93.9%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">199,993,630</td>
<td align="right">0.2%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">199,482,461</td>
<td align="right">0.2%</td>
<td align="right">94.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">194,019,623</td>
<td align="right">0.2%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,242,208</td>
<td align="right">0.2%</td>
<td align="right">94.7%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">175,258,058</td>
<td align="right">0.2%</td>
<td align="right">94.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,840,037</td>
<td align="right">0.2%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">171,302,181</td>
<td align="right">0.2%</td>
<td align="right">95.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">162,164,652</td>
<td align="right">0.2%</td>
<td align="right">95.4%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">154,209,628</td>
<td align="right">0.2%</td>
<td align="right">95.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">150,012,528</td>
<td align="right">0.2%</td>
<td align="right">95.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,850,810</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">142,394,444</td>
<td align="right">0.1%</td>
<td align="right">96.0%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">127,949,769</td>
<td align="right">0.1%</td>
<td align="right">96.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">122,960,738</td>
<td align="right">0.1%</td>
<td align="right">96.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">120,149,971</td>
<td align="right">0.1%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">117,415,976</td>
<td align="right">0.1%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">113,851,815</td>
<td align="right">0.1%</td>
<td align="right">96.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">111,397,400</td>
<td align="right">0.1%</td>
<td align="right">96.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">106,432,679</td>
<td align="right">0.1%</td>
<td align="right">96.8%</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">105,831,786</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,485,616</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">102,943,590</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">98,868,424</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">92,073,718</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">91,966,262</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">91,122,338</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">91,116,078</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">89,459,674</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">88,330,170</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">86,572,046</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">84,974,313</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">82,924,447</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">82,879,854</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,509,048</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">73,645,531</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">73,485,019</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">72,046,194</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">69,205,556</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">66,028,463</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,003,275</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">60,425,999</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">55,983,707</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,783,526</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">50,845,974</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">50,350,954</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">49,532,506</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,697,959</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,957,284</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">45,982,160</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">45,299,732</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">44,920,745</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">44,846,226</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">42,793,885</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">42,109,749</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,240</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,680</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">38,089,451</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">36,454,489</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">34,142,737</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">34,087,465</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">33,197,766</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">30,385,907</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">28,333,678</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">24,373,016</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,462,662</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,469,955</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">16,031,546</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">14,656,790</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">14,649,027</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">14,615,067</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,836,362</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">11,642,749</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">11,381,886</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,889,205</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,365,108</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">8,724,551</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">8,104,137</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,095,340</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">8,000,960</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">7,623,842</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,296,400</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">7,218,510</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,470,307</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">3,005,926</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">2,795,002</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,512,465</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,432,595</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,128,396</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,111,480</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1,337,662</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">991,720</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">807,420</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">698,209</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">541,780</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">495,900</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">481,898</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">278,453</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">241,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">238,482</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">202,660</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">152,063</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">89,680</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">70,864</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">24,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">19,001</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">900</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
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
<td align="left">LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,861,798,291</td>
<td align="right">2.9%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">2,596,520,586</td>
<td align="right">2.7%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">2,298,183,033</td>
<td align="right">2.4%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">2,229,039,767</td>
<td align="right">2.3%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">1,880,501,799</td>
<td align="right">1.9%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">1,801,463,350</td>
<td align="right">1.9%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST</td>
<td align="right">1,788,804,834</td>
<td align="right">1.8%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">1,618,788,378</td>
<td align="right">1.7%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">1,293,126,159</td>
<td align="right">1.3%</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_SLOT</td>
<td align="right">1,043,174,170</td>
<td align="right">1.1%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">985,455,073</td>
<td align="right">1.0%</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">974,851,093</td>
<td align="right">1.0%</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">961,685,106</td>
<td align="right">1.0%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">POP_TOP ENTER_EXECUTOR</td>
<td align="right">915,520,012</td>
<td align="right">0.9%</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_FAST</td>
<td align="right">888,564,999</td>
<td align="right">0.9%</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">829,268,031</td>
<td align="right">0.9%</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST RETURN_VALUE</td>
<td align="right">809,875,829</td>
<td align="right">0.8%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR RETURN_VALUE</td>
<td align="right">797,848,709</td>
<td align="right">0.8%</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">762,507,585</td>
<td align="right">0.8%</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">715,237,696</td>
<td align="right">0.7%</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE INTERPRETER_EXIT</td>
<td align="right">710,762,322</td>
<td align="right">0.7%</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK POP_TOP</td>
<td align="right">702,483,542</td>
<td align="right">0.7%</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST INTERPRETER_EXIT</td>
<td align="right">674,590,582</td>
<td align="right">0.7%</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">666,506,564</td>
<td align="right">0.7%</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">639,297,994</td>
<td align="right">0.7%</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT</td>
<td align="right">633,602,931</td>
<td align="right">0.7%</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST POP_TOP</td>
<td align="right">616,181,608</td>
<td align="right">0.6%</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">592,147,418</td>
<td align="right">0.6%</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST</td>
<td align="right">589,927,774</td>
<td align="right">0.6%</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">585,735,067</td>
<td align="right">0.6%</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">584,311,378</td>
<td align="right">0.6%</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">548,463,593</td>
<td align="right">0.6%</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST COMPARE_OP_INT</td>
<td align="right">545,177,180</td>
<td align="right">0.6%</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS</td>
<td align="right">533,213,262</td>
<td align="right">0.5%</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE YIELD_VALUE</td>
<td align="right">531,072,804</td>
<td align="right">0.5%</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT SEND_GEN</td>
<td align="right">530,964,612</td>
<td align="right">0.5%</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_BOOL</td>
<td align="right">497,068,217</td>
<td align="right">0.5%</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST</td>
<td align="right">484,774,859</td>
<td align="right">0.5%</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">477,978,180</td>
<td align="right">0.5%</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR YIELD_VALUE</td>
<td align="right">476,423,431</td>
<td align="right">0.5%</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">474,321,083</td>
<td align="right">0.5%</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">469,727,651</td>
<td align="right">0.5%</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST</td>
<td align="right">457,534,681</td>
<td align="right">0.5%</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">453,134,592</td>
<td align="right">0.5%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">POP_TOP RESUME_CHECK</td>
<td align="right">451,475,746</td>
<td align="right">0.5%</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN ENTER_EXECUTOR</td>
<td align="right">442,931,000</td>
<td align="right">0.5%</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">441,685,075</td>
<td align="right">0.5%</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_SLOT</td>
<td align="right">437,319,486</td>
<td align="right">0.5%</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST STORE_FAST</td>
<td align="right">432,190,431</td>
<td align="right">0.4%</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">420,092,778</td>
<td align="right">0.4%</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST PUSH_NULL</td>
<td align="right">413,101,689</td>
<td align="right">0.4%</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">408,573,426</td>
<td align="right">0.4%</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">408,496,387</td>
<td align="right">0.4%</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">396,356,816</td>
<td align="right">0.4%</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST</td>
<td align="right">379,743,264</td>
<td align="right">0.4%</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">375,928,899</td>
<td align="right">0.4%</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_FAST</td>
<td align="right">375,867,195</td>
<td align="right">0.4%</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">368,041,399</td>
<td align="right">0.4%</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">362,464,330</td>
<td align="right">0.4%</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">361,466,787</td>
<td align="right">0.4%</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL</td>
<td align="right">361,136,489</td>
<td align="right">0.4%</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">355,454,863</td>
<td align="right">0.4%</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE RETURN_CONST</td>
<td align="right">351,687,172</td>
<td align="right">0.4%</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE POP_JUMP_IF_FALSE</td>
<td align="right">349,974,803</td>
<td align="right">0.4%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">345,570,457</td>
<td align="right">0.4%</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST_LOAD_FAST</td>
<td align="right">345,087,547</td>
<td align="right">0.4%</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_CONST</td>
<td align="right">337,728,102</td>
<td align="right">0.3%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">334,974,979</td>
<td align="right">0.3%</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE</td>
<td align="right">331,707,205</td>
<td align="right">0.3%</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL STORE_FAST</td>
<td align="right">322,019,730</td>
<td align="right">0.3%</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST BINARY_SUBSCR_STR_INT</td>
<td align="right">319,624,166</td>
<td align="right">0.3%</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">315,265,667</td>
<td align="right">0.3%</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">309,285,524</td>
<td align="right">0.3%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST</td>
<td align="right">307,824,169</td>
<td align="right">0.3%</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">POP_TOP RETURN_CONST</td>
<td align="right">301,525,066</td>
<td align="right">0.3%</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE TO_BOOL_BOOL</td>
<td align="right">298,902,286</td>
<td align="right">0.3%</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST_LOAD_FAST</td>
<td align="right">298,212,745</td>
<td align="right">0.3%</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_LOAD_FAST</td>
<td align="right">297,343,137</td>
<td align="right">0.3%</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST BINARY_OP_SUBTRACT_INT</td>
<td align="right">296,609,945</td>
<td align="right">0.3%</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE CALL_ISINSTANCE</td>
<td align="right">294,513,517</td>
<td align="right">0.3%</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE</td>
<td align="right">290,853,551</td>
<td align="right">0.3%</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_FAST</td>
<td align="right">276,515,317</td>
<td align="right">0.3%</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK NOP</td>
<td align="right">276,063,486</td>
<td align="right">0.3%</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">272,697,810</td>
<td align="right">0.3%</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">265,748,725</td>
<td align="right">0.3%</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O POP_TOP</td>
<td align="right">263,265,911</td>
<td align="right">0.3%</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR POP_JUMP_IF_FALSE</td>
<td align="right">256,944,799</td>
<td align="right">0.3%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN POP_TOP</td>
<td align="right">255,635,115</td>
<td align="right">0.3%</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST SEND_GEN</td>
<td align="right">255,208,081</td>
<td align="right">0.3%</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN</td>
<td align="right">254,302,681</td>
<td align="right">0.3%</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT RETURN_CONST</td>
<td align="right">253,867,006</td>
<td align="right">0.3%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST BINARY_OP_ADD_INT</td>
<td align="right">252,549,475</td>
<td align="right">0.3%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_BUILTIN_O</td>
<td align="right">248,110,733</td>
<td align="right">0.3%</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST COMPARE_OP_STR</td>
<td align="right">247,736,807</td>
<td align="right">0.3%</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">247,121,015</td>
<td align="right">0.3%</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O POP_TOP</td>
<td align="right">242,131,962</td>
<td align="right">0.2%</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST STORE_FAST</td>
<td align="right">239,543,249</td>
<td align="right">0.2%</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE RETURN_CONST</td>
<td align="right">235,831,535</td>
<td align="right">0.2%</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_WITH_HINT</td>
<td align="right">235,187,611</td>
<td align="right">0.2%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST</td>
<td align="right">233,305,430</td>
<td align="right">0.2%</td>
<td align="right">61.3%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">121,365,226</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">30,502,940</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">26,564,557</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">10,106,000</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,426,080</td>
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
<td align="left">STORE_FAST</td>
<td align="right">34,719,507</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,167,140</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">32,122,360</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">30,258,805</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">25,332,480</td>
<td align="right">13.1%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">7,290,220</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">6,000</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">7,241,500</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">50,300</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">600</td>
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
<td align="right">1,880,501,799</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">162,045,097</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">97,291,948</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">46,677,304</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,007,418</td>
<td align="right">0.4%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">153,228,323</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">64,773,888</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">38,568,722</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">30,088,600</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">6,404,698</td>
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
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">62,535,860</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60,503,065</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">45,123,852</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">44,235,795</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">27,505,820</td>
<td align="right">9.1%</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">33,146,666</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">51,100</td>
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
<td align="left">POP_TOP</td>
<td align="right">33,196,246</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,520</td>
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
<td align="right">145,432,418</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">46,115,688</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">35,426,423</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">30,258,805</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">18,059,501</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">88,387,461</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">75,221,262</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">52,753,991</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">47,670,513</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">35,369,354</td>
<td align="right">10.1%</td>
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
<td align="right">762,507,585</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">710,762,322</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">674,590,582</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">47,018,185</td>
<td align="right">2.1%</td>
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
<td align="right">60,425,999</td>
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
<td align="right">49,976,898</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,555,020</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,958,543</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">785,190</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">355,592</td>
<td align="right">0.6%</td>
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
<td align="right">276,063,486</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">148,437,204</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">51,201,996</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">48,944,177</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">45,178,778</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">345,087,547</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">183,446,766</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">48,944,177</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,278,377</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">17,807,387</td>
<td align="right">2.7%</td>
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
<td align="right">702,483,542</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">616,181,608</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">263,265,911</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">255,635,115</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">242,131,962</td>
<td align="right">8.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">961,685,106</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">915,520,012</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">451,475,746</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">301,525,066</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">146,094,569</td>
<td align="right">4.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">413,101,689</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">408,573,426</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">73,787,032</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">35,868,562</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">27,458,740</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">441,685,075</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">298,212,745</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">101,265,996</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">100,976,342</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,402,979</td>
<td align="right">1.9%</td>
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
<td align="right">224,629,409</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">46,677,304</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">38,629,905</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">34,456,395</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">9,375,423</td>
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
<td align="left">GET_AWAITABLE</td>
<td align="right">207,312,042</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">47,018,185</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">28,107,909</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">17,965,454</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">17,930,280</td>
<td align="right">5.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">809,875,829</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">797,848,709</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">585,735,067</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">290,853,551</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">169,974,063</td>
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
<td align="left">STORE_FAST</td>
<td align="right">829,268,031</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">762,507,585</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">585,735,067</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">298,902,286</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">220,613,822</td>
<td align="right">6.1%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">42,747,082</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,776,900</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,362,174</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,294,962</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,613,560</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">47,857,535</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,336,994</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,012,380</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,738,340</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">691,800</td>
<td align="right">1.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">108,087,126</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">75,344,644</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">10,292,460</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,489,064</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,282,506</td>
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
<td align="right">105,987,517</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">93,391,257</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">178,202</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">151,301</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">107,798</td>
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
<td align="right">103,076,480</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,124,489</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,607,500</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">800,960</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">346,663</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">94,604,080</td>
<td align="right">84.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,266,380</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,122,420</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,483,403</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">820,220</td>
<td align="right">0.7%</td>
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
<td align="right">111,942,366</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">92,944,408</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">58,656,073</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">38,666,820</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">15,896,504</td>
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
<td align="left">STORE_FAST</td>
<td align="right">117,367,243</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">67,826,894</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">36,291,741</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">23,080,051</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">21,500,970</td>
<td align="right">5.5%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">65,171,942</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">758,533</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">71,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20</td>
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
<td align="right">65,588,313</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">411,122</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,840</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">135,920,956</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">65,572,082</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">49,816,998</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">34,733,924</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">32,167,140</td>
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
<td align="right">169,974,063</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">50,521,161</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">37,867,493</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">30,908,630</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">16,649,242</td>
<td align="right">4.5%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">45,364,727</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">37,560,494</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,457,296</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,386,294</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,930,316</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">44,076,472</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">42,718,888</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,107,760</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">13,407,076</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,364,810</td>
<td align="right">3.4%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">131,106,039</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">38,087,691</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,467,862</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">9,122,337</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">8,236,926</td>
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
<td align="left">POP_TOP</td>
<td align="right">109,157,001</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">25,677,710</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">25,043,707</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">23,590,280</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,303,562</td>
<td align="right">2.2%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">33,193,779</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,469,735</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,336,995</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,152,834</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,403,300</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">75,474,593</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">14,459,225</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,522,540</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">3,442,638</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,034,320</td>
<td align="right">1.9%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">12,982,244</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,822,839</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,269,897</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,236,174</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,784,023</td>
<td align="right">8.2%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">26,549,674</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">16,744,827</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">707,100</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">698,500</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">602,541</td>
<td align="right">1.3%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">164,805,289</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">112,025,916</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">19,191,869</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">16,038,820</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">14,273,240</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">153,389,407</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">111,084,603</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">41,906,695</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,269,920</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">15,814,260</td>
<td align="right">4.0%</td>
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
<td align="right">97,291,948</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">77,776,880</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">36,972,398</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,721,564</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">4,875,936</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">192,739,622</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">38,629,905</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">17,385</td>
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
<td align="right">915,520,012</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">442,931,000</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">227,877,978</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">176,053,256</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">150,444,652</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">797,848,709</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">477,978,180</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">476,423,431</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">146,891,851</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">131,106,039</td>
<td align="right">4.8%</td>
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
<td align="right">52,753,991</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,561,568</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">14,096,279</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">285,094</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">122,909</td>
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
<td align="right">46,750,323</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">18,702,508</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,556,867</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,619,259</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,867,788</td>
<td align="right">2.3%</td>
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
<td align="right">1,539,322</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">193,486</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">140,648</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">118,772</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">87,943</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,495,077</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">285,094</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">181,805</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">139,836</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">101,180</td>
<td align="right">4.2%</td>
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
<td align="right">161,421,946</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">100,928,977</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">46,203,996</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,766,219</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">6,406,760</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">144,433,506</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">77,043,225</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">49,028,263</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">36,787,021</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">17,990,021</td>
<td align="right">5.2%</td>
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
<td align="right">334,974,979</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">96,958,045</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">32,867,171</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">27,397,832</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,770,724</td>
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
<td align="left">STORE_FAST</td>
<td align="right">75,931,907</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">75,635,696</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">62,278,461</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">54,295,243</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">47,443,045</td>
<td align="right">8.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,788,804,834</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">337,728,102</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">229,908,047</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">229,143,926</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">208,354,196</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">888,564,999</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">545,177,180</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">337,728,102</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">296,609,945</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">255,208,081</td>
<td align="right">5.4%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">118,673,877</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">71,196,788</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">64,932,910</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">36,067,708</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">33,058,543</td>
<td align="right">6.3%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">158,217,209</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">88,758,840</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">73,787,032</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">27,397,832</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">25,773,311</td>
<td align="right">4.9%</td>
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
<td align="right">2,596,520,586</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,298,183,033</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,229,039,767</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,293,126,159</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">961,685,106</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,861,798,291</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,788,804,834</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,043,174,170</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">974,851,093</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">809,875,829</td>
<td align="right">4.7%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">457,534,681</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">379,743,264</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">375,928,899</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">345,087,547</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">315,265,667</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">633,602,931</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">361,466,787</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">355,454,863</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">319,624,166</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">315,265,667</td>
<td align="right">8.0%</td>
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
<td align="right">19,550,584</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">141,660</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">134,456</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">90,369</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">65,793</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">19,589,775</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">333,852</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">182,315</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">131,872</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60,970</td>
<td align="right">0.3%</td>
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
<td align="right">18,581</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">260</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">120</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20</td>
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
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">8,180</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,540</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,261</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,400</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,240</td>
<td align="right">6.5%</td>
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
<td align="right">45,781,227</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">31,386,106</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">4,303,562</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">2,151,625</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,276,776</td>
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
<td align="left">MAKE_CELL</td>
<td align="right">45,781,227</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">40,073,973</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">703,906</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">12,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">80</td>
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
<td align="right">1,618,788,378</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">985,455,073</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">349,974,803</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">256,944,799</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">224,567,932</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">2,229,039,767</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">351,687,172</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">331,707,205</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">254,302,681</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">233,305,430</td>
<td align="right">5.6%</td>
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
<td align="right">220,320,866</td>
<td align="right">74.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">31,047,516</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">19,376,481</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">11,350,603</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,142,265</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">192,094,813</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">36,067,708</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">33,701,652</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,629,714</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,772,351</td>
<td align="right">2.3%</td>
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
<td align="right">368,041,399</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">68,395,370</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9,726,640</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,521,062</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,005,640</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">168,630,309</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">128,044,476</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">74,853,459</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">19,900,171</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">19,841,368</td>
<td align="right">4.4%</td>
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
<td align="right">592,147,418</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">93,391,257</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,955,405</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">44,818,686</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">32,680,156</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">484,774,859</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">227,877,978</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">59,670,179</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">56,710,635</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20,482,780</td>
<td align="right">2.3%</td>
</tr>
</tbody>
</table>


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

<table>
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
<td align="right">351,687,172</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">301,525,066</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">253,867,006</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">235,831,535</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">146,891,851</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">674,590,582</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">616,181,608</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">91,116,078</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">69,100,760</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">63,981,867</td>
<td align="right">3.9%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">125,984,080</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">28,894,089</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">18,900,085</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">61,143</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">580</td>
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
<td align="left">END_SEND</td>
<td align="right">146,801,461</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">18,949,840</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">8,000,000</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">61,143</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">10,307</td>
<td align="right">0.0%</td>
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
<td align="right">49,976,898</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">374,056</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">25,346,340</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,473,918</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">9,563,347</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,000,640</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">567,017</td>
<td align="right">1.1%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">24,631,725</td>
<td align="right">72.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,042,813</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">801,120</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">566,722</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">341,950</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">17,938,502</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">4,436,979</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,475,943</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,323,156</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,197,294</td>
<td align="right">6.4%</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">35,847,842</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">25,576,980</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,109,116</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,743,940</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,599,540</td>
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
<td align="left">STORE_FAST</td>
<td align="right">28,914,260</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">19,784,027</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17,926,002</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,946,810</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,259,340</td>
<td align="right">6.8%</td>
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
<td align="right">829,268,031</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">432,190,431</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">322,019,730</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">239,543,249</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">232,095,230</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">2,596,520,586</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">432,190,431</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">396,356,816</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">375,928,899</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">226,403,947</td>
<td align="right">4.6%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">115,576,454</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">35,369,274</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">28,473,629</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">23,442,879</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">18,791,483</td>
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
<td align="left">COPY</td>
<td align="right">112,025,916</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">42,366,215</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">23,400,063</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">17,601,077</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,702,090</td>
<td align="right">5.4%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">249,408</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">128,400</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">43,050</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">19,601</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">8,424</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">433,556</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">24,822</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,779</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5,146</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">3,355</td>
<td align="right">0.7%</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">531,072,804</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">476,423,431</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">125,515,680</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">41,716,800</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">33,224,260</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">710,762,322</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">531,072,804</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">76,703,810</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">14,359,260</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,743,940</td>
<td align="right">0.5%</td>
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
<td align="right">101,580</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">82,249</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">19,228</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,712</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">17,385</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">110,961</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">65,793</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">25,879</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">23,380</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">12,301</td>
<td align="right">4.4%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">252,549,475</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">77,690,840</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">64,790,131</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">30,053,204</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">19,422,680</td>
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
<td align="left">STORE_FAST</td>
<td align="right">153,328,546</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">136,679,261</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">35,847,842</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">35,817,648</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">28,473,629</td>
<td align="right">5.9%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">38,338,619</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">11,842,820</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">11,760,960</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">5,269,240</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,532,748</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">37,915,203</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,571,756</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">11,760,960</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">2,510,147</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,599,920</td>
<td align="right">2.2%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">296,609,945</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">25,134,759</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,781,144</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">11,055,860</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,320,640</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">209,759,960</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">38,610,167</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">37,542,397</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">18,321,569</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,388,801</td>
<td align="right">4.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">225,954,912</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">31,964,028</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">23,273,760</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">23,204,588</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">17,388,801</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">105,403,763</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">50,836,581</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">47,489,960</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">36,129,520</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">25,935,481</td>
<td align="right">7.3%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">157,632,745</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,657,483</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,525</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">60</td>
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
<td align="right">95,999,840</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20,543,720</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,273,436</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,477,929</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,461,080</td>
<td align="right">3.8%</td>
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
<td align="left">CALL_LEN</td>
<td align="right">26,371,292</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,887,699</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,720,426</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,099,532</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,487,302</td>
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
<td align="left">GET_ITER</td>
<td align="right">46,115,688</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">25,180,032</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">9,570,487</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,829,000</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,307,882</td>
<td align="right">4.5%</td>
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
<td align="right">154,977,200</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">30,744,160</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">25,410,072</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,829,000</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,114,840</td>
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
<td align="left">STORE_FAST</td>
<td align="right">40,884,225</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">39,862,910</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">35,164,581</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">26,371,292</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,893,663</td>
<td align="right">7.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">132,571,820</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">112,790,589</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">101,265,996</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">95,999,840</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">43,004,643</td>
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
<td align="right">322,019,730</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">65,031,555</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">55,895,029</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">49,816,998</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">40,683,241</td>
<td align="right">6.7%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">548,463,593</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">533,213,262</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">361,466,787</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">209,759,960</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">153,385,564</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,801,463,350</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">224,629,409</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">77,776,880</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,845,780</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">31,386,106</td>
<td align="right">1.4%</td>
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
<td align="right">91,135,704</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">38,775,471</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">17,965,454</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">16,473,155</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">11,201,440</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">192,362,676</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">9,375,423</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">5,721,564</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,074,294</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,276,776</td>
<td align="right">0.6%</td>
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
<td align="right">4,737,848</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,686,740</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">699,603</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">585,140</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">89,660</td>
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
<td align="left">BINARY_OP</td>
<td align="right">4,825,708</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,344,060</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">756,956</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">332,820</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">234,940</td>
<td align="right">2.4%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">545,177,180</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">113,491,877</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">111,084,603</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">63,590,701</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">48,343,240</td>
<td align="right">4.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">985,455,073</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">32,680,156</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">30,053,893</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">10,226,880</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,330,140</td>
<td align="right">0.6%</td>
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
<td align="right">33,160,473</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">438,780</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">192,560</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">184,622</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">95,140</td>
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
<td align="left">POP_TOP</td>
<td align="right">33,801,455</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">152,780</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">78,800</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">51,094</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">50,448</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">88,617,567</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">75,221,262</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,376,155</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,494,011</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,495,077</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">74,636,649</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">70,351,894</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">14,732,147</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,847,042</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,456,440</td>
<td align="right">2.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">32,132,720</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">9,891,983</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,855,520</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">668,800</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">139,836</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">25,353,644</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">22,043,296</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">225,780</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">38,960</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">24,953</td>
<td align="right">0.1%</td>
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
<td align="right">474,321,083</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,741,927</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,064,051</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">585,800</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">223,400</td>
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
<td align="right">408,573,426</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">25,834,554</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,397,618</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,395,404</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,741,927</td>
<td align="right">1.4%</td>
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
<td align="right">666,506,564</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">408,496,387</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">254,302,681</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">226,403,947</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">60,572,307</td>
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
<td align="right">1,293,126,159</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">221,808,362</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">71,196,788</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">63,255,862</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">60,572,307</td>
<td align="right">3.1%</td>
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
<td align="right">639,297,994</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">469,727,651</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">396,356,816</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">331,707,205</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">117,787,509</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">589,927,774</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">474,321,083</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">457,534,681</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">294,513,517</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">153,385,564</td>
<td align="right">5.4%</td>
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
<td align="right">1,880,501,799</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,801,463,350</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">451,475,746</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">192,739,622</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">192,362,676</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">2,298,183,033</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">702,483,542</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">666,506,564</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">469,727,651</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">297,343,137</td>
<td align="right">5.9%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">33,650,860</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">30,323,339</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,786,889</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">852,180</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">842,720</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">31,175,120</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">22,523,640</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">14,813,848</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">6,317,560</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,202,720</td>
<td align="right">4.1%</td>
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
<td align="right">64,578,027</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,835,871</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">4,895,892</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,649,541</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,857,888</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">74,036,759</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">13,792,936</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">397,041</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">77,544</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,262</td>
<td align="right">0.0%</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">91,116,078</td>
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
<td align="right">91,116,078</td>
<td align="right">100.0%</td>
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
<td align="right">3,442,638</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,977,606</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">673,860</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">397,041</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">91,537</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">4,581,340</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,326,400</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">970,859</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">373,440</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">295,840</td>
<td align="right">3.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">29,940,945</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">23,400,063</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,838,162</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">8,638,625</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,529,677</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">40,092,151</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">36,773,605</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">23,442,879</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,410,489</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">3,038,641</td>
<td align="right">2.5%</td>
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
<td align="right">148,059,195</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">80,665,269</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,400</td>
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
<td align="right">101,801,139</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">65,230,770</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">25,035,772</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">11,041,855</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">9,945,827</td>
<td align="right">4.3%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">140,468,249</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">88,378,253</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">52,760,484</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,711,788</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,030,777</td>
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
<td align="right">224,567,932</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">44,955,405</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">23,812,440</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,117,380</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">13,522,702</td>
<td align="right">4.2%</td>
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
<td align="left">CALL</td>
<td align="right">42,718,888</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">17,930,280</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,398,557</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">7,068,201</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,558,345</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">84,665,825</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">140,648</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">128,080</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">23,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,880</td>
<td align="right">0.0%</td>
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
<td align="right">35,369,354</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">20,614,273</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">80</td>
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
<td align="right">35,369,274</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">20,614,273</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">160</td>
<td align="right">0.0%</td>
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
<td align="right">14,732,147</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,997,963</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,410,122</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">567,481</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">242,260</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">12,206,598</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,861,361</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,409,438</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,154,101</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">414,340</td>
<td align="right">2.1%</td>
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
<td align="right">247,121,015</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">61,208,432</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">27,505,820</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">23,036,571</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,289,820</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">171,971,735</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">61,182,856</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">35,683,514</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">33,058,543</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">26,434,803</td>
<td align="right">7.0%</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,457,360</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,320</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">440</td>
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
<td align="right">1,746,260</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,714,720</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,320</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">180</td>
<td align="right">0.0%</td>
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
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">39,854,801</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,285,431</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,975,096</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,051,736</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,525,480</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">46,819,361</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,004,040</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,593,995</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,438,645</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,400,400</td>
<td align="right">3.5%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">56,957,013</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">47,838,851</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">36,291,741</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,670,197</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,807,980</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">59,892,062</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">30,913,282</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">30,053,204</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">30,018,280</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,292,302</td>
<td align="right">1.4%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">29,130,600</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20,686,460</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">10,772,360</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">10,486,240</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,086,880</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">89,506,398</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,610,220</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">400</td>
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
<td align="right">4,019,348</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,110,616</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">292,428</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">279,303</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">263,618</td>
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
<td align="right">4,628,153</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,354,486</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">64,004</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">24,274</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">19,320</td>
<td align="right">0.2%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">136,904,405</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">78,108,011</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">51,280,320</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,009,716</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,632,214</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">115,238,986</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">102,135,425</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">34,039,168</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">19,191,869</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">10,292,460</td>
<td align="right">3.5%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">248,110,733</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">48,895,220</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">34,894,808</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">21,719,400</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">21,212,480</td>
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
<td align="left">POP_TOP</td>
<td align="right">263,265,911</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">68,689,161</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">44,683,802</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">19,226,990</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">17,162,661</td>
<td align="right">3.8%</td>
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
<td align="right">294,513,517</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">221,808,362</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">37,867,493</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">25,834,554</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,722,911</td>
<td align="right">1.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">584,311,378</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,814,713</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,522,099</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,006,520</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">517,261</td>
<td align="right">0.1%</td>
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
<td align="right">142,439,846</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">104,936,410</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">10,828,980</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,298,980</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,867,429</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">150,444,652</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">81,844,089</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">15,423,360</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,253,041</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,467,659</td>
<td align="right">2.7%</td>
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
<td align="right">91,487,949</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">31,139,095</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">28,326,313</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">19,536,099</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,086,088</td>
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
<td align="left">STORE_FAST</td>
<td align="right">113,249,290</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">40,475,084</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,203,143</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,185,707</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,777,946</td>
<td align="right">3.3%</td>
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
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">98,555,281</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">80,327,269</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">22,856,525</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">523,121</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">207,279</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">106,226,065</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">35,426,423</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">18,600,074</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">12,099,532</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,158,551</td>
<td align="right">3.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">195,435,479</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">44,076,472</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,849,000</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,418,165</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,296,079</td>
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
<td align="left">POP_TOP</td>
<td align="right">242,131,962</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,135,488</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,517,650</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">943,687</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">932,454</td>
<td align="right">0.4%</td>
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
<td align="right">153,334,928</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">689,660</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">87,960</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">59,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">25,720</td>
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
<td align="right">87,559,708</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20,846,052</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,914,804</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,359,226</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,238,822</td>
<td align="right">2.7%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">128,340,953</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,568,480</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,404,496</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,248,848</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">515,198</td>
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
<td align="right">128,337,173</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">12,397,836</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,113,320</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">361</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">123,924,332</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">115,546,206</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">30,849,720</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">2,474,840</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,288,182</td>
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
<td align="right">158,830,085</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">112,151,960</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,417,460</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,256,300</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,159,360</td>
<td align="right">0.4%</td>
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
<td align="right">88,387,461</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">10,856,758</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,047,837</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">426,140</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">181,805</td>
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
<td align="right">97,072,153</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,490,300</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,997,963</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">454,538</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">409,216</td>
<td align="right">0.4%</td>
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
<td align="right">2,861,798,291</td>
<td align="right">86.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">265,748,725</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">47,489,960</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">41,906,695</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">35,721,480</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">715,237,696</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">361,136,489</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">290,853,551</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">272,697,810</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">232,095,230</td>
<td align="right">7.0%</td>
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
<td align="right">362,464,330</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">272,697,810</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">25,773,311</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">22,955,669</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">21,699,333</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">453,134,592</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">94,819,409</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">80,327,269</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">65,310,231</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">36,573,594</td>
<td align="right">4.6%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">974,851,093</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">118,184,594</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">64,220,254</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">62,278,461</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">13,880,366</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">533,213,262</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">345,570,457</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">307,824,169</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">28,460,399</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">18,496,815</td>
<td align="right">1.5%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">235,187,611</td>
<td align="right">86.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">15,814,260</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">8,290,420</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,769,740</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,582,199</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">67,850,513</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">44,078,936</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42,612,220</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">25,951,140</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,287,042</td>
<td align="right">4.9%</td>
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
<td align="right">82,859,634</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">12,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">8,180</td>
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
<td align="right">47,775,424</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">21,646,605</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">11,398,661</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,707,700</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">172,243</td>
<td align="right">0.2%</td>
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
<td align="right">420,092,778</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">309,285,524</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">42,366,215</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">36,129,520</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">27,469,020</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">235,831,535</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">229,400,229</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">173,172,154</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">111,570,033</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">51,201,996</td>
<td align="right">6.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">24,724,682</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,760,200</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">10,025,650</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">321,762</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,220</td>
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
<td align="right">40,306,577</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,415,137</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,116,280</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,077,360</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">477,540</td>
<td align="right">0.9%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">46,946,670</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">26,675,040</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">25,301,409</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,069,290</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">567,480</td>
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
<td align="right">57,168,755</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">44,818,686</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,947,740</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">394,765</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,680</td>
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
<td align="right">584,311,378</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">497,068,217</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">361,136,489</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">298,902,286</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">153,389,407</td>
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
<td align="right">1,618,788,378</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">592,147,418</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">109,548,867</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,064,971</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">2,977,606</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">50,246,367</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,525,729</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">828,733</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">591,220</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">590,480</td>
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
<td align="right">57,149,484</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">13,890,756</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">673,860</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">307,620</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">21,514</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">205,645,458</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">47,443,045</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">47,322,497</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">33,192,365</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">21,274,280</td>
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
<td align="right">349,974,803</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">11,465,441</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,872,420</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">736,460</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">394,939</td>
<td align="right">0.1%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">112,791,018</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">74,636,649</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">46,942,134</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">46,750,323</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,876,841</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">247,121,015</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42,939,823</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">3,599,540</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">548,661</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">87,980</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

<table>
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
<td align="right">6,164,579</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">986,799</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">523,003</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">392,631</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">281,887</td>
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
<td align="left">POP_TOP</td>
<td align="right">8,173,302</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">549,329</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">160</td>
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
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">325,200</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">50,800</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">49,620</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">39,420</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">14,560</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">323,700</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">113,180</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">50,700</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,480</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,060</td>
<td align="right">0.4%</td>
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
<td align="right">13,176,045</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">957,681</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">316,349</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">156,864</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">5,724</td>
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
<td align="right">14,614,727</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">340</td>
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
<td align="left">BUILD_SLICE</td>
<td align="right">65,588,313</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,513,500</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,065,986</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">274,780</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">27,720</td>
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
<td align="right">65,812,713</td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,406,760</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">352,000</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">312,002</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">223,043</td>
<td align="right">0.3%</td>
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
<td align="right">98,868,424</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,247,520</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,696,516</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,108,960</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,034,980</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">52,779,112</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">51,523,114</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,527,160</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,400</td>
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
<td align="right">18,300</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,840</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,500</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">660</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">440</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">24,020</td>
<td align="right">100.0%</td>
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
<td align="right">8,820,381</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,640,111</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,250,336</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">811,400</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">744,879</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">4,266,484</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,690,820</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,079,860</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,079,696</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">875,811</td>
<td align="right">6.0%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,521,832</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,191,346</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,460,674</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">414,692</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">402,613</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,277,571</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,099,803</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">238,482</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">13,134</td>
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
<td align="left">BINARY_OP</td>
<td align="right">1,579,703</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">512,400</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">408,862</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">10,460</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">580</td>
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
<td align="left">BINARY_OP</td>
<td align="right">2,512,465</td>
<td align="right">100.0%</td>
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
<td align="right">238,482</td>
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
<td align="right">229,140</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">8,580</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">762</td>
<td align="right">0.3%</td>
</tr>
</tbody>
</table>


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

<table>
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
<td align="right">2,795,002</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">838,542</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">668,483</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">255,200</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">227,913</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">186,080</td>
<td align="right">6.7%</td>
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
<td align="right">33,834,781</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">11,631,151</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">10,488,553</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">7,098,322</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,606,211</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">43,007,567</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">23,943,871</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">11,631,151</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">9,122,337</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,784,101</td>
<td align="right">1.9%</td>
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
<td align="right">51,523,114</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,260,412</td>
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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">48,895,220</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,754,367</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">551,666</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">192,000</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">88,000</td>
<td align="right">0.2%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">117,515,680</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">23,652,026</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,999,980</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">402,545</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">262,077</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">125,515,680</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,298,817</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">8,236,926</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">6,122,963</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">819,742</td>
<td align="right">0.5%</td>
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
<td align="right">97,691,260</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">907,240</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">120,560</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">76,960</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">24,120</td>
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
<td align="right">98,868,424</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">697,809</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">40</td>
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
<td align="right">463,650</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">202,745</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">28,684</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,610</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,360</td>
<td align="right">0.2%</td>
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
<td align="right">37,047,406</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">502,560</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">208,035</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">184,406</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">42,040</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">38,087,691</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,760</td>
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
<td align="right">10,598,452</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,006,747</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">185,683</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">42,900</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,540</td>
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
<td align="right">9,636,062</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">2,121,520</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">76,000</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">200</td>
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
<td align="right">10,781,632</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">599,914</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">20</td>
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
<td align="right">10,598,452</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">764,774</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">16,840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">140</td>
<td align="right">0.0%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">477,978,180</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">71,879,524</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">5,242,800</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">875,811</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">258,299</td>
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
<td align="right">530,964,612</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">18,900,085</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,827,276</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">296,400</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">130,120</td>
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
<td align="right">22,857,934</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,008,083</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">239,555</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">104,544</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">62,380</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">23,652,026</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">352,835</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">300,035</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">47,620</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,660</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,682,972</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,800,168</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">932,843</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">691,971</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">426,755</td>
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
<td align="right">4,872,472</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,383,740</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,198,436</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">575,920</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">415,728</td>
<td align="right">4.4%</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">3,378,980</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,642,020</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">905,340</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">329,300</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">284,900</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">3,173,160</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,951,820</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">905,340</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">278,860</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">261,880</td>
<td align="right">3.2%</td>
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
<td align="left">CALL</td>
<td align="right">3,700,680</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">193,780</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">180,180</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">172,100</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">106,004</td>
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
<td align="left">PUSH_EXC_INFO</td>
<td align="right">4,191,346</td>
<td align="right">94.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">189,340</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">44,441</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">8,900</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">819,742</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">744,879</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">243,116</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">237,382</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">44,521</td>
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
<td align="left">COPY</td>
<td align="right">552,239</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">334,842</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">262,077</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,320</td>
<td align="right">0.1%</td>
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
<td align="right">104,380</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">93,740</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">76,000</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">59,800</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">56,620</td>
<td align="right">10.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">253,040</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">105,460</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">42,900</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">33,120</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">28,300</td>
<td align="right">5.2%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">22,945,201</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,400,060</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">6,400,200</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,641,100</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">691,644</td>
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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">21,212,480</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,916,940</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,190,403</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,640,800</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,204,441</td>
<td align="right">2.7%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">100,816,460</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">44,636,618</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">42,173,480</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">1,599,920</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">825,800</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">41,716,800</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">39,854,801</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">39,180,785</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">29,547,360</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">16,102,240</td>
<td align="right">8.5%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">79,642,103</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">78,642,376</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">62,535,860</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">58,638,100</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,041,223</td>
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
<td align="left">STORE_FAST</td>
<td align="right">142,010,290</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">42,294,382</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">30,849,720</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">27,458,740</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,427,222</td>
<td align="right">4.3%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">319,624,166</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,329,200</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,834,440</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">607,384</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">197,260</td>
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
<td align="right">213,305,660</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">112,624,140</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">325,858</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">235,140</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">110,200</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">48,889,890</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40,133,721</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">30,018,280</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,405,255</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,304,081</td>
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
<td align="right">84,917,282</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">36,972,398</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">14,796,375</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">3,005,406</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,088,044</td>
<td align="right">0.8%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">14,638,897</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,100,448</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,031,851</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,262,480</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,699,400</td>
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
<td align="left">STORE_FAST</td>
<td align="right">14,666,256</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,799,973</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">4,737,848</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,699,400</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,581,544</td>
<td align="right">7.1%</td>
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
<td align="right">26,227,633</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">805,482</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">651,054</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">388,382</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">104,240</td>
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
<td align="right">20,514,597</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,052,540</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,302,725</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">800,280</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">341,120</td>
<td align="right">1.2%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">18,564,443</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,504,040</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,205,060</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,664,540</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">145,520</td>
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
<td align="right">8,111,483</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">6,400,200</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,121,780</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,581,940</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,278,360</td>
<td align="right">10.8%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">247,736,807</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,250,920</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">10,838,620</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,536,990</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,579,400</td>
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
<td align="right">256,944,799</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">14,273,240</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,385,440</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,926,430</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,659,140</td>
<td align="right">0.6%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">90,357,433</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,758,827</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,644,716</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,575,624</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,941,113</td>
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
<td align="right">104,320,427</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,329,288</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">757,000</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">199,920</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">85,360</td>
<td align="right">0.1%</td>
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
<td align="right">115,055,894</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,863,020</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,728,722</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">289,322</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">19,000</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">63,590,701</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">28,793,039</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,103,531</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,983,240</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,862,820</td>
<td align="right">4.0%</td>
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
<td align="right">202,858,427</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,788,348</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,485,540</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">83,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">63,842</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">98,555,281</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">64,926,271</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">39,342,141</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,543,334</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,541,364</td>
<td align="right">3.0%</td>
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
<td align="right">35,921,169</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,259,240</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,141,840</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">454,343</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">252,840</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">11,990,263</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,536,620</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,440,776</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,288,480</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,007,728</td>
<td align="right">8.8%</td>
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
<td align="right">38,787,681</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,770,384</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,028,821</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">912,107</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">265,400</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">38,053,764</td>
<td align="right">84.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">3,550,911</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,771,615</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">520,043</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">270,313</td>
<td align="right">0.6%</td>
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
<td align="right">1,043,174,170</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">27,741,174</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,726,550</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">4,824,440</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,930,460</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">276,515,317</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">205,645,458</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">128,340,953</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">118,184,594</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">61,208,432</td>
<td align="right">5.6%</td>
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
<td align="right">7,139,730</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">77,300</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">1,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">120</td>
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
<td align="right">7,121,406</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">87,924</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,380</td>
<td align="right">0.0%</td>
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
<td align="right">633,602,931</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">437,319,486</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,712,144</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">472,358</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">88,680</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">379,743,264</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">253,867,006</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">229,908,047</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">181,484,148</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,250,200</td>
<td align="right">1.5%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">48,275,663</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">10,603,220</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">10,232,440</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">10,086,360</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,184,733</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">57,938,218</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">13,566,873</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">11,929,968</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">2,640,111</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,670,045</td>
<td align="right">1.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">6,810,505</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,547,180</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,233,080</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,641,600</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">154,160</td>
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
<td align="right">8,999,589</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">6,922,497</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">94,420</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">8,020</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,920</td>
<td align="right">0.0%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">220,613,822</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">14,359,260</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,808,989</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">943,687</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">431,960</td>
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
<td align="right">215,808,080</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">23,036,571</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">766,280</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">184,660</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">39,760</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">21,074,520</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">5,772,744</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,064,971</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,408,080</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,446,504</td>
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
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">11,350,603</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,402,947</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">9,726,640</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,607,480</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,494,011</td>
<td align="right">10.5%</td>
</tr>
</tbody>
</table>


</details>

### CLEANUP_THROW

<details>
<summary> Successors and predecessors for CLEANUP_THROW </summary>

<table>
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
<td align="right">152,063</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">120,820</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">31,002</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">241</td>
<td align="right">0.2%</td>
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
<td align="right">186,656,276</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">146,801,461</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">69,100,760</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">15,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">241</td>
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
<td align="right">129,810,160</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">104,944,100</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">77,690,840</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">77,690,840</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,588,041</td>
<td align="right">2.1%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">32,921,240</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">9,495,544</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,803,400</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,070,880</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">274,660</td>
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
<td align="right">46,957,284</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">47,349,028</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,191,558</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">838,080</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">77,540</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">30,920</td>
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
<td align="right">49,122,868</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">263,960</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">88,016</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">44,000</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">5,660</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">42,040</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">22,880</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,540</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">742</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">740</td>
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
<td align="right">42,942</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">22,640</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">3,100</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">822</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">580</td>
<td align="right">0.8%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">5,436,580</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,742,308</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">675,560</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">293,280</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">169,520</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">11,542,229</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">38,600</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">38,240</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">19,120</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">3,540</td>
<td align="right">0.0%</td>
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
<td align="right">36,457,398</td>
<td align="right">86.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,172,835</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,599,140</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">342,120</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">144,053</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">18,536,694</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,408,460</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">5,613,336</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,474,840</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,317,360</td>
<td align="right">5.5%</td>
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
<td align="right">530,964,612</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">255,208,081</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">683,754</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">7,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">100</td>
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
<td align="right">442,931,000</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">255,635,115</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">88,262,409</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">15,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">15,140</td>
<td align="right">0.0%</td>
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
<td align="right">469,337</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">338,140</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">194,225</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">90,440</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">89,560</td>
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
<td align="left">STORE_FAST</td>
<td align="right">439,780</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">340,600</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">202,800</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">190,865</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">80,380</td>
<td align="right">6.0%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">84,140</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">80,380</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">36,720</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">22,980</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">8,000</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">233,020</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">7,980</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">202,640</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">20</td>
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
<td align="right">90,480</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">88,000</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">23,040</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">300</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">300</td>
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
<td align="right">800,280</td>
<td align="right">80.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">121,160</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">50,140</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,560</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,200</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">871,760</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">118,900</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,060</td>
<td align="right">0.1%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_EX

<details>
<summary> Successors and predecessors for UNPACK_EX </summary>

<table>
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
<td align="right">514,780</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">291,340</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,280</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">20</td>
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
<td align="right">807,420</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### INSTRUMENTED_RESUME

<details>
<summary> Successors and predecessors for INSTRUMENTED_RESUME </summary>

<table>
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
<td align="right">38,845,780</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">60</td>
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
<td align="right">38,846,000</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### INSTRUMENTED_RETURN_VALUE

<details>
<summary> Successors and predecessors for INSTRUMENTED_RETURN_VALUE </summary>

<table>
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
<td align="right">19,422,960</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">19,422,700</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">19,422,680</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">19,422,680</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### INSTRUMENTED_RETURN_CONST

<details>
<summary> Successors and predecessors for INSTRUMENTED_RETURN_CONST </summary>

<table>
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
<td align="right">100</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">80</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">60</td>
<td align="right">25.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">240</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### INSTRUMENTED_JUMP_BACKWARD

<details>
<summary> Successors and predecessors for INSTRUMENTED_JUMP_BACKWARD </summary>

<table>
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
<td align="right">80</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">80</td>
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
<td align="left">FOR_ITER</td>
<td align="right">160</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### END_ASYNC_FOR

<details>
<summary> Successors and predecessors for END_ASYNC_FOR </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SEND</td>
<td align="right">8,000,000</td>
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
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,242,800</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">2,757,200</td>
<td align="right">34.5%</td>
</tr>
</tbody>
</table>


</details>

### GET_AITER

<details>
<summary> Successors and predecessors for GET_AITER </summary>

<table>
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
<td align="right">7,999,880</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">40</td>
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
<td align="left">GET_ANEXT</td>
<td align="right">8,000,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### GET_ANEXT

<details>
<summary> Successors and predecessors for GET_ANEXT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">GET_AITER</td>
<td align="right">8,000,000</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">960</td>
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
<td align="right">8,000,960</td>
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
<td align="right">1,780</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">240</td>
<td align="right">11.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,000</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20</td>
<td align="right">1.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL_INTRINSIC_2

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_2 </summary>

<table>
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
<td align="right">60</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">20</td>
<td align="right">25.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">60</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">20</td>
<td align="right">25.0%</td>
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
<td align="right">1,284,800</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">322,893</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">192,480</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">113,245</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">66,380</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">648,440</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">642,560</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">360,120</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">143,519</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">129,136</td>
<td align="right">6.1%</td>
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
<td align="right">400</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">240</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">160</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">60</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">20</td>
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
<td align="left">DELETE_NAME</td>
<td align="right">400</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">160</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">140</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">80</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">60</td>
<td align="right">6.7%</td>
</tr>
</tbody>
</table>


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

<table>
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
<td align="right">207,312,042</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,732,690</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,638,973</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,446,287</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">3,005,926</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">229,143,926</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_FROM_DICT_OR_DEREF

<details>
<summary> Successors and predecessors for LOAD_FROM_DICT_OR_DEREF </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,000</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">1,800</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">160</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">40</td>
<td align="right">2.0%</td>
</tr>
</tbody>
</table>


</details>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

<table>
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
<td align="right">2,996,645</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">8,601</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">160</td>
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
<td align="left">GET_AWAITABLE</td>
<td align="right">3,005,926</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">320</td>
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
<td align="right">320</td>
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
<td align="right">880</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">560</td>
<td align="right">38.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,320</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">120</td>
<td align="right">8.3%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN

<details>
<summary> Successors and predecessors for LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN </summary>

<table>
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
<td align="right">88,580</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,080</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">56,160</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">32,440</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,080</td>
<td align="right">1.2%</td>
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
<td align="right">421,141,831</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,345,949,491</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,506,657</td>
<td align="right">1.7%</td>
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
<td align="right">598,396</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,110,591</td>
<td align="right">65.0%</td>
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
<td align="left">subtract different types</td>
<td align="right">782,346</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">83,765</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">39,887</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">37,792</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">35,635</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,704</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">17,313</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">15,014</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">12,365</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,780</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,984</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,841</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,821</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,707</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">5,121</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">3,441</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,975</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


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
<td align="right">302,355,673</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,187,540,996</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,837,691</td>
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
<td align="right">121,005</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">126,009</td>
<td align="right">51.0%</td>
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
<td align="right">45,200</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">34,568</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,800</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">1,640</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,320</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">760</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">121</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
<td align="right">321,144,828</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,860</td>
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
<td align="right">5,269,204,049</td>
<td align="right">94.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">197,589,895</td>
<td align="right">3.5%</td>
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
<td align="right">4,299,237</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">95,599</td>
<td align="right">2.2%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">82,679</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">11,860</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,480</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">1,060</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">680</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">200</td>
<td align="right">0.2%</td>
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
<td align="right">105,037,073</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,505,748,624</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">771,806</td>
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
<td align="right">75,224</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">145,125</td>
<td align="right">65.9%</td>
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
<td align="right">30,527</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,923</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,723</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,855</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">16,412</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,770</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,000</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,060</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,823</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,820</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">1,532</td>
<td align="right">1.1%</td>
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
<td align="right">48,355,987</td>
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
<td align="right">388,409,280</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,517,260</td>
<td align="right">0.6%</td>
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
<td align="right">61,553</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">81,880</td>
<td align="right">57.1%</td>
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
<td align="right">30,074</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">22,360</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">19,746</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,700</td>
<td align="right">11.8%</td>
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
<td align="right">83,096,550</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">359,684,924</td>
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
<td align="right">357,420</td>
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
<td align="right">57,095</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">128,222</td>
<td align="right">69.2%</td>
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
<td align="right">42,313</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,185</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">13,300</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,765</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,739</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">8,580</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,900</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">5,520</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,020</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,980</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,560</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">560</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">520</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.2%</td>
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
<td align="right">765,445,358</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">679,361</td>
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
<td align="right">7,438,194,349</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">237,416,774</td>
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
<td align="right">5,133,421</td>
<td align="right">86.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">777,887</td>
<td align="right">13.2%</td>
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
<td align="left">not managed dict</td>
<td align="right">211,219</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">160,296</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">100,016</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">74,697</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">57,406</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">46,638</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">29,580</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,144</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,140</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,800</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">15,280</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">14,866</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">7,622</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3,383</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">3,000</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">20</td>
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
<td align="right">20,370,033</td>
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
<td align="right">11,760</td>
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
<td align="right">4,804,899,574</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">430,465</td>
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
<td align="right">523,094</td>
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
<td align="right">9,581</td>
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
<td align="right">90,098,364</td>
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
<td align="right">9,420</td>
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

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NONE family </summary>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NOT_NONE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


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
<td align="right">173,802,168</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">786,832,693</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">30,900</td>
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
<td align="right">7,046</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,723</td>
<td align="right">89.8%</td>
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
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,123</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,960</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,220</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">240</td>
<td align="right">0.4%</td>
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
<td align="right">101,031,836</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,912,396,997</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">68,458,697</td>
<td align="right">3.4%</td>
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
<td align="right">1,413,744</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">100,582</td>
<td align="right">6.6%</td>
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
<td align="left">not managed dict</td>
<td align="right">35,462</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,680</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">11,620</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,720</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,780</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">6,060</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">5,340</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">5,020</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">4,360</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>


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
<td align="right">65,956,290</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">167,968,722</td>
<td align="right">71.8%</td>
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
<td align="right">15,140</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">57,033</td>
<td align="right">79.0%</td>
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
<td align="right">35,236</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">11,297</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,320</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">900</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">800</td>
<td align="right">1.4%</td>
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
<td align="right">247,885,670</td>
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
<td align="right">2,842,864,733</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,230,476</td>
<td align="right">1.6%</td>
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
<td align="right">1,144,101</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">194,335</td>
<td align="right">14.5%</td>
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
<td align="left">mapping</td>
<td align="right">49,541</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">38,949</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">30,713</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">23,182</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">20,169</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">17,841</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,212</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">4,747</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2,321</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,240</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.2%</td>
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
<td align="right">447,355</td>
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
<td align="right">535,165,030</td>
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
<td align="right">31,468</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,075</td>
<td align="right">8.9%</td>
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
<td align="right">2,195</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">500</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">12.4%</td>
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
<td align="right">54,028,757,802</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,090,979,799</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">34,434,676,017</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">588,333,016</td>
<td align="right">0.6%</td>
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
<td align="right">765,445,358</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">421,141,831</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">321,144,828</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">302,355,673</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">247,885,670</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,802,168</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">105,037,073</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">101,031,836</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">83,096,550</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">65,956,290</td>
<td align="right">2.5%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">106,105,547</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">91,049,871</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">56,738,451</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,346,085</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">41,828,162</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">39,297,004</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,825,647</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,089,062</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">23,661,451</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">23,643,515</td>
<td align="right">4.0%</td>
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
<td align="right">2,197,532,819</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,663,236,810</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,197,532,819</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,343,253,688</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">854,279,131</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,652,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,340,577,468</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">24,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">454,131,602</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">34,576,367</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">234,867,465</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">213,166,487</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">73,908,840</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,176,848,597</td>
<td align="right">78.6%</td>
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
<td align="right">6,348,387,418</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,350,259,756</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,535,181,943</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,409,484,594</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">105,087,547</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,609,802</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,861,194,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,691,028</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">86,089,572,184</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">98,956,504,107</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">22,760,583,912</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">26,116,461,386</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">6,547,500</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">64,160</td>
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
<td align="right">2,261,849,693</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">30,985,410</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">59,153,575</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,070,129,383</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">28,378,967</td>
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
</tr>
</thead>
<tbody>
<tr>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">0</td>
<td align="right">19,448,993</td>
<td align="right">14,679,676,702</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,753,920</td>
<td align="right">7,054,397,760</td>
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
<td align="right">848,481</td>
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
<td align="right">120,099</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">833</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">449,109</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">728,382</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">16,364</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,260</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,479</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,366</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">8,312,783,272</td>
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
<td align="right">201,479,090,240</td>
<td align="right">2,423.7%</td>
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
<td align="right">120,099</td>
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
<td align="right">116,556</td>
<td align="right">97.0%</td>
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
<td align="right">2,323</td>
<td align="right">1.9%</td>
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
<td align="right">11,932</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,388</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">37,032</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">27,996</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">14,155</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,176</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,280</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">140</td>
<td align="right">0.1%</td>
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
<td align="right">10,152</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">17,571</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">25,290</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,334</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">17,227</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,024</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,618</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">340</td>
<td align="right">0.3%</td>
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
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">1,109,558,722</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,131,562,527</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,116,277,807</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,134,937,384</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">702,538,885</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">339,533,375</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">182,275,777</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">28,644,175</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">7,335,284</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 2,048</td>
<td align="right">19,033,925</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 4,096</td>
<td align="right">685,855</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="right">743,039</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="right">246,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="right">43,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="right">13,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="right">1,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 262,144</td>
<td align="right">2,001</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 524,288</td>
<td align="right">479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 1,048,576</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 2,097,152</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4,194,304</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8,388,608</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16,777,216</td>
<td align="right">240</td>
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
<td align="right">13,927,946,474</td>
<td align="right">6.9%</td>
<td align="right">6.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,867,908,199</td>
<td align="right">5.9%</td>
<td align="right">12.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,600,164,935</td>
<td align="right">4.8%</td>
<td align="right">17.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,201,716,697</td>
<td align="right">3.6%</td>
<td align="right">21.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,662,943,117</td>
<td align="right">3.3%</td>
<td align="right">24.4%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,534,787,643</td>
<td align="right">3.2%</td>
<td align="right">27.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,482,313,607</td>
<td align="right">3.2%</td>
<td align="right">30.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">5,773,435,235</td>
<td align="right">2.9%</td>
<td align="right">33.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,750,493,831</td>
<td align="right">2.9%</td>
<td align="right">36.6%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">5,557,746,682</td>
<td align="right">2.8%</td>
<td align="right">39.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">5,199,848,652</td>
<td align="right">2.6%</td>
<td align="right">42.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,601,596,122</td>
<td align="right">1.8%</td>
<td align="right">43.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,450,746,230</td>
<td align="right">1.7%</td>
<td align="right">45.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,301,534,257</td>
<td align="right">1.6%</td>
<td align="right">47.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,197,535,005</td>
<td align="right">1.6%</td>
<td align="right">48.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,957,868,896</td>
<td align="right">1.5%</td>
<td align="right">50.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,830,581,020</td>
<td align="right">1.4%</td>
<td align="right">51.6%</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,647,007,430</td>
<td align="right">1.3%</td>
<td align="right">52.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,545,569,276</td>
<td align="right">1.3%</td>
<td align="right">54.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">2,539,348,037</td>
<td align="right">1.3%</td>
<td align="right">55.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,260,515,820</td>
<td align="right">1.1%</td>
<td align="right">56.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,240,111,443</td>
<td align="right">1.1%</td>
<td align="right">57.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,237,118,020</td>
<td align="right">1.1%</td>
<td align="right">58.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,188,440,848</td>
<td align="right">1.1%</td>
<td align="right">59.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,180,229,997</td>
<td align="right">1.1%</td>
<td align="right">60.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,096,123,709</td>
<td align="right">1.0%</td>
<td align="right">62.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,974,564,694</td>
<td align="right">1.0%</td>
<td align="right">62.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,954,859,588</td>
<td align="right">1.0%</td>
<td align="right">63.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,865,402,499</td>
<td align="right">0.9%</td>
<td align="right">64.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,854,860,086</td>
<td align="right">0.9%</td>
<td align="right">65.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,821,151,759</td>
<td align="right">0.9%</td>
<td align="right">66.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,785,670,003</td>
<td align="right">0.9%</td>
<td align="right">67.5%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,654,369,972</td>
<td align="right">0.8%</td>
<td align="right">68.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,653,969,851</td>
<td align="right">0.8%</td>
<td align="right">69.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,547,250,318</td>
<td align="right">0.8%</td>
<td align="right">70.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,431,010,164</td>
<td align="right">0.7%</td>
<td align="right">70.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,414,856,751</td>
<td align="right">0.7%</td>
<td align="right">71.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,393,946,229</td>
<td align="right">0.7%</td>
<td align="right">72.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,369,647,949</td>
<td align="right">0.7%</td>
<td align="right">72.7%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,366,933,842</td>
<td align="right">0.7%</td>
<td align="right">73.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,342,290,015</td>
<td align="right">0.7%</td>
<td align="right">74.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,339,737,079</td>
<td align="right">0.7%</td>
<td align="right">74.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,280,027</td>
<td align="right">0.7%</td>
<td align="right">75.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,312,573,045</td>
<td align="right">0.7%</td>
<td align="right">76.1%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,274,222,018</td>
<td align="right">0.6%</td>
<td align="right">76.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,261,514,245</td>
<td align="right">0.6%</td>
<td align="right">77.3%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,242,240,354</td>
<td align="right">0.6%</td>
<td align="right">77.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,237,923,673</td>
<td align="right">0.6%</td>
<td align="right">78.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,564,984</td>
<td align="right">0.6%</td>
<td align="right">79.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,142,115,219</td>
<td align="right">0.6%</td>
<td align="right">79.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,114,785,540</td>
<td align="right">0.6%</td>
<td align="right">80.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,101,129,334</td>
<td align="right">0.5%</td>
<td align="right">80.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,057,622,234</td>
<td align="right">0.5%</td>
<td align="right">81.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,047,992,292</td>
<td align="right">0.5%</td>
<td align="right">81.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,042,082,915</td>
<td align="right">0.5%</td>
<td align="right">82.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,039,529,387</td>
<td align="right">0.5%</td>
<td align="right">82.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">977,042,499</td>
<td align="right">0.5%</td>
<td align="right">83.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">960,542,353</td>
<td align="right">0.5%</td>
<td align="right">83.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">947,714,398</td>
<td align="right">0.5%</td>
<td align="right">84.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">935,791,953</td>
<td align="right">0.5%</td>
<td align="right">84.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,811,548</td>
<td align="right">0.5%</td>
<td align="right">85.2%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">860,793,301</td>
<td align="right">0.4%</td>
<td align="right">85.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">846,008,075</td>
<td align="right">0.4%</td>
<td align="right">86.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">789,532,678</td>
<td align="right">0.4%</td>
<td align="right">86.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">783,343,962</td>
<td align="right">0.4%</td>
<td align="right">86.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">782,806,642</td>
<td align="right">0.4%</td>
<td align="right">87.2%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">758,764,707</td>
<td align="right">0.4%</td>
<td align="right">87.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">736,485,373</td>
<td align="right">0.4%</td>
<td align="right">88.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_INSTR_PTR</td>
<td align="right">732,748,599</td>
<td align="right">0.4%</td>
<td align="right">88.3%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">725,645,516</td>
<td align="right">0.4%</td>
<td align="right">88.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">711,283,450</td>
<td align="right">0.4%</td>
<td align="right">89.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">688,275,628</td>
<td align="right">0.3%</td>
<td align="right">89.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">685,304,339</td>
<td align="right">0.3%</td>
<td align="right">89.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,076,156</td>
<td align="right">0.3%</td>
<td align="right">90.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">619,297,987</td>
<td align="right">0.3%</td>
<td align="right">90.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">595,989,434</td>
<td align="right">0.3%</td>
<td align="right">90.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,466,000</td>
<td align="right">0.3%</td>
<td align="right">90.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">571,573,264</td>
<td align="right">0.3%</td>
<td align="right">91.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">564,925,985</td>
<td align="right">0.3%</td>
<td align="right">91.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">554,425,520</td>
<td align="right">0.3%</td>
<td align="right">91.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">542,126,790</td>
<td align="right">0.3%</td>
<td align="right">92.1%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">531,150,840</td>
<td align="right">0.3%</td>
<td align="right">92.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,667,080</td>
<td align="right">0.3%</td>
<td align="right">92.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">485,735,296</td>
<td align="right">0.2%</td>
<td align="right">92.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">484,718,112</td>
<td align="right">0.2%</td>
<td align="right">93.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">413,980,069</td>
<td align="right">0.2%</td>
<td align="right">93.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">411,356,331</td>
<td align="right">0.2%</td>
<td align="right">93.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">411,071,749</td>
<td align="right">0.2%</td>
<td align="right">93.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">405,268,595</td>
<td align="right">0.2%</td>
<td align="right">93.9%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,673,151</td>
<td align="right">0.2%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">382,410,796</td>
<td align="right">0.2%</td>
<td align="right">94.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">365,224,035</td>
<td align="right">0.2%</td>
<td align="right">94.4%</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">337,800,391</td>
<td align="right">0.2%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">336,478,850</td>
<td align="right">0.2%</td>
<td align="right">94.8%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">331,280,554</td>
<td align="right">0.2%</td>
<td align="right">94.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">324,400,311</td>
<td align="right">0.2%</td>
<td align="right">95.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">314,565,612</td>
<td align="right">0.2%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">275,743,604</td>
<td align="right">0.1%</td>
<td align="right">95.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">263,198,831</td>
<td align="right">0.1%</td>
<td align="right">95.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">261,972,011</td>
<td align="right">0.1%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">244,319,086</td>
<td align="right">0.1%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">233,749,802</td>
<td align="right">0.1%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,890,908</td>
<td align="right">0.1%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">228,072,710</td>
<td align="right">0.1%</td>
<td align="right">96.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">226,122,522</td>
<td align="right">0.1%</td>
<td align="right">96.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">226,004,301</td>
<td align="right">0.1%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">223,137,044</td>
<td align="right">0.1%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">217,699,932</td>
<td align="right">0.1%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">211,683,026</td>
<td align="right">0.1%</td>
<td align="right">96.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">211,164,864</td>
<td align="right">0.1%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,267,436</td>
<td align="right">0.1%</td>
<td align="right">96.9%</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,426,700</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">197,923,251</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,705,058</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">187,158,474</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">184,819,111</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">172,273,544</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">167,731,244</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">153,990,395</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,868,340</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">149,709,514</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,886,100</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">144,482,951</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">139,672,603</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">134,342,649</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">133,239,936</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">133,239,936</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">129,600,309</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">129,531,216</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">128,408,256</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,901,276</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">120,992,816</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">115,482,619</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">110,611,192</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">108,255,443</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">104,635,925</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,863,840</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,291,458</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">100,114,202</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">99,814,940</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">99,792,373</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">98,833,733</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">96,137,708</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,893,588</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,730,798</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">93,630,221</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">92,088,550</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">87,728,439</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,405,920</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,523,902</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">74,248,274</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,911,603</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">64,594,900</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">62,824,761</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">62,441,781</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,844,000</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">61,625,419</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">58,672,976</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">58,443,260</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,336,010</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,344,620</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">51,291,305</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,651,375</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">34,253,820</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,503,359</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">29,730,954</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">22,799,839</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">22,366,680</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,059,820</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">20,745,061</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">20,499,060</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">13,753,700</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,693,500</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,431,968</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,431,968</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,234,995</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,808,227</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,226,210</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,169,907</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,895,308</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,636,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">4,823,420</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">4,523,689</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,610,840</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,865,500</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,133,180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">2,007,660</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,953,580</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,551,514</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">651,574</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">543,640</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">501,700</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">441,339</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">71,420</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">41,100</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
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
<td align="left">_LOAD_FAST_0 _GUARD_TYPE_VERSION</td>
<td align="right">3,997,260,069</td>
<td align="right">2.0%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC _CHECK_VALIDITY</td>
<td align="right">2,571,168,321</td>
<td align="right">1.3%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR _TIER2_RESUME_CHECK</td>
<td align="right">2,431,163,115</td>
<td align="right">1.2%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _GUARD_NOS_INT</td>
<td align="right">2,307,781,590</td>
<td align="right">1.1%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,260,515,820</td>
<td align="right">1.1%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES _LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,237,118,020</td>
<td align="right">1.1%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP _TIER2_RESUME_CHECK</td>
<td align="right">2,103,504,099</td>
<td align="right">1.0%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _SET_IP</td>
<td align="right">2,022,832,804</td>
<td align="right">1.0%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET _PUSH_FRAME</td>
<td align="right">1,854,860,086</td>
<td align="right">0.9%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT _BINARY_OP_ADD_INT</td>
<td align="right">1,818,481,793</td>
<td align="right">0.9%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,816,805,271</td>
<td align="right">0.9%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR _GUARD_IS_FALSE_POP</td>
<td align="right">1,807,472,667</td>
<td align="right">0.9%</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST_7</td>
<td align="right">1,777,816,392</td>
<td align="right">0.9%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _GUARD_IS_FALSE_POP</td>
<td align="right">1,692,191,547</td>
<td align="right">0.8%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET _CHECK_VALIDITY</td>
<td align="right">1,653,479,131</td>
<td align="right">0.8%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_SET_IP _CONTAINS_OP_SET</td>
<td align="right">1,581,223,591</td>
<td align="right">0.8%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _SET_IP</td>
<td align="right">1,538,269,216</td>
<td align="right">0.8%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME _RESUME_CHECK</td>
<td align="right">1,528,021,013</td>
<td align="right">0.8%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0 _LOAD_FAST_1</td>
<td align="right">1,505,279,582</td>
<td align="right">0.7%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,397,366,598</td>
<td align="right">0.7%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">_SET_IP _CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,371,416,463</td>
<td align="right">0.7%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST _GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,312,573,045</td>
<td align="right">0.7%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _SET_IP</td>
<td align="right">1,297,103,533</td>
<td align="right">0.6%</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _BINARY_SUBSCR_STR_INT</td>
<td align="right">1,288,052,100</td>
<td align="right">0.6%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_SET_IP _BINARY_SUBSCR</td>
<td align="right">1,269,280,859</td>
<td align="right">0.6%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,261,514,245</td>
<td align="right">0.6%</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT _GUARD_KEYS_VERSION</td>
<td align="right">1,242,240,354</td>
<td align="right">0.6%</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _SET_IP</td>
<td align="right">1,239,269,790</td>
<td align="right">0.6%</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT _STORE_FAST_1</td>
<td align="right">1,238,532,120</td>
<td align="right">0.6%</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR _CHECK_VALIDITY</td>
<td align="right">1,225,032,578</td>
<td align="right">0.6%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK _ITER_CHECK_LIST</td>
<td align="right">1,205,165,801</td>
<td align="right">0.6%</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL _GUARD_IS_FALSE_POP</td>
<td align="right">1,189,773,791</td>
<td align="right">0.6%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION _LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,142,115,219</td>
<td align="right">0.6%</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST _ITER_NEXT_LIST</td>
<td align="right">1,101,129,334</td>
<td align="right">0.5%</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,088,463,851</td>
<td align="right">0.5%</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST_1</td>
<td align="right">1,068,999,542</td>
<td align="right">0.5%</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _LOAD_FAST</td>
<td align="right">1,061,876,988</td>
<td align="right">0.5%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,057,622,234</td>
<td align="right">0.5%</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _LOAD_FAST</td>
<td align="right">1,018,352,219</td>
<td align="right">0.5%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_SET_IP _LOAD_ATTR</td>
<td align="right">1,014,760,874</td>
<td align="right">0.5%</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP _CHECK_VALIDITY</td>
<td align="right">1,014,149,989</td>
<td align="right">0.5%</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK _LOAD_FAST_0</td>
<td align="right">1,012,487,032</td>
<td align="right">0.5%</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR _SET_IP</td>
<td align="right">995,430,718</td>
<td align="right">0.5%</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _LOAD_ATTR_SLOT_0</td>
<td align="right">977,042,499</td>
<td align="right">0.5%</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7 _LOAD_FAST_7</td>
<td align="right">962,745,708</td>
<td align="right">0.5%</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS _CHECK_STACK_SPACE_OPERAND</td>
<td align="right">947,714,398</td>
<td align="right">0.5%</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK _LOAD_FAST_0</td>
<td align="right">942,880,384</td>
<td align="right">0.5%</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE _COMPARE_OP_STR</td>
<td align="right">939,274,493</td>
<td align="right">0.5%</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST _CHECK_PERIODIC</td>
<td align="right">935,735,713</td>
<td align="right">0.5%</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _GUARD_BOTH_UNICODE</td>
<td align="right">922,688,073</td>
<td align="right">0.5%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7 _LOAD_FAST_3</td>
<td align="right">918,234,157</td>
<td align="right">0.5%</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_SET_IP _BINARY_OP</td>
<td align="right">903,151,043</td>
<td align="right">0.4%</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT _STORE_FAST_7</td>
<td align="right">899,244,240</td>
<td align="right">0.4%</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _TO_BOOL_BOOL</td>
<td align="right">897,804,846</td>
<td align="right">0.4%</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE _SET_IP</td>
<td align="right">895,408,873</td>
<td align="right">0.4%</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1 _JUMP_TO_TOP</td>
<td align="right">892,877,380</td>
<td align="right">0.4%</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_BUILTIN_FAST</td>
<td align="right">885,775,995</td>
<td align="right">0.4%</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _COMPARE_OP_STR</td>
<td align="right">881,145,362</td>
<td align="right">0.4%</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR _CHECK_VALIDITY</td>
<td align="right">860,502,278</td>
<td align="right">0.4%</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">838,636,920</td>
<td align="right">0.4%</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _SET_IP</td>
<td align="right">826,940,829</td>
<td align="right">0.4%</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4 _SET_IP</td>
<td align="right">809,879,895</td>
<td align="right">0.4%</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST</td>
<td align="right">801,494,439</td>
<td align="right">0.4%</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O _CHECK_PERIODIC</td>
<td align="right">787,671,453</td>
<td align="right">0.4%</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE _GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">782,806,642</td>
<td align="right">0.4%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK _ITER_CHECK_RANGE</td>
<td align="right">748,958,240</td>
<td align="right">0.4%</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_BUILTIN_O</td>
<td align="right">738,425,536</td>
<td align="right">0.4%</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE _ITER_NEXT_RANGE</td>
<td align="right">736,485,373</td>
<td align="right">0.4%</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR _GUARD_INSTR_PTR</td>
<td align="right">732,748,599</td>
<td align="right">0.4%</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST_1</td>
<td align="right">719,016,967</td>
<td align="right">0.4%</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_CONST_INLINE_BORROW</td>
<td align="right">715,185,208</td>
<td align="right">0.4%</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL _GUARD_IS_TRUE_POP</td>
<td align="right">713,531,418</td>
<td align="right">0.4%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL _LOAD_FAST_5</td>
<td align="right">686,062,068</td>
<td align="right">0.3%</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _GUARD_IS_TRUE_POP</td>
<td align="right">685,506,593</td>
<td align="right">0.3%</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _LOAD_FAST_4</td>
<td align="right">675,523,579</td>
<td align="right">0.3%</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _LOAD_CONST_INLINE_BORROW</td>
<td align="right">666,483,788</td>
<td align="right">0.3%</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">_GUARD_INSTR_PTR _TIER2_RESUME_CHECK</td>
<td align="right">665,181,438</td>
<td align="right">0.3%</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION _LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">643,978,862</td>
<td align="right">0.3%</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _EXIT_TRACE</td>
<td align="right">638,918,543</td>
<td align="right">0.3%</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _LOAD_FAST_3</td>
<td align="right">633,836,296</td>
<td align="right">0.3%</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT _BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">595,360,644</td>
<td align="right">0.3%</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">587,826,560</td>
<td align="right">0.3%</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _EXIT_TRACE</td>
<td align="right">575,131,543</td>
<td align="right">0.3%</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1 _SAVE_RETURN_OFFSET</td>
<td align="right">571,573,264</td>
<td align="right">0.3%</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK _SET_IP</td>
<td align="right">561,247,000</td>
<td align="right">0.3%</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF _CHECK_VALIDITY</td>
<td align="right">555,028,304</td>
<td align="right">0.3%</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _STORE_FAST</td>
<td align="right">554,059,141</td>
<td align="right">0.3%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4 _SAVE_RETURN_OFFSET</td>
<td align="right">531,150,840</td>
<td align="right">0.3%</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _STORE_FAST</td>
<td align="right">527,697,710</td>
<td align="right">0.3%</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _GUARD_TYPE_VERSION</td>
<td align="right">525,795,832</td>
<td align="right">0.3%</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _FOR_ITER_TIER_TWO</td>
<td align="right">512,196,853</td>
<td align="right">0.3%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">506,231,381</td>
<td align="right">0.3%</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT _COMPARE_OP_INT</td>
<td align="right">498,813,354</td>
<td align="right">0.2%</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL _LOAD_FAST_1</td>
<td align="right">484,440,512</td>
<td align="right">0.2%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT _GUARD_IS_FALSE_POP</td>
<td align="right">483,641,675</td>
<td align="right">0.2%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">_COPY _COPY</td>
<td align="right">480,656,260</td>
<td align="right">0.2%</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">_SWAP _SWAP</td>
<td align="right">480,653,700</td>
<td align="right">0.2%</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">_SET_IP _LOAD_DEREF</td>
<td align="right">479,306,694</td>
<td align="right">0.2%</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK _EXIT_TRACE</td>
<td align="right">478,355,000</td>
<td align="right">0.2%</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _EXIT_TRACE</td>
<td align="right">468,110,581</td>
<td align="right">0.2%</td>
<td align="right">53.1%</td>
</tr>
</tbody>
</table>


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
<td align="left">SEND_GEN</td>
<td align="right">118,380</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">83,968</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">41,962</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,475</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">30,362</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,472</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,523</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,577</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,340</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">1,921</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,640</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">880</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">538</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">400</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">260</td>
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
<td align="right">240</td>
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
<td align="right">400</td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,084</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,084</td>
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
<td align="right">1,980</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-05-05
