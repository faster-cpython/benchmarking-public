
# Pystats results

- benchmark: pathlib
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
<td align="right">35,167,980</td>
<td align="right">15.3%</td>
<td align="right">15.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">13,083,480</td>
<td align="right">5.7%</td>
<td align="right">20.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">13,083,060</td>
<td align="right">5.7%</td>
<td align="right">26.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">12,604,380</td>
<td align="right">5.5%</td>
<td align="right">32.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">12,601,500</td>
<td align="right">5.5%</td>
<td align="right">37.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,482,460</td>
<td align="right">5.4%</td>
<td align="right">43.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">12,001,020</td>
<td align="right">5.2%</td>
<td align="right">48.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">7,562,160</td>
<td align="right">3.3%</td>
<td align="right">51.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,560,720</td>
<td align="right">3.3%</td>
<td align="right">54.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">6,960,600</td>
<td align="right">3.0%</td>
<td align="right">57.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">6,000,360</td>
<td align="right">2.6%</td>
<td align="right">60.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,000,180</td>
<td align="right">2.6%</td>
<td align="right">63.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">5,280,120</td>
<td align="right">2.3%</td>
<td align="right">65.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,043,060</td>
<td align="right">2.2%</td>
<td align="right">67.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,041,020</td>
<td align="right">2.2%</td>
<td align="right">69.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">5,040,120</td>
<td align="right">2.2%</td>
<td align="right">71.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,040,120</td>
<td align="right">2.2%</td>
<td align="right">74.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,921,080</td>
<td align="right">2.1%</td>
<td align="right">76.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,440,420</td>
<td align="right">1.9%</td>
<td align="right">78.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,440,180</td>
<td align="right">1.9%</td>
<td align="right">80.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">3,003,100</td>
<td align="right">1.3%</td>
<td align="right">81.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,002,340</td>
<td align="right">1.3%</td>
<td align="right">82.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,000,360</td>
<td align="right">1.3%</td>
<td align="right">83.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,524,560</td>
<td align="right">1.1%</td>
<td align="right">85.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,523,120</td>
<td align="right">1.1%</td>
<td align="right">86.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,522,100</td>
<td align="right">1.1%</td>
<td align="right">87.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,521,020</td>
<td align="right">1.1%</td>
<td align="right">88.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,520,420</td>
<td align="right">1.1%</td>
<td align="right">89.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,520,120</td>
<td align="right">1.1%</td>
<td align="right">90.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,520,120</td>
<td align="right">1.1%</td>
<td align="right">91.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,520,120</td>
<td align="right">1.1%</td>
<td align="right">92.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">93.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">94.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">2,520,000</td>
<td align="right">1.1%</td>
<td align="right">96.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,402,580</td>
<td align="right">1.0%</td>
<td align="right">97.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,040,060</td>
<td align="right">0.9%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,919,040</td>
<td align="right">0.8%</td>
<td align="right">98.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,446,720</td>
<td align="right">0.6%</td>
<td align="right">99.4%</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">486,720</td>
<td align="right">0.2%</td>
<td align="right">99.6%</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">480,000</td>
<td align="right">0.2%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">480,000</td>
<td align="right">0.2%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">540</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">100</td>
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
<td align="left">JUMP_FORWARD</td>
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
<td align="left">LOAD_SMALL_INT</td>
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
<td align="left">STORE_FAST_STORE_FAST</td>
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
<td align="left">CALL_LEN</td>
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
<td align="left">COMPARE_OP_INT</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
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
<td align="left">BINARY_OP</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
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
<td align="left">CACHE RESUME_CHECK</td>
<td align="right">13,082,160</td>
<td align="right">5.7%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE INTERPRETER_EXIT</td>
<td align="right">12,603,000</td>
<td align="right">5.5%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL LOAD_FAST</td>
<td align="right">12,000,540</td>
<td align="right">5.2%</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_METHOD_NO_DICT</td>
<td align="right">7,562,020</td>
<td align="right">3.3%</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN PUSH_NULL</td>
<td align="right">7,561,260</td>
<td align="right">3.3%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,041,180</td>
<td align="right">2.2%</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">5,040,900</td>
<td align="right">2.2%</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">5,040,240</td>
<td align="right">2.2%</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_MODULE</td>
<td align="right">5,040,120</td>
<td align="right">2.2%</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE TO_BOOL_BOOL</td>
<td align="right">5,040,120</td>
<td align="right">2.2%</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT LOAD_FAST</td>
<td align="right">5,040,060</td>
<td align="right">2.2%</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_ATTR_SLOT</td>
<td align="right">4,441,020</td>
<td align="right">1.9%</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">3,480,060</td>
<td align="right">1.5%</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">POP_TOP JUMP_BACKWARD</td>
<td align="right">3,000,060</td>
<td align="right">1.3%</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK NOP</td>
<td align="right">2,522,940</td>
<td align="right">1.1%</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD LOAD_FAST</td>
<td align="right">2,522,100</td>
<td align="right">1.1%</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">NOP LOAD_FAST</td>
<td align="right">2,522,040</td>
<td align="right">1.1%</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT RETURN_VALUE</td>
<td align="right">2,521,920</td>
<td align="right">1.1%</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL RETURN_VALUE</td>
<td align="right">2,521,200</td>
<td align="right">1.1%</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,521,020</td>
<td align="right">1.1%</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE PUSH_NULL</td>
<td align="right">2,520,360</td>
<td align="right">1.1%</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE</td>
<td align="right">2,520,320</td>
<td align="right">1.1%</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST GET_ITER</td>
<td align="right">2,520,180</td>
<td align="right">1.1%</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL RETURN_VALUE</td>
<td align="right">2,520,120</td>
<td align="right">1.1%</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">2,520,120</td>
<td align="right">1.1%</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_NON_PY_GENERAL</td>
<td align="right">2,520,100</td>
<td align="right">1.1%</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_TUPLE</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">NOP LOAD_GLOBAL_MODULE</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_FAST_LOAD_FAST</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST STORE_FAST</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">IS_OP POP_JUMP_IF_FALSE</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD FOR_ITER_TUPLE</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">60.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_LIST_APPEND</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE NOP</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS STORE_FAST</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND JUMP_BACKWARD</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE POP_ITER</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE STORE_FAST</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_METHOD</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">72.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE IS_OP</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE CALL_ISINSTANCE</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK BUILD_LIST</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">75.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT LOAD_CONST_IMMORTAL</td>
<td align="right">2,520,060</td>
<td align="right">1.1%</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX RETURN_VALUE</td>
<td align="right">2,520,000</td>
<td align="right">1.1%</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_PY_GENERAL</td>
<td align="right">2,520,000</td>
<td align="right">1.1%</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_STR_1</td>
<td align="right">2,520,000</td>
<td align="right">1.1%</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,520,000</td>
<td align="right">1.1%</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL CALL_FUNCTION_EX</td>
<td align="right">2,520,000</td>
<td align="right">1.1%</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL POP_TOP</td>
<td align="right">2,520,000</td>
<td align="right">1.1%</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1 RETURN_VALUE</td>
<td align="right">2,520,000</td>
<td align="right">1.1%</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT CALL_PY_GENERAL</td>
<td align="right">2,520,000</td>
<td align="right">1.1%</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,520,000</td>
<td align="right">1.1%</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD FOR_ITER</td>
<td align="right">2,400,060</td>
<td align="right">1.0%</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER STORE_FAST</td>
<td align="right">2,400,000</td>
<td align="right">1.0%</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_DEREF</td>
<td align="right">2,399,040</td>
<td align="right">1.0%</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD FOR_ITER_LIST</td>
<td align="right">2,040,000</td>
<td align="right">0.9%</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST</td>
<td align="right">2,039,040</td>
<td align="right">0.9%</td>
<td align="right">91.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF PUSH_NULL</td>
<td align="right">1,919,100</td>
<td align="right">0.8%</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF POP_JUMP_IF_NONE</td>
<td align="right">1,919,040</td>
<td align="right">0.8%</td>
<td align="right">93.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE LOAD_DEREF</td>
<td align="right">1,919,040</td>
<td align="right">0.8%</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT CALL_NON_PY_GENERAL</td>
<td align="right">1,919,040</td>
<td align="right">0.8%</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE JUMP_BACKWARD</td>
<td align="right">1,440,000</td>
<td align="right">0.6%</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL TO_BOOL_NONE</td>
<td align="right">1,440,000</td>
<td align="right">0.6%</td>
<td align="right">96.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE POP_JUMP_IF_TRUE</td>
<td align="right">1,440,000</td>
<td align="right">0.6%</td>
<td align="right">96.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF TO_BOOL_BOOL</td>
<td align="right">960,000</td>
<td align="right">0.4%</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF LOAD_METHOD</td>
<td align="right">481,920</td>
<td align="right">0.2%</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD LOAD_FAST_LOAD_FAST</td>
<td align="right">480,060</td>
<td align="right">0.2%</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST</td>
<td align="right">480,060</td>
<td align="right">0.2%</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST YIELD_VALUE</td>
<td align="right">480,000</td>
<td align="right">0.2%</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST LOAD_ATTR_SLOT</td>
<td align="right">480,000</td>
<td align="right">0.2%</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_DEREF</td>
<td align="right">480,000</td>
<td align="right">0.2%</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_DEREF</td>
<td align="right">480,000</td>
<td align="right">0.2%</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE INTERPRETER_EXIT</td>
<td align="right">480,000</td>
<td align="right">0.2%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST STORE_FAST</td>
<td align="right">480,000</td>
<td align="right">0.2%</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT CALL_BUILTIN_FAST</td>
<td align="right">480,000</td>
<td align="right">0.2%</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK POP_TOP</td>
<td align="right">480,000</td>
<td align="right">0.2%</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE</td>
<td align="right">480,000</td>
<td align="right">0.2%</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL TO_BOOL_ALWAYS_TRUE</td>
<td align="right">479,040</td>
<td align="right">0.2%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE TO_BOOL_NONE</td>
<td align="right">6,720</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE TO_BOOL_ALWAYS_TRUE</td>
<td align="right">6,720</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL LOAD_CONST_IMMORTAL</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER POP_ITER</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_FAST</td>
<td align="right">1,500</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_CONST_IMMORTAL</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS STORE_FAST</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL POP_TOP</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST POP_ITER</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST CALL_BUILTIN_CLASS</td>
<td align="right">1,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT CALL_PY_EXACT_ARGS</td>
<td align="right">1,000</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CACHE POP_TOP</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK RETURN_VALUE</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">NOP LOAD_DEREF</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_CONST_IMMORTAL</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_DEREF</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_TOP RESUME_CHECK</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
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
<td align="right">13,082,160</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">960</td>
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
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,520,000</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">2,520,000</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="right">120</td>
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
<td align="left">CALL_PY_GENERAL</td>
<td align="right">960</td>
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
<td align="right">960</td>
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
<td align="right">2,520,180</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,520,060</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,920</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
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
<td align="right">12,603,000</td>
<td align="right">96.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">480,000</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">60</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">2,522,940</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,520,060</td>
<td align="right">50.0%</td>
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
<td align="right">2,522,040</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,520,060</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">960</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,520,060</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
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
<td align="right">2,520,060</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,500</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">480</td>
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
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,520,000</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">480,000</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,000,060</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">180</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">120</td>
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
<td align="right">7,561,260</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,520,360</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,919,100</td>
<td align="right">16.0%</td>
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
<td align="right">12,000,540</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">80</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,521,920</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,521,200</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,520,120</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,520,000</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">2,520,000</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">12,603,000</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">60</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">20</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">60</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">20</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">20</td>
<td align="right">20.0%</td>
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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20</td>
<td align="right">100.0%</td>
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
<td align="right">2,520,060</td>
<td align="right">100.0%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">2,520,060</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="right">60</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">60</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
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
<td align="right">80</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">40</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">40</td>
<td align="right">11.8%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">120</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">100</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">40</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">20</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20</td>
<td align="right">5.9%</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
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
<td align="left">COMPARE_OP_INT</td>
<td align="right">20</td>
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
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">960</td>
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
<td align="left">LOAD_SPECIAL</td>
<td align="right">960</td>
<td align="right">100.0%</td>
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
<td align="right">2,400,060</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,920</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">600</td>
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
<td align="right">2,400,000</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">600</td>
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
<td align="right">2,520,060</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
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
<td align="right">2,520,060</td>
<td align="right">100.0%</td>
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
<td align="left">POP_TOP</td>
<td align="right">3,000,060</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,520,060</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,440,000</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,520,060</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,400,060</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,040,000</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">480</td>
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
<td align="right">100</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">40</td>
<td align="right">25.0%</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">100</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">60</td>
<td align="right">37.5%</td>
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
<td align="right">2,399,040</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,919,040</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">480,000</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">480,000</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">1,919,100</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,919,040</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">960,000</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">481,920</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">12,000,540</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,040,900</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,040,240</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">5,040,060</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">2,522,100</td>
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
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">7,562,020</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,040,120</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,441,020</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,521,020</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,520,180</td>
<td align="right">7.2%</td>
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
<td align="left">POP_ITER</td>
<td align="right">2,520,060</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">480,060</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,520,060</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">480,000</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="right">60</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">60</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">40</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">20</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">20</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">140</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">60</td>
<td align="right">30.0%</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,520,060</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">481,920</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
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
<td align="right">2,522,100</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">480,060</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
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
<td align="right">960</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">960</td>
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
<td align="right">960</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">960</td>
<td align="right">50.0%</td>
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
<td align="right">3,480,060</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,520,060</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
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
<td align="left">NOP</td>
<td align="right">2,520,060</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,520,000</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">480,060</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">480,000</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">120</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">1,919,040</td>
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
<td align="right">1,919,040</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,520,120</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,440,000</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">480,000</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
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
<td align="right">2,520,060</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,440,000</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">480,000</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">40</td>
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
<td align="left">BUILD_LIST</td>
<td align="right">2,520,060</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,520,060</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,520,060</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,400,000</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,039,040</td>
<td align="right">16.3%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">5,041,180</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">5,040,900</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,399,040</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">80</td>
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
<td align="right">960</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">960</td>
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
<td align="left">LOAD_SPECIAL</td>
<td align="right">960</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">960</td>
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
<td align="right">480,000</td>
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
<td align="right">480,000</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
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
<td align="right">1,000</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">40</td>
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
<td align="left">STORE_FAST</td>
<td align="right">1,080</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">480,000</td>
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
<td align="right">480,000</td>
<td align="right">100.0%</td>
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
<td align="right">2,521,020</td>
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
<td align="right">2,520,060</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">960</td>
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
<td align="right">2,520,060</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,520,060</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,040,120</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">40</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">2,520,060</td>
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
<td align="right">2,520,060</td>
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
<td align="left">LOAD_SPECIAL</td>
<td align="right">960</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">40</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">20</td>
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
<td align="left">STORE_FAST</td>
<td align="right">960</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">20</td>
<td align="right">2.0%</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">2,520,100</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,919,040</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">2,520,120</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,440,000</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">479,040</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">120</td>
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
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">1,000</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">960</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">100</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">80</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">40</td>
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
<td align="left">GET_ITER</td>
<td align="right">960</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">960</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">180</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">60</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">40</td>
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
<td align="right">2,520,000</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">2,520,000</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,520,000</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,520,000</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
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
<td align="right">2,520,000</td>
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
<td align="right">2,520,000</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">60</td>
<td align="right">100.0%</td>
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
<td align="right">2,040,000</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
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
<td align="left">STORE_FAST</td>
<td align="right">2,039,040</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,020</td>
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
<td align="left">JUMP_BACKWARD</td>
<td align="right">480</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
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
<td align="left">STORE_FAST</td>
<td align="right">480</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">60</td>
<td align="right">11.1%</td>
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
<td align="right">2,520,060</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,520,060</td>
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
<td align="left">POP_ITER</td>
<td align="right">2,520,060</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,520,060</td>
<td align="right">50.0%</td>
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
<td align="right">140</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">60</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">80</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">60</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">40</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
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
<td align="right">2,520,320</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">2,520,360</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">60</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">60</td>
<td align="right">50.0%</td>
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
<td align="right">4,441,020</td>
<td align="right">90.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">480,000</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">2,521,920</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,919,040</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">480,000</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">120</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,520,060</td>
<td align="right">99.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,040</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">2,521,200</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,040</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">60</td>
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
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">960</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">60</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">60</td>
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
<td align="left">CALL_PY_GENERAL</td>
<td align="right">960</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">60</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">5.6%</td>
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
<td align="right">5,041,180</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,520,060</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,520,000</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">2,520,000</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
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
<td align="right">7,561,260</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">2,520,060</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,520,060</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">120</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">5,040,120</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,520,060</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
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
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,520,320</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,520,060</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,520,060</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="right">7,562,020</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
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
<td align="right">5,040,060</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,520,000</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">960</td>
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
<td align="left">LOAD_FAST</td>
<td align="right">60</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60</td>
<td align="right">50.0%</td>
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
<td align="right">13,082,160</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
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
<td align="right">5,040,240</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,522,940</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,520,060</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,520,000</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">480,000</td>
<td align="right">3.7%</td>
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
<td align="right">2,520,060</td>
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
<td align="right">2,520,060</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">479,040</td>
<td align="right">98.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">6,720</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">960</td>
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
<td align="right">480,000</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">6,720</td>
<td align="right">1.4%</td>
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
<td align="right">5,040,120</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">960,000</td>
<td align="right">16.0%</td>
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
<td align="right">3,480,060</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,520,120</td>
<td align="right">42.0%</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,440,000</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">6,720</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,440,000</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">6,720</td>
<td align="right">0.5%</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
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

<table>
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
<td align="right">60</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">180</td>
<td align="right">90.0%</td>
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
<td align="right">15,624,600</td>
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
<td align="right">340</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,040</td>
<td align="right">99.8%</td>
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
<td align="right">2,401,980</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,080,720</td>
<td align="right">74.7%</td>
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
<td align="right">600</td>
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
<td align="left">map</td>
<td align="right">600</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">19,586,160</td>
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
<td align="right">120</td>
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
<td align="right">25,214,940</td>
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
<td align="right">200</td>
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
<td align="right">3,002,160</td>
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
<td align="right">100</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">840</td>
<td align="right">89.4%</td>
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
<td align="right">620</td>
<td align="right">73.8%</td>
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
<td align="right">5,044,140</td>
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
<td align="right">9,621,780</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">712,320</td>
<td align="right">6.9%</td>
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
<td align="right">13,460</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">1,140</td>
<td align="right">98.3%</td>
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
<td align="right">134,077,320</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">5,406,560</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">90,164,820</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">712,440</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_METHOD</td>
<td align="right">3,002,160</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,401,980</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
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
<td align="left">EXIT_INIT_CHECK</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">356,160</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">356,160</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">120</td>
<td align="right">0.0%</td>
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
<td align="left">EXIT_INIT_CHECK</td>
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
<td align="right">13,083,120</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,049,420</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">13,083,120</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">12,602,160</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">480,960</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">12,602,160</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">2,521,980</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">60</td>
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
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">17,652,540</td>
<td align="right">97.4%</td>
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
<td align="right">47,781,460</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">47,781,400</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">51,617,660</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">51,617,660</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">58,584,553</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">135,628,680</td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">156,685,000</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">84,664,496</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">157,121,949</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">9,008,040</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">8,414,640</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">51,424,208</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">25,747,835</td>
<td align="right">7.4%</td>
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
<td align="right">487,675</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">85</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">94</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">20,167,303</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">17</td>
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
<td align="right">60</td>
<td align="right">0</td>
<td align="right">743,460</td>
<td align="right">940</td>
<td align="right">124,400</td>
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
<td align="right">7,576,140</td>
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
<td align="right">183,531,300</td>
<td align="right">2,422.5%</td>
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
<td align="right">37,465,680</td>
<td align="right">20.4%</td>
<td align="right">20.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">19,757,400</td>
<td align="right">10.8%</td>
<td align="right">31.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">14,716,620</td>
<td align="right">8.0%</td>
<td align="right">39.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">14,702,820</td>
<td align="right">8.0%</td>
<td align="right">47.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">10,091,760</td>
<td align="right">5.5%</td>
<td align="right">52.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">9,155,580</td>
<td align="right">5.0%</td>
<td align="right">57.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5,048,160</td>
<td align="right">2.8%</td>
<td align="right">60.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">5,048,100</td>
<td align="right">2.8%</td>
<td align="right">63.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,043,000</td>
<td align="right">2.7%</td>
<td align="right">65.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,585,740</td>
<td align="right">2.5%</td>
<td align="right">68.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">4,576,920</td>
<td align="right">2.5%</td>
<td align="right">70.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">4,575,240</td>
<td align="right">2.5%</td>
<td align="right">73.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">2,527,740</td>
<td align="right">1.4%</td>
<td align="right">74.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">2,527,740</td>
<td align="right">1.4%</td>
<td align="right">76.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,527,200</td>
<td align="right">1.4%</td>
<td align="right">77.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right">2,525,760</td>
<td align="right">1.4%</td>
<td align="right">78.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">2,525,040</td>
<td align="right">1.4%</td>
<td align="right">80.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">2,525,040</td>
<td align="right">1.4%</td>
<td align="right">81.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">2,524,980</td>
<td align="right">1.4%</td>
<td align="right">83.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">2,524,980</td>
<td align="right">1.4%</td>
<td align="right">84.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">2,524,980</td>
<td align="right">1.4%</td>
<td align="right">85.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">2,524,260</td>
<td align="right">1.4%</td>
<td align="right">87.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,521,080</td>
<td align="right">1.4%</td>
<td align="right">88.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,520,960</td>
<td align="right">1.4%</td>
<td align="right">89.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">2,520,240</td>
<td align="right">1.4%</td>
<td align="right">91.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">2,520,000</td>
<td align="right">1.4%</td>
<td align="right">92.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">2,520,000</td>
<td align="right">1.4%</td>
<td align="right">94.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">2,520,000</td>
<td align="right">1.4%</td>
<td align="right">95.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP</td>
<td align="right">2,042,040</td>
<td align="right">1.1%</td>
<td align="right">96.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">2,041,320</td>
<td align="right">1.1%</td>
<td align="right">97.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">2,041,080</td>
<td align="right">1.1%</td>
<td align="right">98.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">2,041,020</td>
<td align="right">1.1%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">16,560</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">14,760</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">7,980</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">7,860</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">6,300</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">6,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">6,000</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">5,040</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">5,040</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">4,920</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">4,800</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,800</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">4,020</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,960</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">3,960</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">3,960</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_NO_DICT</td>
<td align="right">3,960</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">3,120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">3,120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">3,060</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">3,060</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_NONE</td>
<td align="right">2,880</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_WITH_VALUES</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">120</td>
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
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">60</td>
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
