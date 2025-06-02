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
<td align="left">BUILD_MAP</td>
<td align="right">64</td>
<td align="right">2,097,152</td>
<td align="right">3,276,700.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">819</td>
<td align="right">2,106,255</td>
<td align="right">257,074.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">154,506,779</td>
<td align="right">40,400</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">128,906,676</td>
<td align="right">45,654</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">38,400,124</td>
<td align="right">17,445</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,800,256</td>
<td align="right">8,355</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">76,800,000</td>
<td align="right">50,964</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">76,800,000</td>
<td align="right">50,964</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">38,400,000</td>
<td align="right">25,482</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">76,800,064</td>
<td align="right">50,965</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">19,199,998</td>
<td align="right">13,192</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">57,614,409</td>
<td align="right">39,961</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">25,600,192</td>
<td align="right">25,642</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">38,399,996</td>
<td align="right">42,768</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">76,799,996</td>
<td align="right">85,540</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">76,799,996</td>
<td align="right">85,540</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">76,799,998</td>
<td align="right">85,542</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">76,800,122</td>
<td align="right">85,697</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">211,201,088</td>
<td align="right">370,520</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">249,600,057</td>
<td align="right">2,571,417</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">64</td>
<td align="right">1</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">64</td>
<td align="right">1</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">64</td>
<td align="right">1</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">64</td>
<td align="right">1</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">64</td>
<td align="right">1</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">64</td>
<td align="right">1</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">64</td>
<td align="right">1</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">300,801,216</td>
<td align="right">4,815,474</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">512,000,559</td>
<td align="right">8,591,854</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">512,000,874</td>
<td align="right">8,592,168</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">467,200,178</td>
<td align="right">8,916,667</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">192,000,814</td>
<td align="right">4,396,849</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">288,000,384</td>
<td align="right">6,808,818</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">256,000,576</td>
<td align="right">6,466,222</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">249,600,189</td>
<td align="right">6,388,829</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">249,600,126</td>
<td align="right">6,388,829</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">230,400,183</td>
<td align="right">6,416,577</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">230,400,284</td>
<td align="right">6,416,772</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">780,801,456</td>
<td align="right">22,699,086</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">518,400,512</td>
<td align="right">15,564,260</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,209,600,925</td>
<td align="right">36,939,260</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">704,001,431</td>
<td align="right">21,667,917</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,254,403,072</td>
<td align="right">41,007,692</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">4,300,806,620</td>
<td align="right">145,282,309</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">1,996,803,840</td>
<td align="right">69,210,218</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">64,000,248</td>
<td align="right">2,245,085</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">1,280,002,136</td>
<td align="right">45,637,958</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">1,452,801,628</td>
<td align="right">57,554,692</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,016,002,021</td>
<td align="right">87,010,721</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">460,800,991</td>
<td align="right">21,534,281</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">44,800,256</td>
<td align="right">2,214,602</td>
<td align="right">-95.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">44,800,061</td>
<td align="right">2,223,544</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">812,801,031</td>
<td align="right">44,696,042</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">192,000,256</td>
<td align="right">12,665,733</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">275,201,024</td>
<td align="right">19,100,388</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">76,800,187</td>
<td align="right">6,344,235</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">76,800,124</td>
<td align="right">6,344,235</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">76,800,128</td>
<td align="right">6,344,239</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">76,819,962</td>
<td align="right">6,346,571</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">76,800,376</td>
<td align="right">6,348,330</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">76,800,128</td>
<td align="right">6,348,489</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">102,400,500</td>
<td align="right">8,770,364</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">76,800,192</td>
<td align="right">6,655,615</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">76,819,308</td>
<td align="right">6,657,398</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">76,800,256</td>
<td align="right">6,655,928</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">83,200,187</td>
<td align="right">8,445,483</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">83,200,375</td>
<td align="right">8,852,917</td>
<td align="right">-89.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">115,200,630</td>
<td align="right">12,629,797</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">115,200,312</td>
<td align="right">12,989,898</td>
<td align="right">-88.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">25,600,250</td>
<td align="right">4,211,748</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">38,400,320</td>
<td align="right">6,318,004</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">30</td>
<td align="right">9</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">19,200,126</td>
<td align="right">6,304,648</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">12,800,315</td>
<td align="right">4,394,302</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,400,188</td>
<td align="right">4,294,301</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">7</td>
<td align="right">9</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">76</td>
<td align="right">55</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">138</td>
<td align="right">175</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">126</td>
<td align="right">157</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">128</td>
<td align="right">159</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">128</td>
<td align="right">159</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">128</td>
<td align="right">159</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">128</td>
<td align="right">159</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">128</td>
<td align="right">159</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">128</td>
<td align="right">159</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">128</td>
<td align="right">159</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">128</td>
<td align="right">159</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">155</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">928</td>
<td align="right">716</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">412</td>
<td align="right">352</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">211,200,128</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">63</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">63</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">63</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">62</td>
<td align="right">62</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">29</td>
<td align="right">29</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">14</td>
<td align="right">14</td>
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
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">6,752,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">28,831</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">16,380</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right"></td>
<td align="right">8,343</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">153</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">166,401,002</td>
<td align="right">68.4%</td>
<td align="right">10,828,484</td>
<td align="right">61.9%</td>
<td align="right">-93.5%</td>
</tr>
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
<td align="right">6,655,639</td>
<td align="right">38.1%</td>
<td align="right">-91.3%</td>
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
<td align="right">18,832</td>
<td align="right">98.6%</td>
<td align="right">1,663</td>
<td align="right">94.5%</td>
<td align="right">-91.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">262</td>
<td align="right">1.4%</td>
<td align="right">96</td>
<td align="right">5.5%</td>
<td align="right">-63.4%</td>
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
<td align="right">1,663</td>
<td align="right">100.0%</td>
<td align="right">-91.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,272,003,017</td>
<td align="right">100.0%</td>
<td align="right">83,967,608</td>
<td align="right">100.0%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">94</td>
<td align="right">0.0%</td>
<td align="right">102</td>
<td align="right">0.0%</td>
<td align="right">8.5%</td>
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
<td align="right">834</td>
<td align="right">100.0%</td>
<td align="right">614</td>
<td align="right">100.0%</td>
<td align="right">-26.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,000,248</td>
<td align="right">100.0%</td>
<td align="right">2,245,085</td>
<td align="right">100.0%</td>
<td align="right">-96.5%</td>
</tr>
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
<td align="right">47</td>
<td align="right">100.0%</td>
<td align="right">-30.9%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">332,800,313</td>
<td align="right">100.0%</td>
<td align="right">14,834,312</td>
<td align="right">100.0%</td>
<td align="right">-95.5%</td>
</tr>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">96,106,704</td>
<td align="right">33.9%</td>
<td align="right">27,448</td>
<td align="right">29.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">187,306,751</td>
<td align="right">66.1%</td>
<td align="right">66,949</td>
<td align="right">70.8%</td>
<td align="right">-100.0%</td>
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
<td align="right">0.0%</td>
<td align="right">165</td>
<td align="right">0.2%</td>
<td align="right">25.0%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.8%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,813,335</td>
<td align="right">100.0%</td>
<td align="right">522</td>
<td align="right">99.2%</td>
<td align="right">-100.0%</td>
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
<td align="right">4</td>
<td align="right">100.0%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">tuple</td>
<td align="right">38,400,000</td>
<td align="right">38,400,000 / 0 !!</td>
<td align="right">321,386</td>
<td align="right">321,386 / 0 !!</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">38,400,128</td>
<td align="right">38,400,128 / 0 !!</td>
<td align="right">6,334,228</td>
<td align="right">6,334,228 / 0 !!</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">155</td>
<td align="right">155 / 0 !!</td>
<td align="right"></td>
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
<td align="right">1,196,802,933</td>
<td align="right">94.0%</td>
<td align="right">45,142,510</td>
<td align="right">87.7%</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">76,800,395</td>
<td align="right">6.0%</td>
<td align="right">6,344,474</td>
<td align="right">12.3%</td>
<td align="right">-91.7%</td>
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
<td align="right">18,874</td>
<td align="right">96.5%</td>
<td align="right">1,633</td>
<td align="right">77.9%</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">693</td>
<td align="right">3.5%</td>
<td align="right">464</td>
<td align="right">22.1%</td>
<td align="right">-33.0%</td>
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
<td align="right">18,832</td>
<td align="right">99.8%</td>
<td align="right">1,587</td>
<td align="right">97.2%</td>
<td align="right">-91.6%</td>
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
<td align="right">2,476,802,964</td>
<td align="right">100.0%</td>
<td align="right">108,544,954</td>
<td align="right">100.0%</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">76</td>
<td align="right">0.0%</td>
<td align="right">78</td>
<td align="right">0.0%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">48</td>
<td align="right">0.0%</td>
<td align="right">48</td>
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
<td align="right">336</td>
<td align="right">100.0%</td>
<td align="right">274</td>
<td align="right">100.0%</td>
<td align="right">-18.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">76,799,998</td>
<td align="right">100.0%</td>
<td align="right">85,542</td>
<td align="right">100.0%</td>
<td align="right">-99.9%</td>
</tr>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">76,800,187</td>
<td align="right">100.0%</td>
<td align="right">6,344,235</td>
<td align="right">100.0%</td>
<td align="right">-91.7%</td>
</tr>
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
<td align="right">4</td>
<td align="right">100.0%</td>
<td align="right">-84.0%</td>
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
<td align="right">57,600,169</td>
<td align="right">4.2%</td>
<td align="right">39,789</td>
<td align="right">0.1%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,305,601,175</td>
<td align="right">95.8%</td>
<td align="right">49,588,143</td>
<td align="right">99.9%</td>
<td align="right">-96.2%</td>
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
<td align="right">14,159</td>
<td align="right">99.4%</td>
<td align="right">91</td>
<td align="right">52.9%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">81</td>
<td align="right">0.6%</td>
<td align="right">81</td>
<td align="right">47.1%</td>
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
<td align="left">tuple</td>
<td align="right">9,405</td>
<td align="right">66.4%</td>
<td align="right">25</td>
<td align="right">27.5%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">4,712</td>
<td align="right">33.3%</td>
<td align="right">22</td>
<td align="right">24.2%</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">44</td>
<td align="right">48.4%</td>
<td align="right">4.8%</td>
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
<td align="right">288,000,181</td>
<td align="right">100.0%</td>
<td align="right">2,588,862</td>
<td align="right">100.0%</td>
<td align="right">-99.1%</td>
</tr>
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
<td align="right">96,106,752</td>
<td align="right">0.4%</td>
<td align="right">27,496</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">14,150,427,636</td>
<td align="right">59.2%</td>
<td align="right">503,943,849</td>
<td align="right">57.8%</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">9,377,721,271</td>
<td align="right">39.2%</td>
<td align="right">348,053,036</td>
<td align="right">39.9%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">288,055,475</td>
<td align="right">1.2%</td>
<td align="right">19,393,810</td>
<td align="right">2.2%</td>
<td align="right">-93.3%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">57,600,169</td>
<td align="right">27.3%</td>
<td align="right">39,789</td>
<td align="right">0.3%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">76,800,395</td>
<td align="right">36.4%</td>
<td align="right">6,344,474</td>
<td align="right">48.7%</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">76,800,214</td>
<td align="right">36.4%</td>
<td align="right">6,655,639</td>
<td align="right">51.0%</td>
<td align="right">-91.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">132</td>
<td align="right">0.0%</td>
<td align="right">165</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">94</td>
<td align="right">0.0%</td>
<td align="right">102</td>
<td align="right">0.0%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">76</td>
<td align="right">0.0%</td>
<td align="right">78</td>
<td align="right">0.0%</td>
<td align="right">2.6%</td>
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
<td align="right">48,053,295</td>
<td align="right">50.0%</td>
<td align="right">13,674</td>
<td align="right">49.7%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">48,053,409</td>
<td align="right">50.0%</td>
<td align="right">13,774</td>
<td align="right">50.1%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">24</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">24</td>
<td align="right">0.1%</td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">19,200,000</td>
<td align="right">2.7%</td>
<td align="right">21,386</td>
<td align="right">0.1%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">38,400,000</td>
<td align="right">5.5%</td>
<td align="right">42,772</td>
<td align="right">0.2%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">64</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">588,801,020</td>
<td align="right">83.6%</td>
<td align="right">9,788,201</td>
<td align="right">43.0%</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">780,801,456</td>
<td align="right">110.9%</td>
<td align="right">22,863,798</td>
<td align="right">100.4%</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">115,200,440</td>
<td align="right">16.4%</td>
<td align="right">12,990,057</td>
<td align="right">57.0%</td>
<td align="right">-88.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">115,200,440</td>
<td align="right">16.4%</td>
<td align="right">12,990,057</td>
<td align="right">57.0%</td>
<td align="right">-88.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">115,200,440</td>
<td align="right">16.4%</td>
<td align="right">12,990,057</td>
<td align="right">57.0%</td>
<td align="right">-88.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">115,200,440</td>
<td align="right">16.4%</td>
<td align="right">12,990,057</td>
<td align="right">57.0%</td>
<td align="right">-88.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
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
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">19,800,123</td>
<td align="right"></td>
<td align="right">83</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">19,800,165</td>
<td align="right"></td>
<td align="right">105</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">812,801,330</td>
<td align="right"></td>
<td align="right">27,705,038</td>
<td align="right"></td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">556,200,609</td>
<td align="right"></td>
<td align="right">20,351,908</td>
<td align="right"></td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">716,801,287</td>
<td align="right">52.1%</td>
<td align="right">27,598,398</td>
<td align="right">39.8%</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">716,801,479</td>
<td align="right">52.1%</td>
<td align="right">27,598,423</td>
<td align="right">39.8%</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,537,924,115</td>
<td align="right">28.9%</td>
<td align="right">101,557,716</td>
<td align="right">24.8%</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,072,644,600</td>
<td align="right">25.6%</td>
<td align="right">85,886,752</td>
<td align="right">23.0%</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,700,477,794</td>
<td align="right">21.0%</td>
<td align="right">74,024,875</td>
<td align="right">19.9%</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">4,100,487,993</td>
<td align="right">50.6%</td>
<td align="right">199,560,714</td>
<td align="right">53.5%</td>
<td align="right">-95.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">4,992,010,931</td>
<td align="right">56.9%</td>
<td align="right">243,846,451</td>
<td align="right">59.4%</td>
<td align="right">-95.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,245,703,144</td>
<td align="right">14.2%</td>
<td align="right">64,773,991</td>
<td align="right">15.8%</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">230,400,497</td>
<td align="right">2.8%</td>
<td align="right">13,396,981</td>
<td align="right">3.6%</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">659,201,815</td>
<td align="right"></td>
<td align="right">41,752,351</td>
<td align="right"></td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">659,202,026</td>
<td align="right">47.9%</td>
<td align="right">41,752,593</td>
<td align="right">60.2%</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">211,220,156</td>
<td align="right"></td>
<td align="right">19,947,680</td>
<td align="right"></td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">192</td>
<td align="right">0.0%</td>
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">74</td>
<td align="right"></td>
<td align="right">64</td>
<td align="right"></td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3 / 0 !!</td>
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
Stats gathered on: 2025-06-02
