
# Pystats results

- benchmark: scimark
- fork: faster-cpython
- ref: explicit-check-periodic
- commit hash: be0ebdc
- commit date: 2025-06-20T18:48:55+01:00

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
<td align="right">1,251,473,227</td>
<td align="right">15.8%</td>
<td align="right">15.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">795,629,116</td>
<td align="right">10.1%</td>
<td align="right">25.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">532,147,535</td>
<td align="right">6.7%</td>
<td align="right">32.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">528,720,133</td>
<td align="right">6.7%</td>
<td align="right">39.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">423,128,068</td>
<td align="right">5.4%</td>
<td align="right">44.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">294,775,420</td>
<td align="right">3.7%</td>
<td align="right">48.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">292,710,500</td>
<td align="right">3.7%</td>
<td align="right">52.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">279,807,642</td>
<td align="right">3.5%</td>
<td align="right">55.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">260,606,976</td>
<td align="right">3.3%</td>
<td align="right">58.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">260,600,320</td>
<td align="right">3.3%</td>
<td align="right">62.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">255,717,591</td>
<td align="right">3.2%</td>
<td align="right">65.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">237,260,977</td>
<td align="right">3.0%</td>
<td align="right">68.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">203,384,145</td>
<td align="right">2.6%</td>
<td align="right">71.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">194,484,552</td>
<td align="right">2.5%</td>
<td align="right">73.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">181,182,750</td>
<td align="right">2.3%</td>
<td align="right">75.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">152,359,069</td>
<td align="right">1.9%</td>
<td align="right">77.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">152,323,687</td>
<td align="right">1.9%</td>
<td align="right">79.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">151,938,738</td>
<td align="right">1.9%</td>
<td align="right">81.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">151,719,514</td>
<td align="right">1.9%</td>
<td align="right">83.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">151,446,075</td>
<td align="right">1.9%</td>
<td align="right">85.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">150,818,076</td>
<td align="right">1.9%</td>
<td align="right">87.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">112,494,004</td>
<td align="right">1.4%</td>
<td align="right">88.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">94,440,881</td>
<td align="right">1.2%</td>
<td align="right">89.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">86,771,532</td>
<td align="right">1.1%</td>
<td align="right">91.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">77,931,642</td>
<td align="right">1.0%</td>
<td align="right">92.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">75,355,588</td>
<td align="right">1.0%</td>
<td align="right">92.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">64,360,254</td>
<td align="right">0.8%</td>
<td align="right">93.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">64,348,094</td>
<td align="right">0.8%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">51,097,220</td>
<td align="right">0.6%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">50,478,119</td>
<td align="right">0.6%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">50,451,505</td>
<td align="right">0.6%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">44,404,466</td>
<td align="right">0.6%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">38,160,008</td>
<td align="right">0.5%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">37,526,075</td>
<td align="right">0.5%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">27,144,220</td>
<td align="right">0.3%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">26,972,956</td>
<td align="right">0.3%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">21,773,866</td>
<td align="right">0.3%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">20,370,271</td>
<td align="right">0.3%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">13,580,987</td>
<td align="right">0.2%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">13,177,664</td>
<td align="right">0.2%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">8,136,019</td>
<td align="right">0.1%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">8,135,695</td>
<td align="right">0.1%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">6,798,742</td>
<td align="right">0.1%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,716,798</td>
<td align="right">0.1%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,280,317</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">661,396</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">640,063</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">640,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">451,385</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">233,458</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">193,273</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">143,872</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">131,072</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">130,980</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">80,305</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">15,233</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">13,976</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">12,159</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,905</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,610</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,351</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,658</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">648</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">648</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">638</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">612</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">549</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">378</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">378</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">319</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">319</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">319</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">252</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">192</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">192</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">118</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">67</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">64</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">64</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">44</td>
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
<td align="left">STORE_FAST LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">260,890,264</td>
<td align="right">3.3%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">222,557,841</td>
<td align="right">2.8%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW BINARY_OP</td>
<td align="right">204,102,112</td>
<td align="right">2.6%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">194,414,153</td>
<td align="right">2.5%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_BORROW</td>
<td align="right">181,698,244</td>
<td align="right">2.3%</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_OP_ADD_INT</td>
<td align="right">162,671,224</td>
<td align="right">2.1%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_FAST_BORROW</td>
<td align="right">157,324,800</td>
<td align="right">2.0%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_SMALL_INT</td>
<td align="right">154,011,320</td>
<td align="right">1.9%</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC JUMP_BACKWARD_NO_JIT</td>
<td align="right">144,104,859</td>
<td align="right">1.8%</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE STORE_FAST</td>
<td align="right">144,057,050</td>
<td align="right">1.8%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW</td>
<td align="right">141,956,205</td>
<td align="right">1.8%</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP LOAD_FAST_BORROW</td>
<td align="right">137,942,746</td>
<td align="right">1.7%</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_RANGE</td>
<td align="right">137,698,522</td>
<td align="right">1.7%</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">124,847,980</td>
<td align="right">1.6%</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_SMALL_INT</td>
<td align="right">121,418,092</td>
<td align="right">1.5%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_ADD_INT</td>
<td align="right">118,941,750</td>
<td align="right">1.5%</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">114,940,955</td>
<td align="right">1.5%</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">111,232,716</td>
<td align="right">1.4%</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">111,020,160</td>
<td align="right">1.4%</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP STORE_FAST</td>
<td align="right">105,024,958</td>
<td align="right">1.3%</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT BINARY_OP_ADD_FLOAT</td>
<td align="right">97,200,550</td>
<td align="right">1.2%</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM RESUME_CHECK</td>
<td align="right">94,440,881</td>
<td align="right">1.2%</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">COPY BINARY_OP</td>
<td align="right">93,420,800</td>
<td align="right">1.2%</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">COPY COPY</td>
<td align="right">93,420,800</td>
<td align="right">1.2%</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">SWAP STORE_SUBSCR</td>
<td align="right">93,420,800</td>
<td align="right">1.2%</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">SWAP SWAP</td>
<td align="right">93,420,800</td>
<td align="right">1.2%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW</td>
<td align="right">78,420,629</td>
<td align="right">1.0%</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT STORE_FAST</td>
<td align="right">78,170,798</td>
<td align="right">1.0%</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">78,165,754</td>
<td align="right">1.0%</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">77,931,323</td>
<td align="right">1.0%</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST SWAP</td>
<td align="right">73,758,720</td>
<td align="right">0.9%</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT LOAD_FAST</td>
<td align="right">73,758,720</td>
<td align="right">0.9%</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE JUMP_FORWARD</td>
<td align="right">73,758,720</td>
<td align="right">0.9%</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">SWAP COPY</td>
<td align="right">73,758,720</td>
<td align="right">0.9%</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">COPY COMPARE_OP_INT</td>
<td align="right">73,758,716</td>
<td align="right">0.9%</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT</td>
<td align="right">73,758,716</td>
<td align="right">0.9%</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">72,964,441</td>
<td align="right">0.9%</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT BINARY_OP</td>
<td align="right">72,923,863</td>
<td align="right">0.9%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT LOAD_FAST_BORROW</td>
<td align="right">72,217,476</td>
<td align="right">0.9%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">71,682,764</td>
<td align="right">0.9%</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR CHECK_PERIODIC</td>
<td align="right">71,248,024</td>
<td align="right">0.9%</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST CHECK_PERIODIC</td>
<td align="right">70,165,552</td>
<td align="right">0.9%</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">66,684,790</td>
<td align="right">0.8%</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT STORE_FAST</td>
<td align="right">65,667,385</td>
<td align="right">0.8%</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_SMALL_INT</td>
<td align="right">65,561,732</td>
<td align="right">0.8%</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT SWAP</td>
<td align="right">65,535,996</td>
<td align="right">0.8%</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_ADD_FLOAT</td>
<td align="right">65,535,992</td>
<td align="right">0.8%</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">64,360,508</td>
<td align="right">0.8%</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE CHECK_PERIODIC</td>
<td align="right">64,360,254</td>
<td align="right">0.8%</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC TO_BOOL_BOOL</td>
<td align="right">64,360,252</td>
<td align="right">0.8%</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_GLOBAL_BUILTIN</td>
<td align="right">64,360,252</td>
<td align="right">0.8%</td>
<td align="right">68.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE</td>
<td align="right">64,360,252</td>
<td align="right">0.8%</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT RETURN_VALUE</td>
<td align="right">63,708,095</td>
<td align="right">0.8%</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">63,708,094</td>
<td align="right">0.8%</td>
<td align="right">70.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">63,708,076</td>
<td align="right">0.8%</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE LOAD_FAST_BORROW</td>
<td align="right">63,695,928</td>
<td align="right">0.8%</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT BINARY_OP_MULTIPLY_INT</td>
<td align="right">58,988,794</td>
<td align="right">0.7%</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">57,249,352</td>
<td align="right">0.7%</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT STORE_FAST</td>
<td align="right">52,758,266</td>
<td align="right">0.7%</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT LOAD_FAST_BORROW</td>
<td align="right">52,505,597</td>
<td align="right">0.7%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP BINARY_OP</td>
<td align="right">52,090,697</td>
<td align="right">0.7%</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">51,950,136</td>
<td align="right">0.7%</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">50,477,737</td>
<td align="right">0.6%</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_BORROW</td>
<td align="right">50,467,759</td>
<td align="right">0.6%</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">50,319,816</td>
<td align="right">0.6%</td>
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_FAST_BORROW</td>
<td align="right">48,987,036</td>
<td align="right">0.6%</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT STORE_SUBSCR</td>
<td align="right">42,584,794</td>
<td align="right">0.5%</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BINARY_OP</td>
<td align="right">42,384,490</td>
<td align="right">0.5%</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW COPY</td>
<td align="right">39,321,600</td>
<td align="right">0.5%</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">38,475,904</td>
<td align="right">0.5%</td>
<td align="right">80.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_OP_SUBTRACT_INT</td>
<td align="right">37,921,254</td>
<td align="right">0.5%</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">37,526,075</td>
<td align="right">0.5%</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">36,892,406</td>
<td align="right">0.5%</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_SMALL_INT</td>
<td align="right">36,885,821</td>
<td align="right">0.5%</td>
<td align="right">82.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD LOAD_SMALL_INT</td>
<td align="right">36,879,360</td>
<td align="right">0.5%</td>
<td align="right">83.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT RETURN_VALUE</td>
<td align="right">36,879,359</td>
<td align="right">0.5%</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT LOAD_FAST_BORROW</td>
<td align="right">36,879,359</td>
<td align="right">0.5%</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE BINARY_OP_MULTIPLY_INT</td>
<td align="right">36,879,358</td>
<td align="right">0.5%</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">36,879,358</td>
<td align="right">0.5%</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">36,879,356</td>
<td align="right">0.5%</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW STORE_SUBSCR</td>
<td align="right">35,954,560</td>
<td align="right">0.5%</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">33,813,696</td>
<td align="right">0.4%</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT COPY</td>
<td align="right">32,767,998</td>
<td align="right">0.4%</td>
<td align="right">86.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT LOAD_FAST_BORROW</td>
<td align="right">32,703,226</td>
<td align="right">0.4%</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT STORE_FAST</td>
<td align="right">32,035,192</td>
<td align="right">0.4%</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">31,373,124</td>
<td align="right">0.4%</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP RETURN_VALUE</td>
<td align="right">30,732,811</td>
<td align="right">0.4%</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE BINARY_OP</td>
<td align="right">30,732,803</td>
<td align="right">0.4%</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">30,732,790</td>
<td align="right">0.4%</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT COMPARE_OP_INT</td>
<td align="right">27,223,052</td>
<td align="right">0.3%</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">27,142,594</td>
<td align="right">0.3%</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW</td>
<td align="right">27,142,328</td>
<td align="right">0.3%</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_OP</td>
<td align="right">26,144,660</td>
<td align="right">0.3%</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">25,766,392</td>
<td align="right">0.3%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW BUILD_TUPLE</td>
<td align="right">25,226,564</td>
<td align="right">0.3%</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">24,926,137</td>
<td align="right">0.3%</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS CHECK_PERIODIC</td>
<td align="right">21,773,866</td>
<td align="right">0.3%</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW COPY</td>
<td align="right">21,331,200</td>
<td align="right">0.3%</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT SWAP</td>
<td align="right">21,014,399</td>
<td align="right">0.3%</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW COMPARE_OP_INT</td>
<td align="right">19,724,790</td>
<td align="right">0.2%</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">8,135,116</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,071,474</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">64,064</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">94</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">63</td>
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
<td align="right">6,799,051</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1</td>
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
<td align="right">648</td>
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
<td align="right">319</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5</td>
<td align="right">1.5%</td>
</tr>
</tbody>
</table>


</details>

### CHECK_PERIODIC

<details>
<summary> Successors and predecessors for CHECK_PERIODIC </summary>

<table>
<thead>
<tr>
<th align="left">Predecessors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">71,248,024</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">70,165,552</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">64,360,254</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">21,773,866</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">6,945,199</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">144,104,859</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">64,360,252</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">13,635,064</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">8,135,116</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,553,600</td>
<td align="right">2.8%</td>
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
<td align="right">378</td>
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
<td align="right">378</td>
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
<td align="right">6,798,741</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">324</td>
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
<td align="right">324</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">324</td>
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
<td align="right">324</td>
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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">8,135,566</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">389</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">6,945,199</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,051,736</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">64,388</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">64,040</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,856</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">639,999</td>
<td align="right">96.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">20,656</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">676</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">640,000</td>
<td align="right">96.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">9,600</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,428</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,707</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,240</td>
<td align="right">0.5%</td>
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
<td align="right">129,274</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,036</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">324</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">324</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">128,648</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">856</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">648</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">440</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">388</td>
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
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">63,708,095</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">36,879,359</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">30,732,811</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">13,571,132</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,819,788</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">63,695,928</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">30,732,803</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">18,439,674</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,807,543</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">6,798,741</td>
<td align="right">4.5%</td>
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
<td align="left">SWAP</td>
<td align="right">93,420,800</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">42,584,794</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">35,954,560</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">17,794,138</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">6,786,560</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">111,020,160</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">71,248,024</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,639,136</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,786,561</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">639,999</td>
<td align="right">0.3%</td>
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
<td align="right">322</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">110</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">105</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">4</td>
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
<td align="right">329</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">110</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">105</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5</td>
<td align="right">0.9%</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">204,102,112</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">93,420,800</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">72,923,863</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">52,090,697</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">42,384,490</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">137,942,746</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">114,940,955</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">105,024,958</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">72,964,441</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">52,090,697</td>
<td align="right">9.9%</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">13,460</td>
<td align="right">96.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">324</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">192</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">13,238</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">324</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">222</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">192</td>
<td align="right">1.4%</td>
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
<td align="right">25,226,564</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">6,146,559</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">6,146,559</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">640,324</td>
<td align="right">1.7%</td>
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
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">30,732,790</td>
<td align="right">80.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">6,786,560</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">640,000</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">214</td>
<td align="right">0.0%</td>
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
<td align="right">584</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">440</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">340</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">244</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">222</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">799</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">705</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">357</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">126</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">105</td>
<td align="right">4.0%</td>
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
<td align="right">324</td>
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
<td align="right">324</td>
<td align="right">100.0%</td>
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
<td align="right">13,577,556</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,403</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">13,577,497</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,403</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">93,420,800</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">73,758,720</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">39,321,600</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">32,767,998</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">21,331,200</td>
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
<td align="left">BINARY_OP</td>
<td align="right">93,420,800</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">93,420,800</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">73,758,716</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
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
<td align="right">319</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">319</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5</td>
<td align="right">1.5%</td>
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
<td align="right">6,754</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">94</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">53</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4</td>
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
<td align="right">6,398</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">389</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">53</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">31</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">29</td>
<td align="right">0.4%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">324</td>
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
<td align="right">324</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">73,758,720</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,596,868</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">38,475,904</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">36,879,360</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">324</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">324</td>
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
<td align="right">324</td>
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
<td align="right">1,099</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">423</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">346</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">210</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">116</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">449</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">423</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">363</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">333</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">331</td>
<td align="right">14.1%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">6,786,561</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">6,399,999</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,211,336</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">6,210,558</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,235,364</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">6,819,788</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,399,998</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,275,712</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">6,146,600</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,171,172</td>
<td align="right">4.3%</td>
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
<td align="left">BUILD_LIST</td>
<td align="right">324</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">319</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">324</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">324</td>
<td align="right">50.0%</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">73,758,720</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,992,968</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">19,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">73,758,720</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,011,840</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">214</td>
<td align="right">0.0%</td>
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
<td align="right">181,698,244</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">157,324,800</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">141,956,205</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">137,942,746</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">111,232,716</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">222,557,841</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">157,324,800</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">124,847,980</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">121,418,092</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">118,941,750</td>
<td align="right">9.5%</td>
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
<td align="right">260,890,264</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">114,940,955</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">111,020,160</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">78,165,754</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">51,950,136</td>
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
<td align="left">BINARY_OP</td>
<td align="right">204,102,112</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">154,011,320</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">63,708,076</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">57,249,352</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">51,950,136</td>
<td align="right">6.5%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">319</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">214</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">110</td>
<td align="right">34.0%</td>
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
<td align="right">744</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">444</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">156</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">148</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">24</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,018</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">531</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">37</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">23</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">22</td>
<td align="right">1.3%</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">154,011,320</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">121,418,092</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">65,561,732</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">36,885,821</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">36,879,360</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">162,671,224</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">73,758,720</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">72,217,476</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">37,921,254</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">27,223,052</td>
<td align="right">6.4%</td>
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
<td align="left">CALL_PY_GENERAL</td>
<td align="right">319</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">319</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5</td>
<td align="right">1.5%</td>
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
<td align="right">194,414,153</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">77,931,323</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">13,577,497</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,716,798</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">70,400</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">181,698,244</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">73,758,720</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">33,813,696</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">1,659,712</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,599,944</td>
<td align="right">0.5%</td>
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
<td align="right">192</td>
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
<td align="right">192</td>
<td align="right">100.0%</td>
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
<td align="right">324</td>
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
<td align="right">324</td>
<td align="right">100.0%</td>
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
<td align="right">319</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">5</td>
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
<td align="left">NOP</td>
<td align="right">324</td>
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
<td align="right">324</td>
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
<td align="right">324</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">486</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">126</td>
<td align="right">20.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">576</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">15</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">8</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3</td>
<td align="right">0.5%</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">324</td>
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
<td align="right">324</td>
<td align="right">100.0%</td>
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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">144,057,050</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">105,024,958</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">78,170,798</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">65,667,385</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">52,758,266</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">260,890,264</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">111,232,716</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">70,165,552</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">65,561,732</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,992,968</td>
<td align="right">2.4%</td>
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
<td align="right">37,526,075</td>
<td align="right">73.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,571,132</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">31,373,124</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,571,072</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,152,960</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">22</td>
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
<td align="left">SWAP</td>
<td align="right">93,420,800</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">73,758,720</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">65,535,996</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">21,014,399</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">6,870,398</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">93,420,800</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">93,420,800</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">73,758,720</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">192</td>
<td align="right">0.0%</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">110</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">109</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">9</td>
<td align="right">7.6%</td>
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
<td align="right">97,200,550</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">65,535,992</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">18,439,674</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">6,516</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">STORE_FAST</td>
<td align="right">78,170,798</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">65,535,996</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">24,926,137</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,399,999</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">6,146,558</td>
<td align="right">3.4%</td>
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
<td align="right">162,671,224</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">118,941,750</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">13,162,394</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">52</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">72,923,863</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">58,988,794</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">42,584,794</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">36,879,359</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">32,767,998</td>
<td align="right">11.1%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">124,847,980</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">72,964,441</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">25,766,392</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">13,635,064</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,146,600</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">97,200,550</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">66,684,790</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">52,505,597</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">13,571,132</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">12,546,558</td>
<td align="right">4.9%</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">58,988,794</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">36,879,358</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">13,094,436</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,403,344</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">127,996</td>
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
<td align="right">65,667,385</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">36,879,359</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,547,196</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">3,399,999</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">63</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">63,708,076</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">30,732,790</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">94,440,881</td>
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
<td align="right">1,280,210</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">639,999</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">639,998</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">71,682,764</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">66,684,790</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">13,571,184</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">78,165,754</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">52,758,266</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">21,014,399</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">319</td>
<td align="right">0.0%</td>
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
<td align="right">37,921,254</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,483,198</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">32,035,192</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">6,146,559</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,146,559</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">63,356</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">12,796</td>
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
<td align="left">CALL</td>
<td align="right">126</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">126</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">126</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">378</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">14,117,393</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">6,547,196</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,038,998</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">63,356</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,440</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">21,773,866</td>
<td align="right">100.0%</td>
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
<td align="right">214</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">105</td>
<td align="right">32.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">319</td>
<td align="right">100.0%</td>
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
<td align="right">214</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">105</td>
<td align="right">32.9%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">319</td>
<td align="right">100.0%</td>
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
<td align="left">BUILD_LIST</td>
<td align="right">13,238</td>
<td align="right">86.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">856</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">799</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">214</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">42</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">15,233</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">36,892,406</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">13,571,106</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,822</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,412</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,198</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">50,477,737</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">63</td>
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
<td align="right">214</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">105</td>
<td align="right">32.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">319</td>
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
<td align="left">COPY</td>
<td align="right">73,758,716</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">73,758,716</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">27,223,052</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">19,724,790</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">12,796</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">194,414,153</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">70,399</td>
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
<td align="right">137,698,522</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">8,071,474</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,553,660</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="right">144,057,050</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">8,135,566</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">131,071</td>
<td align="right">0.1%</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">144,104,859</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,553,596</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">639,999</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">143,870</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,707</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">137,698,522</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,611,200</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,489,600</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">639,999</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,754</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">222,557,841</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">57,249,352</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">449</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">141,956,205</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">73,758,716</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">36,879,358</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">13,571,132</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">13,571,066</td>
<td align="right">4.9%</td>
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
<td align="right">428</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">210</td>
<td align="right">32.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">319</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">214</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">105</td>
<td align="right">16.5%</td>
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
<td align="right">50,319,816</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">131,070</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">363</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">36,879,358</td>
<td align="right">73.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,571,106</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">634</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">42</td>
<td align="right">0.0%</td>
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
<td align="right">192,850</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">423</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">129,274</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">63,998</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">64,360,508</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">64,360,252</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">13,571,066</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,323,041</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">70,934</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">78,420,629</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">64,360,252</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">6,674,744</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,362,449</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">148,222</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">63,998</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">12,796</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,840</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,240</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">192,850</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">19,833</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">13,638</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">6,525</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">423</td>
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
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">94,440,881</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">50,477,737</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">6,799,051</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">639,999</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">64,360,508</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">50,467,759</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">36,885,821</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">639,999</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">27,142,594</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,050</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">576</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">27,142,328</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">945</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">189</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">64,360,252</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">13,571,066</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">110</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">77,931,323</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">319</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">36,879,356</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">639,998</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">109</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">37,526,075</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">6,553,600</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,489,600</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">70,399</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">64,064</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">6,553,660</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">6,553,596</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">70,400</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">4</td>
<td align="right">0.0%</td>
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
<td align="right">131,071</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">12,800</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">143,870</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">192</td>
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
<td align="right">192</td>
<td align="right">100.0%</td>
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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">131,071</td>
<td align="right">100.0%</td>
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
<td align="right">131,070</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">67,298</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,516</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">3,258</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">3,198</td>
<td align="right">4.0%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">63,998</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">6,516</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,261</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">3,258</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,199</td>
<td align="right">4.0%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">126</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">84</td>
<td align="right">33.3%</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">252</td>
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
<td align="left">BINARY_OP</td>
<td align="right">387,194</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">64,124</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">67</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">451,385</td>
<td align="right">100.0%</td>
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
<td align="right">13,574,576</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,795,362</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">333</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">13,571,066</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,792,491</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">3,261</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,261</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">126</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">6,399,998</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">316,798</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
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
<td align="right">6,716,798</td>
<td align="right">100.0%</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">28</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">44</td>
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
<td align="right">36</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">14</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">5</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">5</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">5</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">29</td>
<td align="right">43.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">24</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">5</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">5</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3</td>
<td align="right">4.5%</td>
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
<td align="right">64</td>
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
<td align="right">64</td>
<td align="right">100.0%</td>
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
<td align="right">63</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1</td>
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
<td align="left">GET_ITER</td>
<td align="right">63</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right">1</td>
<td align="right">1.6%</td>
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
<td align="right">640,000</td>
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
<td align="right">639,998</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">63,708,094</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">639,998</td>
<td align="right">1.0%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">63,708,095</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">639,999</td>
<td align="right">1.0%</td>
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
<td align="right">64,360,252</td>
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
<td align="left">CHECK_PERIODIC</td>
<td align="right">64,360,254</td>
<td align="right">100.0%</td>
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
<td align="right">639,999</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">63</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">639,999</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,158</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">12,159</td>
<td align="right">100.0%</td>
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
<td align="right">528,588,602</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,265,010,660</td>
<td align="right">70.5%</td>
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
<td align="right">482</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">131,049</td>
<td align="right">99.6%</td>
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
<td align="left">subscr array</td>
<td align="right">121,438</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">3,265</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,197</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,671</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">459</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">442</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">263</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">167</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">147</td>
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
<td align="right">155</td>
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
<td align="right">137,064,892</td>
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
<td align="right">2,455</td>
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
<td align="right">13,577,498</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">201,201,350</td>
<td align="right">93.7%</td>
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
<td align="right">86</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,403</td>
<td align="right">97.5%</td>
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
<td align="right">3,403</td>
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
<td align="right">6,820</td>
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
<td align="right">152,963,750</td>
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
<td align="right">32</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">53</td>
<td align="right">62.4%</td>
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
<td align="right">47</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6</td>
<td align="right">11.3%</td>
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
<td align="right">8,135,567</td>
<td align="right">8,135,567 / 0 !!</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">64</td>
<td align="right">64 / 0 !!</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">64</td>
<td align="right">64 / 0 !!</td>
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
<td align="right">467</td>
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
<td align="right">350,823,329</td>
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
<td align="right">1,778</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">106</td>
<td align="right">5.6%</td>
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
<td align="right">109</td>
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
<td align="right">151,051,534</td>
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
<td align="right">1,549</td>
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
<td align="right">27,144,220</td>
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
<td align="right">576</td>
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
<td align="right">203,333,949</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,159</td>
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
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">50,195</td>
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
<td align="left">array int</td>
<td align="right">48,371</td>
<td align="right">96.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">1,756</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.1%</td>
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
<td align="right">334</td>
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
<td align="right">77,931,642</td>
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
<td align="right">110</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">105</td>
<td align="right">48.8%</td>
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
<td align="right">105</td>
<td align="right">100.0%</td>
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
<td align="right">37,526,075</td>
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
<td align="right">109</td>
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
<td align="right">4,513,473,443</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">753,835,763</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">2,640,202,213</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">528,588,602</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">203,333,949</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">13,577,498</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">467</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">334</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">109</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### Misses by instruction

<details>
<summary> Breakdown of misses (specialized deopts) instruction counts by family </summary>


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
<td align="right">6,799,066</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">145,560,134</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">6,799,066</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,799,065</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,799,065</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">6,798,735</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">324</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">151,719,514</td>
<td align="right">99.6%</td>
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
<td align="right">1,562,006,390</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">1,562,006,134</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">194,337</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">181,005</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">12,868</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">464</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">193,791</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">384</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">663,930,859</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,576,731,562</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">580,351,092</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,229,708,585</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">33,942,388</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">40,719,700</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">422,817,712</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">439,303,374</td>
<td align="right">13.4%</td>
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
<td align="right">2,236</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">304</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">332</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">70,763,643</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">127</td>
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
<td align="right">105</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-22
