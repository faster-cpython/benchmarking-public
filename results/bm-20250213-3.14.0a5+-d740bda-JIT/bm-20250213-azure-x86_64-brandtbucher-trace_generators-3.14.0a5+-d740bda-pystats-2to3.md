
# Pystats results

- benchmark: 2to3
- fork: brandtbucher
- ref: trace-generators
- commit hash: d740bda
- commit date: 2025-02-13T17:39:23-08:00

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
<td align="right">42,980</td>
<td align="right">19.8%</td>
<td align="right">19.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,260</td>
<td align="right">5.2%</td>
<td align="right">25.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">9,560</td>
<td align="right">4.4%</td>
<td align="right">29.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">9,100</td>
<td align="right">4.2%</td>
<td align="right">33.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">8,120</td>
<td align="right">3.7%</td>
<td align="right">37.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">7,960</td>
<td align="right">3.7%</td>
<td align="right">41.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,920</td>
<td align="right">3.2%</td>
<td align="right">44.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,560</td>
<td align="right">3.0%</td>
<td align="right">47.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">6,340</td>
<td align="right">2.9%</td>
<td align="right">50.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,620</td>
<td align="right">2.6%</td>
<td align="right">52.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,960</td>
<td align="right">2.3%</td>
<td align="right">55.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,920</td>
<td align="right">2.3%</td>
<td align="right">57.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,680</td>
<td align="right">2.2%</td>
<td align="right">59.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,640</td>
<td align="right">2.1%</td>
<td align="right">61.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,140</td>
<td align="right">1.9%</td>
<td align="right">63.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,340</td>
<td align="right">1.5%</td>
<td align="right">65.2%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,320</td>
<td align="right">1.5%</td>
<td align="right">66.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,120</td>
<td align="right">1.4%</td>
<td align="right">68.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,880</td>
<td align="right">1.3%</td>
<td align="right">69.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,760</td>
<td align="right">1.3%</td>
<td align="right">70.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,480</td>
<td align="right">1.1%</td>
<td align="right">71.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,320</td>
<td align="right">1.1%</td>
<td align="right">72.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,320</td>
<td align="right">1.1%</td>
<td align="right">74.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,200</td>
<td align="right">1.0%</td>
<td align="right">75.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,060</td>
<td align="right">1.0%</td>
<td align="right">76.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,000</td>
<td align="right">0.9%</td>
<td align="right">76.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,900</td>
<td align="right">0.9%</td>
<td align="right">77.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,880</td>
<td align="right">0.9%</td>
<td align="right">78.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,860</td>
<td align="right">0.9%</td>
<td align="right">79.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,800</td>
<td align="right">0.8%</td>
<td align="right">80.3%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,660</td>
<td align="right">0.8%</td>
<td align="right">81.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,660</td>
<td align="right">0.8%</td>
<td align="right">81.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,640</td>
<td align="right">0.8%</td>
<td align="right">82.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,520</td>
<td align="right">0.7%</td>
<td align="right">83.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,520</td>
<td align="right">0.7%</td>
<td align="right">84.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,500</td>
<td align="right">0.7%</td>
<td align="right">84.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,360</td>
<td align="right">0.6%</td>
<td align="right">85.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,360</td>
<td align="right">0.6%</td>
<td align="right">86.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,200</td>
<td align="right">0.6%</td>
<td align="right">86.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,180</td>
<td align="right">0.5%</td>
<td align="right">87.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,120</td>
<td align="right">0.5%</td>
<td align="right">87.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,120</td>
<td align="right">0.5%</td>
<td align="right">88.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,100</td>
<td align="right">0.5%</td>
<td align="right">88.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,040</td>
<td align="right">0.5%</td>
<td align="right">89.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,020</td>
<td align="right">0.5%</td>
<td align="right">89.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,020</td>
<td align="right">0.5%</td>
<td align="right">90.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">940</td>
<td align="right">0.4%</td>
<td align="right">90.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">840</td>
<td align="right">0.4%</td>
<td align="right">90.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">840</td>
<td align="right">0.4%</td>
<td align="right">91.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">91.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">92.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">760</td>
<td align="right">0.4%</td>
<td align="right">92.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">660</td>
<td align="right">0.3%</td>
<td align="right">92.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">640</td>
<td align="right">0.3%</td>
<td align="right">93.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">93.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">600</td>
<td align="right">0.3%</td>
<td align="right">93.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">600</td>
<td align="right">0.3%</td>
<td align="right">93.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">94.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">94.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">540</td>
<td align="right">0.2%</td>
<td align="right">95.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">500</td>
<td align="right">0.2%</td>
<td align="right">95.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">500</td>
<td align="right">0.2%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">480</td>
<td align="right">0.2%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">460</td>
<td align="right">0.2%</td>
<td align="right">96.0%</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">440</td>
<td align="right">0.2%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">96.4%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">96.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">400</td>
<td align="right">0.2%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">400</td>
<td align="right">0.2%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">380</td>
<td align="right">0.2%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">320</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">300</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">300</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">240</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">240</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">180</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
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
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">5,700</td>
<td align="right">2.6%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">5,140</td>
<td align="right">2.4%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_FAST</td>
<td align="right">4,960</td>
<td align="right">2.3%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">4,940</td>
<td align="right">2.3%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">2,600</td>
<td align="right">1.2%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR</td>
<td align="right">2,380</td>
<td align="right">1.1%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">2,240</td>
<td align="right">1.0%</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL</td>
<td align="right">2,220</td>
<td align="right">1.0%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">2,180</td>
<td align="right">1.0%</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,080</td>
<td align="right">1.0%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,080</td>
<td align="right">1.0%</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">2,080</td>
<td align="right">1.0%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL LOAD_ATTR</td>
<td align="right">1,920</td>
<td align="right">0.9%</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">1,880</td>
<td align="right">0.9%</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP POP_JUMP_IF_FALSE</td>
<td align="right">1,820</td>
<td align="right">0.8%</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">1,680</td>
<td align="right">0.8%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">1,660</td>
<td align="right">0.8%</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">1,640</td>
<td align="right">0.8%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE LOAD_FAST</td>
<td align="right">1,620</td>
<td align="right">0.7%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL RETURN_VALUE</td>
<td align="right">1,620</td>
<td align="right">0.7%</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">1,620</td>
<td align="right">0.7%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST_IMMORTAL</td>
<td align="right">1,540</td>
<td align="right">0.7%</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">1,540</td>
<td align="right">0.7%</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">1,520</td>
<td align="right">0.7%</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL LOAD_GLOBAL_MODULE</td>
<td align="right">1,520</td>
<td align="right">0.7%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL</td>
<td align="right">1,480</td>
<td align="right">0.7%</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,460</td>
<td align="right">0.7%</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST</td>
<td align="right">1,440</td>
<td align="right">0.7%</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR PUSH_NULL</td>
<td align="right">1,420</td>
<td align="right">0.7%</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL</td>
<td align="right">1,400</td>
<td align="right">0.6%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">1,300</td>
<td align="right">0.6%</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">CALL RESUME</td>
<td align="right">1,280</td>
<td align="right">0.6%</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL LOAD_FAST</td>
<td align="right">1,280</td>
<td align="right">0.6%</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL</td>
<td align="right">1,260</td>
<td align="right">0.6%</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST RETURN_VALUE</td>
<td align="right">1,220</td>
<td align="right">0.6%</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST RETURN_VALUE</td>
<td align="right">1,200</td>
<td align="right">0.6%</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">RESUME LOAD_FAST</td>
<td align="right">1,200</td>
<td align="right">0.6%</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">1,200</td>
<td align="right">0.6%</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST</td>
<td align="right">1,180</td>
<td align="right">0.5%</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE LOAD_FAST</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_SMALL_INT</td>
<td align="right">1,140</td>
<td align="right">0.5%</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_CONST</td>
<td align="right">1,120</td>
<td align="right">0.5%</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,100</td>
<td align="right">0.5%</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">1,100</td>
<td align="right">0.5%</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NONE</td>
<td align="right">1,060</td>
<td align="right">0.5%</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_FAST</td>
<td align="right">1,060</td>
<td align="right">0.5%</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">1,040</td>
<td align="right">0.5%</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,000</td>
<td align="right">0.5%</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">980</td>
<td align="right">0.5%</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR LOAD_CONST</td>
<td align="right">960</td>
<td align="right">0.4%</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_ATTR_MODULE</td>
<td align="right">940</td>
<td align="right">0.4%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR LOAD_FAST</td>
<td align="right">940</td>
<td align="right">0.4%</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL STORE_FAST</td>
<td align="right">940</td>
<td align="right">0.4%</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">920</td>
<td align="right">0.4%</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">920</td>
<td align="right">0.4%</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_CONST_IMMORTAL</td>
<td align="right">920</td>
<td align="right">0.4%</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_CONST</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">CALL STORE_FAST</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST COMPARE_OP</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_FAST</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST PUSH_NULL</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST JUMP_FORWARD</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">860</td>
<td align="right">0.4%</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR</td>
<td align="right">860</td>
<td align="right">0.4%</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST STORE_FAST</td>
<td align="right">840</td>
<td align="right">0.4%</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">840</td>
<td align="right">0.4%</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST BUILD_TUPLE</td>
<td align="right">820</td>
<td align="right">0.4%</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR CALL</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST CALL</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">RESUME LOAD_GLOBAL</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_CONST_IMMORTAL</td>
<td align="right">780</td>
<td align="right">0.4%</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST</td>
<td align="right">780</td>
<td align="right">0.4%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_CONST_IMMORTAL</td>
<td align="right">740</td>
<td align="right">0.3%</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL CALL</td>
<td align="right">740</td>
<td align="right">0.3%</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL</td>
<td align="right">740</td>
<td align="right">0.3%</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">740</td>
<td align="right">0.3%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">720</td>
<td align="right">0.3%</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">700</td>
<td align="right">0.3%</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL TO_BOOL_BOOL</td>
<td align="right">680</td>
<td align="right">0.3%</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD LOAD_FAST</td>
<td align="right">680</td>
<td align="right">0.3%</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL</td>
<td align="right">680</td>
<td align="right">0.3%</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL LOAD_GLOBAL_BUILTIN</td>
<td align="right">680</td>
<td align="right">0.3%</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">CALL POP_TOP</td>
<td align="right">640</td>
<td align="right">0.3%</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST STORE_FAST</td>
<td align="right">640</td>
<td align="right">0.3%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST COPY</td>
<td align="right">640</td>
<td align="right">0.3%</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">640</td>
<td align="right">0.3%</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">SWAP SWAP</td>
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR LOAD_FAST_LOAD_FAST</td>
<td align="right">600</td>
<td align="right">0.3%</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST DELETE_ATTR</td>
<td align="right">600</td>
<td align="right">0.3%</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">600</td>
<td align="right">0.3%</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">600</td>
<td align="right">0.3%</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST</td>
<td align="right">600</td>
<td align="right">0.3%</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_CONST_IMMORTAL</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">CALL TO_BOOL</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">COPY LOAD_SPECIAL</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE CALL_FUNCTION_EX</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">59.2%</td>
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
<td align="right">340</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">60</td>
<td align="right">15.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">340</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">15.0%</td>
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
<td align="right">1,040</td>
<td align="right">63.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">400</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">200</td>
<td align="right">12.2%</td>
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
<td align="right">560</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">280</td>
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
<td align="left">RETURN_GENERATOR</td>
<td align="right">200</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">140</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">140</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">140</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">80</td>
<td align="right">11.4%</td>
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
<td align="right">120</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">200</td>
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
<td align="right">440</td>
<td align="right">75.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">140</td>
<td align="right">24.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">280</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">220</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">80</td>
<td align="right">13.8%</td>
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
<td align="right">1,300</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">200</td>
<td align="right">13.3%</td>
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
<td align="right">260</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">160</td>
<td align="right">38.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">420</td>
<td align="right">100.0%</td>
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
<td align="right">400</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">360</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">280</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">220</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">200</td>
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
<td align="right">1,180</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">460</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">240</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">140</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">120</td>
<td align="right">5.5%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">120</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">80</td>
<td align="right">40.0%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">300</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">140</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">120</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">80</td>
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
<td align="left">LOAD_GLOBAL</td>
<td align="right">240</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">140</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">120</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">80</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">60</td>
<td align="right">9.4%</td>
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
<td align="right">2,240</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">640</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">420</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">320</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">240</td>
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
<td align="right">1,660</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">880</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">740</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">400</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">200</td>
<td align="right">4.1%</td>
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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">120</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">80</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">120</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
<td align="right">40.0%</td>
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
<td align="right">1,640</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,420</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">880</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">140</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60</td>
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
<td align="right">2,180</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">740</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">320</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">280</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">280</td>
<td align="right">6.8%</td>
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
<td align="left">CALL_FUNCTION_EX</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">200</td>
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
<td align="right">1,620</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,220</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,200</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">540</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">360</td>
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
<td align="left">POP_TOP</td>
<td align="right">2,240</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,520</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,300</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">360</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">320</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
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
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">20</td>
<td align="right">100.0%</td>
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
<td align="right">1,260</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">560</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">560</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">520</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">480</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,600</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">860</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">680</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">200</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">140</td>
<td align="right">3.0%</td>
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
<td align="right">420</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">340</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">340</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">180</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">160</td>
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
<td align="left">STORE_FAST</td>
<td align="right">500</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">340</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">180</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">140</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">100</td>
<td align="right">6.1%</td>
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
<td align="right">200</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">140</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">80</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">60</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
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
<td align="left">STORE_FAST</td>
<td align="right">340</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">140</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">60</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">40</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20</td>
<td align="right">3.3%</td>
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
<td align="right">200</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">140</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">140</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">80</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">9.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">420</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">140</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">9.7%</td>
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
<td align="right">820</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">560</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">140</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">60</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">540</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">280</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">260</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">160</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">160</td>
<td align="right">9.6%</td>
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
<td align="right">2,220</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">800</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">800</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">740</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">680</td>
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
<td align="left">RESUME</td>
<td align="right">1,280</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">880</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">640</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">560</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">480</td>
<td align="right">6.0%</td>
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
<td align="right">140</td>
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
<td align="right">320</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">180</td>
<td align="right">36.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">240</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">140</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">80</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">40</td>
<td align="right">8.0%</td>
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
<td align="right">880</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">560</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">360</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">260</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">80</td>
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
<td align="right">1,820</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">400</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">80</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">20</td>
<td align="right">0.9%</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">160</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">640</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">260</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">80</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">80</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">60</td>
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
<td align="left">LOAD_SPECIAL</td>
<td align="right">560</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">380</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">120</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">60</td>
<td align="right">5.1%</td>
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
<td align="left">CALL</td>
<td align="right">160</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">140</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">120</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">60</td>
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
<td align="left">RESUME</td>
<td align="right">240</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">240</td>
<td align="right">50.0%</td>
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
<td align="right">600</td>
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
<td align="right">400</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">200</td>
<td align="right">33.3%</td>
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
<td align="right">420</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">140</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">560</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">340</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">140</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">60</td>
<td align="right">11.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">280</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">140</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">60</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">60</td>
<td align="right">11.1%</td>
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
<td align="right">280</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">220</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">80</td>
<td align="right">13.8%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">300</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">80</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">80</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">80</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">40</td>
<td align="right">6.9%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">200</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">140</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">80</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
<td align="right">16.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">280</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">220</td>
<td align="right">44.0%</td>
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
<td align="right">160</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">80</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">80</td>
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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">320</td>
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
<td align="right">880</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">120</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">60</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">60</td>
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
<td align="right">680</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">260</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">80</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">60</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">40</td>
<td align="right">3.6%</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">140</td>
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
<td align="right">5,700</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,920</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">860</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">360</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">280</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">1,420</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,100</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">940</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">800</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">800</td>
<td align="right">8.4%</td>
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
<td align="right">1,440</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,120</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">960</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">880</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">240</td>
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
<td align="right">1,200</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,120</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">880</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">880</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">800</td>
<td align="right">12.2%</td>
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
<td align="right">420</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">280</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">240</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">140</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">140</td>
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
<td align="left">CALL</td>
<td align="right">400</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">340</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">140</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">140</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">140</td>
<td align="right">7.4%</td>
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
<td align="right">5,140</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,960</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,940</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,180</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,080</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">5,700</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,960</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,380</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,220</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,080</td>
<td align="right">4.8%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">920</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">600</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">600</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">500</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">400</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,160</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">920</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">820</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">680</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">440</td>
<td align="right">7.8%</td>
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
<td align="right">1,480</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,400</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">800</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">740</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">540</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">1,920</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,520</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,280</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">680</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">560</td>
<td align="right">6.9%</td>
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
<td align="right">1,140</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">340</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">80</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">80</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">360</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">340</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">340</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">240</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">160</td>
<td align="right">8.0%</td>
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
<td align="right">560</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">560</td>
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
<td align="right">560</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">400</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">120</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">40</td>
<td align="right">3.6%</td>
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
<td align="right">280</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">240</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">140</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">120</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">60</td>
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
<td align="right">320</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">280</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">240</td>
<td align="right">28.6%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">2,600</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,820</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,680</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,200</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">420</td>
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
<td align="right">5,140</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">740</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">600</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">440</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">420</td>
<td align="right">4.6%</td>
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
<td align="right">1,060</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">280</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">200</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">160</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
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
<td align="right">1,160</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">240</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">240</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">220</td>
<td align="right">11.8%</td>
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
<td align="right">2,080</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">380</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">320</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">140</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,620</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">340</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">240</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">200</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">200</td>
<td align="right">6.4%</td>
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
<td align="right">860</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">580</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">180</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">160</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">60</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">540</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">420</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">300</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">280</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">160</td>
<td align="right">8.4%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">420</td>
<td align="right">100.0%</td>
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
<td align="right">2,380</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">440</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">60</td>
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
<td align="right">960</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">940</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">500</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">180</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">120</td>
<td align="right">4.2%</td>
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
<td align="right">200</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">140</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">80</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">80</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">60</td>
<td align="right">10.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">280</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">200</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">80</td>
<td align="right">14.3%</td>
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
<td align="right">1,520</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">940</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">880</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">840</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">640</td>
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
<td align="right">4,940</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,480</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">980</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">880</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">840</td>
<td align="right">7.5%</td>
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
<td align="right">740</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">560</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">60</td>
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
<td align="right">540</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">400</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">240</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">120</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">4.4%</td>
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
<td align="right">620</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">560</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">200</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">80</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
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
<td align="left">SWAP</td>
<td align="right">620</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">560</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">200</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">80</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">60</td>
<td align="right">3.9%</td>
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
<td align="right">320</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">240</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">240</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">80</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">60</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">560</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">260</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">160</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">40</td>
<td align="right">3.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">140</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">200</td>
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
<td align="right">1,280</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">400</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">240</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">240</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">240</td>
<td align="right">9.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,200</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">800</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">80</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">80</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">80</td>
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
<td align="right">340</td>
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
<td align="right">340</td>
<td align="right">100.0%</td>
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
<td align="left">BINARY_OP</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">80</td>
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
<td align="right">160</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">100</td>
<td align="right">38.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">260</td>
<td align="right">100.0%</td>
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
<td align="left">CALL</td>
<td align="right">260</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">240</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">180</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">160</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">140</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">340</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">240</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">120</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">100</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">80</td>
<td align="right">7.8%</td>
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
<td align="right">700</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">160</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">40</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
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
<td align="left">STORE_FAST</td>
<td align="right">520</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">180</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">120</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">40</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">40</td>
<td align="right">4.3%</td>
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
<td align="left">CALL</td>
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
<td align="left">STORE_FAST</td>
<td align="right">80</td>
<td align="right">100.0%</td>
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
<td align="right">560</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">120</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">40</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">40</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">640</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">120</td>
<td align="right">15.8%</td>
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
<td align="left">CALL_KW</td>
<td align="right">140</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">120</td>
<td align="right">46.2%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">260</td>
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
<td align="right">380</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
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
<td align="left">BINARY_OP</td>
<td align="right">340</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">40</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">20</td>
<td align="right">5.0%</td>
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
<td align="right">800</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">100</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">80</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">40</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">40</td>
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
<td align="right">520</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">340</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">160</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">60</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">20</td>
<td align="right">1.8%</td>
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
<td align="right">120</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">100</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">40</td>
<td align="right">15.4%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">120</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">80</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">60</td>
<td align="right">23.1%</td>
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
<td align="left">BUILD_TUPLE</td>
<td align="right">160</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">140</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">40</td>
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
<td align="left">POP_TOP</td>
<td align="right">320</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">60</td>
<td align="right">15.8%</td>
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
<td align="left">CALL</td>
<td align="right">460</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">320</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">240</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">60</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
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
<td align="left">POP_TOP</td>
<td align="right">240</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">240</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">200</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">200</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">120</td>
<td align="right">8.8%</td>
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
<td align="right">600</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">400</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">140</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">120</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">120</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,540</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">60</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">60</td>
<td align="right">3.6%</td>
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
<td align="left">CALL</td>
<td align="right">240</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">200</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">160</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">120</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">560</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">120</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">120</td>
<td align="right">15.0%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">340</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">80</td>
<td align="right">19.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">420</td>
<td align="right">100.0%</td>
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
<td align="left">FOR_ITER</td>
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
<td align="left">POP_ITER</td>
<td align="right">80</td>
<td align="right">100.0%</td>
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
<td align="right">220</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">160</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">60</td>
<td align="right">13.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">300</td>
<td align="right">68.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">140</td>
<td align="right">31.8%</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">320</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">160</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">120</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">60</td>
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
<td align="right">280</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">220</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">160</td>
<td align="right">24.2%</td>
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
<td align="right">2,080</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,100</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">140</td>
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
<td align="left">TO_BOOL</td>
<td align="right">520</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">380</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">360</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">320</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">240</td>
<td align="right">7.2%</td>
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
<td align="right">1,000</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">360</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">320</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">80</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">40</td>
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
<td align="right">920</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">260</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">140</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">120</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">120</td>
<td align="right">6.7%</td>
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
<td align="right">600</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">400</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">40</td>
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
<td align="right">440</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">300</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">120</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">60</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">60</td>
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
<td align="right">1,620</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">940</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">160</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">1,640</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">180</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">160</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">140</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">120</td>
<td align="right">4.3%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">120</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">80</td>
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
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">80</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">80</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">40</td>
<td align="right">20.0%</td>
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
<td align="right">1,540</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">920</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">780</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">740</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">580</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">1,620</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,060</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">940</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">780</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">360</td>
<td align="right">5.7%</td>
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
<td align="right">380</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">260</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">200</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">120</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">80</td>
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
<td align="left">MAKE_FUNCTION</td>
<td align="right">260</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">200</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">180</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">140</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">120</td>
<td align="right">7.9%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">720</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">680</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">520</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">340</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">240</td>
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
<td align="right">2,080</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">560</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">160</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">120</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">100</td>
<td align="right">3.0%</td>
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
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,520</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,100</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">980</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">360</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">320</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,620</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">860</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">780</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">280</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">240</td>
<td align="right">4.8%</td>
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
<td align="right">1,540</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">1,040</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">560</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">480</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">320</td>
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
<td align="right">1,880</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,100</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">540</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">520</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">180</td>
<td align="right">3.9%</td>
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
<td align="right">1,460</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">500</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">100</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">920</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">840</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">120</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">120</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">2.9%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">680</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">640</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">260</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">240</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">240</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,680</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">580</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">60</td>
<td align="right">2.6%</td>
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
<td align="right">400</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">40</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">20</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">400</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">60</td>
<td align="right">13.0%</td>
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
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">260</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">120</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">120</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">120</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">100</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">740</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">7.5%</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">60</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">60</td>
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
<td align="right">160</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">80</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">60</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">60</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">40</td>
<td align="right">16.7%</td>
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
<td align="right">120</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">100</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">80</td>
<td align="right">26.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">240</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">40</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
<td align="right">6.7%</td>
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
<td align="right">80</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">40</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">50.0%</td>
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
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">40</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">40</td>
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
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">50.0%</td>
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
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">BUILD_LIST</td>
<td align="right">60</td>
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
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20</td>
<td align="right">33.3%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">400</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">360</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">240</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">120</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">40</td>
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
<td align="right">1,200</td>
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
<td align="right">80</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">40</td>
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
<td align="left">POP_ITER</td>
<td align="right">120</td>
<td align="right">100.0%</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">60</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">80</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">60</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">40</td>
<td align="right">22.2%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">120</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60</td>
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
<td align="left">CALL_TYPE_1</td>
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">40</td>
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
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">40</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">40</td>
<td align="right">33.3%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">100.0%</td>
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
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">60</td>
<td align="right">100.0%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">80</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">80</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">40</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">240</td>
<td align="right">100.0%</td>
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
<td align="left">COPY</td>
<td align="right">120</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">80</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">40</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">180</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">120</td>
<td align="right">40.0%</td>
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
<td align="right">80</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">40</td>
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
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">60</td>
<td align="right">50.0%</td>
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
<td align="right">1,200</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,040</td>
<td align="right">38.8%</td>
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
<td align="right">260</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">180</td>
<td align="right">40.9%</td>
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
<td align="left">multiply different types</td>
<td align="right">100</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">40</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">20</td>
<td align="right">11.1%</td>
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
<td align="right">400</td>
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
<td align="right">5,680</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,200</td>
<td align="right">47.5%</td>
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
<td align="right">2,280</td>
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
<td align="right">320</td>
<td align="right">64.0%</td>
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
<td align="right">1,820</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,480</td>
<td align="right">37.6%</td>
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
<td align="right">3.6%</td>
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
<td align="right">480</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">4.0%</td>
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
<td align="right">20</td>
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
<td align="right">160</td>
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
<td align="right">380</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">640</td>
<td align="right">52.5%</td>
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
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">80</td>
<td align="right">40.0%</td>
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
<td align="left">dict values</td>
<td align="right">80</td>
<td align="right">100.0%</td>
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
<td align="right">6,500</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,200</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">280</td>
<td align="right">1.5%</td>
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
<td align="right">3,020</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">1.3%</td>
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
<td align="right">5,920</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,640</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">660</td>
<td align="right">4.0%</td>
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
<td align="right">2,200</td>
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
<td align="right">2,320</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,060</td>
<td align="right">41.7%</td>
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
<td align="right">500</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60</td>
<td align="right">10.7%</td>
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
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">20</td>
<td align="right">33.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">60</td>
<td align="right">75.0%</td>
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
<td align="right">3,600</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,180</td>
<td align="right">39.8%</td>
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
<td align="right">1.8%</td>
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
<td align="right">880</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">200</td>
<td align="right">18.5%</td>
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
<td align="right">100</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">40</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">20</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">20</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">20</td>
<td align="right">10.0%</td>
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
<td align="right">720</td>
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
<td align="right">920</td>
<td align="right">47.4%</td>
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
<td align="right">300</td>
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
<td align="right">126,260</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">39,840</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">49,240</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,220</td>
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
<td align="right">6,500</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">5,920</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,680</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,600</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,320</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,820</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,200</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">720</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">400</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">380</td>
<td align="right">1.3%</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">660</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">280</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">140</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">140</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">0</td>
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
<td align="right">1,640</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,680</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,640</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,240</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">400</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,240</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">480</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">200</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">200</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,920</td>
<td align="right">94.5%</td>
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
<td align="right">11,721</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,661</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">14,280</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">13,880</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">140</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">260</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,950</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">540</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">62,860</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">84,340</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">52,837</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">51,651</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">39,640</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">50,240</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">52,024</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">46,657</td>
<td align="right">20.0%</td>
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
<td align="right">9,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">5,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">5,704</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,523</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,657</td>
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
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
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
<td align="right">0</td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right"></td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">0</td>
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
<td align="right">0</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### JIT trace total memory histogram

<details>
<summary> JIT trace total memory histogram </summary>


</details>

### Trace length histogram

<details>
<summary> trace length histogram </summary>


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>


</details>

### Uop execution stats

<details>
<summary> uop execution stats </summary>


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
<td align="right">100</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-14
