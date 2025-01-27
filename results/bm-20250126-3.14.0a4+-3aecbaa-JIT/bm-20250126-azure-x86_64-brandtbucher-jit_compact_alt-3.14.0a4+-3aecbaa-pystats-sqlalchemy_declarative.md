
# Pystats results

- benchmark: sqlalchemy_declarative
- fork: brandtbucher
- ref: jit-compact-alt
- commit hash: 3aecbaa
- commit date: 2025-01-26T20:12:27-08:00

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
<td align="right">33,218,248</td>
<td align="right">17.4%</td>
<td align="right">17.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">7,876,020</td>
<td align="right">4.1%</td>
<td align="right">21.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,755,452</td>
<td align="right">4.1%</td>
<td align="right">25.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,736,940</td>
<td align="right">4.1%</td>
<td align="right">29.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,463,960</td>
<td align="right">3.9%</td>
<td align="right">33.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,418,920</td>
<td align="right">3.4%</td>
<td align="right">37.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,085,940</td>
<td align="right">2.7%</td>
<td align="right">39.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,030,460</td>
<td align="right">2.6%</td>
<td align="right">42.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,912,485</td>
<td align="right">2.6%</td>
<td align="right">44.9%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,744,860</td>
<td align="right">2.5%</td>
<td align="right">47.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,713,300</td>
<td align="right">2.5%</td>
<td align="right">49.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,554,224</td>
<td align="right">2.4%</td>
<td align="right">52.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,974,400</td>
<td align="right">2.1%</td>
<td align="right">54.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">3,605,120</td>
<td align="right">1.9%</td>
<td align="right">56.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,590,620</td>
<td align="right">1.9%</td>
<td align="right">58.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,525,660</td>
<td align="right">1.9%</td>
<td align="right">60.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,491,200</td>
<td align="right">1.8%</td>
<td align="right">61.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,099,600</td>
<td align="right">1.6%</td>
<td align="right">63.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">3,098,820</td>
<td align="right">1.6%</td>
<td align="right">65.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">3,045,736</td>
<td align="right">1.6%</td>
<td align="right">66.7%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,981,816</td>
<td align="right">1.6%</td>
<td align="right">68.2%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,893,360</td>
<td align="right">1.5%</td>
<td align="right">69.7%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,581,080</td>
<td align="right">1.4%</td>
<td align="right">71.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,501,260</td>
<td align="right">1.3%</td>
<td align="right">72.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,355,000</td>
<td align="right">1.2%</td>
<td align="right">73.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,348,660</td>
<td align="right">1.2%</td>
<td align="right">74.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,264,080</td>
<td align="right">1.2%</td>
<td align="right">76.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,204,140</td>
<td align="right">1.2%</td>
<td align="right">77.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,192,060</td>
<td align="right">1.2%</td>
<td align="right">78.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,035,700</td>
<td align="right">1.1%</td>
<td align="right">79.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">2,006,280</td>
<td align="right">1.1%</td>
<td align="right">80.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,986,460</td>
<td align="right">1.0%</td>
<td align="right">81.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,914,300</td>
<td align="right">1.0%</td>
<td align="right">82.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,747,720</td>
<td align="right">0.9%</td>
<td align="right">83.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,640,356</td>
<td align="right">0.9%</td>
<td align="right">84.3%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,624,680</td>
<td align="right">0.9%</td>
<td align="right">85.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,465,680</td>
<td align="right">0.8%</td>
<td align="right">86.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,435,380</td>
<td align="right">0.8%</td>
<td align="right">86.7%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,358,880</td>
<td align="right">0.7%</td>
<td align="right">87.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,343,760</td>
<td align="right">0.7%</td>
<td align="right">88.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,281,760</td>
<td align="right">0.7%</td>
<td align="right">88.8%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,139,860</td>
<td align="right">0.6%</td>
<td align="right">89.4%</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">1,123,444</td>
<td align="right">0.6%</td>
<td align="right">90.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,099,300</td>
<td align="right">0.6%</td>
<td align="right">90.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,058,820</td>
<td align="right">0.6%</td>
<td align="right">91.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,039,820</td>
<td align="right">0.5%</td>
<td align="right">91.7%</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,003,140</td>
<td align="right">0.5%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">994,220</td>
<td align="right">0.5%</td>
<td align="right">92.7%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">847,600</td>
<td align="right">0.4%</td>
<td align="right">93.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">842,800</td>
<td align="right">0.4%</td>
<td align="right">93.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">802,320</td>
<td align="right">0.4%</td>
<td align="right">94.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">768,400</td>
<td align="right">0.4%</td>
<td align="right">94.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">726,240</td>
<td align="right">0.4%</td>
<td align="right">94.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">718,540</td>
<td align="right">0.4%</td>
<td align="right">95.2%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">705,660</td>
<td align="right">0.4%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">672,240</td>
<td align="right">0.4%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">642,120</td>
<td align="right">0.3%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">630,060</td>
<td align="right">0.3%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">582,180</td>
<td align="right">0.3%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">513,540</td>
<td align="right">0.3%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">312,540</td>
<td align="right">0.2%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">308,680</td>
<td align="right">0.2%</td>
<td align="right">97.5%</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">256,740</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">248,560</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">241,920</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">229,380</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">226,380</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">186,120</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">184,300</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">180,840</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">180,360</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">170,600</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">170,160</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">150,960</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">127,440</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">126,660</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">113,820</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">105,420</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">97,100</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">85,080</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">79,380</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">79,380</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">76,200</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">72,480</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">72,240</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">66,300</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">66,120</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">60,240</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">60,180</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">54,720</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">54,120</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">52,140</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">52,040</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">52,040</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">48,600</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">48,000</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">48,000</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">48,000</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">47,680</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">42,980</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">41,680</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">36,000</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">29,740</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">29,740</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">28,160</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">24,120</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">21,760</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">18,160</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">18,120</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">18,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">18,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,920</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">12,600</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">12,240</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD_METHOD</td>
<td align="right">12,120</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,080</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD_LAZY_DICT</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">7,320</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">6,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
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
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">20</td>
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
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">5,608,300</td>
<td align="right">2.9%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">4,480,800</td>
<td align="right">2.4%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_SLOT</td>
<td align="right">3,904,912</td>
<td align="right">2.1%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">3,893,540</td>
<td align="right">2.0%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR</td>
<td align="right">2,782,980</td>
<td align="right">1.5%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL RETURN_VALUE</td>
<td align="right">2,710,400</td>
<td align="right">1.4%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN PUSH_NULL</td>
<td align="right">2,653,140</td>
<td align="right">1.4%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND JUMP_BACKWARD</td>
<td align="right">2,581,080</td>
<td align="right">1.4%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">2,540,340</td>
<td align="right">1.3%</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_FAST</td>
<td align="right">2,507,056</td>
<td align="right">1.3%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE POP_JUMP_IF_FALSE</td>
<td align="right">2,282,660</td>
<td align="right">1.2%</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">2,252,140</td>
<td align="right">1.2%</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,165,960</td>
<td align="right">1.1%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">2,158,820</td>
<td align="right">1.1%</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST POP_ITER</td>
<td align="right">2,017,980</td>
<td align="right">1.1%</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT</td>
<td align="right">2,010,440</td>
<td align="right">1.1%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_LIST</td>
<td align="right">1,987,900</td>
<td align="right">1.0%</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">1,950,340</td>
<td align="right">1.0%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL STORE_FAST</td>
<td align="right">1,945,260</td>
<td align="right">1.0%</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL STORE_FAST</td>
<td align="right">1,860,480</td>
<td align="right">1.0%</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LIST_APPEND</td>
<td align="right">1,860,000</td>
<td align="right">1.0%</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT RETURN_VALUE</td>
<td align="right">1,806,120</td>
<td align="right">0.9%</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,800,120</td>
<td align="right">0.9%</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL BINARY_SUBSCR_DICT</td>
<td align="right">1,794,140</td>
<td align="right">0.9%</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR LOAD_DEREF</td>
<td align="right">1,794,120</td>
<td align="right">0.9%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT GET_ITER</td>
<td align="right">1,782,300</td>
<td align="right">0.9%</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">1,684,980</td>
<td align="right">0.9%</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">1,560,380</td>
<td align="right">0.8%</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD FOR_ITER</td>
<td align="right">1,470,540</td>
<td align="right">0.8%</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST_LOAD_FAST</td>
<td align="right">1,443,840</td>
<td align="right">0.8%</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,383,220</td>
<td align="right">0.7%</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP POP_JUMP_IF_FALSE</td>
<td align="right">1,343,000</td>
<td align="right">0.7%</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD FOR_ITER_LIST</td>
<td align="right">1,339,680</td>
<td align="right">0.7%</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_NONE</td>
<td align="right">1,339,140</td>
<td align="right">0.7%</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST_IMMORTAL</td>
<td align="right">1,328,040</td>
<td align="right">0.7%</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_FAST</td>
<td align="right">1,313,120</td>
<td align="right">0.7%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST LOAD_FAST</td>
<td align="right">1,308,940</td>
<td align="right">0.7%</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_FAST</td>
<td align="right">1,302,720</td>
<td align="right">0.7%</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_CONST_IMMORTAL</td>
<td align="right">1,296,660</td>
<td align="right">0.7%</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,290,120</td>
<td align="right">0.7%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_DEREF</td>
<td align="right">1,284,480</td>
<td align="right">0.7%</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_ATTR</td>
<td align="right">1,240,520</td>
<td align="right">0.7%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR CONTAINS_OP</td>
<td align="right">1,240,020</td>
<td align="right">0.7%</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF LOAD_FAST</td>
<td align="right">1,230,960</td>
<td align="right">0.6%</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST</td>
<td align="right">1,211,780</td>
<td align="right">0.6%</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">1,200,120</td>
<td align="right">0.6%</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_METHOD_WITH_VALUES</td>
<td align="right">1,095,216</td>
<td align="right">0.6%</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER</td>
<td align="right">1,023,320</td>
<td align="right">0.5%</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER POP_ITER</td>
<td align="right">1,020,300</td>
<td align="right">0.5%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_CONST_IMMORTAL</td>
<td align="right">996,300</td>
<td align="right">0.5%</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST</td>
<td align="right">942,840</td>
<td align="right">0.5%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">938,376</td>
<td align="right">0.5%</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">933,500</td>
<td align="right">0.5%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_NON_PY_GENERAL</td>
<td align="right">907,800</td>
<td align="right">0.5%</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">881,820</td>
<td align="right">0.5%</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST</td>
<td align="right">876,600</td>
<td align="right">0.5%</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_SLOT</td>
<td align="right">858,160</td>
<td align="right">0.5%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">841,520</td>
<td align="right">0.4%</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL</td>
<td align="right">828,880</td>
<td align="right">0.4%</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_FAST</td>
<td align="right">824,260</td>
<td align="right">0.4%</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_FAST</td>
<td align="right">816,200</td>
<td align="right">0.4%</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">810,720</td>
<td align="right">0.4%</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_METHOD</td>
<td align="right">810,200</td>
<td align="right">0.4%</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">809,100</td>
<td align="right">0.4%</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">807,640</td>
<td align="right">0.4%</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN</td>
<td align="right">796,520</td>
<td align="right">0.4%</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST_IMMORTAL</td>
<td align="right">792,720</td>
<td align="right">0.4%</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">786,320</td>
<td align="right">0.4%</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">GET_ITER LOAD_FAST_AND_CLEAR</td>
<td align="right">769,560</td>
<td align="right">0.4%</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR SWAP</td>
<td align="right">769,560</td>
<td align="right">0.4%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">SWAP GET_ITER</td>
<td align="right">769,560</td>
<td align="right">0.4%</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_LOAD_FAST</td>
<td align="right">768,600</td>
<td align="right">0.4%</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST</td>
<td align="right">768,200</td>
<td align="right">0.4%</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR</td>
<td align="right">750,720</td>
<td align="right">0.4%</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST SWAP</td>
<td align="right">739,560</td>
<td align="right">0.4%</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">SWAP BUILD_LIST</td>
<td align="right">739,560</td>
<td align="right">0.4%</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NONE</td>
<td align="right">736,520</td>
<td align="right">0.4%</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS INTERPRETER_EXIT</td>
<td align="right">735,360</td>
<td align="right">0.4%</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_NON_PY_GENERAL</td>
<td align="right">732,760</td>
<td align="right">0.4%</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST</td>
<td align="right">732,360</td>
<td align="right">0.4%</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK RETURN_VALUE</td>
<td align="right">726,240</td>
<td align="right">0.4%</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST STORE_FAST</td>
<td align="right">720,240</td>
<td align="right">0.4%</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE LOAD_FAST</td>
<td align="right">718,320</td>
<td align="right">0.4%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_WITH_HINT</td>
<td align="right">712,880</td>
<td align="right">0.4%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES CALL_PY_GENERAL</td>
<td align="right">711,700</td>
<td align="right">0.4%</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST PUSH_NULL</td>
<td align="right">709,500</td>
<td align="right">0.4%</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">POP_ITER SWAP</td>
<td align="right">709,260</td>
<td align="right">0.4%</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">SWAP STORE_FAST</td>
<td align="right">709,260</td>
<td align="right">0.4%</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR LOAD_FAST_AND_CLEAR</td>
<td align="right">696,120</td>
<td align="right">0.4%</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP LOAD_FAST</td>
<td align="right">695,680</td>
<td align="right">0.4%</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST</td>
<td align="right">691,440</td>
<td align="right">0.4%</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_CONST_IMMORTAL</td>
<td align="right">690,080</td>
<td align="right">0.4%</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_METHOD_NO_DICT</td>
<td align="right">688,280</td>
<td align="right">0.4%</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST POP_JUMP_IF_FALSE</td>
<td align="right">679,520</td>
<td align="right">0.4%</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_BUILTIN_O</td>
<td align="right">675,520</td>
<td align="right">0.4%</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">673,480</td>
<td align="right">0.4%</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">673,320</td>
<td align="right">0.4%</td>
<td align="right">69.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_ATTR</td>
<td align="right">668,280</td>
<td align="right">0.4%</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS LOAD_FAST</td>
<td align="right">666,240</td>
<td align="right">0.3%</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE EXIT_INIT_CHECK</td>
<td align="right">660,080</td>
<td align="right">0.3%</td>
<td align="right">70.5%</td>
</tr>
</tbody>
</table>


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each Tier 1 opcode. </summary>


This does not include the unspecialized instructions that occur after a
specialized instruction deoptimizes.

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
<td align="right">4,480,800</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">252,120</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,000</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">78,460</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">43,320</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">24,000</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">12,000</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">6,000</td>
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
<td align="right">72,240</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">18,000</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,000</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">12,000</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">12,000</td>
<td align="right">7.0%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">75,300</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">47,680</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">43,280</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">32,940</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">24,720</td>
<td align="right">10.2%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">84,360</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">60,540</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">48,360</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">24,480</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">12,120</td>
<td align="right">5.0%</td>
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
<td align="right">24,000</td>
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
<td align="right">24,000</td>
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
<td align="right">24,000</td>
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
<td align="right">24,000</td>
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
<td align="right">660,080</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">54,000</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,000</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">726,240</td>
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
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,782,300</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">769,560</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">612,000</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">243,060</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">216,060</td>
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
<td align="right">1,987,900</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,023,320</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">769,560</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">79,320</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">36,060</td>
<td align="right">0.9%</td>
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
<td align="right">3,893,540</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">735,360</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">48,120</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">48,000</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,000</td>
<td align="right">0.3%</td>
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
<td align="right">229,380</td>
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
<td align="right">79,380</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">66,000</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">66,000</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,000</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">6,000</td>
<td align="right">2.6%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">48,000</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">45,760</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">24,120</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">18,120</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">18,120</td>
<td align="right">9.8%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">142,180</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,120</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,000</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">12,000</td>
<td align="right">6.5%</td>
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
<td align="right">24,000</td>
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
<td align="right">12,000</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">12,000</td>
<td align="right">50.0%</td>
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
<td align="right">2,017,980</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,020,300</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">60,360</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,302,720</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">996,300</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">709,260</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42,120</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">24,120</td>
<td align="right">0.8%</td>
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
<td align="left">CACHE</td>
<td align="right">252,120</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">163,440</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">72,120</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">48,000</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">36,240</td>
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
<td align="right">252,120</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">151,920</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">120,540</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">72,480</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">42,360</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,000</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">12,000</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">24,000</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,653,140</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">709,500</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">673,320</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">605,260</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">290,220</td>
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
<td align="right">2,252,140</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,443,840</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">642,840</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">606,000</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">36,480</td>
<td align="right">0.7%</td>
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
<td align="right">12,000</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">12,000</td>
<td align="right">100.0%</td>
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
<td align="right">2,710,400</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,806,120</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">726,240</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">356,280</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">204,240</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">3,893,540</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">660,080</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">618,100</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">600,080</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">172,460</td>
<td align="right">2.7%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">52,040</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">80</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
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
<td align="right">52,040</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">80</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">20</td>
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
<td align="right">828,880</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">102,740</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">80,440</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">30,120</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">24,240</td>
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
<td align="right">786,320</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">304,720</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,000</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,900</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">200</td>
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
<td align="right">24,000</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">24,000</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">24,000</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12,000</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,000</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">6,000</td>
<td align="right">12.5%</td>
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
<td align="right">84,020</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">54,000</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">48,120</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">24,120</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">24,000</td>
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
<td align="right">90,240</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">48,240</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">36,120</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">36,000</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,000</td>
<td align="right">4.7%</td>
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
<td align="left">SWAP</td>
<td align="right">739,560</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">46,260</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">29,740</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">24,120</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,120</td>
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
<td align="left">SWAP</td>
<td align="right">739,560</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">49,380</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">29,680</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">24,120</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">60</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">600,000</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">48,000</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">24,000</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,840</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">18,000</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">695,680</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">30,120</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">18,000</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">12,000</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,240</td>
<td align="right">0.8%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">24,000</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,120</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,000</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">12,000</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">120</td>
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
<td align="left">BINARY_OP</td>
<td align="right">48,120</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">12,000</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">120</td>
<td align="right">0.2%</td>
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
<td align="left">JUMP_FORWARD</td>
<td align="right">600,000</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">559,460</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">237,400</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">113,980</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">48,000</td>
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
<td align="left">LIST_APPEND</td>
<td align="right">625,320</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">508,280</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">219,360</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">84,000</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">79,380</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">12,020</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">160</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">100</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">80</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">12,120</td>
<td align="right">96.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">120</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">100</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">100</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">60</td>
<td align="right">0.5%</td>
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
<td align="right">29,740</td>
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
<td align="right">24,540</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">5,200</td>
<td align="right">17.5%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">12,000</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">40</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">40</td>
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
<td align="right">12,000</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">40</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">24,000</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,000</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,000</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">480</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">240</td>
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
<td align="right">36,480</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">18,000</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">240</td>
<td align="right">0.4%</td>
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
<td align="right">1,240,020</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">58,160</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">38,700</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,000</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">760</td>
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
<td align="right">1,343,000</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">760</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">52,160</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">52,040</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">48,000</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">36,240</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">12,120</td>
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
<td align="right">60,120</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60,000</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">52,040</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">52,040</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">12,120</td>
<td align="right">4.9%</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">12,120</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">9,580</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">16,560</td>
<td align="right">76.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">5,200</td>
<td align="right">23.9%</td>
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
<td align="right">47,680</td>
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
<td align="right">47,680</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">168,060</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">54,360</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">36,060</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">18,000</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">12,000</td>
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
<td align="right">198,000</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">48,360</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">36,000</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">18,060</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,000</td>
<td align="right">1.9%</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,470,540</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,023,320</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,000</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,400</td>
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
<td align="right">1,290,120</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,020,300</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">99,540</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">89,820</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,400</td>
<td align="right">0.1%</td>
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
<td align="right">6,000</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,000</td>
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
<td align="right">12,000</td>
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
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">6,000</td>
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
<td align="right">6,000</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">450,000</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">48,000</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">24,120</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">18,060</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,000</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">510,120</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">60,000</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,000</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,000</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
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
<td align="left">LIST_APPEND</td>
<td align="right">2,581,080</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">132,240</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">120,540</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">48,480</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">48,000</td>
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
<td align="left">FOR_ITER</td>
<td align="right">1,470,540</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,339,680</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">168,060</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">85,320</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,000</td>
<td align="right">0.4%</td>
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
<td align="right">12,000</td>
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
<td align="right">12,000</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">606,000</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">600,000</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">68,880</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">24,120</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">12,000</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">606,000</td>
<td align="right">44.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">600,000</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">105,000</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">12,000</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">12,000</td>
<td align="right">0.9%</td>
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
<td align="right">1,860,000</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">625,320</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">47,760</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">36,000</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,000</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,581,080</td>
<td align="right">100.0%</td>
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
<td align="right">29,680</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">29,740</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">2,158,820</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,240,520</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">668,280</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">104,048</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">96,360</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">1,240,020</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">606,120</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">559,460</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">532,740</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">145,720</td>
<td align="right">3.2%</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">1,794,120</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,284,480</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">78,060</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">54,000</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">48,120</td>
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
<td align="right">1,230,960</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">606,000</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">605,260</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">600,000</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">90,000</td>
<td align="right">2.6%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,608,300</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,540,340</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,507,056</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,252,140</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,560,380</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,904,912</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,782,980</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,158,820</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,860,000</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,800,120</td>
<td align="right">5.4%</td>
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
<td align="right">769,560</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">696,120</td>
<td align="right">47.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">769,560</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">696,120</td>
<td align="right">47.5%</td>
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
<td align="right">24,120</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">24,120</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">12,000</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">12,000</td>
<td align="right">16.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">24,120</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">24,120</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">12,000</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">12,000</td>
<td align="right">16.6%</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">1,443,840</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">881,820</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">876,600</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">768,600</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">768,200</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,010,440</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">810,720</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">807,640</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">750,720</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">732,760</td>
<td align="right">9.8%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">80</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">40</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">40</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">40</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">20</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">180</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">60</td>
<td align="right">25.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_METHOD

<details>
<summary> Successors and predecessors for LOAD_METHOD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">810,200</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">181,440</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">61,616</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">28,800</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,160</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">618,000</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">344,216</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">126,040</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">12,120</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,000</td>
<td align="right">1.1%</td>
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
<td align="right">108,180</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">52,040</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">24,240</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">12,000</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">12,000</td>
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
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">114,160</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">52,040</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">24,240</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,920</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">12,000</td>
<td align="right">5.3%</td>
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
<td align="right">24,320</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,400</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">5,200</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
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
<td align="left">MAKE_CELL</td>
<td align="right">24,320</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">18,660</td>
<td align="right">43.4%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">24,000</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">24,000</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">48,000</td>
<td align="right">100.0%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,282,660</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,684,980</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,343,000</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">786,320</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">679,520</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">5,608,300</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">796,520</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">792,720</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">156,240</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">147,780</td>
<td align="right">1.9%</td>
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
<td align="right">736,520</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">47,800</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,000</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,000</td>
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
<td align="right">718,320</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">54,000</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">12,000</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">12,000</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,000</td>
<td align="right">0.7%</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">606,000</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">391,380</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">30,000</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">24,000</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">6,000</td>
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
<td align="right">942,840</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">48,480</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">42,360</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,480</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">12,000</td>
<td align="right">1.1%</td>
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
<td align="left">CONTAINS_OP_SET</td>
<td align="right">624,120</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">428,720</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">304,720</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">60,000</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">48,360</td>
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
<td align="right">1,211,780</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">132,240</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">102,200</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">82,160</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">36,240</td>
<td align="right">2.2%</td>
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
<td align="right">79,380</td>
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
<td align="right">66,060</td>
<td align="right">83.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,320</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">6,000</td>
<td align="right">7.6%</td>
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
<td align="right">2,782,980</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">750,720</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">48,240</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,000</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,580</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">1,794,120</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">653,440</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">600,000</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">365,300</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">90,360</td>
<td align="right">2.5%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">19,380</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">18,000</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">12,000</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">12,000</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,000</td>
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
<td align="right">18,060</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">18,000</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">12,000</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">12,000</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,320</td>
<td align="right">9.2%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,945,260</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,860,480</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">720,240</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">709,260</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">691,440</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">2,540,340</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,296,660</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,284,480</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">881,820</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">720,240</td>
<td align="right">9.1%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">89,820</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">24,000</td>
<td align="right">21.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">77,820</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">24,000</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,000</td>
<td align="right">10.5%</td>
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
<td align="right">1,950,340</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">180,840</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">24,840</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">24,120</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">12,000</td>
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
<td align="right">1,308,940</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">648,120</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">192,120</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">24,840</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">18,120</td>
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
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">769,560</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">739,560</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">709,260</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">52,040</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">48,240</td>
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
<td align="left">GET_ITER</td>
<td align="right">769,560</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">739,560</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">709,260</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">52,040</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">48,240</td>
<td align="right">2.1%</td>
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
<td align="right">20</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">20</td>
<td align="right">100.0%</td>
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
<td align="left">BUILD_TUPLE</td>
<td align="right">36,120</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,000</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,000</td>
<td align="right">18.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">48,120</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">12,000</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">6,000</td>
<td align="right">9.1%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">60</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">52,040</td>
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
<td align="left">SWAP</td>
<td align="right">52,040</td>
<td align="right">100.0%</td>
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
<td align="right">120</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,794,140</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">133,440</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">54,480</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">18,120</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,000</td>
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
<td align="left">GET_ITER</td>
<td align="right">1,782,300</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">108,600</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">36,000</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">24,000</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">18,000</td>
<td align="right">0.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">18,120</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">18,120</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">17,920</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">12,000</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,920</td>
<td align="right">33.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,800,120</td>
<td align="right">94.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">114,160</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">1,806,120</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">36,000</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">24,180</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">24,000</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">12,000</td>
<td align="right">0.6%</td>
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
<td align="right">24,240</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,260</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,740</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,120</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">120</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">12,000</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">12,000</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">11,880</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,240</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,000</td>
<td align="right">12.3%</td>
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
<td align="right">40,560</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">24,160</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">19,680</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">12,120</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">460</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">30,000</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">24,540</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,000</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">9,600</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">9,120</td>
<td align="right">9.4%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">12,000</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,000</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">18,000</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">606,000</td>
<td align="right">60.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">204,240</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">66,600</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">24,000</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">18,000</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">666,240</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">204,240</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">42,360</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">36,300</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">18,000</td>
<td align="right">1.8%</td>
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
<td align="right">43,800</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">42,240</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">24,120</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">18,000</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">12,000</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">67,080</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">66,120</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">36,120</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">840</td>
<td align="right">0.5%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">7,320</td>
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
<td align="left">GET_ITER</td>
<td align="right">7,320</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">675,520</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">594,000</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,000</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">618,240</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">600,000</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">33,160</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">30,120</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">240</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">36,000</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">24,360</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">12,120</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">72,480</td>
<td align="right">100.0%</td>
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
<td align="right">18,000</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">160</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">8,480</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,680</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,840</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">160</td>
<td align="right">0.9%</td>
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
<td align="right">54,120</td>
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
<td align="right">36,000</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,120</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">6,000</td>
<td align="right">11.1%</td>
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
<td align="right">150,920</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
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
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">57,580</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">18,000</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">18,000</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">12,000</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">10,900</td>
<td align="right">7.2%</td>
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
<td align="right">24,000</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">12,000</td>
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
<td align="right">24,000</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,000</td>
<td align="right">33.3%</td>
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
<td align="left">CALL_TUPLE_1</td>
<td align="right">24,120</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,040</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">24,120</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,040</td>
<td align="right">14.3%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">66,980</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">58,740</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">36,000</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">27,540</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">24,120</td>
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
<td align="right">118,520</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">47,880</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">36,000</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">24,120</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">18,360</td>
<td align="right">5.9%</td>
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
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">60,160</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">GET_ITER</td>
<td align="right">30,000</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">12,000</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">12,000</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,120</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40</td>
<td align="right">0.1%</td>
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
<td align="right">624,000</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">6,000</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">600,000</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">12,060</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,000</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">6,000</td>
<td align="right">1.0%</td>
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
<td align="right">907,800</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">732,760</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">618,000</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">606,120</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">600,080</td>
<td align="right">16.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,945,260</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">642,180</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">612,000</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">163,440</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">84,500</td>
<td align="right">2.3%</td>
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
<td align="right">933,500</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">807,640</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">618,100</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">289,200</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">79,320</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">735,360</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">606,120</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">594,000</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">230,200</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">124,640</td>
<td align="right">4.2%</td>
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
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">711,700</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">606,120</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">78,120</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">18,040</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">6,120</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">612,120</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">594,000</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">68,340</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">43,280</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">24,120</td>
<td align="right">1.7%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">52,040</td>
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
<td align="left">COPY</td>
<td align="right">52,040</td>
<td align="right">100.0%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">612,000</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60,240</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">642,120</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">24,120</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">6,000</td>
<td align="right">0.9%</td>
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
<td align="right">12,000</td>
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
<td align="right">12,000</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">12,000</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">6,000</td>
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
<td align="right">12,000</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,000</td>
<td align="right">33.3%</td>
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
<td align="right">18,120</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">6,000</td>
<td align="right">24.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">18,120</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">6,000</td>
<td align="right">24.9%</td>
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
<td align="right">102,000</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">48,000</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">12,120</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">12,000</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,120</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">144,120</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">30,120</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,120</td>
<td align="right">3.4%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">624,120</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">18,000</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">624,120</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">18,000</td>
<td align="right">2.8%</td>
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
<td align="right">36,000</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">12,000</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">48,000</td>
<td align="right">100.0%</td>
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
<td align="right">1,987,900</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,339,680</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">198,000</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="left">POP_ITER</td>
<td align="right">2,017,980</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">691,440</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">636,240</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">180,000</td>
<td align="right">5.1%</td>
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
<td align="right">12,000</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">120</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">120</td>
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
<td align="right">12,060</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">180</td>
<td align="right">1.5%</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">85,320</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">30,120</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">9,120</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,880</td>
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
<td align="left">POP_ITER</td>
<td align="right">60,360</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42,240</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">24,000</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">840</td>
<td align="right">0.7%</td>
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
<td align="right">27,120</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">24,480</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,000</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">6,240</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,120</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">51,600</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">24,360</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">240</td>
<td align="right">0.3%</td>
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
<td align="right">74,820</td>
<td align="right">71.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,060</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,000</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,000</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,000</td>
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
<td align="right">44,580</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,240</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,000</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">12,000</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">12,000</td>
<td align="right">11.4%</td>
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
<td align="right">614,980</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">164,060</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">68,340</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">57,700</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">52,040</td>
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
<td align="right">152,780</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">110,120</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">102,000</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">66,000</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">60,400</td>
<td align="right">5.8%</td>
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
<td align="right">841,520</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,000</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">673,320</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">48,720</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">36,000</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">25,200</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">24,120</td>
<td align="right">2.8%</td>
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
<td align="right">72,720</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,000</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">240</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">120</td>
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
<td align="right">36,360</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">24,360</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12,120</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">12,000</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">240</td>
<td align="right">0.3%</td>
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
<td align="right">673,480</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">118,180</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">110,520</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">108,360</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">48,240</td>
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
<td align="right">423,640</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">343,560</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">80,440</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">78,000</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">48,120</td>
<td align="right">4.2%</td>
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
<td align="right">54,180</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,000</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">120</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">18,000</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">12,000</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">11,940</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,120</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">6,000</td>
<td align="right">9.0%</td>
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
<td align="right">3,904,912</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">612,120</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">90,000</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">77,820</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">76,140</td>
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
<td align="right">2,507,056</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,240,520</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">216,060</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">204,240</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">144,240</td>
<td align="right">2.9%</td>
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
<td align="right">712,880</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">600,000</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">87,436</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">63,840</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60,000</td>
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
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">618,120</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">196,700</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">193,080</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">108,360</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">96,360</td>
<td align="right">5.9%</td>
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
<td align="right">1,328,040</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,296,660</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">996,300</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">792,720</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">690,080</td>
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
<td align="right">2,710,400</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,860,480</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,794,140</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">824,260</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">109,456</td>
<td align="right">1.4%</td>
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
<td align="right">90,480</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">79,380</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">66,060</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">66,000</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">42,120</td>
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
<td align="left">MAKE_FUNCTION</td>
<td align="right">229,380</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">150,920</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">54,120</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">24,000</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">18,000</td>
<td align="right">3.5%</td>
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
<td align="right">2,165,960</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">796,520</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">642,840</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">600,000</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">175,760</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">2,653,140</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,200,120</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">606,000</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">181,440</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">24,480</td>
<td align="right">0.5%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">660,000</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">630,640</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">188,580</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">147,780</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">78,200</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">841,520</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">450,000</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">290,220</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">66,320</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">59,800</td>
<td align="right">2.9%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_METHOD_LAZY_DICT </summary>

<table>
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
<td align="right">12,000</td>
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
<td align="right">12,000</td>
<td align="right">100.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_METHOD_NO_DICT </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">688,280</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">128,620</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">50,580</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">42,360</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">24,000</td>
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
<td align="right">809,100</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">60,160</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">35,880</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">30,180</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">24,120</td>
<td align="right">2.4%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_METHOD_WITH_VALUES </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,095,216</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">618,120</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">606,000</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">230,200</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">172,460</td>
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
<td align="right">938,376</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">876,600</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">711,700</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">289,200</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">147,300</td>
<td align="right">4.8%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_SUPER_METHOD_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_METHOD_METHOD </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,120</td>
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
<td align="right">12,120</td>
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
<td align="left">CACHE</td>
<td align="right">4,480,800</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">252,120</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">124,640</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">60,540</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">24,540</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,165,960</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,560,380</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">768,600</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">188,580</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">77,840</td>
<td align="right">1.5%</td>
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
<td align="right">1,383,220</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">810,720</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">52,040</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">12,000</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,000</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">732,360</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">660,000</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">600,000</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">163,140</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">48,480</td>
<td align="right">2.1%</td>
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
<td align="right">2,010,440</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">858,160</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">12,000</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">11,880</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">880</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">816,200</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">768,200</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">690,080</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">606,000</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">12,000</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">66,040</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">24,360</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">18,000</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">12,000</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,000</td>
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
<td align="right">48,000</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">36,240</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">24,300</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">12,000</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">6,120</td>
<td align="right">4.8%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">72,240</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">41,840</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">36,120</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">12,000</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,080</td>
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
<td align="right">168,020</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">18,000</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
<td align="left">CALL_BUILTIN_O</td>
<td align="right">618,240</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">343,560</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">316,660</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">193,080</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">145,720</td>
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
<td align="right">1,684,980</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">428,720</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">54,360</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">24,000</td>
<td align="right">1.1%</td>
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
<td align="right">36,000</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,600</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">36,000</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,600</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">80</td>
<td align="right">0.2%</td>
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
<td align="right">653,300</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">28,960</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12,120</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">12,000</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">5,940</td>
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
<td align="right">679,520</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">38,720</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">100</td>
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
<td align="right">1,339,140</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">600,000</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">65,880</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">60,400</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">48,240</td>
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
<td align="right">2,282,660</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">47,920</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">24,000</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">120</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">12,000</td>
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
<td align="right">12,000</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">180,000</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">840</td>
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
<td align="right">180,840</td>
<td align="right">100.0%</td>
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
<td align="right">1,290,120</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">636,240</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">24,000</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,120</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">17,800</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,950,340</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">30,120</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,000</td>
<td align="right">0.3%</td>
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
<td align="right">255,840</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">102,480</td>
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
<td align="right">40</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">860</td>
<td align="right">95.6%</td>
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
<td align="left">add other</td>
<td align="right">320</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">240</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">100</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">80</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">60</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">40</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">20</td>
<td align="right">2.3%</td>
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
<td align="right">169,800</td>
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
<td align="right">5,841,660</td>
<td align="right">97.2%</td>
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
<td align="right">120</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">680</td>
<td align="right">85.0%</td>
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
<td align="right">600</td>
<td align="right">88.2%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">80</td>
<td align="right">11.8%</td>
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
<td align="right">12,120</td>
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
<td align="right">15,248,860</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">379,740</td>
<td align="right">2.4%</td>
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
<td align="right">7,600</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">100</td>
<td align="right">1.3%</td>
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
<td align="right">140</td>
<td align="right">140.0%</td>
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
<td align="right">12,000</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,840</td>
<td align="right">39.4%</td>
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
<td align="right">200</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">16.7%</td>
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
<td align="right">54,480</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">144,480</td>
<td align="right">72.5%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">240</td>
<td align="right">100.0%</td>
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
<td align="right">160</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">40</td>
<td align="right">16.7%</td>
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
<td align="right">1,343,000</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,247,489</td>
<td align="right">62.6%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">760</td>
<td align="right">100.0%</td>
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
<td align="right">520</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">240</td>
<td align="right">31.6%</td>
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
<td align="right">2,499,780</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,229,340</td>
<td align="right">62.8%</td>
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
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,400</td>
<td align="right">94.6%</td>
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
<td align="left">zip</td>
<td align="right">480</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">400</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">140</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">120</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">80</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">40</td>
<td align="right">2.9%</td>
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
<td align="right">4,536,876</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">26,033,874</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,529,515</td>
<td align="right">4.8%</td>
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
<td align="right">29,349</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">15,020</td>
<td align="right">33.9%</td>
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
<td align="right">4,800</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">980</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">800</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">460</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">460</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">140</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">120</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">60</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,547,880</td>
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
<td align="right">240</td>
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

### LOAD_METHOD

<details>
<summary> specialization stats for LOAD_METHOD family </summary>

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
<td align="right">1,121,036</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">561,920</td>
<td align="right">33.3%</td>
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
<td align="right">10,960</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,248</td>
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
<td align="right">1,988</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">kind 13</td>
<td align="right">160</td>
<td align="right">7.1%</td>
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
<td align="right">12,240</td>
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
<td align="right">3,587,940</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,711,180</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">51,540</td>
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
<td align="right">980</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,680</td>
<td align="right">73.2%</td>
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
<td align="right">7,180</td>
<td align="right">267.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,640</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">560</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">180</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">140</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">80</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">80</td>
<td align="right">3.0%</td>
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
<td align="right">52,040</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,263,380</td>
<td align="right">97.7%</td>
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
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">80</td>
<td align="right">80.0%</td>
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
<td align="right">80</td>
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
<td align="right">1,097,040</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,234,560</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">47,620</td>
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
<td align="right">940</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,220</td>
<td align="right">70.3%</td>
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
<td align="right">1,120</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">360</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">300</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">180</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">120</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">120</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">0.9%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,329,060</td>
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
<td align="right">107,346,328</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">14,771,748</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">65,734,590</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">2,578,175</td>
<td align="right">1.4%</td>
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
<td align="right">4,536,876</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">3,587,940</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,499,780</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,343,000</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">1,121,036</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,097,040</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">255,840</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">169,800</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">54,480</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">52,040</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">862,040</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">536,900</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">280,420</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">200,559</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">178,220</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">139,920</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">130,036</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">46,240</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">31,620</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">25,060</td>
<td align="right">1.0%</td>
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
<td align="right">4,744,920</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">10,588,740</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">4,744,920</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,420,680</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">324,240</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,420,680</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">1,284,480</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">72,660</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">438,480</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">36,000</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">15,171,660</td>
<td align="right">98.9%</td>
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
<td align="right">18,219,820</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">18,219,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">21,114,100</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">21,005,760</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">96,300</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">12,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">22,815,775</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,622,520</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">91,502,742</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">160,140,440</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">219,498,848</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">187,433,221</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">26,654,900</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">33,175,660</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">109,106,679</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">96,272,570</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">696,720</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">24,120</td>
<td align="right">1.5%</td>
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
<td align="right">26,491,416</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">631,227</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">811,827</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">11,232,717</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">180,603</td>
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
<td align="right">0</td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right"></td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">0</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">20,829,100</td>
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
<td align="right">688,182,999</td>
<td align="right">3,303.9%</td>
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
<td align="right">0</td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right"></td>
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
<th align="right">Count</th>
<th align="right">Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="left">_NOP</td>
<td align="right">132,496,546</td>
<td align="right">19.3%</td>
<td align="right">19.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">75,598,408</td>
<td align="right">11.0%</td>
<td align="right">30.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">71,276,776</td>
<td align="right">10.4%</td>
<td align="right">40.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">61,709,271</td>
<td align="right">9.0%</td>
<td align="right">49.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">33,129,666</td>
<td align="right">4.8%</td>
<td align="right">54.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">18,424,009</td>
<td align="right">2.7%</td>
<td align="right">57.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">16,124,328</td>
<td align="right">2.3%</td>
<td align="right">59.4%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">15,370,629</td>
<td align="right">2.2%</td>
<td align="right">61.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">13,066,889</td>
<td align="right">1.9%</td>
<td align="right">63.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">12,465,260</td>
<td align="right">1.8%</td>
<td align="right">65.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">9,775,080</td>
<td align="right">1.4%</td>
<td align="right">66.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">8,902,100</td>
<td align="right">1.3%</td>
<td align="right">68.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">8,734,740</td>
<td align="right">1.3%</td>
<td align="right">69.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">8,672,280</td>
<td align="right">1.3%</td>
<td align="right">70.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">8,137,228</td>
<td align="right">1.2%</td>
<td align="right">71.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">7,751,144</td>
<td align="right">1.1%</td>
<td align="right">72.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">7,575,820</td>
<td align="right">1.1%</td>
<td align="right">74.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">6,833,360</td>
<td align="right">1.0%</td>
<td align="right">75.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,755,120</td>
<td align="right">1.0%</td>
<td align="right">76.0%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_JUMP</td>
<td align="right">6,247,689</td>
<td align="right">0.9%</td>
<td align="right">76.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,978,409</td>
<td align="right">0.9%</td>
<td align="right">77.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">5,693,100</td>
<td align="right">0.8%</td>
<td align="right">78.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">5,681,100</td>
<td align="right">0.8%</td>
<td align="right">79.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">5,674,504</td>
<td align="right">0.8%</td>
<td align="right">80.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">5,619,524</td>
<td align="right">0.8%</td>
<td align="right">81.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,697,260</td>
<td align="right">0.7%</td>
<td align="right">81.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">4,551,980</td>
<td align="right">0.7%</td>
<td align="right">82.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">4,524,580</td>
<td align="right">0.7%</td>
<td align="right">83.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">4,407,524</td>
<td align="right">0.6%</td>
<td align="right">83.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">4,364,060</td>
<td align="right">0.6%</td>
<td align="right">84.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">4,321,760</td>
<td align="right">0.6%</td>
<td align="right">84.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">4,145,680</td>
<td align="right">0.6%</td>
<td align="right">85.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,145,680</td>
<td align="right">0.6%</td>
<td align="right">86.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,951,044</td>
<td align="right">0.6%</td>
<td align="right">86.7%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">3,942,060</td>
<td align="right">0.6%</td>
<td align="right">87.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">3,713,040</td>
<td align="right">0.5%</td>
<td align="right">87.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,654,360</td>
<td align="right">0.5%</td>
<td align="right">88.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,422,084</td>
<td align="right">0.5%</td>
<td align="right">88.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">3,422,084</td>
<td align="right">0.5%</td>
<td align="right">89.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">3,422,084</td>
<td align="right">0.5%</td>
<td align="right">89.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD</td>
<td align="right">2,977,644</td>
<td align="right">0.4%</td>
<td align="right">90.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_NONE</td>
<td align="right">2,639,160</td>
<td align="right">0.4%</td>
<td align="right">90.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,412,204</td>
<td align="right">0.4%</td>
<td align="right">91.0%</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,410,960</td>
<td align="right">0.4%</td>
<td align="right">91.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">2,274,300</td>
<td align="right">0.3%</td>
<td align="right">91.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">2,274,300</td>
<td align="right">0.3%</td>
<td align="right">92.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">2,274,300</td>
<td align="right">0.3%</td>
<td align="right">92.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">2,112,600</td>
<td align="right">0.3%</td>
<td align="right">92.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_NO_DICT</td>
<td align="right">2,105,180</td>
<td align="right">0.3%</td>
<td align="right">93.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,026,920</td>
<td align="right">0.3%</td>
<td align="right">93.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,941,844</td>
<td align="right">0.3%</td>
<td align="right">93.6%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">1,874,568</td>
<td align="right">0.3%</td>
<td align="right">93.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,650,360</td>
<td align="right">0.2%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,554,440</td>
<td align="right">0.2%</td>
<td align="right">94.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_WITH_VALUES</td>
<td align="right">1,461,764</td>
<td align="right">0.2%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,419,920</td>
<td align="right">0.2%</td>
<td align="right">94.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,362,700</td>
<td align="right">0.2%</td>
<td align="right">94.9%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,359,020</td>
<td align="right">0.2%</td>
<td align="right">95.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,355,600</td>
<td align="right">0.2%</td>
<td align="right">95.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">1,334,920</td>
<td align="right">0.2%</td>
<td align="right">95.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">1,316,920</td>
<td align="right">0.2%</td>
<td align="right">95.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,310,920</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,254,429</td>
<td align="right">0.2%</td>
<td align="right">96.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,247,400</td>
<td align="right">0.2%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">1,224,000</td>
<td align="right">0.2%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,153,040</td>
<td align="right">0.2%</td>
<td align="right">96.6%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">1,116,000</td>
<td align="right">0.2%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,064,320</td>
<td align="right">0.2%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,025,000</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">1,017,360</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">949,456</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">809,620</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">808,860</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">806,096</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">806,096</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">804,660</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">696,860</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">692,900</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">692,900</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">684,000</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">672,240</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right">665,280</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">595,320</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">534,960</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">516,120</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">516,000</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">361,880</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">312,360</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">310,520</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">309,009</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right">300,000</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">300,000</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">298,920</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">294,360</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">286,920</td>
<td align="right">0.0%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">270,040</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_FOR</td>
<td align="right">270,000</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">267,360</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">264,560</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">258,120</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">209,329</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">198,360</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">198,360</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">192,360</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">180,360</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">168,360</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">151,520</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">146,560</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">144,360</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">132,240</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">120,000</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">120,000</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">114,840</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">106,920</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">102,360</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">102,360</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">102,120</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">97,960</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">96,360</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">96,000</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">96,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">90,440</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">84,360</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">80,960</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">66,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">60,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">39,360</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">38,200</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">37,160</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">37,160</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">36,120</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">36,120</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">36,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">28,920</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">24,120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">24,120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">20,080</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">15,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_LAZY_DICT</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">6,120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">6,060</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">6,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">6,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">2,080</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_METHOD_METHOD</td>
<td align="right">120</td>
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
<td align="right">20</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-01-27
