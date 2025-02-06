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
<td align="left">NOT_TAKEN</td>
<td align="right">24,570</td>
<td align="right">438,808</td>
<td align="right">1,686.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,276,834</td>
<td align="right">9,979,158</td>
<td align="right">681.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,305,196</td>
<td align="right">9,579,159</td>
<td align="right">633.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">665,617</td>
<td align="right">2,189,511</td>
<td align="right">228.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">677,777</td>
<td align="right">2,201,671</td>
<td align="right">224.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">310,437</td>
<td align="right">836,997</td>
<td align="right">169.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,644,531</td>
<td align="right">6,684,971</td>
<td align="right">152.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">373,141</td>
<td align="right">885,335</td>
<td align="right">137.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,490,551</td>
<td align="right">3,240,828</td>
<td align="right">117.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">690,853</td>
<td align="right">1,187,674</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,252,506</td>
<td align="right">1,991,083</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">24,810,443</td>
<td align="right">35,931,338</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">55,584,134</td>
<td align="right">68,672,952</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">55,590,790</td>
<td align="right">68,679,608</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">36,704,333</td>
<td align="right">44,018,556</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,221,017</td>
<td align="right">1,448,193</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,618,802</td>
<td align="right">1,916,986</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">48,081,605</td>
<td align="right">55,385,166</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">66,271,307</td>
<td align="right">75,443,901</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">113,197,572</td>
<td align="right">125,374,875</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">14,398,914</td>
<td align="right">15,928,564</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">172,106,606</td>
<td align="right">185,583,903</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">28,910,491</td>
<td align="right">31,071,524</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">29,488,790</td>
<td align="right">31,253,151</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">24,985,057</td>
<td align="right">26,341,765</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">43,067,443</td>
<td align="right">44,939,222</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">7,813,833</td>
<td align="right">8,137,031</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">13,020,222</td>
<td align="right">13,286,157</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">12,486,313</td>
<td align="right">12,716,010</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">31,393,876</td>
<td align="right">31,928,818</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">26,627,923</td>
<td align="right">27,037,353</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">66,767,464</td>
<td align="right">67,769,421</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">108,331,242</td>
<td align="right">108,962,492</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">798,768</td>
<td align="right">800,094</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">7,042,692</td>
<td align="right">7,052,918</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">7,626,756</td>
<td align="right">7,630,277</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,834,700</td>
<td align="right">6,836,895</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">13,368,384</td>
<td align="right">13,370,579</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,394,998</td>
<td align="right">13,397,193</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">545,557</td>
<td align="right">545,597</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">28,468,541</td>
<td align="right">28,469,873</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">121,028,139</td>
<td align="right">121,030,334</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">219,391</td>
<td align="right">219,393</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">31,706,142</td>
<td align="right">31,706,142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">6,838,949</td>
<td align="right">6,838,949</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">6,798,742</td>
<td align="right">6,798,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">6,723,524</td>
<td align="right">6,723,524</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,716,798</td>
<td align="right">6,716,798</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,280,317</td>
<td align="right">1,280,317</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">640,000</td>
<td align="right">640,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">451,385</td>
<td align="right">451,385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">262,143</td>
<td align="right">262,143</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">233,458</td>
<td align="right">233,458</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">193,273</td>
<td align="right">193,273</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">143,872</td>
<td align="right">143,872</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">131,072</td>
<td align="right">131,072</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">130,980</td>
<td align="right">130,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">80,305</td>
<td align="right">80,305</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">15,233</td>
<td align="right">15,233</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">13,976</td>
<td align="right">13,976</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">12,159</td>
<td align="right">12,159</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,905</td>
<td align="right">6,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,610</td>
<td align="right">2,610</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,351</td>
<td align="right">2,351</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,658</td>
<td align="right">1,658</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">648</td>
<td align="right">648</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">648</td>
<td align="right">648</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">638</td>
<td align="right">638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">612</td>
<td align="right">612</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">549</td>
<td align="right">549</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">378</td>
<td align="right">378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">378</td>
<td align="right">378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">324</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">324</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">324</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">324</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">324</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">324</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">324</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">324</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">324</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">324</td>
<td align="right">324</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">319</td>
<td align="right">319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">319</td>
<td align="right">319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">319</td>
<td align="right">319</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">118</td>
<td align="right">118</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">67</td>
<td align="right">67</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">44</td>
<td align="right">44</td>
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
<td align="right">688,809</td>
<td align="right">0.1%</td>
<td align="right">1,185,509</td>
<td align="right">0.1%</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,040,593,274</td>
<td align="right">99.9%</td>
<td align="right">1,040,593,274</td>
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
<td align="left">Failure</td>
<td align="right">1,686</td>
<td align="right">82.5%</td>
<td align="right">1,807</td>
<td align="right">83.5%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">358</td>
<td align="right">17.5%</td>
<td align="right">358</td>
<td align="right">16.5%</td>
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
<td align="left">rshift</td>
<td align="right">23</td>
<td align="right">1.4%</td>
<td align="right">104</td>
<td align="right">5.8%</td>
<td align="right">352.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">69</td>
<td align="right">4.1%</td>
<td align="right">109</td>
<td align="right">6.0%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">459</td>
<td align="right">27.2%</td>
<td align="right">459</td>
<td align="right">25.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">442</td>
<td align="right">26.2%</td>
<td align="right">442</td>
<td align="right">24.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">263</td>
<td align="right">15.6%</td>
<td align="right">263</td>
<td align="right">14.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">167</td>
<td align="right">9.9%</td>
<td align="right">167</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">147</td>
<td align="right">8.7%</td>
<td align="right">147</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">116</td>
<td align="right">6.9%</td>
<td align="right">116</td>
<td align="right">6.4%</td>
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
<td align="right">66,254,589</td>
<td align="right">29.3%</td>
<td align="right">75,424,982</td>
<td align="right">32.0%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">160,069,292</td>
<td align="right">70.7%</td>
<td align="right">160,069,292</td>
<td align="right">68.0%</td>
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
<td align="right">16,594</td>
<td align="right">99.3%</td>
<td align="right">18,795</td>
<td align="right">99.3%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">124</td>
<td align="right">0.7%</td>
<td align="right">124</td>
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
<td align="left">array int</td>
<td align="right">16,573</td>
<td align="right">99.9%</td>
<td align="right">18,774</td>
<td align="right">99.9%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
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
<td align="right">155</td>
<td align="right">0.0%</td>
<td align="right">155</td>
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
<td align="right">137,064,892</td>
<td align="right">100.0%</td>
<td align="right">137,064,892</td>
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
<td align="right">2,455</td>
<td align="right">100.0%</td>
<td align="right">2,455</td>
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
<td align="right">798,409</td>
<td align="right">0.4%</td>
<td align="right">799,735</td>
<td align="right">0.4%</td>
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
<td align="right">201,201,350</td>
<td align="right">99.6%</td>
<td align="right">201,201,350</td>
<td align="right">99.6%</td>
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
<td align="right">86</td>
<td align="right">24.0%</td>
<td align="right">86</td>
<td align="right">24.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">273</td>
<td align="right">76.0%</td>
<td align="right">273</td>
<td align="right">76.0%</td>
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
<td align="left">float long</td>
<td align="right">273</td>
<td align="right">100.0%</td>
<td align="right">273</td>
<td align="right">100.0%</td>
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
<td align="right">1,916,897</td>
<td align="right">99.6%</td>
<td align="right">10,619,221</td>
<td align="right">99.9%</td>
<td align="right">454.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,820</td>
<td align="right">0.4%</td>
<td align="right">6,820</td>
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
<td align="right">32</td>
<td align="right">37.6%</td>
<td align="right">32</td>
<td align="right">37.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">53</td>
<td align="right">62.4%</td>
<td align="right">53</td>
<td align="right">62.4%</td>
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
<td align="left">zip</td>
<td align="right">47</td>
<td align="right">88.7%</td>
<td align="right">47</td>
<td align="right">88.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6</td>
<td align="right">11.3%</td>
<td align="right">6</td>
<td align="right">11.3%</td>
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
<td align="right">467</td>
<td align="right">0.0%</td>
<td align="right">467</td>
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
<td align="right">350,823,329</td>
<td align="right">100.0%</td>
<td align="right">350,823,329</td>
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
<td align="right">1,778</td>
<td align="right">94.4%</td>
<td align="right">1,778</td>
<td align="right">94.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">106</td>
<td align="right">5.6%</td>
<td align="right">106</td>
<td align="right">5.6%</td>
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
<td align="right">2,877,989</td>
<td align="right">99.9%</td>
<td align="right">6,918,429</td>
<td align="right">100.0%</td>
<td align="right">140.4%</td>
</tr>
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
<td align="right">109</td>
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
<td align="right">1,549</td>
<td align="right">100.0%</td>
<td align="right">1,549</td>
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
<td align="right">36</td>
<td align="right">0.0%</td>
<td align="right">36</td>
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
<td align="right">27,144,220</td>
<td align="right">100.0%</td>
<td align="right">27,144,220</td>
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
<td align="right">576</td>
<td align="right">100.0%</td>
<td align="right">576</td>
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
<td align="right">36,694,845</td>
<td align="right">99.9%</td>
<td align="right">44,007,323</td>
<td align="right">99.9%</td>
<td align="right">19.9%</td>
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
<td align="right">12,159</td>
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
<td align="left">Failure</td>
<td align="right">9,487</td>
<td align="right">100.0%</td>
<td align="right">11,232</td>
<td align="right">100.0%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="left">array int</td>
<td align="right">7,663</td>
<td align="right">80.8%</td>
<td align="right">9,408</td>
<td align="right">83.8%</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">1,756</td>
<td align="right">18.5%</td>
<td align="right">1,756</td>
<td align="right">15.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.7%</td>
<td align="right">68</td>
<td align="right">0.6%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">334</td>
<td align="right">0.0%</td>
<td align="right">334</td>
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
<td align="right">77,931,642</td>
<td align="right">100.0%</td>
<td align="right">77,931,642</td>
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
<td align="right">110</td>
<td align="right">51.2%</td>
<td align="right">110</td>
<td align="right">51.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">105</td>
<td align="right">48.8%</td>
<td align="right">105</td>
<td align="right">48.8%</td>
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
<td align="right">105</td>
<td align="right">100.0%</td>
<td align="right">105</td>
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
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
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
<td align="right">37,526,075</td>
<td align="right">100.0%</td>
<td align="right">37,526,075</td>
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
<td align="right">109</td>
<td align="right">100.0%</td>
<td align="right">109</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,142</td>
<td align="right">0.0%</td>
<td align="right">9,575</td>
<td align="right">0.0%</td>
<td align="right">738.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">104,480,064</td>
<td align="right">8.3%</td>
<td align="right">121,465,028</td>
<td align="right">8.8%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">359,924,933</td>
<td align="right">28.7%</td>
<td align="right">401,503,114</td>
<td align="right">29.0%</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">790,506,999</td>
<td align="right">63.0%</td>
<td align="right">859,812,639</td>
<td align="right">62.2%</td>
<td align="right">8.8%</td>
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
<td align="right">688,809</td>
<td align="right">0.7%</td>
<td align="right">1,185,509</td>
<td align="right">1.0%</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">36,694,845</td>
<td align="right">35.1%</td>
<td align="right">44,007,323</td>
<td align="right">36.2%</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">66,254,589</td>
<td align="right">63.4%</td>
<td align="right">75,424,982</td>
<td align="right">62.1%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">798,409</td>
<td align="right">0.8%</td>
<td align="right">799,735</td>
<td align="right">0.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,820</td>
<td align="right">0.0%</td>
<td align="right">6,820</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">467</td>
<td align="right">0.0%</td>
<td align="right">467</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">334</td>
<td align="right">0.0%</td>
<td align="right">334</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">155</td>
<td align="right">0.0%</td>
<td align="right">155</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">109</td>
<td align="right">0.0%</td>
<td align="right">109</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">36</td>
<td align="right">0.0%</td>
<td align="right">36</td>
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
<td align="left">RESUME_CHECK</td>
<td align="right">1,142</td>
<td align="right">50.0%</td>
<td align="right">9,575</td>
<td align="right">50.0%</td>
<td align="right">738.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,142</td>
<td align="right">50.0%</td>
<td align="right">9,575</td>
<td align="right">50.0%</td>
<td align="right">738.4%</td>
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
<td align="left">GET_ITER</td>
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
<td align="left">POP_ITER</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">6,799,066</td>
<td align="right">4.5%</td>
<td align="right">6,799,066</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">145,560,134</td>
<td align="right">95.5%</td>
<td align="right">145,560,134</td>
<td align="right">95.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">6,799,066</td>
<td align="right">4.5%</td>
<td align="right">6,799,066</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,799,065</td>
<td align="right">4.5%</td>
<td align="right">6,799,065</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">6,799,065</td>
<td align="right">4.5%</td>
<td align="right">6,799,065</td>
<td align="right">4.5%</td>
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
<td align="right">6,798,735</td>
<td align="right">4.5%</td>
<td align="right">6,798,735</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">324</td>
<td align="right">0.0%</td>
<td align="right">324</td>
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
<td align="right">151,719,514</td>
<td align="right">99.6%</td>
<td align="right">151,719,514</td>
<td align="right">99.6%</td>
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
<td align="right">468</td>
<td align="right">0.0%</td>
<td align="right">576</td>
<td align="right">0.0%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">13,064</td>
<td align="right">0.0%</td>
<td align="right">15,413</td>
<td align="right">0.0%</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">530,145,412</td>
<td align="right">10.0%</td>
<td align="right">581,297,284</td>
<td align="right">11.1%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">880,990,124</td>
<td align="right">12.2%</td>
<td align="right">937,082,954</td>
<td align="right">13.0%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">289,117,706</td>
<td align="right">5.5%</td>
<td align="right">299,343,788</td>
<td align="right">5.7%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">256</td>
<td align="right"></td>
<td align="right">265</td>
<td align="right"></td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">461,965,748</td>
<td align="right">6.4%</td>
<td align="right">476,327,829</td>
<td align="right">6.6%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">3,185,555,591</td>
<td align="right">60.3%</td>
<td align="right">3,103,025,089</td>
<td align="right">59.1%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">3,977,577,497</td>
<td align="right">54.9%</td>
<td align="right">3,890,159,776</td>
<td align="right">53.9%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">105</td>
<td align="right"></td>
<td align="right">106</td>
<td align="right"></td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">238</td>
<td align="right"></td>
<td align="right">236</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,927,139,451</td>
<td align="right">26.6%</td>
<td align="right">1,913,402,761</td>
<td align="right">26.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,277,189,435</td>
<td align="right">24.2%</td>
<td align="right">1,269,229,038</td>
<td align="right">24.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,302</td>
<td align="right"></td>
<td align="right">2,304</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,465,690</td>
<td align="right"></td>
<td align="right">16,470,225</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,465,795</td>
<td align="right">1.4%</td>
<td align="right">16,468,377</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">1,126,442,918</td>
<td align="right"></td>
<td align="right">1,126,494,085</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">1,126,443,181</td>
<td align="right">98.6%</td>
<td align="right">1,126,494,348</td>
<td align="right">98.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">70,537,383</td>
<td align="right"></td>
<td align="right">70,539,583</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">16,452,263</td>
<td align="right">1.4%</td>
<td align="right">16,452,388</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">384</td>
<td align="right"></td>
<td align="right">384</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">331</td>
<td align="right">1.2%</td>
<td align="right">2,657</td>
<td align="right">9.4%</td>
<td align="right">702.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">188,716,203</td>
<td align="right"></td>
<td align="right">156,705,331</td>
<td align="right"></td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">26,521</td>
<td align="right"></td>
<td align="right">28,273</td>
<td align="right"></td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">13,115,478,911</td>
<td align="right">6,949.8%</td>
<td align="right">12,784,955,667</td>
<td align="right">8,158.6%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">26,190</td>
<td align="right">98.8%</td>
<td align="right">25,616</td>
<td align="right">90.6%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">26,262</td>
<td align="right">99.0%</td>
<td align="right">25,789</td>
<td align="right">91.2%</td>
<td align="right">-1.8%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">331</td>
<td align="right"></td>
<td align="right">2,657</td>
<td align="right"></td>
<td align="right">702.7%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">331</td>
<td align="right">100.0%</td>
<td align="right">2,657</td>
<td align="right">100.0%</td>
<td align="right">702.7%</td>
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
<td align="right">232,024</td>
<td align="right">9.8%</td>
<td align="right">3,540,848</td>
<td align="right">11.7%</td>
<td align="right">1,426.1%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">1,321,222</td>
<td align="right">55.8%</td>
<td align="right">20,027,804</td>
<td align="right">66.4%</td>
<td align="right">1,415.9%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">2,367,488</td>
<td align="right"></td>
<td align="right">30,183,424</td>
<td align="right"></td>
<td align="right">1,174.9%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">3,284,992</td>
<td align="right">138.8%</td>
<td align="right">29,745,152</td>
<td align="right">98.5%</td>
<td align="right">805.5%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">814,242</td>
<td align="right">34.4%</td>
<td align="right">6,614,772</td>
<td align="right">21.9%</td>
<td align="right">712.4%</td>
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
<td align="left">133</td>
<td align="right">40.2%</td>
<td align="left">298</td>
<td align="right">10.2%</td>
<td align="right">124.1%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">183</td>
<td align="right">55.3%</td>
<td align="left">2,221</td>
<td align="right">76.2%</td>
<td align="right">1,113.7%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">7</td>
<td align="right">2.1%</td>
<td align="left">258</td>
<td align="right">8.9%</td>
<td align="right">3,585.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">7</td>
<td align="right">2.1%</td>
<td align="left">49</td>
<td align="right">1.7%</td>
<td align="right">600.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1</td>
<td align="right">0.3%</td>
<td align="left">44</td>
<td align="right">1.5%</td>
<td align="right">4,300.0%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">43</td>
<td align="right">1.5%</td>
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
<td align="right">66</td>
<td align="right">19.9%</td>
<td align="right">127</td>
<td align="right">4.8%</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">67</td>
<td align="right">20.2%</td>
<td align="right">171</td>
<td align="right">6.4%</td>
<td align="right">155.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">180</td>
<td align="right">54.4%</td>
<td align="right">2,007</td>
<td align="right">75.5%</td>
<td align="right">1,015.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">7</td>
<td align="right">2.1%</td>
<td align="right">236</td>
<td align="right">8.9%</td>
<td align="right">3,271.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7</td>
<td align="right">2.1%</td>
<td align="right">112</td>
<td align="right">4.2%</td>
<td align="right">1,500.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3</td>
<td align="right">0.9%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1</td>
<td align="right">0.3%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">2</td>
<td align="right">0.6%</td>
<td align="right">63</td>
<td align="right">2.4%</td>
<td align="right">3,050.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">128</td>
<td align="right">38.7%</td>
<td align="right">128</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">68</td>
<td align="right">20.5%</td>
<td align="right">192</td>
<td align="right">7.2%</td>
<td align="right">182.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">118</td>
<td align="right">35.6%</td>
<td align="right">2,053</td>
<td align="right">77.3%</td>
<td align="right">1,639.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">7</td>
<td align="right">2.1%</td>
<td align="right">193</td>
<td align="right">7.3%</td>
<td align="right">2,657.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">6</td>
<td align="right">1.8%</td>
<td align="right">26</td>
<td align="right">1.0%</td>
<td align="right">333.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2</td>
<td align="right">0.6%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
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
<td align="left">_DEOPT</td>
<td align="right">1,142</td>
<td align="right">9,681</td>
<td align="right">747.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">154,271,978</td>
<td align="right">123,254,524</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">38,715,468</td>
<td align="right">31,573,175</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">188,716,203</td>
<td align="right">156,705,331</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">1,486,525</td>
<td align="right">1,261,218</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">71,591,571</td>
<td align="right">64,266,383</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">7,941,421</td>
<td align="right">7,414,821</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">7,762,746</td>
<td align="right">7,250,552</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">205,016,186</td>
<td align="right">191,927,368</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">205,016,186</td>
<td align="right">191,927,368</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">142,929,046</td>
<td align="right">134,247,854</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">142,275,068</td>
<td align="right">133,960,743</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">151,046,853</td>
<td align="right">142,344,529</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">151,046,853</td>
<td align="right">142,344,529</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">170,662,491</td>
<td align="right">161,651,971</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">142,873,732</td>
<td align="right">135,568,852</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">14,534,334</td>
<td align="right">13,896,353</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">166,639,104</td>
<td align="right">159,326,626</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">281,161,840</td>
<td align="right">270,062,393</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">27,673,417</td>
<td align="right">26,671,460</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">27,673,417</td>
<td align="right">26,671,460</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">20,521,360</td>
<td align="right">19,782,783</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">207,635,986</td>
<td align="right">200,332,425</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">84,491,068</td>
<td align="right">81,974,522</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">84,491,068</td>
<td align="right">81,974,522</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">34,443,083</td>
<td align="right">33,441,126</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">71,083,364</td>
<td align="right">69,039,460</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">84,203,837</td>
<td align="right">81,941,366</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">18,753,058</td>
<td align="right">18,266,414</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">1,647,884,725</td>
<td align="right">1,606,197,956</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">63,682,477</td>
<td align="right">62,158,583</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">63,682,477</td>
<td align="right">62,158,583</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">76,441,091</td>
<td align="right">74,690,814</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">1,474,525,662</td>
<td align="right">1,441,800,450</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">429,171,579</td>
<td align="right">420,001,186</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">576,638,406</td>
<td align="right">565,718,589</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">111,884,798</td>
<td align="right">109,937,431</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">92,445,637</td>
<td align="right">90,948,017</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">65,134,458</td>
<td align="right">64,130,306</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">32,473,625</td>
<td align="right">31,976,925</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">121,415,566</td>
<td align="right">119,662,311</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">107,269,922</td>
<td align="right">105,750,900</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">44,696,923</td>
<td align="right">44,084,087</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">6,536,709</td>
<td align="right">6,454,847</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">19,149,254</td>
<td align="right">18,922,078</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">25,525,418</td>
<td align="right">25,227,234</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">25,525,418</td>
<td align="right">25,227,234</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">25,525,418</td>
<td align="right">25,227,234</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">190,755,147</td>
<td align="right">188,699,404</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">353,358,316</td>
<td align="right">350,064,443</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">36,590,633</td>
<td align="right">36,267,435</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">391,439,833</td>
<td align="right">388,006,328</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">110,459,950</td>
<td align="right">109,515,028</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">200,756,961</td>
<td align="right">199,189,336</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">250,318,852</td>
<td align="right">248,554,491</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">250,318,852</td>
<td align="right">248,554,491</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">12,616,495</td>
<td align="right">12,534,633</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">12,958,254</td>
<td align="right">12,876,391</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">84,250,029</td>
<td align="right">83,763,380</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">959,654,833</td>
<td align="right">954,590,227</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">269,790,363</td>
<td align="right">268,433,655</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">214,020,658</td>
<td align="right">213,024,779</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">56,232,375</td>
<td align="right">56,003,004</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">56,232,375</td>
<td align="right">56,003,004</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">56,603,158</td>
<td align="right">56,373,254</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">149,788,874</td>
<td align="right">149,253,932</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">25,545,893</td>
<td align="right">25,472,766</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">167,856,629</td>
<td align="right">167,447,199</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">145,192,011</td>
<td align="right">144,978,345</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">187,412,396</td>
<td align="right">187,143,387</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">106,125,182</td>
<td align="right">106,046,338</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">215,430,382</td>
<td align="right">215,329,516</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">12,779,089</td>
<td align="right">12,777,763</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">105,451,312</td>
<td align="right">105,441,086</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">30,691,375</td>
<td align="right">30,689,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">30,691,375</td>
<td align="right">30,689,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">30,691,375</td>
<td align="right">30,689,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">30,691,375</td>
<td align="right">30,689,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">30,691,375</td>
<td align="right">30,689,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">49,862,210</td>
<td align="right">49,858,689</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">37,083,121</td>
<td align="right">37,080,926</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">37,083,121</td>
<td align="right">37,080,926</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">37,083,121</td>
<td align="right">37,080,926</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">37,083,121</td>
<td align="right">37,080,926</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">123,470,197</td>
<td align="right">123,468,865</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">12,843,090</td>
<td align="right">12,843,088</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">71,691,957</td>
<td align="right">71,691,954</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">6,453,866</td>
<td align="right">6,453,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">6,391,746</td>
<td align="right">6,391,746</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">6,391,746</td>
<td align="right">6,391,746</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">377,920</td>
<td align="right">377,920</td>
<td align="right">0.0%</td>
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
<td align="right">105</td>
<td align="right">105</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-06
