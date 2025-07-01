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
<td align="right">2,650,940</td>
<td align="right">1,054,140</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">762,460</td>
<td align="right">408,920</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">727,540</td>
<td align="right">410,680</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,744,260</td>
<td align="right">2,502,080</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,340</td>
<td align="right">1,720</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">150,480</td>
<td align="right">190,080</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,361,460</td>
<td align="right">1,007,920</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">809,200</td>
<td align="right">649,360</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,036,300</td>
<td align="right">7,129,480</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">236,200</td>
<td align="right">200,820</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,315,320</td>
<td align="right">2,081,720</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">66,055,840</td>
<td align="right">60,883,320</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">19,224,040</td>
<td align="right">17,753,380</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,743,900</td>
<td align="right">1,613,220</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,743,900</td>
<td align="right">1,613,220</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,283,860</td>
<td align="right">3,039,740</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">20,654,440</td>
<td align="right">19,159,740</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">21,935,040</td>
<td align="right">20,365,740</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">15,120,300</td>
<td align="right">14,040,940</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,788,300</td>
<td align="right">7,268,520</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,661,940</td>
<td align="right">2,486,420</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,173,400</td>
<td align="right">3,918,100</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">28,581,120</td>
<td align="right">26,888,620</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">118,668,400</td>
<td align="right">111,733,700</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">33,899,960</td>
<td align="right">31,952,740</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">33,044,340</td>
<td align="right">31,184,660</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">10,941,520</td>
<td align="right">10,361,720</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,898,760</td>
<td align="right">2,749,600</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">12,654,400</td>
<td align="right">12,004,580</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">26,167,540</td>
<td align="right">24,907,460</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,430,060</td>
<td align="right">5,174,600</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">35,851,880</td>
<td align="right">34,204,700</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">17,489,220</td>
<td align="right">16,697,260</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">17,532,100</td>
<td align="right">16,757,300</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,546,940</td>
<td align="right">2,437,460</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,844,460</td>
<td align="right">1,767,600</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">20,500,620</td>
<td align="right">19,771,060</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,261,620</td>
<td align="right">2,186,180</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">4,312,560</td>
<td align="right">4,181,880</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,785,840</td>
<td align="right">2,785,220</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">4,584,720</td>
<td align="right">4,584,720</td>
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
<td align="right">2,551,460</td>
<td align="right">2,551,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,389,320</td>
<td align="right">2,389,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,182,440</td>
<td align="right">1,182,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,182,440</td>
<td align="right">1,182,440</td>
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
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">67,140</td>
<td align="right">67,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">45,960</td>
<td align="right">45,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">17,200</td>
<td align="right">17,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">7,840</td>
<td align="right">7,840</td>
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
<td align="right">7,660</td>
<td align="right">7,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">6,000</td>
<td align="right">6,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4,040</td>
<td align="right">4,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,840</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,980</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,300</td>
<td align="right">1,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,240</td>
<td align="right">1,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
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
<td align="left">UNPACK_SEQUENCE</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
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
<td align="right">807,560</td>
<td align="right">7.3%</td>
<td align="right">647,920</td>
<td align="right">6.0%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,223,840</td>
<td align="right">92.7%</td>
<td align="right">10,223,840</td>
<td align="right">94.0%</td>
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
<td align="right">1,360</td>
<td align="right">82.9%</td>
<td align="right">1,160</td>
<td align="right">80.6%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">280</td>
<td align="right">17.1%</td>
<td align="right">280</td>
<td align="right">19.4%</td>
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
<td align="left">subscr</td>
<td align="right">440</td>
<td align="right">32.4%</td>
<td align="right">240</td>
<td align="right">20.7%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">720</td>
<td align="right">52.9%</td>
<td align="right">720</td>
<td align="right">62.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">200</td>
<td align="right">14.7%</td>
<td align="right">200</td>
<td align="right">17.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,103,240</td>
<td align="right">8.0%</td>
<td align="right">9,087,340</td>
<td align="right">7.9%</td>
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
<td align="right">8,934,860</td>
<td align="right">7.8%</td>
<td align="right">8,919,260</td>
<td align="right">7.8%</td>
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
<td align="right">105,211,700</td>
<td align="right">92.0%</td>
<td align="right">105,227,300</td>
<td align="right">92.0%</td>
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
<td align="right">174,380</td>
<td align="right">100.0%</td>
<td align="right">174,080</td>
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
<td align="right">2,313,320</td>
<td align="right">3.4%</td>
<td align="right">2,079,780</td>
<td align="right">3.1%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">65,853,720</td>
<td align="right">96.6%</td>
<td align="right">65,853,720</td>
<td align="right">96.9%</td>
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
<td align="right">1,580</td>
<td align="right">79.0%</td>
<td align="right">1,520</td>
<td align="right">78.4%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">420</td>
<td align="right">21.0%</td>
<td align="right">420</td>
<td align="right">21.6%</td>
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
<td align="left">different types</td>
<td align="right">240</td>
<td align="right">15.2%</td>
<td align="right">100</td>
<td align="right">6.6%</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">1,240</td>
<td align="right">78.5%</td>
<td align="right">1,320</td>
<td align="right">86.8%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">100</td>
<td align="right">6.3%</td>
<td align="right">100</td>
<td align="right">6.6%</td>
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
<td align="right">727,540</td>
<td align="right">16.3%</td>
<td align="right">410,680</td>
<td align="right">14.1%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,742,140</td>
<td align="right">83.7%</td>
<td align="right">2,500,300</td>
<td align="right">85.8%</td>
<td align="right">-33.2%</td>
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
<td align="right">1,980</td>
<td align="right">93.4%</td>
<td align="right">1,640</td>
<td align="right">92.1%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">140</td>
<td align="right">6.6%</td>
<td align="right">140</td>
<td align="right">7.9%</td>
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
<td align="right">1,960</td>
<td align="right">99.0%</td>
<td align="right">1,620</td>
<td align="right">98.8%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">20</td>
<td align="right">1.0%</td>
<td align="right">20</td>
<td align="right">1.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,420,200</td>
<td align="right">2.1%</td>
<td align="right">5,164,900</td>
<td align="right">2.1%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">242,005,100</td>
<td align="right">94.9%</td>
<td align="right">239,083,000</td>
<td align="right">95.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,511,460</td>
<td align="right">2.9%</td>
<td align="right">7,494,520</td>
<td align="right">3.0%</td>
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
<td align="right">5,560</td>
<td align="right">3.7%</td>
<td align="right">5,400</td>
<td align="right">3.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">145,680</td>
<td align="right">96.3%</td>
<td align="right">145,360</td>
<td align="right">96.4%</td>
<td align="right">-0.2%</td>
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
<td align="left">class method obj</td>
<td align="right">2,760</td>
<td align="right">49.6%</td>
<td align="right">2,600</td>
<td align="right">48.1%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2,780</td>
<td align="right">50.0%</td>
<td align="right">2,780</td>
<td align="right">51.5%</td>
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
<td align="right">74,921,240</td>
<td align="right">100.0%</td>
<td align="right">75,637,720</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
<td align="right">2,020</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">220</td>
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
<td align="right">2,551,460</td>
<td align="right">100.0%</td>
<td align="right">2,551,460</td>
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
<td align="right">220</td>
<td align="right">100.0%</td>
<td align="right">220</td>
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
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">1,140</td>
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
<td align="right">39,914,400</td>
<td align="right">96.6%</td>
<td align="right">39,914,400</td>
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
<td align="right">1,402,320</td>
<td align="right">3.4%</td>
<td align="right">1,402,320</td>
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
<td align="right">27,360</td>
<td align="right">99.9%</td>
<td align="right">27,360</td>
<td align="right">99.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
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
<td align="left">not in keys</td>
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
<td align="right">100.0%</td>
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
<td align="right">15,167,080</td>
<td align="right">100.0%</td>
<td align="right">14,817,440</td>
<td align="right">100.0%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
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
<td align="right">580</td>
<td align="right">96.7%</td>
<td align="right">580</td>
<td align="right">96.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">3.3%</td>
<td align="right">20</td>
<td align="right">3.3%</td>
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
<td align="right">20</td>
<td align="right">25.0%</td>
<td align="right">20</td>
<td align="right">25.0%</td>
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
<td align="right">14,974,740</td>
<td align="right">2.6%</td>
<td align="right">12,908,140</td>
<td align="right">2.4%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">265,053,140</td>
<td align="right">46.0%</td>
<td align="right">245,939,240</td>
<td align="right">45.5%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">277,970,680</td>
<td align="right">48.3%</td>
<td align="right">264,116,600</td>
<td align="right">48.8%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">18,017,280</td>
<td align="right">3.1%</td>
<td align="right">17,984,660</td>
<td align="right">3.3%</td>
<td align="right">-0.2%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">3,742,140</td>
<td align="right">17.6%</td>
<td align="right">2,500,300</td>
<td align="right">12.9%</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">807,560</td>
<td align="right">3.8%</td>
<td align="right">647,920</td>
<td align="right">3.4%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,313,320</td>
<td align="right">10.9%</td>
<td align="right">2,079,780</td>
<td align="right">10.8%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,420,200</td>
<td align="right">25.5%</td>
<td align="right">5,164,900</td>
<td align="right">26.7%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">8,934,860</td>
<td align="right">42.1%</td>
<td align="right">8,919,260</td>
<td align="right">46.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="left">RESUME</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,121,400</td>
<td align="right">11.8%</td>
<td align="right">2,105,500</td>
<td align="right">11.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,468,200</td>
<td align="right">24.8%</td>
<td align="right">4,451,260</td>
<td align="right">24.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">4,584,720</td>
<td align="right">25.4%</td>
<td align="right">4,584,720</td>
<td align="right">25.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,043,260</td>
<td align="right">16.9%</td>
<td align="right">3,043,260</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,389,320</td>
<td align="right">13.3%</td>
<td align="right">2,389,320</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,402,320</td>
<td align="right">7.8%</td>
<td align="right">1,402,320</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">7,800</td>
<td align="right">0.0%</td>
<td align="right">7,800</td>
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
<td align="right">2,260</td>
<td align="right">0.0%</td>
<td align="right">2,260</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">98,726,420</td>
<td align="right">100.0%</td>
<td align="right">98,726,420</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,260</td>
<td align="right">0.0%</td>
<td align="right">2,260</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">2,260</td>
<td align="right">0.0%</td>
<td align="right">2,260</td>
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
<td align="right">2,260</td>
<td align="right">0.0%</td>
<td align="right">2,260</td>
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
<td align="right">99,911,120</td>
<td align="right">101.2%</td>
<td align="right">99,911,120</td>
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
<td align="left">Method cache collisions</td>
<td align="right">5,274</td>
<td align="right"></td>
<td align="right">15,124</td>
<td align="right"></td>
<td align="right">186.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">5,611</td>
<td align="right"></td>
<td align="right">15,452</td>
<td align="right"></td>
<td align="right">175.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">560</td>
<td align="right">0.0%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">1,475</td>
<td align="right"></td>
<td align="right">1,058</td>
<td align="right"></td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">10,246,820</td>
<td align="right">1.9%</td>
<td align="right">9,523,280</td>
<td align="right">1.8%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">325</td>
<td align="right"></td>
<td align="right">342</td>
<td align="right"></td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">148,857,520</td>
<td align="right">28.9%</td>
<td align="right">141,302,580</td>
<td align="right">27.3%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">9,977,520</td>
<td align="right">1.9%</td>
<td align="right">9,487,520</td>
<td align="right">1.8%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">174,347,706</td>
<td align="right">32.7%</td>
<td align="right">180,767,851</td>
<td align="right">33.7%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">314,334,217</td>
<td align="right">61.0%</td>
<td align="right">323,760,680</td>
<td align="right">62.6%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">41,782,620</td>
<td align="right">7.8%</td>
<td align="right">42,533,653</td>
<td align="right">7.9%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">307,451,340</td>
<td align="right">57.6%</td>
<td align="right">302,963,540</td>
<td align="right">56.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">42,047,444</td>
<td align="right">8.2%</td>
<td align="right">42,553,176</td>
<td align="right">8.2%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">5,062,889</td>
<td align="right"></td>
<td align="right">5,086,897</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">21,851,269</td>
<td align="right"></td>
<td align="right">21,827,428</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">4,058,180</td>
<td align="right">19.7%</td>
<td align="right">4,058,560</td>
<td align="right">19.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">16,535,300</td>
<td align="right"></td>
<td align="right">16,535,580</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">16,536,100</td>
<td align="right">80.3%</td>
<td align="right">16,536,380</td>
<td align="right">80.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">4,057,560</td>
<td align="right">19.7%</td>
<td align="right">4,057,540</td>
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
<td align="right">880</td>
<td align="right">1,295,280</td>
<td align="right">21,454,099</td>
<td align="right">629,160</td>
<td align="right">1,524,280</td>
<td align="right">880</td>
<td align="right">1,307,280</td>
<td align="right">21,537,842</td>
<td align="right">613,540</td>
<td align="right">1,540,320</td>
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
<td align="right">60</td>
<td align="right">3.3%</td>
<td align="right">300</td>
<td align="right">10.6%</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">15,718,120</td>
<td align="right"></td>
<td align="right">59,103,480</td>
<td align="right"></td>
<td align="right">276.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">80</td>
<td align="right">4.4%</td>
<td align="right">280</td>
<td align="right">9.9%</td>
<td align="right">250.0%</td>
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
<td align="right">12.5%</td>
<td align="right">380</td>
<td align="right">22.9%</td>
<td align="right">216.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
</details>
</td>
<td align="right">20</td>
<td align="right">1.1%</td>
<td align="right">60</td>
<td align="right">2.1%</td>
<td align="right">200.0%</td>
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
<td align="right">1.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">960</td>
<td align="right">53.3%</td>
<td align="right">1,660</td>
<td align="right">58.9%</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,800</td>
<td align="right"></td>
<td align="right">2,820</td>
<td align="right"></td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">740</td>
<td align="right">41.1%</td>
<td align="right">820</td>
<td align="right">29.1%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,561,852,120</td>
<td align="right">16,298.7%</td>
<td align="right">2,775,971,520</td>
<td align="right">4,696.8%</td>
<td align="right">8.4%</td>
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
<td align="right">960</td>
<td align="right"></td>
<td align="right">1,660</td>
<td align="right"></td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">640</td>
<td align="right">66.7%</td>
<td align="right">1,040</td>
<td align="right">62.7%</td>
<td align="right">62.5%</td>
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
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">13,765,240</td>
<td align="right">89.9%</td>
<td align="right">27,751,160</td>
<td align="right">91.8%</td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">282,720</td>
<td align="right">1.8%</td>
<td align="right">558,880</td>
<td align="right">1.8%</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">15,319,040</td>
<td align="right"></td>
<td align="right">30,228,480</td>
<td align="right"></td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">1,271,080</td>
<td align="right">8.3%</td>
<td align="right">1,918,440</td>
<td align="right">6.3%</td>
<td align="right">50.9%</td>
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
<td align="right">409,600</td>
<td align="right">1.4%</td>
<td align="right">409,600 / 0 !!</td>
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
<td align="left">140</td>
<td align="right">21.9%</td>
<td align="left">160</td>
<td align="right">15.4%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">80</td>
<td align="right">12.5%</td>
<td align="left">180</td>
<td align="right">17.3%</td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">120</td>
<td align="right">18.8%</td>
<td align="left">200</td>
<td align="right">19.2%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">180</td>
<td align="right">28.1%</td>
<td align="left">200</td>
<td align="right">19.2%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="left">120</td>
<td align="right">11.5%</td>
<td align="right">120 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">120</td>
<td align="right">18.8%</td>
<td align="left">180</td>
<td align="right">17.3%</td>
<td align="right">50.0%</td>
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
<td align="right">2.1%</td>
<td align="right">20</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">40</td>
<td align="right">4.2%</td>
<td align="right">40</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">100</td>
<td align="right">10.4%</td>
<td align="right">140</td>
<td align="right">8.4%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">100</td>
<td align="right">10.4%</td>
<td align="right">140</td>
<td align="right">8.4%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">280</td>
<td align="right">29.2%</td>
<td align="right">480</td>
<td align="right">28.9%</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">160</td>
<td align="right">16.7%</td>
<td align="right">180</td>
<td align="right">10.8%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">2.1%</td>
<td align="right">60</td>
<td align="right">3.6%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">240</td>
<td align="right">25.0%</td>
<td align="right">600</td>
<td align="right">36.1%</td>
<td align="right">150.0%</td>
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
<td align="right">6.2%</td>
<td align="right">60</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
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
<td align="right">140</td>
<td align="right">14.6%</td>
<td align="right">200</td>
<td align="right">12.0%</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">140</td>
<td align="right">14.6%</td>
<td align="right">220</td>
<td align="right">13.3%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">18.8%</td>
<td align="right">260</td>
<td align="right">15.7%</td>
<td align="right">44.4%</td>
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
<td align="right">120</td>
<td align="right">12.5%</td>
<td align="right">300</td>
<td align="right">18.1%</td>
<td align="right">150.0%</td>
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
<td align="left">_START_EXECUTOR</td>
<td align="right">15,718,120</td>
<td align="right">59,103,480</td>
<td align="right">276.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">15,718,120</td>
<td align="right">59,103,200</td>
<td align="right">276.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">326,460</td>
<td align="right">643,320</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">326,460</td>
<td align="right">643,320</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">19,430,800</td>
<td align="right">948,600</td>
<td align="right">-95.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">323,140</td>
<td align="right">630,080</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">214,160</td>
<td align="right">373,800</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">214,160</td>
<td align="right">373,800</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">108,980</td>
<td align="right">188,820</td>
<td align="right">73.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">108,980</td>
<td align="right">188,820</td>
<td align="right">73.3%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">35,148,920</td>
<td align="right">60,052,080</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">399,180</td>
<td align="right">598,620</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">399,180</td>
<td align="right">598,620</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">399,180</td>
<td align="right">598,620</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">381,320</td>
<td align="right">556,840</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">867,820</td>
<td align="right">1,231,820</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">63,334,100</td>
<td align="right">89,291,580</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,834,800</td>
<td align="right">1,109,360</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">2,639,740</td>
<td align="right">3,348,180</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">890,580</td>
<td align="right">1,120,740</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,258,020</td>
<td align="right">1,579,800</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,258,020</td>
<td align="right">1,579,800</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">593,720</td>
<td align="right">742,880</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">296,860</td>
<td align="right">371,440</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">307,860</td>
<td align="right">384,720</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">750,300</td>
<td align="right">935,640</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">307,520</td>
<td align="right">382,960</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,043,060</td>
<td align="right">1,298,360</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,043,060</td>
<td align="right">1,298,360</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,043,060</td>
<td align="right">1,298,360</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,043,060</td>
<td align="right">1,298,360</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">3,769,560</td>
<td align="right">4,612,460</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">496,380</td>
<td align="right">605,860</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,372,640</td>
<td align="right">2,874,980</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">572,240</td>
<td align="right">682,880</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,763,320</td>
<td align="right">3,281,900</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,706,560</td>
<td align="right">2,019,100</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">1,818,940</td>
<td align="right">2,052,480</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">4,109,100</td>
<td align="right">4,599,160</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">272,340</td>
<td align="right">301,180</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">4,012,520</td>
<td align="right">4,366,060</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">4,012,520</td>
<td align="right">4,366,060</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,591,080</td>
<td align="right">1,722,380</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,591,080</td>
<td align="right">1,721,760</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,591,080</td>
<td align="right">1,721,760</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">8,643,180</td>
<td align="right">9,286,680</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">1,591,080</td>
<td align="right">1,697,960</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,591,080</td>
<td align="right">1,697,960</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">1,591,080</td>
<td align="right">1,697,960</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">25,458,500</td>
<td align="right">26,931,140</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">29,378,940</td>
<td align="right">30,976,700</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">42,850,060</td>
<td align="right">44,850,420</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">27,534,860</td>
<td align="right">28,776,700</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">42,103,860</td>
<td align="right">43,938,320</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">42,103,860</td>
<td align="right">43,938,320</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">353,626,600</td>
<td align="right">368,571,740</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">422,501,120</td>
<td align="right">439,989,300</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">135,249,920</td>
<td align="right">140,422,440</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">135,249,920</td>
<td align="right">140,422,440</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">48,997,640</td>
<td align="right">50,686,240</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">22,918,940</td>
<td align="right">23,703,380</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">46,736,560</td>
<td align="right">48,307,060</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">23,827,500</td>
<td align="right">24,619,460</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">23,827,500</td>
<td align="right">24,619,460</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">23,827,500</td>
<td align="right">24,619,460</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">45,199,280</td>
<td align="right">46,693,980</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">23,978,060</td>
<td align="right">24,717,220</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">23,824,800</td>
<td align="right">24,553,740</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">64,827,420</td>
<td align="right">66,774,920</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">64,827,420</td>
<td align="right">66,774,920</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">64,827,420</td>
<td align="right">66,774,920</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">64,827,420</td>
<td align="right">66,774,920</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">140,037,100</td>
<td align="right">144,202,920</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">64,835,460</td>
<td align="right">66,694,820</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">64,835,460</td>
<td align="right">66,694,820</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">64,835,460</td>
<td align="right">66,694,820</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">64,059,240</td>
<td align="right">65,706,420</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">63,569,400</td>
<td align="right">65,195,120</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">63,034,060</td>
<td align="right">64,540,920</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">26,316,320</td>
<td align="right">26,580,140</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right"></td>
<td align="right">38,620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right"></td>
<td align="right">620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">280</td>
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
<td align="right">20</td>
<td align="right">60</td>
<td align="right">200.0%</td>
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
