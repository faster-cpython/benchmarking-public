
# Pystats results

- benchmark: logging
- fork: brandtbucher
- ref: underflow-jump-backward-0
- commit hash: e448061
- commit date: 2024-08-29T16:38:24-07:00

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
<td align="left">POP_TOP</td>
<td align="right">9,876,900</td>
<td align="right">21.9%</td>
<td align="right">21.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">7,453,763</td>
<td align="right">16.5%</td>
<td align="right">38.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,667,491</td>
<td align="right">14.8%</td>
<td align="right">53.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,093,340</td>
<td align="right">9.1%</td>
<td align="right">62.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">3,709,240</td>
<td align="right">8.2%</td>
<td align="right">70.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,411,836</td>
<td align="right">7.6%</td>
<td align="right">78.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,474,671</td>
<td align="right">5.5%</td>
<td align="right">83.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,259,700</td>
<td align="right">2.8%</td>
<td align="right">86.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,252,540</td>
<td align="right">2.8%</td>
<td align="right">89.2%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,229,280</td>
<td align="right">2.7%</td>
<td align="right">91.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,152,040</td>
<td align="right">2.6%</td>
<td align="right">94.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,118,540</td>
<td align="right">2.5%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">427,300</td>
<td align="right">0.9%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">87,242</td>
<td align="right">0.2%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">85,180</td>
<td align="right">0.2%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">82,924</td>
<td align="right">0.2%</td>
<td align="right">98.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">66,702</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">57,311</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">52,531</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">49,327</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">42,922</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">29,040</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">26,407</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">23,220</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21,645</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">21,120</td>
<td align="right">0.0%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">20,142</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">19,468</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">16,780</td>
<td align="right">0.0%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">15,160</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">15,040</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">13,320</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">12,340</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">12,280</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,060</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">11,520</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">11,120</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">10,800</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,560</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">9,291</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,960</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,920</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">6,880</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,868</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,640</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">6,240</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5,720</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">5,640</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">4,580</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,480</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">4,400</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4,288</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">4,100</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,800</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,720</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">3,520</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">3,160</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,880</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,430</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,761</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,740</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,487</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,460</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">720</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">600</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">600</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">600</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">600</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">60</td>
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
<td align="left">LOAD_CONST LOAD_CONST</td>
<td align="right">4,915,320</td>
<td align="right">10.9%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CACHE ENTER_EXECUTOR</td>
<td align="right">4,090,080</td>
<td align="right">9.1%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR INTERPRETER_EXIT</td>
<td align="right">4,081,280</td>
<td align="right">9.1%</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">POP_TOP RETURN_CONST</td>
<td align="right">3,700,720</td>
<td align="right">8.2%</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST POP_TOP</td>
<td align="right">3,695,920</td>
<td align="right">8.2%</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL POP_TOP</td>
<td align="right">2,463,700</td>
<td align="right">5.5%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_CONST</td>
<td align="right">2,461,120</td>
<td align="right">5.5%</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST CALL_NON_PY_GENERAL</td>
<td align="right">2,457,440</td>
<td align="right">5.5%</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">2,361,440</td>
<td align="right">5.2%</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">POP_TOP ENTER_EXECUTOR</td>
<td align="right">1,351,080</td>
<td align="right">3.0%</td>
<td align="right">70.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST RETURN_VALUE</td>
<td align="right">1,239,920</td>
<td align="right">2.8%</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE POP_TOP</td>
<td align="right">1,228,800</td>
<td align="right">2.7%</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX POP_TOP</td>
<td align="right">1,228,800</td>
<td align="right">2.7%</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS POP_TOP</td>
<td align="right">1,228,760</td>
<td align="right">2.7%</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR CALL_FUNCTION_EX</td>
<td align="right">1,228,120</td>
<td align="right">2.7%</td>
<td align="right">83.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,228,120</td>
<td align="right">2.7%</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,149,580</td>
<td align="right">2.6%</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL ENTER_EXECUTOR</td>
<td align="right">1,118,120</td>
<td align="right">2.5%</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">779,300</td>
<td align="right">1.7%</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_GENERAL</td>
<td align="right">749,300</td>
<td align="right">1.7%</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST</td>
<td align="right">369,440</td>
<td align="right">0.8%</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_PY_GENERAL</td>
<td align="right">368,640</td>
<td align="right">0.8%</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR ENTER_EXECUTOR</td>
<td align="right">59,860</td>
<td align="right">0.1%</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">55,620</td>
<td align="right">0.1%</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">48,130</td>
<td align="right">0.1%</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">47,551</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">45,163</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">41,582</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS ENTER_EXECUTOR</td>
<td align="right">33,811</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">33,102</td>
<td align="right">0.1%</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">32,120</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR POP_TOP</td>
<td align="right">28,340</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">24,240</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST</td>
<td align="right">23,931</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">23,600</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD RESUME_CHECK</td>
<td align="right">23,040</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE</td>
<td align="right">21,182</td>
<td align="right">0.0%</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST</td>
<td align="right">20,840</td>
<td align="right">0.0%</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">20,791</td>
<td align="right">0.0%</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST</td>
<td align="right">20,587</td>
<td align="right">0.0%</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST BINARY_OP</td>
<td align="right">19,102</td>
<td align="right">0.0%</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS JUMP_BACKWARD</td>
<td align="right">18,720</td>
<td align="right">0.0%</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">18,562</td>
<td align="right">0.0%</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">16,640</td>
<td align="right">0.0%</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR</td>
<td align="right">15,768</td>
<td align="right">0.0%</td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST STORE_FAST</td>
<td align="right">15,420</td>
<td align="right">0.0%</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE POP_JUMP_IF_FALSE</td>
<td align="right">15,120</td>
<td align="right">0.0%</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR LOAD_FAST</td>
<td align="right">15,080</td>
<td align="right">0.0%</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST LOAD_FAST</td>
<td align="right">14,241</td>
<td align="right">0.0%</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE TO_BOOL_BOOL</td>
<td align="right">13,571</td>
<td align="right">0.0%</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">13,440</td>
<td align="right">0.0%</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_ALWAYS_TRUE</td>
<td align="right">13,280</td>
<td align="right">0.0%</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE CALL_ISINSTANCE</td>
<td align="right">13,280</td>
<td align="right">0.0%</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE LOAD_FAST</td>
<td align="right">11,960</td>
<td align="right">0.0%</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST INTERPRETER_EXIT</td>
<td align="right">11,440</td>
<td align="right">0.0%</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE STORE_FAST</td>
<td align="right">11,280</td>
<td align="right">0.0%</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE</td>
<td align="right">11,091</td>
<td align="right">0.0%</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP LOAD_FAST</td>
<td align="right">10,931</td>
<td align="right">0.0%</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST TO_BOOL_NONE</td>
<td align="right">10,480</td>
<td align="right">0.0%</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR STORE_FAST</td>
<td align="right">10,160</td>
<td align="right">0.0%</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">9,960</td>
<td align="right">0.0%</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">9,760</td>
<td align="right">0.0%</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL CALL_NON_PY_GENERAL</td>
<td align="right">9,691</td>
<td align="right">0.0%</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST STORE_FAST</td>
<td align="right">8,960</td>
<td align="right">0.0%</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE LOAD_ATTR_MODULE</td>
<td align="right">8,960</td>
<td align="right">0.0%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE RETURN_CONST</td>
<td align="right">8,520</td>
<td align="right">0.0%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE LOAD_FAST</td>
<td align="right">8,160</td>
<td align="right">0.0%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST STORE_FAST</td>
<td align="right">7,960</td>
<td align="right">0.0%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE</td>
<td align="right">7,960</td>
<td align="right">0.0%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,920</td>
<td align="right">0.0%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_MODULE</td>
<td align="right">7,840</td>
<td align="right">0.0%</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL LOAD_FAST</td>
<td align="right">7,751</td>
<td align="right">0.0%</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">7,360</td>
<td align="right">0.0%</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE</td>
<td align="right">7,080</td>
<td align="right">0.0%</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">7,040</td>
<td align="right">0.0%</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST ENTER_EXECUTOR</td>
<td align="right">6,680</td>
<td align="right">0.0%</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE COPY</td>
<td align="right">6,600</td>
<td align="right">0.0%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST COMPARE_OP_INT</td>
<td align="right">6,480</td>
<td align="right">0.0%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP LOAD_CONST</td>
<td align="right">6,440</td>
<td align="right">0.0%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">COPY TO_BOOL_BOOL</td>
<td align="right">6,320</td>
<td align="right">0.0%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_CONST</td>
<td align="right">6,320</td>
<td align="right">0.0%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE GET_ITER</td>
<td align="right">6,320</td>
<td align="right">0.0%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT LOAD_FAST</td>
<td align="right">6,320</td>
<td align="right">0.0%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_LIST</td>
<td align="right">6,280</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_SLOT</td>
<td align="right">6,240</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS</td>
<td align="right">6,240</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">6,200</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,160</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_CONST</td>
<td align="right">6,160</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE JUMP_FORWARD</td>
<td align="right">6,160</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">COPY LOAD_SPECIAL</td>
<td align="right">6,140</td>
<td align="right">0.0%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL SWAP</td>
<td align="right">6,140</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">SWAP LOAD_SPECIAL</td>
<td align="right">6,140</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">SWAP SWAP</td>
<td align="right">6,140</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST BINARY_OP_ADD_INT</td>
<td align="right">6,080</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,080</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL CALL_NON_PY_GENERAL</td>
<td align="right">5,920</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD LOAD_FAST</td>
<td align="right">5,760</td>
<td align="right">0.0%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">5,760</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST JUMP_FORWARD</td>
<td align="right">5,760</td>
<td align="right">0.0%</td>
<td align="right">99.1%</td>
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
<td align="right">2,520</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">640</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">600</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">40</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">1,880</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">640</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">640</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">640</td>
<td align="right">16.8%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,090,080</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,260</td>
<td align="right">0.1%</td>
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
<td align="right">120</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">120</td>
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
<td align="left">PUSH_EXC_INFO</td>
<td align="right">60</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">60</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">60</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20</td>
<td align="right">8.3%</td>
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
<td align="left">LOAD_GLOBAL</td>
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
<td align="right">6,320</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">240</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">80</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,280</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">180</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">180</td>
<td align="right">2.7%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,081,280</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">11,440</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">3,160</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,760</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,600</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">240</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">80</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,680</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,880</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">240</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
<td align="right">1.2%</td>
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
<td align="left">SWAP</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
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
<td align="left">RETURN_CONST</td>
<td align="right">3,695,920</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,463,700</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,228,800</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,228,800</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,228,760</td>
<td align="right">12.4%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">3,700,720</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,461,120</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,361,440</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,351,080</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,700</td>
<td align="right">0.0%</td>
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
<td align="left">BINARY_SUBSCR</td>
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
<td align="left">LOAD_GLOBAL</td>
<td align="right">60</td>
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
<td align="right">18,562</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,100</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">480</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">9,691</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,451</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,400</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">680</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">640</td>
<td align="right">3.2%</td>
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
<td align="right">1,239,920</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,840</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,520</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,440</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,000</td>
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
<td align="right">1,228,800</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">11,280</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,600</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,760</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,440</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">60</td>
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
<td align="right">2,540</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">980</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">480</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">280</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">280</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,820</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">820</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">360</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">280</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">200</td>
<td align="right">3.5%</td>
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
<td align="right">19,102</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,303</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">760</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">300</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">10,931</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,440</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,371</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,303</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">640</td>
<td align="right">3.0%</td>
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
<td align="right">240</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">240</td>
<td align="right">100.0%</td>
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
<td align="right">640</td>
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
<td align="right">640</td>
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
<td align="right">3,200</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">640</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">640</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">3,840</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">640</td>
<td align="right">14.3%</td>
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
<td align="right">2,880</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">740</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">680</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">624</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">600</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,780</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,160</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">600</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">540</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">520</td>
<td align="right">7.6%</td>
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
<td align="right">1,228,120</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">640</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
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
<td align="left">POP_TOP</td>
<td align="right">1,228,800</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">480</td>
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
<td align="right">240</td>
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
<td align="right">240</td>
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
<td align="left">BINARY_OP</td>
<td align="right">1,371</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">400</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">160</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">140</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">99</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,711</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">320</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">100</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">99</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">80</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">3,520</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">200</td>
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
<td align="left">COPY</td>
<td align="right">3,520</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">200</td>
<td align="right">5.4%</td>
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
<td align="right">6,600</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,520</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,920</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">120</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">100</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,320</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">6,140</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">640</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">160</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">60</td>
<td align="right">0.5%</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">240</td>
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
<td align="right">180</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">60</td>
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
<td align="right">640</td>
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
<td align="right">640</td>
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
<td align="left">GET_ITER</td>
<td align="right">180</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">100</td>
<td align="right">35.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">100</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">80</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">60</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">14.3%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">18,720</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">3,260</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,780</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,700</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,360</td>
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
<td align="right">23,040</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,120</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,340</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">900</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">600</td>
<td align="right">2.1%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,160</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,760</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">80</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">5,760</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,120</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,040</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">60</td>
<td align="right">0.5%</td>
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
<td align="right">240</td>
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
<td align="right">240</td>
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
<td align="right">15,768</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,440</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">760</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">720</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">220</td>
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
<td align="right">5,160</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,740</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,440</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,340</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,284</td>
<td align="right">6.6%</td>
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
<td align="right">4,915,320</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,461,120</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">23,931</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,440</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">6,320</td>
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
<td align="right">4,915,320</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,457,440</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">19,102</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">14,241</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,960</td>
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
<td align="left">NOP</td>
<td align="right">240</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">240</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">180</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">60</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">480</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">240</td>
<td align="right">33.3%</td>
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
<td align="left">POP_TOP</td>
<td align="right">2,361,440</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">779,300</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">55,620</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">48,130</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">20,587</td>
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
<td align="right">1,239,920</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,149,580</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">749,300</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">45,163</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">41,582</td>
<td align="right">1.2%</td>
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
<td align="left">JUMP_FORWARD</td>
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
<td align="left">SWAP</td>
<td align="right">60</td>
<td align="right">100.0%</td>
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
<td align="right">369,440</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,840</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,440</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,760</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,720</td>
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
<td align="left">CALL_PY_GENERAL</td>
<td align="right">368,640</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">24,240</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,440</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,040</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,240</td>
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
<td align="left">STORE_FAST</td>
<td align="right">840</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">560</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">440</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">400</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">400</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,660</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">720</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">524</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">464</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">220</td>
<td align="right">5.1%</td>
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
<td align="right">6,140</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,140</td>
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
<td align="right">6,140</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,920</td>
<td align="right">48.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">220</td>
<td align="right">1.8%</td>
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
<td align="right">47,551</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">15,120</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">7,360</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">7,080</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,820</td>
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
<td align="right">48,130</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">11,091</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">8,520</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,620</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,880</td>
<td align="right">4.4%</td>
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
<td align="right">4,400</td>
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
<td align="right">3,040</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,280</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
<td align="right">1.8%</td>
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
<td align="right">1,920</td>
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
<td align="right">1,920</td>
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
<td align="right">9,760</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">7,960</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,160</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">200</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,920</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,320</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,840</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,000</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">960</td>
<td align="right">4.5%</td>
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
<td align="right">3,700,720</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,520</td>
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
<td align="right">3,695,920</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,440</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,880</td>
<td align="right">0.1%</td>
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
<td align="right">1,041</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">720</td>
<td align="right">40.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">880</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">280</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">240</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">201</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">80</td>
<td align="right">4.5%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">15,420</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">11,280</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">10,160</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,960</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,960</td>
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
<td align="right">55,620</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,680</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,160</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,080</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,480</td>
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
<td align="left">COPY</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">60</td>
<td align="right">100.0%</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,760</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5,720</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
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
<td align="left">JUMP_FORWARD</td>
<td align="right">5,760</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,760</td>
<td align="right">50.0%</td>
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
<td align="left">LOAD_SPECIAL</td>
<td align="right">6,140</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,140</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
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
<td align="left">LOAD_SPECIAL</td>
<td align="right">6,140</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,140</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">60</td>
<td align="right">0.5%</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">40</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">40</td>
<td align="right">50.0%</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,340</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">60</td>
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
<td align="right">820</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">400</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">80</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">60</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">40</td>
<td align="right">2.9%</td>
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
<td align="right">6,080</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">160</td>
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
<td align="right">5,640</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">600</td>
<td align="right">9.6%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">560</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">40</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">560</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">6.7%</td>
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
<td align="right">80</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">80</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">40</td>
<td align="right">33.3%</td>
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
<td align="right">120</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
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
<td align="left">STORE_FAST</td>
<td align="right">180</td>
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
<td align="right">4,760</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,451</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">80</td>
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
<td align="right">4,800</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,491</td>
<td align="right">48.3%</td>
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
<td align="right">840</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">560</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">60</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">1,460</td>
<td align="right">100.0%</td>
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
<td align="right">4,040</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">3,160</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">920</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,283</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">120</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">84</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">1,307</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">180</td>
<td align="right">12.1%</td>
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
<td align="right">4,160</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">280</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">140</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,600</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">900</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">80</td>
<td align="right">1.7%</td>
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
<td align="right">2,800</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">80</td>
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
<td align="right">2,480</td>
<td align="right">86.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">400</td>
<td align="right">13.9%</td>
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
<td align="right">13,280</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,440</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">920</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">140</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">16,640</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">140</td>
<td align="right">0.8%</td>
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
<td align="right">1,000</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">80</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">1,000</td>
<td align="right">89.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">120</td>
<td align="right">10.7%</td>
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
<td align="right">6,200</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,520</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">560</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">400</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">120</td>
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
<td align="right">7,960</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,480</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">360</td>
<td align="right">3.3%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">80</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="right">120</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,228,120</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">23,600</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">680</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
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
<td align="left">POP_TOP</td>
<td align="right">1,228,760</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">23,600</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">40</td>
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
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">560</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
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
<td align="left">POP_TOP</td>
<td align="right">600</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">2,457,440</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">9,691</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">5,920</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">2,463,700</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">7,751</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,660</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">560</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">32,120</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,240</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,451</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,360</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,240</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">33,811</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">18,720</td>
<td align="right">35.6%</td>
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
<td align="right">749,300</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">368,640</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">600</td>
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
<td align="right">1,118,120</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">420</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">560</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
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
<td align="right">600</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">3,120</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,160</td>
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
<td align="right">6,480</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,120</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,120</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">320</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">80</td>
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
<td align="right">7,360</td>
<td align="right">66.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,160</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">600</td>
<td align="right">5.4%</td>
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
<td align="right">2,880</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">560</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">80</td>
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
<td align="left">COPY</td>
<td align="right">2,920</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">600</td>
<td align="right">17.0%</td>
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
<td align="right">6,280</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">600</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="right">3,800</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,160</td>
<td align="right">45.4%</td>
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
<td align="right">900</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">180</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">60</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,140</td>
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
<td align="right">45,163</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,520</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,284</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">280</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">40</td>
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
<td align="left">COPY</td>
<td align="right">6,600</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,320</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">5,720</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,080</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,660</td>
<td align="right">9.4%</td>
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
<td align="right">920</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">560</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">260</td>
<td align="right">14.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">680</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">600</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">180</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">160</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">120</td>
<td align="right">6.9%</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">6,080</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,960</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">560</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">560</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">320</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">6,160</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,280</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">80</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">0.4%</td>
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
<td align="right">1,149,580</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,340</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,120</td>
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
<td align="right">779,300</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">369,440</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,240</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">160</td>
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
<td align="right">33,102</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">8,960</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">860</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">18,562</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">8,960</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,160</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,080</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">920</td>
<td align="right">2.1%</td>
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
<td align="right">560</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">560</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">80</td>
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
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">560</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">560</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">40</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">3.3%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,520</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">480</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">40</td>
<td align="right">1.3%</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,440</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">640</td>
<td align="right">20.8%</td>
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
<td align="right">6,240</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">680</td>
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
<td align="right">6,320</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">560</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">0.6%</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,920</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">6,160</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,620</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,440</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,440</td>
<td align="right">9.2%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">20,587</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,040</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,440</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">180</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">80</td>
<td align="right">0.3%</td>
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
<td align="right">21,182</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,791</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,091</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,840</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,320</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">33,102</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">13,571</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">13,280</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,180</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,451</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">23,040</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">180</td>
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
<td align="right">9,960</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,840</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,440</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,760</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">600</td>
<td align="right">2.6%</td>
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
<td align="right">41,582</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">24,240</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">880</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">21,182</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,840</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,960</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,160</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">3,160</td>
<td align="right">4.7%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">13,280</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,040</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">560</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">120</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,960</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">7,080</td>
<td align="right">47.1%</td>
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
<td align="right">16,640</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,571</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,320</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,600</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,080</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">47,551</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,760</td>
<td align="right">17.0%</td>
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
<td align="right">10,480</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,240</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,480</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">560</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">360</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">15,120</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">40</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">560</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">40</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">600</td>
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
<td align="right">3,120</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,560</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,720</td>
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
<td align="left">CACHE</td>
<td align="right">4,090,080</td>
<td align="right">61.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,351,080</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,118,120</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">59,860</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">33,811</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">4,081,280</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,228,120</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,228,120</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">59,860</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">28,340</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">180</td>
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
<td align="right">19,962</td>
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
<td align="right">8,601,660</td>
<td align="right">99.7%</td>
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
<td align="right">380</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,303</td>
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
<td align="left">true divide different types</td>
<td align="right">424</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">380</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">299</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">200</td>
<td align="right">15.3%</td>
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
<td align="right">120</td>
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
<td align="right">56,524,680</td>
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
<td align="right">120</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,464</td>
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
<td align="right">117,556,167</td>
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
<td align="right">1,252,360</td>
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
<td align="right">27,004</td>
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
<td align="right">40</td>
<td align="right">40 / 0 !!</td>
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
<td align="right">1,891</td>
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
<td align="right">17,612,600</td>
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
<td align="right">440</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">99</td>
<td align="right">18.4%</td>
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
<td align="left">big int</td>
<td align="right">99</td>
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
<td align="right">3,520</td>
<td align="right">94.6%</td>
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
<td align="right">200</td>
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
<td align="left">str</td>
<td align="right">200</td>
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
<td align="right">140</td>
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
<td align="right">8,100</td>
<td align="right">96.7%</td>
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
<td align="right">14,244</td>
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
<td align="right">291,268,369</td>
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
<td align="right">2,120</td>
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
<td align="right">4,344</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">920</td>
<td align="right">17.5%</td>
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
<td align="right">800</td>
<td align="right">87.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">120</td>
<td align="right">13.0%</td>
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
<td align="right">2,164</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">106,811</td>
<td align="right">94.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,520</td>
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
<td align="right">2,204</td>
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
<td align="right">881</td>
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
<td align="right">27,032,720</td>
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
<td align="right">880</td>
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
<td align="right">60</td>
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
<td align="right">4,020</td>
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
<td align="right">129,871,151</td>
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
<td align="right">2,120</td>
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
<td align="right">1,380</td>
<td align="right">83.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">280</td>
<td align="right">16.9%</td>
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
<td align="right">280</td>
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
<td align="right">40</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,720</td>
<td align="right">98.6%</td>
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
<td align="right">38,347,572</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">184,962</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">5,286,893</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,259,120</td>
<td align="right">2.8%</td>
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
<td align="right">19,962</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">14,244</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,020</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,520</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,464</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,164</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,891</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">881</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">140</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">120</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,252,360</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,340</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,120</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,120</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
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
<td align="left">NOP</td>
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
<td align="right">4,093,340</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">144,183,060</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">4,093,340</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,093,340</td>
<td align="right">2.8%</td>
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
<td align="right">4,093,340</td>
<td align="right">2.8%</td>
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
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,225,780</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">3,686,620</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">148,276,400</td>
<td align="right">100.0%</td>
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
<td align="right">73,729,340</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">73,729,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">36,492,367</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">36,490,887</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">36,489,676</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,228,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">84,332,943</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">616,602,678</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">1,066,315,492</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">641,805,632</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">1,228,800</td>
<td align="right">100.0%</td>
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
<td align="right">16,800,428</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">3,181</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,651</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">10,650,070</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">730</td>
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
<td align="right">3,160</td>
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
<td align="right">2,200</td>
<td align="right">69.6%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">20</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">960</td>
<td align="right">30.4%</td>
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
<td align="right">20</td>
<td align="right">0.6%</td>
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
<td align="right">176,848,740</td>
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
<td align="right">4,416,775,239</td>
<td align="right">2,497.5%</td>
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
<td align="right">2,200</td>
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
<td align="right">2,060</td>
<td align="right">93.6%</td>
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
<td align="right">140</td>
<td align="right">6.4%</td>
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
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">200</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">100</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">980</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">400</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">340</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">80</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">40</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">40</td>
<td align="right">1.8%</td>
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
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">280</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">600</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">660</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">340</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">120</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">40</td>
<td align="right">1.8%</td>
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
<td align="left">_SET_IP</td>
<td align="right">291,998,207</td>
<td align="right">6.6%</td>
<td align="right">6.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">258,720,918</td>
<td align="right">5.9%</td>
<td align="right">12.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">216,277,980</td>
<td align="right">4.9%</td>
<td align="right">17.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">176,848,740</td>
<td align="right">4.0%</td>
<td align="right">21.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">159,655,240</td>
<td align="right">3.6%</td>
<td align="right">25.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">148,732,840</td>
<td align="right">3.4%</td>
<td align="right">28.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">148,251,780</td>
<td align="right">3.4%</td>
<td align="right">31.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">144,094,278</td>
<td align="right">3.3%</td>
<td align="right">35.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">143,310,760</td>
<td align="right">3.2%</td>
<td align="right">38.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">143,310,760</td>
<td align="right">3.2%</td>
<td align="right">41.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">143,307,460</td>
<td align="right">3.2%</td>
<td align="right">44.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">143,006,649</td>
<td align="right">3.2%</td>
<td align="right">47.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">143,006,649</td>
<td align="right">3.2%</td>
<td align="right">51.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">143,006,649</td>
<td align="right">3.2%</td>
<td align="right">54.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">129,507,740</td>
<td align="right">2.9%</td>
<td align="right">57.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">129,507,740</td>
<td align="right">2.9%</td>
<td align="right">60.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">127,051,420</td>
<td align="right">2.9%</td>
<td align="right">63.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">119,982,520</td>
<td align="right">2.7%</td>
<td align="right">65.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">119,169,960</td>
<td align="right">2.7%</td>
<td align="right">68.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">100,706,440</td>
<td align="right">2.3%</td>
<td align="right">70.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">90,884,729</td>
<td align="right">2.1%</td>
<td align="right">72.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">90,468,189</td>
<td align="right">2.0%</td>
<td align="right">75.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">79,423,760</td>
<td align="right">1.8%</td>
<td align="right">76.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">78,186,589</td>
<td align="right">1.8%</td>
<td align="right">78.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">77,082,460</td>
<td align="right">1.7%</td>
<td align="right">80.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">76,142,300</td>
<td align="right">1.7%</td>
<td align="right">82.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">75,713,040</td>
<td align="right">1.7%</td>
<td align="right">83.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">54,884,880</td>
<td align="right">1.2%</td>
<td align="right">85.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">52,538,460</td>
<td align="right">1.2%</td>
<td align="right">86.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">41,370,769</td>
<td align="right">0.9%</td>
<td align="right">87.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">32,289,436</td>
<td align="right">0.7%</td>
<td align="right">87.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">31,876,800</td>
<td align="right">0.7%</td>
<td align="right">88.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">30,665,160</td>
<td align="right">0.7%</td>
<td align="right">89.2%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">26,966,018</td>
<td align="right">0.6%</td>
<td align="right">89.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">26,966,018</td>
<td align="right">0.6%</td>
<td align="right">90.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">24,539,020</td>
<td align="right">0.6%</td>
<td align="right">91.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">19,608,429</td>
<td align="right">0.4%</td>
<td align="right">91.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">17,218,160</td>
<td align="right">0.4%</td>
<td align="right">91.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">14,726,658</td>
<td align="right">0.3%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">13,504,080</td>
<td align="right">0.3%</td>
<td align="right">92.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">13,489,600</td>
<td align="right">0.3%</td>
<td align="right">92.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">12,676,429</td>
<td align="right">0.3%</td>
<td align="right">93.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">12,252,320</td>
<td align="right">0.3%</td>
<td align="right">93.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">11,865,600</td>
<td align="right">0.3%</td>
<td align="right">93.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">11,457,600</td>
<td align="right">0.3%</td>
<td align="right">93.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">11,448,280</td>
<td align="right">0.3%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">11,045,840</td>
<td align="right">0.3%</td>
<td align="right">94.4%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">9,823,360</td>
<td align="right">0.2%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,590,920</td>
<td align="right">0.2%</td>
<td align="right">94.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">8,590,920</td>
<td align="right">0.2%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">8,588,400</td>
<td align="right">0.2%</td>
<td align="right">95.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">8,584,749</td>
<td align="right">0.2%</td>
<td align="right">95.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">8,584,749</td>
<td align="right">0.2%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">7,777,760</td>
<td align="right">0.2%</td>
<td align="right">95.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">7,764,109</td>
<td align="right">0.2%</td>
<td align="right">95.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">7,366,400</td>
<td align="right">0.2%</td>
<td align="right">96.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">7,365,069</td>
<td align="right">0.2%</td>
<td align="right">96.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">6,141,440</td>
<td align="right">0.1%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">6,141,080</td>
<td align="right">0.1%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">6,139,760</td>
<td align="right">0.1%</td>
<td align="right">96.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">6,138,880</td>
<td align="right">0.1%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">6,136,960</td>
<td align="right">0.1%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">6,134,600</td>
<td align="right">0.1%</td>
<td align="right">97.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">6,129,280</td>
<td align="right">0.1%</td>
<td align="right">97.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">5,364,800</td>
<td align="right">0.1%</td>
<td align="right">97.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">5,364,800</td>
<td align="right">0.1%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">5,364,560</td>
<td align="right">0.1%</td>
<td align="right">97.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">5,307,880</td>
<td align="right">0.1%</td>
<td align="right">97.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">4,911,600</td>
<td align="right">0.1%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">4,911,400</td>
<td align="right">0.1%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">4,908,840</td>
<td align="right">0.1%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">4,908,160</td>
<td align="right">0.1%</td>
<td align="right">98.2%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">4,908,160</td>
<td align="right">0.1%</td>
<td align="right">98.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">4,903,040</td>
<td align="right">0.1%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">4,903,040</td>
<td align="right">0.1%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">4,897,920</td>
<td align="right">0.1%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">4,897,280</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">4,091,460</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">3,681,920</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,680,000</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,679,760</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">2,456,320</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">2,456,320</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,456,320</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,456,320</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">2,455,080</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,453,840</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">2,453,760</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,448,229</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,634,240</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,268,720</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">1,228,160</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">1,228,160</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,228,160</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,228,160</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">1,228,160</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,228,160</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">1,228,160</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,228,160</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">1,225,600</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">1,225,600</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,225,600</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,225,600</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">1,225,280</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">1,223,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,223,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">408,640</td>
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
<td align="right">540</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">540</td>
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
<td align="right">60</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-08-30
