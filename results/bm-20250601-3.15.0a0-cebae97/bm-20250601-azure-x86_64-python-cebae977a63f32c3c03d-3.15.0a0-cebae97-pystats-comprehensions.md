
# Pystats results

- benchmark: comprehensions
- fork: python
- ref: cebae977a63f32c3c03d14c040df3cea55b8f585
- commit hash: cebae97
- commit date: 2025-06-01T00:33:02+03:00

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
<td align="right">188,751,120</td>
<td align="right">12.2%</td>
<td align="right">12.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">138,126,960</td>
<td align="right">8.9%</td>
<td align="right">21.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">124,365,540</td>
<td align="right">8.0%</td>
<td align="right">29.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">108,633,780</td>
<td align="right">7.0%</td>
<td align="right">36.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">103,227,300</td>
<td align="right">6.7%</td>
<td align="right">42.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">79,634,100</td>
<td align="right">5.1%</td>
<td align="right">48.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">53,577,240</td>
<td align="right">3.5%</td>
<td align="right">51.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">53,084,160</td>
<td align="right">3.4%</td>
<td align="right">54.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">40,304,760</td>
<td align="right">2.6%</td>
<td align="right">57.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">37,847,100</td>
<td align="right">2.4%</td>
<td align="right">60.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">36,375,120</td>
<td align="right">2.4%</td>
<td align="right">62.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">32,931,900</td>
<td align="right">2.1%</td>
<td align="right">64.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">32,448,540</td>
<td align="right">2.1%</td>
<td align="right">66.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">31,951,680</td>
<td align="right">2.1%</td>
<td align="right">68.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">30,475,080</td>
<td align="right">2.0%</td>
<td align="right">70.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">29,983,200</td>
<td align="right">1.9%</td>
<td align="right">72.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">28,023,120</td>
<td align="right">1.8%</td>
<td align="right">74.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">26,542,440</td>
<td align="right">1.7%</td>
<td align="right">76.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,613,640</td>
<td align="right">1.5%</td>
<td align="right">77.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">21,135,480</td>
<td align="right">1.4%</td>
<td align="right">78.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">20,646,900</td>
<td align="right">1.3%</td>
<td align="right">80.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">20,643,840</td>
<td align="right">1.3%</td>
<td align="right">81.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">20,155,320</td>
<td align="right">1.3%</td>
<td align="right">82.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">18,199,440</td>
<td align="right">1.2%</td>
<td align="right">84.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">18,186,420</td>
<td align="right">1.2%</td>
<td align="right">85.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">17,694,720</td>
<td align="right">1.1%</td>
<td align="right">86.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">14,746,140</td>
<td align="right">1.0%</td>
<td align="right">87.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">14,376,960</td>
<td align="right">0.9%</td>
<td align="right">88.2%</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">14,254,440</td>
<td align="right">0.9%</td>
<td align="right">89.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">12,289,980</td>
<td align="right">0.8%</td>
<td align="right">89.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">11,919,360</td>
<td align="right">0.8%</td>
<td align="right">90.7%</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,799,660</td>
<td align="right">0.8%</td>
<td align="right">91.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">11,799,380</td>
<td align="right">0.8%</td>
<td align="right">92.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,797,920</td>
<td align="right">0.8%</td>
<td align="right">93.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,305,320</td>
<td align="right">0.7%</td>
<td align="right">93.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">10,815,000</td>
<td align="right">0.7%</td>
<td align="right">94.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">9,338,940</td>
<td align="right">0.6%</td>
<td align="right">95.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">9,338,940</td>
<td align="right">0.6%</td>
<td align="right">95.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,849,560</td>
<td align="right">0.6%</td>
<td align="right">96.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">8,847,900</td>
<td align="right">0.6%</td>
<td align="right">96.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,847,660</td>
<td align="right">0.6%</td>
<td align="right">97.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">8,847,600</td>
<td align="right">0.6%</td>
<td align="right">97.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">8,847,540</td>
<td align="right">0.6%</td>
<td align="right">98.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">8,847,420</td>
<td align="right">0.6%</td>
<td align="right">99.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">99.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,483,200</td>
<td align="right">0.1%</td>
<td align="right">99.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">986,160</td>
<td align="right">0.1%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">983,040</td>
<td align="right">0.1%</td>
<td align="right">99.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">492,960</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">492,960</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">491,820</td>
<td align="right">0.0%</td>
<td align="right">99.9%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">491,700</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">491,520</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">3,240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,880</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">660</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">540</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">300</td>
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
<td align="left">MAKE_CELL</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">180</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
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
<td align="left">NOP</td>
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
<td align="left">FOR_ITER</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
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
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_LIST</td>
<td align="right">117,973,020</td>
<td align="right">7.6%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST_LOAD_FAST</td>
<td align="right">108,633,780</td>
<td align="right">7.0%</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND JUMP_BACKWARD_NO_JIT</td>
<td align="right">79,634,100</td>
<td align="right">5.1%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">76,677,260</td>
<td align="right">5.0%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">53,084,160</td>
<td align="right">3.4%</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">53,084,160</td>
<td align="right">3.4%</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST LIST_APPEND</td>
<td align="right">53,084,160</td>
<td align="right">3.4%</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_BORROW</td>
<td align="right">53,084,160</td>
<td align="right">3.4%</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST_BORROW</td>
<td align="right">26,542,080</td>
<td align="right">1.7%</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_FALSE</td>
<td align="right">23,592,960</td>
<td align="right">1.5%</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RESUME_CHECK</td>
<td align="right">21,135,600</td>
<td align="right">1.4%</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW CALL_PY_EXACT_ARGS</td>
<td align="right">21,135,360</td>
<td align="right">1.4%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">GET_ITER FOR_ITER_LIST</td>
<td align="right">20,153,940</td>
<td align="right">1.3%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST_BORROW</td>
<td align="right">18,680,820</td>
<td align="right">1.2%</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST STORE_FAST</td>
<td align="right">17,695,080</td>
<td align="right">1.1%</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">17,694,760</td>
<td align="right">1.1%</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD JUMP_BACKWARD_NO_JIT</td>
<td align="right">17,694,720</td>
<td align="right">1.1%</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE JUMP_BACKWARD_NO_JIT</td>
<td align="right">17,694,720</td>
<td align="right">1.1%</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE BINARY_OP_SUBSCR_DICT</td>
<td align="right">17,694,720</td>
<td align="right">1.1%</td>
<td align="right">52.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE POP_TOP</td>
<td align="right">14,745,600</td>
<td align="right">1.0%</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE LOAD_FAST_BORROW</td>
<td align="right">14,254,140</td>
<td align="right">0.9%</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL POP_JUMP_IF_TRUE</td>
<td align="right">14,254,140</td>
<td align="right">0.9%</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST TO_BOOL_ALWAYS_TRUE</td>
<td align="right">14,254,080</td>
<td align="right">0.9%</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE TO_BOOL_BOOL</td>
<td align="right">14,254,080</td>
<td align="right">0.9%</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE YIELD_VALUE</td>
<td align="right">14,254,080</td>
<td align="right">0.9%</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE</td>
<td align="right">14,254,080</td>
<td align="right">0.9%</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_BORROW</td>
<td align="right">12,288,060</td>
<td align="right">0.8%</td>
<td align="right">59.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST POP_ITER</td>
<td align="right">11,798,100</td>
<td align="right">0.8%</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST_BORROW</td>
<td align="right">11,796,840</td>
<td align="right">0.8%</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE LOAD_ATTR</td>
<td align="right">11,796,560</td>
<td align="right">0.8%</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE TO_BOOL_BOOL</td>
<td align="right">11,796,480</td>
<td align="right">0.8%</td>
<td align="right">63.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP COPY</td>
<td align="right">11,796,480</td>
<td align="right">0.8%</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">COPY TO_BOOL_BOOL</td>
<td align="right">11,796,480</td>
<td align="right">0.8%</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR COMPARE_OP</td>
<td align="right">11,796,480</td>
<td align="right">0.8%</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,796,480</td>
<td align="right">0.8%</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST TO_BOOL_NONE</td>
<td align="right">11,796,480</td>
<td align="right">0.8%</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE</td>
<td align="right">11,796,480</td>
<td align="right">0.8%</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE POP_JUMP_IF_TRUE</td>
<td align="right">11,796,480</td>
<td align="right">0.8%</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR SWAP</td>
<td align="right">11,306,400</td>
<td align="right">0.7%</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">SWAP GET_ITER</td>
<td align="right">11,306,400</td>
<td align="right">0.7%</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST RETURN_VALUE</td>
<td align="right">10,323,720</td>
<td align="right">0.7%</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST SWAP</td>
<td align="right">10,323,360</td>
<td align="right">0.7%</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">SWAP BUILD_LIST</td>
<td align="right">10,323,360</td>
<td align="right">0.7%</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">POP_ITER LOAD_CONST</td>
<td align="right">9,339,060</td>
<td align="right">0.6%</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_CONST</td>
<td align="right">9,339,060</td>
<td align="right">0.6%</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_FAST</td>
<td align="right">9,339,060</td>
<td align="right">0.6%</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,338,920</td>
<td align="right">0.6%</td>
<td align="right">74.2%</td>
</tr>
<tr>
<td align="left">POP_ITER SWAP</td>
<td align="right">9,338,880</td>
<td align="right">0.6%</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">SWAP STORE_FAST</td>
<td align="right">9,338,880</td>
<td align="right">0.6%</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,855,220</td>
<td align="right">0.6%</td>
<td align="right">76.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LOAD_CONST</td>
<td align="right">8,848,920</td>
<td align="right">0.6%</td>
<td align="right">76.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST MAKE_FUNCTION</td>
<td align="right">8,847,600</td>
<td align="right">0.6%</td>
<td align="right">77.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST GET_ITER</td>
<td align="right">8,847,600</td>
<td align="right">0.6%</td>
<td align="right">77.7%</td>
</tr>
<tr>
<td align="left">POP_TOP RESUME_CHECK</td>
<td align="right">8,847,540</td>
<td align="right">0.6%</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN POP_TOP</td>
<td align="right">8,847,540</td>
<td align="right">0.6%</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE LOAD_FAST_BORROW</td>
<td align="right">8,847,420</td>
<td align="right">0.6%</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,847,400</td>
<td align="right">0.6%</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL FOR_ITER_GEN</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR PUSH_NULL</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP BINARY_OP_SUBSCR_DICT</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">82.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE LIST_APPEND</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">83.4%</td>
</tr>
<tr>
<td align="left">COPY LOAD_COMMON_CONSTANT</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">IS_OP POP_JUMP_IF_FALSE</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT IS_OP</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">85.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST BINARY_OP</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW LIST_APPEND</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW MAP_ADD</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">86.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST MAP_ADD</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">87.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT LIST_APPEND</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT CALL_LEN</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">89.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT CALL_PY_EXACT_ARGS</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS RETURN_GENERATOR</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE BUILD_TUPLE</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE LOAD_FAST_AND_CLEAR</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">93.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN COPY</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">94.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">0.6%</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE POP_ITER</td>
<td align="right">8,355,840</td>
<td align="right">0.5%</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">POP_TOP JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,898,660</td>
<td align="right">0.4%</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN RESUME_CHECK</td>
<td align="right">5,898,600</td>
<td align="right">0.4%</td>
<td align="right">96.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT FOR_ITER_GEN</td>
<td align="right">5,898,600</td>
<td align="right">0.4%</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK POP_TOP</td>
<td align="right">5,898,600</td>
<td align="right">0.4%</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">POP_TOP LOAD_FAST_BORROW</td>
<td align="right">5,898,240</td>
<td align="right">0.4%</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE RETURN_VALUE</td>
<td align="right">5,898,240</td>
<td align="right">0.4%</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE</td>
<td align="right">5,898,240</td>
<td align="right">0.4%</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,440,640</td>
<td align="right">0.2%</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST STORE_FAST</td>
<td align="right">2,459,040</td>
<td align="right">0.2%</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST LOAD_FAST_AND_CLEAR</td>
<td align="right">2,457,600</td>
<td align="right">0.2%</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">POP_ITER STORE_FAST</td>
<td align="right">1,967,520</td>
<td align="right">0.1%</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST LOAD_FAST</td>
<td align="right">1,474,680</td>
<td align="right">0.1%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP SWAP</td>
<td align="right">983,040</td>
<td align="right">0.1%</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">983,040</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">SWAP BUILD_MAP</td>
<td align="right">983,040</td>
<td align="right">0.1%</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">500,160</td>
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
<td align="left">SWAP</td>
<td align="right">11,306,400</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,847,600</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
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
<td align="right">20,153,940</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">120</td>
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
<td align="left">MAKE_CELL</td>
<td align="right">180</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">60</td>
<td align="right">25.0%</td>
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
<td align="right">491,700</td>
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
<td align="right">491,700</td>
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
<td align="right">492,960</td>
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
<td align="right">492,960</td>
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
<td align="right">180</td>
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
<td align="right">8,847,600</td>
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
<td align="right">8,847,360</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">240</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">60</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">11,798,100</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,355,840</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">491,700</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">9,339,060</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">9,338,880</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,967,520</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">1,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">60</td>
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
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">14,745,600</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">8,847,540</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,898,600</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">491,700</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">491,520</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">9,339,060</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">8,847,540</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,898,660</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">5,898,240</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">491,580</td>
<td align="right">1.6%</td>
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
<td align="left">RETURN_GENERATOR</td>
<td align="right">8,847,360</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="left">FOR_ITER_GEN</td>
<td align="right">8,847,360</td>
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
<td align="left">LOAD_FAST_BORROW</td>
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
<td align="right">8,847,360</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">8,847,360</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">180</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">10,323,720</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,898,240</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,898,240</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">492,960</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,796,480</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,847,360</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">492,960</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">491,760</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">491,700</td>
<td align="right">2.2%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
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
<td align="left">LOAD_CONST</td>
<td align="right">8,847,360</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
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
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">8,847,360</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">10,323,360</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">491,520</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
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
<td align="right">10,323,360</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">491,520</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
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
<td align="left">SWAP</td>
<td align="right">983,040</td>
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
<td align="right">983,040</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,440</td>
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
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">1,440</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,847,360</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
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
<td align="left">LIST_APPEND</td>
<td align="right">8,847,360</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
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
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">40</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">40</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">40</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
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
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">100</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">100</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">40</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">20</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20</td>
<td align="right">6.2%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">11,796,480</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
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
<td align="left">COPY</td>
<td align="right">11,796,480</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">20</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">11,796,480</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,847,360</td>
<td align="right">42.9%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">11,796,480</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">8,847,360</td>
<td align="right">42.9%</td>
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
<td align="left">RETURN_GENERATOR</td>
<td align="right">180</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">60</td>
<td align="right">25.0%</td>
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
<td align="left">POP_ITER</td>
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
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">8,847,360</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
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
<td align="right">8,847,360</td>
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
<td align="left">LOAD_FAST_BORROW</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">53,084,160</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,847,360</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">8,847,360</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,860</td>
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
<td align="right">79,634,100</td>
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
<td align="right">11,796,560</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">11,796,480</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
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


</details>

### LOAD_COMMON_CONSTANT

<details>
<summary> Successors and predecessors for LOAD_COMMON_CONSTANT </summary>

<table>
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
<td align="right">8,847,360</td>
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
<td align="left">IS_OP</td>
<td align="right">8,847,360</td>
<td align="right">100.0%</td>
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
<td align="left">POP_ITER</td>
<td align="right">9,339,060</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,339,060</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,848,920</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">492,960</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,560</td>
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
<td align="right">10,323,720</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">8,847,600</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,847,360</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
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
<td align="right">360</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">180</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">60</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
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
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">540</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">60</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">60</td>
<td align="right">9.1%</td>
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
<td align="right">9,339,060</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,474,680</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">491,580</td>
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
<td align="left">GET_ITER</td>
<td align="right">8,847,600</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,457,600</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,847,360</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,457,600</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">491,520</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">1,440</td>
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
<td align="right">11,306,400</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">491,520</td>
<td align="right">4.2%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">53,084,160</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">26,542,080</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">18,680,820</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">14,254,140</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,288,060</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">76,677,260</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">53,084,160</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">21,135,360</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,338,920</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,848,920</td>
<td align="right">4.7%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,847,360</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,847,360</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">492,960</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">7,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,880</td>
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
<td align="right">17,694,760</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">500,160</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">2,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">60</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
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
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">60</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
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
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">120</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">60</td>
<td align="right">33.3%</td>
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
<td align="left">CALL_LEN</td>
<td align="right">491,580</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">491,520</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">2,940</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
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
<td align="right">491,560</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">491,520</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,880</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="left">CACHE</td>
<td align="right">180</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">240</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">8,847,360</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">17,694,720</td>
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
<td align="right">23,592,960</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">8,847,360</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">491,520</td>
<td align="right">1.5%</td>
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
<td align="left">POP_TOP</td>
<td align="right">14,745,600</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,847,420</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,898,240</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">3,440,640</td>
<td align="right">10.4%</td>
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
<td align="right">14,254,140</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">14,254,080</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">11,796,480</td>
<td align="right">29.3%</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">17,694,720</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">14,254,140</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">8,355,840</td>
<td align="right">20.7%</td>
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
<td align="right">180</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">25.0%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">17,695,080</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">9,338,880</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,459,040</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,967,520</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">491,760</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">18,680,820</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">8,847,360</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">2,459,040</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,474,680</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">491,820</td>
<td align="right">1.5%</td>
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
<td align="right">108,633,780</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">53,084,160</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">14,254,080</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">11,796,480</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">11,796,480</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,855,220</td>
<td align="right">8.2%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
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
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">11,306,400</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">10,323,360</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">9,338,880</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">983,040</td>
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
<td align="left">GET_ITER</td>
<td align="right">11,306,400</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">10,323,360</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">9,338,880</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">983,040</td>
<td align="right">3.1%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">14,254,080</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">14,254,080</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">360</td>
<td align="right">0.0%</td>
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
<td align="right">2,880</td>
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
<td align="left">BUILD_SLICE</td>
<td align="right">1,440</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,440</td>
<td align="right">50.0%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">17,694,720</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,847,360</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
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
<td align="right">8,847,360</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">8,847,360</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,847,360</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">360</td>
<td align="right">0.0%</td>
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
<td align="right">1,440</td>
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
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,440</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">491,520</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,440</td>
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
<td align="right">492,960</td>
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
<td align="left">CALL</td>
<td align="right">40</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">40</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
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
<td align="left">GET_ITER</td>
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
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">8,847,360</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">491,520</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">491,580</td>
<td align="right">5.3%</td>
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
<td align="left">RETURN_VALUE</td>
<td align="right">1,440</td>
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
<td align="right">1,440</td>
<td align="right">100.0%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">53,084,160</td>
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
<td align="left">LIST_APPEND</td>
<td align="right">53,084,160</td>
<td align="right">100.0%</td>
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
<td align="right">491,520</td>
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
<td align="right">491,520</td>
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
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">100</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
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
<td align="left">POP_TOP</td>
<td align="right">60</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">60</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">60</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">60</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">60</td>
<td align="right">20.0%</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">21,135,360</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">8,847,360</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">21,135,600</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">8,847,360</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">240</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,847,360</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">491,560</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">491,520</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">60</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">8,847,360</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,898,600</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
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
<td align="left">POP_TOP</td>
<td align="right">8,847,540</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,898,600</td>
<td align="right">40.0%</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">117,973,020</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">20,153,940</td>
<td align="right">14.6%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Successors</th>
<th align="right">Count</th>
<th align="right">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">108,633,780</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,695,080</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">11,798,100</td>
<td align="right">8.5%</td>
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
<td align="right">491,700</td>
<td align="right">100.0%</td>
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
<td align="left">STORE_FAST</td>
<td align="right">491,700</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">120</td>
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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">2,160</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,080</td>
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
<td align="right">2,160</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,080</td>
<td align="right">33.3%</td>
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
<td align="right">79,634,100</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">17,694,720</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">17,694,720</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,898,660</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,440,640</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">117,973,020</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">5,898,600</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">491,700</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">540</td>
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
<td align="right">360</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">180</td>
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
<td align="right">76,677,260</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">17,694,760</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">8,855,220</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">26,542,080</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">17,694,720</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">14,254,080</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">11,796,480</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">8,847,360</td>
<td align="right">8.6%</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">53,084,160</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">492,960</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">53,084,160</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">491,520</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">40</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">11,796,480</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">9,338,920</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">12,288,060</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60</td>
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
<td align="right">160</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
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
<td align="left">PUSH_NULL</td>
<td align="right">240</td>
<td align="right">100.0%</td>
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
<td align="right">8,847,400</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">8,847,360</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">491,560</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
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
<td align="left">COPY</td>
<td align="right">8,847,360</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">8,847,360</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">491,640</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">11,796,480</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">491,820</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">11,796,560</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">491,520</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">160</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">21,135,600</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,847,540</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">5,898,600</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">492,960</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
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
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">11,796,840</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,339,060</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">8,847,400</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,898,600</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">492,960</td>
<td align="right">1.4%</td>
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
<td align="right">983,040</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">500,160</td>
<td align="right">33.7%</td>
</tr>
</tbody>
</table>

<table>
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
<td align="right">492,960</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">491,520</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">491,520</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">7,200</td>
<td align="right">0.5%</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">14,254,080</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">122,880</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">14,254,080</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">122,880</td>
<td align="right">0.9%</td>
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
<td align="left">YIELD_VALUE</td>
<td align="right">14,254,080</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">11,796,480</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,796,480</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
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
<td align="right">23,592,960</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">14,254,140</td>
<td align="right">37.7%</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">11,796,480</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">122,880</td>
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
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">11,796,480</td>
<td align="right">99.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">122,880</td>
<td align="right">1.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,847,360</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">26,546,880</td>
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
<td align="right">40</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,160</td>
<td align="right">98.2%</td>
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
<td align="right">2,160</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">93,392,460</td>
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
<td align="right">320</td>
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
<td align="right">11,796,480</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,338,940</td>
<td align="right">44.2%</td>
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
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,880</td>
<td align="right">99.3%</td>
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
<td align="left">baseobject</td>
<td align="right">2,880</td>
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
<td align="right">153,368,160</td>
<td align="right">100.0%</td>
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
<td align="right">20,153,940</td>
<td align="right">20,153,940 / 0 !!</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,080</td>
<td align="right">1,080 / 0 !!</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">300</td>
<td align="right">300 / 0 !!</td>
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
<td align="right">11,796,540</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">177,940,260</td>
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
<td align="right">540</td>
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
<td align="right">220</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,900</td>
<td align="right">92.9%</td>
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
<td align="right">2,880</td>
<td align="right">99.3%</td>
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
<td align="right">30,476,400</td>
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
<td align="right">1,483,200</td>
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
<td align="right">43,253,820</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">13,025,280</td>
<td align="right">23.1%</td>
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
<td align="right">245,780</td>
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
<td align="right">777,168,240</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">52,604,600</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">704,405,520</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">13,025,820</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">11,796,540</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">11,796,480</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,847,360</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
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
<td align="left">GET_ITER</td>
<td align="right">0</td>
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
<td align="right">6,512,640</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">6,512,640</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">540</td>
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
<td align="left">END_FOR</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
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
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">45,222,420</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">240</td>
<td align="right">0.0%</td>
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
<td align="right">240</td>
<td align="right">0.0%</td>
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
<td align="right">180</td>
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
<td align="right">30,969,480</td>
<td align="right">68.5%</td>
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
<td align="right">21,125,360</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">21,125,260</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">21,138,940</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">20,155,900</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">983,040</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">31,462,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">492,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">368,178,240</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">401,098,540</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">114,050,244</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">120,443,364</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">49,166,100</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">17,203,560</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">143,531,668</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">176,968,368</td>
<td align="right">24.7%</td>
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
<td align="right">23,599,978</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">42</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">42</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,336</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">4</td>
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
<td align="right">20</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-01
