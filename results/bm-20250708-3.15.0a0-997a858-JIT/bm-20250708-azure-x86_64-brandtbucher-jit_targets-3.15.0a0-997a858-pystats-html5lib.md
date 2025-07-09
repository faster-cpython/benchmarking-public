
# Pystats results

- benchmark: html5lib
- fork: brandtbucher
- ref: jit-targets
- commit hash: 997a858
- commit date: 2025-07-08T17:21:50-07:00

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
<td align="right">161,894,656</td>
<td align="right">21.2%</td>
<td align="right">21.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">84,116,842</td>
<td align="right">11.0%</td>
<td align="right">32.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">55,329,302</td>
<td align="right">7.2%</td>
<td align="right">39.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">49,904,104</td>
<td align="right">6.5%</td>
<td align="right">46.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42,914,446</td>
<td align="right">5.6%</td>
<td align="right">51.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">23,576,953</td>
<td align="right">3.1%</td>
<td align="right">54.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,851,329</td>
<td align="right">3.0%</td>
<td align="right">57.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">15,666,561</td>
<td align="right">2.1%</td>
<td align="right">59.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">14,592,205</td>
<td align="right">1.9%</td>
<td align="right">61.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,112,642</td>
<td align="right">1.8%</td>
<td align="right">63.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">14,084,318</td>
<td align="right">1.8%</td>
<td align="right">65.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,418,503</td>
<td align="right">1.8%</td>
<td align="right">67.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,588,565</td>
<td align="right">1.6%</td>
<td align="right">68.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,106,621</td>
<td align="right">1.6%</td>
<td align="right">70.4%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,567,799</td>
<td align="right">1.5%</td>
<td align="right">71.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">11,413,845</td>
<td align="right">1.5%</td>
<td align="right">73.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,741,235</td>
<td align="right">1.4%</td>
<td align="right">74.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,336,582</td>
<td align="right">1.4%</td>
<td align="right">76.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,317,196</td>
<td align="right">1.4%</td>
<td align="right">77.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,868,336</td>
<td align="right">1.2%</td>
<td align="right">78.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,136,029</td>
<td align="right">1.1%</td>
<td align="right">79.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">8,055,262</td>
<td align="right">1.1%</td>
<td align="right">80.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,876,642</td>
<td align="right">0.9%</td>
<td align="right">81.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,791,769</td>
<td align="right">0.9%</td>
<td align="right">82.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,658,813</td>
<td align="right">0.9%</td>
<td align="right">83.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,554,089</td>
<td align="right">0.9%</td>
<td align="right">84.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">6,442,168</td>
<td align="right">0.8%</td>
<td align="right">85.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,089,805</td>
<td align="right">0.8%</td>
<td align="right">85.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">5,595,545</td>
<td align="right">0.7%</td>
<td align="right">86.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,433,450</td>
<td align="right">0.7%</td>
<td align="right">87.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,382,654</td>
<td align="right">0.7%</td>
<td align="right">88.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">5,270,967</td>
<td align="right">0.7%</td>
<td align="right">88.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,093,382</td>
<td align="right">0.7%</td>
<td align="right">89.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,906,919</td>
<td align="right">0.5%</td>
<td align="right">89.9%</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,837,043</td>
<td align="right">0.5%</td>
<td align="right">90.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,457,897</td>
<td align="right">0.5%</td>
<td align="right">90.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,372,103</td>
<td align="right">0.4%</td>
<td align="right">91.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,136,654</td>
<td align="right">0.4%</td>
<td align="right">91.7%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,908,966</td>
<td align="right">0.4%</td>
<td align="right">92.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,908,027</td>
<td align="right">0.4%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2,719,978</td>
<td align="right">0.4%</td>
<td align="right">92.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,376,540</td>
<td align="right">0.3%</td>
<td align="right">93.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,292,003</td>
<td align="right">0.3%</td>
<td align="right">93.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,242,053</td>
<td align="right">0.3%</td>
<td align="right">93.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,173,773</td>
<td align="right">0.3%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,832,240</td>
<td align="right">0.2%</td>
<td align="right">94.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,785,928</td>
<td align="right">0.2%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,775,746</td>
<td align="right">0.2%</td>
<td align="right">94.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,754,112</td>
<td align="right">0.2%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,714,157</td>
<td align="right">0.2%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,697,997</td>
<td align="right">0.2%</td>
<td align="right">95.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,697,295</td>
<td align="right">0.2%</td>
<td align="right">95.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,689,137</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,660,231</td>
<td align="right">0.2%</td>
<td align="right">96.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,594,259</td>
<td align="right">0.2%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,580,276</td>
<td align="right">0.2%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,557,557</td>
<td align="right">0.2%</td>
<td align="right">96.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,308,794</td>
<td align="right">0.2%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,243,025</td>
<td align="right">0.2%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,190,071</td>
<td align="right">0.2%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,187,872</td>
<td align="right">0.2%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,134,162</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,131,846</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,084,273</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,080,854</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,080,834</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">992,665</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">966,946</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">912,362</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">781,406</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">761,560</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">758,869</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">726,462</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">721,069</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">701,111</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">696,584</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">696,500</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">595,192</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">496,881</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">432,584</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">404,731</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">403,416</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">398,566</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">390,188</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">355,222</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">353,697</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">351,700</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">351,007</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">350,968</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">348,292</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">139,463</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">96,335</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">59,879</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">59,116</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">46,746</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">40,768</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">34,958</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">21,588</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">18,231</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">14,262</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">13,617</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">12,925</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">12,243</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">12,136</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">11,938</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">11,814</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">9,953</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">9,829</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">9,277</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">9,082</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">7,498</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">6,846</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">6,314</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">4,599</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,104</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,232</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,854</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,274</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,219</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,210</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,009</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">1,008</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">988</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">966</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">965</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">924</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">861</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">861</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">861</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">819</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">817</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">756</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">693</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">672</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">651</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">630</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">627</td>
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
<td align="left">CALL_KW</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">419</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">398</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">336</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">210</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">209</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">208</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">168</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">125</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">21</td>
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
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">65,506,715</td>
<td align="right">8.6%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_BORROW</td>
<td align="right">40,908,949</td>
<td align="right">5.4%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">28,106,066</td>
<td align="right">3.7%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_BORROW</td>
<td align="right">19,931,784</td>
<td align="right">2.6%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_CONST</td>
<td align="right">19,746,291</td>
<td align="right">2.6%</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW</td>
<td align="right">12,876,509</td>
<td align="right">1.7%</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST BINARY_OP_SUBSCR_DICT</td>
<td align="right">12,535,011</td>
<td align="right">1.6%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">12,133,718</td>
<td align="right">1.6%</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">12,054,825</td>
<td align="right">1.6%</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">11,338,041</td>
<td align="right">1.5%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST RETURN_VALUE</td>
<td align="right">10,787,491</td>
<td align="right">1.4%</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR POP_JUMP_IF_FALSE</td>
<td align="right">10,154,445</td>
<td align="right">1.3%</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,690,695</td>
<td align="right">1.3%</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST COMPARE_OP_STR</td>
<td align="right">9,645,619</td>
<td align="right">1.3%</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">8,686,018</td>
<td align="right">1.1%</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">7,557,215</td>
<td align="right">1.0%</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE STORE_FAST</td>
<td align="right">7,196,448</td>
<td align="right">0.9%</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_MODULE</td>
<td align="right">7,150,241</td>
<td align="right">0.9%</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST POP_JUMP_IF_FALSE</td>
<td align="right">6,790,719</td>
<td align="right">0.9%</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS</td>
<td align="right">6,715,730</td>
<td align="right">0.9%</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT LOAD_FAST_BORROW</td>
<td align="right">6,544,038</td>
<td align="right">0.9%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,505,484</td>
<td align="right">0.9%</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE TO_BOOL_LIST</td>
<td align="right">6,446,022</td>
<td align="right">0.8%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW</td>
<td align="right">6,424,471</td>
<td align="right">0.8%</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE TO_BOOL_BOOL</td>
<td align="right">6,327,695</td>
<td align="right">0.8%</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT</td>
<td align="right">6,238,124</td>
<td align="right">0.8%</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW RETURN_VALUE</td>
<td align="right">6,108,693</td>
<td align="right">0.8%</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_CONST</td>
<td align="right">6,088,390</td>
<td align="right">0.8%</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">6,079,334</td>
<td align="right">0.8%</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE TO_BOOL</td>
<td align="right">6,078,539</td>
<td align="right">0.8%</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_SMALL_INT</td>
<td align="right">5,788,917</td>
<td align="right">0.8%</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_OP_ADD_INT</td>
<td align="right">5,570,494</td>
<td align="right">0.7%</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW</td>
<td align="right">5,562,217</td>
<td align="right">0.7%</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,407,713</td>
<td align="right">0.7%</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT STORE_FAST</td>
<td align="right">5,407,461</td>
<td align="right">0.7%</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT LOAD_FAST_BORROW</td>
<td align="right">5,378,607</td>
<td align="right">0.7%</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_SLOT</td>
<td align="right">4,870,237</td>
<td align="right">0.6%</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE CONTAINS_OP_SET</td>
<td align="right">4,831,636</td>
<td align="right">0.6%</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE JUMP_BACKWARD_JIT</td>
<td align="right">4,608,571</td>
<td align="right">0.6%</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_CONST</td>
<td align="right">4,489,558</td>
<td align="right">0.6%</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST BINARY_OP</td>
<td align="right">4,239,793</td>
<td align="right">0.6%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST_BORROW</td>
<td align="right">4,214,379</td>
<td align="right">0.6%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET POP_JUMP_IF_FALSE</td>
<td align="right">4,134,287</td>
<td align="right">0.5%</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT STORE_FAST</td>
<td align="right">4,097,975</td>
<td align="right">0.5%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW COMPARE_OP_INT</td>
<td align="right">3,990,581</td>
<td align="right">0.5%</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST_BORROW</td>
<td align="right">3,921,867</td>
<td align="right">0.5%</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR</td>
<td align="right">3,917,772</td>
<td align="right">0.5%</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS RESUME_CHECK</td>
<td align="right">3,855,016</td>
<td align="right">0.5%</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY RESUME_CHECK</td>
<td align="right">3,837,043</td>
<td align="right">0.5%</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE</td>
<td align="right">3,833,819</td>
<td align="right">0.5%</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,691,604</td>
<td align="right">0.5%</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,666,126</td>
<td align="right">0.5%</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_CONST</td>
<td align="right">3,551,879</td>
<td align="right">0.5%</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_PROPERTY</td>
<td align="right">3,418,204</td>
<td align="right">0.4%</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">3,328,250</td>
<td align="right">0.4%</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_CONST</td>
<td align="right">3,301,621</td>
<td align="right">0.4%</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD STORE_FAST</td>
<td align="right">3,242,625</td>
<td align="right">0.4%</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_BORROW</td>
<td align="right">3,226,241</td>
<td align="right">0.4%</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_CONST</td>
<td align="right">2,967,863</td>
<td align="right">0.4%</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,940,671</td>
<td align="right">0.4%</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">2,869,014</td>
<td align="right">0.4%</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">2,831,230</td>
<td align="right">0.4%</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT LOAD_CONST</td>
<td align="right">2,785,203</td>
<td align="right">0.4%</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,736,707</td>
<td align="right">0.4%</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST_BORROW</td>
<td align="right">2,659,483</td>
<td align="right">0.3%</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,644,439</td>
<td align="right">0.3%</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_FAST_BORROW</td>
<td align="right">2,560,692</td>
<td align="right">0.3%</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">2,549,804</td>
<td align="right">0.3%</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">2,547,088</td>
<td align="right">0.3%</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,535,104</td>
<td align="right">0.3%</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST STORE_FAST</td>
<td align="right">2,512,130</td>
<td align="right">0.3%</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW TO_BOOL_BOOL</td>
<td align="right">2,476,475</td>
<td align="right">0.3%</td>
<td align="right">70.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_BORROW</td>
<td align="right">2,465,562</td>
<td align="right">0.3%</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE CALL_PY_EXACT_ARGS</td>
<td align="right">2,426,665</td>
<td align="right">0.3%</td>
<td align="right">71.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_FAST</td>
<td align="right">2,387,973</td>
<td align="right">0.3%</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST</td>
<td align="right">2,365,464</td>
<td align="right">0.3%</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_TRUE</td>
<td align="right">2,326,424</td>
<td align="right">0.3%</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE</td>
<td align="right">2,292,003</td>
<td align="right">0.3%</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,291,940</td>
<td align="right">0.3%</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,251,485</td>
<td align="right">0.3%</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">2,212,819</td>
<td align="right">0.3%</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG JUMP_BACKWARD_JIT</td>
<td align="right">2,200,053</td>
<td align="right">0.3%</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_CONST</td>
<td align="right">2,169,839</td>
<td align="right">0.3%</td>
<td align="right">74.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG POP_JUMP_IF_NONE</td>
<td align="right">2,165,125</td>
<td align="right">0.3%</td>
<td align="right">74.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW EXTENDED_ARG</td>
<td align="right">2,165,125</td>
<td align="right">0.3%</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE JUMP_FORWARD</td>
<td align="right">2,161,708</td>
<td align="right">0.3%</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT LOAD_GLOBAL_MODULE</td>
<td align="right">2,042,499</td>
<td align="right">0.3%</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,947,656</td>
<td align="right">0.3%</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT LOAD_FAST_BORROW</td>
<td align="right">1,923,859</td>
<td align="right">0.3%</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE CALL_LEN</td>
<td align="right">1,905,389</td>
<td align="right">0.2%</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,872,828</td>
<td align="right">0.2%</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE SWAP</td>
<td align="right">1,860,622</td>
<td align="right">0.2%</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,856,423</td>
<td align="right">0.2%</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST JUMP_FORWARD</td>
<td align="right">1,850,606</td>
<td align="right">0.2%</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">1,807,780</td>
<td align="right">0.2%</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN LOAD_SMALL_INT</td>
<td align="right">1,756,529</td>
<td align="right">0.2%</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,750,815</td>
<td align="right">0.2%</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">IS_OP POP_JUMP_IF_FALSE</td>
<td align="right">1,712,980</td>
<td align="right">0.2%</td>
<td align="right">77.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE IS_OP</td>
<td align="right">1,712,686</td>
<td align="right">0.2%</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,659,624</td>
<td align="right">0.2%</td>
<td align="right">78.2%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">826,750</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">368,336</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">27,920</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">19,935</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">827,666</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">356,875</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">25,131</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">17,976</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">6,416</td>
<td align="right">0.5%</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">592,012</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">498,920</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">356,875</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">221,856</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">96,083</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">856,634</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">811,843</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">98,057</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">15,944</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,450</td>
<td align="right">0.2%</td>
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
<td align="right">396,723</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,047</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">714</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">273</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">125</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,208</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,814</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,680</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,533</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">42</td>
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
<td align="left">JUMP_FORWARD</td>
<td align="right">3,229</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,814</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,680</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,407</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">147</td>
<td align="right">1.6%</td>
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
<td align="right">1,210</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">64</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">376</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">375</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">146</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">125</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">125</td>
<td align="right">10.3%</td>
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
<td align="right">819</td>
<td align="right">95.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">42</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">861</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">42</td>
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
<td align="right">42</td>
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
<td align="right">125</td>
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
<td align="right">125</td>
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
<td align="right">350,968</td>
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
<td align="right">350,968</td>
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
<td align="right">696,500</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
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
<td align="left">BUILD_STRING</td>
<td align="right">348,292</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">348,292</td>
<td align="right">50.0%</td>
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
<td align="right">398,336</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">125</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">105</td>
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
<td align="left">STORE_FAST</td>
<td align="right">462</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">168</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">21</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">21</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">672</td>
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
<td align="right">777</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">210</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">21</td>
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
<td align="left">STORE_DEREF</td>
<td align="right">672</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">336</td>
<td align="right">33.3%</td>
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
<td align="right">7,498</td>
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
<td align="right">6,195</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">988</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">273</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42</td>
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
<td align="left">STORE_FAST</td>
<td align="right">894,992</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">859,606</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">23,730</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">23,688</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">20,592</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">863,319</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">860,754</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">79,607</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">23,688</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,521</td>
<td align="right">0.1%</td>
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
<td align="right">12,925</td>
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
<td align="right">12,925</td>
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
<td align="right">273</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">273</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">168</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">105</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21</td>
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
<td align="left">JUMP_FORWARD</td>
<td align="right">273</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">273</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">210</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">84</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">21</td>
<td align="right">2.4%</td>
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
<td align="right">679,616</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">194,846</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">86,371</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">3,932</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,014</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">360,106</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">326,965</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">265,260</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,096</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">966</td>
<td align="right">0.1%</td>
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
<td align="right">3,328,250</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,344,982</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,080,813</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">819,587</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">459,732</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">2,967,863</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,659,483</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">994,734</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">819,587</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">349,000</td>
<td align="right">4.3%</td>
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
<td align="right">462</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">273</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">84</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">42</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">798</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">63</td>
<td align="right">7.3%</td>
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
<td align="right">770,945</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,875</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,431</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,717</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">878</td>
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
<td align="right">712,526</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">22,049</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">20,262</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">15,330</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,463</td>
<td align="right">1.1%</td>
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
<td align="left">CACHE</td>
<td align="right">125</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">84</td>
<td align="right">40.2%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">125</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">84</td>
<td align="right">40.2%</td>
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
<td align="right">10,787,491</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,108,693</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,833,819</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">859,254</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">683,217</td>
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
<td align="right">7,557,215</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,327,695</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,328,250</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,161,708</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">683,217</td>
<td align="right">3.0%</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">23,436</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21,504</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">672</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">441</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">378</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">19,362</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">11,970</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">11,634</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,394</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">504</td>
<td align="right">1.1%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,078,539</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">352,098</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,167</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,821</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,834</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">6,079,334</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">358,186</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,821</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,407</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">252</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">168</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">168</td>
<td align="right">100.0%</td>
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
<td align="right">189</td>
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
<td align="right">189</td>
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
<td align="right">378</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">273</td>
<td align="right">41.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">378</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">273</td>
<td align="right">41.9%</td>
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
<td align="right">4,239,793</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">499,151</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">410,987</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">218,524</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,114</td>
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
<td align="left">JUMP_FORWARD</td>
<td align="right">1,080,875</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">944,546</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">930,678</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">498,920</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">414,831</td>
<td align="right">7.7%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">1,208,317</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">992,027</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">698,937</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,875</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,056</td>
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
<td align="right">999,113</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">881,917</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">700,339</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">224,833</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">100,500</td>
<td align="right">3.5%</td>
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
<td align="right">682,146</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">396,645</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">100,500</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,708</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,960</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">688,985</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">398,914</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">101,126</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">357</td>
<td align="right">0.0%</td>
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
<td align="right">595,192</td>
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
<td align="left">BINARY_OP</td>
<td align="right">499,151</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">96,041</td>
<td align="right">16.1%</td>
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
<td align="right">348,292</td>
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
<td align="right">348,292</td>
<td align="right">100.0%</td>
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
<td align="right">870,075</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">496,772</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">348,583</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">17,325</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">6,635</td>
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
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">859,106</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">506,220</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">349,757</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">9,030</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">6,635</td>
<td align="right">0.4%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,136</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,129</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,806</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,302</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">924</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,520</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,289</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,491</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,491</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,450</td>
<td align="right">8.0%</td>
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
<td align="right">188</td>
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
<td align="right">188</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">420</td>
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
<td align="right">189</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">126</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">63</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">21</td>
<td align="right">5.0%</td>
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
<td align="right">713,251</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">670,497</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">135,439</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">132,315</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">29,459</td>
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
<td align="right">1,250,342</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">441,301</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,291</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,055</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">882</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">669,583</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">128,032</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">101,376</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,334</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,250</td>
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
<td align="right">803,400</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">105,105</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,429</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">798</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">420</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">696,500</td>
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
<td align="left">FORMAT_SIMPLE</td>
<td align="right">696,500</td>
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
<td align="right">1,455,875</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">980,605</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">476,005</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">259,063</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">145,467</td>
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
<td align="left">COPY</td>
<td align="right">1,455,875</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">980,290</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">475,207</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">399,628</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">29,711</td>
<td align="right">0.9%</td>
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
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">349,020</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">1,047</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">479</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">231</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">125</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">350,251</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">399</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">273</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">84</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,189</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,210</td>
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
<td align="left">BUILD_MAP</td>
<td align="right">21</td>
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
<td align="right">21</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,165,125</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,319,737</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,106,832</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,080,750</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">681,820</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">2,200,053</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,165,125</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,080,833</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">831,538</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">474,722</td>
<td align="right">6.9%</td>
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
<td align="right">811,843</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">177,802</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,638</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,298</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">677,703</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">226,747</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">86,371</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,298</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">168</td>
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
<td align="right">335</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">84</td>
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
<td align="left">STORE_NAME</td>
<td align="right">294</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">125</td>
<td align="right">29.8%</td>
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
<td align="right">398</td>
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
<td align="left">IMPORT_FROM</td>
<td align="right">335</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">63</td>
<td align="right">15.8%</td>
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
<td align="right">1,712,686</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">819</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,712,980</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,113</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">64</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">273</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">189</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">168</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">105</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">84</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">924</td>
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
<td align="left">EXTENDED_ARG</td>
<td align="right">126</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">84</td>
<td align="right">40.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">126</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">84</td>
<td align="right">40.0%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">2,161,708</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,850,606</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,080,875</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">827,520</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">474,722</td>
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
<td align="left">STORE_FAST</td>
<td align="right">3,242,625</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,340,861</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,081,545</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">859,250</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">23,478</td>
<td align="right">0.4%</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">17,976</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,407</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">924</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">693</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">588</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">19,362</td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,554</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">588</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">42</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">21</td>
<td align="right">0.1%</td>
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
<td align="right">167</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">188</td>
<td align="right">100.0%</td>
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
<td align="right">3,917,772</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">493,787</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">399,628</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">259,630</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">13,582</td>
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
<td align="right">3,921,867</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">368,556</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">352,765</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">352,483</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">30,610</td>
<td align="right">0.6%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">19,746,291</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,088,390</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,489,558</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,551,879</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,301,621</td>
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
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">12,535,011</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">10,787,491</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">9,645,619</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,239,793</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,551,879</td>
<td align="right">6.4%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">348,604</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">958</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">672</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">292</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">251</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">349,041</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">689</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">609</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">291</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">210</td>
<td align="right">0.1%</td>
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
<td align="right">2,831,230</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,549,804</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,547,088</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,807,780</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,081,587</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,666,126</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,736,707</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,387,973</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">860,148</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">859,254</td>
<td align="right">6.8%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">378</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">189</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">125</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">104</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">21</td>
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
<td align="left">SWAP</td>
<td align="right">692</td>
<td align="right">84.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">125</td>
<td align="right">15.3%</td>
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
<td align="right">40,908,949</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">28,106,066</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">19,931,784</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,876,509</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">6,544,038</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">65,506,715</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">19,746,291</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">11,338,041</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,150,241</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,108,693</td>
<td align="right">3.8%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,644,439</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,251,485</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,750,815</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,081,545</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">876,520</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,990,581</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,872,828</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,078,483</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,076,766</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">870,075</td>
<td align="right">8.1%</td>
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
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,080,750</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,250</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,080,750</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,250</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">42</td>
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
<td align="right">827,750</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">826,729</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">29,232</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,750</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,680</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">855,940</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">829,388</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,750</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">378</td>
<td align="right">0.0%</td>
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
<td align="right">336</td>
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
<td align="right">210</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">126</td>
<td align="right">37.5%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,604</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">966</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">903</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">630</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">587</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,066</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,742</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,575</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">777</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">756</td>
<td align="right">7.6%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">2,562</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,491</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,008</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">672</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">462</td>
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
<td align="left">BUILD_TUPLE</td>
<td align="right">2,562</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,008</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">903</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">756</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">672</td>
<td align="right">9.8%</td>
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
<td align="right">5,788,917</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,756,529</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">930,678</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">264,315</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">31,080</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">5,570,494</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,538,784</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">476,005</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">410,695</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">265,572</td>
<td align="right">3.0%</td>
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
<td align="right">378</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">378</td>
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
<td align="right">378</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">252</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">84</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">42</td>
<td align="right">5.6%</td>
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
<td align="right">126</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">42</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">42</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">21</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">21</td>
<td align="right">16.7%</td>
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
<td align="left">COPY_FREE_VARS</td>
<td align="right">399</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">315</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">273</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">84</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">63</td>
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
<td align="left">RESUME</td>
<td align="right">777</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">315</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">127</td>
<td align="right">10.4%</td>
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
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,687</td>
<td align="right">83.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">315</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">167</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">42</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">21</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">2,854</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">357</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">21</td>
<td align="right">0.6%</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">12,133,718</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,154,445</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">8,686,018</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,790,719</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">4,134,287</td>
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
<td align="right">40,908,949</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,644,439</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,365,464</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,807,780</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,101,549</td>
<td align="right">2.2%</td>
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
<td align="left">EXTENDED_ARG</td>
<td align="right">2,165,125</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,133</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,280</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">416</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,081,587</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,080,750</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,525</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,375</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">651</td>
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
<td align="right">1,515,302</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">860,148</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">461</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,164,124</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">860,417</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">348,565</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,400</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">378</td>
<td align="right">0.0%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">6,079,334</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,869,014</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,326,424</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,221,561</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">441,301</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">4,608,571</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,214,379</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,750,815</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,080,750</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,028,190</td>
<td align="right">7.3%</td>
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
<td align="right">988</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">21</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">399</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">315</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">148</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">84</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">21</td>
<td align="right">2.1%</td>
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
<td align="left">SWAP</td>
<td align="right">399,961</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">354,459</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">230,750</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">137,646</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,750</td>
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
<td align="right">724,154</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">402,622</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,528</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,054</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">502</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_LOCALS</td>
<td align="right">672</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">189</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">43</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">21</td>
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
<td align="right">462</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">232</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">168</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">84</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21</td>
<td align="right">2.1%</td>
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
<td align="right">7,557,215</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,196,448</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,407,461</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">4,097,975</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,242,625</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">28,106,066</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,831,230</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,251,485</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,169,839</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,850,606</td>
<td align="right">4.3%</td>
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
<td align="left">COPY</td>
<td align="right">10,750</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">798</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">588</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,916</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">4,750</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">798</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">588</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">84</td>
<td align="right">0.7%</td>
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
<td align="right">756,070</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,104</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">630</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">483</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">713,845</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">23,730</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,771</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">7,759</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">4,554</td>
<td align="right">0.6%</td>
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
<td align="right">6,195</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,079</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,491</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">672</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">672</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">8,610</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,491</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">819</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">777</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">210</td>
<td align="right">1.7%</td>
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
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">1,860,622</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,456,337</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">132,042</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">3,729</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,813</td>
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
<td align="right">1,456,337</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">980,290</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">475,207</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">399,961</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">132,126</td>
<td align="right">3.8%</td>
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
<td align="right">168</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">63</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">42</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">42</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">210</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">210</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">21</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,080,729</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">84</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,080,729</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">105</td>
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
<td align="right">1,491</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">840</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">777</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">714</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">378</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,541</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">672</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">630</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">252</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">147</td>
<td align="right">3.2%</td>
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
<td align="right">5,570,494</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">21,504</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">336</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">5,378,607</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">140,147</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">29,232</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">27,920</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">12,054</td>
<td align="right">0.2%</td>
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
<td align="right">1,396,537</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">592,707</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">462,207</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">266,000</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,708</td>
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
<td align="right">1,860,622</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">462,207</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">396,645</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">168</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">6,375</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,032</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">609</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">273</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">273</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">6,333</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,528</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">609</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">441</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">315</td>
<td align="right">2.7%</td>
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
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">336</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">210</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">84</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">336</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">105</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">105</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">84</td>
<td align="right">13.3%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">12,535,011</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,189,071</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">980,290</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">859,106</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">100,458</td>
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
<td align="left">STORE_FAST</td>
<td align="right">4,097,975</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,785,203</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,042,499</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,923,859</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,361,666</td>
<td align="right">8.7%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,546</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,008</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">63</td>
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
<td align="right">13,617</td>
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
<td align="left">COPY</td>
<td align="right">475,207</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">240,691</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">10,102</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">273</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">479,395</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">232,541</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,416</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,229</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,415</td>
<td align="right">0.3%</td>
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
<td align="left">BUILD_SLICE</td>
<td align="right">96,041</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">252</td>
<td align="right">0.3%</td>
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
<td align="left">GET_ITER</td>
<td align="right">96,083</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">252</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,407,713</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">19,698</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,708</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">609</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">5,407,461</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">19,509</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,729</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">609</td>
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
<td align="right">59,585</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">294</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">19,698</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,327</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,306</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,138</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,008</td>
<td align="right">1.7%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">21</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
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
<td align="left">STORE_FAST</td>
<td align="right">42</td>
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
<td align="right">410,695</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">18,774</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,708</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,050</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">273</td>
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
<td align="right">407,607</td>
<td align="right">94.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">18,728</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,729</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,050</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">798</td>
<td align="right">0.2%</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">348,250</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,833</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">984</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">458</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">273</td>
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
<td align="left">COPY_FREE_VARS</td>
<td align="right">349,020</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,687</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,948</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">42</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,940,671</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">879,866</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">51,042</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">20,262</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,049</td>
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
<td align="right">3,855,016</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">51,063</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">840</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">588,666</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">349,720</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">214,625</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">19,383</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">12,054</td>
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
<td align="left">GET_ITER</td>
<td align="right">592,012</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">360,554</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">214,458</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">17,976</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,407</td>
<td align="right">0.1%</td>
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
<td align="right">488,877</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,897</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,729</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">397</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">375</td>
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
<td align="right">492,437</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,708</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">626</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">626</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">354</td>
<td align="right">0.1%</td>
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
<td align="right">8,023</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,260</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">273</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">126</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">84</td>
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
<td align="left">STORE_FAST</td>
<td align="right">7,981</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">630</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">630</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">525</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">42</td>
<td align="right">0.4%</td>
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
<td align="right">26,124</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">6,027</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,730</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,708</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,365</td>
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
<td align="left">POP_TOP</td>
<td align="right">18,900</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">17,325</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,729</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,386</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,386</td>
<td align="right">3.4%</td>
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
<td align="right">836,962</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">715,390</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,318</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">819</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">546</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,556,382</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">273</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">104</td>
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
<td align="right">125</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">21</td>
<td align="right">14.4%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">146</td>
<td align="right">100.0%</td>
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
<td align="right">389,999</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">390,188</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,905,389</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">985,976</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,291</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,291</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,708</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,756,529</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">399,250</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">366,776</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">355,235</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,244</td>
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
<td align="left">BINARY_SLICE</td>
<td align="right">827,666</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">701,212</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">224,833</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,124</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">9,030</td>
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
<td align="right">923,606</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">826,729</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">21,881</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,333</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">979</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,178,412</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">361,957</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">150,914</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,916</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,022</td>
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
<td align="right">1,557,811</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">96,021</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">16,458</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,750</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">8,124</td>
<td align="right">0.5%</td>
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
<td align="right">4,333</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,708</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">189</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">84</td>
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
<td align="right">3,646</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,708</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">375</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">375</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">189</td>
<td align="right">3.0%</td>
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
<td align="right">1,659,624</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">357</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">1,080,729</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">348,229</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">221,856</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,062</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">3,999</td>
<td align="right">0.2%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">905,749</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">858,833</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">827,751</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">398,914</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">131,958</td>
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
<td align="left">POP_TOP</td>
<td align="right">1,344,982</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">905,812</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">859,043</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,416</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">5,042</td>
<td align="right">0.2%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,214,624</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">348,583</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">13,153</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">897</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">672</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">861,152</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">350,595</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">349,209</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">18,899</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">168</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,715,730</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,426,665</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,212,819</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">475,375</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">132,041</td>
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
<td align="right">12,054,825</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">51,042</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">231</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">84</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">490,894</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">414,207</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">404,212</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">263,916</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">19,415</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,593,737</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">43</td>
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
<td align="right">126</td>
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
<td align="right">84</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">42</td>
<td align="right">33.3%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">356</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">166</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">63</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">42</td>
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
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">273</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">104</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">104</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">83</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">42</td>
<td align="right">6.7%</td>
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
<td align="right">546</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">273</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">83</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">42</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">21</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">273</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">273</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">273</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">83</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">42</td>
<td align="right">4.4%</td>
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
<td align="right">42</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,238,124</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,990,581</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,538,784</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,361,666</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,090,696</td>
<td align="right">7.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">12,133,718</td>
<td align="right">83.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,326,424</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">131,979</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">9,645,619</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,094,966</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">394,581</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">139,979</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">102,105</td>
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
<td align="right">10,154,445</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,221,561</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">29,354</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,132</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,062</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">681,166</td>
<td align="right">94.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">21,587</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">17,416</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">357</td>
<td align="right">0.0%</td>
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
<td align="right">717,337</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,229</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">357</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">104</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42</td>
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
<td align="right">4,831,636</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">218,711</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">214,458</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">5,196</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">798</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">4,134,287</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">681,820</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">236,084</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">218,524</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">252</td>
<td align="right">0.0%</td>
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
<td align="left">EXTENDED_ARG</td>
<td align="right">1,080,833</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,080,729</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">104</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">21</td>
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
<td align="right">856,634</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">152,374</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">122,418</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">POP_ITER</td>
<td align="right">679,616</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">419,272</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">28,812</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,083</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">63</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">43,130</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">15,944</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">STORE_FAST</td>
<td align="right">55,184</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">3,932</td>
<td align="right">6.7%</td>
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
<td align="right">10,035</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,450</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">630</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">147</td>
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
<td align="right">10,181</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,014</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,458</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">588</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">21</td>
<td align="right">0.1%</td>
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
<td align="right">4,608,571</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,200,053</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">994,775</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">90,504</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">86,099</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,544,038</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,106,832</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">177,802</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">152,374</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">43,130</td>
<td align="right">0.5%</td>
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
<td align="left">LIST_APPEND</td>
<td align="right">588</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">126</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">126</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">126</td>
<td align="right">13.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">630</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">252</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">84</td>
<td align="right">8.7%</td>
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
<td align="right">138,713</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">291</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">291</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">138,901</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">562</td>
<td align="right">0.4%</td>
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
<td align="right">819</td>
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
<td align="right">273</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">273</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">273</td>
<td align="right">33.3%</td>
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
<td align="right">65,506,715</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,690,695</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,666,126</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,535,104</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,872,828</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,876,509</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,690,695</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,196,448</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,505,484</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,446,022</td>
<td align="right">7.7%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">5,958</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,290</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">624</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">210</td>
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
<td align="right">8,291</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">520</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">208</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">42</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">21</td>
<td align="right">0.2%</td>
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
<td align="right">3,691,604</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,736,707</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,856,423</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">909,914</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">880,041</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,226,241</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,547,088</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,659,624</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,178,412</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">907,553</td>
<td align="right">8.8%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,505,484</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,947,656</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,512,553</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">348,188</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,458</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,715,730</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,465,562</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">734,748</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">368,374</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">29,875</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">349,041</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,240</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">524</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">292</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">83</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">349,440</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,431</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">772</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">672</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">378</td>
<td align="right">0.1%</td>
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
<td align="right">1,833</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">21</td>
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
<td align="right">1,854</td>
<td align="right">100.0%</td>
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
<td align="right">3,418,204</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">414,831</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,124</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">629</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">3,837,043</td>
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
<td align="right">4,870,237</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,078,483</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">132,000</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,916</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,562</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">2,535,104</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,947,656</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">812,189</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">681,166</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">102,703</td>
<td align="right">1.7%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,293,707</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,101,549</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,028,190</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">947,502</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">910,809</td>
<td align="right">13.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">5,562,217</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">715,390</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">215,565</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">138,713</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">11,638</td>
<td align="right">0.2%</td>
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
<td align="right">7,150,241</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">2,042,499</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,080,785</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">907,553</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">863,319</td>
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
<td align="left">CONTAINS_OP_SET</td>
<td align="right">4,831,636</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,301,621</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,712,686</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">905,749</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">879,767</td>
<td align="right">6.2%</td>
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
<td align="right">166</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">42</td>
<td align="right">20.2%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">208</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">167</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">21</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">84</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">83</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">21</td>
<td align="right">11.2%</td>
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
<td align="right">12,054,825</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,855,016</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,837,043</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,593,737</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,080,729</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">19,931,784</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,080,813</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">910,809</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">859,606</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">400,766</td>
<td align="right">1.7%</td>
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
<td align="right">11,338,041</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,076,766</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">855,940</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">102,703</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">31,213</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,424,471</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,489,558</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">827,520</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">698,937</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">362,817</td>
<td align="right">2.7%</td>
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
<td align="right">5,915</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">5,708</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">168</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">147</td>
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
<td align="left">BUILD_MAP</td>
<td align="right">5,708</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,062</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,854</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">168</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">104</td>
<td align="right">0.9%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">1,029,539</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">980,290</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">231,132</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">378</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,032,162</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">980,124</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">136,933</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">86,099</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,189</td>
<td align="right">0.3%</td>
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
<td align="left">SWAP</td>
<td align="right">475,207</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">224,833</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">861</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">105</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">475,669</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">224,854</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">525</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">63</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,291,940</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">42</td>
<td align="right">0.0%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,292,003</td>
<td align="right">100.0%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">6,327,695</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,476,475</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,556,382</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">680,791</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">267,439</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,686,018</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,869,014</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">12,767</td>
<td align="right">0.1%</td>
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
<td align="right">399,250</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">3,528</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,680</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">210</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">400,447</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,906</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">378</td>
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
<td align="right">6,446,022</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">332,708</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,955</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">6,790,719</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">777</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">273</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">368,556</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">30,464</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,666</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">478</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">252</td>
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
<td align="right">368,910</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">33,986</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">478</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">42</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">30,610</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,127</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,092</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">588</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">478</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">34,144</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">478</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">336</td>
<td align="right">1.0%</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,083</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,104</td>
<td align="right">100.0%</td>
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
<td align="right">336</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">273</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">84</td>
<td align="right">12.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">483</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">210</td>
<td align="right">30.3%</td>
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
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">488,208</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">226,747</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">28,812</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,708</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,807</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">756,070</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,854</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">945</td>
<td align="right">0.1%</td>
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
<td align="right">994,734</td>
<td align="right">76.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">165,157</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">136,933</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">11,970</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">994,775</td>
<td align="right">76.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">194,846</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">106,248</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">12,925</td>
<td align="right">1.0%</td>
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
<td align="right">5,370,655</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">31,458,849</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">33,430</td>
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
<td align="right">4,704</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,904</td>
<td align="right">62.7%</td>
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
<td align="right">4,967</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">1,089</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">714</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">252</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">252</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">147</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">126</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">84</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">84</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">84</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">63</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">21</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">21</td>
<td align="right">0.3%</td>
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
<td align="right">1,243,025</td>
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
<td align="right">5,600,754</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,057,160</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,697,689</td>
<td align="right">16.4%</td>
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
<td align="right">115,166</td>
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
<td align="right">210</td>
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
<td align="right">210</td>
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
<td align="right">1,691,769</td>
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
<td align="right">25,990,754</td>
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
<td align="right">15,338</td>
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
<td align="right">2,937</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,582</td>
<td align="right">54.9%</td>
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
<td align="right">1,528</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">734</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">524</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">398</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">251</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">126</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">21</td>
<td align="right">0.6%</td>
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
<td align="right">908,967</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,674,866</td>
<td align="right">88.0%</td>
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
<td align="right">966</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,429</td>
<td align="right">71.5%</td>
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
<td align="right">1,234</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">985</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">168</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">42</td>
<td align="right">1.7%</td>
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
<td align="right">990,989</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,285,826</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">252</td>
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
<td align="right">378</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,298</td>
<td align="right">77.4%</td>
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
<td align="left">reversed list</td>
<td align="right">565</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">481</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">168</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">63</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">21</td>
<td align="right">1.6%</td>
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
<td align="left">list</td>
<td align="right">954,440</td>
<td align="right">954,440 / 0 !!</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">588,750</td>
<td align="right">588,750 / 0 !!</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">238,721</td>
<td align="right">238,721 / 0 !!</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,639</td>
<td align="right">3,639 / 0 !!</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">273</td>
<td align="right">273 / 0 !!</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">84</td>
<td align="right">84 / 0 !!</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">5,068,964</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">42</td>
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
<td align="right">117,550,594</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">26,654</td>
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
<td align="right">15,767</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,630</td>
<td align="right">35.4%</td>
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
<td align="right">5,426</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,403</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">545</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">482</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">42</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">42</td>
<td align="right">0.5%</td>
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
<td align="right">5,145</td>
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
<td align="right">20,770,330</td>
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
<td align="right">1,125</td>
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
<td align="right">4,808</td>
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
<td align="right">63</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">396</td>
<td align="right">75.9%</td>
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
<td align="right">63</td>
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
<td align="right">1,128,433</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,410,246</td>
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
<td align="right">20,195</td>
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
<td align="right">3,969</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,054</td>
<td align="right">34.1%</td>
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
<td align="right">1,091</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">544</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">377</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">42</td>
<td align="right">2.0%</td>
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
<td align="right">46,116</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,944,965</td>
<td align="right">98.4%</td>
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
<td align="right">483</td>
<td align="right">76.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">147</td>
<td align="right">23.3%</td>
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
<td align="left">bytearray int</td>
<td align="right">126</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">21</td>
<td align="right">14.3%</td>
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
<td align="right">6,437,541</td>
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
<td align="right">20,527,429</td>
<td align="right">76.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">54,245</td>
<td align="right">0.2%</td>
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
<td align="right">2,804</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,821</td>
<td align="right">50.2%</td>
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
<td align="right">1,544</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">606</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">356</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">210</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">105</td>
<td align="right">3.7%</td>
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
<td align="right">765,467</td>
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
<td align="right">433,081,340</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">24,760,281</td>
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
<td align="right">299,853,046</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">5,849,219</td>
<td align="right">0.8%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">6,437,541</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,600,754</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,370,655</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,068,964</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,691,769</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,243,025</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,128,433</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">990,989</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">908,967</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">46,116</td>
<td align="right">0.2%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,709,157</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,708,174</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">269,042</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">33,010</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">28,369</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">25,460</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">15,338</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">12,886</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">10,916</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,279</td>
<td align="right">0.2%</td>
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
<td align="right">398,987</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">23,182,774</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">398,987</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">398,798</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">398,084</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">17,063</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">334</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">350,717</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">1,596</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">22,851,686</td>
<td align="right">96.9%</td>
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
<td align="right">23,463,100</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">23,458,822</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,147,802</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,919,506</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">219,021</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">9,275</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">9,780,895</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">364,935</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">191,035,367</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">225,890,871</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">65,742,832</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">56,519,281</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,253,661</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">2,846,646</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">72,846,062</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">55,312,829</td>
<td align="right">16.2%</td>
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
<td align="right">7,101,842</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">12,949</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">13,882</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">901,086</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">3,149</td>
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
<td align="right">1,042</td>
<td align="right">302,694</td>
<td align="right">20,751,445</td>
<td align="right">1,794,276</td>
<td align="right">1,405,353</td>
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
<td align="right">2,126</td>
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
<td align="right">84</td>
<td align="right">4.0%</td>
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
<td align="right">42</td>
<td align="right">2.0%</td>
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

A potential trace is abandoned because it is too short.
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
<td align="right">2,000</td>
<td align="right">94.1%</td>
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
<td align="right">1,308,837</td>
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
<td align="right">89,011,475</td>
<td align="right">6,800.8%</td>
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
<td align="right">84</td>
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
<td align="right">84</td>
<td align="right">100.0%</td>
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
<td align="right">688,128</td>
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
<td align="right">510,279</td>
<td align="right">74.2%</td>
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
<td align="right">15,288</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">162,477</td>
<td align="right">23.6%</td>
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
<td align="left">21</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">42</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">21</td>
<td align="right">25.0%</td>
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
<td align="left"><= 32</td>
<td align="right">21</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">42</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21</td>
<td align="right">25.0%</td>
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
<td align="left"><= 32</td>
<td align="right">42</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">42</td>
<td align="right">50.0%</td>
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
<td align="right">17,584,084</td>
<td align="right">19.8%</td>
<td align="right">19.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">13,842,148</td>
<td align="right">15.6%</td>
<td align="right">35.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">5,444,416</td>
<td align="right">6.1%</td>
<td align="right">41.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">4,449,661</td>
<td align="right">5.0%</td>
<td align="right">46.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">3,941,047</td>
<td align="right">4.4%</td>
<td align="right">50.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">3,140,824</td>
<td align="right">3.5%</td>
<td align="right">54.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,070,896</td>
<td align="right">3.5%</td>
<td align="right">57.8%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">2,574,432</td>
<td align="right">2.9%</td>
<td align="right">60.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">2,574,432</td>
<td align="right">2.9%</td>
<td align="right">63.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,564,263</td>
<td align="right">2.9%</td>
<td align="right">66.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,562,462</td>
<td align="right">2.9%</td>
<td align="right">69.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">2,562,462</td>
<td align="right">2.9%</td>
<td align="right">72.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,562,462</td>
<td align="right">2.9%</td>
<td align="right">75.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">2,562,462</td>
<td align="right">2.9%</td>
<td align="right">78.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,373,340</td>
<td align="right">2.7%</td>
<td align="right">80.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,373,340</td>
<td align="right">2.7%</td>
<td align="right">83.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">1,690,510</td>
<td align="right">1.9%</td>
<td align="right">85.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,378,585</td>
<td align="right">1.5%</td>
<td align="right">86.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">1,308,837</td>
<td align="right">1.5%</td>
<td align="right">88.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">1,308,837</td>
<td align="right">1.5%</td>
<td align="right">89.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">994,755</td>
<td align="right">1.1%</td>
<td align="right">90.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">994,755</td>
<td align="right">1.1%</td>
<td align="right">92.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">834,469</td>
<td align="right">0.9%</td>
<td align="right">92.9%</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">697,556</td>
<td align="right">0.8%</td>
<td align="right">93.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">695,755</td>
<td align="right">0.8%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">695,755</td>
<td align="right">0.8%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">695,755</td>
<td align="right">0.8%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">684,631</td>
<td align="right">0.8%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">684,631</td>
<td align="right">0.8%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">682,830</td>
<td align="right">0.8%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">682,830</td>
<td align="right">0.8%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">682,830</td>
<td align="right">0.8%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">46,005</td>
<td align="right">0.1%</td>
<td align="right">99.9%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">46,005</td>
<td align="right">0.1%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,801</td>
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
