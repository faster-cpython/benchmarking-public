
# Pystats results

- benchmark: all
- fork: faster-cpython
- ref: dynamic-underflow
- commit hash: 6f75dbe
- commit date: 2024-05-04T12:15:01+01:00

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
<td align="right">12,679,411,371</td>
<td align="right">17.8%</td>
<td align="right">17.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,764,819,592</td>
<td align="right">6.7%</td>
<td align="right">24.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,441,281,356</td>
<td align="right">4.8%</td>
<td align="right">29.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,132,345,237</td>
<td align="right">4.4%</td>
<td align="right">33.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,715,870,673</td>
<td align="right">3.8%</td>
<td align="right">37.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,516,379,116</td>
<td align="right">3.5%</td>
<td align="right">41.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,500,848,324</td>
<td align="right">3.5%</td>
<td align="right">44.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,419,399,542</td>
<td align="right">3.4%</td>
<td align="right">48.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,205,780,232</td>
<td align="right">3.1%</td>
<td align="right">51.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,105,585,936</td>
<td align="right">3.0%</td>
<td align="right">54.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,952,491,772</td>
<td align="right">2.7%</td>
<td align="right">56.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,859,375,767</td>
<td align="right">2.6%</td>
<td align="right">59.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,542,061,498</td>
<td align="right">2.2%</td>
<td align="right">61.6%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,459,694,882</td>
<td align="right">2.1%</td>
<td align="right">63.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,418,379,717</td>
<td align="right">2.0%</td>
<td align="right">65.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,285,740,919</td>
<td align="right">1.8%</td>
<td align="right">67.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,068,366,853</td>
<td align="right">1.5%</td>
<td align="right">68.9%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,061,888,010</td>
<td align="right">1.5%</td>
<td align="right">70.4%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">911,763,324</td>
<td align="right">1.3%</td>
<td align="right">71.7%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">890,547,363</td>
<td align="right">1.3%</td>
<td align="right">72.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">788,342,701</td>
<td align="right">1.1%</td>
<td align="right">74.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,895,053</td>
<td align="right">1.1%</td>
<td align="right">75.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">736,329,701</td>
<td align="right">1.0%</td>
<td align="right">76.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">685,391,683</td>
<td align="right">1.0%</td>
<td align="right">77.2%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">616,883,109</td>
<td align="right">0.9%</td>
<td align="right">78.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">582,006,266</td>
<td align="right">0.8%</td>
<td align="right">78.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">556,311,842</td>
<td align="right">0.8%</td>
<td align="right">79.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">469,274,482</td>
<td align="right">0.7%</td>
<td align="right">80.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">466,296,281</td>
<td align="right">0.7%</td>
<td align="right">80.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">446,100,692</td>
<td align="right">0.6%</td>
<td align="right">81.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">404,099,284</td>
<td align="right">0.6%</td>
<td align="right">82.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">391,311,119</td>
<td align="right">0.5%</td>
<td align="right">82.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">375,108,668</td>
<td align="right">0.5%</td>
<td align="right">83.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">369,224,427</td>
<td align="right">0.5%</td>
<td align="right">83.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">355,945,350</td>
<td align="right">0.5%</td>
<td align="right">84.2%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">350,629,397</td>
<td align="right">0.5%</td>
<td align="right">84.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">301,496,004</td>
<td align="right">0.4%</td>
<td align="right">85.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">296,484,241</td>
<td align="right">0.4%</td>
<td align="right">85.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">283,143,751</td>
<td align="right">0.4%</td>
<td align="right">86.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">278,070,313</td>
<td align="right">0.4%</td>
<td align="right">86.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">276,256,267</td>
<td align="right">0.4%</td>
<td align="right">86.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">273,430,618</td>
<td align="right">0.4%</td>
<td align="right">87.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">251,190,860</td>
<td align="right">0.4%</td>
<td align="right">87.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">250,449,071</td>
<td align="right">0.4%</td>
<td align="right">87.8%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">248,521,252</td>
<td align="right">0.3%</td>
<td align="right">88.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">246,831,984</td>
<td align="right">0.3%</td>
<td align="right">88.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">242,773,463</td>
<td align="right">0.3%</td>
<td align="right">88.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">238,936,933</td>
<td align="right">0.3%</td>
<td align="right">89.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">231,418,870</td>
<td align="right">0.3%</td>
<td align="right">89.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">230,422,003</td>
<td align="right">0.3%</td>
<td align="right">89.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">228,717,573</td>
<td align="right">0.3%</td>
<td align="right">90.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">227,743,331</td>
<td align="right">0.3%</td>
<td align="right">90.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">223,443,555</td>
<td align="right">0.3%</td>
<td align="right">90.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">209,228,683</td>
<td align="right">0.3%</td>
<td align="right">91.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">200,348,044</td>
<td align="right">0.3%</td>
<td align="right">91.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">199,339,184</td>
<td align="right">0.3%</td>
<td align="right">91.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">194,650,262</td>
<td align="right">0.3%</td>
<td align="right">91.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">191,868,655</td>
<td align="right">0.3%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">191,048,682</td>
<td align="right">0.3%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">188,850,351</td>
<td align="right">0.3%</td>
<td align="right">92.7%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">178,613,116</td>
<td align="right">0.3%</td>
<td align="right">93.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,848,029</td>
<td align="right">0.2%</td>
<td align="right">93.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">154,248,557</td>
<td align="right">0.2%</td>
<td align="right">93.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">154,023,635</td>
<td align="right">0.2%</td>
<td align="right">93.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">152,359,948</td>
<td align="right">0.2%</td>
<td align="right">93.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">149,415,330</td>
<td align="right">0.2%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">145,735,336</td>
<td align="right">0.2%</td>
<td align="right">94.3%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">144,865,101</td>
<td align="right">0.2%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">140,463,601</td>
<td align="right">0.2%</td>
<td align="right">94.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">140,367,788</td>
<td align="right">0.2%</td>
<td align="right">94.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">139,647,078</td>
<td align="right">0.2%</td>
<td align="right">95.1%</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">137,767,862</td>
<td align="right">0.2%</td>
<td align="right">95.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">137,450,697</td>
<td align="right">0.2%</td>
<td align="right">95.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">127,400,632</td>
<td align="right">0.2%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">115,661,862</td>
<td align="right">0.2%</td>
<td align="right">95.8%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">110,568,603</td>
<td align="right">0.2%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">101,538,676</td>
<td align="right">0.1%</td>
<td align="right">96.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">97,559,572</td>
<td align="right">0.1%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">92,742,051</td>
<td align="right">0.1%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">92,675,801</td>
<td align="right">0.1%</td>
<td align="right">96.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">91,122,464</td>
<td align="right">0.1%</td>
<td align="right">96.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">91,116,204</td>
<td align="right">0.1%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">89,482,276</td>
<td align="right">0.1%</td>
<td align="right">96.9%</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">88,781,794</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">88,388,463</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">78,138,021</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">75,937,219</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">67,804,897</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">64,945,279</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">64,468,160</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">64,197,780</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">63,433,984</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">62,484,749</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">56,777,995</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">55,577,081</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">53,940,757</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">53,535,035</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">52,707,051</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">48,682,743</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">45,911,950</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">44,487,871</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">43,790,042</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">42,871,581</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">42,766,778</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">40,526,177</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">39,058,859</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,240</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,680</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">38,568,148</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">37,811,247</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,187,640</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">34,503,157</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">34,453,224</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">34,117,284</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">33,349,762</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">33,224,654</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">31,162,410</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">28,533,489</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">28,436,330</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">27,298,299</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">26,863,952</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">25,089,844</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">24,440,558</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">21,275,841</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,464,032</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,749,642</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,369,077</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">17,168,667</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">16,802,621</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">14,679,100</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">14,637,435</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">14,300,455</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">12,798,013</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,839,984</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">11,495,072</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">11,385,419</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">8,652,645</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,095,340</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
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
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">7,358,189</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">7,218,733</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">6,901,723</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">6,818,330</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5,721,193</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,202,898</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,470,864</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,197,522</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">3,385,115</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">3,006,046</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">2,885,693</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">2,858,540</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">2,581,986</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">2,453,360</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,269,128</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,263,284</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,112,799</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,032,964</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">1,698,760</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1,337,880</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">642,586</td>
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
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">484,046</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">434,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">278,767</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">258,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
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
<td align="right">238,579</td>
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
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">153,645</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">152,057</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">73,617</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">25,520</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">62.3%</td>
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
<td align="right">19,008</td>
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
<td align="right">2,184,328,155</td>
<td align="right">3.1%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">1,929,735,222</td>
<td align="right">2.7%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">1,886,503,231</td>
<td align="right">2.6%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">1,721,137,468</td>
<td align="right">2.4%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">1,590,517,460</td>
<td align="right">2.2%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST</td>
<td align="right">1,256,333,909</td>
<td align="right">1.8%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">1,221,271,490</td>
<td align="right">1.7%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">1,212,244,615</td>
<td align="right">1.7%</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_SLOT</td>
<td align="right">1,020,181,475</td>
<td align="right">1.4%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">977,022,343</td>
<td align="right">1.4%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">POP_TOP ENTER_EXECUTOR</td>
<td align="right">916,882,639</td>
<td align="right">1.3%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">829,121,400</td>
<td align="right">1.2%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">754,156,835</td>
<td align="right">1.1%</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_FAST</td>
<td align="right">735,230,407</td>
<td align="right">1.0%</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK POP_TOP</td>
<td align="right">702,801,700</td>
<td align="right">1.0%</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">702,530,154</td>
<td align="right">1.0%</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST RETURN_VALUE</td>
<td align="right">649,343,916</td>
<td align="right">0.9%</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT</td>
<td align="right">631,113,590</td>
<td align="right">0.9%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">626,032,084</td>
<td align="right">0.9%</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR INTERPRETER_EXIT</td>
<td align="right">595,900,600</td>
<td align="right">0.8%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST</td>
<td align="right">564,723,982</td>
<td align="right">0.8%</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST INTERPRETER_EXIT</td>
<td align="right">561,096,152</td>
<td align="right">0.8%</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">549,877,585</td>
<td align="right">0.8%</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">539,789,409</td>
<td align="right">0.8%</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT SEND_GEN</td>
<td align="right">530,981,243</td>
<td align="right">0.7%</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN RESUME_CHECK</td>
<td align="right">525,492,676</td>
<td align="right">0.7%</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE YIELD_VALUE</td>
<td align="right">502,551,424</td>
<td align="right">0.7%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">496,697,954</td>
<td align="right">0.7%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST COMPARE_OP_INT</td>
<td align="right">494,732,769</td>
<td align="right">0.7%</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">453,944,247</td>
<td align="right">0.6%</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">453,678,267</td>
<td align="right">0.6%</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS</td>
<td align="right">439,122,175</td>
<td align="right">0.6%</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_SLOT</td>
<td align="right">432,479,432</td>
<td align="right">0.6%</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST POP_TOP</td>
<td align="right">419,583,550</td>
<td align="right">0.6%</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">POP_TOP RESUME_CHECK</td>
<td align="right">411,439,272</td>
<td align="right">0.6%</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">397,177,465</td>
<td align="right">0.6%</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">396,663,048</td>
<td align="right">0.6%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">390,910,698</td>
<td align="right">0.5%</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST</td>
<td align="right">379,661,454</td>
<td align="right">0.5%</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">370,425,264</td>
<td align="right">0.5%</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">362,686,586</td>
<td align="right">0.5%</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">362,085,331</td>
<td align="right">0.5%</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE POP_JUMP_IF_FALSE</td>
<td align="right">344,573,510</td>
<td align="right">0.5%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL</td>
<td align="right">327,818,259</td>
<td align="right">0.5%</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_FAST</td>
<td align="right">319,844,287</td>
<td align="right">0.4%</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">318,700,866</td>
<td align="right">0.4%</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">317,901,722</td>
<td align="right">0.4%</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL STORE_FAST</td>
<td align="right">311,223,597</td>
<td align="right">0.4%</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE RETURN_CONST</td>
<td align="right">300,218,284</td>
<td align="right">0.4%</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">298,663,976</td>
<td align="right">0.4%</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">289,915,733</td>
<td align="right">0.4%</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_LOAD_FAST</td>
<td align="right">279,946,258</td>
<td align="right">0.4%</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_FAST</td>
<td align="right">276,738,907</td>
<td align="right">0.4%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST BINARY_OP_SUBTRACT_INT</td>
<td align="right">267,427,451</td>
<td align="right">0.4%</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST_LOAD_FAST</td>
<td align="right">267,066,628</td>
<td align="right">0.4%</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE</td>
<td align="right">264,330,892</td>
<td align="right">0.4%</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">263,571,765</td>
<td align="right">0.4%</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT RETURN_CONST</td>
<td align="right">253,220,700</td>
<td align="right">0.4%</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">251,899,574</td>
<td align="right">0.4%</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN POP_TOP</td>
<td align="right">247,774,343</td>
<td align="right">0.3%</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE INTERPRETER_EXIT</td>
<td align="right">247,604,283</td>
<td align="right">0.3%</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST SEND_GEN</td>
<td align="right">245,158,196</td>
<td align="right">0.3%</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">POP_TOP RETURN_CONST</td>
<td align="right">239,103,181</td>
<td align="right">0.3%</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">238,891,748</td>
<td align="right">0.3%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST</td>
<td align="right">237,542,296</td>
<td align="right">0.3%</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE CALL_ISINSTANCE</td>
<td align="right">235,669,198</td>
<td align="right">0.3%</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O POP_TOP</td>
<td align="right">232,196,366</td>
<td align="right">0.3%</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">231,035,030</td>
<td align="right">0.3%</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_CONST</td>
<td align="right">229,710,469</td>
<td align="right">0.3%</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">227,745,882</td>
<td align="right">0.3%</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE LOAD_CONST</td>
<td align="right">227,743,331</td>
<td align="right">0.3%</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE</td>
<td align="right">227,560,573</td>
<td align="right">0.3%</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST PUSH_NULL</td>
<td align="right">218,984,290</td>
<td align="right">0.3%</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">217,852,454</td>
<td align="right">0.3%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">216,671,517</td>
<td align="right">0.3%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST</td>
<td align="right">216,175,938</td>
<td align="right">0.3%</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_WITH_HINT</td>
<td align="right">214,354,530</td>
<td align="right">0.3%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST STORE_FAST</td>
<td align="right">212,107,302</td>
<td align="right">0.3%</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BINARY_SUBSCR_LIST_INT</td>
<td align="right">209,710,390</td>
<td align="right">0.3%</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RETURN_GENERATOR</td>
<td align="right">209,475,857</td>
<td align="right">0.3%</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">209,042,665</td>
<td align="right">0.3%</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">206,764,580</td>
<td align="right">0.3%</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR GET_AWAITABLE</td>
<td align="right">206,184,219</td>
<td align="right">0.3%</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT TO_BOOL_NONE</td>
<td align="right">205,705,494</td>
<td align="right">0.3%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT CALL_PY_EXACT_ARGS</td>
<td align="right">205,324,260</td>
<td align="right">0.3%</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">203,099,660</td>
<td align="right">0.3%</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_CONST</td>
<td align="right">198,343,151</td>
<td align="right">0.3%</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE RETURN_CONST</td>
<td align="right">196,856,083</td>
<td align="right">0.3%</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE</td>
<td align="right">193,236,187</td>
<td align="right">0.3%</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">186,059,952</td>
<td align="right">0.3%</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS RESUME_CHECK</td>
<td align="right">185,737,033</td>
<td align="right">0.3%</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">185,731,886</td>
<td align="right">0.3%</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">182,248,487</td>
<td align="right">0.3%</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR CALL_LIST_APPEND</td>
<td align="right">179,975,880</td>
<td align="right">0.3%</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">179,494,274</td>
<td align="right">0.3%</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_FAST</td>
<td align="right">176,147,586</td>
<td align="right">0.2%</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">174,391,620</td>
<td align="right">0.2%</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST</td>
<td align="right">170,742,110</td>
<td align="right">0.2%</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE LOAD_FAST</td>
<td align="right">170,034,987</td>
<td align="right">0.2%</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST</td>
<td align="right">169,944,669</td>
<td align="right">0.2%</td>
<td align="right">64.2%</td>
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
<td align="right">59,917,343</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">22,158,875</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,426,080</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">5,184,453</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">17,120</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">32,865,268</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">32,122,391</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,487,783</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,840,262</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,671,852</td>
<td align="right">6.1%</td>
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
<td align="right">2,879,513</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">6,000</td>
<td align="right">0.2%</td>
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
<td align="right">2,828,120</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">52,973</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,380</td>
<td align="right">0.1%</td>
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
<td align="right">1,886,503,231</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">161,946,046</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">99,020,511</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">46,679,273</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">11,582,507</td>
<td align="right">0.5%</td>
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
<td align="right">6,155,662</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,028,749</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">450,139</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">380,286</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">265,261</td>
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
<td align="left">POP_TOP</td>
<td align="right">8,173,467</td>
<td align="right">94.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">477,258</td>
<td align="right">5.5%</td>
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
<td align="right">262,780</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">50,800</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">49,620</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">39,420</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">15,720</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">262,140</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">112,860</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">50,700</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,480</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,060</td>
<td align="right">0.5%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">64,068,148</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">54,984,176</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">38,549,076</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">19,552,592</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">6,405,839</td>
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
<td align="right">60,283,905</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">45,109,465</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">35,709,422</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">20,643,136</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">16,015,240</td>
<td align="right">8.4%</td>
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
<td align="right">13,193,765</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">957,722</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">316,489</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">161,292</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">5,740</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">14,637,095</td>
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
<td align="right">30,759,834</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,513,500</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">977,440</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">274,936</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">27,721</td>
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
<td align="right">30,983,686</td>
<td align="right">80.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,406,760</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">352,000</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">308,009</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">223,045</td>
<td align="right">0.6%</td>
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
<td align="right">1,572,420</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">125,700</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
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
<td align="left">POP_TOP</td>
<td align="right">1,697,240</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,520</td>
<td align="right">0.1%</td>
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
<td align="right">89,315,039</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,801,165</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">91,116,204</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">71,429,041</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">33,089,474</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">16,241,001</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">14,437,380</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">13,410,032</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">55,346,298</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">47,984,662</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">32,442,307</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,391,553</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">14,440,746</td>
<td align="right">7.4%</td>
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
<td align="right">754,156,835</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">595,900,600</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">561,096,152</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">247,604,283</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">47,020,226</td>
<td align="right">2.1%</td>
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
<td align="right">26,863,952</td>
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
<td align="right">16,589,992</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,554,158</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,790,238</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">788,029</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">355,164</td>
<td align="right">1.3%</td>
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
<td align="right">82,725,862</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60,985,969</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">51,149,795</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">21,809,550</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">16,903,461</td>
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
<td align="right">141,426,458</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">44,777,216</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">21,809,550</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20,219,441</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">17,821,946</td>
<td align="right">6.4%</td>
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
<td align="right">8,818,853</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,642,549</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">906,943</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">816,392</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">744,967</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">4,259,530</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,690,698</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,079,860</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">880,460</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">746,499</td>
<td align="right">5.2%</td>
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
<td align="right">702,801,700</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">419,583,550</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">247,774,343</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">232,196,366</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">161,946,046</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">916,882,639</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">539,789,409</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">411,439,272</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">239,103,181</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">141,228,826</td>
<td align="right">5.8%</td>
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
<td align="right">5,499,102</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,191,883</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,994,795</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">420,174</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">402,724</td>
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
<td align="right">13,295,272</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,104,254</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">238,579</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">13,199</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">397,177,465</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">218,984,290</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">73,604,256</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">26,396,185</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">7,121,549</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">267,066,628</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">227,745,882</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">99,752,782</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">98,534,632</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">16,238,309</td>
<td align="right">2.2%</td>
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
<td align="right">209,475,857</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">46,679,273</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">8,960,890</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">6,008,264</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">665,653</td>
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
<td align="left">GET_AWAITABLE</td>
<td align="right">206,184,219</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">47,020,226</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">7,617,949</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">3,686,740</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,726,339</td>
<td align="right">1.0%</td>
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
<td align="right">649,343,916</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">231,035,030</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">227,560,573</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">128,374,886</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">125,620,812</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">754,156,835</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">370,425,264</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">231,035,030</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">168,270,369</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">146,088,173</td>
<td align="right">6.9%</td>
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
<td align="right">42,031,754</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,776,900</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,217,844</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,567,082</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,608,120</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">47,186,405</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,508,388</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,040,844</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,651,900</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">675,480</td>
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
<td align="right">74,740,888</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">49,439,615</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">10,292,460</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,487,040</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,103,881</td>
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
<td align="right">103,320,142</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">36,534,404</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">161,933</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">151,334</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">108,976</td>
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
<td align="right">90,281,088</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,124,508</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,607,500</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">342,618</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">117,468</td>
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
<td align="right">59,715,120</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">30,482,020</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,122,420</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,639,082</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">292,980</td>
<td align="right">0.3%</td>
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
<td align="right">85,844,504</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60,065,991</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">47,074,274</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">38,560,891</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">10,064,294</td>
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
<td align="right">64,446,043</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">56,902,298</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">36,265,749</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">20,686,460</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17,875,569</td>
<td align="right">6.3%</td>
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
<td align="right">2,581,986</td>
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
<td align="right">841,307</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">664,361</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">225,252</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">186,060</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">176,880</td>
<td align="right">6.9%</td>
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
<td align="right">25,002,564</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">20,568,748</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">9,493,831</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">8,063,349</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">5,101,536</td>
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
<td align="right">34,677,040</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">30,700,151</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">20,614,052</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,048,670</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">3,040,165</td>
<td align="right">3.0%</td>
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
<td align="right">31,973,625</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">11,626,599</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">10,336,610</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">7,027,482</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,413,636</td>
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
<td align="right">42,626,922</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">23,569,420</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">11,626,599</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">9,000,611</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">313,681</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">49,657,935</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">31,697,377</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">28,529,974</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,699,132</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">5,122,420</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">80,557,830</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">16,966,404</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">10,376,534</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">7,027,482</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">6,773,520</td>
<td align="right">4.4%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">50,173,773</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">45,376,725</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,701,040</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,727,064</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,203,733</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">44,080,822</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">42,088,104</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,124,955</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">13,410,032</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,373,122</td>
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
<td align="right">136,639,433</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">37,809,487</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,315,457</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">9,000,611</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">3,202,894</td>
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
<td align="left">POP_TOP</td>
<td align="right">109,196,464</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">25,432,354</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">25,025,944</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">23,595,100</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,306,290</td>
<td align="right">2.2%</td>
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
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,518,016</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,999,980</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">403,671</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">262,072</td>
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
<td align="right">86.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,201,311</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">6,111,671</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">3,202,894</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">820,885</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">117,361,743</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">111,354,490</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,340</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">101,386,034</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">65,234,905</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">25,036,208</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">11,581,505</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">11,041,884</td>
<td align="right">4.8%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">18,038,956</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,650,335</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,704,111</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,403,300</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,862,878</td>
<td align="right">9.4%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">43,909,938</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,733,600</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">3,442,717</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,034,320</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,034,180</td>
<td align="right">3.3%</td>
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
<td align="right">12,706,745</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,393,281</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,236,167</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,703,395</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,122,956</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">23,785,561</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">16,395,986</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">698,500</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">683,960</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">595,151</td>
<td align="right">1.4%</td>
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
<td align="left">SWAP</td>
<td align="right">93,436,547</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,317,408</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">19,196,044</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">16,021,300</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">13,948,440</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">92,495,654</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">48,950,364</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">22,512,147</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,242,332</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">15,814,260</td>
<td align="right">6.6%</td>
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
<td align="right">99,020,511</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">38,375,564</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">36,972,789</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,533,610</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">4,875,997</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">185,737,033</td>
<td align="right">96.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">6,008,264</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,961</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">17,397</td>
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
<td align="right">36,763,793</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">449,460</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">210,704</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">184,449</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">53,100</td>
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
<td align="right">37,809,487</td>
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
<td align="right">916,882,639</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">153,417,505</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">150,430,864</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">67,654,917</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">67,620,259</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">595,900,600</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">179,975,880</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">154,208,229</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">136,639,433</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,109,924</td>
<td align="right">6.9%</td>
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
<td align="right">20,330,330</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">5,167,898</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,572,227</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,410,720</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,441,109</td>
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
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,606,448</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">9,726,640</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">9,600,774</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,578,640</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,372,967</td>
<td align="right">10.8%</td>
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
<td align="right">47,984,662</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,547,230</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">14,095,333</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">285,427</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">121,026</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">44,900,677</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">18,543,455</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,842,843</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,602,993</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,823,713</td>
<td align="right">2.3%</td>
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
<td align="right">10,601,703</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,007,093</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">185,708</td>
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
<td align="right">9,639,589</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">2,121,615</td>
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
<td align="right">9,991,692</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,393,387</td>
<td align="right">12.2%</td>
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
<td align="right">10,601,703</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">765,056</td>
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
<td align="right">82,153,217</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">50,126,661</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">49,092,897</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,857,606</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,732,039</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">150,827,880</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">39,493,566</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,115,360</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">12,927,701</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,892,692</td>
<td align="right">1.7%</td>
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
<td align="right">1,357,268</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">192,087</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">140,618</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">134,593</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">88,232</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,313,028</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">285,427</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">181,852</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">139,900</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">101,200</td>
<td align="right">4.5%</td>
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
<td align="right">549,877,585</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">5,242,800</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">880,460</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">260,830</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">43,667</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">530,981,243</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">18,902,583</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,831,328</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">296,380</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">130,161</td>
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
<td align="right">95,071,394</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">94,952,815</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">31,358,195</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">6,406,760</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">5,111,730</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">112,543,918</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">48,985,138</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">47,856,907</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">17,976,601</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">9,054,084</td>
<td align="right">3.6%</td>
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
<td align="right">42,088,104</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">21,155,110</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,385,486</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,262,218</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">721,756</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">67,620,259</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">140,618</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">24,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">8,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,880</td>
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
<td align="right">18,451,771</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">104,537</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">57,400</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">51,474</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">47,440</td>
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
<td align="right">18,518,016</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">119,086</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">50,160</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">47,620</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,600</td>
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
<td align="right">263,571,765</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">86,272,283</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">31,698,050</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">26,828,658</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">13,661,521</td>
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
<td align="right">73,907,994</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">69,939,232</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">51,430,737</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">47,224,122</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">26,396,185</td>
<td align="right">5.9%</td>
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
<td align="right">1,256,333,909</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">229,710,469</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">227,743,331</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">198,343,151</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">169,944,669</td>
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
<td align="right">735,230,407</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">494,732,769</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">267,427,451</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">245,158,196</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">212,107,302</td>
<td align="right">6.2%</td>
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
<td align="right">90,787,125</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">63,035,696</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">39,091,186</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">36,075,975</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">31,361,077</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">122,672,888</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">73,604,256</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">38,147,777</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">26,828,658</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">25,681,803</td>
<td align="right">6.4%</td>
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
<td align="right">1,929,735,222</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,721,137,468</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,590,517,460</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">977,022,343</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">735,230,407</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,184,328,155</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,256,333,909</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,020,181,475</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">702,530,154</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">649,343,916</td>
<td align="right">5.1%</td>
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
<td align="right">32,442,307</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">20,264,664</td>
<td align="right">38.4%</td>
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
<td align="right">32,442,227</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">20,264,664</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">160</td>
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
<td align="right">4,682,963</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">691,008</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">459,698</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">426,931</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">350,590</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,872,463</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">849,740</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">575,920</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">417,995</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">129,082</td>
<td align="right">1.8%</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">379,661,454</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">279,946,258</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">267,066,628</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">216,175,938</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">209,042,665</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">631,113,590</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">289,915,733</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">209,042,665</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">206,764,580</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">203,099,660</td>
<td align="right">8.1%</td>
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
<td align="right">19,550,454</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">141,791</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">134,753</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">90,443</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">65,907</td>
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
<td align="right">19,589,975</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">334,354</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">182,422</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">132,090</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60,995</td>
<td align="right">0.3%</td>
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
<td align="right">311,660</td>
<td align="right">3.8%</td>
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
<td align="right">18,588</td>
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
<td align="right">8,181</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,540</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,267</td>
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
<td align="right">20,247,008</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,909,018</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">4,306,290</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">2,151,870</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,171,138</td>
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
<td align="left">MAKE_CELL</td>
<td align="right">20,247,008</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">13,732,350</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">460,926</td>
<td align="right">1.3%</td>
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
<td align="right">1,212,244,615</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">829,121,400</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">344,573,510</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">150,827,880</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">103,320,142</td>
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
<td align="right">1,721,137,468</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">300,218,284</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">264,330,892</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">169,944,669</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">153,417,505</td>
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
<td align="right">159,012,168</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">30,063,821</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">19,385,515</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">10,606,448</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,142,585</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">170,034,987</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">36,075,975</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,337,190</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,421,669</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,055,810</td>
<td align="right">2.2%</td>
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
<td align="right">298,663,976</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">56,647,808</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9,726,640</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,156,851</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">892,920</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">122,405,574</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">106,055,519</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">74,306,032</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">19,607,113</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">18,143,738</td>
<td align="right">4.9%</td>
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
<td align="right">174,391,620</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">39,616,625</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">39,493,566</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">36,534,404</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">26,488,220</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">237,542,296</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">41,928,273</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">25,211,215</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">25,048,261</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,874,868</td>
<td align="right">4.8%</td>
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
<td align="right">300,218,284</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">253,220,700</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">239,103,181</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">196,856,083</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">98,509,087</td>
<td align="right">7.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">561,096,152</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">419,583,550</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">89,315,039</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">59,961,897</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">49,344,257</td>
<td align="right">3.8%</td>
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
<td align="right">129,109,924</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">25,773,735</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">18,902,583</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">61,147</td>
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
<td align="right">146,806,753</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">18,952,275</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">8,000,000</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">61,147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">10,387</td>
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
<td align="right">16,589,992</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">212,629</td>
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
<td align="right">9,456,102</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,207,903</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,000,099</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">284,046</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">212,629</td>
<td align="right">1.3%</td>
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
<td align="right">24,494,778</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,814,775</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">801,120</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">483,922</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">288,442</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">17,938,510</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">4,196,442</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,461,021</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,880,247</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,108,423</td>
<td align="right">6.3%</td>
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
<td align="right">370,425,264</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">311,223,597</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">212,107,302</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">129,815,066</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">120,283,760</td>
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
<td align="right">1,590,517,460</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">216,671,517</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">179,494,274</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">137,705,330</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">98,509,087</td>
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
<td align="right">14,420,838</td>
<td align="right">78.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,987,501</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,410,103</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">211,300</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">206,840</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">12,201,482</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,341,340</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,248,483</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,057,261</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">412,686</td>
<td align="right">2.2%</td>
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
<td align="right">134,953,283</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">61,208,507</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,977,437</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,492,712</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,200,160</td>
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
<td align="right">130,701,172</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">32,178,761</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">16,955,076</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">12,682,429</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">7,702,712</td>
<td align="right">3.7%</td>
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
<td align="right">101,225,572</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">32,442,227</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">22,363,226</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">20,614,052</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">13,530,413</td>
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
<td align="left">COPY</td>
<td align="right">93,436,547</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">22,514,147</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">20,568,748</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">15,843,813</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">15,814,260</td>
<td align="right">6.4%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">42,254</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">25,193</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">24,900</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">19,627</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">8,724</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">105,331</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">24,867</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,098</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5,172</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2,937</td>
<td align="right">1.9%</td>
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
<td align="right">502,551,424</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">125,515,680</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">41,716,800</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">32,241,160</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">20,643,136</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">502,551,424</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">247,604,283</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">33,365,764</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,616,314</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">86,720</td>
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
<td align="right">101,627</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">82,303</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">19,309</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,832</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">17,397</td>
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
<td align="right">111,051</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">65,907</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">25,883</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">23,380</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">12,303</td>
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
<td align="right">141,172,678</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">77,690,840</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">62,998,127</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">29,119,360</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">19,422,680</td>
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
<td align="right">125,620,812</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">67,437,492</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">35,847,882</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">27,274,146</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">22,363,226</td>
<td align="right">6.4%</td>
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
<td align="right">22,549,501</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,210,702</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">6,400,200</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,641,100</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">550,200</td>
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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">21,212,480</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,676,480</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,097,183</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,640,800</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">960,313</td>
<td align="right">2.2%</td>
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
<td align="right">52,669,876</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">47,819,908</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">36,265,749</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,766,159</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,770,580</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">54,037,110</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">30,621,850</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">30,018,280</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">29,119,360</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,292,342</td>
<td align="right">1.5%</td>
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
<td align="right">38,331,900</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,517,123</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">450,330</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">345,531</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">122,445</td>
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
<td align="right">37,917,180</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">2,505,544</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">800,713</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">425,720</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">341,940</td>
<td align="right">0.8%</td>
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
<td align="right">267,427,451</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,628,858</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,604,140</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,768,661</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,330,500</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">205,324,260</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">35,223,062</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">24,168,497</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">13,530,413</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">9,513,277</td>
<td align="right">3.2%</td>
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
<td align="right">53,590,396</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">35,709,422</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">22,478,464</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">18,779,807</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,041,227</td>
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
<td align="left">STORE_FAST</td>
<td align="right">57,229,582</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">42,147,549</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,238,166</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,004,514</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,453,279</td>
<td align="right">3.2%</td>
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
<td align="right">47,315,504</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">607,415</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">593,664</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">90,700</td>
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
<td align="right">48,314,715</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">263,960</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">88,022</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">5,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,040</td>
<td align="right">0.0%</td>
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
<td align="right">209,710,390</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">30,482,020</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">15,966,837</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,947,353</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,065,980</td>
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
<td align="right">104,824,730</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">47,396,520</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">40,976,076</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">36,129,520</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">24,833,281</td>
<td align="right">8.4%</td>
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
<td align="right">123,818,273</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,619,849</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">8,547</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,968</td>
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
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,071,817</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,461,080</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">6,403,300</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,432,838</td>
<td align="right">4.0%</td>
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
<td align="right">31,073,626</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20,686,460</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">10,486,240</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">9,931,100</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,944,800</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">89,506,524</td>
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
<td align="right">39,392,593</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">30,018,280</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">28,277,350</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,299,764</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,405,316</td>
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
<td align="right">58,280,126</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">36,972,789</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">15,355,143</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">3,005,526</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">796,109</td>
<td align="right">0.7%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">2,640,314</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">696,986</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">279,163</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">225,943</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">221,185</td>
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
<td align="left">POP_TOP</td>
<td align="right">3,281,234</td>
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">785,196</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">62,581</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">47,208</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">19,323</td>
<td align="right">0.5%</td>
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
<td align="right">16,810,120</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">11,942,886</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,157,641</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,048,311</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,149,999</td>
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
<td align="left">STORE_FAST</td>
<td align="right">22,273,656</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">16,241,001</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,212,046</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,405,316</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,041,870</td>
<td align="right">6.3%</td>
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
<td align="right">105,087,247</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">78,002,331</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">27,259,460</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,717,082</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,144,787</td>
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
<td align="right">83,520,612</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">70,488,216</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">34,048,175</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">19,196,044</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">10,292,460</td>
<td align="right">4.5%</td>
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
<td align="right">13,448,002</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,041,870</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,267,826</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,699,380</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,197,387</td>
<td align="right">7.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">12,507,091</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,804,211</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,699,380</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,553,925</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,185,967</td>
<td align="right">4.2%</td>
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
<td align="right">122,456,208</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">33,462,784</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">21,698,477</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">21,212,480</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,025,729</td>
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
<td align="left">POP_TOP</td>
<td align="right">83,914,445</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">59,533,743</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">41,651,591</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">18,827,091</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">17,148,750</td>
<td align="right">6.8%</td>
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
<td align="right">235,669,198</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">193,236,187</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">20,816,111</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">10,376,534</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,897,597</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">453,944,247</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,409,434</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,512,090</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,937,753</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">258,440</td>
<td align="right">0.1%</td>
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
<td align="right">117,203,708</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">24,323,746</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,114,840</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,258,840</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,054,251</td>
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
<td align="right">36,403,912</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">30,753,790</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">29,521,648</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">16,055,528</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">10,086,360</td>
<td align="right">6.8%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">179,975,880</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">85,523,776</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,527,520</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,247,113</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">637,460</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">150,430,864</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">81,846,871</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">15,423,300</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,253,039</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,467,679</td>
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
<td align="right">44,038,624</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">29,380,898</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">29,092,038</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,451,018</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,707,145</td>
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
<td align="left">STORE_FAST</td>
<td align="right">87,957,109</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,166,205</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,107,934</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,994,645</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,765,442</td>
<td align="right">3.4%</td>
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
<td align="right">22,427,545</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">791,221</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">600,485</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">391,063</td>
<td align="right">1.6%</td>
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
<td align="right">17,553,554</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,981,260</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,260,225</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">322,140</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">310,400</td>
<td align="right">1.3%</td>
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
<td align="right">94,698,193</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">70,267,082</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">22,817,446</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">523,225</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">364,227</td>
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
<td align="right">105,938,828</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">33,089,474</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,940,944</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">11,942,886</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,868,057</td>
<td align="right">3.1%</td>
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
<td align="right">186,059,952</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">44,080,822</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,849,000</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,244,853</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,172,987</td>
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
<td align="right">232,196,366</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,652,853</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,489,029</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">884,833</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">849,176</td>
<td align="right">0.3%</td>
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
<td align="right">128,980,589</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">105,572,187</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">99,752,782</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">95,999,840</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">41,198,351</td>
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
<td align="right">311,223,597</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">61,905,850</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">55,895,733</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">49,657,935</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">38,430,944</td>
<td align="right">6.6%</td>
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
<td align="right">439,122,175</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">390,910,698</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">205,324,260</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">182,248,487</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">100,869,820</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,221,271,490</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">209,475,857</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,845,780</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">38,375,564</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">28,017,405</td>
<td align="right">1.8%</td>
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
<td align="right">42,023,723</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">27,031,679</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">21,111,850</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,789,312</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">11,201,440</td>
<td align="right">7.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">125,973,628</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">8,960,890</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">5,533,610</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,986,010</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,171,138</td>
<td align="right">0.8%</td>
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
<td align="right">13,346,927</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,482,140</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,205,060</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,664,540</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">145,520</td>
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
<td align="right">8,089,727</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">6,400,200</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,581,940</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,278,360</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,199,960</td>
<td align="right">12.8%</td>
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
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,686,740</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">698,342</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">585,140</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">89,660</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">88,462</td>
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
<td align="left">BUILD_TUPLE</td>
<td align="right">3,344,060</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">721,236</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">331,534</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">234,940</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">232,980</td>
<td align="right">4.5%</td>
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
<td align="right">109,693,900</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">689,660</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">87,961</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">59,320</td>
<td align="right">0.1%</td>
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
<td align="right">52,341,990</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,918,981</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">16,694,850</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,335,407</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,052,540</td>
<td align="right">3.7%</td>
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
<td align="right">128,378,666</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,470,540</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,241,378</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">382,455</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">361,290</td>
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
<td align="right">128,374,886</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,970,310</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">20,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">432</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">494,732,769</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">106,015,909</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">92,495,654</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">44,000,670</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">29,639,313</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">829,121,400</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">27,094,093</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">26,488,220</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,441,109</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,568,712</td>
<td align="right">0.2%</td>
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
<td align="right">63,303,194</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,975,732</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">10,779,244</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,799,453</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">703,280</td>
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
<td align="right">71,822,435</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">13,948,440</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,346,840</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,628,479</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,490,680</td>
<td align="right">1.6%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">9,730,052</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,499,478</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,644,748</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,070,773</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">813,702</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">20,149,195</td>
<td align="right">70.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,392,094</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">757,000</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">85,360</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">63,860</td>
<td align="right">0.2%</td>
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
<td align="right">45,362,772</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,083,767</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">2,474,840</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,164,459</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">663,827</td>
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
<td align="right">54,262,443</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">741,238</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">229,920</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">86,140</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">83,660</td>
<td align="right">0.2%</td>
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
<td align="right">1,645,462</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">438,780</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">137,583</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">95,140</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">65,220</td>
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
<td align="left">POP_TOP</td>
<td align="right">1,663,705</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">571,219</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">78,800</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">66,740</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">64,736</td>
<td align="right">2.6%</td>
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
<td align="right">88,617,820</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">55,346,298</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,372,967</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,318,595</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,313,028</td>
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
<td align="right">69,400,367</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">59,222,566</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">14,420,838</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,427,492</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,994,299</td>
<td align="right">1.9%</td>
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
<td align="right">6,828,660</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,292,027</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,230,160</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">668,800</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">139,900</td>
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
<td align="left">STORE_FAST</td>
<td align="right">16,876,433</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">206,840</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">33,230</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">24,992</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,813</td>
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
<td align="left">GET_ITER</td>
<td align="right">30,391,553</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">10,751,796</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,048,859</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">181,852</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">69,633</td>
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
<td align="right">41,044,555</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,987,501</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">435,838</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">364,630</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">207,699</td>
<td align="right">0.5%</td>
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
<td align="right">2,184,328,155</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">206,764,580</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">47,396,520</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">22,512,147</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">21,774,958</td>
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
<td align="right">496,697,954</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">327,818,259</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">251,899,574</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">227,560,573</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">120,283,760</td>
<td align="right">4.8%</td>
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
<td align="right">185,731,886</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,846,734</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,473,114</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">83,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">63,841</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">94,698,193</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">53,494,827</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">39,201,761</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,535,351</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,924,642</td>
<td align="right">2.0%</td>
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
<td align="right">251,899,574</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">238,891,748</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">25,681,803</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">19,005,828</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">15,125,550</td>
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
<td align="right">362,686,586</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">70,267,082</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">64,517,749</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60,249,865</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">23,880,385</td>
<td align="right">3.9%</td>
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
<td align="right">702,530,154</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">117,537,424</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">53,750,313</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">17,608,001</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,505,699</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">439,122,175</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">217,852,454</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">216,175,938</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">17,596,197</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">11,789,312</td>
<td align="right">1.3%</td>
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
<td align="right">453,678,267</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,560,000</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,045,569</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">585,680</td>
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
<td align="right">397,177,465</td>
<td align="right">85.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">20,816,111</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,188,462</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,390,163</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,560,000</td>
<td align="right">1.4%</td>
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
<td align="right">28,692,092</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,871,056</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">860,275</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">450,068</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">361,961</td>
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
<td align="right">29,138,094</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,785,245</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,772,573</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">511,699</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">264,294</td>
<td align="right">0.8%</td>
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
<td align="right">1,020,181,475</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">27,694,006</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,951,378</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,920,040</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,667,515</td>
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
<td align="right">276,738,907</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">205,705,494</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">128,378,666</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">117,537,424</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">61,208,507</td>
<td align="right">5.8%</td>
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
<td align="right">626,032,084</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">318,700,866</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">137,705,330</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">136,807,861</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">30,888,540</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">977,022,343</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">193,236,187</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">62,494,095</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">49,092,897</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">39,091,186</td>
<td align="right">2.7%</td>
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
<td align="right">396,663,048</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">362,085,331</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">264,330,892</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">216,671,517</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">77,690,840</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">564,723,982</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">453,678,267</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">235,669,198</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">133,391,348</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">86,272,283</td>
<td align="right">4.4%</td>
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
<td align="right">75,916,998</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">12,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">8,181</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">47,524,085</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">15,045,823</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">11,308,148</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,707,700</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">172,263</td>
<td align="right">0.2%</td>
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
<td align="right">1,886,503,231</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,221,271,490</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">525,492,676</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">411,439,272</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">185,737,033</td>
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
<td align="right">1,929,735,222</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">702,801,700</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">626,032,084</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">549,877,585</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">362,085,331</td>
<td align="right">7.6%</td>
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
<td align="right">317,901,722</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">289,915,733</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">36,129,520</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">22,514,147</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,493,000</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">196,856,083</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">170,742,110</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">138,467,398</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">83,401,188</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">51,149,795</td>
<td align="right">7.5%</td>
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
<td align="right">631,113,590</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">432,479,432</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,667,515</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,479,402</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">488,574</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">379,661,454</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">253,220,700</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">229,710,469</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">176,147,586</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">16,004,120</td>
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
<td align="right">21,845,224</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">10,284,040</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">10,086,360</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,640,240</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,516,632</td>
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
<td align="right">31,513,542</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">11,411,390</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,045,716</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">2,642,549</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,031,021</td>
<td align="right">1.9%</td>
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
<td align="right">42,576,944</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">26,675,280</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,192,489</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">888,698</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">529,880</td>
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
<td align="right">49,414,433</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">39,616,625</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">361,943</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">28,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">20,800</td>
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
<td align="right">453,944,247</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">327,818,259</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">146,088,173</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">111,991,064</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">105,938,828</td>
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
<td align="right">1,212,244,615</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">174,391,620</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">25,523,449</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,572,227</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">2,628,590</td>
<td align="right">0.2%</td>
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
<td align="right">52,552,581</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,835,927</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,698,523</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,136,378</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">841,724</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">56,741,714</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,278,346</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">100,766</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,971</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,270</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">48,108,387</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">14,840,644</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">642,870</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">590,480</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">496,600</td>
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
<td align="right">50,647,146</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">13,316,334</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">673,883</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">290,916</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">15,720</td>
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
<td align="right">205,705,494</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">47,309,366</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">47,224,122</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">25,720,574</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">21,270,780</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">344,573,510</td>
<td align="right">96.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">10,231,865</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">714,060</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">361,999</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">20,480</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">6,177,311</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,388,369</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,641,600</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">141,720</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">102,520</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,374,870</td>
<td align="right">65.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,344,363</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">65,100</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">8,020</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,560</td>
<td align="right">0.0%</td>
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
<td align="right">292,583</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">121,183</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">50,140</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,560</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,200</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">364,086</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">118,900</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,060</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">2,497,933</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,197,350</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">849,176</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">431,960</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">289,147</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,977,437</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">494,887</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">184,660</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">39,760</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,669</td>
<td align="right">0.4%</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">69,400,367</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">46,907,981</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">44,900,677</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,955,705</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,800,421</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">134,953,283</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42,775,394</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">711,898</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">87,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">47,401</td>
<td align="right">0.0%</td>
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
<td align="right">214,354,530</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">15,814,260</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">8,064,920</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,744,041</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,291,970</td>
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
<td align="right">61,972,064</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">44,000,670</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">39,855,180</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">25,588,803</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,278,801</td>
<td align="right">5.3%</td>
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
<td align="right">9,140,735</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,791,098</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">2,505,544</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">943,320</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">302,373</td>
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
<td align="right">14,374,530</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,886,432</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,438,160</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">925,560</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">507,750</td>
<td align="right">2.4%</td>
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
<td align="right">42,159,940</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">30,065,440</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">16,033,112</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">28,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,245</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">19,869,520</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">16,096,800</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">9,931,100</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">302,373</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">33,598,513</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">10,049,623</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">977,474</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">842,720</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">390,560</td>
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
<td align="right">30,629,940</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">10,798,502</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,202,720</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">750,060</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">287,480</td>
<td align="right">0.6%</td>
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
<td align="right">2,996,745</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">8,621</td>
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
<td align="right">3,006,046</td>
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
<td align="right">168,270,369</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">146,806,753</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">59,961,897</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">56,530</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">12,880</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">129,815,066</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">81,144,090</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">77,690,840</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">77,690,840</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,588,113</td>
<td align="right">2.3%</td>
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
<td align="right">1,400,290</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">439,542</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">411,572</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">10,840</td>
<td align="right">0.5%</td>
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
<td align="right">2,263,284</td>
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
<td align="right">3,442,717</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,628,590</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">673,883</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">57,971</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">57,402</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">4,524,360</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">959,541</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">942,795</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">373,440</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">34,368</td>
<td align="right">0.5%</td>
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
<td align="right">206,184,219</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,728,040</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,629,756</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,175,175</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">3,006,046</td>
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
<td align="right">227,743,331</td>
<td align="right">100.0%</td>
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
<td align="right">3,701,094</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">193,760</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">176,088</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">172,100</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">110,164</td>
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
<td align="left">PUSH_EXC_INFO</td>
<td align="right">4,191,883</td>
<td align="right">94.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">189,340</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">44,439</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">8,922</td>
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
<td align="right">820,885</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">744,967</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">243,113</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">237,479</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">44,515</td>
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
<td align="right">552,327</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">291,517</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">262,072</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,320</td>
<td align="right">0.1%</td>
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
<td align="right">31,683,439</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,805,758</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,264,551</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">281,515</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">18,816</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">18,167,743</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">11,564,587</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,805,618</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,797,060</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">273,598</td>
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
<td align="right">26,241,858</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,310,880</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,339,315</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">252,840</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">175,844</td>
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
<td align="right">11,810,908</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,535,500</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,440,779</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,125,680</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,048,100</td>
<td align="right">5.9%</td>
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
<td align="right">530,981,243</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">245,158,196</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">10,748,387</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">7,127</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">525,492,676</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">247,774,343</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">13,595,200</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">15,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">12,880</td>
<td align="right">0.0%</td>
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
<td align="right">2,858,540</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,196,156</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,108,840</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">679,620</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">294,114</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">3,205,708</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,149,149</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,461,073</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,400</td>
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
<td align="right">341,772</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">268,180</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">246,960</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">194,248</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">90,440</td>
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
<td align="right">190,888</td>
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
<td align="right">30,325,788</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">763,882</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">71,980</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">720</td>
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
<td align="right">30,759,834</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">398,736</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,840</td>
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
<td align="left">FORMAT_SIMPLE</td>
<td align="right">2,149,149</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,235,966</td>
<td align="right">36.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,482,143</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">902,740</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">470,974</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">191,980</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">88,000</td>
<td align="right">2.6%</td>
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
<td align="right">1,706,280</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">907,240</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">120,560</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">50,920</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">24,120</td>
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
<td align="left">FORMAT_SIMPLE</td>
<td align="right">2,858,540</td>
<td align="right">100.0%</td>
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
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">303,959</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">197,826</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">69,043</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">68,782</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">645,880</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">642,560</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">355,286</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">148,825</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">95,835</td>
<td align="right">4.7%</td>
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
<td align="right">35,847,882</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,111,867</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,040,165</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,990,540</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">2,121,615</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">19,590,318</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17,926,029</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,422,885</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,172,724</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,993,148</td>
<td align="right">5.3%</td>
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
<td align="right">22,100,170</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,312,380</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">567,309</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">197,380</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">46,740</td>
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
<td align="right">24,464,040</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,048,160</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">317,919</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">235,140</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">110,200</td>
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
<td align="right">29,038,307</td>
<td align="right">87.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,173,589</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">342,120</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">243,169</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">178,768</td>
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
<td align="right">10,347,667</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,408,253</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">5,617,745</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,474,840</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,317,360</td>
<td align="right">6.9%</td>
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
<td align="right">7,139,953</td>
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
<td align="left">EXTENDED_ARG</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
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
<td align="right">7,121,549</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">88,004</td>
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
<td align="right">24,722,234</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,814,260</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">10,027,305</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,643,757</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">321,904</td>
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
<td align="right">40,307,503</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,804,320</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,415,197</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,077,360</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">477,526</td>
<td align="right">0.9%</td>
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
<td align="right">642,186</td>
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
<td align="right">425,868</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">203,047</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">9,791</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">2,360</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,360</td>
<td align="right">0.2%</td>
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
<td align="right">32,483,020</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">791,500</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">670,740</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">555,700</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">274,640</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">35,187,640</td>
<td align="right">100.0%</td>
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
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,742,400</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">527,691</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">293,280</td>
<td align="right">2.6%</td>
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
<td align="right">11,394,496</td>
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
<td align="right">19,176</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">86,320</td>
<td align="right">35.8%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">4,200</td>
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
<td align="right">44,713</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">22,880</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,540</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">782</td>
<td align="right">1.1%</td>
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
<td align="right">45,655</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">22,640</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">3,100</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">862</td>
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
<td align="right">152,057</td>
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
<td align="right">30,998</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">239</td>
<td align="right">0.2%</td>
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
<td align="right">235,660</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">19,780</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,280</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,280</td>
<td align="right">0.5%</td>
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
<td align="right">258,020</td>
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
<td align="right">238,579</td>
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
<td align="right">229,199</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">8,580</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">800</td>
<td align="right">0.3%</td>
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
<td align="right">24,460</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">740</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">300</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">15,600</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">9,620</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">300</td>
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
<td align="right">301,795,829</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">983,082,211</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">20,051,694</td>
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
<td align="right">420,216</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">979,400</td>
<td align="right">70.0%</td>
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
<td align="right">734,751</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">55,696</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,605</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">30,817</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">28,114</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">17,173</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">12,963</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">12,063</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">11,886</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,937</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,739</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">6,885</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,505</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">3,904</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">3,349</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,960</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,656</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,977</td>
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
<td align="right">192,588,183</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">645,928,587</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,755,255</td>
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
<td align="right">119,589</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">96,165</td>
<td align="right">44.6%</td>
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
<td align="right">33,999</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">30,440</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">13,220</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">10,300</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">1,640</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,280</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">760</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">126</td>
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
<td align="right">283,892,907</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">20,080</td>
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
<td align="right">3,915,441,083</td>
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
<td align="right">160,181,917</td>
<td align="right">3.8%</td>
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
<td align="right">3,594,074</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">95,568</td>
<td align="right">2.6%</td>
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
<td align="right">82,648</td>
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
<td align="right">63,036,130</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,122,834,614</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">756,338</td>
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
<td align="right">74,976</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">129,981</td>
<td align="right">63.4%</td>
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
<td align="right">28,494</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,099</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,410</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,865</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">10,456</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,251</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">2,740</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2,060</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,786</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,660</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">1,480</td>
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
<td align="right">45,144,483</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">81,593,310</td>
<td align="right">64.3%</td>
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
<td align="right">2.0%</td>
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
<td align="right">61,560</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">77,995</td>
<td align="right">55.9%</td>
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
<td align="right">29,032</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">21,880</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">18,203</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">8,880</td>
<td align="right">11.4%</td>
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
<td align="right">78,283,937</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">217,805,170</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">328,363</td>
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
<td align="right">56,601</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">125,846</td>
<td align="right">69.0%</td>
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
<td align="right">41,467</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,343</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">13,160</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,639</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,407</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">8,580</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,914</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">5,480</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,980</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,960</td>
<td align="right">1.6%</td>
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
<td align="right">516</td>
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
<td align="right">596,312,673</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">488,353</td>
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
<td align="right">5,995,016,848</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">154,513,897</td>
<td align="right">2.3%</td>
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
<td align="right">3,571,182</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">730,734</td>
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
<td align="left">not managed dict</td>
<td align="right">189,929</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">157,343</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">95,746</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">72,431</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">51,065</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">41,317</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">28,400</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">19,898</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">15,280</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,920</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">14,780</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">14,610</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">7,138</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3,397</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,820</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,080</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">200</td>
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
<td align="right">20,368,874</td>
<td align="right">0.6%</td>
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
<td align="right">3,411,758,129</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">428,525</td>
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
<td align="right">523,683</td>
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
<td align="right">9,587</td>
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
<td align="right">83,155,952</td>
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
<td align="right">9,421</td>
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
<td align="right">173,810,075</td>
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
<td align="right">786,864,153</td>
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
<td align="right">7,127</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,727</td>
<td align="right">89.6%</td>
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
<td align="right">16,127</td>
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
<td align="right">74,129,608</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,765,376,558</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">41,917,013</td>
<td align="right">2.3%</td>
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
<td align="right">913,193</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">98,866</td>
<td align="right">9.8%</td>
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
<td align="right">35,090</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,188</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">11,342</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,400</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,780</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">6,080</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">5,340</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,746</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">4,360</td>
<td align="right">4.4%</td>
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
<td align="right">63,363,502</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">99,852,707</td>
<td align="right">61.2%</td>
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
<td align="right">15,144</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">55,338</td>
<td align="right">78.5%</td>
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
<td align="right">34,039</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">11,159</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,120</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,320</td>
<td align="right">4.2%</td>
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
<td align="right">182,386,430</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,893,493,513</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">43,129,987</td>
<td align="right">2.1%</td>
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
<td align="right">1,029,650</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">177,508</td>
<td align="right">14.7%</td>
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
<td align="right">48,875</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">38,650</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">22,943</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">22,739</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">17,378</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,435</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,123</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">4,677</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">2,028</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,240</td>
<td align="right">0.7%</td>
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
<td align="right">119,449</td>
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
<td align="right">184,818,355</td>
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
<td align="right">31,539</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,657</td>
<td align="right">7.8%</td>
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
<td align="right">1,857</td>
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">500</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">300</td>
<td align="right">11.3%</td>
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
<td align="right">38,253,804,231</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">5,881,620,788</td>
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
<td align="right">26,632,975,816</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">425,796,072</td>
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
<td align="right">596,312,673</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">301,795,829</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">283,892,907</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">192,588,183</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">182,386,430</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,810,075</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">78,283,937</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">74,129,608</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">63,363,502</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">63,036,130</td>
<td align="right">3.0%</td>
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
<td align="right">72,301,562</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">58,202,838</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">39,376,427</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">39,267,102</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,831,441</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,946,518</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">23,102,105</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">20,980,092</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">20,357,361</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">19,159,107</td>
<td align="right">4.5%</td>
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
<td align="right">2,208,744,708</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,597,548,079</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,208,744,708</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,354,358,762</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">854,385,946</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,652,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,351,682,542</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">24,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">455,022,272</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">34,623,171</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">245,345,856</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">213,221,899</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">73,946,567</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,122,230,960</td>
<td align="right">78.4%</td>
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
<td align="right">6,273,715,883</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,275,588,328</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,799,434,370</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,673,694,148</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">105,123,152</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,617,070</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">11,124,958,459</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,546,110</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">86,203,373,782</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">99,739,000,366</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">23,452,415,952</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">26,329,284,939</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">6,547,460</td>
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
<td align="right">2,326,935,849</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">30,873,929</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">38,141,858</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,090,848,181</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,479,540</td>
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
<td align="right">19,533,998</td>
<td align="right">14,657,845,618</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">7,052,275,830</td>
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
<td align="right">534,203</td>
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
<td align="right">182,900</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">867</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">50,677</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">380</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">351,303</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">96,866</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,660</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">10,011</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,773</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,707,416,115</td>
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
<td align="right">243,812,821,294</td>
<td align="right">3,163.4%</td>
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
<td align="right">182,900</td>
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
<td align="right">179,080</td>
<td align="right">97.9%</td>
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
<td align="right">2,354</td>
<td align="right">1.3%</td>
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
<td align="right">14,854</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">41,120</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">54,517</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">39,241</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">20,955</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,657</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,136</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">420</td>
<td align="right">0.2%</td>
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
<td align="right">2,992</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">36,078</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">40,334</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">54,103</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">27,291</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,330</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,272</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">680</td>
<td align="right">0.4%</td>
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
<td align="right">28,222,400</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">190,273,294</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,031,368,449</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">850,947,895</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">890,846,364</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">779,478,569</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">433,393,339</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">212,852,313</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">26,941,643</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">7,342,898</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 2,048</td>
<td align="right">18,394,013</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 4,096</td>
<td align="right">685,827</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="right">740,528</td>
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
<td align="right">13,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="right">960</td>
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
<td align="right">399</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4,194,304</td>
<td align="right">241</td>
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
<td align="right">19,044,434,970</td>
<td align="right">7.8%</td>
<td align="right">7.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">14,114,639,559</td>
<td align="right">5.8%</td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">11,102,364,931</td>
<td align="right">4.6%</td>
<td align="right">18.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">8,615,272,594</td>
<td align="right">3.5%</td>
<td align="right">21.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,146,737,228</td>
<td align="right">3.3%</td>
<td align="right">25.0%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,134,865,193</td>
<td align="right">3.3%</td>
<td align="right">28.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">7,805,829,745</td>
<td align="right">3.2%</td>
<td align="right">31.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,845,887,429</td>
<td align="right">2.8%</td>
<td align="right">34.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,517,785,507</td>
<td align="right">2.7%</td>
<td align="right">37.0%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,694,560,798</td>
<td align="right">1.9%</td>
<td align="right">39.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">4,337,559,792</td>
<td align="right">1.8%</td>
<td align="right">40.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,255,471,258</td>
<td align="right">1.7%</td>
<td align="right">42.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,046,061,848</td>
<td align="right">1.7%</td>
<td align="right">44.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">4,009,292,160</td>
<td align="right">1.6%</td>
<td align="right">45.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,694,727,775</td>
<td align="right">1.5%</td>
<td align="right">47.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,534,625,499</td>
<td align="right">1.4%</td>
<td align="right">48.8%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,406,398,269</td>
<td align="right">1.4%</td>
<td align="right">50.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,903,514,817</td>
<td align="right">1.2%</td>
<td align="right">51.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,847,466,815</td>
<td align="right">1.2%</td>
<td align="right">52.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,804,654,107</td>
<td align="right">1.2%</td>
<td align="right">53.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,767,971,794</td>
<td align="right">1.1%</td>
<td align="right">54.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,700,380,524</td>
<td align="right">1.1%</td>
<td align="right">55.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,684,245,594</td>
<td align="right">1.1%</td>
<td align="right">57.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">2,664,455,634</td>
<td align="right">1.1%</td>
<td align="right">58.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,620,060,115</td>
<td align="right">1.1%</td>
<td align="right">59.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,580,419,174</td>
<td align="right">1.1%</td>
<td align="right">60.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,552,554,149</td>
<td align="right">1.0%</td>
<td align="right">61.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,514,046,018</td>
<td align="right">1.0%</td>
<td align="right">62.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,480,406,008</td>
<td align="right">1.0%</td>
<td align="right">63.3%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">2,374,091,377</td>
<td align="right">1.0%</td>
<td align="right">64.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,323,956,463</td>
<td align="right">1.0%</td>
<td align="right">65.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,323,288,641</td>
<td align="right">1.0%</td>
<td align="right">66.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,160,058,825</td>
<td align="right">0.9%</td>
<td align="right">67.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,110,187,678</td>
<td align="right">0.9%</td>
<td align="right">68.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,040,702,771</td>
<td align="right">0.8%</td>
<td align="right">68.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,008,850,318</td>
<td align="right">0.8%</td>
<td align="right">69.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,903,347,184</td>
<td align="right">0.8%</td>
<td align="right">70.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,875,482,541</td>
<td align="right">0.8%</td>
<td align="right">71.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,824,598,800</td>
<td align="right">0.7%</td>
<td align="right">71.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,634,737,910</td>
<td align="right">0.7%</td>
<td align="right">72.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,603,031,398</td>
<td align="right">0.7%</td>
<td align="right">73.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_OFFSET</td>
<td align="right">1,580,645,353</td>
<td align="right">0.6%</td>
<td align="right">73.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,540,115,940</td>
<td align="right">0.6%</td>
<td align="right">74.5%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,526,510,178</td>
<td align="right">0.6%</td>
<td align="right">75.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,516,944,737</td>
<td align="right">0.6%</td>
<td align="right">75.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,406,961,783</td>
<td align="right">0.6%</td>
<td align="right">76.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,390,575,456</td>
<td align="right">0.6%</td>
<td align="right">76.9%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,352,729,927</td>
<td align="right">0.6%</td>
<td align="right">77.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,333,354,563</td>
<td align="right">0.5%</td>
<td align="right">78.0%</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,332,915,316</td>
<td align="right">0.5%</td>
<td align="right">78.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,329,351,021</td>
<td align="right">0.5%</td>
<td align="right">79.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,304,102,553</td>
<td align="right">0.5%</td>
<td align="right">79.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,294,857,860</td>
<td align="right">0.5%</td>
<td align="right">80.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,231,842,667</td>
<td align="right">0.5%</td>
<td align="right">80.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,225,362,832</td>
<td align="right">0.5%</td>
<td align="right">81.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,220,664,125</td>
<td align="right">0.5%</td>
<td align="right">81.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,220,153,494</td>
<td align="right">0.5%</td>
<td align="right">82.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,186,545,243</td>
<td align="right">0.5%</td>
<td align="right">82.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,173,085,257</td>
<td align="right">0.5%</td>
<td align="right">83.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,134,596,094</td>
<td align="right">0.5%</td>
<td align="right">83.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,117,535,571</td>
<td align="right">0.5%</td>
<td align="right">84.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,098,161,306</td>
<td align="right">0.5%</td>
<td align="right">84.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,003,339,161</td>
<td align="right">0.4%</td>
<td align="right">85.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">999,272,386</td>
<td align="right">0.4%</td>
<td align="right">85.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">986,138,826</td>
<td align="right">0.4%</td>
<td align="right">85.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">975,555,017</td>
<td align="right">0.4%</td>
<td align="right">86.2%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">970,094,696</td>
<td align="right">0.4%</td>
<td align="right">86.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">918,608,652</td>
<td align="right">0.4%</td>
<td align="right">86.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">868,044,132</td>
<td align="right">0.4%</td>
<td align="right">87.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">861,528,686</td>
<td align="right">0.4%</td>
<td align="right">87.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">786,192,940</td>
<td align="right">0.3%</td>
<td align="right">88.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">778,678,833</td>
<td align="right">0.3%</td>
<td align="right">88.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">777,993,130</td>
<td align="right">0.3%</td>
<td align="right">88.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">777,390,430</td>
<td align="right">0.3%</td>
<td align="right">88.9%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">716,321,107</td>
<td align="right">0.3%</td>
<td align="right">89.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">715,462,649</td>
<td align="right">0.3%</td>
<td align="right">89.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">706,397,789</td>
<td align="right">0.3%</td>
<td align="right">89.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">652,736,239</td>
<td align="right">0.3%</td>
<td align="right">90.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">650,067,212</td>
<td align="right">0.3%</td>
<td align="right">90.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">628,780,943</td>
<td align="right">0.3%</td>
<td align="right">90.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">597,196,017</td>
<td align="right">0.2%</td>
<td align="right">90.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">585,341,217</td>
<td align="right">0.2%</td>
<td align="right">91.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">579,435,810</td>
<td align="right">0.2%</td>
<td align="right">91.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right">554,293,148</td>
<td align="right">0.2%</td>
<td align="right">91.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_OFFSET</td>
<td align="right">554,293,148</td>
<td align="right">0.2%</td>
<td align="right">91.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">547,162,353</td>
<td align="right">0.2%</td>
<td align="right">92.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">546,664,784</td>
<td align="right">0.2%</td>
<td align="right">92.2%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">542,268,067</td>
<td align="right">0.2%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">534,880,755</td>
<td align="right">0.2%</td>
<td align="right">92.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">534,277,081</td>
<td align="right">0.2%</td>
<td align="right">92.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">516,046,241</td>
<td align="right">0.2%</td>
<td align="right">93.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">512,895,843</td>
<td align="right">0.2%</td>
<td align="right">93.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">491,562,064</td>
<td align="right">0.2%</td>
<td align="right">93.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">462,626,161</td>
<td align="right">0.2%</td>
<td align="right">93.7%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">422,564,317</td>
<td align="right">0.2%</td>
<td align="right">93.9%</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">419,890,666</td>
<td align="right">0.2%</td>
<td align="right">94.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">418,697,877</td>
<td align="right">0.2%</td>
<td align="right">94.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">416,428,944</td>
<td align="right">0.2%</td>
<td align="right">94.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">413,357,472</td>
<td align="right">0.2%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">406,896,280</td>
<td align="right">0.2%</td>
<td align="right">94.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">405,536,727</td>
<td align="right">0.2%</td>
<td align="right">94.9%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">384,363,673</td>
<td align="right">0.2%</td>
<td align="right">95.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">357,987,407</td>
<td align="right">0.1%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">342,037,940</td>
<td align="right">0.1%</td>
<td align="right">95.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">316,236,152</td>
<td align="right">0.1%</td>
<td align="right">95.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">294,125,769</td>
<td align="right">0.1%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">289,030,234</td>
<td align="right">0.1%</td>
<td align="right">95.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">284,840,782</td>
<td align="right">0.1%</td>
<td align="right">95.8%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">262,574,789</td>
<td align="right">0.1%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">251,757,815</td>
<td align="right">0.1%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">248,347,692</td>
<td align="right">0.1%</td>
<td align="right">96.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">240,106,433</td>
<td align="right">0.1%</td>
<td align="right">96.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">238,329,802</td>
<td align="right">0.1%</td>
<td align="right">96.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">237,027,248</td>
<td align="right">0.1%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">232,463,146</td>
<td align="right">0.1%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">224,559,660</td>
<td align="right">0.1%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">222,291,948</td>
<td align="right">0.1%</td>
<td align="right">96.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">211,972,400</td>
<td align="right">0.1%</td>
<td align="right">96.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">210,823,778</td>
<td align="right">0.1%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">209,322,327</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">207,668,457</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">206,736,564</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">204,106,312</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">192,025,711</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">188,707,329</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">187,893,129</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">187,873,023</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">179,841,576</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">179,732,340</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">178,338,063</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">175,580,021</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">170,794,175</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">165,880,424</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">157,928,634</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">157,049,370</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,281,720</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">153,619,818</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">149,620,165</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">149,620,165</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">137,614,660</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">137,088,106</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">136,785,734</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">131,806,145</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">127,327,359</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">127,150,885</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">126,388,043</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">123,370,372</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">122,841,272</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">118,131,528</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">117,246,901</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">116,017,023</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">112,112,092</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">110,823,884</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">109,199,614</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">105,441,334</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">104,075,420</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">101,032,941</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">100,148,083</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">97,629,965</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">96,592,850</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">96,082,420</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">82,670,624</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">82,443,101</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,913,617</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">72,281,312</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">70,416,220</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">69,919,780</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">69,597,513</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">65,697,421</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">58,384,619</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">58,333,120</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">57,767,637</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">55,122,382</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">51,360,321</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">50,278,645</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,374,040</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">38,937,994</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">35,827,972</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,652,300</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">32,644,030</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">30,891,300</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right">27,485,438</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">25,923,935</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">23,051,496</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">20,500,503</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">12,914,864</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,693,120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">12,271,336</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,998,778</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,978,598</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,147,189</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">10,095,895</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">9,429,529</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">6,729,622</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">5,500,976</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">5,046,751</td>
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
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,946,700</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,489,080</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">2,416,549</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">2,072,415</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">871,420</td>
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
<td align="left">_POP_EXCEPT</td>
<td align="right">378,499</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">113,183</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">57,582</td>
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
<td align="right">4,841,756,853</td>
<td align="right">2.0%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC _CHECK_VALIDITY</td>
<td align="right">2,931,633,609</td>
<td align="right">1.2%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,903,514,817</td>
<td align="right">1.2%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES _LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,847,466,815</td>
<td align="right">1.2%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR _TIER2_RESUME_CHECK</td>
<td align="right">2,632,496,338</td>
<td align="right">1.1%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET _PUSH_FRAME</td>
<td align="right">2,552,554,149</td>
<td align="right">1.0%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _GUARD_NOS_INT</td>
<td align="right">2,443,251,891</td>
<td align="right">1.0%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _SET_IP</td>
<td align="right">2,432,210,970</td>
<td align="right">1.0%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME _RESUME_CHECK</td>
<td align="right">2,085,930,637</td>
<td align="right">0.9%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR _SET_IP</td>
<td align="right">2,081,742,396</td>
<td align="right">0.9%</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP _TIER2_RESUME_CHECK</td>
<td align="right">2,062,064,460</td>
<td align="right">0.8%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0 _LOAD_FAST_1</td>
<td align="right">2,020,719,604</td>
<td align="right">0.8%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _SET_IP</td>
<td align="right">2,008,931,132</td>
<td align="right">0.8%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _GUARD_IS_FALSE_POP</td>
<td align="right">2,007,533,945</td>
<td align="right">0.8%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,963,339,143</td>
<td align="right">0.8%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR _GUARD_IS_FALSE_POP</td>
<td align="right">1,935,973,272</td>
<td align="right">0.8%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT _BINARY_OP_ADD_INT</td>
<td align="right">1,887,013,696</td>
<td align="right">0.8%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET _CHECK_VALIDITY</td>
<td align="right">1,849,097,401</td>
<td align="right">0.8%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,821,600,117</td>
<td align="right">0.7%</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST_7</td>
<td align="right">1,782,246,035</td>
<td align="right">0.7%</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_SET_IP _CONTAINS_OP_SET</td>
<td align="right">1,771,663,977</td>
<td align="right">0.7%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_RETURN_OFFSET _DYNAMIC_EXIT</td>
<td align="right">1,580,645,353</td>
<td align="right">0.6%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,540,115,940</td>
<td align="right">0.6%</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _BINARY_SUBSCR_STR_INT</td>
<td align="right">1,531,009,400</td>
<td align="right">0.6%</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_POP_FRAME _RETURN_OFFSET</td>
<td align="right">1,530,306,757</td>
<td align="right">0.6%</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,518,404,902</td>
<td align="right">0.6%</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT _GUARD_KEYS_VERSION</td>
<td align="right">1,516,944,737</td>
<td align="right">0.6%</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL _GUARD_IS_FALSE_POP</td>
<td align="right">1,512,703,677</td>
<td align="right">0.6%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _SET_IP</td>
<td align="right">1,484,219,143</td>
<td align="right">0.6%</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _SET_IP</td>
<td align="right">1,407,497,756</td>
<td align="right">0.6%</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION _LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,406,961,783</td>
<td align="right">0.6%</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK _LOAD_FAST_0</td>
<td align="right">1,345,423,798</td>
<td align="right">0.6%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST _GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,333,354,563</td>
<td align="right">0.5%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS _CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,329,351,021</td>
<td align="right">0.5%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">_SET_IP _BINARY_SUBSCR</td>
<td align="right">1,314,273,687</td>
<td align="right">0.5%</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT _STORE_FAST_1</td>
<td align="right">1,284,800,473</td>
<td align="right">0.5%</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _LOAD_FAST</td>
<td align="right">1,272,208,637</td>
<td align="right">0.5%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">_SET_IP _LOAD_ATTR</td>
<td align="right">1,265,747,091</td>
<td align="right">0.5%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR _CHECK_VALIDITY</td>
<td align="right">1,221,152,750</td>
<td align="right">0.5%</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,220,153,494</td>
<td align="right">0.5%</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE _SET_IP</td>
<td align="right">1,213,870,020</td>
<td align="right">0.5%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK _ITER_CHECK_LIST</td>
<td align="right">1,204,891,185</td>
<td align="right">0.5%</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _SET_IP</td>
<td align="right">1,161,490,443</td>
<td align="right">0.5%</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,121,412,387</td>
<td align="right">0.5%</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST _ITER_NEXT_LIST</td>
<td align="right">1,117,535,571</td>
<td align="right">0.5%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_FAST_1</td>
<td align="right">1,117,031,561</td>
<td align="right">0.5%</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">_SET_IP _POP_FRAME</td>
<td align="right">1,114,126,351</td>
<td align="right">0.5%</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST _LOAD_FAST</td>
<td align="right">1,113,160,879</td>
<td align="right">0.5%</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE _COMPARE_OP_STR</td>
<td align="right">1,112,472,758</td>
<td align="right">0.5%</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP _CHECK_VALIDITY</td>
<td align="right">1,105,622,727</td>
<td align="right">0.5%</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _TO_BOOL_BOOL</td>
<td align="right">1,098,147,234</td>
<td align="right">0.5%</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL _GUARD_IS_TRUE_POP</td>
<td align="right">1,098,061,576</td>
<td align="right">0.5%</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _GUARD_BOTH_UNICODE</td>
<td align="right">1,092,750,841</td>
<td align="right">0.4%</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_SET_IP _BINARY_OP</td>
<td align="right">1,025,943,319</td>
<td align="right">0.4%</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK _LOAD_FAST_0</td>
<td align="right">1,024,399,865</td>
<td align="right">0.4%</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR _CHECK_VALIDITY</td>
<td align="right">1,022,312,520</td>
<td align="right">0.4%</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION _LOAD_ATTR_SLOT_0</td>
<td align="right">1,003,339,161</td>
<td align="right">0.4%</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST _CHECK_PERIODIC</td>
<td align="right">999,215,246</td>
<td align="right">0.4%</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4 _SET_IP</td>
<td align="right">992,941,993</td>
<td align="right">0.4%</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">987,619,668</td>
<td align="right">0.4%</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O _CHECK_PERIODIC</td>
<td align="right">984,276,805</td>
<td align="right">0.4%</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7 _LOAD_FAST_7</td>
<td align="right">967,215,345</td>
<td align="right">0.4%</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_BUILTIN_FAST</td>
<td align="right">949,171,967</td>
<td align="right">0.4%</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _GUARD_IS_TRUE_POP</td>
<td align="right">940,996,527</td>
<td align="right">0.4%</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION _LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">929,405,664</td>
<td align="right">0.4%</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">_SET_IP _CALL_BUILTIN_O</td>
<td align="right">918,649,368</td>
<td align="right">0.4%</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7 _LOAD_FAST_3</td>
<td align="right">918,268,846</td>
<td align="right">0.4%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST _STORE_FAST</td>
<td align="right">915,090,431</td>
<td align="right">0.4%</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT _STORE_FAST_7</td>
<td align="right">901,075,920</td>
<td align="right">0.4%</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1 _JUMP_TO_TOP</td>
<td align="right">899,204,320</td>
<td align="right">0.4%</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _COMPARE_OP_STR</td>
<td align="right">895,637,565</td>
<td align="right">0.4%</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2 _LOAD_FAST_3</td>
<td align="right">859,823,903</td>
<td align="right">0.4%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST</td>
<td align="right">853,718,828</td>
<td align="right">0.4%</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_CONST_INLINE_BORROW</td>
<td align="right">837,212,775</td>
<td align="right">0.3%</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _STORE_FAST</td>
<td align="right">802,911,469</td>
<td align="right">0.3%</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3 _LOAD_FAST_4</td>
<td align="right">802,767,941</td>
<td align="right">0.3%</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _LOAD_FAST_1</td>
<td align="right">796,540,854</td>
<td align="right">0.3%</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW _LOAD_CONST_INLINE_BORROW</td>
<td align="right">788,629,791</td>
<td align="right">0.3%</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL _LOAD_FAST_5</td>
<td align="right">778,940,453</td>
<td align="right">0.3%</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE _GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">777,390,430</td>
<td align="right">0.3%</td>
<td align="right">47.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _EXIT_TRACE</td>
<td align="right">753,240,845</td>
<td align="right">0.3%</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK _ITER_CHECK_RANGE</td>
<td align="right">713,750,068</td>
<td align="right">0.3%</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE _ITER_NEXT_RANGE</td>
<td align="right">706,397,789</td>
<td align="right">0.3%</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1 _GUARD_TYPE_VERSION</td>
<td align="right">679,665,960</td>
<td align="right">0.3%</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _EXIT_TRACE</td>
<td align="right">676,457,478</td>
<td align="right">0.3%</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT _BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">664,699,768</td>
<td align="right">0.3%</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1 _SAVE_RETURN_OFFSET</td>
<td align="right">652,736,239</td>
<td align="right">0.3%</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF _CHECK_VALIDITY</td>
<td align="right">648,361,577</td>
<td align="right">0.3%</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP _LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">638,100,023</td>
<td align="right">0.3%</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY _POP_TOP</td>
<td align="right">625,474,074</td>
<td align="right">0.3%</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR _POP_TOP</td>
<td align="right">619,615,733</td>
<td align="right">0.3%</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6 _LOAD_CONST_INLINE_BORROW</td>
<td align="right">588,292,135</td>
<td align="right">0.2%</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT _COMPARE_OP_INT</td>
<td align="right">582,844,081</td>
<td align="right">0.2%</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4 _SAVE_RETURN_OFFSET</td>
<td align="right">579,435,810</td>
<td align="right">0.2%</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP _LOAD_FAST_0</td>
<td align="right">578,658,751</td>
<td align="right">0.2%</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">_SET_IP _LOAD_DEREF</td>
<td align="right">573,458,535</td>
<td align="right">0.2%</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK _SET_IP</td>
<td align="right">561,627,478</td>
<td align="right">0.2%</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT _GUARD_IS_FALSE_POP</td>
<td align="right">557,853,308</td>
<td align="right">0.2%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">_YIELD_VALUE _YIELD_OFFSET</td>
<td align="right">554,293,148</td>
<td align="right">0.2%</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">_YIELD_OFFSET _DYNAMIC_EXIT</td>
<td align="right">554,293,148</td>
<td align="right">0.2%</td>
<td align="right">52.2%</td>
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
<td align="left">CALL</td>
<td align="right">148,207</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">46,483</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">44,622</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">38,683</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">10,522</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">7,858</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">5,705</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">3,065</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,700</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">2,298</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,980</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,660</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,599</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1,080</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">620</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">600</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">68</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">20</td>
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
<td align="right">1,086</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,086</td>
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
Stats gathered on: 2024-05-04
