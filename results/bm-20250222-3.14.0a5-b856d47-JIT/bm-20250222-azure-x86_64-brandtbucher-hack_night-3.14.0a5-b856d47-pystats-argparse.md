
# Pystats results

- benchmark: argparse
- fork: brandtbucher
- ref: hack-night
- commit hash: b856d47
- commit date: 2025-02-22T15:39:18-08:00

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
<td align="right">82,504,924</td>
<td align="right">19.6%</td>
<td align="right">19.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">25,768,162</td>
<td align="right">6.1%</td>
<td align="right">25.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">19,672,164</td>
<td align="right">4.7%</td>
<td align="right">30.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">15,363,642</td>
<td align="right">3.6%</td>
<td align="right">34.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,230,337</td>
<td align="right">3.6%</td>
<td align="right">37.6%</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">14,895,721</td>
<td align="right">3.5%</td>
<td align="right">41.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,134,231</td>
<td align="right">3.1%</td>
<td align="right">44.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,104,041</td>
<td align="right">3.1%</td>
<td align="right">47.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">12,847,886</td>
<td align="right">3.0%</td>
<td align="right">50.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,487,502</td>
<td align="right">3.0%</td>
<td align="right">53.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,424,034</td>
<td align="right">2.7%</td>
<td align="right">56.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,021,354</td>
<td align="right">2.1%</td>
<td align="right">58.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,290,660</td>
<td align="right">2.0%</td>
<td align="right">60.2%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">7,617,939</td>
<td align="right">1.8%</td>
<td align="right">62.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">7,054,033</td>
<td align="right">1.7%</td>
<td align="right">63.7%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,941,311</td>
<td align="right">1.6%</td>
<td align="right">65.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">6,728,415</td>
<td align="right">1.6%</td>
<td align="right">67.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">6,165,417</td>
<td align="right">1.5%</td>
<td align="right">68.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,107,709</td>
<td align="right">1.4%</td>
<td align="right">69.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,441,574</td>
<td align="right">1.3%</td>
<td align="right">71.2%</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">5,026,562</td>
<td align="right">1.2%</td>
<td align="right">72.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,917,177</td>
<td align="right">1.2%</td>
<td align="right">73.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,026,539</td>
<td align="right">1.0%</td>
<td align="right">74.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">3,759,951</td>
<td align="right">0.9%</td>
<td align="right">75.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,701,809</td>
<td align="right">0.9%</td>
<td align="right">76.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,603,302</td>
<td align="right">0.9%</td>
<td align="right">77.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,078,169</td>
<td align="right">0.7%</td>
<td align="right">77.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">3,071,056</td>
<td align="right">0.7%</td>
<td align="right">78.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,732,182</td>
<td align="right">0.6%</td>
<td align="right">79.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,687,041</td>
<td align="right">0.6%</td>
<td align="right">79.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,585,007</td>
<td align="right">0.6%</td>
<td align="right">80.5%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,536,405</td>
<td align="right">0.6%</td>
<td align="right">81.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,528,994</td>
<td align="right">0.6%</td>
<td align="right">81.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,396,066</td>
<td align="right">0.6%</td>
<td align="right">82.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,113,132</td>
<td align="right">0.5%</td>
<td align="right">82.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,063,117</td>
<td align="right">0.5%</td>
<td align="right">83.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,054,857</td>
<td align="right">0.5%</td>
<td align="right">83.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,004,194</td>
<td align="right">0.5%</td>
<td align="right">84.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,947,893</td>
<td align="right">0.5%</td>
<td align="right">84.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,938,331</td>
<td align="right">0.5%</td>
<td align="right">85.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,938,331</td>
<td align="right">0.5%</td>
<td align="right">85.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,938,331</td>
<td align="right">0.5%</td>
<td align="right">86.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,920,251</td>
<td align="right">0.5%</td>
<td align="right">86.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,836,502</td>
<td align="right">0.4%</td>
<td align="right">86.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,833,219</td>
<td align="right">0.4%</td>
<td align="right">87.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,813,613</td>
<td align="right">0.4%</td>
<td align="right">87.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,796,979</td>
<td align="right">0.4%</td>
<td align="right">88.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,771,074</td>
<td align="right">0.4%</td>
<td align="right">88.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,684,192</td>
<td align="right">0.4%</td>
<td align="right">89.0%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,636,267</td>
<td align="right">0.4%</td>
<td align="right">89.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,614,124</td>
<td align="right">0.4%</td>
<td align="right">89.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,505,806</td>
<td align="right">0.4%</td>
<td align="right">90.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">1,480,781</td>
<td align="right">0.4%</td>
<td align="right">90.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,447,170</td>
<td align="right">0.3%</td>
<td align="right">90.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,427,660</td>
<td align="right">0.3%</td>
<td align="right">91.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,380,288</td>
<td align="right">0.3%</td>
<td align="right">91.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,344,466</td>
<td align="right">0.3%</td>
<td align="right">91.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,305,405</td>
<td align="right">0.3%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,297,764</td>
<td align="right">0.3%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,282,468</td>
<td align="right">0.3%</td>
<td align="right">92.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,251,996</td>
<td align="right">0.3%</td>
<td align="right">93.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,213,781</td>
<td align="right">0.3%</td>
<td align="right">93.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,156,569</td>
<td align="right">0.3%</td>
<td align="right">93.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,148,093</td>
<td align="right">0.3%</td>
<td align="right">93.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,078,416</td>
<td align="right">0.3%</td>
<td align="right">94.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,039,674</td>
<td align="right">0.2%</td>
<td align="right">94.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,006,634</td>
<td align="right">0.2%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,006,627</td>
<td align="right">0.2%</td>
<td align="right">94.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">932,516</td>
<td align="right">0.2%</td>
<td align="right">95.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">931,809</td>
<td align="right">0.2%</td>
<td align="right">95.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">906,805</td>
<td align="right">0.2%</td>
<td align="right">95.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">890,204</td>
<td align="right">0.2%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">866,424</td>
<td align="right">0.2%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">856,883</td>
<td align="right">0.2%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">815,552</td>
<td align="right">0.2%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">732,100</td>
<td align="right">0.2%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">732,072</td>
<td align="right">0.2%</td>
<td align="right">96.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">706,308</td>
<td align="right">0.2%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">623,925</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">599,126</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">565,695</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">532,398</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">517,877</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">499,215</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">490,892</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">482,502</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">457,543</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">449,234</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">449,226</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">424,277</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">401,051</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">391,064</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">378,524</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">375,701</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">371,594</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">366,037</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">362,927</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">341,150</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">299,625</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">299,524</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">290,826</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">273,781</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">249,580</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">241,616</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">218,748</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">207,983</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">205,195</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">191,381</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">174,710</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">174,710</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">149,750</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">149,742</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">133,104</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">124,785</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">108,219</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">108,147</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">83,308</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">83,190</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">66,552</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">66,552</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">66,552</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">58,232</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">33,276</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">24,956</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">437</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">194</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">136</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">69</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">47</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">36</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">34</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">2,160.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">15</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">10</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
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
<td align="right">13,320,264</td>
<td align="right">3.2%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">12,725,336</td>
<td align="right">3.0%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">7,501,513</td>
<td align="right">1.8%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,404,695</td>
<td align="right">1.8%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">6,866,635</td>
<td align="right">1.6%</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">5,994,489</td>
<td align="right">1.4%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">5,983,007</td>
<td align="right">1.4%</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">5,915,013</td>
<td align="right">1.4%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST</td>
<td align="right">5,654,968</td>
<td align="right">1.3%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">5,108,015</td>
<td align="right">1.2%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL RETURN_VALUE</td>
<td align="right">4,397,355</td>
<td align="right">1.0%</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">4,203,963</td>
<td align="right">1.0%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">4,127,351</td>
<td align="right">1.0%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,109,659</td>
<td align="right">1.0%</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">4,043,305</td>
<td align="right">1.0%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">3,884,858</td>
<td align="right">0.9%</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">3,733,075</td>
<td align="right">0.9%</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,726,937</td>
<td align="right">0.9%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">3,550,852</td>
<td align="right">0.8%</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,277,727</td>
<td align="right">0.8%</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">3,194,424</td>
<td align="right">0.8%</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">3,186,324</td>
<td align="right">0.8%</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST STORE_FAST</td>
<td align="right">3,126,935</td>
<td align="right">0.7%</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_SMALL_INT</td>
<td align="right">3,110,771</td>
<td align="right">0.7%</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">3,107,046</td>
<td align="right">0.7%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">3,104,427</td>
<td align="right">0.7%</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">3,028,246</td>
<td align="right">0.7%</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">2,978,472</td>
<td align="right">0.7%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_FAST</td>
<td align="right">2,969,917</td>
<td align="right">0.7%</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST</td>
<td align="right">2,870,079</td>
<td align="right">0.7%</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,861,102</td>
<td align="right">0.7%</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST TO_BOOL_BOOL</td>
<td align="right">2,719,669</td>
<td align="right">0.6%</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST RETURN_VALUE</td>
<td align="right">2,579,172</td>
<td align="right">0.6%</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_FAST</td>
<td align="right">2,508,175</td>
<td align="right">0.6%</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST_IMMORTAL</td>
<td align="right">2,487,681</td>
<td align="right">0.6%</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_STR</td>
<td align="right">2,433,544</td>
<td align="right">0.6%</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,412,596</td>
<td align="right">0.6%</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST</td>
<td align="right">2,389,052</td>
<td align="right">0.6%</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_CONST_IMMORTAL</td>
<td align="right">2,353,283</td>
<td align="right">0.6%</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST</td>
<td align="right">2,278,159</td>
<td align="right">0.5%</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,255,541</td>
<td align="right">0.5%</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_CONST_IMMORTAL</td>
<td align="right">2,187,893</td>
<td align="right">0.5%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,171,259</td>
<td align="right">0.5%</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">2,054,851</td>
<td align="right">0.5%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE POP_TOP</td>
<td align="right">2,046,482</td>
<td align="right">0.5%</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">1,963,350</td>
<td align="right">0.5%</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR POP_JUMP_IF_TRUE</td>
<td align="right">1,946,890</td>
<td align="right">0.5%</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE STORE_FAST</td>
<td align="right">1,946,650</td>
<td align="right">0.5%</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH POP_JUMP_IF_FALSE</td>
<td align="right">1,938,331</td>
<td align="right">0.5%</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,938,331</td>
<td align="right">0.5%</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_CONST_IMMORTAL</td>
<td align="right">1,920,554</td>
<td align="right">0.5%</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT FOR_ITER_LIST</td>
<td align="right">1,906,422</td>
<td align="right">0.5%</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_SUBSCR_DICT</td>
<td align="right">1,906,299</td>
<td align="right">0.5%</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK NOP</td>
<td align="right">1,855,139</td>
<td align="right">0.4%</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BUILD_MAP</td>
<td align="right">1,855,137</td>
<td align="right">0.4%</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST</td>
<td align="right">1,813,680</td>
<td align="right">0.4%</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS RESUME_CHECK</td>
<td align="right">1,813,609</td>
<td align="right">0.4%</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">1,805,329</td>
<td align="right">0.4%</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS STORE_FAST</td>
<td align="right">1,796,904</td>
<td align="right">0.4%</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST_IMMORTAL</td>
<td align="right">1,779,286</td>
<td align="right">0.4%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT LOAD_CONST_IMMORTAL</td>
<td align="right">1,755,309</td>
<td align="right">0.4%</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL RESUME_CHECK</td>
<td align="right">1,722,038</td>
<td align="right">0.4%</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_FAST</td>
<td align="right">1,705,799</td>
<td align="right">0.4%</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_LIST</td>
<td align="right">1,696,823</td>
<td align="right">0.4%</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,688,072</td>
<td align="right">0.4%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR POP_JUMP_IF_FALSE</td>
<td align="right">1,679,478</td>
<td align="right">0.4%</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_GLOBAL_MODULE</td>
<td align="right">1,672,118</td>
<td align="right">0.4%</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_LIST_APPEND</td>
<td align="right">1,653,472</td>
<td align="right">0.4%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT COMPARE_OP_INT</td>
<td align="right">1,647,238</td>
<td align="right">0.4%</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,630,524</td>
<td align="right">0.4%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE CALL_PY_EXACT_ARGS</td>
<td align="right">1,597,248</td>
<td align="right">0.4%</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST</td>
<td align="right">1,507,137</td>
<td align="right">0.4%</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_FAST</td>
<td align="right">1,499,853</td>
<td align="right">0.4%</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE JUMP_BACKWARD_JIT</td>
<td align="right">1,499,777</td>
<td align="right">0.4%</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE</td>
<td align="right">1,497,468</td>
<td align="right">0.4%</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">1,464,344</td>
<td align="right">0.3%</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST PUSH_NULL</td>
<td align="right">1,456,315</td>
<td align="right">0.3%</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BINARY_OP_ADD_UNICODE</td>
<td align="right">1,405,911</td>
<td align="right">0.3%</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,405,911</td>
<td align="right">0.3%</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP POP_JUMP_IF_FALSE</td>
<td align="right">1,393,343</td>
<td align="right">0.3%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,388,936</td>
<td align="right">0.3%</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,364,372</td>
<td align="right">0.3%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE</td>
<td align="right">1,355,601</td>
<td align="right">0.3%</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,313,601</td>
<td align="right">0.3%</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,297,764</td>
<td align="right">0.3%</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_TUPLE</td>
<td align="right">1,297,764</td>
<td align="right">0.3%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,297,439</td>
<td align="right">0.3%</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS COPY_FREE_VARS</td>
<td align="right">1,272,874</td>
<td align="right">0.3%</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">1,264,494</td>
<td align="right">0.3%</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">NOP LOAD_GLOBAL_MODULE</td>
<td align="right">1,256,168</td>
<td align="right">0.3%</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,250,023</td>
<td align="right">0.3%</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT STORE_FAST</td>
<td align="right">1,247,860</td>
<td align="right">0.3%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">1,239,638</td>
<td align="right">0.3%</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">1,239,552</td>
<td align="right">0.3%</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">1,214,726</td>
<td align="right">0.3%</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST GET_ITER</td>
<td align="right">1,206,338</td>
<td align="right">0.3%</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST STORE_FAST</td>
<td align="right">1,206,279</td>
<td align="right">0.3%</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST POP_JUMP_IF_FALSE</td>
<td align="right">1,151,052</td>
<td align="right">0.3%</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_LIST</td>
<td align="right">1,143,548</td>
<td align="right">0.3%</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,139,714</td>
<td align="right">0.3%</td>
<td align="right">63.3%</td>
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
<td align="right">673,949</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">424,387</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">58,233</td>
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
<td align="left">STORE_FAST</td>
<td align="right">790,305</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">249,789</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">108,147</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,319</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8</td>
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
<td align="right">632,353</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">366,037</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">8,319</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2</td>
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
<td align="left">DICT_MERGE</td>
<td align="right">482,502</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">8,390</td>
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
<td align="left">STORE_FAST</td>
<td align="right">382,674</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">99,828</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">8,319</td>
<td align="right">1.7%</td>
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
<td align="right">1,405,911</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">230,356</td>
<td align="right">14.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,297,764</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">230,356</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">108,147</td>
<td align="right">6.6%</td>
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
<td align="right">1,056,517</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">881,814</td>
<td align="right">45.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,938,331</td>
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
<td align="right">174,710</td>
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
<td align="right">174,710</td>
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
<td align="right">66,552</td>
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
<td align="left">BUILD_STRING</td>
<td align="right">24,957</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">24,956</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,319</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">8,318</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
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
<td align="right">1,206,338</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">973,081</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">507,460</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">357,718</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">216,294</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,696,823</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">765,346</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">407,646</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">366,109</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">357,718</td>
<td align="right">9.7%</td>
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
<td align="right">1,006,634</td>
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
<td align="right">341,149</td>
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
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">307,874</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">33,276</td>
<td align="right">9.8%</td>
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
<td align="right">1,855,139</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">931,763</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">532,420</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">399,383</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">149,742</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,813,680</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,256,168</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">474,183</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">432,588</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">41,600</td>
<td align="right">1.0%</td>
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
<td align="right">205,192</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">201,065</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">2,728</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,402</td>
<td align="right">0.7%</td>
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
<td align="right">623,925</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">449,226</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">432,590</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">432,588</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
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
<td align="left">RERAISE</td>
<td align="right">623,925</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">449,226</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">432,590</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">432,588</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2</td>
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
<td align="right">931,368</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">695,285</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">589,755</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">422,365</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">93,216</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,705,799</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">232,938</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">191,337</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">183,018</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">174,031</td>
<td align="right">6.4%</td>
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
<td align="right">2,978,472</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,046,482</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">722,508</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">499,433</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">257,959</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">3,107,046</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">831,902</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">532,631</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">478,897</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">432,590</td>
<td align="right">6.2%</td>
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
<td align="right">623,927</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">623,925</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">432,588</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">149,742</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">108,147</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,938,331</td>
<td align="right">100.0%</td>
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
<td align="right">3,186,324</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,456,315</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">124,789</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">124,785</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">24,956</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">3,028,246</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">565,710</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">440,906</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">399,401</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">232,932</td>
<td align="right">4.7%</td>
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
<td align="right">4,397,355</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,579,172</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,264,494</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">840,219</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">557,373</td>
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
<td align="left">STORE_FAST</td>
<td align="right">4,043,305</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,978,472</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,264,494</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,006,634</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">732,072</td>
<td align="right">5.9%</td>
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
<td align="right">108,147</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">52</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">108,150</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">52</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">4</td>
<td align="right">0.0%</td>
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
<td align="right">158,119</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">83,190</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">217</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">76</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">241,342</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">217</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">32</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">9</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">218,742</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">218,748</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">515,810</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">183,020</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">133,104</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">58,235</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">33,314</td>
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
<td align="left">CALL_PY_GENERAL</td>
<td align="right">432,588</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">274,539</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">108,147</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">58,233</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">33,276</td>
<td align="right">3.6%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">657,200</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">482,508</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">357,718</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">307,812</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">291,275</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,206,279</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">873,499</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">357,718</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">208,085</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">174,699</td>
<td align="right">5.7%</td>
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
<td align="right">1,855,137</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">407,634</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">149,741</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">83,190</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">83,190</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,630,524</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">890,137</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">166,380</td>
<td align="right">6.2%</td>
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
<td align="right">24,957</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">8,318</td>
<td align="right">25.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">24,957</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,319</td>
<td align="right">25.0%</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">881,818</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">807,024</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">391,075</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">141,423</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">124,788</td>
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
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">881,814</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">557,373</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">307,873</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">166,386</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">149,742</td>
<td align="right">6.2%</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">93</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">79</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">75</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">57</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">25</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">116</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">110</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">30</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">28</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">28</td>
<td align="right">6.4%</td>
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
<td align="right">83,190</td>
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
<td align="right">83,190</td>
<td align="right">100.0%</td>
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
<td align="right">26</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">21</td>
<td align="right">44.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">21</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">17</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">3</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">2</td>
<td align="right">4.3%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">298,940</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">58,257</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">9,685</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">4,704</td>
<td align="right">1.3%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">357,168</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">9,685</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">4,716</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">25</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">869,222</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">632,246</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">218,742</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">49,914</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">912</td>
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
<td align="right">1,393,343</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">376,805</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">912</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6</td>
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
<td align="right">41,595</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">24,956</td>
<td align="right">37.5%</td>
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
<td align="left">FORMAT_SIMPLE</td>
<td align="right">66,552</td>
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
<td align="left">RAISE_VARARGS</td>
<td align="right">623,925</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">299,484</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">58,231</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">24,959</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
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
<td align="left">POP_EXCEPT</td>
<td align="right">623,925</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">299,488</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">83,198</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4</td>
<td align="right">0.0%</td>
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
<td align="right">1,272,874</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">366,037</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">74,871</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">41,595</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">33,276</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,813,609</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">4</td>
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
<td align="right">482,502</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">482,502</td>
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
<td align="left">GET_ITER</td>
<td align="right">108,167</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">66,552</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">58,265</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">58,243</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,333</td>
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
<td align="left">FOR_ITER</td>
<td align="right">166,380</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">66,552</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">58,267</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">8,334</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">52</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">503,976</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">407,646</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">166,380</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">414</td>
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
<td align="right">531,475</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">422,365</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">124,148</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">5</td>
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
<td align="right">108,147</td>
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
<td align="right">108,147</td>
<td align="right">100.0%</td>
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
<td align="right">267,554</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">108,147</td>
<td align="right">28.8%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">267,554</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">108,147</td>
<td align="right">28.8%</td>
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
<td align="right">1,039,591</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">70</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
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

<table>
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
<td align="right">731,691</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">307,912</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">71</td>
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
<td align="left">POP_EXCEPT</td>
<td align="right">449,226</td>
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
<td align="right">299,484</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">149,742</td>
<td align="right">33.3%</td>
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
<td align="right">698,086</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">191,346</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">191,337</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">133,107</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">33,276</td>
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
<td align="right">922,706</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">116,466</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">83,199</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">83,190</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">58,233</td>
<td align="right">4.5%</td>
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
<td align="right">266,208</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">91,509</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">58,233</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">8,319</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">423,517</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">756</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">4</td>
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
<td align="right">83,190</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">41,590</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">83,190</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">33,276</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">8,319</td>
<td align="right">6.7%</td>
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
<td align="right">915,462</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">174,706</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">149,743</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,369</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,593</td>
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
<td align="right">465,907</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">158,089</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">149,744</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">149,742</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">149,742</td>
<td align="right">12.0%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">923,409</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">698,796</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">667,225</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">574,082</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">432,588</td>
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
<td align="right">898,452</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">840,219</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">557,481</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">524,096</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">359,420</td>
<td align="right">7.2%</td>
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
<td align="right">12,725,336</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,501,513</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,994,489</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,983,007</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,915,013</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,320,264</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,404,695</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,203,963</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,109,659</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,277,727</td>
<td align="right">4.0%</td>
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
<td align="right">357,718</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">8,319</td>
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
<td align="left">SWAP</td>
<td align="right">357,718</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">8,319</td>
<td align="right">2.3%</td>
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
<td align="right">3,194,424</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,870,079</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,278,159</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,029,789</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">757,095</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,726,937</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,550,852</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,250,023</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,239,638</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,125,674</td>
<td align="right">7.6%</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">69</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">30</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">28</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">117</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">51</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4</td>
<td align="right">2.1%</td>
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
<td align="right">3,110,771</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">865,184</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">640,579</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">449,228</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">299,486</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,647,238</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,247,860</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">865,184</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">532,431</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">399,461</td>
<td align="right">6.5%</td>
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
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">4</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1</td>
<td align="right">14.3%</td>
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
<td align="right">998,280</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">141,423</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">8,319</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">70</td>
<td align="right">0.0%</td>
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
<td align="left">MAKE_CELL</td>
<td align="right">998,280</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">149,811</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2</td>
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
<td align="right">3,884,858</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,938,331</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,805,329</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,679,478</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,393,343</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">5,994,489</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,278,159</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,046,482</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,779,286</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">698,796</td>
<td align="right">4.5%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">465,872</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">324,451</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">66,552</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">715,443</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">83,190</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">41,598</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,318</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,318</td>
<td align="right">1.0%</td>
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
<td align="right">1,688,072</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">282,846</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">33,274</td>
<td align="right">1.7%</td>
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
<td align="right">739,621</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">415,950</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">316,120</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">266,208</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">149,742</td>
<td align="right">7.5%</td>
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
<td align="right">3,733,075</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,946,890</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">731,691</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">682,165</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">449,646</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">5,654,968</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,499,777</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">798,235</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">399,383</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">299,484</td>
<td align="right">3.3%</td>
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
<td align="right">623,925</td>
<td align="right">85.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">108,147</td>
<td align="right">14.8%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">623,925</td>
<td align="right">85.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">108,147</td>
<td align="right">14.8%</td>
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
<td align="right">623,925</td>
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
<td align="left">PUSH_EXC_INFO</td>
<td align="right">623,925</td>
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
<td align="right">307,874</td>
<td align="right">78.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">83,190</td>
<td align="right">21.3%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">224,684</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">83,190</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">83,190</td>
<td align="right">21.3%</td>
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
<td align="right">20</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">14</td>
<td align="right">41.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">27</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1</td>
<td align="right">2.9%</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">249,570</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">166,380</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">166,380</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">83,190</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">83,190</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">249,567</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">224,684</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">166,380</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">83,190</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">83,190</td>
<td align="right">9.3%</td>
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
<td align="right">4,043,305</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,126,935</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,389,052</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,946,650</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,796,904</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">12,725,336</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,194,424</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,104,427</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,297,439</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">931,763</td>
<td align="right">3.6%</td>
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
<td align="right">207,974</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">207,971</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
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
<td align="right">706,298</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">249,576</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">108,147</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">83,198</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">66,556</td>
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
<td align="right">449,334</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">208,085</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">191,337</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">183,022</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">115,414</td>
<td align="right">9.5%</td>
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
<td align="right">490,821</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">357,718</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">357,718</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">174,031</td>
<td align="right">12.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">432,588</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">357,718</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">357,718</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">174,031</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">58,233</td>
<td align="right">4.2%</td>
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
<td align="right">21</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">27</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">6</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3</td>
<td align="right">8.3%</td>
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
<td align="right">10</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">4</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">2</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">2</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">13</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1</td>
<td align="right">5.0%</td>
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
<td align="right">399,461</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">124,784</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">74,873</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
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
<td align="right">224,632</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">216,294</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">83,300</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">58,233</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">16,637</td>
<td align="right">2.8%</td>
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
<td align="right">1,405,911</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">74,867</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,405,911</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">33,276</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">33,276</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,318</td>
<td align="right">0.6%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,125,674</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">218,748</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
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
<td align="left">TO_BOOL_INT</td>
<td align="right">1,128,148</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">216,298</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">149,746</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
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
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">149,742</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">732,072</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">682,158</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">557,373</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">91,508</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="left">PUSH_EXC_INFO</td>
<td align="right">623,927</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">557,373</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">507,459</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">366,035</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">8,318</td>
<td align="right">0.4%</td>
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
<td align="right">432,588</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">299,484</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
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
<td align="right">732,100</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">273,738</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">STORE_FAST</td>
<td align="right">165,587</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">66,552</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,593</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">865,184</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">41,616</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">865,172</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">41,610</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">83,286</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">83,190</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">70</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">19</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4</td>
<td align="right">0.0%</td>
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
<td align="right">48</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21</td>
<td align="right">30.4%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">69</td>
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
<td align="right">299,494</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">12</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">149,752</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">149,746</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">6</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">149,742</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">24,961</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">149,754</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">24,956</td>
<td align="right">14.3%</td>
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
<td align="right">174,698</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,317</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,317</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18</td>
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
<td align="right">191,381</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">66,550</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">66,552</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">823,459</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">257,884</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">216,294</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">108,146</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">99,827</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">623,925</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">507,460</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">249,570</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">108,516</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,318</td>
<td align="right">0.6%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,022,847</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">274,527</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">173,649</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">149,742</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">133,104</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">831,704</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">722,508</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">149,742</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">133,104</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">83,190</td>
<td align="right">4.3%</td>
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
<td align="right">2,171,259</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">149,742</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">149,742</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">58,232</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,796,904</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">432,588</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">149,742</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">149,742</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">499,170</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">499,140</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">66</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">9</td>
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
<td align="right">1,497,468</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">557,375</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,054,851</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
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
<td align="right">58,230</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
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
<td align="left">COPY_FREE_VARS</td>
<td align="right">33,276</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">24,956</td>
<td align="right">42.9%</td>
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
<td align="right">290,823</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
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
<td align="right">274,190</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,318</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,318</td>
<td align="right">2.9%</td>
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
<td align="right">532,377</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
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
<td align="right">490,803</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">41,595</td>
<td align="right">7.8%</td>
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
<td align="right">865,212</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">66,552</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">24</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">640,579</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">108,148</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">66,576</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">58,233</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">58,233</td>
<td align="right">6.2%</td>
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
<td align="right">1,653,472</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">108,149</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">74,876</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">697,433</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">373,710</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">266,212</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">158,061</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">133,105</td>
<td align="right">7.2%</td>
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
<td align="right">2,861,102</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,630,524</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,313,601</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">507,459</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">208,085</td>
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
<td align="left">STORE_FAST</td>
<td align="right">3,126,935</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,719,669</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">507,459</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">124,785</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">108,147</td>
<td align="right">1.6%</td>
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
<td align="right">1,388,936</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">58,232</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">840,219</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">440,570</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">108,148</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">58,233</td>
<td align="right">4.0%</td>
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
<td align="right">213,163</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">149,742</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">149,742</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">117,812</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">53,707</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">41,596</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">49</td>
<td align="right">0.0%</td>
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
<td align="right">374,357</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">249,789</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">116,461</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">74,868</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">49</td>
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
<td align="right">499,433</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">116,461</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">83,190</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">58,233</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">41,595</td>
<td align="right">5.1%</td>
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
<td align="right">724,739</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">149,742</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">133,104</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">124,834</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">83,189</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">274,599</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">257,959</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">241,321</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">184,009</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">108,147</td>
<td align="right">8.4%</td>
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
<td align="right">4,203,963</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,597,248</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,239,638</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">416,001</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">391,029</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">6,866,635</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,272,874</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">141,423</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,017</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,560</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">615,610</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">432,588</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">299,480</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">183,018</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">149,742</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,722,038</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">74,871</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">70</td>
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
<td align="right">565,694</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">557,375</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,317</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="right">1,647,238</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">407,629</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">58,233</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">25</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
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
<td align="right">1,805,329</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">307,803</td>
<td align="right">14.6%</td>
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
<td align="right">715,988</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">582,393</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">316,122</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">64,952</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,716</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,679,478</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">4,704</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">10</td>
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
<td align="right">358,961</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">282,838</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">183,018</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">41,601</td>
<td align="right">4.8%</td>
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
<td align="right">732,069</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">134,349</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">359,420</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">41,593</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">24</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">359,421</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">41,614</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,906,422</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,696,823</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">52</td>
<td align="right">0.0%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">2,389,052</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">931,368</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">207,974</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">66,552</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,355</td>
<td align="right">0.2%</td>
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
<td align="left">GET_ITER</td>
<td align="right">366,109</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">12,413</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">STORE_FAST</td>
<td align="right">285,308</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">93,216</td>
<td align="right">24.6%</td>
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
<td align="right">1,297,764</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">765,346</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">473,293</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,946,650</td>
<td align="right">76.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">589,755</td>
<td align="right">23.3%</td>
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
<td align="right">1,499,777</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">478,897</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">423,517</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">373,710</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">116,466</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,906,422</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">503,976</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">473,293</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">116,466</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">58,265</td>
<td align="right">1.9%</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,297,764</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,297,764</td>
<td align="right">100.0%</td>
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
<td align="right">24,955</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">24,956</td>
<td align="right">100.0%</td>
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
<td align="right">13,320,264</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,250,023</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">332,756</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">220,815</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">106,363</td>
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
<td align="right">4,127,351</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,255,541</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,355,601</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,022,847</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">973,081</td>
<td align="right">6.4%</td>
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
<td align="right">7,404,695</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,255,541</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">557,481</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">507,459</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">324,443</td>
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
<td align="right">7,501,513</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,920,554</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">923,409</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">665,703</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">213,163</td>
<td align="right">1.9%</td>
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
<td align="right">4,109,659</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">524,096</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">432,588</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">207,971</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">141,418</td>
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
<td align="right">2,187,893</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,963,350</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">757,095</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">391,029</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">108,134</td>
<td align="right">2.0%</td>
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
<td align="right">5,108,015</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">873,494</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">117,812</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">8,318</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">3,186,324</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">873,494</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">558,719</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">432,588</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">432,588</td>
<td align="right">7.1%</td>
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
<td align="right">299,486</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">149,742</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="left">COPY</td>
<td align="right">299,484</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">149,742</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">2,487,681</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,353,283</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,187,893</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,920,554</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,779,286</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">4,397,355</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,508,175</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,353,283</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,672,118</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,388,936</td>
<td align="right">7.1%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">848,215</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">740,377</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">440,906</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">307,873</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">158,060</td>
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
<td align="right">806,941</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">532,377</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">341,149</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">316,122</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">299,480</td>
<td align="right">8.0%</td>
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
<td align="right">2,412,596</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,938,331</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,364,372</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,297,439</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,139,714</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">5,915,013</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,497,468</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,139,714</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,056,517</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,029,789</td>
<td align="right">7.8%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">3,104,427</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,672,118</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,464,344</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,355,601</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,256,168</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,108,015</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,597,248</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,507,137</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,039,591</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">715,988</td>
<td align="right">5.5%</td>
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
<td align="right">133,103</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
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
<td align="right">133,104</td>
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
<td align="right">457,539</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">324,439</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">133,104</td>
<td align="right">29.1%</td>
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
<td align="right">6,866,635</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,813,609</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,722,038</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">732,100</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">632,353</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">5,983,007</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,412,596</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,855,139</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,214,726</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">382,674</td>
<td align="right">3.0%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,726,937</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,277,727</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">49,340</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">27</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
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
<td align="right">2,870,079</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,239,552</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">748,754</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">657,200</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">449,228</td>
<td align="right">6.4%</td>
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
<td align="right">1,906,299</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">41,590</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
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
<td align="right">1,755,309</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">89,663</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">58,232</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">36,368</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,320</td>
<td align="right">0.4%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,719,669</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,054,851</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">831,704</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">663,916</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">499,140</td>
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
<td align="right">3,884,858</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,733,075</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">1,128,148</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">299,488</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,128,156</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">299,500</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4</td>
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
<td align="right">1,143,548</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">689,662</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,151,052</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">682,165</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">2</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">323,853</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">184,009</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,305</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,709</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">449,646</td>
<td align="right">86.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">66,542</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,689</td>
<td align="right">0.3%</td>
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
<td align="right">2,433,544</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">149,756</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,689</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12</td>
<td align="right">0.0%</td>
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
<td align="right">1,946,890</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">636,408</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,709</td>
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
<td align="left">BINARY_OP</td>
<td align="right">108,147</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">41,595</td>
<td align="right">27.8%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">108,147</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">41,595</td>
<td align="right">27.8%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">116,461</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">66,552</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">66,552</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">249,576</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4</td>
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
<td align="right">531,475</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">166,398</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">8,355</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">49</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
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
<td align="right">706,298</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10</td>
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
<td align="left">CALL_LIST_APPEND</td>
<td align="right">697,433</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">291,139</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">228,048</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">218,466</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">89,663</td>
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
<td align="left">POP_ITER</td>
<td align="right">695,285</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">220,815</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">218,466</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">205,192</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">170,971</td>
<td align="right">10.6%</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1</td>
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
<td align="left">TO_BOOL_INT</td>
<td align="right">4</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2</td>
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
<td align="left">COPY</td>
<td align="right">4</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2</td>
<td align="right">33.3%</td>
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
<td align="right">5</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">4</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">15</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">47</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">29</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">47</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">21</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">15</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">11</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8</td>
<td align="right">5.9%</td>
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
<td align="left">LOAD_FAST</td>
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
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2</td>
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
<td align="right">6</td>
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
<td align="right">2</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2</td>
<td align="right">33.3%</td>
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
<td align="right">4</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">8</td>
<td align="right">100.0%</td>
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
<td align="right">8</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2</td>
<td align="right">20.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">6</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">4</td>
<td align="right">40.0%</td>
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
<td align="right">931,758</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,840,108</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8</td>
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
<td align="right">60</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">698</td>
<td align="right">92.1%</td>
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
<td align="right">402</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">101</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">98</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">97</td>
<td align="right">13.9%</td>
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
<td align="right">1,156,569</td>
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
<td align="right">97,088</td>
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
<td align="right">31,141,777</td>
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
<td align="right">98,883</td>
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
<td align="right">2,232</td>
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
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
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
<td align="right">21</td>
<td align="right">44.7%</td>
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
<td align="right">26</td>
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
<td align="right">357,168</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,561,975</td>
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
<td align="right">253,585</td>
<td align="right">6.1%</td>
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
<td align="right">4,741</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">14,389</td>
<td align="right">75.2%</td>
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
<td align="right">14,389</td>
<td align="right">100.0%</td>
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
<td align="right">1,770,154</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,306,119</td>
<td align="right">42.4%</td>
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
<td align="right">8</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">912</td>
<td align="right">99.1%</td>
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
<td align="right">714</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">102</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">96</td>
<td align="right">10.5%</td>
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
<td align="right">1,077,993</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,518,215</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">16</td>
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
<td align="right">9</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">414</td>
<td align="right">97.9%</td>
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
<td align="left">dict keys</td>
<td align="right">184</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">145</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">52</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">31</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2</td>
<td align="right">0.5%</td>
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
<td align="right">1,248,076</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">33,356,973</td>
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
<td align="right">6,557,680</td>
<td align="right">15.9%</td>
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
<td align="right">124,123</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">702</td>
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
<td align="left">method</td>
<td align="right">394</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">49</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">47</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">47</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">47</td>
<td align="right">6.7%</td>
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
<td align="right">26</td>
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
<td align="right">36</td>
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
<td align="right">26,238,236</td>
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
<td align="right">36</td>
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
<td align="right">169</td>
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
<td align="right">2</td>
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
<td align="right">590,647</td>
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
<td align="right">5</td>
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
<td align="right">7</td>
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
<td align="right">4,437,830</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,616,203</td>
<td align="right">37.1%</td>
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
<td align="right">49,367</td>
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
<td align="right">108,163</td>
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
<td align="right">1,979,933</td>
<td align="right">94.8%</td>
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
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">52</td>
<td align="right">92.9%</td>
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
<td align="left">list slice</td>
<td align="right">52</td>
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
<td align="right">241,351</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,076,442</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">180,101</td>
<td align="right">1.2%</td>
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
<td align="right">3,446</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">217</td>
<td align="right">5.9%</td>
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
<td align="right">145</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">51</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">9.7%</td>
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
<td align="right">1,164,801</td>
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
<td align="right">229,073,878</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">6,912,755</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">175,571,447</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">9,706,944</td>
<td align="right">2.3%</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">1,770,154</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,248,076</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,156,569</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,077,993</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">931,758</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">357,168</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">241,351</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">108,163</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">97,088</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">26</td>
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
<td align="right">5,188,974</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,616,203</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,368,706</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">253,585</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">90,878</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">90,351</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">89,744</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">8,003</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">432</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">432</td>
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
<td align="right">1,006,711</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">12,038,159</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,006,711</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,006,711</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,006,711</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">1,747,006</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">13,219,580</td>
<td align="right">101.3%</td>
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
<td align="right">20,456,945</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">20,456,969</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">20,908,052</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">20,774,577</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">133,453</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">22,691,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">673,851</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">165,260,711</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">194,087,368</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">67,961,157</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">76,232,461</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">57,185,759</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">77,427,512</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">63,380,092</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">65,709,538</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">83,190</td>
<td align="right">12.3%</td>
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
<td align="right">12,229,791</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">467,047</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">467,014</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,847,842</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">5,867</td>
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
<td align="right">694</td>
<td align="right">1,405,345</td>
<td align="right">17,673,459</td>
<td align="right">127,979</td>
<td align="right">1,407,489</td>
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
<td align="right">929</td>
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
<td align="right">560</td>
<td align="right">60.3%</td>
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
<td align="right">108</td>
<td align="right">11.6%</td>
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
<td align="right">22</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">43</td>
<td align="right">4.6%</td>
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
<td align="right">42</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">347</td>
<td align="right">37.4%</td>
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
<td align="right">2,467,773</td>
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
<td align="right">55,121,099</td>
<td align="right">2,233.6%</td>
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
<td align="right">560</td>
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
<td align="right">414</td>
<td align="right">73.9%</td>
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
<td align="right">3,891,200</td>
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
<td align="right">2,788,122</td>
<td align="right">71.7%</td>
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
<td align="right">470,368</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">632,710</td>
<td align="right">16.3%</td>
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
<td align="left">149</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">132</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">88</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">45</td>
<td align="right">10.9%</td>
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
<td align="left"><= 8</td>
<td align="right">42</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">65</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">132</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">126</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">195</td>
<td align="right">34.8%</td>
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
<td align="left"><= 4</td>
<td align="right">21</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">43</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">64</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">174</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">89</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">23</td>
<td align="right">4.1%</td>
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
<td align="right">7,638,714</td>
<td align="right">13.9%</td>
<td align="right">13.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">6,429,308</td>
<td align="right">11.7%</td>
<td align="right">25.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,117,981</td>
<td align="right">5.7%</td>
<td align="right">31.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">3,112,149</td>
<td align="right">5.6%</td>
<td align="right">36.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,924,800</td>
<td align="right">5.3%</td>
<td align="right">42.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,467,773</td>
<td align="right">4.5%</td>
<td align="right">46.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">2,467,773</td>
<td align="right">4.5%</td>
<td align="right">51.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">1,581,441</td>
<td align="right">2.9%</td>
<td align="right">54.0%</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">1,452,966</td>
<td align="right">2.6%</td>
<td align="right">56.6%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,413,110</td>
<td align="right">2.6%</td>
<td align="right">59.2%</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,413,110</td>
<td align="right">2.6%</td>
<td align="right">61.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,180,204</td>
<td align="right">2.1%</td>
<td align="right">63.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,057,769</td>
<td align="right">1.9%</td>
<td align="right">65.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,034,832</td>
<td align="right">1.9%</td>
<td align="right">67.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">1,034,832</td>
<td align="right">1.9%</td>
<td align="right">69.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">1,034,832</td>
<td align="right">1.9%</td>
<td align="right">71.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,004,712</td>
<td align="right">1.8%</td>
<td align="right">73.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">861,209</td>
<td align="right">1.6%</td>
<td align="right">74.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">755,528</td>
<td align="right">1.4%</td>
<td align="right">76.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">712,121</td>
<td align="right">1.3%</td>
<td align="right">77.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">644,376</td>
<td align="right">1.2%</td>
<td align="right">78.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">637,591</td>
<td align="right">1.2%</td>
<td align="right">79.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">617,439</td>
<td align="right">1.1%</td>
<td align="right">80.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">594,783</td>
<td align="right">1.1%</td>
<td align="right">82.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">577,513</td>
<td align="right">1.0%</td>
<td align="right">83.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">536,655</td>
<td align="right">1.0%</td>
<td align="right">84.0%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">536,655</td>
<td align="right">1.0%</td>
<td align="right">85.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">464,301</td>
<td align="right">0.8%</td>
<td align="right">85.8%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">442,921</td>
<td align="right">0.8%</td>
<td align="right">86.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">388,325</td>
<td align="right">0.7%</td>
<td align="right">87.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">366,847</td>
<td align="right">0.7%</td>
<td align="right">88.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">365,444</td>
<td align="right">0.7%</td>
<td align="right">88.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">321,993</td>
<td align="right">0.6%</td>
<td align="right">89.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">321,993</td>
<td align="right">0.6%</td>
<td align="right">89.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">319,681</td>
<td align="right">0.6%</td>
<td align="right">90.4%</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">312,335</td>
<td align="right">0.6%</td>
<td align="right">91.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">304,765</td>
<td align="right">0.6%</td>
<td align="right">91.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">261,069</td>
<td align="right">0.5%</td>
<td align="right">92.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">223,696</td>
<td align="right">0.4%</td>
<td align="right">92.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">220,468</td>
<td align="right">0.4%</td>
<td align="right">92.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">202,232</td>
<td align="right">0.4%</td>
<td align="right">93.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">201,315</td>
<td align="right">0.4%</td>
<td align="right">93.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">196,964</td>
<td align="right">0.4%</td>
<td align="right">93.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">196,964</td>
<td align="right">0.4%</td>
<td align="right">94.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">196,964</td>
<td align="right">0.4%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">196,964</td>
<td align="right">0.4%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">185,451</td>
<td align="right">0.3%</td>
<td align="right">95.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">162,795</td>
<td align="right">0.3%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">133,601</td>
<td align="right">0.2%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">133,601</td>
<td align="right">0.2%</td>
<td align="right">96.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">132,440</td>
<td align="right">0.2%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">132,440</td>
<td align="right">0.2%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">125,604</td>
<td align="right">0.2%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">125,019</td>
<td align="right">0.2%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">99,274</td>
<td align="right">0.2%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">98,482</td>
<td align="right">0.2%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">98,482</td>
<td align="right">0.2%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">98,482</td>
<td align="right">0.2%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">98,482</td>
<td align="right">0.2%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">98,482</td>
<td align="right">0.2%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">98,482</td>
<td align="right">0.2%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">98,482</td>
<td align="right">0.2%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">67,446</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">67,446</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">66,332</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">66,332</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">59,171</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">44,517</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">39,780</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">34,632</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">33,166</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">33,166</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">33,166</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">33,166</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">32,283</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">32,283</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">32,283</td>
<td align="right">0.1%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">32,030</td>
<td align="right">0.1%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">32,030</td>
<td align="right">0.1%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">26,395</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">21,938</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">18,236</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">14,453</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">12,487</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">12,487</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">6,614</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">792</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">792</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">669</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">390</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">337</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">337</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">337</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">337</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">253</td>
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
Stats gathered on: 2025-02-24
