
# Pystats results

- benchmark: regex_v8
- fork: brandtbucher
- ref: underflow-static-no-yield
- commit hash: bab095f
- commit date: 2024-08-26T23:09:22-07:00

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
<td align="left">LOAD_CONST</td>
<td align="right">9,557,540</td>
<td align="right">17.8%</td>
<td align="right">17.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,938,680</td>
<td align="right">12.9%</td>
<td align="right">30.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,891,620</td>
<td align="right">9.1%</td>
<td align="right">39.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,335,960</td>
<td align="right">8.1%</td>
<td align="right">47.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,165,800</td>
<td align="right">5.9%</td>
<td align="right">53.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,726,160</td>
<td align="right">5.1%</td>
<td align="right">58.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,634,380</td>
<td align="right">4.9%</td>
<td align="right">63.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,647,940</td>
<td align="right">3.1%</td>
<td align="right">66.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,627,080</td>
<td align="right">3.0%</td>
<td align="right">69.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,353,100</td>
<td align="right">2.5%</td>
<td align="right">72.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,288,560</td>
<td align="right">2.4%</td>
<td align="right">74.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,252,260</td>
<td align="right">2.3%</td>
<td align="right">77.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,041,000</td>
<td align="right">1.9%</td>
<td align="right">79.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">858,120</td>
<td align="right">1.6%</td>
<td align="right">80.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">847,200</td>
<td align="right">1.6%</td>
<td align="right">82.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">715,800</td>
<td align="right">1.3%</td>
<td align="right">83.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">618,520</td>
<td align="right">1.2%</td>
<td align="right">84.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">578,780</td>
<td align="right">1.1%</td>
<td align="right">85.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">532,640</td>
<td align="right">1.0%</td>
<td align="right">86.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">500,260</td>
<td align="right">0.9%</td>
<td align="right">87.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">493,560</td>
<td align="right">0.9%</td>
<td align="right">88.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">480,620</td>
<td align="right">0.9%</td>
<td align="right">89.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">451,760</td>
<td align="right">0.8%</td>
<td align="right">90.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">445,820</td>
<td align="right">0.8%</td>
<td align="right">91.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">301,500</td>
<td align="right">0.6%</td>
<td align="right">91.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">283,560</td>
<td align="right">0.5%</td>
<td align="right">92.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">280,740</td>
<td align="right">0.5%</td>
<td align="right">92.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">276,560</td>
<td align="right">0.5%</td>
<td align="right">93.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">273,820</td>
<td align="right">0.5%</td>
<td align="right">93.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">246,480</td>
<td align="right">0.5%</td>
<td align="right">94.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">206,820</td>
<td align="right">0.4%</td>
<td align="right">94.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">181,660</td>
<td align="right">0.3%</td>
<td align="right">95.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">179,080</td>
<td align="right">0.3%</td>
<td align="right">95.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">167,260</td>
<td align="right">0.3%</td>
<td align="right">95.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">167,200</td>
<td align="right">0.3%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">164,580</td>
<td align="right">0.3%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">94,260</td>
<td align="right">0.2%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">89,820</td>
<td align="right">0.2%</td>
<td align="right">96.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">89,560</td>
<td align="right">0.2%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">88,300</td>
<td align="right">0.2%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">84,960</td>
<td align="right">0.2%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">83,580</td>
<td align="right">0.2%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">82,040</td>
<td align="right">0.2%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">81,960</td>
<td align="right">0.2%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">81,480</td>
<td align="right">0.2%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">79,780</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">77,160</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">66,600</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">61,620</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">54,220</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">53,860</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">51,780</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">45,580</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">44,960</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">38,700</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">36,880</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">33,660</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">33,360</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">32,940</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">29,100</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">28,560</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">27,560</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">27,240</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">26,720</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">22,980</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">21,040</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">20,540</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">20,460</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">20,380</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">12,780</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">11,720</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">11,680</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,640</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">11,380</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">10,840</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">10,320</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">9,020</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,000</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,720</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">8,700</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">8,540</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">8,040</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">7,620</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">7,300</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">6,960</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">6,260</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">5,840</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">5,840</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">5,840</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">5,320</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,280</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5,280</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">5,160</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">4,760</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">4,660</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">4,500</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,440</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">4,300</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,180</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,100</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,480</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">3,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">2,900</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,600</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,380</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,280</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">980</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">940</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">800</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">600</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">40</td>
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
<td align="left">LOAD_GLOBAL_MODULE LOAD_CONST</td>
<td align="right">4,319,580</td>
<td align="right">8.0%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,280,980</td>
<td align="right">8.0%</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_GLOBAL_MODULE</td>
<td align="right">2,777,100</td>
<td align="right">5.2%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,214,920</td>
<td align="right">4.1%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL POP_TOP</td>
<td align="right">2,187,040</td>
<td align="right">4.1%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_CONST</td>
<td align="right">1,988,380</td>
<td align="right">3.7%</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_CONST</td>
<td align="right">1,747,980</td>
<td align="right">3.3%</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_GLOBAL_MODULE</td>
<td align="right">1,640,480</td>
<td align="right">3.1%</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT CALL_NON_PY_GENERAL</td>
<td align="right">1,479,340</td>
<td align="right">2.8%</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">1,040,740</td>
<td align="right">1.9%</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">1,013,400</td>
<td align="right">1.9%</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">832,380</td>
<td align="right">1.5%</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">811,880</td>
<td align="right">1.5%</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">756,320</td>
<td align="right">1.4%</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">687,420</td>
<td align="right">1.3%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST CALL_NON_PY_GENERAL</td>
<td align="right">686,400</td>
<td align="right">1.3%</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">682,940</td>
<td align="right">1.3%</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">533,540</td>
<td align="right">1.0%</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">531,840</td>
<td align="right">1.0%</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">518,340</td>
<td align="right">1.0%</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST</td>
<td align="right">512,500</td>
<td align="right">1.0%</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">511,060</td>
<td align="right">1.0%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">493,560</td>
<td align="right">0.9%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">491,760</td>
<td align="right">0.9%</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_CONST</td>
<td align="right">487,180</td>
<td align="right">0.9%</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE CALL_ISINSTANCE</td>
<td align="right">482,300</td>
<td align="right">0.9%</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">481,700</td>
<td align="right">0.9%</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST BUILD_TUPLE</td>
<td align="right">448,760</td>
<td align="right">0.8%</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">NOP LOAD_GLOBAL_MODULE</td>
<td align="right">446,460</td>
<td align="right">0.8%</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_TYPE_1</td>
<td align="right">445,760</td>
<td align="right">0.8%</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_NON_PY_GENERAL</td>
<td align="right">444,460</td>
<td align="right">0.8%</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL RETURN_VALUE</td>
<td align="right">444,020</td>
<td align="right">0.8%</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1 LOAD_FAST_LOAD_FAST</td>
<td align="right">444,020</td>
<td align="right">0.8%</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">443,920</td>
<td align="right">0.8%</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_GLOBAL_BUILTIN</td>
<td align="right">443,140</td>
<td align="right">0.8%</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE BINARY_SUBSCR_DICT</td>
<td align="right">441,200</td>
<td align="right">0.8%</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT RETURN_VALUE</td>
<td align="right">440,100</td>
<td align="right">0.8%</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT LOAD_GLOBAL_MODULE</td>
<td align="right">371,920</td>
<td align="right">0.7%</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">349,820</td>
<td align="right">0.7%</td>
<td align="right">73.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">328,560</td>
<td align="right">0.6%</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">308,040</td>
<td align="right">0.6%</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">296,140</td>
<td align="right">0.6%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">288,400</td>
<td align="right">0.5%</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">284,460</td>
<td align="right">0.5%</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">282,660</td>
<td align="right">0.5%</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">278,460</td>
<td align="right">0.5%</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL RESUME_CHECK</td>
<td align="right">276,500</td>
<td align="right">0.5%</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST</td>
<td align="right">267,740</td>
<td align="right">0.5%</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NONE</td>
<td align="right">267,680</td>
<td align="right">0.5%</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE LOAD_FAST</td>
<td align="right">264,500</td>
<td align="right">0.5%</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE NOP</td>
<td align="right">261,000</td>
<td align="right">0.5%</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">259,660</td>
<td align="right">0.5%</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR RETURN_VALUE</td>
<td align="right">257,120</td>
<td align="right">0.5%</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_GLOBAL_MODULE</td>
<td align="right">256,960</td>
<td align="right">0.5%</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR STORE_FAST</td>
<td align="right">253,440</td>
<td align="right">0.5%</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">IS_OP POP_JUMP_IF_FALSE</td>
<td align="right">243,420</td>
<td align="right">0.5%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE IS_OP</td>
<td align="right">241,060</td>
<td align="right">0.4%</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST NOP</td>
<td align="right">210,220</td>
<td align="right">0.4%</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_CONST</td>
<td align="right">207,280</td>
<td align="right">0.4%</td>
<td align="right">83.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE CALL_PY_EXACT_ARGS</td>
<td align="right">198,800</td>
<td align="right">0.4%</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST CALL_PY_GENERAL</td>
<td align="right">194,120</td>
<td align="right">0.4%</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST LOAD_FAST</td>
<td align="right">188,500</td>
<td align="right">0.4%</td>
<td align="right">84.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_LIST</td>
<td align="right">180,220</td>
<td align="right">0.3%</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">177,880</td>
<td align="right">0.3%</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">173,480</td>
<td align="right">0.3%</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST POP_JUMP_IF_FALSE</td>
<td align="right">172,620</td>
<td align="right">0.3%</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL</td>
<td align="right">171,340</td>
<td align="right">0.3%</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST</td>
<td align="right">170,040</td>
<td align="right">0.3%</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_GLOBAL_BUILTIN</td>
<td align="right">167,320</td>
<td align="right">0.3%</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST IMPORT_NAME</td>
<td align="right">167,260</td>
<td align="right">0.3%</td>
<td align="right">86.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST CALL_KW_NON_PY</td>
<td align="right">167,180</td>
<td align="right">0.3%</td>
<td align="right">87.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY POP_TOP</td>
<td align="right">167,120</td>
<td align="right">0.3%</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME STORE_FAST</td>
<td align="right">167,020</td>
<td align="right">0.3%</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_MODULE</td>
<td align="right">166,940</td>
<td align="right">0.3%</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE LOAD_CONST</td>
<td align="right">165,960</td>
<td align="right">0.3%</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST UNPACK_EX</td>
<td align="right">164,580</td>
<td align="right">0.3%</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">UNPACK_EX STORE_FAST_STORE_FAST</td>
<td align="right">164,580</td>
<td align="right">0.3%</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_LOAD_FAST</td>
<td align="right">164,540</td>
<td align="right">0.3%</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST</td>
<td align="right">142,180</td>
<td align="right">0.3%</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">132,420</td>
<td align="right">0.2%</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">POP_TOP ENTER_EXECUTOR</td>
<td align="right">129,860</td>
<td align="right">0.2%</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST PUSH_NULL</td>
<td align="right">125,400</td>
<td align="right">0.2%</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR RETURN_VALUE</td>
<td align="right">117,340</td>
<td align="right">0.2%</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT LOAD_CONST</td>
<td align="right">111,620</td>
<td align="right">0.2%</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE STORE_FAST</td>
<td align="right">88,420</td>
<td align="right">0.2%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST BINARY_SUBSCR</td>
<td align="right">83,800</td>
<td align="right">0.2%</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">81,720</td>
<td align="right">0.2%</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">76,940</td>
<td align="right">0.1%</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT CALL_PY_GENERAL</td>
<td align="right">73,320</td>
<td align="right">0.1%</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O POP_TOP</td>
<td align="right">72,220</td>
<td align="right">0.1%</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE BINARY_OP</td>
<td align="right">61,920</td>
<td align="right">0.1%</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST COMPARE_OP_STR</td>
<td align="right">57,380</td>
<td align="right">0.1%</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR POP_JUMP_IF_FALSE</td>
<td align="right">56,620</td>
<td align="right">0.1%</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST POP_TOP</td>
<td align="right">54,220</td>
<td align="right">0.1%</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT POP_JUMP_IF_FALSE</td>
<td align="right">54,060</td>
<td align="right">0.1%</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS POP_TOP</td>
<td align="right">53,580</td>
<td align="right">0.1%</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST</td>
<td align="right">52,440</td>
<td align="right">0.1%</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR POP_TOP</td>
<td align="right">52,080</td>
<td align="right">0.1%</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP TO_BOOL_INT</td>
<td align="right">51,620</td>
<td align="right">0.1%</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">51,080</td>
<td align="right">0.1%</td>
<td align="right">92.6%</td>
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
<td align="right">4,160</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">300</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">40</td>
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
<td align="right">3,560</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">340</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">180</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">180</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">120</td>
<td align="right">2.7%</td>
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
<td align="right">400</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">40</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">280</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">9.1%</td>
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
<td align="right">282,660</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">25,240</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">240</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">160</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">140</td>
<td align="right">0.0%</td>
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
<td align="right">83,800</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">4,300</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">140</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">20</td>
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
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">41,080</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">21,480</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">16,180</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">4,120</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,880</td>
<td align="right">3.3%</td>
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
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">3,360</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,080</td>
<td align="right">24.3%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">4,440</td>
<td align="right">100.0%</td>
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
<td align="right">5,840</td>
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
<td align="right">5,840</td>
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
<td align="right">140</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60</td>
<td align="right">30.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">80</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">60</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">60</td>
<td align="right">30.0%</td>
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
<td align="right">6,960</td>
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
<td align="right">6,960</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,240</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,320</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">80</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">20</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">4,600</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">60</td>
<td align="right">1.3%</td>
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
<td align="right">40,060</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,000</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,400</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">4,120</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,820</td>
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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">32,940</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">27,820</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">9,860</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">7,520</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,840</td>
<td align="right">3.5%</td>
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
<td align="right">296,140</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">5,140</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">220</td>
<td align="right">0.1%</td>
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
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">20</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">60</td>
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
<td align="right">40</td>
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
<td align="right">40</td>
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
<td align="right">1,160</td>
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
<td align="right">480</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">460</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">80</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">3.4%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">261,000</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">210,220</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">10,300</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,580</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,820</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">446,460</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">36,820</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,520</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,420</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,820</td>
<td align="right">0.4%</td>
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
<td align="right">2,820</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,820</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">200</td>
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
<td align="left">JUMP_FORWARD</td>
<td align="right">2,820</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">2,820</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">160</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">40</td>
<td align="right">0.7%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,187,040</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">533,540</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">167,120</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">72,220</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">54,220</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,777,100</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">129,860</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">81,720</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">48,440</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">42,440</td>
<td align="right">1.3%</td>
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
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,980</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,820</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">40</td>
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
<td align="right">5,840</td>
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
<td align="right">481,700</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">125,400</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">6,800</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,080</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,060</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">487,180</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">76,940</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">31,240</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,640</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">8,980</td>
<td align="right">1.5%</td>
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
<td align="right">120</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">20</td>
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
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">120</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">20</td>
<td align="right">14.3%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">444,020</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">440,100</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">259,660</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">257,120</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">117,340</td>
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
<td align="left">POP_TOP</td>
<td align="right">533,540</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">443,920</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">296,140</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">259,660</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">51,080</td>
<td align="right">3.1%</td>
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
<td align="right">2,300</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">840</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">720</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">160</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">80</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">2,280</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">940</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">360</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">180</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">100</td>
<td align="right">2.4%</td>
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
<td align="right">171,340</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,920</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,940</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">1,720</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">640</td>
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
<td align="right">173,480</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,660</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">640</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">140</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">60</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,960</td>
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
<td align="right">1,960</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">180</td>
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
<td align="right">180</td>
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
<td align="right">4,880</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">3,840</td>
<td align="right">44.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">4,880</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,840</td>
<td align="right">44.0%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">61,920</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,200</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,540</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,000</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,820</td>
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
<td align="left">TO_BOOL_INT</td>
<td align="right">51,620</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,480</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,860</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,920</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,900</td>
<td align="right">3.5%</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">9,220</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,080</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,180</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,420</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">960</td>
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
<td align="left">STORE_FAST</td>
<td align="right">18,680</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,880</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,500</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">900</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">180</td>
<td align="right">0.7%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">5,640</td>
<td align="right">90.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">160</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">100</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">60</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">60</td>
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
<td align="right">5,800</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">160</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">80</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60</td>
<td align="right">1.0%</td>
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
<td align="right">60</td>
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
<td align="right">60</td>
<td align="right">100.0%</td>
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
<td align="right">4,300</td>
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
<td align="left">BINARY_SUBSCR</td>
<td align="right">4,300</td>
<td align="right">100.0%</td>
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
<td align="right">1,220</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">60</td>
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
<td align="right">1,120</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">80</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">20</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">20</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">20</td>
<td align="right">1.6%</td>
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
<td align="right">448,760</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">8,760</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,680</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,420</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,860</td>
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
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">441,200</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,780</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,200</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">5,700</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,640</td>
<td align="right">0.8%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">17,560</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">16,180</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">16,160</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">940</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">760</td>
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
<td align="left">POP_TOP</td>
<td align="right">21,620</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">20,920</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,380</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,100</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,300</td>
<td align="right">2.4%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">480</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">240</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">140</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">80</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">60</td>
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
<td align="left">GET_ITER</td>
<td align="right">480</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">200</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">160</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">80</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">80</td>
<td align="right">7.7%</td>
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
<td align="right">140</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">20</td>
<td align="right">12.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">80</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">60</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">20</td>
<td align="right">12.5%</td>
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
<td align="right">80</td>
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
<td align="right">20</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">20</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">20</td>
<td align="right">25.0%</td>
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
<td align="right">5,800</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,140</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">300</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">160</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">160</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">6,280</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,340</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">160</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">160</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">60</td>
<td align="right">0.7%</td>
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
<td align="right">14,920</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,780</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">140</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">40</td>
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
<td align="right">17,200</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">5,560</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">140</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">40</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">20</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,900</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,600</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,880</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,280</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,040</td>
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
<td align="left">TO_BOOL_STR</td>
<td align="right">9,760</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">6,580</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,980</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,080</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,060</td>
<td align="right">3.9%</td>
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
<td align="right">240</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">120</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">80</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">80</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">60</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">420</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">120</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">60</td>
<td align="right">10.0%</td>
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
<td align="left">POP_TOP</td>
<td align="right">40</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">20</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
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
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">20</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">20</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">20</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">20</td>
<td align="right">25.0%</td>
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
<td align="right">160</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">80</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">240</td>
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
<td align="right">20</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">20</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">20</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">20</td>
<td align="right">50.0%</td>
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
<td align="right">27,820</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">10,740</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">9,920</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,420</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,220</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">30,200</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">16,560</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">9,820</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,300</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">7,280</td>
<td align="right">9.1%</td>
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
<td align="left">EXTENDED_ARG</td>
<td align="right">9,300</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">7,520</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,000</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">540</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">120</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,240</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,820</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,740</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,740</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,260</td>
<td align="right">6.1%</td>
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
<td align="right">80</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">20</td>
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
<td align="right">100</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">167,260</td>
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
<td align="right">167,020</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">140</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">20</td>
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
<td align="right">241,060</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,460</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,800</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">243,420</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,960</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">100</td>
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
<td align="right">42,440</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,620</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">480</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">400</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">340</td>
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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">38,620</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">5,940</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,000</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,360</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,140</td>
<td align="right">2.2%</td>
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
<td align="right">160</td>
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
<td align="right">160</td>
<td align="right">100.0%</td>
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
<td align="right">11,460</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,980</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">7,280</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,540</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,840</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">17,140</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">11,380</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,660</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,900</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">960</td>
<td align="right">2.5%</td>
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
<td align="left">BUILD_TUPLE</td>
<td align="right">560</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">240</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">180</td>
<td align="right">18.4%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">640</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">340</td>
<td align="right">34.7%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">120</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">80</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">23.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">140</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">40</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20</td>
<td align="right">7.7%</td>
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
<td align="right">518,340</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">21,480</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">21,460</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,620</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,760</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">257,120</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">253,440</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">21,720</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">19,240</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,660</td>
<td align="right">1.2%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,319,580</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,988,380</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,747,980</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">487,180</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">207,280</td>
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
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,280,980</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,747,980</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,640,480</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">686,400</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">194,120</td>
<td align="right">2.0%</td>
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
<td align="right">260</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">240</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">160</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">140</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">140</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">360</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">280</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">200</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">140</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">80</td>
<td align="right">5.8%</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,013,400</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">811,880</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">756,320</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">349,820</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">308,040</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">832,380</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">682,940</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">518,340</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">445,760</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">444,460</td>
<td align="right">9.1%</td>
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
<td align="right">920</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">20</td>
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
<td align="left">SWAP</td>
<td align="right">920</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">20</td>
<td align="right">2.1%</td>
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
<td align="right">1,320</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">280</td>
<td align="right">17.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,320</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">260</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">20</td>
<td align="right">1.2%</td>
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
<td align="right">512,500</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">444,020</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">164,540</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">27,840</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">13,880</td>
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
<td align="right">493,560</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">448,760</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">177,880</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">35,900</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">18,560</td>
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
<td align="left">POP_TOP</td>
<td align="right">48,440</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">30,220</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,880</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,880</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,720</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">45,580</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">42,320</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,760</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,400</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">380</td>
<td align="right">0.4%</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">3,060</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">2,380</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,140</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,120</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">960</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">3,500</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">3,060</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,080</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,080</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,060</td>
<td align="right">9.1%</td>
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
<td align="right">480</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">480</td>
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
<td align="right">480</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">240</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">160</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">60</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
<td align="right">2.1%</td>
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
<td align="right">220</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">120</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">60</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">40</td>
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
<td align="left">MAKE_CELL</td>
<td align="right">220</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">160</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">60</td>
<td align="right">13.6%</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">680</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">340</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">640</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">340</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">20</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">20</td>
<td align="right">2.0%</td>
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
<td align="right">511,060</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">243,420</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">173,480</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">172,620</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">56,620</td>
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
<td align="right">811,880</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">261,000</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">170,040</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">29,160</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">26,520</td>
<td align="right">2.0%</td>
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
<td align="right">267,680</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,280</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,720</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">120</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">264,500</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,660</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,720</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">580</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">360</td>
<td align="right">0.1%</td>
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
<td align="right">278,460</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,420</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">440</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">260</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">267,740</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,540</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,160</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,340</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,320</td>
<td align="right">0.5%</td>
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
<td align="left">TO_BOOL_INT</td>
<td align="right">18,220</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">18,120</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">10,020</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">5,140</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,660</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">28,380</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">9,620</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,620</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,920</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,360</td>
<td align="right">5.5%</td>
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
<td align="left">POP_TOP</td>
<td align="right">21,460</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,780</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">14,200</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,240</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">3,820</td>
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
<td align="right">54,220</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">9,840</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">6,960</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,180</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">5,140</td>
<td align="right">6.3%</td>
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
<td align="right">460</td>
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
<td align="right">200</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">120</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">100</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">20</td>
<td align="right">4.3%</td>
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
<td align="right">460</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">340</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">80</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">40</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">360</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">180</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">120</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">80</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">80</td>
<td align="right">8.7%</td>
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
<td align="left">STORE_DEREF</td>
<td align="right">80</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">40</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">20</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">20</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">120</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">80</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">80</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20</td>
<td align="right">6.2%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">253,440</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">167,020</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">88,420</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">51,080</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">48,120</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">349,820</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">210,220</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">132,420</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">47,660</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">39,120</td>
<td align="right">4.6%</td>
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
<td align="left">CALL_LEN</td>
<td align="right">6,800</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">800</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">20</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">6,800</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">560</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">240</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">20</td>
<td align="right">0.3%</td>
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
<td align="left">UNPACK_EX</td>
<td align="right">164,580</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">31,720</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,580</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3,520</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">360</td>
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
<td align="right">188,500</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,180</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,160</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,820</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">900</td>
<td align="right">0.4%</td>
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
<td align="right">1,900</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,120</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">720</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">480</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">300</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">2,520</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">2,380</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">100</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">80</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">40</td>
<td align="right">0.8%</td>
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
<td align="right">1,240</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">920</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">900</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">620</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">480</td>
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
<td align="left">COPY</td>
<td align="right">1,100</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">900</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">700</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">700</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">620</td>
<td align="right">11.7%</td>
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
<td align="right">164,580</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">164,580</td>
<td align="right">100.0%</td>
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
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">20</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">20</td>
<td align="right">33.3%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">120</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">80</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">20</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">220</td>
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
<td align="right">480</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">160</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">60</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">60</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40</td>
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
<td align="left">LOAD_GLOBAL</td>
<td align="right">360</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">120</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">100</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">100</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">60</td>
<td align="right">7.5%</td>
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
<td align="right">40,280</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,280</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">400</td>
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
<td align="right">20,160</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,140</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,060</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">980</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">740</td>
<td align="right">1.6%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">3,080</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">360</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">220</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">120</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">120</td>
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
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,200</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">800</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">800</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">380</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">380</td>
<td align="right">9.7%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">2,580</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">400</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">40</td>
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
<td align="right">1,600</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">980</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">400</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">40</td>
<td align="right">1.3%</td>
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
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">20</td>
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
<td align="right">60</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">11,040</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">9,680</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,360</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">9,680</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,220</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,520</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,020</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,920</td>
<td align="right">10.0%</td>
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
<td align="left">BUILD_TUPLE</td>
<td align="right">441,200</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,080</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,280</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">440,100</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,860</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,080</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">2,980</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,300</td>
<td align="right">0.3%</td>
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
<td align="right">6,760</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,080</td>
<td align="right">37.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">10,840</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">4,280,980</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">41,080</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">8,420</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,480</td>
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
<td align="right">2,214,920</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,479,340</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">371,920</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">111,620</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">73,320</td>
<td align="right">1.7%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">17,520</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,780</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,300</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">60</td>
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
<td align="right">13,640</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,840</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,360</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">2,820</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,940</td>
<td align="right">5.8%</td>
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
<td align="right">20,360</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">6,260</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,700</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,460</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,220</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,880</td>
<td align="right">9.2%</td>
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
<td align="right">9,840</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,820</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">120</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,860</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,920</td>
<td align="right">46.3%</td>
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
<td align="left">BUILD_TUPLE</td>
<td align="right">9,780</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">8,980</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,300</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,480</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">28,540</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">37,160</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">5,620</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,280</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">680</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">320</td>
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
<td align="left">GET_ITER</td>
<td align="right">40,060</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,120</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">680</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">440</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">180</td>
<td align="right">0.4%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">920</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">620</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">120</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">100</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">80</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">680</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">440</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">340</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">180</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">160</td>
<td align="right">8.1%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,280</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">2,820</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,820</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">400</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">200</td>
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
<td align="right">3,160</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,180</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,640</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,640</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">80</td>
<td align="right">0.9%</td>
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
<td align="right">48,400</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">12,440</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,760</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">6,260</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">3,860</td>
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
<td align="left">POP_TOP</td>
<td align="right">72,220</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,760</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,960</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,820</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">40</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">482,300</td>
<td align="right">96.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,580</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,700</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,440</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,720</td>
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
<td align="right">491,760</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,640</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,820</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">40</td>
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
<td align="right">167,180</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
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
<td align="left">POP_TOP</td>
<td align="right">167,120</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">140</td>
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
<td align="right">140</td>
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
<td align="right">39,940</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">26,640</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,620</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,640</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60</td>
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
<td align="right">26,400</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">10,540</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">9,680</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,780</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">6,800</td>
<td align="right">8.3%</td>
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
<td align="right">14,120</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,760</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,400</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,680</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">14,200</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,360</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,240</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">980</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">180</td>
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
<td align="right">5,360</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,140</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,260</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,140</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">460</td>
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
<td align="right">10,560</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">380</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">240</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">120</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">120</td>
<td align="right">1.0%</td>
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
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">27,840</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">25,120</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">700</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">180</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
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
<td align="left">POP_TOP</td>
<td align="right">53,580</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">180</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">20</td>
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
<td align="right">3,400</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">60</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
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
<td align="left">GET_ITER</td>
<td align="right">2,820</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">540</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">40</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">20</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">4,100</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,500</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,080</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">920</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">640</td>
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
<td align="left">POP_TOP</td>
<td align="right">6,560</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">940</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">640</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">360</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">220</td>
<td align="right">2.4%</td>
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
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,479,340</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">686,400</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">444,460</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20,920</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,260</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">2,187,040</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">444,020</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,240</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">320</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">493,560</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">288,400</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">198,800</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">32,180</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,980</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,040,740</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">20</td>
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
<td align="right">194,120</td>
<td align="right">70.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">73,320</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,980</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,720</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,100</td>
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
<td align="right">276,500</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">60</td>
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
<td align="right">200</td>
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
<td align="right">120</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">60</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">20</td>
<td align="right">10.0%</td>
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
<td align="right">2,820</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">60</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">20</td>
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
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,820</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">60</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20</td>
<td align="right">0.7%</td>
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
<td align="right">445,760</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">444,020</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,720</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">60</td>
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
<td align="right">60</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">14,380</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,240</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,000</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,420</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,060</td>
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
<td align="right">26,280</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">340</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">40</td>
<td align="right">0.1%</td>
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
<td align="right">57,380</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,800</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,160</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">160</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">100</td>
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
<td align="right">56,620</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9,920</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">60</td>
<td align="right">0.1%</td>
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
<td align="right">7,080</td>
<td align="right">82.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,220</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">160</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">40</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
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
<td align="right">8,100</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">360</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">80</td>
<td align="right">0.9%</td>
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
<td align="right">19,200</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,720</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">20,460</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">10,740</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,740</td>
<td align="right">5.3%</td>
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
<td align="right">9,860</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9,820</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">720</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">60</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">14,320</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,680</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">220</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">160</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">40</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">38,620</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">32,940</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">16,560</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,260</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">180</td>
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
<td align="right">88,420</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">480</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">420</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">220</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">2,840</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,140</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">700</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">60</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20</td>
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
<td align="right">2,120</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,120</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">800</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">240</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">240</td>
<td align="right">5.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">20</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">20</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">20</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20</td>
<td align="right">33.3%</td>
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
<td align="right">5,160</td>
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
<td align="right">1,720</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,720</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,720</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">682,940</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">18,560</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,880</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">284,460</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">267,680</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">34,500</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">26,640</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">16,120</td>
<td align="right">2.3%</td>
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
<td align="right">60</td>
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
<td align="right">60</td>
<td align="right">100.0%</td>
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
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,214,920</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">443,920</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">21,720</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">16,480</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">16,120</td>
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
<td align="right">1,988,380</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">308,040</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">256,960</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">164,540</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,400</td>
<td align="right">0.1%</td>
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
<td align="right">33,000</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,880</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,600</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">320</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">80</td>
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
<td align="right">32,180</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,040</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">940</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">620</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">100</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">687,420</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">166,940</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">3,760</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">481,700</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">198,800</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">165,960</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,900</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,520</td>
<td align="right">0.2%</td>
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
<td align="right">5,580</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,420</td>
<td align="right">38.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">9,000</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,440</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">320</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">280</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
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
<td align="left">CALL_ISINSTANCE</td>
<td align="right">3,440</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">220</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">220</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">80</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">60</td>
<td align="right">1.5%</td>
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
<td align="right">531,840</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">443,140</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">167,320</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">34,620</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">28,340</td>
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
<td align="right">1,013,400</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">207,280</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,340</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,660</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,340</td>
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
<td align="left">POP_TOP</td>
<td align="right">2,777,100</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,640,480</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">832,380</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">446,460</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">371,920</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">4,319,580</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">687,420</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">512,500</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">482,300</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">443,140</td>
<td align="right">6.4%</td>
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
<td align="right">160</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">160</td>
<td align="right">100.0%</td>
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
<td align="right">1,040,740</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">282,660</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">276,500</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">28,540</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,000</td>
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
<td align="right">756,320</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">531,840</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">328,560</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,600</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">9,220</td>
<td align="right">0.6%</td>
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
<td align="right">45,980</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">35,900</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,740</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">180</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">160</td>
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
<td align="right">27,840</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">20,780</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">12,620</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,960</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">5,640</td>
<td align="right">6.6%</td>
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
<td align="right">80</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">20</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">140</td>
<td align="right">100.0%</td>
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
<td align="right">5,860</td>
<td align="right">80.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">1,200</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">160</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">80</td>
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
<td align="right">2,940</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,820</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">960</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">320</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">160</td>
<td align="right">2.2%</td>
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
<td align="right">8,740</td>
<td align="right">84.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,580</td>
<td align="right">15.3%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">6,120</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">3,820</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">160</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">140</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">80</td>
<td align="right">0.8%</td>
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
<td align="right">491,760</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">9,840</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">7,660</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,360</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">5,960</td>
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
<td align="right">511,060</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">18,120</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,460</td>
<td align="right">0.6%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">51,620</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,520</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,080</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">760</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">80</td>
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
<td align="right">54,060</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">18,220</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,880</td>
<td align="right">6.3%</td>
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
<td align="right">180,220</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,420</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">172,620</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,140</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">3,840</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">60</td>
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
<td align="right">10,760</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">840</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">60</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">60</td>
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
<td align="right">11,660</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">40</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="left">COPY</td>
<td align="right">9,760</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,360</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">240</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">20</td>
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
<td align="right">10,020</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,360</td>
<td align="right">12.0%</td>
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
<td align="right">3,040</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,960</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">140</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">120</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">20</td>
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
<td align="right">3,520</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,740</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20</td>
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
<td align="right">14,320</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,860</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">8,240</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,340</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">340</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">31,720</td>
<td align="right">95.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,640</td>
<td align="right">4.9%</td>
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
<td align="right">129,860</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">39,120</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">29,160</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">28,100</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">25,240</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">117,340</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">52,080</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">28,100</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,760</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">14,280</td>
<td align="right">5.0%</td>
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
<td align="right">82,080</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">178,260</td>
<td align="right">68.1%</td>
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
<td align="right">280</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,220</td>
<td align="right">81.3%</td>
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
<td align="left">and int</td>
<td align="right">600</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">240</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">120</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">80</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">80</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">80</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">20</td>
<td align="right">1.6%</td>
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
<td align="right">47,100</td>
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
<td align="right">21,931,020</td>
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
<td align="right">10,000</td>
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
<td align="right">41,380</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
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
<td align="left">other</td>
<td align="right">20</td>
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
<td align="right">27,700</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,727,820</td>
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
<td align="right">1,440</td>
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
<td align="right">26,560</td>
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
<td align="right">60</td>
<td align="right">75.0%</td>
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
<td align="right">7,660</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">160,100</td>
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
<td align="right">2,760</td>
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
<td align="right">220</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">220</td>
<td align="right">50.0%</td>
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
<td align="right">100</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">40</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">20</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">20</td>
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
<td align="right">22,780</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">122,620</td>
<td align="right">84.2%</td>
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
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">140</td>
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
<td align="left">str</td>
<td align="right">120</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">20</td>
<td align="right">14.3%</td>
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
<td align="right">18,620</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">113,660</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,120</td>
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
<td align="right">1,380</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">560</td>
<td align="right">28.9%</td>
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
<td align="left">itertools</td>
<td align="right">160</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">140</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">120</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">80</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">40</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">20</td>
<td align="right">3.6%</td>
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
<td align="right">547,460</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,797,780</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">140</td>
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
<td align="right">30,660</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">660</td>
<td align="right">2.1%</td>
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
<td align="right">220</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">160</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">140</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">100</td>
<td align="right">15.2%</td>
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
<td align="right">47,280</td>
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
<td align="right">9,458,160</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,440</td>
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
<td align="right">47,440</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">160</td>
<td align="right">100.0%</td>
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
<td align="right">660</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">168,100</td>
<td align="right">99.5%</td>
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
<td align="right">180</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">80</td>
<td align="right">30.8%</td>
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
<td align="left">overridden</td>
<td align="right">60</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">20</td>
<td align="right">25.0%</td>
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
<td align="right">4,020</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">26,040</td>
<td align="right">86.2%</td>
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
<td align="right">80</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">80</td>
<td align="right">50.0%</td>
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
<td align="right">60</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">20</td>
<td align="right">25.0%</td>
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
<td align="right">178,140</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,801,560</td>
<td align="right">93.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,440</td>
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
<td align="right">360</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">680</td>
<td align="right">65.4%</td>
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
<td align="right">260</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">200</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">100</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">80</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">40</td>
<td align="right">5.9%</td>
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
<td align="right">40</td>
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
<td align="right">130,200</td>
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
<td align="right">20</td>
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
<td align="right">24,788,180</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">3,109,240</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">25,766,860</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">44,340</td>
<td align="right">0.1%</td>
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
<td align="right">547,460</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">178,140</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">82,080</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">47,280</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">47,100</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">27,700</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">22,780</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">18,620</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">7,660</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,020</td>
<td align="right">0.4%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">25,000</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,120</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,020</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,880</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,760</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,120</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">700</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">440</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">360</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">300</td>
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
<td align="right">308,480</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,040,800</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">308,480</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">308,120</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">307,980</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">46,860</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">775,720</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">4,364,740</td>
<td align="right">100.4%</td>
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
<td align="right">9,852,540</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">9,855,360</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">50,278,060</td>
<td align="right">83.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">49,914,260</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">317,320</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">46,480</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">70,342,298</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">17,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">27,984,640</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">43,721,504</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">157,104,795</td>
<td align="right">84.9%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">176,572,233</td>
<td align="right">80.2%</td>
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
<td align="right">1,398,317</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,503</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,610</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">6,359,779</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">561</td>
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
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">2</td>
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
<td align="right">4,160</td>
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
<td align="right">3,800</td>
<td align="right">91.3%</td>
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
<td align="right">380</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">320</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">360</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">340</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">260</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">1,095,060</td>
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
<td align="right">341,898,300</td>
<td align="right">31,221.9%</td>
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
<td align="right">3,800</td>
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
<td align="right">3,240</td>
<td align="right">85.3%</td>
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
<td align="right">560</td>
<td align="right">14.7%</td>
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
<td align="right">20</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">20</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">840</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">960</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">620</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">680</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">320</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">320</td>
<td align="right">8.4%</td>
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
<td align="right">20</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">40</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">60</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">880</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">700</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">780</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">340</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">420</td>
<td align="right">11.1%</td>
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
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">30,717,980</td>
<td align="right">9.0%</td>
<td align="right">9.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">30,151,240</td>
<td align="right">8.8%</td>
<td align="right">17.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">28,656,660</td>
<td align="right">8.4%</td>
<td align="right">26.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">22,797,200</td>
<td align="right">6.7%</td>
<td align="right">32.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">17,461,040</td>
<td align="right">5.1%</td>
<td align="right">38.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">15,698,360</td>
<td align="right">4.6%</td>
<td align="right">42.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">13,776,440</td>
<td align="right">4.0%</td>
<td align="right">46.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">13,342,780</td>
<td align="right">3.9%</td>
<td align="right">50.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">13,157,400</td>
<td align="right">3.8%</td>
<td align="right">54.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">13,021,380</td>
<td align="right">3.8%</td>
<td align="right">58.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">13,021,380</td>
<td align="right">3.8%</td>
<td align="right">61.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">11,599,400</td>
<td align="right">3.4%</td>
<td align="right">65.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">8,850,820</td>
<td align="right">2.6%</td>
<td align="right">67.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">8,850,820</td>
<td align="right">2.6%</td>
<td align="right">70.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">8,803,220</td>
<td align="right">2.6%</td>
<td align="right">73.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">8,760,660</td>
<td align="right">2.6%</td>
<td align="right">75.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">8,708,780</td>
<td align="right">2.5%</td>
<td align="right">78.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">7,832,720</td>
<td align="right">2.3%</td>
<td align="right">80.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">4,238,520</td>
<td align="right">1.2%</td>
<td align="right">81.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">4,210,800</td>
<td align="right">1.2%</td>
<td align="right">83.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,703,120</td>
<td align="right">0.8%</td>
<td align="right">83.8%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,657,600</td>
<td align="right">0.8%</td>
<td align="right">84.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,649,200</td>
<td align="right">0.8%</td>
<td align="right">85.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,625,320</td>
<td align="right">0.8%</td>
<td align="right">86.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,625,200</td>
<td align="right">0.8%</td>
<td align="right">86.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,625,040</td>
<td align="right">0.8%</td>
<td align="right">87.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,514,840</td>
<td align="right">0.7%</td>
<td align="right">88.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,826,480</td>
<td align="right">0.5%</td>
<td align="right">88.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">1,554,340</td>
<td align="right">0.5%</td>
<td align="right">89.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,429,500</td>
<td align="right">0.4%</td>
<td align="right">89.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,408,900</td>
<td align="right">0.4%</td>
<td align="right">90.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,396,860</td>
<td align="right">0.4%</td>
<td align="right">90.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,352,280</td>
<td align="right">0.4%</td>
<td align="right">91.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">1,341,040</td>
<td align="right">0.4%</td>
<td align="right">91.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,332,680</td>
<td align="right">0.4%</td>
<td align="right">91.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,328,860</td>
<td align="right">0.4%</td>
<td align="right">92.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,313,160</td>
<td align="right">0.4%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">1,301,020</td>
<td align="right">0.4%</td>
<td align="right">92.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,286,280</td>
<td align="right">0.4%</td>
<td align="right">93.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,265,300</td>
<td align="right">0.4%</td>
<td align="right">93.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,256,360</td>
<td align="right">0.4%</td>
<td align="right">94.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,215,760</td>
<td align="right">0.4%</td>
<td align="right">94.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,154,140</td>
<td align="right">0.3%</td>
<td align="right">94.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,131,920</td>
<td align="right">0.3%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">1,095,060</td>
<td align="right">0.3%</td>
<td align="right">95.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">1,053,260</td>
<td align="right">0.3%</td>
<td align="right">95.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">1,029,560</td>
<td align="right">0.3%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">1,029,560</td>
<td align="right">0.3%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALLER_IP</td>
<td align="right">780,940</td>
<td align="right">0.2%</td>
<td align="right">96.5%</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">759,180</td>
<td align="right">0.2%</td>
<td align="right">96.7%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">703,040</td>
<td align="right">0.2%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">636,580</td>
<td align="right">0.2%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">618,900</td>
<td align="right">0.2%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">613,400</td>
<td align="right">0.2%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">595,200</td>
<td align="right">0.2%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">593,420</td>
<td align="right">0.2%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">590,660</td>
<td align="right">0.2%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">585,340</td>
<td align="right">0.2%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">584,220</td>
<td align="right">0.2%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">582,940</td>
<td align="right">0.2%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">581,660</td>
<td align="right">0.2%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">581,660</td>
<td align="right">0.2%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">406,300</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">226,840</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">218,800</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">218,800</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">197,100</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">130,120</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">124,440</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">124,440</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">110,220</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">89,660</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">87,500</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">83,000</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">83,000</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">78,020</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">75,200</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">71,480</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">69,980</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">69,380</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">65,840</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">63,780</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">60,880</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">60,440</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">58,740</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">56,080</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">55,640</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">50,000</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">49,880</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">49,020</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">49,020</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">48,380</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">46,140</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">45,880</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">38,200</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">37,060</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">36,820</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">32,760</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">32,640</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">32,640</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">32,640</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">32,400</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">29,240</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">29,240</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">28,060</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">23,860</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">19,920</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">18,280</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">17,040</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">16,280</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">15,720</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">15,300</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">13,740</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">13,340</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">12,520</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">11,600</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">10,460</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">10,140</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">10,060</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">9,400</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_INIT_CHECK</td>
<td align="right">8,860</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,560</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">7,700</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">7,700</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">7,620</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">6,820</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">6,800</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">5,960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">5,300</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">5,100</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">4,800</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">4,260</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">3,940</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">3,260</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">3,120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">3,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">3,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">2,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,360</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">2,340</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,900</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,900</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,900</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,720</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,260</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">1,160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">1,160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">800</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">540</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">540</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">20</td>
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
<td align="right">20</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">20</td>
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
<td align="right">20</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-08-27
