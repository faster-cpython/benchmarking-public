
# Pystats results

- benchmark: raytrace
- fork: brandtbucher
- ref: chain-depth-5
- commit hash: dc27e14
- commit date: 2024-12-12T09:22:12-08:00

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
<td align="right">395,754,920</td>
<td align="right">24.0%</td>
<td align="right">24.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">259,962,380</td>
<td align="right">15.7%</td>
<td align="right">39.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">173,889,680</td>
<td align="right">10.5%</td>
<td align="right">50.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">82,573,480</td>
<td align="right">5.0%</td>
<td align="right">55.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">65,489,120</td>
<td align="right">4.0%</td>
<td align="right">59.2%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">60,696,360</td>
<td align="right">3.7%</td>
<td align="right">62.9%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">50,365,800</td>
<td align="right">3.0%</td>
<td align="right">65.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">50,339,280</td>
<td align="right">3.0%</td>
<td align="right">69.0%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">46,451,720</td>
<td align="right">2.8%</td>
<td align="right">71.8%</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">40,256,160</td>
<td align="right">2.4%</td>
<td align="right">74.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">39,133,120</td>
<td align="right">2.4%</td>
<td align="right">76.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">33,664,600</td>
<td align="right">2.0%</td>
<td align="right">78.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">33,388,200</td>
<td align="right">2.0%</td>
<td align="right">80.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">30,385,440</td>
<td align="right">1.8%</td>
<td align="right">82.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">30,333,720</td>
<td align="right">1.8%</td>
<td align="right">84.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">26,795,280</td>
<td align="right">1.6%</td>
<td align="right">85.9%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">23,940,160</td>
<td align="right">1.4%</td>
<td align="right">87.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">21,059,120</td>
<td align="right">1.3%</td>
<td align="right">88.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,520,600</td>
<td align="right">1.2%</td>
<td align="right">89.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">19,112,340</td>
<td align="right">1.2%</td>
<td align="right">91.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">18,690,320</td>
<td align="right">1.1%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">18,511,920</td>
<td align="right">1.1%</td>
<td align="right">93.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">10,448,680</td>
<td align="right">0.6%</td>
<td align="right">93.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">8,688,720</td>
<td align="right">0.5%</td>
<td align="right">94.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,114,740</td>
<td align="right">0.4%</td>
<td align="right">94.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">6,450,420</td>
<td align="right">0.4%</td>
<td align="right">95.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">5,983,540</td>
<td align="right">0.4%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">5,875,200</td>
<td align="right">0.4%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">5,534,960</td>
<td align="right">0.3%</td>
<td align="right">96.3%</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">5,489,460</td>
<td align="right">0.3%</td>
<td align="right">96.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,877,700</td>
<td align="right">0.3%</td>
<td align="right">97.0%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,919,980</td>
<td align="right">0.2%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,488,680</td>
<td align="right">0.2%</td>
<td align="right">97.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,424,500</td>
<td align="right">0.2%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,117,960</td>
<td align="right">0.2%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,500,500</td>
<td align="right">0.2%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,403,560</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,237,720</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,175,880</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,046,240</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,855,900</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,836,120</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,831,800</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,831,800</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,813,380</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">1,669,620</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,569,440</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,545,420</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,530,540</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,511,880</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">983,540</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">969,260</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">919,980</td>
<td align="right">0.1%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">832,680</td>
<td align="right">0.1%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">616,440</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">614,760</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">600,180</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">600,060</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">600,060</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">319,980</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">288,340</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">258,360</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">231,420</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">860</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">580</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20</td>
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
<td align="left">LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">258,090,860</td>
<td align="right">15.6%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">124,416,500</td>
<td align="right">7.5%</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">63,418,440</td>
<td align="right">3.8%</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">62,954,360</td>
<td align="right">3.8%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">55,486,280</td>
<td align="right">3.4%</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR RETURN_VALUE</td>
<td align="right">46,839,040</td>
<td align="right">2.8%</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">41,019,740</td>
<td align="right">2.5%</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">36,233,020</td>
<td align="right">2.2%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS</td>
<td align="right">36,097,680</td>
<td align="right">2.2%</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE RETURN_VALUE</td>
<td align="right">34,178,400</td>
<td align="right">2.1%</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL RETURN_VALUE</td>
<td align="right">33,661,840</td>
<td align="right">2.0%</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK RETURN_VALUE</td>
<td align="right">33,388,200</td>
<td align="right">2.0%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE EXIT_INIT_CHECK</td>
<td align="right">33,388,200</td>
<td align="right">2.0%</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">27,452,940</td>
<td align="right">1.7%</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE BINARY_OP</td>
<td align="right">27,135,880</td>
<td align="right">1.6%</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT LOAD_FAST</td>
<td align="right">27,133,200</td>
<td align="right">1.6%</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT LOAD_FAST</td>
<td align="right">22,954,500</td>
<td align="right">1.4%</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">21,862,740</td>
<td align="right">1.3%</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT LOAD_FAST</td>
<td align="right">21,372,560</td>
<td align="right">1.3%</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT ENTER_EXECUTOR</td>
<td align="right">20,737,820</td>
<td align="right">1.3%</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">20,708,360</td>
<td align="right">1.3%</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">19,112,400</td>
<td align="right">1.2%</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST</td>
<td align="right">19,112,400</td>
<td align="right">1.2%</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">19,112,340</td>
<td align="right">1.2%</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE TO_BOOL_BOOL</td>
<td align="right">18,511,860</td>
<td align="right">1.1%</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE</td>
<td align="right">18,511,860</td>
<td align="right">1.1%</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT BINARY_OP_ADD_FLOAT</td>
<td align="right">18,448,260</td>
<td align="right">1.1%</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST RETURN_VALUE</td>
<td align="right">18,005,180</td>
<td align="right">1.1%</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_CONST_IMMORTAL</td>
<td align="right">17,871,900</td>
<td align="right">1.1%</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">17,871,900</td>
<td align="right">1.1%</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">17,352,620</td>
<td align="right">1.1%</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">16,780,320</td>
<td align="right">1.0%</td>
<td align="right">75.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">16,559,580</td>
<td align="right">1.0%</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_SMALL_INT</td>
<td align="right">15,709,240</td>
<td align="right">1.0%</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">15,227,400</td>
<td align="right">0.9%</td>
<td align="right">78.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE ENTER_EXECUTOR</td>
<td align="right">14,900,120</td>
<td align="right">0.9%</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE LOAD_FAST</td>
<td align="right">11,699,880</td>
<td align="right">0.7%</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT COMPARE_OP</td>
<td align="right">10,446,120</td>
<td align="right">0.6%</td>
<td align="right">80.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP POP_JUMP_IF_FALSE</td>
<td align="right">9,831,960</td>
<td align="right">0.6%</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">8,872,380</td>
<td align="right">0.5%</td>
<td align="right">81.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE LOAD_FAST_LOAD_FAST</td>
<td align="right">8,872,020</td>
<td align="right">0.5%</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">8,872,020</td>
<td align="right">0.5%</td>
<td align="right">82.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT STORE_FAST</td>
<td align="right">8,819,780</td>
<td align="right">0.5%</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">8,819,720</td>
<td align="right">0.5%</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP LOAD_FAST</td>
<td align="right">8,643,400</td>
<td align="right">0.5%</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_CONST_IMMORTAL</td>
<td align="right">8,513,640</td>
<td align="right">0.5%</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">7,724,440</td>
<td align="right">0.5%</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_CONST_IMMORTAL</td>
<td align="right">6,212,500</td>
<td align="right">0.4%</td>
<td align="right">85.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE CALL_PY_EXACT_ARGS</td>
<td align="right">6,120,860</td>
<td align="right">0.4%</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST POP_JUMP_IF_NOT_NONE</td>
<td align="right">5,983,540</td>
<td align="right">0.4%</td>
<td align="right">86.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">5,875,180</td>
<td align="right">0.4%</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE CALL_PY_EXACT_ARGS</td>
<td align="right">5,610,360</td>
<td align="right">0.3%</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BUILD_TUPLE</td>
<td align="right">5,489,580</td>
<td align="right">0.3%</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE LIST_APPEND</td>
<td align="right">5,489,460</td>
<td align="right">0.3%</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND ENTER_EXECUTOR</td>
<td align="right">5,489,460</td>
<td align="right">0.3%</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP STORE_FAST</td>
<td align="right">5,194,000</td>
<td align="right">0.3%</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE ENTER_EXECUTOR</td>
<td align="right">3,980,460</td>
<td align="right">0.2%</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_SMALL_INT</td>
<td align="right">3,920,040</td>
<td align="right">0.2%</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE BINARY_OP_ADD_FLOAT</td>
<td align="right">3,919,980</td>
<td align="right">0.2%</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_SMALL_INT</td>
<td align="right">3,711,840</td>
<td align="right">0.2%</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,600,000</td>
<td align="right">0.2%</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE BINARY_OP_MULTIPLY_INT</td>
<td align="right">3,519,840</td>
<td align="right">0.2%</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT LOAD_FAST</td>
<td align="right">3,254,740</td>
<td align="right">0.2%</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BINARY_OP</td>
<td align="right">2,899,940</td>
<td align="right">0.2%</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_SMALL_INT</td>
<td align="right">2,898,020</td>
<td align="right">0.2%</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT LOAD_FAST_LOAD_FAST</td>
<td align="right">2,879,820</td>
<td align="right">0.2%</td>
<td align="right">90.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP BINARY_OP_ADD_FLOAT</td>
<td align="right">2,873,340</td>
<td align="right">0.2%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT BINARY_OP</td>
<td align="right">2,847,420</td>
<td align="right">0.2%</td>
<td align="right">91.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,755,080</td>
<td align="right">0.2%</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST</td>
<td align="right">2,660,120</td>
<td align="right">0.2%</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,658,120</td>
<td align="right">0.2%</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS ENTER_EXECUTOR</td>
<td align="right">2,500,380</td>
<td align="right">0.2%</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">2,500,380</td>
<td align="right">0.2%</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_OP_ADD_INT</td>
<td align="right">2,361,660</td>
<td align="right">0.1%</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP RETURN_VALUE</td>
<td align="right">2,254,640</td>
<td align="right">0.1%</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_LIST</td>
<td align="right">2,195,820</td>
<td align="right">0.1%</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT LOAD_FAST</td>
<td align="right">2,096,280</td>
<td align="right">0.1%</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT RETURN_VALUE</td>
<td align="right">2,011,880</td>
<td align="right">0.1%</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_OP_MULTIPLY_INT</td>
<td align="right">1,894,840</td>
<td align="right">0.1%</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE GET_ITER</td>
<td align="right">1,875,840</td>
<td align="right">0.1%</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,870,340</td>
<td align="right">0.1%</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,860,480</td>
<td align="right">0.1%</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">1,855,900</td>
<td align="right">0.1%</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,855,840</td>
<td align="right">0.1%</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_SMALL_INT</td>
<td align="right">1,850,040</td>
<td align="right">0.1%</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,800,000</td>
<td align="right">0.1%</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS LOAD_FAST</td>
<td align="right">1,800,000</td>
<td align="right">0.1%</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,800,000</td>
<td align="right">0.1%</td>
<td align="right">93.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT LOAD_FAST</td>
<td align="right">1,612,860</td>
<td align="right">0.1%</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">1,612,800</td>
<td align="right">0.1%</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">1,530,120</td>
<td align="right">0.1%</td>
<td align="right">93.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL</td>
<td align="right">1,530,100</td>
<td align="right">0.1%</td>
<td align="right">94.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE BINARY_OP</td>
<td align="right">1,530,060</td>
<td align="right">0.1%</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST UNARY_NEGATIVE</td>
<td align="right">1,530,060</td>
<td align="right">0.1%</td>
<td align="right">94.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,515,980</td>
<td align="right">0.1%</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST</td>
<td align="right">1,511,880</td>
<td align="right">0.1%</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT STORE_SUBSCR</td>
<td align="right">1,445,760</td>
<td align="right">0.1%</td>
<td align="right">94.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST</td>
<td align="right">1,381,320</td>
<td align="right">0.1%</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_GLOBAL_MODULE</td>
<td align="right">1,380,520</td>
<td align="right">0.1%</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">1,379,920</td>
<td align="right">0.1%</td>
<td align="right">94.7%</td>
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
<td align="right">19,112,400</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_SMALL_INT</td>
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
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">20</td>
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
<td align="right">33,388,200</td>
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
<td align="right">33,388,200</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,875,840</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">915,900</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">319,980</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,180</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,195,820</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">915,900</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">6,180</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="right">19,112,340</td>
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
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">60</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">915,900</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">595,920</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
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
<td align="right">1,511,880</td>
<td align="right">100.0%</td>
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
<td align="right">17,352,620</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">711,560</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">600,000</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">25,800</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">16,780,320</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">640,080</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">600,000</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">391,260</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">271,680</td>
<td align="right">1.5%</td>
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
<td align="right">969,200</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">600,000</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
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
<td align="right">969,080</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">600,060</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">46,839,040</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">34,178,400</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">33,661,840</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">33,388,200</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,005,180</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">34,178,400</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">33,388,200</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,862,740</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">19,112,340</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">18,511,860</td>
<td align="right">10.6%</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,445,760</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">600,000</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,200,000</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">600,000</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">245,760</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">480</td>
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
<td align="right">1,530,100</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
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
<td align="right">1,530,120</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">1,530,060</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">139,560</td>
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
<td align="left">BINARY_OP</td>
<td align="right">1,530,060</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">139,560</td>
<td align="right">8.4%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">27,135,880</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,899,940</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">2,847,420</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">1,530,060</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,342,980</td>
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
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">16,559,580</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,643,400</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,194,000</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">2,873,340</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,254,640</td>
<td align="right">5.8%</td>
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
<td align="right">915,900</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">600,000</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">320,040</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
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
<td align="left">SWAP</td>
<td align="right">915,900</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">600,120</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">319,980</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="left">BUILD_TUPLE</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">5,489,580</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">953,900</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,040</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">5,489,460</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">959,940</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">60</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">160</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">80</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">80</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">300</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">220</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">140</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">80</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">40</td>
<td align="right">4.7%</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">600,060</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
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
<td align="left">POP_TOP</td>
<td align="right">600,000</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">120</td>
<td align="right">0.0%</td>
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
<td align="right">600,060</td>
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
<td align="right">600,060</td>
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
<td align="left">CALL_KW_NON_PY</td>
<td align="right">20</td>
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
<td align="right">10,446,120</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,560</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">9,831,960</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">614,160</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,560</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">60</td>
<td align="right">100.0%</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">60</td>
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
<td align="right">60</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">60</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">60</td>
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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">120</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">60</td>
<td align="right">33.3%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
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
<td align="left">STORE_FAST</td>
<td align="right">409,600</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">392,020</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">245,760</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">245,760</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">245,760</td>
<td align="right">15.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,292,860</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">252,060</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">60</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">100.0%</td>
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
<td align="right">5,489,460</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,489,460</td>
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
<td align="right">600,000</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">600,060</td>
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
<td align="right">600,480</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">231,760</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">600,000</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">231,420</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">240</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">784,220</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">694,260</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">596,400</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">320,040</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,080</td>
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
<td align="right">784,760</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">694,260</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">600,000</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">320,040</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,480</td>
<td align="right">0.1%</td>
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
<td align="right">60</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">60</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">60</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">60</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">124,416,500</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">63,418,440</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">36,233,020</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">27,133,200</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">22,954,500</td>
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
<td align="right">258,090,860</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">55,486,280</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">18,005,180</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">15,709,240</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">15,227,400</td>
<td align="right">3.8%</td>
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
<td align="right">915,900</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">915,900</td>
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
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">915,900</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">915,900</td>
<td align="right">50.0%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">8,872,020</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">2,879,820</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,660,120</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,381,320</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">915,940</td>
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
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">8,872,020</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,898,020</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,860,480</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,379,920</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,174,280</td>
<td align="right">5.7%</td>
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
<td align="right">140</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">120</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">120</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">60</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">500</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">80</td>
<td align="right">13.8%</td>
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
<td align="right">15,709,240</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,920,040</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,711,840</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,898,020</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,850,040</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">10,446,120</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">5,875,180</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,600,000</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,361,660</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,096,280</td>
<td align="right">6.9%</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">60</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">17,871,900</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">9,831,960</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,530,120</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">919,980</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">231,420</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,511,860</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,513,640</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,850,040</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">915,900</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">589,920</td>
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
<td align="right">288,340</td>
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
<td align="right">272,060</td>
<td align="right">94.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">16,280</td>
<td align="right">5.6%</td>
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
<td align="right">5,983,540</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,980,460</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,161,340</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">595,920</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">245,760</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60</td>
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
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">983,540</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">640,020</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">614,160</td>
<td align="right">27.4%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">682,680</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">593,200</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">543,960</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">392,020</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">25,800</td>
<td align="right">1.2%</td>
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
<td align="right">200</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">80</td>
<td align="right">28.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">280</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">21,862,740</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">8,819,780</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,194,000</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,016,580</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">600,000</td>
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
<td align="right">36,233,020</td>
<td align="right">90.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,240,200</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">784,100</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">606,040</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">417,020</td>
<td align="right">1.0%</td>
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
<td align="right">1,855,900</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">319,980</td>
<td align="right">14.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">939,960</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">915,940</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">319,980</td>
<td align="right">14.7%</td>
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
<td align="left">BUILD_LIST</td>
<td align="right">915,900</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">915,900</td>
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
<td align="left">GET_ITER</td>
<td align="right">915,900</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">915,900</td>
<td align="right">50.0%</td>
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
<td align="right">18,448,260</td>
<td align="right">68.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,919,980</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,873,340</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">694,260</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">524,420</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">21,372,560</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,011,880</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,200,000</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">953,900</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">694,260</td>
<td align="right">2.6%</td>
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
<td align="right">2,361,660</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">600,000</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">462,840</td>
<td align="right">13.5%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,445,760</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">915,900</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">831,420</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">231,420</td>
<td align="right">6.8%</td>
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
<td align="right">41,019,740</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,872,020</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">365,160</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">49,420</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">32,400</td>
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
<td align="right">22,954,500</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">18,448,260</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">8,872,380</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">39,580</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">24,440</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,519,840</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,894,840</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">69,820</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">25,940</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">24,440</td>
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
<td align="right">3,254,740</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,049,080</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">600,000</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">334,220</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">245,820</td>
<td align="right">4.4%</td>
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
<td align="right">27,452,940</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">8,872,380</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">8,819,720</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">606,040</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">416,040</td>
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
<td align="right">27,133,200</td>
<td align="right">58.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,819,780</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">8,819,720</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">606,000</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">416,040</td>
<td align="right">0.9%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,755,080</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,515,980</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">600,000</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,100</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,658,120</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,612,860</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">600,000</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,240</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">480</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">5,875,180</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,879,820</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,847,420</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">97,360</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">32,400</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">18,200</td>
<td align="right">0.3%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">16,559,580</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,658,120</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">1,200,000</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">320,100</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">319,980</td>
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
<td align="right">20,737,820</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">321,300</td>
<td align="right">1.5%</td>
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
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">1,049,080</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">750,960</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">694,260</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,040</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,800,000</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">462,840</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">231,420</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,180</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,800,000</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,800,000</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">319,980</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,800,000</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,800,000</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">319,980</td>
<td align="right">8.2%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">703,020</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">694,260</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">416,080</td>
<td align="right">22.9%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">703,020</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">694,260</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">416,040</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
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
<td align="right">400</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">400</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
<td align="right">4.8%</td>
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
<td align="right">614,280</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">480</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">368,400</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">245,760</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">600</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">1,480</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">40</td>
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
<td align="right">1,560</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">20</td>
<td align="right">33.3%</td>
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
<td align="left">POP_TOP</td>
<td align="right">60</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">160</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">140</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">40</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">40</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">40</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">120</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">60</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">60</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">14.3%</td>
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
<td align="right">36,097,680</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,227,400</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,120,860</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,610,360</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">934,440</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">62,954,360</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,500,380</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">34,320</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">60</td>
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
<td align="left">MAKE_CELL</td>
<td align="right">60</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">825,780</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">139,560</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">18,200</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">983,540</td>
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
<td align="right">919,980</td>
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
<td align="right">919,980</td>
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
<td align="right">2,195,820</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,292,860</td>
<td align="right">37.1%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">1,855,840</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,016,580</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">264,620</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">191,460</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">160,180</td>
<td align="right">4.6%</td>
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
<td align="right">252,060</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,180</td>
<td align="right">2.4%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">258,180</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">60</td>
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
<td align="right">258,090,860</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,860,480</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">10,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">124,416,500</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">41,019,740</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">27,452,940</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,135,880</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">14,900,120</td>
<td align="right">5.7%</td>
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
<td align="right">615,680</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">680</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">614,280</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,560</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">540</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
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
<td align="right">55,486,280</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,870,340</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,174,280</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">974,300</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">614,240</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">36,097,680</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,708,360</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,381,320</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,380,520</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">784,220</td>
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
<td align="right">969,120</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">969,200</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">17,871,900</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,513,640</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,212,500</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">600,000</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">271,680</td>
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
<td align="right">33,661,840</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">120</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,600,000</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,200,000</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">694,260</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">606,040</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">391,260</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,920,040</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,500,380</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">694,260</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">18,511,860</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,612,800</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,380,520</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,240,200</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">640,080</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">19,112,400</td>
<td align="right">79.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,660,120</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">969,120</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">825,780</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">231,760</td>
<td align="right">1.0%</td>
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
<td align="right">62,954,360</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">19,112,400</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">321,300</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">185,120</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">63,418,440</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">17,871,900</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">553,160</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">409,720</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">320,040</td>
<td align="right">0.4%</td>
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
<td align="right">7,724,440</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">964,000</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">6,212,500</td>
<td align="right">71.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">917,040</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">642,440</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">596,400</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">319,980</td>
<td align="right">3.7%</td>
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
<td align="right">18,511,860</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="right">17,871,900</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">640,020</td>
<td align="right">3.5%</td>
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
<td align="right">231,420</td>
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
<td align="right">231,420</td>
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
<td align="left">LOAD_FAST</td>
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
<td align="right">319,980</td>
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
<td align="right">319,980</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,855,840</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
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
<td align="right">1,855,900</td>
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
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">20,737,820</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">14,900,120</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">5,489,460</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,980,460</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,500,380</td>
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
<td align="right">46,839,040</td>
<td align="right">93.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">974,300</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">711,560</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">412,060</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">397,280</td>
<td align="right">0.8%</td>
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
<td align="right">38,473,860</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">225,283,580</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,769,020</td>
<td align="right">7.9%</td>
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
<td align="right">429,740</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">659,120</td>
<td align="right">60.5%</td>
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
<td align="right">582,760</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">40,380</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">33,080</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">1,860</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">520</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,105,260</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">165,867,360</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,817,820</td>
<td align="right">1.1%</td>
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
<td align="right">35,200</td>
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
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
</tr>
</tbody>
</table>


</details>

### CALL_KW

<details>
<summary> specialization stats for CALL_KW family </summary>


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
<td align="right">10,446,120</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,884,440</td>
<td align="right">21.6%</td>
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
<td align="right">2,560</td>
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
<td align="left">float long</td>
<td align="right">2,560</td>
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
<td align="right">60</td>
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
<td align="right">3,747,040</td>
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
<td align="right">831,660</td>
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
<td align="right">509,012,940</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,849,220</td>
<td align="right">0.4%</td>
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
<td align="right">35,640</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">280</td>
<td align="right">0.8%</td>
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
<td align="right">140</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">120</td>
<td align="right">42.9%</td>
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
<td align="right">31,054,900</td>
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
<td align="right">580</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">96,107,640</td>
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
<td align="right">240</td>
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
<td align="right">280</td>
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
<td align="right">2,045,760</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">480</td>
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
<td align="right">480</td>
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
<td align="right">1,530,120</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,743,400</td>
<td align="right">92.5%</td>
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
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">380</td>
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
<td align="left">float</td>
<td align="right">360</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">5.3%</td>
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
<td align="right">12,617,520</td>
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
<td align="right">854,441,280</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">53,993,100</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">717,056,980</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">26,437,140</td>
<td align="right">1.6%</td>
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
<td align="right">38,473,860</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">10,446,120</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,045,760</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,530,120</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">831,660</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">0</td>
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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">15,083,100</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,666,880</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">2,642,820</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">2,026,420</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,817,820</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,276,700</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">572,520</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">349,800</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">840</td>
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
<td align="right">19,112,400</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">152,910,540</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">19,112,400</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">19,112,400</td>
<td align="right">11.1%</td>
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
<td align="right">19,112,400</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,511,860</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">120</td>
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
<td align="right">205,411,140</td>
<td align="right">119.4%</td>
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
<td align="right">227,038,740</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">227,038,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">47,851,420</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">47,850,580</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">49,082,076</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">33,388,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,010,788,820</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,221,836,840</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">954,067,180</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,016,707,277</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">84,516,400</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">185,514,560</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">63,069,594</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">143,095,097</td>
<td align="right">5.6%</td>
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
<td align="right">3,677,101</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">119</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">183</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">18,512,512</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">108</td>
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
<td align="right">12,320</td>
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
<td align="right">940</td>
<td align="right">7.6%</td>
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
<td align="right">11,500</td>
<td align="right">93.3%</td>
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
<td align="right">11,380</td>
<td align="right">92.4%</td>
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
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">98,714,380</td>
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
<td align="right">2,690,210,160</td>
<td align="right">2,725.2%</td>
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
<td align="right">940</td>
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
<td align="right">840</td>
<td align="right">89.4%</td>
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
<td align="right">80</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">40</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">280</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">300</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">140</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">80</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">2.1%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">120</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">60</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">480</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">19.1%</td>
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
<td align="left">_LOAD_FAST_0</td>
<td align="right">205,362,380</td>
<td align="right">7.6%</td>
<td align="right">7.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">138,234,300</td>
<td align="right">5.1%</td>
<td align="right">12.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">132,406,960</td>
<td align="right">4.9%</td>
<td align="right">17.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">132,406,960</td>
<td align="right">4.9%</td>
<td align="right">22.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">127,691,960</td>
<td align="right">4.7%</td>
<td align="right">27.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">115,848,080</td>
<td align="right">4.3%</td>
<td align="right">31.7%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">106,163,680</td>
<td align="right">3.9%</td>
<td align="right">35.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">98,714,380</td>
<td align="right">3.7%</td>
<td align="right">39.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">87,419,160</td>
<td align="right">3.2%</td>
<td align="right">42.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">87,419,160</td>
<td align="right">3.2%</td>
<td align="right">45.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">83,498,600</td>
<td align="right">3.1%</td>
<td align="right">48.9%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">79,715,920</td>
<td align="right">3.0%</td>
<td align="right">51.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">70,007,920</td>
<td align="right">2.6%</td>
<td align="right">54.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">67,137,080</td>
<td align="right">2.5%</td>
<td align="right">56.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">66,396,440</td>
<td align="right">2.5%</td>
<td align="right">59.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">60,559,660</td>
<td align="right">2.3%</td>
<td align="right">61.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">56,210,700</td>
<td align="right">2.1%</td>
<td align="right">63.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">56,210,700</td>
<td align="right">2.1%</td>
<td align="right">65.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">56,210,700</td>
<td align="right">2.1%</td>
<td align="right">67.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">54,067,360</td>
<td align="right">2.0%</td>
<td align="right">69.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">53,533,080</td>
<td align="right">2.0%</td>
<td align="right">71.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">53,151,460</td>
<td align="right">2.0%</td>
<td align="right">73.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">47,398,480</td>
<td align="right">1.8%</td>
<td align="right">75.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">46,329,120</td>
<td align="right">1.7%</td>
<td align="right">77.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">42,051,480</td>
<td align="right">1.6%</td>
<td align="right">79.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">39,154,680</td>
<td align="right">1.5%</td>
<td align="right">80.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">38,398,800</td>
<td align="right">1.4%</td>
<td align="right">81.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">31,521,460</td>
<td align="right">1.2%</td>
<td align="right">83.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">30,106,940</td>
<td align="right">1.1%</td>
<td align="right">84.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">27,689,320</td>
<td align="right">1.0%</td>
<td align="right">85.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">26,404,640</td>
<td align="right">1.0%</td>
<td align="right">86.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">26,193,360</td>
<td align="right">1.0%</td>
<td align="right">87.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">21,021,760</td>
<td align="right">0.8%</td>
<td align="right">87.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">20,511,860</td>
<td align="right">0.8%</td>
<td align="right">88.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">20,476,040</td>
<td align="right">0.8%</td>
<td align="right">89.4%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">20,476,040</td>
<td align="right">0.8%</td>
<td align="right">90.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">20,434,040</td>
<td align="right">0.8%</td>
<td align="right">90.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">18,997,960</td>
<td align="right">0.7%</td>
<td align="right">91.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">18,006,380</td>
<td align="right">0.7%</td>
<td align="right">92.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">17,328,640</td>
<td align="right">0.6%</td>
<td align="right">93.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">15,876,460</td>
<td align="right">0.6%</td>
<td align="right">93.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">13,490,680</td>
<td align="right">0.5%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">13,133,020</td>
<td align="right">0.5%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">13,061,600</td>
<td align="right">0.5%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">12,329,080</td>
<td align="right">0.5%</td>
<td align="right">95.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">12,329,080</td>
<td align="right">0.5%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">10,441,640</td>
<td align="right">0.4%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">9,554,960</td>
<td align="right">0.4%</td>
<td align="right">96.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">7,449,300</td>
<td align="right">0.3%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">7,272,260</td>
<td align="right">0.3%</td>
<td align="right">97.2%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">7,230,060</td>
<td align="right">0.3%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">7,230,060</td>
<td align="right">0.3%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">6,841,680</td>
<td align="right">0.3%</td>
<td align="right">98.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">6,668,880</td>
<td align="right">0.2%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,040,420</td>
<td align="right">0.2%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">5,890,200</td>
<td align="right">0.2%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">4,384,800</td>
<td align="right">0.2%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">3,599,960</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,811,300</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,895,400</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">1,895,400</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,895,400</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,837,740</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,837,740</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">1,338,160</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">980,920</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">980,920</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">980,760</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">956,340</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">954,300</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">954,300</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">948,240</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">915,900</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">915,900</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">763,240</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">744,160</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">594,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">354,240</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">354,240</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">354,240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">354,240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">354,240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">354,240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">184,680</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">7,640</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">500</td>
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
Stats gathered on: 2024-12-13