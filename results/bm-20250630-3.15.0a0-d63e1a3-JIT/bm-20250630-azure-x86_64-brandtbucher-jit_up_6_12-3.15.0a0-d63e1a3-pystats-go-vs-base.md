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
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">2,977,660</td>
<td align="right">162,280</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">172,900</td>
<td align="right">14,760</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">104,940</td>
<td align="right">27,800</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">48,580</td>
<td align="right">14,500</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">38,900</td>
<td align="right">11,940</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">248,540</td>
<td align="right">76,520</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">242,680</td>
<td align="right">86,860</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">635,400</td>
<td align="right">341,620</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">492,420</td>
<td align="right">266,460</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">183,420</td>
<td align="right">101,000</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">664,700</td>
<td align="right">370,920</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">665,180</td>
<td align="right">371,400</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,076,900</td>
<td align="right">3,526,760</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">627,740</td>
<td align="right">872,180</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">296,240</td>
<td align="right">204,180</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">222,540</td>
<td align="right">153,920</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">183,140</td>
<td align="right">127,200</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">225,360</td>
<td align="right">157,540</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">225,360</td>
<td align="right">157,540</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">412,920</td>
<td align="right">293,280</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">412,940</td>
<td align="right">293,300</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">266,500</td>
<td align="right">198,680</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">22,695,720</td>
<td align="right">17,408,180</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">39,630,620</td>
<td align="right">30,708,040</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,172,300</td>
<td align="right">917,620</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">21,223,360</td>
<td align="right">17,251,240</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,356,300</td>
<td align="right">2,738,200</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">15,510,480</td>
<td align="right">12,747,920</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">20,068,480</td>
<td align="right">16,566,480</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">17,399,220</td>
<td align="right">20,304,980</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">56,172,720</td>
<td align="right">47,202,580</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">129,488,760</td>
<td align="right">110,598,620</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">25,463,240</td>
<td align="right">21,798,600</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">51,854,200</td>
<td align="right">44,540,720</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,703,460</td>
<td align="right">6,492,740</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">220,852,860</td>
<td align="right">190,291,480</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,584,340</td>
<td align="right">2,230,760</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,183,120</td>
<td align="right">1,023,340</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">10,912,600</td>
<td align="right">9,464,380</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,666,700</td>
<td align="right">3,283,240</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">1,565,360</td>
<td align="right">1,723,020</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,572,100</td>
<td align="right">3,259,560</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,833,780</td>
<td align="right">2,598,500</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">107,040</td>
<td align="right">114,660</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">11,982,520</td>
<td align="right">11,167,760</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">67,800</td>
<td align="right">63,240</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">30,102,400</td>
<td align="right">28,230,440</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,091,200</td>
<td align="right">1,963,580</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">3,420,720</td>
<td align="right">3,253,360</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">29,273,460</td>
<td align="right">28,081,720</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">38,410,960</td>
<td align="right">36,930,600</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">20,778,640</td>
<td align="right">21,232,200</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">23,045,820</td>
<td align="right">22,641,220</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">17,234,880</td>
<td align="right">16,986,140</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,858,700</td>
<td align="right">1,834,460</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">19,375,840</td>
<td align="right">19,136,660</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">19,631,940</td>
<td align="right">19,404,060</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">48,331,120</td>
<td align="right">47,777,620</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">11,350,200</td>
<td align="right">11,461,300</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,494,520</td>
<td align="right">3,473,360</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,504,180</td>
<td align="right">4,479,940</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">8,496,980</td>
<td align="right">8,496,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,346,200</td>
<td align="right">1,346,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,296,080</td>
<td align="right">1,296,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">53,280</td>
<td align="right">53,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">46,000</td>
<td align="right">46,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">46,000</td>
<td align="right">46,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">41,220</td>
<td align="right">41,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">41,220</td>
<td align="right">41,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">41,160</td>
<td align="right">41,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">33,960</td>
<td align="right">33,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">19,200</td>
<td align="right">19,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">19,120</td>
<td align="right">19,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">8,420</td>
<td align="right">8,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,120</td>
<td align="right">4,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,800</td>
<td align="right">3,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,420</td>
<td align="right">2,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,040</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">880</td>
<td align="right">880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">20</td>
<td align="right">20</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">205,900</td>
<td align="right">0.2%</td>
<td align="right">96,040</td>
<td align="right">0.1%</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,689,580</td>
<td align="right">6.6%</td>
<td align="right">6,484,920</td>
<td align="right">7.5%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">79,929,360</td>
<td align="right">93.1%</td>
<td align="right">80,108,500</td>
<td align="right">92.4%</td>
<td align="right">0.2%</td>
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
<td align="right">12,740</td>
<td align="right">71.8%</td>
<td align="right">6,700</td>
<td align="right">69.6%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,000</td>
<td align="right">28.2%</td>
<td align="right">2,920</td>
<td align="right">30.4%</td>
<td align="right">-41.6%</td>
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
<td align="left">add different types</td>
<td align="right">9,560</td>
<td align="right">75.0%</td>
<td align="right">3,420</td>
<td align="right">51.0%</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">1,940</td>
<td align="right">15.2%</td>
<td align="right">2,040</td>
<td align="right">30.4%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">960</td>
<td align="right">7.5%</td>
<td align="right">960</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">140</td>
<td align="right">1.1%</td>
<td align="right">140</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">140</td>
<td align="right">1.1%</td>
<td align="right">140</td>
<td align="right">2.1%</td>
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
<td align="right">51,180</td>
<td align="right">0.1%</td>
<td align="right">51,180</td>
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
<td align="right">59,415,480</td>
<td align="right">99.9%</td>
<td align="right">59,415,480</td>
<td align="right">99.9%</td>
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
<td align="right">50,080</td>
<td align="right">0.1%</td>
<td align="right">50,080</td>
<td align="right">0.1%</td>
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
<td align="right">3,020</td>
<td align="right">100.0%</td>
<td align="right">3,020</td>
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
<td align="right">40</td>
<td align="right">50.0%</td>
<td align="right">40</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">23,260</td>
<td align="right">0.0%</td>
<td align="right">15,440</td>
<td align="right">0.0%</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">104,620</td>
<td align="right">0.1%</td>
<td align="right">111,940</td>
<td align="right">0.1%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">79,658,800</td>
<td align="right">99.8%</td>
<td align="right">79,652,020</td>
<td align="right">99.8%</td>
<td align="right">-0.0%</td>
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
<td align="right">1,680</td>
<td align="right">59.2%</td>
<td align="right">1,980</td>
<td align="right">66.0%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,160</td>
<td align="right">40.8%</td>
<td align="right">1,020</td>
<td align="right">34.0%</td>
<td align="right">-12.1%</td>
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
<td align="left">float long</td>
<td align="right">420</td>
<td align="right">25.0%</td>
<td align="right">720</td>
<td align="right">36.4%</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">920</td>
<td align="right">54.8%</td>
<td align="right">920</td>
<td align="right">46.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">180</td>
<td align="right">10.7%</td>
<td align="right">180</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">160</td>
<td align="right">9.5%</td>
<td align="right">160</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">1,887,520</td>
<td align="right">100.0%</td>
<td align="right">1,887,520</td>
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
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
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
<td align="right">6,374,020</td>
<td align="right">100.0%</td>
<td align="right">3,617,780</td>
<td align="right">100.0%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">460</td>
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
<td align="right">400</td>
<td align="right">95.2%</td>
<td align="right">400</td>
<td align="right">95.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">4.8%</td>
<td align="right">20</td>
<td align="right">4.8%</td>
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
<td align="right">6,674,940</td>
<td align="right">6,674,940 / 0 !!</td>
<td align="right">6,674,940</td>
<td align="right">6,674,940 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">33,960</td>
<td align="right">33,960 / 0 !!</td>
<td align="right">33,960</td>
<td align="right">33,960 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,720</td>
<td align="right">9,720 / 0 !!</td>
<td align="right">9,720</td>
<td align="right">9,720 / 0 !!</td>
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
<td align="right">283,383,480</td>
<td align="right">100.0%</td>
<td align="right">279,324,720</td>
<td align="right">100.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,240</td>
<td align="right">0.0%</td>
<td align="right">4,240</td>
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
<td align="right">3,180</td>
<td align="right">0.0%</td>
<td align="right">3,180</td>
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
<td align="right">4,220</td>
<td align="right">99.5%</td>
<td align="right">4,220</td>
<td align="right">99.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">0.5%</td>
<td align="right">20</td>
<td align="right">0.5%</td>
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
<td align="right">57,153,380</td>
<td align="right">100.0%</td>
<td align="right">57,119,120</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,780</td>
<td align="right">0.0%</td>
<td align="right">1,780</td>
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
<td align="right">2,020</td>
<td align="right">100.0%</td>
<td align="right">2,020</td>
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

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

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
<td align="right">60</td>
<td align="right">75.0%</td>
<td align="right">60</td>
<td align="right">75.0%</td>
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
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
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
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">1,200</td>
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
<td align="right">46,588,140</td>
<td align="right">100.0%</td>
<td align="right">46,588,140</td>
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
<td align="right">1,220</td>
<td align="right">100.0%</td>
<td align="right">1,220</td>
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
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
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
<td align="right">8,496,980</td>
<td align="right">100.0%</td>
<td align="right">8,496,980</td>
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
<td align="right">100</td>
<td align="right">100.0%</td>
<td align="right">100</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,441,800</td>
<td align="right">3.6%</td>
<td align="right">1,397,740</td>
<td align="right">3.5%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,270,940</td>
<td align="right">96.4%</td>
<td align="right">38,203,600</td>
<td align="right">96.5%</td>
<td align="right">-0.2%</td>
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
<td align="right">27,680</td>
<td align="right">99.9%</td>
<td align="right">26,840</td>
<td align="right">99.9%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
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
<td align="right">38,900</td>
<td align="right">99.8%</td>
<td align="right">38,900</td>
<td align="right">99.8%</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
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
<td align="right">393,968,560</td>
<td align="right">40.7%</td>
<td align="right">337,099,760</td>
<td align="right">39.2%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,724,480</td>
<td align="right">0.2%</td>
<td align="right">1,562,800</td>
<td align="right">0.2%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">563,882,020</td>
<td align="right">58.2%</td>
<td align="right">511,953,300</td>
<td align="right">59.5%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,326,120</td>
<td align="right">1.0%</td>
<td align="right">10,101,860</td>
<td align="right">1.2%</td>
<td align="right">8.3%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">5,689,580</td>
<td align="right">97.2%</td>
<td align="right">6,484,920</td>
<td align="right">97.4%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">104,620</td>
<td align="right">1.8%</td>
<td align="right">111,940</td>
<td align="right">1.7%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">51,180</td>
<td align="right">0.9%</td>
<td align="right">51,180</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,240</td>
<td align="right">0.1%</td>
<td align="right">4,240</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,780</td>
<td align="right">0.0%</td>
<td align="right">1,780</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">1,200</td>
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
<td align="left">FOR_ITER</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">162,860</td>
<td align="right">9.4%</td>
<td align="right">53,000</td>
<td align="right">3.4%</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">19,020</td>
<td align="right">1.1%</td>
<td align="right">11,200</td>
<td align="right">0.7%</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">85,920</td>
<td align="right">5.0%</td>
<td align="right">63,660</td>
<td align="right">4.1%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">84,940</td>
<td align="right">4.9%</td>
<td align="right">63,140</td>
<td align="right">4.0%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">636,000</td>
<td align="right">36.9%</td>
<td align="right">636,000</td>
<td align="right">40.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">634,940</td>
<td align="right">36.8%</td>
<td align="right">634,940</td>
<td align="right">40.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">50,020</td>
<td align="right">2.9%</td>
<td align="right">50,020</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">43,040</td>
<td align="right">2.5%</td>
<td align="right">43,040</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">4,240</td>
<td align="right">0.2%</td>
<td align="right">4,240</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,180</td>
<td align="right">0.2%</td>
<td align="right">3,180</td>
<td align="right">0.2%</td>
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
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">55,311,700</td>
<td align="right">100.0%</td>
<td align="right">55,311,700</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">55,357,900</td>
<td align="right">100.1%</td>
<td align="right">55,357,900</td>
<td align="right">100.1%</td>
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
<td align="left">Immortal decrefs</td>
<td align="right">12,703,734</td>
<td align="right">2.8%</td>
<td align="right">14,042,134</td>
<td align="right">3.1%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">182,514,476</td>
<td align="right">41.6%</td>
<td align="right">200,035,208</td>
<td align="right">45.3%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">20,374,548</td>
<td align="right">4.6%</td>
<td align="right">21,864,085</td>
<td align="right">5.0%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">203,161,800</td>
<td align="right">46.3%</td>
<td align="right">188,550,600</td>
<td align="right">42.7%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">102,422,572</td>
<td align="right">22.5%</td>
<td align="right">108,345,044</td>
<td align="right">23.7%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">32,452,540</td>
<td align="right">7.4%</td>
<td align="right">30,965,500</td>
<td align="right">7.0%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">30,495,140</td>
<td align="right">6.7%</td>
<td align="right">29,165,620</td>
<td align="right">6.4%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,244</td>
<td align="right"></td>
<td align="right">1,267</td>
<td align="right"></td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">12,160</td>
<td align="right">0.0%</td>
<td align="right">12,380</td>
<td align="right">0.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">309,519,880</td>
<td align="right">68.0%</td>
<td align="right">306,507,640</td>
<td align="right">66.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">243</td>
<td align="right"></td>
<td align="right">242</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,548</td>
<td align="right"></td>
<td align="right">1,542</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">49,260</td>
<td align="right">0.2%</td>
<td align="right">49,360</td>
<td align="right">0.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">13,372</td>
<td align="right"></td>
<td align="right">13,358</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">1,237</td>
<td align="right"></td>
<td align="right">1,238</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">9,400,860</td>
<td align="right">35.5%</td>
<td align="right">9,401,240</td>
<td align="right">35.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">17,083,500</td>
<td align="right"></td>
<td align="right">17,083,620</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">17,085,500</td>
<td align="right">64.5%</td>
<td align="right">17,085,620</td>
<td align="right">64.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">9,339,440</td>
<td align="right">35.3%</td>
<td align="right">9,339,500</td>
<td align="right">35.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">9,360,412</td>
<td align="right"></td>
<td align="right">9,360,467</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">46,140</td>
<td align="right"></td>
<td align="right">46,140</td>
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
<td align="right">40</td>
<td align="right">27,620</td>
<td align="right">3,195,280</td>
<td align="right">12,940</td>
<td align="right">60,920</td>
<td align="right">40</td>
<td align="right">27,620</td>
<td align="right">3,196,780</td>
<td align="right">12,060</td>
<td align="right">61,800</td>
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">20</td>
<td align="right">0.5%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">20</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">120</td>
<td align="right">9.4%</td>
<td align="right">240</td>
<td align="right">13.8%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,280</td>
<td align="right">33.7%</td>
<td align="right">1,740</td>
<td align="right">34.8%</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,800</td>
<td align="right"></td>
<td align="right">5,000</td>
<td align="right"></td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">33,888,780</td>
<td align="right"></td>
<td align="right">44,433,920</td>
<td align="right"></td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">460</td>
<td align="right">12.1%</td>
<td align="right">340</td>
<td align="right">6.8%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">2,520</td>
<td align="right">66.3%</td>
<td align="right">3,080</td>
<td align="right">61.6%</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,233,393,560</td>
<td align="right">6,590.4%</td>
<td align="right">2,544,014,120</td>
<td align="right">5,725.4%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">160</td>
<td align="right">4.2%</td>
<td align="right">180</td>
<td align="right">3.6%</td>
<td align="right">12.5%</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
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
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">180</td>
<td align="right">3.6%</td>
<td align="right">180 / 0 !!</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,280</td>
<td align="right"></td>
<td align="right">1,740</td>
<td align="right"></td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,280</td>
<td align="right">100.0%</td>
<td align="right">1,660</td>
<td align="right">95.4%</td>
<td align="right">29.7%</td>
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
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">342,880</td>
<td align="right">1.9%</td>
<td align="right">486,560</td>
<td align="right">1.9%</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">15,050,760</td>
<td align="right">83.1%</td>
<td align="right">20,869,940</td>
<td align="right">83.3%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">18,104,320</td>
<td align="right"></td>
<td align="right">25,067,520</td>
<td align="right"></td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">2,710,680</td>
<td align="right">15.0%</td>
<td align="right">3,711,020</td>
<td align="right">14.8%</td>
<td align="right">36.9%</td>
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
<td align="left">240</td>
<td align="right">18.8%</td>
<td align="left">320</td>
<td align="right">19.3%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">300</td>
<td align="right">23.4%</td>
<td align="left">360</td>
<td align="right">21.7%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">420</td>
<td align="right">32.8%</td>
<td align="left">420</td>
<td align="right">25.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">280</td>
<td align="right">21.9%</td>
<td align="left">480</td>
<td align="right">28.9%</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">20</td>
<td align="right">1.6%</td>
<td align="left">80</td>
<td align="right">4.8%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">20</td>
<td align="right">1.6%</td>
<td align="left"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">60</td>
<td align="right">4.7%</td>
<td align="right">80</td>
<td align="right">4.6%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">2.3%</td>
<td align="right">40 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">180</td>
<td align="right">14.1%</td>
<td align="right">220</td>
<td align="right">12.6%</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">380</td>
<td align="right">29.7%</td>
<td align="right">560</td>
<td align="right">32.2%</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">400</td>
<td align="right">31.2%</td>
<td align="right">300</td>
<td align="right">17.2%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">220</td>
<td align="right">17.2%</td>
<td align="right">420</td>
<td align="right">24.1%</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">1.6%</td>
<td align="right">120</td>
<td align="right">6.9%</td>
<td align="right">500.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">20</td>
<td align="right">1.6%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">60</td>
<td align="right">4.7%</td>
<td align="right">80</td>
<td align="right">4.6%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">2.3%</td>
<td align="right">40 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">140</td>
<td align="right">10.9%</td>
<td align="right">180</td>
<td align="right">10.3%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">280</td>
<td align="right">21.9%</td>
<td align="right">300</td>
<td align="right">17.2%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">340</td>
<td align="right">26.6%</td>
<td align="right">420</td>
<td align="right">24.1%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">380</td>
<td align="right">29.7%</td>
<td align="right">480</td>
<td align="right">27.6%</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">40</td>
<td align="right">3.1%</td>
<td align="right">140</td>
<td align="right">8.0%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">40</td>
<td align="right">3.1%</td>
<td align="right">20</td>
<td align="right">1.1%</td>
<td align="right">-50.0%</td>
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
<td align="left">_CHECK_FUNCTION</td>
<td align="right">240</td>
<td align="right">19,060</td>
<td align="right">7,841.7%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,914,560</td>
<td align="right">11,116,220</td>
<td align="right">126.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">220</td>
<td align="right">340</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">19,052,740</td>
<td align="right">27,891,740</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">119,360</td>
<td align="right">167,080</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">33,888,780</td>
<td align="right">44,433,920</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">33,888,560</td>
<td align="right">44,433,580</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">2,766,340</td>
<td align="right">3,593,120</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">3,083,260</td>
<td align="right">3,898,020</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">41,283,440</td>
<td align="right">52,061,800</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">333,680</td>
<td align="right">247,040</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">333,680</td>
<td align="right">247,040</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">1,474,600</td>
<td align="right">1,849,760</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">1,955,860</td>
<td align="right">2,436,240</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">19,059,060</td>
<td align="right">23,420,020</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">39,255,500</td>
<td align="right">48,178,080</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,750,100</td>
<td align="right">8,267,560</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">12,173,340</td>
<td align="right">14,909,640</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">48,451,460</td>
<td align="right">58,776,500</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">4,120,920</td>
<td align="right">3,254,280</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">333,680</td>
<td align="right">264,400</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">333,680</td>
<td align="right">264,400</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,347,520</td>
<td align="right">1,068,840</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">79,673,020</td>
<td align="right">94,736,520</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">8,177,180</td>
<td align="right">9,657,540</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">8,177,180</td>
<td align="right">9,657,540</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">8,177,180</td>
<td align="right">9,657,540</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">20,235,620</td>
<td align="right">23,653,800</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">35,286,580</td>
<td align="right">41,247,060</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">54,524,180</td>
<td align="right">63,704,960</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">53,169,120</td>
<td align="right">62,024,400</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">1,549,680</td>
<td align="right">1,804,360</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">1,549,680</td>
<td align="right">1,804,360</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">72,010,760</td>
<td align="right">83,339,780</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">123,497,900</td>
<td align="right">142,388,040</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">123,497,900</td>
<td align="right">142,388,040</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">612,520</td>
<td align="right">704,580</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">2,224,780</td>
<td align="right">2,557,720</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">24,709,920</td>
<td align="right">28,340,300</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">1,802,500</td>
<td align="right">2,035,860</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">662,220</td>
<td align="right">747,760</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">16,702,640</td>
<td align="right">18,832,320</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">16,997,360</td>
<td align="right">19,124,580</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">30,916,200</td>
<td align="right">34,647,260</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">33,680,840</td>
<td align="right">37,739,600</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">32,799,560</td>
<td align="right">36,716,020</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">32,799,560</td>
<td align="right">36,716,020</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">31,249,880</td>
<td align="right">34,911,660</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">34,014,520</td>
<td align="right">37,986,660</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">34,014,520</td>
<td align="right">37,986,660</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">348,712,680</td>
<td align="right">389,235,580</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">314,229,000</td>
<td align="right">350,133,920</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">1,225,040</td>
<td align="right">1,360,680</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">612,520</td>
<td align="right">680,340</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">612,520</td>
<td align="right">680,340</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">612,520</td>
<td align="right">680,340</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">612,520</td>
<td align="right">680,340</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">612,520</td>
<td align="right">680,340</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">4,886,040</td>
<td align="right">5,413,080</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">24,209,020</td>
<td align="right">26,759,160</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">24,209,020</td>
<td align="right">26,759,160</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">1,594,020</td>
<td align="right">1,761,380</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">31,378,920</td>
<td align="right">34,606,420</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">2,212,300</td>
<td align="right">1,986,520</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">19,782,140</td>
<td align="right">21,796,280</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">38,974,340</td>
<td align="right">42,903,500</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,371,020</td>
<td align="right">1,508,080</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">6,835,640</td>
<td align="right">7,505,060</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,334,320</td>
<td align="right">1,461,940</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">1,334,320</td>
<td align="right">1,461,940</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,730,780</td>
<td align="right">1,886,600</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,464,860</td>
<td align="right">4,861,720</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_INT</td>
<td align="right">647,900</td>
<td align="right">702,100</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">8,069,960</td>
<td align="right">8,741,560</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">1,939,900</td>
<td align="right">2,098,840</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">12,244,040</td>
<td align="right">13,245,820</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">1,474,600</td>
<td align="right">1,594,240</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,474,600</td>
<td align="right">1,594,240</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">1,474,600</td>
<td align="right">1,594,240</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">2,121,180</td>
<td align="right">2,293,200</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">2,121,180</td>
<td align="right">2,293,200</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">1,472,580</td>
<td align="right">1,591,960</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,110,120</td>
<td align="right">2,281,080</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">4,395,880</td>
<td align="right">4,749,460</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">4,395,880</td>
<td align="right">4,749,460</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,517,100</td>
<td align="right">4,879,600</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">3,674,080</td>
<td align="right">3,967,860</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">3,674,080</td>
<td align="right">3,967,860</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">3,674,080</td>
<td align="right">3,967,860</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">7,026,780</td>
<td align="right">7,580,280</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">7,885,860</td>
<td align="right">8,503,960</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,061,560</td>
<td align="right">3,287,520</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,313,820</td>
<td align="right">3,549,100</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">4,540,040</td>
<td align="right">4,855,920</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">16,639,720</td>
<td align="right">17,744,840</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,783,500</td>
<td align="right">1,900,360</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,449,040</td>
<td align="right">2,607,180</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,449,040</td>
<td align="right">2,607,180</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">4,888,740</td>
<td align="right">5,137,480</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,097,700</td>
<td align="right">2,010,800</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">33,654,680</td>
<td align="right">34,918,560</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,347,520</td>
<td align="right">1,300,120</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">27,701,000</td>
<td align="right">26,786,940</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">3,466,440</td>
<td align="right">3,578,040</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">7,394,660</td>
<td align="right">7,627,880</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,149,640</td>
<td align="right">5,309,420</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">16,536,920</td>
<td align="right">16,030,760</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">5,945,080</td>
<td align="right">6,070,600</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">9,346,600</td>
<td align="right">9,235,500</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">9,346,600</td>
<td align="right">9,259,740</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,224,100</td>
<td align="right">3,245,260</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">5,483,120</td>
<td align="right">5,515,740</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right"></td>
<td align="right">52,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right"></td>
<td align="right">34,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right"></td>
<td align="right">29,520</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right"></td>
<td align="right">26,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right"></td>
<td align="right">26,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right"></td>
<td align="right">26,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right"></td>
<td align="right">26,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right"></td>
<td align="right">24,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right"></td>
<td align="right">24,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right"></td>
<td align="right">24,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right"></td>
<td align="right">10,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">7,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right"></td>
<td align="right">6,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right"></td>
<td align="right">4,560</td>
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
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
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
Stats gathered on: 2025-07-01
