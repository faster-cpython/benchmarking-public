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
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">580,220</td>
<td align="right">390,460</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">580,300</td>
<td align="right">390,540</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">580,300</td>
<td align="right">390,540</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">580,300</td>
<td align="right">390,540</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">580,360</td>
<td align="right">390,600</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">5,868,260</td>
<td align="right">4,237,020</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,443,460</td>
<td align="right">1,144,340</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">921,480</td>
<td align="right">731,720</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">418,620</td>
<td align="right">346,980</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">1,426,060</td>
<td align="right">1,189,700</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">4,707,660</td>
<td align="right">4,120,180</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">369,720</td>
<td align="right">328,020</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">764,560</td>
<td align="right">692,920</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,117,320</td>
<td align="right">5,569,900</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">4,692,580</td>
<td align="right">4,311,540</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">4,274,960</td>
<td align="right">3,950,080</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">4,033,880</td>
<td align="right">3,734,760</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,630,200</td>
<td align="right">2,446,360</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,330,200</td>
<td align="right">1,238,280</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">11,673,400</td>
<td align="right">10,907,760</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">11,580,420</td>
<td align="right">10,830,580</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,494,460</td>
<td align="right">1,402,540</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,220,600</td>
<td align="right">3,036,760</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">24,772,840</td>
<td align="right">23,360,820</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,746,360</td>
<td align="right">10,170,480</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">9,261,780</td>
<td align="right">8,824,600</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">15,744,660</td>
<td align="right">15,061,980</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">27,247,600</td>
<td align="right">26,102,140</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">99,434,180</td>
<td align="right">96,251,380</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">20,487,500</td>
<td align="right">19,855,200</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">9,517,540</td>
<td align="right">9,256,580</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">20,183,140</td>
<td align="right">19,705,000</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">53,361,320</td>
<td align="right">52,418,260</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">55,789,620</td>
<td align="right">55,020,180</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">46,421,160</td>
<td align="right">45,791,060</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">47,142,760</td>
<td align="right">46,566,880</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">28,823,800</td>
<td align="right">28,482,220</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">4,083,740</td>
<td align="right">4,042,780</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">28,550,500</td>
<td align="right">28,304,360</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">7,053,320</td>
<td align="right">7,013,660</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">29,760,720</td>
<td align="right">29,689,080</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">35,674,160</td>
<td align="right">35,592,260</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">35,068,840</td>
<td align="right">35,068,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">28,723,960</td>
<td align="right">28,723,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">27,287,340</td>
<td align="right">27,287,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">7,015,640</td>
<td align="right">7,015,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">6,933,820</td>
<td align="right">6,933,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,243,900</td>
<td align="right">6,243,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,382,080</td>
<td align="right">3,382,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">763,260</td>
<td align="right">763,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">708,200</td>
<td align="right">708,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">506,280</td>
<td align="right">506,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">482,000</td>
<td align="right">482,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">338,820</td>
<td align="right">338,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">302,860</td>
<td align="right">302,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">295,840</td>
<td align="right">295,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">236,020</td>
<td align="right">236,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">236,020</td>
<td align="right">236,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">205,500</td>
<td align="right">205,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">190,440</td>
<td align="right">190,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">188,480</td>
<td align="right">188,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">188,120</td>
<td align="right">188,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">156,480</td>
<td align="right">156,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">154,540</td>
<td align="right">154,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">124,920</td>
<td align="right">124,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">124,840</td>
<td align="right">124,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">109,420</td>
<td align="right">109,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">98,880</td>
<td align="right">98,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">36,440</td>
<td align="right">36,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">36,400</td>
<td align="right">36,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">29,800</td>
<td align="right">29,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">27,720</td>
<td align="right">27,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">23,040</td>
<td align="right">23,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">18,200</td>
<td align="right">18,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">11,480</td>
<td align="right">11,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">7,580</td>
<td align="right">7,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">6,100</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,180</td>
<td align="right">5,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,800</td>
<td align="right">4,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4,240</td>
<td align="right">4,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,640</td>
<td align="right">1,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,180</td>
<td align="right">1,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,140</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,000</td>
<td align="right">1,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">940</td>
<td align="right">940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">940</td>
<td align="right">940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">800</td>
<td align="right">800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 opcode pairs </summary>


Pairs of specialized operations that deoptimize and are then followed by
the corresponding unspecialized instruction are not counted as pairs.

Not included in comparative output.


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each Tier 1 opcode. </summary>


This does not include the unspecialized instructions that occur after a
specialized instruction deoptimizes.

Not included in comparative output.


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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">27,040</td>
<td align="right">0.0%</td>
<td align="right">27,040</td>
<td align="right">0.0%</td>
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
<td align="right">170,760,380</td>
<td align="right">100.0%</td>
<td align="right">170,760,380</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">2,080</td>
<td align="right">75.4%</td>
<td align="right">2,080</td>
<td align="right">75.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">680</td>
<td align="right">24.6%</td>
<td align="right">680</td>
<td align="right">24.6%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">multiply different types</td>
<td align="right">380</td>
<td align="right">55.9%</td>
<td align="right">380</td>
<td align="right">55.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">300</td>
<td align="right">44.1%</td>
<td align="right">300</td>
<td align="right">44.1%</td>
<td align="right">0.0%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">23,040</td>
<td align="right">100.0%</td>
<td align="right">23,040</td>
<td align="right">100.0%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">2,400</td>
<td align="right">0.0%</td>
<td align="right">2,400</td>
<td align="right">0.0%</td>
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
<td align="right">76,123,960</td>
<td align="right">100.0%</td>
<td align="right">76,123,960</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">2,400</td>
<td align="right">100.0%</td>
<td align="right">2,400</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">50.0%</td>
<td align="right">140</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">780</td>
<td align="right">0.0%</td>
<td align="right">780</td>
<td align="right">0.0%</td>
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
<td align="right">53,531,760</td>
<td align="right">100.0%</td>
<td align="right">53,531,760</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">780</td>
<td align="right">100.0%</td>
<td align="right">780</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">28,542,560</td>
<td align="right">99.6%</td>
<td align="right">28,296,480</td>
<td align="right">99.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">109,420</td>
<td align="right">0.4%</td>
<td align="right">109,420</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">7,920</td>
<td align="right">99.7%</td>
<td align="right">7,860</td>
<td align="right">99.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">list</td>
<td align="right">7,920</td>
<td align="right">100.0%</td>
<td align="right">7,860</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">39,606,800</td>
<td align="right">99.7%</td>
<td align="right">39,225,780</td>
<td align="right">99.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">101,240</td>
<td align="right">0.3%</td>
<td align="right">101,240</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">2,660</td>
<td align="right">99.3%</td>
<td align="right">2,660</td>
<td align="right">99.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">0.7%</td>
<td align="right">20</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dict values</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">list</td>
<td align="right">3,569,340</td>
<td align="right">3,569,340 / 0 !!</td>
<td align="right">3,569,340</td>
<td align="right">3,569,340 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,988,220</td>
<td align="right">1,988,220 / 0 !!</td>
<td align="right">1,988,220</td>
<td align="right">1,988,220 / 0 !!</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">81,444,980</td>
<td align="right">100.0%</td>
<td align="right">80,869,100</td>
<td align="right">100.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,620</td>
<td align="right">0.0%</td>
<td align="right">2,620</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">2,540</td>
<td align="right">99.2%</td>
<td align="right">2,540</td>
<td align="right">99.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">0.8%</td>
<td align="right">20</td>
<td align="right">0.8%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">19,522,060</td>
<td align="right">100.0%</td>
<td align="right">18,992,620</td>
<td align="right">100.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,120</td>
<td align="right">0.0%</td>
<td align="right">2,120</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">2,120</td>
<td align="right">100.0%</td>
<td align="right">2,120</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">280</td>
<td align="right">0.0%</td>
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
<td align="right">708,200</td>
<td align="right">99.9%</td>
<td align="right">708,200</td>
<td align="right">99.9%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">280</td>
<td align="right">100.0%</td>
<td align="right">280</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">200</td>
<td align="right">0.0%</td>
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
<td align="right">3,494,200</td>
<td align="right">100.0%</td>
<td align="right">3,494,200</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">200</td>
<td align="right">100.0%</td>
<td align="right">200</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">9,261,780</td>
<td align="right">100.0%</td>
<td align="right">8,824,600</td>
<td align="right">100.0%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">520</td>
<td align="right">0.0%</td>
<td align="right">520</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">460</td>
<td align="right">95.8%</td>
<td align="right">460</td>
<td align="right">95.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">4.2%</td>
<td align="right">20</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
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
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
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
<td align="right">124,840</td>
<td align="right">99.9%</td>
<td align="right">124,840</td>
<td align="right">99.9%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">276,919,580</td>
<td align="right">36.2%</td>
<td align="right">269,127,720</td>
<td align="right">36.2%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">453,883,920</td>
<td align="right">59.4%</td>
<td align="right">442,057,960</td>
<td align="right">59.4%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">33,315,740</td>
<td align="right">4.4%</td>
<td align="right">32,688,560</td>
<td align="right">4.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">101,240</td>
<td align="right">0.0%</td>
<td align="right">101,280</td>
<td align="right">0.0%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">28,542,560</td>
<td align="right">99.8%</td>
<td align="right">28,296,480</td>
<td align="right">99.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">27,040</td>
<td align="right">0.1%</td>
<td align="right">27,040</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">23,040</td>
<td align="right">0.1%</td>
<td align="right">23,040</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,620</td>
<td align="right">0.0%</td>
<td align="right">2,620</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,400</td>
<td align="right">0.0%</td>
<td align="right">2,400</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,120</td>
<td align="right">0.0%</td>
<td align="right">2,120</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">780</td>
<td align="right">0.0%</td>
<td align="right">780</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">520</td>
<td align="right">0.0%</td>
<td align="right">520</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">280</td>
<td align="right">0.0%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">50,880</td>
<td align="right">50.3%</td>
<td align="right">50,880</td>
<td align="right">50.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">50,360</td>
<td align="right">49.7%</td>
<td align="right">50,360</td>
<td align="right">49.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">28,724,020</td>
<td align="right">39.7%</td>
<td align="right">28,724,020</td>
<td align="right">39.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">43,590,740</td>
<td align="right">60.3%</td>
<td align="right">43,590,740</td>
<td align="right">60.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">28,724,020</td>
<td align="right">39.7%</td>
<td align="right">28,724,020</td>
<td align="right">39.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">28,723,560</td>
<td align="right">39.7%</td>
<td align="right">28,723,560</td>
<td align="right">39.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">43,827,220</td>
<td align="right">60.6%</td>
<td align="right">43,827,220</td>
<td align="right">60.6%</td>
<td align="right">0.0%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,480</td>
<td align="right">0.0%</td>
<td align="right">1,540</td>
<td align="right">0.0%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">992</td>
<td align="right"></td>
<td align="right">959</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">786</td>
<td align="right"></td>
<td align="right">762</td>
<td align="right"></td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">178,079,060</td>
<td align="right">36.4%</td>
<td align="right">182,136,828</td>
<td align="right">37.1%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">134,455,051</td>
<td align="right">28.6%</td>
<td align="right">137,433,135</td>
<td align="right">29.1%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">4,567,840</td>
<td align="right">1.0%</td>
<td align="right">4,475,180</td>
<td align="right">0.9%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">148,116,640</td>
<td align="right">30.3%</td>
<td align="right">146,223,160</td>
<td align="right">29.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">61,265,960</td>
<td align="right">12.5%</td>
<td align="right">60,790,760</td>
<td align="right">12.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">183</td>
<td align="right"></td>
<td align="right">184</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">101,379,612</td>
<td align="right">20.7%</td>
<td align="right">101,855,320</td>
<td align="right">20.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">204,307,280</td>
<td align="right">43.5%</td>
<td align="right">203,493,280</td>
<td align="right">43.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">56,288</td>
<td align="right"></td>
<td align="right">56,381</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">126,793,363</td>
<td align="right">27.0%</td>
<td align="right">126,886,415</td>
<td align="right">26.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,852,560</td>
<td align="right">44.7%</td>
<td align="right">6,852,680</td>
<td align="right">44.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">94,757</td>
<td align="right"></td>
<td align="right">94,756</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,850,920</td>
<td align="right">44.7%</td>
<td align="right">6,850,940</td>
<td align="right">44.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">7,179,199</td>
<td align="right"></td>
<td align="right">7,179,202</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,491,020</td>
<td align="right">55.3%</td>
<td align="right">8,491,020</td>
<td align="right">55.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,492,660</td>
<td align="right"></td>
<td align="right">8,492,660</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">236,160</td>
<td align="right"></td>
<td align="right">236,160</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (str subclass)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<th align="right">Base Collections</th>
<th align="right">Base Objects collected</th>
<th align="right">Base Object visits</th>
<th align="right">Base Reachable from roots</th>
<th align="right">Base Not reachable from roots</th>
<th align="right">Head Collections</th>
<th align="right">Head Objects collected</th>
<th align="right">Head Object visits</th>
<th align="right">Head Reachable from roots</th>
<th align="right">Head Not reachable from roots</th>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">20</td>
<td align="right">5,680</td>
<td align="right">306,200</td>
<td align="right">7,540</td>
<td align="right">24,780</td>
<td align="right">20</td>
<td align="right">5,680</td>
<td align="right">306,200</td>
<td align="right">7,540</td>
<td align="right">24,780</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">900</td>
<td align="right">10.0%</td>
<td align="right">1,000</td>
<td align="right">10.9%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,820,571,180</td>
<td align="right">5,565.3%</td>
<td align="right">1,867,901,140</td>
<td align="right">5,673.0%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">9,040</td>
<td align="right"></td>
<td align="right">9,180</td>
<td align="right"></td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">1,440</td>
<td align="right">15.9%</td>
<td align="right">1,460</td>
<td align="right">15.9%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">32,712,960</td>
<td align="right"></td>
<td align="right">32,926,220</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,700</td>
<td align="right">74.1%</td>
<td align="right">6,720</td>
<td align="right">73.2%</td>
<td align="right">0.3%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">60</td>
<td align="right">0.7%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">860</td>
<td align="right">95.6%</td>
<td align="right">980</td>
<td align="right">98.0%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">900</td>
<td align="right"></td>
<td align="right">1,000</td>
<td align="right"></td>
<td align="right">11.1%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<th align="right">Base Size (bytes)</th>
<th align="right">Base Ratio</th>
<th align="right">Head Size (bytes)</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">1,709,380</td>
<td align="right">14.6%</td>
<td align="right">2,090,640</td>
<td align="right">15.3%</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">11,714,560</td>
<td align="right"></td>
<td align="right">13,680,640</td>
<td align="right"></td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">9,769,500</td>
<td align="right">83.4%</td>
<td align="right">11,317,200</td>
<td align="right">82.7%</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">235,680</td>
<td align="right">2.0%</td>
<td align="right">272,800</td>
<td align="right">2.0%</td>
<td align="right">15.8%</td>
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
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### JIT trace total memory histogram

<details>
<summary> JIT trace total memory histogram </summary>

<table>
<thead>
<tr>
<th align="left">Size (bytes)</th>
<th align="left">Base Count</th>
<th align="right">Base Ratio</th>
<th align="left">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 4,096</td>
<td align="left">180</td>
<td align="right">20.9%</td>
<td align="left">200</td>
<td align="right">20.4%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">180</td>
<td align="right">20.9%</td>
<td align="left">200</td>
<td align="right">20.4%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">340</td>
<td align="right">39.5%</td>
<td align="left">380</td>
<td align="right">38.8%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">120</td>
<td align="right">14.0%</td>
<td align="left">160</td>
<td align="right">16.3%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">40</td>
<td align="right">4.7%</td>
<td align="left">40</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### Trace length histogram

<details>
<summary> trace length histogram </summary>

<table>
<thead>
<tr>
<th align="left">Range</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 8</td>
<td align="right">140</td>
<td align="right">15.6%</td>
<td align="right">140</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">40</td>
<td align="right">4.4%</td>
<td align="right">60</td>
<td align="right">6.0%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">120</td>
<td align="right">13.3%</td>
<td align="right">160</td>
<td align="right">16.0%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">420</td>
<td align="right">46.7%</td>
<td align="right">400</td>
<td align="right">40.0%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">160</td>
<td align="right">17.8%</td>
<td align="right">220</td>
<td align="right">22.0%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">2.2%</td>
<td align="right">20</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 4</td>
<td align="right">100</td>
<td align="right">11.1%</td>
<td align="right">140</td>
<td align="right">14.0%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">80</td>
<td align="right">8.9%</td>
<td align="right">60</td>
<td align="right">6.0%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">120</td>
<td align="right">13.3%</td>
<td align="right">140</td>
<td align="right">14.0%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">300</td>
<td align="right">33.3%</td>
<td align="right">320</td>
<td align="right">32.0%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">20.0%</td>
<td align="right">240</td>
<td align="right">24.0%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">80</td>
<td align="right">8.9%</td>
<td align="right">80</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>


</details>

### Uop execution stats

<details>
<summary> uop execution stats </summary>

<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">109,440</td>
<td align="right">181,080</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">650,700</td>
<td align="right">949,820</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">864,980</td>
<td align="right">1,246,020</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">792,240</td>
<td align="right">1,081,060</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">125,440</td>
<td align="right">166,400</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">1,160,740</td>
<td align="right">1,485,620</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">926,000</td>
<td align="right">1,146,400</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">926,000</td>
<td align="right">1,146,400</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">463,000</td>
<td align="right">573,200</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">855,920</td>
<td align="right">1,045,680</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">855,920</td>
<td align="right">1,045,680</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">855,920</td>
<td align="right">1,045,680</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">855,920</td>
<td align="right">1,045,680</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">855,920</td>
<td align="right">1,045,680</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">855,920</td>
<td align="right">1,045,680</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">855,920</td>
<td align="right">1,045,680</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">855,920</td>
<td align="right">1,045,680</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">860,400</td>
<td align="right">1,050,160</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,553,560</td>
<td align="right">1,799,640</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">3,394,340</td>
<td align="right">3,712,060</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">994,420</td>
<td align="right">1,075,040</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,874,740</td>
<td align="right">2,015,220</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">13,618,040</td>
<td align="right">14,599,060</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">5,462,660</td>
<td align="right">5,827,320</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">6,985,780</td>
<td align="right">7,386,920</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right">3,963,080</td>
<td align="right">4,146,920</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,981,540</td>
<td align="right">2,073,460</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,981,540</td>
<td align="right">2,073,460</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">1,981,540</td>
<td align="right">2,073,460</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right">1,981,540</td>
<td align="right">2,073,460</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">868,980</td>
<td align="right">908,640</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">7,173,100</td>
<td align="right">7,498,340</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">37,252,600</td>
<td align="right">38,758,380</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">9,020,480</td>
<td align="right">9,362,060</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">23,390,320</td>
<td align="right">24,244,280</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">30,993,440</td>
<td align="right">32,105,420</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,289,220</td>
<td align="right">1,330,920</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">44,861,580</td>
<td align="right">46,273,600</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">44,861,580</td>
<td align="right">46,273,600</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">7,830,900</td>
<td align="right">8,076,980</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">24,590,900</td>
<td align="right">25,356,540</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">24,590,900</td>
<td align="right">25,356,540</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">24,590,900</td>
<td align="right">25,356,540</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">27,453,660</td>
<td align="right">28,255,200</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">253,010,400</td>
<td align="right">260,268,780</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">24,920,700</td>
<td align="right">25,622,580</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">27,212,980</td>
<td align="right">27,962,820</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">283,388,660</td>
<td align="right">291,131,880</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">23,718,000</td>
<td align="right">24,293,880</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">23,718,000</td>
<td align="right">24,293,880</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">23,718,000</td>
<td align="right">24,293,880</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">23,734,980</td>
<td align="right">24,310,860</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">23,734,980</td>
<td align="right">24,310,860</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">47,696,100</td>
<td align="right">48,841,560</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">23,279,660</td>
<td align="right">23,825,300</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">49,680,280</td>
<td align="right">50,825,740</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">35,448,020</td>
<td align="right">36,242,020</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">24,408,520</td>
<td align="right">24,951,440</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">23,644,080</td>
<td align="right">24,122,220</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">3,027,620</td>
<td align="right">3,086,760</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">33,007,820</td>
<td align="right">33,640,120</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">26,206,540</td>
<td align="right">26,695,020</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">3,802,160</td>
<td align="right">3,871,000</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">34,277,660</td>
<td align="right">34,876,920</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">35,689,340</td>
<td align="right">36,249,840</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">22,181,420</td>
<td align="right">22,511,220</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">6,137,080</td>
<td align="right">6,219,000</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">26,099,280</td>
<td align="right">26,439,800</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">28,132,640</td>
<td align="right">28,472,720</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">25,149,900</td>
<td align="right">25,449,760</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,903,340</td>
<td align="right">6,985,240</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">32,401,220</td>
<td align="right">32,785,460</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,932,220</td>
<td align="right">7,014,120</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">26,857,980</td>
<td align="right">27,157,100</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">26,857,980</td>
<td align="right">27,157,100</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">25,689,380</td>
<td align="right">25,950,340</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">21,417,420</td>
<td align="right">21,596,460</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">16,133,460</td>
<td align="right">16,243,660</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">32,712,960</td>
<td align="right">32,926,220</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">32,712,960</td>
<td align="right">32,926,220</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">46,546,760</td>
<td align="right">46,760,020</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">13,833,800</td>
<td align="right">13,833,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">1,874,740</td>
<td align="right">1,874,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">1,874,740</td>
<td align="right">1,874,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,862,240</td>
<td align="right">1,862,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">1,857,760</td>
<td align="right">1,857,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">343,380</td>
<td align="right">343,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">109,440</td>
<td align="right">109,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">109,440</td>
<td align="right">109,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">109,440</td>
<td align="right">109,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">24,340</td>
<td align="right">24,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">24,340</td>
<td align="right">24,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">16,980</td>
<td align="right">16,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">16,980</td>
<td align="right">16,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">16,980</td>
<td align="right">16,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">16,980</td>
<td align="right">16,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">16,980</td>
<td align="right">16,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">4,480</td>
<td align="right">4,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">71,640</td>
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

Not included in comparative output.


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
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Number of data files</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-29
