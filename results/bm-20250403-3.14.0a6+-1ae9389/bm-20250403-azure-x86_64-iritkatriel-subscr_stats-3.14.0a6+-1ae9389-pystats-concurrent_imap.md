
# Pystats results

- benchmark: concurrent_imap
- fork: iritkatriel
- ref: subscr_stats
- commit hash: 1ae9389
- commit date: 2025-04-03T20:29:38+01:00

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
<td align="right">85,941,179</td>
<td align="right">17.4%</td>
<td align="right">17.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">30,031,515</td>
<td align="right">6.1%</td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">25,526,684</td>
<td align="right">5.2%</td>
<td align="right">28.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">25,015,342</td>
<td align="right">5.1%</td>
<td align="right">33.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">19,066,890</td>
<td align="right">3.9%</td>
<td align="right">37.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">19,022,400</td>
<td align="right">3.9%</td>
<td align="right">41.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">15,828,873</td>
<td align="right">3.2%</td>
<td align="right">44.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">15,730,563</td>
<td align="right">3.2%</td>
<td align="right">47.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">14,611,421</td>
<td align="right">3.0%</td>
<td align="right">50.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">13,929,989</td>
<td align="right">2.8%</td>
<td align="right">53.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,321,220</td>
<td align="right">2.7%</td>
<td align="right">56.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,077,766</td>
<td align="right">2.4%</td>
<td align="right">58.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,037,542</td>
<td align="right">1.8%</td>
<td align="right">60.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">8,527,370</td>
<td align="right">1.7%</td>
<td align="right">62.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,453,981</td>
<td align="right">1.7%</td>
<td align="right">64.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">8,196,592</td>
<td align="right">1.7%</td>
<td align="right">65.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,154,136</td>
<td align="right">1.7%</td>
<td align="right">67.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">7,862,849</td>
<td align="right">1.6%</td>
<td align="right">69.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,810,106</td>
<td align="right">1.6%</td>
<td align="right">70.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,448,966</td>
<td align="right">1.5%</td>
<td align="right">72.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">7,126,568</td>
<td align="right">1.4%</td>
<td align="right">73.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">6,800,203</td>
<td align="right">1.4%</td>
<td align="right">74.9%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,229,777</td>
<td align="right">1.3%</td>
<td align="right">76.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,370,977</td>
<td align="right">1.1%</td>
<td align="right">77.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,282</td>
<td align="right">1.0%</td>
<td align="right">78.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,964,560</td>
<td align="right">1.0%</td>
<td align="right">79.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,724,481</td>
<td align="right">1.0%</td>
<td align="right">80.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,680,007</td>
<td align="right">0.9%</td>
<td align="right">81.2%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">0.9%</td>
<td align="right">82.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,582,247</td>
<td align="right">0.9%</td>
<td align="right">83.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,312,550</td>
<td align="right">0.9%</td>
<td align="right">84.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,959,748</td>
<td align="right">0.8%</td>
<td align="right">84.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,528,185</td>
<td align="right">0.7%</td>
<td align="right">85.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,510,910</td>
<td align="right">0.7%</td>
<td align="right">86.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,385,525</td>
<td align="right">0.7%</td>
<td align="right">86.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,351,372</td>
<td align="right">0.7%</td>
<td align="right">87.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,312,429</td>
<td align="right">0.7%</td>
<td align="right">88.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,150,126</td>
<td align="right">0.6%</td>
<td align="right">88.9%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,124,493</td>
<td align="right">0.6%</td>
<td align="right">89.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,733,525</td>
<td align="right">0.6%</td>
<td align="right">90.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,331,109</td>
<td align="right">0.5%</td>
<td align="right">90.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,234,033</td>
<td align="right">0.5%</td>
<td align="right">91.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,899,668</td>
<td align="right">0.4%</td>
<td align="right">91.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,861,847</td>
<td align="right">0.4%</td>
<td align="right">91.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,833,597</td>
<td align="right">0.4%</td>
<td align="right">92.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,698</td>
<td align="right">0.4%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,724,278</td>
<td align="right">0.3%</td>
<td align="right">92.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,707,172</td>
<td align="right">0.3%</td>
<td align="right">93.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,634,945</td>
<td align="right">0.3%</td>
<td align="right">93.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,593,173</td>
<td align="right">0.3%</td>
<td align="right">93.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,572,999</td>
<td align="right">0.3%</td>
<td align="right">94.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,538,593</td>
<td align="right">0.3%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,512,499</td>
<td align="right">0.3%</td>
<td align="right">94.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,468,465</td>
<td align="right">0.3%</td>
<td align="right">95.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,378,956</td>
<td align="right">0.3%</td>
<td align="right">95.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,269,392</td>
<td align="right">0.3%</td>
<td align="right">95.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,220,322</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,173,006</td>
<td align="right">0.2%</td>
<td align="right">96.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,077,600</td>
<td align="right">0.2%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">999,156</td>
<td align="right">0.2%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">967,690</td>
<td align="right">0.2%</td>
<td align="right">96.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">940,661</td>
<td align="right">0.2%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,820</td>
<td align="right">0.2%</td>
<td align="right">97.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">923,929</td>
<td align="right">0.2%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">857,674</td>
<td align="right">0.2%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">856,263</td>
<td align="right">0.2%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">826,831</td>
<td align="right">0.2%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">717,717</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">688,339</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">604,419</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">571,399</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">544,975</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">543,287</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">538,931</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">516,607</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">489,070</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">462,687</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">426,672</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">360,347</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">360,024</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">344,886</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">336,572</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">325,350</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">204,455</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">200,987</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">198,548</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,023</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">189,945</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">182,913</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,142</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,110</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,335</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,373</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">87,314</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">84,727</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,665</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,368</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">69,638</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">69,638</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,589</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,867</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,863</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">51,440</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">44,014</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,908</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">38,452</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,138</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,051</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,563</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">21,938</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,471</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,858</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,633</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,633</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,143</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,410</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,839</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">10,381</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,287</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,491</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,012</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,599</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,227</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,239</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,630</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">810</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">522</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">479</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">415</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">349</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">322</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">273</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">183</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">154</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">128</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">110</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">38</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">29</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
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
<td align="left">LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">16,939,197</td>
<td align="right">3.4%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">15,823,897</td>
<td align="right">3.2%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">12,043,783</td>
<td align="right">2.4%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">11,115,508</td>
<td align="right">2.3%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST RETURN_VALUE</td>
<td align="right">9,657,692</td>
<td align="right">2.0%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">8,495,400</td>
<td align="right">1.7%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">7,731,150</td>
<td align="right">1.6%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">7,447,269</td>
<td align="right">1.5%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL RETURN_VALUE</td>
<td align="right">7,388,713</td>
<td align="right">1.5%</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">POP_TOP JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,877,653</td>
<td align="right">1.4%</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">6,522,931</td>
<td align="right">1.3%</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">6,084,961</td>
<td align="right">1.2%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_LIST</td>
<td align="right">6,080,846</td>
<td align="right">1.2%</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,716,747</td>
<td align="right">1.2%</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST</td>
<td align="right">5,493,216</td>
<td align="right">1.1%</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">5,250,543</td>
<td align="right">1.1%</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">5,241,917</td>
<td align="right">1.1%</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK POP_TOP</td>
<td align="right">5,068,271</td>
<td align="right">1.0%</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">5,047,842</td>
<td align="right">1.0%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT POP_JUMP_IF_FALSE</td>
<td align="right">4,964,412</td>
<td align="right">1.0%</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,948,185</td>
<td align="right">1.0%</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,678,044</td>
<td align="right">0.9%</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE STORE_FAST</td>
<td align="right">4,645,296</td>
<td align="right">0.9%</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN RESUME_CHECK</td>
<td align="right">4,645,296</td>
<td align="right">0.9%</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_GEN</td>
<td align="right">4,645,296</td>
<td align="right">0.9%</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST PUSH_NULL</td>
<td align="right">4,326,671</td>
<td align="right">0.9%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST_LOAD_FAST</td>
<td align="right">4,223,003</td>
<td align="right">0.9%</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST YIELD_VALUE</td>
<td align="right">4,223,000</td>
<td align="right">0.9%</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST NOP</td>
<td align="right">3,695,675</td>
<td align="right">0.7%</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS</td>
<td align="right">3,651,315</td>
<td align="right">0.7%</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE BINARY_OP_EXTEND</td>
<td align="right">3,632,806</td>
<td align="right">0.7%</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,470,523</td>
<td align="right">0.7%</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">3,383,631</td>
<td align="right">0.7%</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_CONST_IMMORTAL</td>
<td align="right">3,362,472</td>
<td align="right">0.7%</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,350,350</td>
<td align="right">0.7%</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">3,283,363</td>
<td align="right">0.7%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">3,258,146</td>
<td align="right">0.7%</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_CONST_IMMORTAL</td>
<td align="right">3,210,938</td>
<td align="right">0.7%</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">3,161,726</td>
<td align="right">0.6%</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">3,129,107</td>
<td align="right">0.6%</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">3,111,633</td>
<td align="right">0.6%</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">3,038,209</td>
<td align="right">0.6%</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST</td>
<td align="right">2,993,646</td>
<td align="right">0.6%</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_CONST_IMMORTAL</td>
<td align="right">2,921,008</td>
<td align="right">0.6%</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">2,856,171</td>
<td align="right">0.6%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_SMALL_INT</td>
<td align="right">2,823,930</td>
<td align="right">0.6%</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">2,782,989</td>
<td align="right">0.6%</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">2,744,696</td>
<td align="right">0.6%</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND COPY</td>
<td align="right">2,663,120</td>
<td align="right">0.5%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">COPY TO_BOOL_INT</td>
<td align="right">2,663,112</td>
<td align="right">0.5%</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">2,532,487</td>
<td align="right">0.5%</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST</td>
<td align="right">2,517,716</td>
<td align="right">0.5%</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">SWAP SWAP</td>
<td align="right">2,366,713</td>
<td align="right">0.5%</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL RESUME_CHECK</td>
<td align="right">2,360,132</td>
<td align="right">0.5%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST</td>
<td align="right">2,240,110</td>
<td align="right">0.5%</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL STORE_FAST</td>
<td align="right">2,157,595</td>
<td align="right">0.4%</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,151,946</td>
<td align="right">0.4%</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_LIST</td>
<td align="right">2,115,730</td>
<td align="right">0.4%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST POP_ITER</td>
<td align="right">2,115,686</td>
<td align="right">0.4%</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">COPY STORE_FAST</td>
<td align="right">2,090,443</td>
<td align="right">0.4%</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST COPY</td>
<td align="right">2,090,123</td>
<td align="right">0.4%</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL CALL_NON_PY_GENERAL</td>
<td align="right">2,074,668</td>
<td align="right">0.4%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL LOAD_FAST</td>
<td align="right">2,067,700</td>
<td align="right">0.4%</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL RETURN_VALUE</td>
<td align="right">2,065,121</td>
<td align="right">0.4%</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS RESUME_CHECK</td>
<td align="right">1,861,791</td>
<td align="right">0.4%</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT COMPARE_OP_INT</td>
<td align="right">1,857,740</td>
<td align="right">0.4%</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF LOAD_FAST</td>
<td align="right">1,857,443</td>
<td align="right">0.4%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_DEREF</td>
<td align="right">1,857,397</td>
<td align="right">0.4%</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST_IMMORTAL</td>
<td align="right">1,834,917</td>
<td align="right">0.4%</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,833,566</td>
<td align="right">0.4%</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,820,712</td>
<td align="right">0.4%</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">1,803,707</td>
<td align="right">0.4%</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST</td>
<td align="right">1,803,584</td>
<td align="right">0.4%</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">1,783,948</td>
<td align="right">0.4%</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST</td>
<td align="right">1,778,070</td>
<td align="right">0.4%</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST GET_ITER</td>
<td align="right">1,714,833</td>
<td align="right">0.3%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">1,676,874</td>
<td align="right">0.3%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">COPY LOAD_SPECIAL</td>
<td align="right">1,675,686</td>
<td align="right">0.3%</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL SWAP</td>
<td align="right">1,675,686</td>
<td align="right">0.3%</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">SWAP LOAD_SPECIAL</td>
<td align="right">1,675,686</td>
<td align="right">0.3%</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND STORE_FAST</td>
<td align="right">1,652,304</td>
<td align="right">0.3%</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR</td>
<td align="right">1,647,013</td>
<td align="right">0.3%</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,631,058</td>
<td align="right">0.3%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_NON_PY_GENERAL</td>
<td align="right">1,618,599</td>
<td align="right">0.3%</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BUILD_TUPLE</td>
<td align="right">1,605,626</td>
<td align="right">0.3%</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL CALL_PY_EXACT_ARGS</td>
<td align="right">1,594,665</td>
<td align="right">0.3%</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL CALL_PY_GENERAL</td>
<td align="right">1,586,247</td>
<td align="right">0.3%</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT POP_JUMP_IF_FALSE</td>
<td align="right">1,572,959</td>
<td align="right">0.3%</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE CONTAINS_OP_DICT</td>
<td align="right">1,572,921</td>
<td align="right">0.3%</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT LOAD_FAST</td>
<td align="right">1,562,702</td>
<td align="right">0.3%</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_FAST</td>
<td align="right">1,520,755</td>
<td align="right">0.3%</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT BINARY_OP_EXTEND</td>
<td align="right">1,512,487</td>
<td align="right">0.3%</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST</td>
<td align="right">1,495,922</td>
<td align="right">0.3%</td>
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE POP_TOP</td>
<td align="right">1,365,343</td>
<td align="right">0.3%</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL CALL_FUNCTION_EX</td>
<td align="right">1,356,011</td>
<td align="right">0.3%</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST JUMP_FORWARD</td>
<td align="right">1,350,370</td>
<td align="right">0.3%</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK NOP</td>
<td align="right">1,345,883</td>
<td align="right">0.3%</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL</td>
<td align="right">1,331,921</td>
<td align="right">0.3%</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE</td>
<td align="right">1,319,317</td>
<td align="right">0.3%</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NONE</td>
<td align="right">1,301,019</td>
<td align="right">0.3%</td>
<td align="right">71.8%</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">13,179</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">670</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">289</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,177</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">896</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">33</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4</td>
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
<td align="right">7,447,269</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">706,672</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,397</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">39</td>
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
<td align="right">1,356,011</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">462,687</td>
<td align="right">25.4%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">928,897</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">441,500</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">415,898</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">28,027</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,231</td>
<td align="right">0.2%</td>
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
<td align="left">BUILD_STRING</td>
<td align="right">20,983</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,985</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3</td>
<td align="right">0.0%</td>
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
<td align="right">9,245</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">4,158</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">6</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">13,410</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">29,326</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">20,985</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">17,272</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">54,508</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,053</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7</td>
<td align="right">0.0%</td>
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
<td align="right">8,446</td>
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
<td align="right">8,446</td>
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
<td align="right">55,863</td>
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
<td align="right">55,863</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">20,997</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
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
<td align="right">29,690</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">8,708</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">2</td>
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
<td align="right">1,714,833</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">422,300</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">422,300</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">357,995</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">189,697</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,115,730</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">422,300</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">357,995</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">185,400</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,479</td>
<td align="right">0.7%</td>
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
<td align="right">7,731,150</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">422,986</td>
<td align="right">5.2%</td>
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
<td align="right">42,552</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">356</td>
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
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,562</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,702</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,355</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">210</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">42</td>
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
<td align="left">STORE_FAST</td>
<td align="right">3,695,675</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,345,883</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,102,298</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">970,605</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">844,600</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">5,493,216</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,299,925</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">935,910</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">442,227</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">435,400</td>
<td align="right">4.8%</td>
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
<td align="left">COPY</td>
<td align="right">8,449</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,883</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,297</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
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
<td align="left">RERAISE</td>
<td align="right">8,449</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,883</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,161</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4</td>
<td align="right">0.0%</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,115,686</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">176,661</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">21,555</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">8,761</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,520,755</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">422,298</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">357,994</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">21,524</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,440</td>
<td align="right">0.4%</td>
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
<td align="right">8,495,400</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,068,271</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,365,343</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,150,666</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">870,377</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,877,653</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,084,961</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,210,938</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,102,298</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">691,093</td>
<td align="right">3.6%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">9,061</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">4,226</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">4,158</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">128</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">47</td>
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
<td align="right">9,241</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,157</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">12</td>
<td align="right">0.1%</td>
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
<td align="right">4,326,671</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,803,707</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">920,669</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">34,036</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
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
<td align="right">2,532,487</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,074,668</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,356,011</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">945,448</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">145,337</td>
<td align="right">2.0%</td>
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
<td align="right">12,792</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">36</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">11</td>
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
<td align="right">4,223</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,223</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,223</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">129</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">33</td>
<td align="right">0.3%</td>
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
<td align="right">9,657,692</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,388,713</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,065,121</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,676,874</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">928,897</td>
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
<td align="left">POP_TOP</td>
<td align="right">8,495,400</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,731,150</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,856,171</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,676,874</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,150,629</td>
<td align="right">4.6%</td>
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
<td align="left">BUILD_TUPLE</td>
<td align="right">8,702</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,335</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,225</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">187</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">10</td>
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
<td align="right">12,921</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,316</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">187</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">19</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">12</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">686,446</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">878</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">107</td>
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
<td align="right">611,888</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">75,111</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">878</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">59</td>
<td align="right">0.0%</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,150,627</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">361,866</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,512,487</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">200,983</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">200,987</td>
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
<td align="right">4,223</td>
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
<td align="right">4,199</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">24</td>
<td align="right">0.6%</td>
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
<td align="right">442,159</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">26,005</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">20,987</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">8,801</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,717</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">422,296</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">36,859</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">34,853</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">21,118</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">793</td>
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
<td align="left">JUMP_FORWARD</td>
<td align="right">669,876</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">357,994</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">325,121</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">181,004</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">168,213</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">674,371</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">670,164</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">357,994</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,159</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">252</td>
<td align="right">0.0%</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">678,192</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">428,637</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">422,300</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">34,036</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">13,054</td>
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
<td align="right">1,158,151</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">422,301</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,685</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">20,985</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">8,708</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,983</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,702</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4</td>
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
<td align="right">1,605,626</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">849,216</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">422,301</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">416,411</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">180,933</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,150,625</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">844,605</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">422,300</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">415,900</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">415,898</td>
<td align="right">11.8%</td>
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
<td align="right">835</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">594</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">586</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">445</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">383</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,252</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">671</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">528</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">280</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">266</td>
<td align="right">5.8%</td>
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
<td align="right">140</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">43</td>
<td align="right">23.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">128</td>
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">12</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">12</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">7</td>
<td align="right">3.8%</td>
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
<td align="right">512,604</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">19,869</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,409</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,093</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">464</td>
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
<td align="right">488,995</td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">52,142</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,321</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">464</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">48</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">257</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">43</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">267</td>
<td align="right">82.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">43</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">3</td>
<td align="right">0.9%</td>
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
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">8,700</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">8,700</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">FORMAT_SIMPLE</td>
<td align="right">17,404</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">2,663,120</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,090,123</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">938,238</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">855,724</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">678,784</td>
<td align="right">8.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">2,663,112</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,090,443</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,675,686</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">842,423</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">422,287</td>
<td align="right">5.4%</td>
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
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,150,646</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">706,672</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,221</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">172</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,861,791</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">20</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">63,345</td>
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
<td align="right">42,230</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">20,985</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">126</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2</td>
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
<td align="left">POP_TOP</td>
<td align="right">128</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">126</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2</td>
<td align="right">1.6%</td>
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
<td align="right">428,639</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">34,036</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">8</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">462,687</td>
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
<td align="left">POP_EXCEPT</td>
<td align="right">129</td>
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
<td align="right">129</td>
<td align="right">100.0%</td>
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
<td align="right">918,694</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">21,479</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">488</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">491,944</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">426,516</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">21,555</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">488</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">69</td>
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
<td align="right">360,004</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
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
<td align="right">359,956</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">68</td>
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
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">359,944</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">255</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">148</td>
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
<td align="right">360,004</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">262</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">81</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">20,987</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,694</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">223</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">132</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">13</td>
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
<td align="right">33,896</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">134</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21</td>
<td align="right">0.1%</td>
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
<td align="right">4,883</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4,838</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">172</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">1,350,370</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">320,757</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">31,678</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,052</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">4,221</td>
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
<td align="right">695,059</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">669,876</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">324,980</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,057</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,084</td>
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
<td align="right">320,501</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">180,936</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">69,638</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">322</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">571,394</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5</td>
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
<td align="right">168,351</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">168,208</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">168,272</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">168,208</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11</td>
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
<td align="right">6,522,931</td>
<td align="right">77.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,647,013</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">242,247</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">19,580</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,620</td>
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
<td align="right">2,993,646</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,150,625</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">920,669</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">730,027</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">689,747</td>
<td align="right">8.2%</td>
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
<td align="left">STORE_NAME</td>
<td align="right">389</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">214</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">155</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">152</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">131</td>
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
<td align="left">MAKE_FUNCTION</td>
<td align="right">356</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">297</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">214</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">172</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">148</td>
<td align="right">9.1%</td>
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
<td align="right">1,857,397</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">20,987</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20,987</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">167</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">48</td>
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
<td align="right">1,857,443</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">41,974</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">134</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">36</td>
<td align="right">0.0%</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">15,823,897</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,115,508</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,084,961</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,493,216</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,241,917</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">16,939,197</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">9,657,692</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,522,931</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,716,747</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,250,543</td>
<td align="right">6.1%</td>
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
<td align="right">357,995</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">180,936</td>
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
<td align="left">SWAP</td>
<td align="right">357,995</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">180,936</td>
<td align="right">33.6%</td>
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
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">488,941</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">422,384</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,578</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">13</td>
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
<td align="right">488,937</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">422,296</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">12,568</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">82</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,517,716</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,783,948</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,778,070</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,159,371</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,150,629</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">3,283,363</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,783,948</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,631,058</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,618,599</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,150,625</td>
<td align="right">8.6%</td>
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
<td align="left">POP_TOP</td>
<td align="right">453</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">444</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">323</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">287</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">226</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,839</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">551</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">385</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">183</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">72</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">2,823,930</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">822,557</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">422,294</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">320,798</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">39,534</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,857,740</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">843,051</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">512,604</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">510,075</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">381,678</td>
<td align="right">8.3%</td>
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
<td align="right">1,675,686</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,675,686</td>
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
<td align="right">1,675,686</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,594,665</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">80,775</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">105</td>
<td align="right">0.0%</td>
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
<td align="right">68</td>
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
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">31</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">24</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3</td>
<td align="right">4.4%</td>
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
<td align="right">83,949</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">21,018</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">132</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">39</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">MAKE_CELL</td>
<td align="right">83,949</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">21,153</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">40</td>
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
<td align="left">TO_BOOL_INT</td>
<td align="right">4,964,412</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,129,107</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,038,209</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,572,959</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">883,478</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">5,241,917</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,834,917</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,778,070</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,365,343</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,319,317</td>
<td align="right">9.0%</td>
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
<td align="right">1,301,019</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">47,932</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20,985</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,713</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">159</td>
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
<td align="left">NOP</td>
<td align="right">621,788</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">536,382</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">177,361</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">17,020</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,069</td>
<td align="right">0.9%</td>
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
<td align="right">2,151,946</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,102,903</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">337,502</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">325,172</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">41,974</td>
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
<td align="right">1,803,584</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">898,960</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">488,941</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">336,555</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">320,798</td>
<td align="right">8.1%</td>
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
<td align="right">1,073,358</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">611,888</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">488,995</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">320,818</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">176,722</td>
<td align="right">6.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,236,939</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">746,595</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">612,215</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">34,992</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">26,171</td>
<td align="right">1.0%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4,224</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
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
<td align="left">COPY</td>
<td align="right">4,226</td>
<td align="right">100.0%</td>
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
<td align="right">8,449</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,223</td>
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
<td align="left">PUSH_EXC_INFO</td>
<td align="right">4,226</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,223</td>
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
<td align="right">29,562</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
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
<td align="right">29,461</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">65</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">33</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">58,795</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,729</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,112</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">743</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">255</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">33,592</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">28,431</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,858</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,833</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">972</td>
<td align="right">1.2%</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">41,974</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">41,974</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20,987</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">132</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">38</td>
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
<td align="right">41,970</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,121</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">20,987</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20,985</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">36</td>
<td align="right">0.0%</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">4,645,296</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,856,171</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,157,595</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,090,443</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,652,304</td>
<td align="right">6.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">11,115,508</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,678,044</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,695,675</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,090,123</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,350,370</td>
<td align="right">5.3%</td>
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
<td align="right">4,223,003</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">491,944</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,702</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">510</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">322</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">4,223,000</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">422,300</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">69,640</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">8,698</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">512</td>
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
<td align="right">1,215,843</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">842,423</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">838,229</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">415,901</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,200,490</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">838,232</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">426,519</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">422,437</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">415,901</td>
<td align="right">12.6%</td>
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
<td align="left">SWAP</td>
<td align="right">2,366,713</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,675,686</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">509,973</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">422,294</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">357,995</td>
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
<td align="left">SWAP</td>
<td align="right">2,366,713</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,675,686</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">691,020</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">422,287</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">357,995</td>
<td align="right">5.7%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">42</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">37</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">23</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">15</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">106</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">33</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2</td>
<td align="right">1.3%</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,223,000</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">844,605</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">510</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
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
<td align="right">4,645,296</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">422,986</td>
<td align="right">8.3%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">180,882</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">2,030</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="right">180,883</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">2,030</td>
<td align="right">1.1%</td>
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
<td align="right">843,051</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,177</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">35</td>
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
<td align="right">422,294</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">415,899</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">13,179</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,199</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">288</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">220</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">126</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">30</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17</td>
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
<td align="right">237</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">127</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">110</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">34</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">10</td>
<td align="right">1.9%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,632,806</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,512,487</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,150,625</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">320,742</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">180,931</td>
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
<td align="left">COPY</td>
<td align="right">2,663,120</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,652,304</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,150,638</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,150,627</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">180,933</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">69,636</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">69,636</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">75,631</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,980</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">109</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">75,763</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">8,700</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">188</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">47</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">15</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">336,412</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,428</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">46</td>
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
<td align="right">336,414</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,442</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">30</td>
<td align="right">0.0%</td>
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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">69,636</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">LIST_APPEND</td>
<td align="right">69,638</td>
<td align="right">100.0%</td>
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
<td align="right">43,948</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">66</td>
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
<td align="right">39,471</td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,221</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">322</td>
<td align="right">0.7%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">488,937</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">89</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">44</td>
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
<td align="right">489,070</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">71,772</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">26,333</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">4,199</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">31</td>
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
<td align="right">97,603</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,199</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">511</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">22</td>
<td align="right">0.0%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">25,184</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20,985</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,820</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">510</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">126</td>
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
<td align="right">55,736</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">127</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">17,522</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,716</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,536</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,199</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">126</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">35,138</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">180,782</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,319</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,326</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">28</td>
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
<td align="right">200,234</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4,221</td>
<td align="right">2.1%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">509,326</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">415,898</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">193,624</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">168,204</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">168,204</td>
<td align="right">11.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">596,770</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">509,432</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">189,697</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">168,204</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,351</td>
<td align="right">0.3%</td>
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
<td align="right">456,259</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">242,010</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">47,635</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">26,073</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">19,443</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">449,924</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">281,538</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">26,460</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">19,443</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">13,052</td>
<td align="right">1.6%</td>
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
<td align="right">455,693</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">415,898</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">29,723</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">12,568</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,355</td>
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
<td align="right">870,377</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">39,125</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">19,167</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">15</td>
<td align="right">0.0%</td>
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
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">69,636</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,543</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">126</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">69,636</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,700</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,700</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">254</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">21</td>
<td align="right">0.0%</td>
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
<td align="right">1,172,449</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">529</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13</td>
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
<td align="right">1,172,991</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">15</td>
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
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">77,240</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">128</td>
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
<td align="right">29,824</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,362</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,051</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,845</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">4,158</td>
<td align="right">5.4%</td>
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
<td align="right">198,536</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12</td>
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
<td align="right">198,548</td>
<td align="right">100.0%</td>
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
<td align="right">303,553</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">21,560</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">111</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">168,204</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">87,009</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">25,184</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">17,526</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">17,402</td>
<td align="right">5.3%</td>
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
<td align="left">BUILD_TUPLE</td>
<td align="right">180,931</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,952</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">13</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">180,933</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,442</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">510</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">35</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">22</td>
<td align="right">0.0%</td>
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
<td align="right">1,820,712</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">411,941</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">511</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">256</td>
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
<td align="right">1,150,666</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,081,890</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">426</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">255</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">47,184</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,199</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">55</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
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
<td align="left">POP_TOP</td>
<td align="right">25,075</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,404</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,953</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8</td>
<td align="right">0.0%</td>
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
<td align="right">1,236,397</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">32,401</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
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
<td align="left">POP_TOP</td>
<td align="right">721,906</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">422,569</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">38,588</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">20,197</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,706</td>
<td align="right">1.6%</td>
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
<td align="right">534,401</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">39,435</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">21,239</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,701</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">148</td>
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
<td align="right">555,849</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">39,534</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,849</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">30</td>
<td align="right">0.0%</td>
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
<td align="right">2,074,668</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,618,599</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,150,625</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">981,313</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">951,842</td>
<td align="right">11.2%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">2,157,595</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,067,700</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,065,121</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">678,784</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">488,937</td>
<td align="right">5.7%</td>
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
<td align="right">5,250,543</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,651,315</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,594,665</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">669,872</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">617,082</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">12,043,783</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">21,018</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,792</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">172</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,586,247</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,150,625</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">414,319</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">200,702</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">71,487</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">2,360,132</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,150,646</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">132</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">8,489</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">8,317</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">127</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">30</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">17</td>
<td align="right">0.2%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">426,519</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">23</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">STORE_FAST</td>
<td align="right">426,522</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">23</td>
<td align="right">0.0%</td>
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
<td align="right">130</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">127</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">19</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2</td>
<td align="right">1.3%</td>
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
<td align="right">1,857,740</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">435,488</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">422,487</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">320,795</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">37,106</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,129,107</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">17,891</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,093</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,033,841</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">39,495</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,214</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="right">883,478</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">176,722</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,700</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,700</td>
<td align="right">0.8%</td>
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
<td align="right">1,572,921</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">55</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">6</td>
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
<td align="right">1,572,959</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">19</td>
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
<td align="right">266</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">110</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">36</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3</td>
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
<td align="right">297</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">118</td>
<td align="right">28.4%</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,645,296</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">8,442</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">4,645,296</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,442</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">4</td>
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
<td align="right">6,080,846</td>
<td align="right">74.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,115,730</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,223,003</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,115,686</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,495,922</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">361,976</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">5</td>
<td align="right">0.0%</td>
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
<td align="right">357,863</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">185,400</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">24</td>
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
<td align="right">366,116</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">176,661</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">510</td>
<td align="right">0.1%</td>
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
<td align="right">9,097</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">8,754</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">POP_ITER</td>
<td align="right">8,761</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,759</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">322</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">13</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3</td>
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
<td align="left">POP_TOP</td>
<td align="right">6,877,653</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,678,044</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">571,394</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">426,519</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">422,298</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,080,846</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,645,296</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,073,593</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">918,694</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">844,600</td>
<td align="right">6.1%</td>
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
<td align="right">21,553</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">16,759</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">131</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">17,400</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,603</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,447</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">16,939,197</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,631,058</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">422,287</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">18,496</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,698</td>
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
<td align="right">4,948,185</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,161,726</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,647,013</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,572,921</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,331,921</td>
<td align="right">7.0%</td>
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
<td align="right">97,362</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">39,019</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">32,401</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">25,930</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">8</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,948,185</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">330,131</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">39,421</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,400</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">17,400</td>
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
<td align="right">2,782,989</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,236,397</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">981,313</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">198,722</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">148,271</td>
<td align="right">2.8%</td>
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
<td align="right">5,716,747</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,150,625</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">422,296</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">321,742</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">220,559</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,651,315</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,258,146</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">455,370</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">414,319</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">30,570</td>
<td align="right">0.4%</td>
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
<td align="right">3,383,631</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,086</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">256</td>
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
<td align="right">1,803,707</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,150,625</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">320,795</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">41,974</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">22,644</td>
<td align="right">0.7%</td>
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
<td align="right">1,176,548</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">361,862</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">183</td>
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
<td align="right">1,150,627</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">361,866</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,828</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,703</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,221</td>
<td align="right">0.3%</td>
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
<td align="right">695,764</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">21,110</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">510</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">174</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">707,822</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">9,721</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">174</td>
<td align="right">0.0%</td>
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
<td align="right">10,043</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">199</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">29</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">16</td>
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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">8,720</td>
<td align="right">84.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">510</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">255</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">254</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">169</td>
<td align="right">1.6%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,362,472</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,210,938</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,921,008</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,834,917</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">898,960</td>
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
<td align="right">7,388,713</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,362,472</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,586,247</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,267,793</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">855,724</td>
<td align="right">5.4%</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">381,678</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">168,216</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">145,337</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">78,251</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">50,601</td>
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
<td align="left">IMPORT_NAME</td>
<td align="right">359,944</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">198,536</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">90,658</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,240</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">71,487</td>
<td align="right">7.4%</td>
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
<td align="right">3,470,523</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,216,437</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">935,910</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">785,244</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">752,704</td>
<td align="right">10.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">3,111,633</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,857,397</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,172,449</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">752,704</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">502,796</td>
<td align="right">6.7%</td>
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
<td align="right">5,047,842</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,744,696</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,319,317</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,299,925</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,268,390</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">3,632,806</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,383,631</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,517,716</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,240,110</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,268,390</td>
<td align="right">8.0%</td>
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
<td align="right">23,776</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">24</td>
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
<td align="right">23,800</td>
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
<td align="right">1,833,566</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">31</td>
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
<td align="right">1,159,371</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">669,872</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,352</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,043,783</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">7,447,269</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,645,296</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,360,132</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,861,791</td>
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
<td align="right">15,823,897</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,068,271</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,470,523</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,744,696</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,345,883</td>
<td align="right">4.5%</td>
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
<td align="right">3,350,350</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">882,467</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">422,287</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,597</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">8,698</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,921,008</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">863,898</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">411,925</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">257,917</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">101,970</td>
<td align="right">2.2%</td>
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
<td align="right">8,720</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,651</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">10</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">9,615</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">766</td>
<td align="right">7.4%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">1,150,625</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">441,645</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">34,075</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">8,316</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">253</td>
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
<td align="right">1,562,702</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">51,181</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,025</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">13</td>
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
<td align="right">254</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">39</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">14</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">286</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">63</td>
<td align="right">18.1%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,331,921</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,172,991</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">679,802</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">507,863</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">449,924</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,038,209</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,073,358</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">200,983</td>
<td align="right">4.7%</td>
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
<td align="left">COPY</td>
<td align="right">2,663,112</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,150,730</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,150,638</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">37</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">22</td>
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
<td align="right">4,964,412</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">148</td>
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
<td align="right">678,291</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">320,795</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">47</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">22</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">678,338</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">320,818</td>
<td align="right">32.1%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">148,213</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,051</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">17,375</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,199</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">169,400</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21,623</td>
<td align="right">11.3%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">20,983</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">468</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">322</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">156</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">6</td>
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
<td align="right">21,858</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">80</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">838,196</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">19,443</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">30</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">838,229</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,445</td>
<td align="right">2.3%</td>
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
<td align="right">426,516</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">422,296</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">361,976</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,631</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,599</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,215,843</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,476</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">3</td>
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
<td align="right">64</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">10</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">8</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">5</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">110</td>
<td align="right">100.0%</td>
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
<td align="right">266</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">117</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">40</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">20</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12</td>
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
<td align="right">219</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">130</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">42</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">20</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">20</td>
<td align="right">4.2%</td>
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
<td align="right">37</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">42</td>
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
<td align="right">38</td>
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
<td align="right">38</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
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
<td align="right">1</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1</td>
<td align="right">50.0%</td>
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
<td align="left">BUILD_MAP</td>
<td align="right">15</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1</td>
<td align="right">6.2%</td>
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
<td align="right">5</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
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
<td align="right">5</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1</td>
<td align="right">16.7%</td>
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
<td align="right">91</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">47</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">42</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">29</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">14</td>
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
<td align="right">65</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">53</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">49</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">43</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">30</td>
<td align="right">11.0%</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">1</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">3</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">2</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2</td>
<td align="right">50.0%</td>
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
<td align="right">210</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">111</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">89</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">81</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">68</td>
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
<td align="right">389</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">123</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">91</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">48</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">4.9%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">3</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">29</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">29</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">12</td>
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
<td align="left">TO_BOOL</td>
<td align="right">4</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4</td>
<td align="right">33.3%</td>
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
<td align="right">515,553</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,194,807</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">215,279</td>
<td align="right">2.2%</td>
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
<td align="right">4,321</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">793</td>
<td align="right">15.5%</td>
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
<td align="right">294</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">164</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">79</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
<td align="right">14,143</td>
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
<td align="right">2,014</td>
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
<td align="right">21,797,446</td>
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
<td align="right">795</td>
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
<td align="right">3,380</td>
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
<td align="right">43</td>
<td align="right">23.5%</td>
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
<td align="right">140</td>
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
<td align="right">541,142</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,063,086</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">164,669</td>
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
<td align="right">3,369</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,557</td>
<td align="right">51.4%</td>
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
<td align="left">float long</td>
<td align="right">3,265</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">153</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">1.2%</td>
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
<td align="right">270</td>
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
<td align="right">1,573,414</td>
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
<td align="right">9</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43</td>
<td align="right">82.7%</td>
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
<td align="right">43</td>
<td align="right">100.0%</td>
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
<td align="right">940,122</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,411,479</td>
<td align="right">93.4%</td>
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
<td align="right">51</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
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
<td align="left">other</td>
<td align="right">164</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">164</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
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
<td align="right">8,442,564</td>
<td align="right">18.2%</td>
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
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">37,656,754</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">387,431</td>
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
<td align="right">11,588</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,862</td>
<td align="right">37.2%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">1,681</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,520</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">823</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">684</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.3%</td>
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
<td align="right">849</td>
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
<td align="right">9</td>
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
<td align="right">23,277,569</td>
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
<td align="right">270</td>
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
<td align="right">2,396</td>
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
<td align="right">13</td>
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
<td align="right">1,857,397</td>
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
<td align="right">55</td>
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
<td align="right">79,940</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,549,988</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">140,400</td>
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
<td align="right">3,618</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">743</td>
<td align="right">17.0%</td>
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
<td align="right">804</td>
<td align="right">108.2%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">44</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.3%</td>
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
<td align="right">21,265</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,634,945</td>
<td align="right">98.7%</td>
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
<td align="right">19</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">90.8%</td>
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
<td align="right">119</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
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
<td align="right">687,003</td>
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
<td align="right">10,489,199</td>
<td align="right">93.8%</td>
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
<td align="right">458</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">878</td>
<td align="right">65.7%</td>
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
<td align="right">336</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">133</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">22</td>
<td align="right">2.5%</td>
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
<td align="right">38</td>
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
<td align="right">2,077,996</td>
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
<td align="right">111</td>
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
<td align="right">276,496,747</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,270,402</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">204,382,812</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">908,873</td>
<td align="right">0.2%</td>
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
<td align="right">8,442,564</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">940,122</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">687,003</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">541,142</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">515,553</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,940</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,265</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,143</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,014</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">849</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">318,011</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">164,668</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,400</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">107,646</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">107,633</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">59,375</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">276</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">162</td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,158,494</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">21,886,339</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,158,494</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,731,115</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,379</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">17</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,731,056</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,509</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">467,565</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,648</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">25,019,575</td>
<td align="right">83.3%</td>
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
<td align="right">21,161,312</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">21,163,473</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">14,725,587</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">14,604,462</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,601</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,524</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">15,969,641</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,483,409</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">178,020,492</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">200,464,243</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">57,066,938</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">66,947,712</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">6,396,937</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,256,684</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">50,042,192</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">50,754,067</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
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
<td align="right">10,306,975</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">30,079</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">40,411</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">10,842,317</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">10,632</td>
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
<td align="right">1</td>
<td align="right">212</td>
<td align="right">9,538</td>
<td align="right">701</td>
<td align="right">643</td>
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
<td align="right">42</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-04
