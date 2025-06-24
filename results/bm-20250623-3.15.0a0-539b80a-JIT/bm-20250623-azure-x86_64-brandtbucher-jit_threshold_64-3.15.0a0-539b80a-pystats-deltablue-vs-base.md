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
<td align="left">PUSH_NULL</td>
<td align="right">2,340</td>
<td align="right">1,100</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">516,460</td>
<td align="right">403,880</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">238,340</td>
<td align="right">200,680</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,129,020</td>
<td align="right">985,660</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,215,600</td>
<td align="right">5,852,800</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">682,140</td>
<td align="right">645,420</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">837,380</td>
<td align="right">799,720</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,473,000</td>
<td align="right">2,381,540</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,456,960</td>
<td align="right">2,388,540</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,294,480</td>
<td align="right">2,244,600</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">26,182,620</td>
<td align="right">25,671,680</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">30,546,860</td>
<td align="right">30,027,760</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,117,740</td>
<td align="right">6,997,740</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">31,221,460</td>
<td align="right">30,709,380</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,057,000</td>
<td align="right">3,020,280</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">17,719,360</td>
<td align="right">17,519,560</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,999,780</td>
<td align="right">11,885,980</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">10,245,180</td>
<td align="right">10,150,300</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">13,406,820</td>
<td align="right">13,293,240</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">109,398,000</td>
<td align="right">108,491,140</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">18,535,440</td>
<td align="right">18,384,160</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,985,980</td>
<td align="right">1,970,580</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">16,443,160</td>
<td align="right">16,336,520</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">33,420,560</td>
<td align="right">33,228,360</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">24,255,060</td>
<td align="right">24,132,820</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">58,127,020</td>
<td align="right">57,847,620</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">16,407,420</td>
<td align="right">16,336,520</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">19,418,500</td>
<td align="right">19,345,380</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">19,756,380</td>
<td align="right">19,699,120</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,138,080</td>
<td align="right">5,128,420</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,739,840</td>
<td align="right">2,737,880</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,893,760</td>
<td align="right">3,891,800</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,786,220</td>
<td align="right">2,784,980</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">4,585,060</td>
<td align="right">4,585,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,149,180</td>
<td align="right">4,149,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,551,740</td>
<td align="right">2,551,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">2,551,680</td>
<td align="right">2,551,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,389,420</td>
<td align="right">2,389,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,181,300</td>
<td align="right">2,181,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,762,560</td>
<td align="right">1,762,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,580,160</td>
<td align="right">1,580,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,580,160</td>
<td align="right">1,580,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,182,720</td>
<td align="right">1,182,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,182,720</td>
<td align="right">1,182,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">597,120</td>
<td align="right">597,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">203,520</td>
<td align="right">203,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">195,900</td>
<td align="right">195,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">190,080</td>
<td align="right">190,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">67,200</td>
<td align="right">67,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">46,080</td>
<td align="right">46,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">17,340</td>
<td align="right">17,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">7,880</td>
<td align="right">7,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">7,680</td>
<td align="right">7,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">7,680</td>
<td align="right">7,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,840</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,980</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">100</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">100</td>
<td align="right">100</td>
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
<td align="left">NOP</td>
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
<td align="left">LOAD_DEREF</td>
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
<td align="left">POP_JUMP_IF_NOT_NONE</td>
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
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">681,840</td>
<td align="right">6.3%</td>
<td align="right">645,120</td>
<td align="right">5.9%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,224,120</td>
<td align="right">93.7%</td>
<td align="right">10,224,120</td>
<td align="right">94.1%</td>
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
<td align="right">13.3%</td>
<td align="right">40</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">260</td>
<td align="right">86.7%</td>
<td align="right">260</td>
<td align="right">86.7%</td>
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
<td align="left">remainder</td>
<td align="right">180</td>
<td align="right">69.2%</td>
<td align="right">180</td>
<td align="right">69.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">40</td>
<td align="right">15.4%</td>
<td align="right">40</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">40</td>
<td align="right">15.4%</td>
<td align="right">40</td>
<td align="right">15.4%</td>
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
<td align="right">8,913,640</td>
<td align="right">7.8%</td>
<td align="right">8,895,000</td>
<td align="right">7.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,085,080</td>
<td align="right">7.9%</td>
<td align="right">9,066,100</td>
<td align="right">7.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">105,232,700</td>
<td align="right">92.1%</td>
<td align="right">105,251,340</td>
<td align="right">92.1%</td>
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
<td align="right">171,700</td>
<td align="right">100.0%</td>
<td align="right">171,360</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">1,985,280</td>
<td align="right">2.9%</td>
<td align="right">1,969,920</td>
<td align="right">2.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">65,854,140</td>
<td align="right">97.1%</td>
<td align="right">65,854,140</td>
<td align="right">97.1%</td>
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
<td align="right">680</td>
<td align="right">97.1%</td>
<td align="right">640</td>
<td align="right">97.0%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">2.9%</td>
<td align="right">20</td>
<td align="right">3.0%</td>
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
<td align="left">baseobject</td>
<td align="right">640</td>
<td align="right">94.1%</td>
<td align="right">600</td>
<td align="right">93.8%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">40</td>
<td align="right">5.9%</td>
<td align="right">40</td>
<td align="right">6.2%</td>
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
<td align="right">516,460</td>
<td align="right">17.3%</td>
<td align="right">403,880</td>
<td align="right">14.5%</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,472,320</td>
<td align="right">82.7%</td>
<td align="right">2,380,860</td>
<td align="right">85.5%</td>
<td align="right">-3.7%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">680</td>
<td align="right">100.0%</td>
<td align="right">680</td>
<td align="right">100.0%</td>
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
<td align="right">680</td>
<td align="right">100.0%</td>
<td align="right">680</td>
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
<td align="left">other</td>
<td align="right">3,043,260</td>
<td align="right">3,043,260 / 0 !!</td>
<td align="right">3,043,260</td>
<td align="right">3,043,260 / 0 !!</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,513,840</td>
<td align="right">3.0%</td>
<td align="right">7,442,080</td>
<td align="right">3.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">237,794,820</td>
<td align="right">94.9%</td>
<td align="right">237,233,900</td>
<td align="right">95.0%</td>
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
<td align="right">5,136,060</td>
<td align="right">2.1%</td>
<td align="right">5,126,420</td>
<td align="right">2.1%</td>
<td align="right">-0.2%</td>
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
<td align="right">1,820</td>
<td align="right">1.3%</td>
<td align="right">1,800</td>
<td align="right">1.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">142,060</td>
<td align="right">98.7%</td>
<td align="right">140,720</td>
<td align="right">98.7%</td>
<td align="right">-0.9%</td>
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
<td align="left">mutable class</td>
<td align="right">840</td>
<td align="right">46.2%</td>
<td align="right">800</td>
<td align="right">44.4%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">960</td>
<td align="right">52.7%</td>
<td align="right">980</td>
<td align="right">54.4%</td>
<td align="right">2.1%</td>
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
<td align="right">76,758,060</td>
<td align="right">100.0%</td>
<td align="right">76,758,060</td>
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
<td align="right">2,551,680</td>
<td align="right">100.0%</td>
<td align="right">2,551,680</td>
<td align="right">100.0%</td>
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
<td align="right">39,907,040</td>
<td align="right">96.6%</td>
<td align="right">39,907,040</td>
<td align="right">96.6%</td>
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
<td align="right">1,411,140</td>
<td align="right">3.4%</td>
<td align="right">1,411,140</td>
<td align="right">3.4%</td>
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
<td align="right">26,660</td>
<td align="right">100.0%</td>
<td align="right">26,660</td>
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
<td align="right">14,709,180</td>
<td align="right">100.0%</td>
<td align="right">14,632,600</td>
<td align="right">100.0%</td>
<td align="right">-0.5%</td>
</tr>
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
<td align="right">60</td>
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
<td align="right">20</td>
<td align="right">50.0%</td>
<td align="right">20</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">50.0%</td>
<td align="right">20</td>
<td align="right">50.0%</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">12,736,640</td>
<td align="right">2.4%</td>
<td align="right">12,514,980</td>
<td align="right">2.4%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">238,483,900</td>
<td align="right">45.2%</td>
<td align="right">235,865,260</td>
<td align="right">45.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">258,465,740</td>
<td align="right">49.0%</td>
<td align="right">256,243,460</td>
<td align="right">49.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">18,010,320</td>
<td align="right">3.4%</td>
<td align="right">17,920,100</td>
<td align="right">3.4%</td>
<td align="right">-0.5%</td>
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
<td align="right">681,840</td>
<td align="right">3.6%</td>
<td align="right">645,120</td>
<td align="right">3.4%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,472,320</td>
<td align="right">12.9%</td>
<td align="right">2,380,860</td>
<td align="right">12.5%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,985,280</td>
<td align="right">10.3%</td>
<td align="right">1,969,920</td>
<td align="right">10.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">8,913,640</td>
<td align="right">46.5%</td>
<td align="right">8,895,000</td>
<td align="right">46.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,136,060</td>
<td align="right">26.8%</td>
<td align="right">5,126,420</td>
<td align="right">27.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left">RESUME</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">780</td>
<td align="right">0.0%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">780</td>
<td align="right">0.0%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,453,740</td>
<td align="right">24.7%</td>
<td align="right">4,381,980</td>
<td align="right">24.5%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,102,780</td>
<td align="right">11.7%</td>
<td align="right">2,083,800</td>
<td align="right">11.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">4,585,060</td>
<td align="right">25.5%</td>
<td align="right">4,585,060</td>
<td align="right">25.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,060,100</td>
<td align="right">17.0%</td>
<td align="right">3,060,100</td>
<td align="right">17.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,389,420</td>
<td align="right">13.3%</td>
<td align="right">2,389,420</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,411,140</td>
<td align="right">7.8%</td>
<td align="right">1,411,140</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">7,820</td>
<td align="right">0.0%</td>
<td align="right">7,820</td>
<td align="right">0.0%</td>
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
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">98,726,700</td>
<td align="right">100.0%</td>
<td align="right">98,726,700</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">1,980</td>
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
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">1,980</td>
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
<td align="right">99,911,400</td>
<td align="right">101.2%</td>
<td align="right">99,911,400</td>
<td align="right">101.2%</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">10,902</td>
<td align="right"></td>
<td align="right">7,080</td>
<td align="right"></td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">10,904</td>
<td align="right"></td>
<td align="right">7,082</td>
<td align="right"></td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7</td>
<td align="right"></td>
<td align="right">5</td>
<td align="right"></td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">73</td>
<td align="right"></td>
<td align="right">75</td>
<td align="right"></td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">136,756,580</td>
<td align="right">26.4%</td>
<td align="right">135,131,820</td>
<td align="right">26.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">21,837,238</td>
<td align="right"></td>
<td align="right">22,087,760</td>
<td align="right"></td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">5,033,925</td>
<td align="right"></td>
<td align="right">5,071,781</td>
<td align="right"></td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">9,320,760</td>
<td align="right">1.7%</td>
<td align="right">9,269,400</td>
<td align="right">1.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">9,377,280</td>
<td align="right">1.8%</td>
<td align="right">9,333,600</td>
<td align="right">1.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">328,443,681</td>
<td align="right">63.5%</td>
<td align="right">329,708,767</td>
<td align="right">63.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">184,238,066</td>
<td align="right">34.4%</td>
<td align="right">184,761,268</td>
<td align="right">34.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">299,489,860</td>
<td align="right">55.9%</td>
<td align="right">298,702,600</td>
<td align="right">55.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">43,096,752</td>
<td align="right">8.0%</td>
<td align="right">43,161,362</td>
<td align="right">8.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">42,680,045</td>
<td align="right">8.3%</td>
<td align="right">42,720,568</td>
<td align="right">8.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">4,059,180</td>
<td align="right">19.7%</td>
<td align="right">4,059,000</td>
<td align="right">19.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">16,533,800</td>
<td align="right"></td>
<td align="right">16,534,060</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">16,534,000</td>
<td align="right">80.3%</td>
<td align="right">16,534,260</td>
<td align="right">80.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">4,058,940</td>
<td align="right">19.7%</td>
<td align="right">4,058,900</td>
<td align="right">19.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">2,784,000</td>
<td align="right"></td>
<td align="right">2,784,000</td>
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
<td align="right">860</td>
<td align="right">1,277,760</td>
<td align="right">21,138,442</td>
<td align="right">623,220</td>
<td align="right">1,500,100</td>
<td align="right">860</td>
<td align="right">1,295,680</td>
<td align="right">21,235,647</td>
<td align="right">608,360</td>
<td align="right">1,515,340</td>
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
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">18,549,880</td>
<td align="right"></td>
<td align="right">62,487,060</td>
<td align="right"></td>
<td align="right">236.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">140</td>
<td align="right">8.0%</td>
<td align="right">280</td>
<td align="right">11.8%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">860</td>
<td align="right">49.4%</td>
<td align="right">1,320</td>
<td align="right">55.5%</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,740</td>
<td align="right"></td>
<td align="right">2,380</td>
<td align="right"></td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">120</td>
<td align="right">6.9%</td>
<td align="right">140</td>
<td align="right">5.9%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,752,209,600</td>
<td align="right">14,836.8%</td>
<td align="right">2,885,041,760</td>
<td align="right">4,617.0%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">620</td>
<td align="right">35.6%</td>
<td align="right">640</td>
<td align="right">26.9%</td>
<td align="right">3.2%</td>
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
<td align="right">40</td>
<td align="right">1.7%</td>
<td align="right">40 / 0 !!</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">260</td>
<td align="right">41.9%</td>
<td align="right">120</td>
<td align="right">18.8%</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">620</td>
<td align="right"></td>
<td align="right">640</td>
<td align="right"></td>
<td align="right">3.2%</td>
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
<td align="right">534,600</td>
<td align="right">10.2%</td>
<td align="right">209,080</td>
<td align="right">9.5%</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">99,200</td>
<td align="right">1.9%</td>
<td align="right">40,640</td>
<td align="right">1.8%</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">5,242,880</td>
<td align="right"></td>
<td align="right">2,211,840</td>
<td align="right"></td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">4,609,080</td>
<td align="right">87.9%</td>
<td align="right">1,962,120</td>
<td align="right">88.7%</td>
<td align="right">-57.4%</td>
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
<td align="left">60</td>
<td align="right">23.1%</td>
<td align="left">20</td>
<td align="right">16.7%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">40</td>
<td align="right">15.4%</td>
<td align="left">80</td>
<td align="right">66.7%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">120</td>
<td align="right">46.2%</td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">40</td>
<td align="right">15.4%</td>
<td align="left">20</td>
<td align="right">16.7%</td>
<td align="right">-50.0%</td>
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
<td align="right">20</td>
<td align="right">3.2%</td>
<td align="right">20</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">40</td>
<td align="right">6.5%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">40</td>
<td align="right">6.5%</td>
<td align="right">80</td>
<td align="right">12.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">40</td>
<td align="right">6.5%</td>
<td align="right">120</td>
<td align="right">18.8%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">300</td>
<td align="right">48.4%</td>
<td align="right">160</td>
<td align="right">25.0%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">6.2%</td>
<td align="right">40 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">180</td>
<td align="right">29.0%</td>
<td align="right">220</td>
<td align="right">34.4%</td>
<td align="right">22.2%</td>
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
<td align="left"><= 8</td>
<td align="right">60</td>
<td align="right">9.7%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">80</td>
<td align="right">12.5%</td>
<td align="right">80 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">160</td>
<td align="right">25.8%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">40</td>
<td align="right">6.5%</td>
<td align="right">20</td>
<td align="right">3.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">3.1%</td>
<td align="right"></td>
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
<td align="left">_DEOPT</td>
<td align="right">20</td>
<td align="right">500</td>
<td align="right">2,400.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">18,549,880</td>
<td align="right">62,487,060</td>
<td align="right">236.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">18,549,860</td>
<td align="right">62,486,560</td>
<td align="right">236.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">19,919,760</td>
<td align="right">757,720</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">38,469,640</td>
<td align="right">63,244,780</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">775,500</td>
<td align="right">1,128,960</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">775,500</td>
<td align="right">1,128,960</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">775,500</td>
<td align="right">1,128,960</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">67,800,700</td>
<td align="right">91,514,640</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,322,880</td>
<td align="right">1,650,380</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,322,880</td>
<td align="right">1,642,700</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,322,880</td>
<td align="right">1,636,520</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,556,100</td>
<td align="right">3,095,040</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">537,680</td>
<td align="right">650,260</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">537,680</td>
<td align="right">650,260</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">530,380</td>
<td align="right">636,760</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">586,300</td>
<td align="right">654,720</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">339,600</td>
<td align="right">376,320</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">172,340</td>
<td align="right">190,080</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">172,340</td>
<td align="right">190,080</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,321,420</td>
<td align="right">1,434,240</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">748,840</td>
<td align="right">798,720</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">4,726,560</td>
<td align="right">5,035,280</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,884,760</td>
<td align="right">2,995,200</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,432,720</td>
<td align="right">3,552,720</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">25,130,220</td>
<td align="right">25,637,460</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,128,960</td>
<td align="right">1,147,260</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">775,680</td>
<td align="right">783,360</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">4,536,700</td>
<td align="right">4,574,360</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">4,536,700</td>
<td align="right">4,574,360</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">65,233,960</td>
<td align="right">65,744,560</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">67,507,240</td>
<td align="right">68,019,800</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">67,507,240</td>
<td align="right">68,019,800</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">67,507,240</td>
<td align="right">68,019,800</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">67,507,240</td>
<td align="right">68,019,800</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">2,146,560</td>
<td align="right">2,161,920</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">481,277,960</td>
<td align="right">484,677,780</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">3,380,660</td>
<td align="right">3,404,280</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">25,797,320</td>
<td align="right">25,940,680</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">30,900,560</td>
<td align="right">31,045,100</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">26,883,780</td>
<td align="right">27,006,800</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">385,180,800</td>
<td align="right">386,794,200</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">146,222,400</td>
<td align="right">146,761,040</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">47,318,700</td>
<td align="right">47,469,980</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">28,804,540</td>
<td align="right">28,896,000</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">66,184,360</td>
<td align="right">66,383,280</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">67,334,440</td>
<td align="right">67,534,340</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">67,334,440</td>
<td align="right">67,534,340</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">67,334,440</td>
<td align="right">67,534,340</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">51,515,800</td>
<td align="right">51,668,020</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">24,906,920</td>
<td align="right">24,980,040</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">23,645,500</td>
<td align="right">23,714,900</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">66,490,840</td>
<td align="right">66,683,040</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">24,910,760</td>
<td align="right">24,981,660</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">24,910,760</td>
<td align="right">24,981,660</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">24,910,760</td>
<td align="right">24,981,660</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">46,598,940</td>
<td align="right">46,721,180</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">752,640</td>
<td align="right">754,600</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">376,320</td>
<td align="right">377,300</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">45,652,380</td>
<td align="right">45,765,960</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">45,652,380</td>
<td align="right">45,765,960</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">143,181,580</td>
<td align="right">143,460,980</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">143,181,580</td>
<td align="right">143,460,980</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,322,880</td>
<td align="right">1,324,840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,322,880</td>
<td align="right">1,324,840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,322,880</td>
<td align="right">1,324,840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">48,916,380</td>
<td align="right">48,973,640</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,754,880</td>
<td align="right">1,756,120</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">4,659,840</td>
<td align="right">4,662,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">9,720,920</td>
<td align="right">9,723,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,754,880</td>
<td align="right">1,754,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,754,880</td>
<td align="right">1,754,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">1,754,880</td>
<td align="right">1,754,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,754,880</td>
<td align="right">1,754,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">1,754,880</td>
<td align="right">1,754,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">950,400</td>
<td align="right">950,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">395,520</td>
<td align="right">395,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">389,760</td>
<td align="right">389,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">387,840</td>
<td align="right">387,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">1,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">1,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">1,240</td>
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

<table>
<thead>
<tr>
<th align="left">Opcode</th>
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL</td>
<td align="right">140</td>
<td align="right">280</td>
<td align="right">100.0%</td>
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
Stats gathered on: 2025-06-24
