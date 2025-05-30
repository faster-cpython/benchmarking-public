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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">40,400</td>
<td align="right">857,155</td>
<td align="right">2,021.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">357,201</td>
<td align="right">1,230,845</td>
<td align="right">244.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">357,264</td>
<td align="right">1,230,908</td>
<td align="right">244.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,237,872</td>
<td align="right">2,985,228</td>
<td align="right">141.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,238,187</td>
<td align="right">2,985,543</td>
<td align="right">141.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">13,360</td>
<td align="right">29,629</td>
<td align="right">121.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">27,008</td>
<td align="right">59,370</td>
<td align="right">119.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">13,452</td>
<td align="right">29,545</td>
<td align="right">119.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">20,083,649</td>
<td align="right">759,772</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">20,083,722</td>
<td align="right">759,845</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">17,582</td>
<td align="right">33,851</td>
<td align="right">92.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">42,538,725</td>
<td align="right">3,875,926</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">45,822</td>
<td align="right">86,870</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">132,497,618</td>
<td align="right">24,664,160</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">26,198,863</td>
<td align="right">7,109,903</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">19,194,826</td>
<td align="right">6,498,819</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">136,104,910</td>
<td align="right">59,746,794</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">239,219,997</td>
<td align="right">139,594,261</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">187,032,339</td>
<td align="right">125,006,977</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,616,812</td>
<td align="right">1,143,417</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">350,073,335</td>
<td align="right">249,053,592</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">449,363,414</td>
<td align="right">339,602,415</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">128,292,747</td>
<td align="right">97,237,316</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">263,566,205</td>
<td align="right">201,529,696</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">135,474,121</td>
<td align="right">103,795,071</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">134,446,966</td>
<td align="right">103,407,783</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">992,870,180</td>
<td align="right">766,178,951</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">172,847,293</td>
<td align="right">141,808,110</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">179,501,067</td>
<td align="right">148,445,636</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">492,895,094</td>
<td align="right">430,816,728</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">831,509</td>
<td align="right">900,742</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">831,513</td>
<td align="right">900,746</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">831,513</td>
<td align="right">900,746</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">831,572</td>
<td align="right">900,805</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">831,761</td>
<td align="right">900,994</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">832,769</td>
<td align="right">902,018</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">818,584</td>
<td align="right">871,736</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,093,780</td>
<td align="right">1,163,034</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">275,820</td>
<td align="right">292,110</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">135,639,819</td>
<td align="right">137,387,149</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">233,694,058</td>
<td align="right">236,486,062</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">77,171,124</td>
<td align="right">78,061,037</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">7,204,758</td>
<td align="right">7,241,627</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">6,417,714</td>
<td align="right">6,433,983</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">79,530,699</td>
<td align="right">79,706,055</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">26,404,945</td>
<td align="right">26,441,814</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">116,036,101</td>
<td align="right">116,105,332</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">77,076,070</td>
<td align="right">77,092,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">524,672</td>
<td align="right">524,714</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">60,234,560</td>
<td align="right">60,234,770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">19,462,336</td>
<td align="right">19,462,357</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">83,200,375</td>
<td align="right">83,200,375</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">76,819,308</td>
<td align="right">76,819,308</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">76,800,256</td>
<td align="right">76,800,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">76,800,192</td>
<td align="right">76,800,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">76,800,122</td>
<td align="right">76,800,122</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">76,799,998</td>
<td align="right">76,799,998</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">76,799,996</td>
<td align="right">76,799,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">76,799,996</td>
<td align="right">76,799,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">57,600,132</td>
<td align="right">57,600,132</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">38,408,256</td>
<td align="right">38,408,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,408,192</td>
<td align="right">38,408,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">38,408,192</td>
<td align="right">38,408,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">38,399,996</td>
<td align="right">38,399,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">19,204,096</td>
<td align="right">19,204,096</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">12,800,315</td>
<td align="right">12,800,315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,400,188</td>
<td align="right">6,400,188</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">278,656</td>
<td align="right">278,656</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">924</td>
<td align="right">924</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">819</td>
<td align="right">819</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">396</td>
<td align="right">396</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">378</td>
<td align="right">378</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">138</td>
<td align="right">138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">76</td>
<td align="right">76</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">73</td>
<td align="right">73</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">30</td>
<td align="right">30</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">27</td>
<td align="right">27</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">7</td>
<td align="right">7</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">4</td>
<td align="right">4</td>
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
<td align="right">76,800,214</td>
<td align="right">31.6%</td>
<td align="right">76,800,214</td>
<td align="right">31.6%</td>
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
<td align="right">166,401,002</td>
<td align="right">68.4%</td>
<td align="right">166,401,002</td>
<td align="right">68.4%</td>
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
<td align="right">262</td>
<td align="right">1.4%</td>
<td align="right">262</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">18,832</td>
<td align="right">98.6%</td>
<td align="right">18,832</td>
<td align="right">98.6%</td>
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
<td align="right">18,811</td>
<td align="right">99.9%</td>
<td align="right">18,811</td>
<td align="right">99.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
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
<td align="right">92</td>
<td align="right">0.0%</td>
<td align="right">92</td>
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
<td align="right">2,156,802,739</td>
<td align="right">100.0%</td>
<td align="right">2,156,802,739</td>
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
<td align="right">832</td>
<td align="right">100.0%</td>
<td align="right">832</td>
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
<td align="right">2</td>
<td align="right">50.0%</td>
<td align="right">2</td>
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
<td align="right">2</td>
<td align="right">100.0%</td>
<td align="right">2</td>
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
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">8</td>
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
<td align="right">64,000,248</td>
<td align="right">100.0%</td>
<td align="right">64,000,248</td>
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
<td align="right">68</td>
<td align="right">100.0%</td>
<td align="right">68</td>
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
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
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
<td align="right">332,800,313</td>
<td align="right">100.0%</td>
<td align="right">332,800,313</td>
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
<td align="right">7</td>
<td align="right">100.0%</td>
<td align="right">7</td>
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
<td align="right">58,774</td>
<td align="right">68.1%</td>
<td align="right">894,111</td>
<td align="right">94.7%</td>
<td align="right">1,421.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">27,448</td>
<td align="right">31.8%</td>
<td align="right">49,914</td>
<td align="right">5.3%</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">132</td>
<td align="right">0.2%</td>
<td align="right">132</td>
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
<td align="right">520</td>
<td align="right">99.6%</td>
<td align="right">943</td>
<td align="right">99.8%</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.2%</td>
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
<td align="right">2</td>
<td align="right">100.0%</td>
<td align="right">2</td>
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
<td align="right">38,400,128</td>
<td align="right">38,400,128 / 0 !!</td>
<td align="right">38,400,128</td>
<td align="right">38,400,128 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">38,400,000</td>
<td align="right">38,400,000 / 0 !!</td>
<td align="right">38,400,000</td>
<td align="right">38,400,000 / 0 !!</td>
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
<td align="right">831,776</td>
<td align="right">0.1%</td>
<td align="right">901,009</td>
<td align="right">0.1%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,081,602,681</td>
<td align="right">99.9%</td>
<td align="right">1,081,602,681</td>
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
<td align="right">304</td>
<td align="right">30.6%</td>
<td align="right">320</td>
<td align="right">31.7%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">689</td>
<td align="right">69.4%</td>
<td align="right">689</td>
<td align="right">68.3%</td>
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
<td align="left">method</td>
<td align="right">262</td>
<td align="right">86.2%</td>
<td align="right">278</td>
<td align="right">86.9%</td>
<td align="right">6.1%</td>
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
<td align="right">209,668,742</td>
<td align="right">100.0%</td>
<td align="right">102,725,197</td>
<td align="right">100.0%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">68</td>
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
<td align="right">328</td>
<td align="right">100.0%</td>
<td align="right">328</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">76,799,998</td>
<td align="right">100.0%</td>
<td align="right">76,799,998</td>
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
<td align="right">2</td>
<td align="right">100.0%</td>
<td align="right">2</td>
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
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">5</td>
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
<td align="right">76,800,187</td>
<td align="right">100.0%</td>
<td align="right">76,800,187</td>
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
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">25</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">818,226</td>
<td align="right">0.1%</td>
<td align="right">871,364</td>
<td align="right">0.1%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,069,126,255</td>
<td align="right">99.9%</td>
<td align="right">1,007,015,372</td>
<td align="right">99.9%</td>
<td align="right">-5.8%</td>
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
<td align="right">279</td>
<td align="right">77.9%</td>
<td align="right">293</td>
<td align="right">78.8%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">79</td>
<td align="right">22.1%</td>
<td align="right">79</td>
<td align="right">21.2%</td>
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
<td align="left">dict</td>
<td align="right">22</td>
<td align="right">7.9%</td>
<td align="right">26</td>
<td align="right">8.9%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">215</td>
<td align="right">77.1%</td>
<td align="right">225</td>
<td align="right">76.8%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">42</td>
<td align="right">15.1%</td>
<td align="right">42</td>
<td align="right">14.3%</td>
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
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">11</td>
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
<td align="right">288,000,181</td>
<td align="right">100.0%</td>
<td align="right">288,000,181</td>
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
<td align="right">51</td>
<td align="right">100.0%</td>
<td align="right">51</td>
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
<td align="right">28,701</td>
<td align="right">0.0%</td>
<td align="right">51,141</td>
<td align="right">0.0%</td>
<td align="right">78.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,950,262,474</td>
<td align="right">33.4%</td>
<td align="right">1,480,859,095</td>
<td align="right">31.6%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,814,963,906</td>
<td align="right">65.3%</td>
<td align="right">3,123,801,810</td>
<td align="right">66.7%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">79,303,822</td>
<td align="right">1.4%</td>
<td align="right">79,495,456</td>
<td align="right">1.7%</td>
<td align="right">0.2%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">831,776</td>
<td align="right">1.1%</td>
<td align="right">901,009</td>
<td align="right">1.1%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">818,226</td>
<td align="right">1.0%</td>
<td align="right">871,364</td>
<td align="right">1.1%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">76,800,214</td>
<td align="right">97.9%</td>
<td align="right">76,800,214</td>
<td align="right">97.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">132</td>
<td align="right">0.0%</td>
<td align="right">132</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">92</td>
<td align="right">0.0%</td>
<td align="right">92</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">8</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">5</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">13,674</td>
<td align="right">45.6%</td>
<td align="right">24,920</td>
<td align="right">47.6%</td>
<td align="right">82.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,774</td>
<td align="right">46.0%</td>
<td align="right">24,994</td>
<td align="right">47.7%</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,253</td>
<td align="right">4.2%</td>
<td align="right">1,227</td>
<td align="right">2.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,253</td>
<td align="right">4.2%</td>
<td align="right">1,227</td>
<td align="right">2.3%</td>
<td align="right">-2.1%</td>
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
<td align="left">DELETE_SUBSCR</td>
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
<td align="left">FORMAT_SIMPLE</td>
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
<td align="right">57,600,260</td>
<td align="right">8.9%</td>
<td align="right">57,600,260</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">588,801,020</td>
<td align="right">91.1%</td>
<td align="right">588,801,020</td>
<td align="right">91.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">57,600,260</td>
<td align="right">8.9%</td>
<td align="right">57,600,260</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">57,600,260</td>
<td align="right">8.9%</td>
<td align="right">57,600,260</td>
<td align="right">8.9%</td>
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
<td align="right">57,600,260</td>
<td align="right">8.9%</td>
<td align="right">57,600,260</td>
<td align="right">8.9%</td>
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
<td align="right">19,200,000</td>
<td align="right">3.0%</td>
<td align="right">19,200,000</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
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
<td align="right">38,400,000</td>
<td align="right">5.9%</td>
<td align="right">38,400,000</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
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
<td align="right">64</td>
<td align="right">0.0%</td>
<td align="right">64</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">723,201,276</td>
<td align="right">111.9%</td>
<td align="right">723,201,276</td>
<td align="right">111.9%</td>
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
<td align="right">401</td>
<td align="right">0.0%</td>
<td align="right">477</td>
<td align="right">0.0%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,147,265,599</td>
<td align="right">15.4%</td>
<td align="right">1,000,167,196</td>
<td align="right">13.5%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">80</td>
<td align="right"></td>
<td align="right">73</td>
<td align="right"></td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">71</td>
<td align="right"></td>
<td align="right">65</td>
<td align="right"></td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">19</td>
<td align="right"></td>
<td align="right">18</td>
<td align="right"></td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,146,376,126</td>
<td align="right">38.4%</td>
<td align="right">2,995,660,852</td>
<td align="right">36.7%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">4,061,079,307</td>
<td align="right">49.6%</td>
<td align="right">4,180,073,573</td>
<td align="right">51.2%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,528,758,236</td>
<td align="right">20.5%</td>
<td align="right">1,490,353,384</td>
<td align="right">20.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">4,684,182,652</td>
<td align="right">62.8%</td>
<td align="right">4,799,553,465</td>
<td align="right">65.0%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">96,831,702</td>
<td align="right">1.3%</td>
<td align="right">96,900,935</td>
<td align="right">1.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">678,406,543</td>
<td align="right"></td>
<td align="right">678,413,043</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">678,406,754</td>
<td align="right">48.6%</td>
<td align="right">678,413,254</td>
<td align="right">48.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">985,607,396</td>
<td align="right">12.0%</td>
<td align="right">985,606,948</td>
<td align="right">12.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">96,001,281</td>
<td align="right"></td>
<td align="right">96,001,303</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">812,801,418</td>
<td align="right"></td>
<td align="right">812,801,547</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">716,801,576</td>
<td align="right">51.4%</td>
<td align="right">716,801,656</td>
<td align="right">51.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">518,400,449</td>
<td align="right"></td>
<td align="right">518,400,450</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">716,801,175</td>
<td align="right">51.4%</td>
<td align="right">716,801,175</td>
<td align="right">51.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">4 / 0 !!</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (str subclass)</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">446,919,394</td>
<td align="right"></td>
<td align="right">281,101,994</td>
<td align="right"></td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">32,814</td>
<td align="right">99.4%</td>
<td align="right">25,044</td>
<td align="right">99.1%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">33,023</td>
<td align="right"></td>
<td align="right">25,265</td>
<td align="right"></td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">209</td>
<td align="right">0.6%</td>
<td align="right">221</td>
<td align="right">0.9%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">36,702,226,883</td>
<td align="right">8,212.3%</td>
<td align="right">38,578,593,371</td>
<td align="right">13,724.1%</td>
<td align="right">5.1%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
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
<td align="right">209</td>
<td align="right"></td>
<td align="right">221</td>
<td align="right"></td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">209</td>
<td align="right">100.0%</td>
<td align="right">221</td>
<td align="right">100.0%</td>
<td align="right">5.7%</td>
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
<td align="right">7,540,863</td>
<td align="right">90.4%</td>
<td align="right">15,173,879</td>
<td align="right">95.0%</td>
<td align="right">101.2%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">40,960</td>
<td align="right">0.5%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">8,339,456</td>
<td align="right"></td>
<td align="right">15,966,208</td>
<td align="right"></td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">168,296</td>
<td align="right">2.0%</td>
<td align="right">307,904</td>
<td align="right">1.9%</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">630,297</td>
<td align="right">7.6%</td>
<td align="right">484,425</td>
<td align="right">3.0%</td>
<td align="right">-23.1%</td>
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
<td align="left"><= 32,768</td>
<td align="left">133</td>
<td align="right">63.6%</td>
<td align="left">71</td>
<td align="right">24.6%</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">76</td>
<td align="right">36.4%</td>
<td align="left">146</td>
<td align="right">50.5%</td>
<td align="right">92.1%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">4</td>
<td align="right">1.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">68</td>
<td align="right">23.5%</td>
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
<td align="left"><= 256</td>
<td align="right">127</td>
<td align="right">60.8%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">14</td>
<td align="right">6.7%</td>
<td align="right">213</td>
<td align="right">96.4%</td>
<td align="right">1,421.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">68</td>
<td align="right">32.5%</td>
<td align="right">4</td>
<td align="right">1.8%</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">4</td>
<td align="right">1.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="left"><= 256</td>
<td align="right">141</td>
<td align="right">67.5%</td>
<td align="right">213</td>
<td align="right">96.4%</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">68</td>
<td align="right">32.5%</td>
<td align="right">4</td>
<td align="right">1.8%</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">4</td>
<td align="right">1.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="left">_JUMP_TO_TOP</td>
<td align="right">38,394,994</td>
<td align="right">287,115,735</td>
<td align="right">647.8%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">446,918,077</td>
<td align="right">281,100,678</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">446,919,394</td>
<td align="right">281,101,994</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">70,380,594</td>
<td align="right">89,518,526</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">230,306,182</td>
<td align="right">292,384,548</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">115,153,091</td>
<td align="right">146,192,274</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">115,153,091</td>
<td align="right">146,192,274</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">153,568,018</td>
<td align="right">191,076,360</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">280,167,839</td>
<td align="right">342,193,201</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">95,985,894</td>
<td align="right">114,347,938</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">598,818,178</td>
<td align="right">713,136,397</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">108,775,718</td>
<td align="right">127,913,650</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">178,072,860</td>
<td align="right">209,059,058</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">485,314,388</td>
<td align="right">568,217,729</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">382,367,715</td>
<td align="right">445,256,756</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">134,381,344</td>
<td align="right">152,743,388</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">510,998,641</td>
<td align="right">572,150,394</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">165,801,951</td>
<td align="right">184,890,911</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">165,801,951</td>
<td align="right">184,890,911</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">210,316,534</td>
<td align="right">229,640,411</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">210,316,534</td>
<td align="right">229,640,411</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">210,316,534</td>
<td align="right">229,640,411</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,006,018,078</td>
<td align="right">1,097,915,752</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">210,869,485</td>
<td align="right">229,712,403</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">216,454,326</td>
<td align="right">235,778,182</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">1,190,662,411</td>
<td align="right">1,291,318,013</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,701,596,528</td>
<td align="right">1,839,492,399</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,260,441,371</td>
<td align="right">1,360,186,481</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">4,617,465,392</td>
<td align="right">4,930,448,505</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">623,052,670</td>
<td align="right">661,961,530</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">655,062,028</td>
<td align="right">693,724,827</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">660,269,282</td>
<td align="right">622,304,038</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">5,300,218,116</td>
<td align="right">5,593,054,958</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">230,452,903</td>
<td align="right">243,109,584</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,291,884,187</td>
<td align="right">1,360,488,366</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">910,442,681</td>
<td align="right">948,231,815</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">897,553,465</td>
<td align="right">926,600,733</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">664,289,054</td>
<td align="right">681,630,700</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">210,861,636</td>
<td align="right">210,004,235</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">236,186,066</td>
<td align="right">235,312,375</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">498,487,103</td>
<td align="right">496,739,789</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">249,242,925</td>
<td align="right">248,369,281</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">249,242,925</td>
<td align="right">248,369,281</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">249,242,925</td>
<td align="right">248,369,281</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">510,762,687</td>
<td align="right">509,015,331</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">510,762,687</td>
<td align="right">509,015,331</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">510,762,687</td>
<td align="right">509,015,331</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">510,762,687</td>
<td align="right">509,015,331</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">510,762,687</td>
<td align="right">509,015,331</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">510,762,687</td>
<td align="right">509,015,331</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">510,762,687</td>
<td align="right">509,015,331</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">510,762,687</td>
<td align="right">509,015,331</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">510,762,687</td>
<td align="right">509,015,331</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">568,317,926</td>
<td align="right">566,501,400</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">574,455,718</td>
<td align="right">572,639,171</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">650,424,333</td>
<td align="right">648,538,553</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">37,595,303</td>
<td align="right">37,558,434</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">37,595,303</td>
<td align="right">37,558,434</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">56,781,941</td>
<td align="right">56,728,803</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">75,968,615</td>
<td align="right">75,899,382</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">75,968,615</td>
<td align="right">75,899,382</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">75,968,615</td>
<td align="right">75,899,382</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">75,968,615</td>
<td align="right">75,899,382</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">75,968,615</td>
<td align="right">75,899,382</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">75,968,615</td>
<td align="right">75,899,382</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">75,968,615</td>
<td align="right">75,899,382</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">75,968,615</td>
<td align="right">75,899,382</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">195,670,325</td>
<td align="right">195,494,969</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">158,075,022</td>
<td align="right">157,936,535</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">19,186,638</td>
<td align="right">19,170,369</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">19,186,638</td>
<td align="right">19,170,369</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">82,106,407</td>
<td align="right">82,037,153</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">82,106,407</td>
<td align="right">82,037,153</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">82,106,407</td>
<td align="right">82,037,153</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">19,186,674</td>
<td align="right">19,170,581</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">19,186,674</td>
<td align="right">19,170,581</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">1,253</td>
<td align="right">1,252</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">25,324,430</td>
<td align="right">25,308,140</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">25,324,430</td>
<td align="right">25,308,140</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">38,382,542</td>
<td align="right">38,366,273</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">38,382,542</td>
<td align="right">38,366,273</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">12,275,584</td>
<td align="right">12,275,542</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,137,792</td>
<td align="right">6,137,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">6,137,792</td>
<td align="right">6,137,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">6,137,792</td>
<td align="right">6,137,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">6,137,792</td>
<td align="right">6,137,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">6,137,792</td>
<td align="right">6,137,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">6,137,792</td>
<td align="right">6,137,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">6,137,792</td>
<td align="right">6,137,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">75,218,816</td>
<td align="right">75,218,690</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">38,391,808</td>
<td align="right">38,391,808</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">38,391,808</td>
<td align="right">38,391,808</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">38,357,356</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">19,195,904</td>
<td align="right">19,195,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">19,195,904</td>
<td align="right">19,195,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">64</td>
<td align="right">64</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-05-13
