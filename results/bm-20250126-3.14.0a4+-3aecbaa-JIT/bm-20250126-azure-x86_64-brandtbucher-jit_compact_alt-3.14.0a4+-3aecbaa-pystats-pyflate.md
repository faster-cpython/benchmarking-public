
# Pystats results

- benchmark: pyflate
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
<td align="right">336,539,580</td>
<td align="right">18.4%</td>
<td align="right">18.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">168,030,860</td>
<td align="right">9.2%</td>
<td align="right">27.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">123,311,180</td>
<td align="right">6.7%</td>
<td align="right">34.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">97,942,020</td>
<td align="right">5.4%</td>
<td align="right">39.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">97,743,900</td>
<td align="right">5.4%</td>
<td align="right">45.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">94,228,340</td>
<td align="right">5.2%</td>
<td align="right">50.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">81,594,420</td>
<td align="right">4.5%</td>
<td align="right">54.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">68,517,260</td>
<td align="right">3.8%</td>
<td align="right">58.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">68,459,280</td>
<td align="right">3.7%</td>
<td align="right">62.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">68,459,280</td>
<td align="right">3.7%</td>
<td align="right">65.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">67,994,080</td>
<td align="right">3.7%</td>
<td align="right">69.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">58,031,080</td>
<td align="right">3.2%</td>
<td align="right">72.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">46,001,000</td>
<td align="right">2.5%</td>
<td align="right">75.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">45,985,140</td>
<td align="right">2.5%</td>
<td align="right">77.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">43,258,000</td>
<td align="right">2.4%</td>
<td align="right">80.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">42,631,400</td>
<td align="right">2.3%</td>
<td align="right">82.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">40,342,080</td>
<td align="right">2.2%</td>
<td align="right">84.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">36,978,800</td>
<td align="right">2.0%</td>
<td align="right">86.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">36,420,320</td>
<td align="right">2.0%</td>
<td align="right">88.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">23,134,320</td>
<td align="right">1.3%</td>
<td align="right">90.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">21,584,000</td>
<td align="right">1.2%</td>
<td align="right">91.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">20,477,160</td>
<td align="right">1.1%</td>
<td align="right">92.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">20,245,720</td>
<td align="right">1.1%</td>
<td align="right">93.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">20,216,460</td>
<td align="right">1.1%</td>
<td align="right">94.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">20,191,540</td>
<td align="right">1.1%</td>
<td align="right">95.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,633,480</td>
<td align="right">1.0%</td>
<td align="right">96.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">15,001,760</td>
<td align="right">0.8%</td>
<td align="right">97.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,722,940</td>
<td align="right">0.5%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">9,403,440</td>
<td align="right">0.5%</td>
<td align="right">98.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,928,160</td>
<td align="right">0.5%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">8,905,140</td>
<td align="right">0.5%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,652,820</td>
<td align="right">0.3%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">515,340</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">512,760</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">333,060</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">261,660</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">108,200</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">89,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">69,160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">62,640</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">54,800</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">53,400</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">53,240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">52,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">45,100</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">33,720</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">30,900</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">30,700</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">29,880</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">24,060</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">15,540</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">15,420</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">8,700</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">2,240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">720</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">700</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">620</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">380</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">120</td>
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
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD_LAZY_DICT</td>
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
<td align="left">CALL_INTRINSIC_1</td>
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
<td align="left">IS_OP</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
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
<td align="left">MAKE_CELL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
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
<td align="left">COMPARE_OP_STR</td>
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
<td align="left">COMPARE_OP_INT POP_JUMP_IF_FALSE</td>
<td align="right">97,426,260</td>
<td align="right">5.3%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_SMALL_INT</td>
<td align="right">88,117,040</td>
<td align="right">4.8%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_OP_ADD_INT</td>
<td align="right">78,088,420</td>
<td align="right">4.3%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">63,199,440</td>
<td align="right">3.5%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_FAST</td>
<td align="right">54,528,840</td>
<td align="right">3.0%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_METHOD_NO_DICT</td>
<td align="right">46,000,700</td>
<td align="right">2.5%</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_OP_SUBTRACT_INT</td>
<td align="right">43,221,660</td>
<td align="right">2.4%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">42,349,180</td>
<td align="right">2.3%</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT</td>
<td align="right">40,342,080</td>
<td align="right">2.2%</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN PUSH_NULL</td>
<td align="right">36,978,800</td>
<td align="right">2.0%</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">36,434,420</td>
<td align="right">2.0%</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_LEN</td>
<td align="right">36,420,260</td>
<td align="right">2.0%</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">35,517,840</td>
<td align="right">1.9%</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">SWAP COPY</td>
<td align="right">28,117,080</td>
<td align="right">1.5%</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">COPY COMPARE_OP_INT</td>
<td align="right">28,117,040</td>
<td align="right">1.5%</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT COMPARE_OP_INT</td>
<td align="right">26,936,020</td>
<td align="right">1.5%</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">25,784,820</td>
<td align="right">1.4%</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND JUMP_BACKWARD</td>
<td align="right">25,784,340</td>
<td align="right">1.4%</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT STORE_FAST</td>
<td align="right">25,739,220</td>
<td align="right">1.4%</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT COMPARE_OP_INT</td>
<td align="right">23,511,240</td>
<td align="right">1.3%</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">22,459,300</td>
<td align="right">1.2%</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT STORE_FAST</td>
<td align="right">22,040,220</td>
<td align="right">1.2%</td>
<td align="right">50.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST JUMP_BACKWARD</td>
<td align="right">21,729,360</td>
<td align="right">1.2%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD LOAD_FAST</td>
<td align="right">21,583,820</td>
<td align="right">1.2%</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD FOR_ITER_RANGE</td>
<td align="right">20,447,100</td>
<td align="right">1.1%</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE STORE_FAST</td>
<td align="right">20,447,100</td>
<td align="right">1.1%</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST</td>
<td align="right">20,216,260</td>
<td align="right">1.1%</td>
<td align="right">56.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD FOR_ITER</td>
<td align="right">20,186,460</td>
<td align="right">1.1%</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">20,186,400</td>
<td align="right">1.1%</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT LOAD_FAST_LOAD_FAST</td>
<td align="right">20,171,100</td>
<td align="right">1.1%</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR CALL_LIST_APPEND</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">COPY COPY</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">COPY BINARY_SUBSCR_LIST_INT</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">63.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST BINARY_SUBSCR</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST COPY</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">SWAP SWAP</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">SWAP STORE_SUBSCR_LIST_INT</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">69.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT SWAP</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT LOAD_SMALL_INT</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT STORE_SUBSCR_LIST_INT</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT JUMP_BACKWARD</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT LOAD_FAST_LOAD_FAST</td>
<td align="right">20,171,040</td>
<td align="right">1.1%</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT BINARY_SUBSCR</td>
<td align="right">19,724,640</td>
<td align="right">1.1%</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR SWAP</td>
<td align="right">19,167,780</td>
<td align="right">1.0%</td>
<td align="right">77.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT BINARY_SLICE</td>
<td align="right">18,633,480</td>
<td align="right">1.0%</td>
<td align="right">78.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD LOAD_FAST</td>
<td align="right">18,375,900</td>
<td align="right">1.0%</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN COMPARE_OP_INT</td>
<td align="right">18,298,980</td>
<td align="right">1.0%</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR LOAD_FAST</td>
<td align="right">18,120,960</td>
<td align="right">1.0%</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BINARY_SUBSCR</td>
<td align="right">18,120,960</td>
<td align="right">1.0%</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_FAST_LOAD_FAST</td>
<td align="right">18,120,960</td>
<td align="right">1.0%</td>
<td align="right">83.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_SMALL_INT</td>
<td align="right">18,120,960</td>
<td align="right">1.0%</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN LOAD_SMALL_INT</td>
<td align="right">18,120,960</td>
<td align="right">1.0%</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND LOAD_FAST</td>
<td align="right">18,120,960</td>
<td align="right">1.0%</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE CALL_LIST_APPEND</td>
<td align="right">17,608,440</td>
<td align="right">1.0%</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">POP_TOP JUMP_FORWARD</td>
<td align="right">17,564,360</td>
<td align="right">1.0%</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE POP_TOP</td>
<td align="right">17,564,100</td>
<td align="right">1.0%</td>
<td align="right">89.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_SMALL_INT</td>
<td align="right">11,207,040</td>
<td align="right">0.6%</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_METHOD_WITH_VALUES</td>
<td align="right">9,369,460</td>
<td align="right">0.5%</td>
<td align="right">90.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_SMALL_INT</td>
<td align="right">9,127,440</td>
<td align="right">0.5%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT LOAD_FAST</td>
<td align="right">8,949,420</td>
<td align="right">0.5%</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST SWAP</td>
<td align="right">8,949,300</td>
<td align="right">0.5%</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT STORE_FAST</td>
<td align="right">8,930,040</td>
<td align="right">0.5%</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_CONST_IMMORTAL</td>
<td align="right">8,926,100</td>
<td align="right">0.5%</td>
<td align="right">92.8%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST</td>
<td align="right">8,905,140</td>
<td align="right">0.5%</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS STORE_FAST</td>
<td align="right">8,898,120</td>
<td align="right">0.5%</td>
<td align="right">93.8%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES LOAD_FAST</td>
<td align="right">8,896,380</td>
<td align="right">0.5%</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL CALL_PY_EXACT_ARGS</td>
<td align="right">8,896,300</td>
<td align="right">0.5%</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD NOP</td>
<td align="right">8,896,260</td>
<td align="right">0.5%</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE PUSH_NULL</td>
<td align="right">5,652,000</td>
<td align="right">0.3%</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST BINARY_OP</td>
<td align="right">5,585,840</td>
<td align="right">0.3%</td>
<td align="right">95.9%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST</td>
<td align="right">5,569,080</td>
<td align="right">0.3%</td>
<td align="right">96.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS POP_TOP</td>
<td align="right">5,568,680</td>
<td align="right">0.3%</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">5,390,940</td>
<td align="right">0.3%</td>
<td align="right">96.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_LIST_APPEND</td>
<td align="right">5,390,580</td>
<td align="right">0.3%</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT BINARY_SUBSCR_LIST_INT</td>
<td align="right">5,390,220</td>
<td align="right">0.3%</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT CALL_PY_EXACT_ARGS</td>
<td align="right">5,390,220</td>
<td align="right">0.3%</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT STORE_FAST</td>
<td align="right">4,515,780</td>
<td align="right">0.2%</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE JUMP_FORWARD</td>
<td align="right">4,019,520</td>
<td align="right">0.2%</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_FAST</td>
<td align="right">3,684,000</td>
<td align="right">0.2%</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP STORE_FAST</td>
<td align="right">3,591,900</td>
<td align="right">0.2%</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_OP</td>
<td align="right">3,521,480</td>
<td align="right">0.2%</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP BINARY_OP_ADD_INT</td>
<td align="right">3,506,000</td>
<td align="right">0.2%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP CALL_LIST_APPEND</td>
<td align="right">2,592,360</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,258,000</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT LOAD_FAST</td>
<td align="right">2,079,840</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND LOAD_SMALL_INT</td>
<td align="right">2,079,840</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST</td>
<td align="right">1,735,560</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR COMPARE_OP_INT</td>
<td align="right">556,860</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT POP_JUMP_IF_FALSE</td>
<td align="right">515,340</td>
<td align="right">0.0%</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE CALL_BUILTIN_O</td>
<td align="right">512,520</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE LOAD_GLOBAL_BUILTIN</td>
<td align="right">512,520</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT BINARY_OP</td>
<td align="right">512,520</td>
<td align="right">0.0%</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT LOAD_FAST</td>
<td align="right">512,520</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O LOAD_SMALL_INT</td>
<td align="right">512,520</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES LOAD_SMALL_INT</td>
<td align="right">506,160</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT CALL_PY_EXACT_ARGS</td>
<td align="right">506,000</td>
<td align="right">0.0%</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS TO_BOOL_INT</td>
<td align="right">470,460</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT POP_JUMP_IF_TRUE</td>
<td align="right">317,640</td>
<td align="right">0.0%</td>
<td align="right">99.8%</td>
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
<td align="right">18,633,480</td>
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
<td align="left">CALL_LIST_APPEND</td>
<td align="right">17,608,440</td>
<td align="right">94.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">512,520</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">512,520</td>
<td align="right">2.8%</td>
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
<td align="right">52,980</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,171,040</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">19,724,640</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,120,960</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">14,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">20,171,040</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">19,167,780</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,120,960</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">556,860</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">14,220</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">60</td>
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
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">29,560</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">23,840</td>
<td align="right">44.6%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">53,400</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">30,120</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">400</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">200</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">120</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">30,060</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">660</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">120</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">60</td>
<td align="right">0.2%</td>
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
<td align="right">52,920</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">8,896,260</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">8,700</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">120</td>
<td align="right">0.0%</td>
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
<td align="right">8,905,140</td>
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
<td align="right">30,060</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">460</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">180</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">29,760</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">460</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">240</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">60</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">0.2%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">17,564,100</td>
<td align="right">75.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,568,680</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">17,564,360</td>
<td align="right">75.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,569,080</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">0.0%</td>
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
<td align="right">36,978,800</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,652,000</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
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
<td align="right">42,349,180</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">280,860</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">160</td>
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
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">53,400</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">52,920</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,220</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">360</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">52,920</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">29,400</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">23,840</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">960</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">900</td>
<td align="right">0.8%</td>
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
<td align="right">60</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">20</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">60</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">40</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">20</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">20</td>
<td align="right">14.3%</td>
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
<td align="right">5,585,840</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,521,480</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">512,520</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">67,880</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">29,760</td>
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
<td align="right">3,591,900</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,506,000</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,592,360</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,360</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">14,400</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">53,280</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">14,400</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">540</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">320</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">200</td>
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
<td align="left">BINARY_OP</td>
<td align="right">67,880</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,040</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">60</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">60</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">60</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">52,920</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">200</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="right">52,920</td>
<td align="right">99.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">200</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">60</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">40</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">420</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">180</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">160</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">100</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">80</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">440</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">180</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">140</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">80</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">80</td>
<td align="right">6.8%</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">60</td>
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
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">240</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">40</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">40</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">40</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">20</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">180</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">140</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">40</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">20</td>
<td align="right">5.3%</td>
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
<td align="right">28,117,080</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">20,171,040</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,171,040</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">28,117,040</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">20,171,040</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">20,171,040</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">60</td>
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
<td align="right">20,186,460</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">20,186,400</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">180</td>
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
<td align="left">CALL_LIST_APPEND</td>
<td align="right">25,784,340</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,729,360</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">20,171,040</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">268,560</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">31,960</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">20,447,100</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">20,186,460</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,375,900</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">8,896,260</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">88,360</td>
<td align="right">0.1%</td>
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
<td align="left">POP_TOP</td>
<td align="right">17,564,360</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,019,520</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
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
<td align="right">21,583,820</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">8,700</td>
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
<td align="right">8,700</td>
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
<td align="left">LOAD_DEREF</td>
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
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">60</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">300</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">140</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20</td>
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
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">200</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">160</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">100</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20</td>
<td align="right">4.2%</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">63,199,440</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">54,528,840</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">42,349,180</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">35,517,840</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">25,784,820</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">88,117,040</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">54,528,840</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">46,000,700</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">36,434,420</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">36,420,260</td>
<td align="right">10.8%</td>
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
<td align="right">60</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
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
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">60</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">60</td>
<td align="right">50.0%</td>
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
<td align="left">PUSH_NULL</td>
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
<td align="right">22,459,300</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">20,171,100</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,171,040</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">20,171,040</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">20,171,040</td>
<td align="right">16.4%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">40,342,080</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">20,171,040</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">20,171,040</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,171,040</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">18,120,960</td>
<td align="right">14.7%</td>
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
<td align="right">300</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">100</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">80</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">60</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">40</td>
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
<td align="right">420</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">300</td>
<td align="right">41.7%</td>
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
<td align="right">360</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">200</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">40</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">40</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">40</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">260</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">260</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">100</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">40</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_LAZY_DICT</td>
<td align="right">40</td>
<td align="right">5.7%</td>
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
<td align="right">88,117,040</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">20,171,040</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">18,120,960</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">18,120,960</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,207,040</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">78,088,420</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">43,221,660</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">26,936,020</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,949,420</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,515,780</td>
<td align="right">2.7%</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">97,426,260</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">515,340</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
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
<td align="right">63,199,440</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">17,564,100</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">11,207,040</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,019,520</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,735,560</td>
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
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">60</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">317,640</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">15,420</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">268,560</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">55,480</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">8,740</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">200</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">60</td>
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
<td align="right">140</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">160</td>
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
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">25,739,220</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">22,040,220</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">20,447,100</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">8,930,040</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,898,120</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">35,517,840</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">22,459,300</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">21,729,360</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">9,127,440</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,390,940</td>
<td align="right">5.7%</td>
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
<td align="right">20,216,260</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">29,400</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
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
<td align="right">20,171,040</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">74,620</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">60</td>
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
<td align="right">20,171,040</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">20,171,040</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">19,167,780</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,949,300</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
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
<td align="left">COPY</td>
<td align="right">28,117,080</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">20,171,040</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">20,171,040</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">60</td>
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
<td align="right">78,088,420</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,506,000</td>
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
<td align="right">22,040,220</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">20,171,040</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">19,724,640</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,633,480</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">512,520</td>
<td align="right">0.6%</td>
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
<td align="right">33,720</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">33,720</td>
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
<td align="left">STORE_FAST</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">43,221,660</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">33,720</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">40</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">23,511,240</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,930,040</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">5,390,220</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,390,220</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">33,720</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">40,342,080</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">20,171,040</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,390,220</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,258,000</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">177,960</td>
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
<td align="right">25,739,220</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">20,171,040</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">20,171,040</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,079,840</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">177,960</td>
<td align="right">0.3%</td>
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
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">29,400</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">440</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">29,560</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">320</td>
<td align="right">1.1%</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">29,400</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">14,400</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">800</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">200</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">180</td>
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
<td align="left">GET_ITER</td>
<td align="right">30,120</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">14,400</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">400</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">120</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">40</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">24,060</td>
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
<td align="right">15,360</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">8,700</td>
<td align="right">36.2%</td>
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
<td align="left">CALL</td>
<td align="right">80</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">80</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">40</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">60</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">40</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">40</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
<td align="right">8.3%</td>
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
<td align="left">BINARY_SLICE</td>
<td align="right">512,520</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">160</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">512,520</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">120</td>
<td align="right">100.0%</td>
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
<td align="left">POP_TOP</td>
<td align="right">200</td>
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
<td align="right">36,420,260</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">18,298,980</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">18,120,960</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="left">BINARY_SUBSCR</td>
<td align="right">20,171,040</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">17,608,440</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,390,580</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,592,360</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">177,960</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">25,784,340</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,120,960</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,079,840</td>
<td align="right">4.5%</td>
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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">15,360</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="left">CALL_LIST_APPEND</td>
<td align="right">15,360</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">60</td>
<td align="right">0.4%</td>
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
<td align="right">80</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">60</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_LAZY_DICT</td>
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
<td align="left">POP_TOP</td>
<td align="right">60</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">60</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">20</td>
<td align="right">11.1%</td>
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
<td align="right">80</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">60</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
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
<td align="left">POP_TOP</td>
<td align="right">60</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">33.3%</td>
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
<td align="right">240</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">160</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">140</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">40</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">40</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">200</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">120</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">120</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">60</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">9.7%</td>
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
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,896,300</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,390,220</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">506,000</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">207,720</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">800</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">8,898,120</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,568,680</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">470,460</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">33,720</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">29,400</td>
<td align="right">0.2%</td>
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
<td align="right">28,117,040</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">26,936,020</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">23,511,240</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">18,298,980</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">556,860</td>
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
<td align="right">97,426,260</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">317,640</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">88,360</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">660</td>
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
<td align="right">59,160</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">29,400</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">460</td>
<td align="right">0.5%</td>
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
<td align="right">20,447,100</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">30,060</td>
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
<td align="right">20,447,100</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">30,060</td>
<td align="right">0.1%</td>
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
<td align="right">258,900</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,600</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">160</td>
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
<td align="right">146,680</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">58,800</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">52,920</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,560</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">400</td>
<td align="right">0.2%</td>
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
<td align="right">200</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">100</td>
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
<td align="right">300</td>
<td align="right">100.0%</td>
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
<td align="right">8,926,100</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">8,896,300</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">29,400</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">1,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">180</td>
<td align="right">0.0%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">960</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">500</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">400</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">200</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">60</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,020</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">400</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">240</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">200</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">200</td>
<td align="right">8.9%</td>
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
<td align="right">36,434,420</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">512,520</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">29,440</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">520</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">36,978,800</td>
<td align="right">100.0%</td>
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
<td align="right">5,390,940</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">178,080</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">44,960</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">29,400</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,740</td>
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
<td align="right">5,652,000</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">120</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">80</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
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
<td align="left">LOAD_SMALL_INT</td>
<td align="right">60</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">40</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
<td align="right">16.7%</td>
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
<td align="right">46,000,700</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
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
<td align="right">25,784,820</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,171,100</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">44,960</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="right">9,369,460</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">33,720</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">8,896,380</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">506,160</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
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
<td align="left">CACHE</td>
<td align="right">52,980</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,320</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">320</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">60</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">53,400</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">400</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">400</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">320</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">120</td>
<td align="right">0.2%</td>
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
<td align="right">32,840</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">29,640</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">160</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">31,960</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">29,400</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">780</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">320</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">180</td>
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
<td align="right">20,171,040</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">20,171,040</td>
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
<td align="right">20,171,040</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">20,171,040</td>
<td align="right">50.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">15,400</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">120</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">15,420</td>
<td align="right">99.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">120</td>
<td align="right">0.8%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">470,460</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">29,440</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">15,360</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
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

<table>
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
<td align="right">515,340</td>
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
<td align="right">20,186,400</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">29,400</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">20,216,260</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">200</td>
<td align="right">0.0%</td>
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
<td align="right">9,720,120</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">226,917,180</td>
<td align="right">95.9%</td>
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
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,760</td>
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
<td align="left">lshift</td>
<td align="right">1,740</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">660</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">140</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">140</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">80</td>
<td align="right">2.9%</td>
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
<td align="right">18,633,480</td>
<td align="right">100.0%</td>
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
<td align="right">58,016,840</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">68,517,480</td>
<td align="right">54.1%</td>
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
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">14,220</td>
<td align="right">99.9%</td>
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
<td align="left">buffer int</td>
<td align="right">14,200</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">20</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">191,196,300</td>
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
<td align="right">1,180</td>
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
<td align="right">180</td>
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
<td align="right">241,876,620</td>
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
<td align="right">160</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">20.0%</td>
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
<td align="right">40</td>
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
<td align="right">20,186,580</td>
<td align="right">49.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">20,566,180</td>
<td align="right">50.5%</td>
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
<td align="right">4,960</td>
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
<td align="left">enumerate</td>
<td align="right">4,960</td>
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
<td align="right">200</td>
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
<td align="right">460,713,120</td>
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
<td align="right">260</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">7.1%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">20</td>
<td align="right">100.0%</td>
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
<td align="right">50,863,500</td>
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
<td align="right">720</td>
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
<td align="right">260</td>
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
<td align="right">400</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">9.1%</td>
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
<td align="right">50.0%</td>
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
<td align="right">35,343,900</td>
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
<td align="right">160</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">40,342,080</td>
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
<td align="right">106,589,160</td>
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
<td align="right">60</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">25.0%</td>
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
<td align="right">20</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">20,240,460</td>
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
<td align="right">1,142,206,440</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">106,582,820</td>
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
<td align="right">578,185,100</td>
<td align="right">31.6%</td>
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
<td align="left">BINARY_SUBSCR</td>
<td align="right">58,016,840</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">20,186,580</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">18,633,480</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">9,720,120</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">60</td>
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
<td align="right">52,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">95,931,300</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">52,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">52,980</td>
<td align="right">0.1%</td>
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
<td align="right">52,980</td>
<td align="right">0.1%</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">52,920</td>
<td align="right">0.1%</td>
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
<td align="right">96,037,680</td>
<td align="right">100.1%</td>
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
<td align="right">241,191,180</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">241,191,380</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">64,339,040</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">48,089,060</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">16,248,580</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">64,339,418</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">53,400</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">691,883,000</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,077,970,180</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">873,156,960</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">759,383,378</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">197,435,320</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">591,325,840</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">3,302,806,684</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">3,508,349,506</td>
<td align="right">59.1%</td>
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
<td align="right">3,777</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">123</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">15,491</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">9</td>
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
<td align="right">176,829,020</td>
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
<td align="right">7,677,868,000</td>
<td align="right">4,342.0%</td>
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
<td align="right">1,778,052,080</td>
<td align="right">23.2%</td>
<td align="right">23.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">851,273,300</td>
<td align="right">11.1%</td>
<td align="right">34.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">557,526,880</td>
<td align="right">7.3%</td>
<td align="right">41.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">463,801,160</td>
<td align="right">6.0%</td>
<td align="right">47.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">405,046,600</td>
<td align="right">5.3%</td>
<td align="right">52.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">320,116,860</td>
<td align="right">4.2%</td>
<td align="right">57.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">320,116,860</td>
<td align="right">4.2%</td>
<td align="right">61.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">246,163,640</td>
<td align="right">3.2%</td>
<td align="right">64.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">197,126,520</td>
<td align="right">2.6%</td>
<td align="right">66.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">144,132,660</td>
<td align="right">1.9%</td>
<td align="right">68.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">135,707,160</td>
<td align="right">1.8%</td>
<td align="right">70.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">131,263,400</td>
<td align="right">1.7%</td>
<td align="right">72.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">120,785,600</td>
<td align="right">1.6%</td>
<td align="right">73.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">108,395,740</td>
<td align="right">1.4%</td>
<td align="right">75.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">106,034,760</td>
<td align="right">1.4%</td>
<td align="right">76.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">95,929,480</td>
<td align="right">1.2%</td>
<td align="right">77.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">95,929,480</td>
<td align="right">1.2%</td>
<td align="right">79.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">80,899,540</td>
<td align="right">1.1%</td>
<td align="right">80.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">80,899,540</td>
<td align="right">1.1%</td>
<td align="right">81.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">80,876,020</td>
<td align="right">1.1%</td>
<td align="right">82.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">80,876,020</td>
<td align="right">1.1%</td>
<td align="right">83.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">80,876,020</td>
<td align="right">1.1%</td>
<td align="right">84.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">80,876,020</td>
<td align="right">1.1%</td>
<td align="right">85.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">80,876,020</td>
<td align="right">1.1%</td>
<td align="right">86.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">80,852,340</td>
<td align="right">1.1%</td>
<td align="right">87.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">80,852,340</td>
<td align="right">1.1%</td>
<td align="right">88.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_WITH_VALUES</td>
<td align="right">80,852,340</td>
<td align="right">1.1%</td>
<td align="right">89.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">78,709,940</td>
<td align="right">1.0%</td>
<td align="right">90.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">57,118,140</td>
<td align="right">0.7%</td>
<td align="right">91.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">56,773,140</td>
<td align="right">0.7%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">53,088,260</td>
<td align="right">0.7%</td>
<td align="right">92.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">53,088,260</td>
<td align="right">0.7%</td>
<td align="right">93.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">53,087,940</td>
<td align="right">0.7%</td>
<td align="right">94.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP</td>
<td align="right">48,588,780</td>
<td align="right">0.6%</td>
<td align="right">94.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">43,916,100</td>
<td align="right">0.6%</td>
<td align="right">95.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">37,323,080</td>
<td align="right">0.5%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">35,281,260</td>
<td align="right">0.5%</td>
<td align="right">96.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">35,281,260</td>
<td align="right">0.5%</td>
<td align="right">96.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">35,281,260</td>
<td align="right">0.5%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">35,019,840</td>
<td align="right">0.5%</td>
<td align="right">97.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">25,975,040</td>
<td align="right">0.3%</td>
<td align="right">98.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">23,321,040</td>
<td align="right">0.3%</td>
<td align="right">98.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">16,704,540</td>
<td align="right">0.2%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">15,053,460</td>
<td align="right">0.2%</td>
<td align="right">98.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">9,402,480</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">8,973,180</td>
<td align="right">0.1%</td>
<td align="right">99.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">8,231,560</td>
<td align="right">0.1%</td>
<td align="right">99.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">8,184,520</td>
<td align="right">0.1%</td>
<td align="right">99.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">8,184,520</td>
<td align="right">0.1%</td>
<td align="right">99.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">8,184,520</td>
<td align="right">0.1%</td>
<td align="right">99.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right">5,568,820</td>
<td align="right">0.1%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">5,568,180</td>
<td align="right">0.1%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">4,053,880</td>
<td align="right">0.1%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">4,053,720</td>
<td align="right">0.1%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,053,720</td>
<td align="right">0.1%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">4,053,720</td>
<td align="right">0.1%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_LAZY_DICT</td>
<td align="right">4,053,720</td>
<td align="right">0.1%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">4,053,720</td>
<td align="right">0.1%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">419,820</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">419,820</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">343,380</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">76,760</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">47,360</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">47,360</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">24,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_NO_DICT</td>
<td align="right">23,680</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">23,520</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">23,520</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">23,520</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">23,520</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD</td>
<td align="right">160</td>
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
