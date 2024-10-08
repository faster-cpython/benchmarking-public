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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">61,320</td>
<td align="right">16,440</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">10,220</td>
<td align="right">2,740</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">10,240</td>
<td align="right">2,760</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,094,920</td>
<td align="right">306,900</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">1,097,580</td>
<td align="right">309,560</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">18,467,940</td>
<td align="right">9,526,780</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">18,206,840</td>
<td align="right">10,101,180</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,636,600</td>
<td align="right">1,569,540</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,942,220</td>
<td align="right">1,164,800</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,102,280</td>
<td align="right">1,314,520</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">40,440</td>
<td align="right">25,780</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,364,780</td>
<td align="right">5,412,680</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,183,140</td>
<td align="right">2,116,760</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,190,440</td>
<td align="right">2,127,060</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">13,842,460</td>
<td align="right">9,525,460</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">21,864,160</td>
<td align="right">15,114,800</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">36,060,400</td>
<td align="right">25,076,700</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">15,661,400</td>
<td align="right">10,906,780</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">32,736,840</td>
<td align="right">23,500,200</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">21,966,740</td>
<td align="right">15,988,320</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,758,280</td>
<td align="right">2,755,380</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">26,084,240</td>
<td align="right">19,144,020</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">23,691,200</td>
<td align="right">17,392,020</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">37,959,960</td>
<td align="right">27,934,020</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">128,351,580</td>
<td align="right">94,616,360</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">23,574,660</td>
<td align="right">17,527,600</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">271,360</td>
<td align="right">201,800</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">68,964,460</td>
<td align="right">52,072,700</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,468,000</td>
<td align="right">2,623,580</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,830,420</td>
<td align="right">8,985,400</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">3,999,920</td>
<td align="right">3,056,520</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">15,284,400</td>
<td align="right">11,889,620</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">7,858,880</td>
<td align="right">6,333,600</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,651,240</td>
<td align="right">2,968,360</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,456,660</td>
<td align="right">3,647,040</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,352,800</td>
<td align="right">4,486,820</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">2,640,380</td>
<td align="right">2,425,500</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,640,660</td>
<td align="right">2,425,800</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">796,160</td>
<td align="right">794,520</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">949,900</td>
<td align="right">948,240</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,064,060</td>
<td align="right">1,062,440</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">13,500</td>
<td align="right">13,520</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">271,280</td>
<td align="right">271,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">151,220</td>
<td align="right">151,200</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,185,780</td>
<td align="right">3,185,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,576,680</td>
<td align="right">1,576,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">25,100</td>
<td align="right">25,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">22,980</td>
<td align="right">22,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">16,800</td>
<td align="right">16,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">10,400</td>
<td align="right">10,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">6,000</td>
<td align="right">6,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,640</td>
<td align="right">5,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">5,120</td>
<td align="right">5,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,960</td>
<td align="right">3,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,840</td>
<td align="right">2,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">2,560</td>
<td align="right">2,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,560</td>
<td align="right">2,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,540</td>
<td align="right">2,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,200</td>
<td align="right">1,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,120</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">700</td>
<td align="right">700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">520</td>
<td align="right">520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
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
<td align="right">270,400</td>
<td align="right">1.9%</td>
<td align="right">270,440</td>
<td align="right">1.9%</td>
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
<td align="right">13,621,600</td>
<td align="right">98.0%</td>
<td align="right">13,621,600</td>
<td align="right">98.0%</td>
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
<td align="right">240</td>
<td align="right">27.3%</td>
<td align="right">240</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">640</td>
<td align="right">72.7%</td>
<td align="right">640</td>
<td align="right">72.7%</td>
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
<td align="right">500</td>
<td align="right">78.1%</td>
<td align="right">500</td>
<td align="right">78.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">140</td>
<td align="right">21.9%</td>
<td align="right">140</td>
<td align="right">21.9%</td>
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
<td align="right">5,740</td>
<td align="right">35.4%</td>
<td align="right">5,740</td>
<td align="right">35.4%</td>
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
<td align="right">10,220</td>
<td align="right">63.0%</td>
<td align="right">10,220</td>
<td align="right">63.0%</td>
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
<td align="right">7.7%</td>
<td align="right">20</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">240</td>
<td align="right">92.3%</td>
<td align="right">240</td>
<td align="right">92.3%</td>
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
<td align="left">buffer int</td>
<td align="right">240</td>
<td align="right">100.0%</td>
<td align="right">240</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,981,840</td>
<td align="right">3.9%</td>
<td align="right">4,875,700</td>
<td align="right">3.2%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">146,322,760</td>
<td align="right">96.1%</td>
<td align="right">147,408,120</td>
<td align="right">96.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,820</td>
<td align="right">0.0%</td>
<td align="right">2,820</td>
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
<td align="right">115,440</td>
<td align="right">100.0%</td>
<td align="right">94,660</td>
<td align="right">100.0%</td>
<td align="right">-18.0%</td>
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
<td align="right">2,634,540</td>
<td align="right">2.9%</td>
<td align="right">1,567,820</td>
<td align="right">1.8%</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">87,805,100</td>
<td align="right">97.1%</td>
<td align="right">87,805,100</td>
<td align="right">98.2%</td>
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
<td align="right">1,640</td>
<td align="right">79.6%</td>
<td align="right">1,300</td>
<td align="right">75.6%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">420</td>
<td align="right">20.4%</td>
<td align="right">420</td>
<td align="right">24.4%</td>
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
<td align="right">80</td>
<td align="right">4.9%</td>
<td align="right">60</td>
<td align="right">4.6%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">1,440</td>
<td align="right">87.8%</td>
<td align="right">1,120</td>
<td align="right">86.2%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">120</td>
<td align="right">7.3%</td>
<td align="right">120</td>
<td align="right">9.2%</td>
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
<td align="right">3,208,240</td>
<td align="right">100.0%</td>
<td align="right">2,141,860</td>
<td align="right">100.0%</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">260</td>
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
<td align="right">260</td>
<td align="right">100.0%</td>
<td align="right">260</td>
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
<td align="right">9,767,520</td>
<td align="right">2.0%</td>
<td align="right">7,529,540</td>
<td align="right">1.6%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,343,200</td>
<td align="right">1.1%</td>
<td align="right">4,477,720</td>
<td align="right">0.9%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">467,858,360</td>
<td align="right">96.9%</td>
<td align="right">469,090,860</td>
<td align="right">97.5%</td>
<td align="right">0.3%</td>
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
<td align="right">188,120</td>
<td align="right">97.2%</td>
<td align="right">145,900</td>
<td align="right">96.7%</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,460</td>
<td align="right">2.8%</td>
<td align="right">4,960</td>
<td align="right">3.3%</td>
<td align="right">-9.2%</td>
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
<td align="right">2,820</td>
<td align="right">51.6%</td>
<td align="right">2,500</td>
<td align="right">50.4%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">2,640</td>
<td align="right">48.4%</td>
<td align="right">2,460</td>
<td align="right">49.6%</td>
<td align="right">-6.8%</td>
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
<td align="right">100,805,720</td>
<td align="right">100.0%</td>
<td align="right">100,797,840</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">1,980</td>
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
<td align="right">1,980</td>
<td align="right">100.0%</td>
<td align="right">1,980</td>
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
<td align="right">3,402,020</td>
<td align="right">100.0%</td>
<td align="right">3,402,020</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">53,216,500</td>
<td align="right">96.6%</td>
<td align="right">53,109,520</td>
<td align="right">96.6%</td>
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
<td align="right">1,872,960</td>
<td align="right">3.4%</td>
<td align="right">1,870,820</td>
<td align="right">3.4%</td>
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
<td align="right">1,140</td>
<td align="right">0.0%</td>
<td align="right">1,140</td>
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
<td align="right">36,260</td>
<td align="right">99.9%</td>
<td align="right">36,240</td>
<td align="right">99.9%</td>
<td align="right">-0.1%</td>
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
<td align="right">17,803,100</td>
<td align="right">100.0%</td>
<td align="right">16,204,200</td>
<td align="right">100.0%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">560</td>
<td align="right">0.0%</td>
<td align="right">560</td>
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
<td align="right">560</td>
<td align="right">100.0%</td>
<td align="right">560</td>
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
<td align="right">0.8%</td>
<td align="right">20</td>
<td align="right">0.8%</td>
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
<td align="right">2,540</td>
<td align="right">98.4%</td>
<td align="right">2,540</td>
<td align="right">98.4%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">282,002,100</td>
<td align="right">48.2%</td>
<td align="right">199,643,440</td>
<td align="right">47.2%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">276,595,640</td>
<td align="right">47.3%</td>
<td align="right">202,444,480</td>
<td align="right">47.9%</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,280,600</td>
<td align="right">1.4%</td>
<td align="right">6,347,600</td>
<td align="right">1.5%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">17,623,520</td>
<td align="right">3.0%</td>
<td align="right">14,277,300</td>
<td align="right">3.4%</td>
<td align="right">-19.0%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">2,634,540</td>
<td align="right">31.9%</td>
<td align="right">1,567,820</td>
<td align="right">24.8%</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,343,200</td>
<td align="right">64.7%</td>
<td align="right">4,477,720</td>
<td align="right">70.8%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">270,400</td>
<td align="right">3.3%</td>
<td align="right">270,440</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">5,740</td>
<td align="right">0.1%</td>
<td align="right">5,740</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,820</td>
<td align="right">0.0%</td>
<td align="right">2,820</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
<td align="right">1,980</td>
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
<td align="right">560</td>
<td align="right">0.0%</td>
<td align="right">560</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">260</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,785,660</td>
<td align="right">15.8%</td>
<td align="right">1,679,520</td>
<td align="right">11.8%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,731,420</td>
<td align="right">32.5%</td>
<td align="right">3,803,660</td>
<td align="right">26.6%</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,036,100</td>
<td align="right">22.9%</td>
<td align="right">3,725,880</td>
<td align="right">26.1%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">1,240</td>
<td align="right">0.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">1,240</td>
<td align="right">0.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,872,960</td>
<td align="right">10.6%</td>
<td align="right">1,870,820</td>
<td align="right">13.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,185,780</td>
<td align="right">18.1%</td>
<td align="right">3,185,780</td>
<td align="right">22.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">10,400</td>
<td align="right">0.1%</td>
<td align="right">10,400</td>
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
<td align="left">EXIT_INIT_CHECK</td>
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
<td align="right">2,840</td>
<td align="right">0.0%</td>
<td align="right">2,840</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">131,635,000</td>
<td align="right">100.0%</td>
<td align="right">131,635,000</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,840</td>
<td align="right">0.0%</td>
<td align="right">2,840</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">2,840</td>
<td align="right">0.0%</td>
<td align="right">2,840</td>
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
<td align="right">2,840</td>
<td align="right">0.0%</td>
<td align="right">2,840</td>
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
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">80</td>
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
<td align="right">133,214,520</td>
<td align="right">101.2%</td>
<td align="right">133,214,520</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">331</td>
<td align="right"></td>
<td align="right">850</td>
<td align="right"></td>
<td align="right">156.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">1,420</td>
<td align="right">0.0%</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,940</td>
<td align="right">0.0%</td>
<td align="right">2,640</td>
<td align="right">0.0%</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">92,902,180</td>
<td align="right">6.5%</td>
<td align="right">64,864,680</td>
<td align="right">4.5%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">95,817,580</td>
<td align="right">6.5%</td>
<td align="right">70,111,840</td>
<td align="right">4.7%</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">294,054,940</td>
<td align="right">20.5%</td>
<td align="right">217,257,340</td>
<td align="right">15.1%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">813,830,324</td>
<td align="right">56.8%</td>
<td align="right">902,489,862</td>
<td align="right">62.8%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">256,296,838</td>
<td align="right">17.3%</td>
<td align="right">281,325,816</td>
<td align="right">18.8%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">529,762,910</td>
<td align="right">35.7%</td>
<td align="right">578,867,604</td>
<td align="right">38.7%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">231,754,122</td>
<td align="right">16.2%</td>
<td align="right">251,672,417</td>
<td align="right">17.5%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">603,199,380</td>
<td align="right">40.6%</td>
<td align="right">566,021,880</td>
<td align="right">37.8%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">26,850,049</td>
<td align="right"></td>
<td align="right">25,667,621</td>
<td align="right"></td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,126,328</td>
<td align="right"></td>
<td align="right">2,140,649</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,127,111</td>
<td align="right"></td>
<td align="right">2,140,779</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">507,709</td>
<td align="right"></td>
<td align="right">507,190</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">27,229,024</td>
<td align="right"></td>
<td align="right">27,255,039</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">1,672,260</td>
<td align="right">6.1%</td>
<td align="right">1,672,480</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">1,672,860</td>
<td align="right"></td>
<td align="right">1,673,060</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">25,778,580</td>
<td align="right">93.9%</td>
<td align="right">25,780,260</td>
<td align="right">93.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">25,775,800</td>
<td align="right">93.9%</td>
<td align="right">25,776,200</td>
<td align="right">93.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,712,000</td>
<td align="right"></td>
<td align="right">3,712,000</td>
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
<th align="right">Head Collections</th>
<th align="right">Head Objects collected</th>
<th align="right">Head Object visits</th>
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
</tr>
<tr>
<td align="right">1</td>
<td align="right">1,160</td>
<td align="right">1,788,240</td>
<td align="right">34,537,500</td>
<td align="right">1,160</td>
<td align="right">1,800,160</td>
<td align="right">34,437,020</td>
</tr>
<tr>
<td align="right">2</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">3,680</td>
<td align="right">49.5%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">80</td>
<td align="right">1.1%</td>
<td align="right">160</td>
<td align="right">2.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">260</td>
<td align="right">3.5%</td>
<td align="right">460</td>
<td align="right">5.6%</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">3,580</td>
<td align="right">48.1%</td>
<td align="right">5,660</td>
<td align="right">69.2%</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">3,840</td>
<td align="right">51.6%</td>
<td align="right">2,500</td>
<td align="right">30.6%</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">91,381,260</td>
<td align="right"></td>
<td align="right">104,677,780</td>
<td align="right"></td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">3,286,123,440</td>
<td align="right">3,596.1%</td>
<td align="right">3,656,950,000</td>
<td align="right">3,493.5%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">1,440</td>
<td align="right">40.2%</td>
<td align="right">1,600</td>
<td align="right">28.3%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">7,440</td>
<td align="right"></td>
<td align="right">8,180</td>
<td align="right"></td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
<td align="right">3,580</td>
<td align="right"></td>
<td align="right">5,660</td>
<td align="right"></td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">3,320</td>
<td align="right">92.7%</td>
<td align="right">5,080</td>
<td align="right">89.8%</td>
<td align="right">53.0%</td>
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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">340</td>
<td align="right">9.5%</td>
<td align="right">560</td>
<td align="right">9.9%</td>
<td align="right">64.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">160</td>
<td align="right">4.5%</td>
<td align="right">400</td>
<td align="right">7.1%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">460</td>
<td align="right">12.8%</td>
<td align="right">660</td>
<td align="right">11.7%</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">840</td>
<td align="right">23.5%</td>
<td align="right">1,000</td>
<td align="right">17.7%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">580</td>
<td align="right">16.2%</td>
<td align="right">800</td>
<td align="right">14.1%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">220</td>
<td align="right">6.1%</td>
<td align="right">400</td>
<td align="right">7.1%</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">860</td>
<td align="right">24.0%</td>
<td align="right">1,540</td>
<td align="right">27.2%</td>
<td align="right">79.1%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">120</td>
<td align="right">3.4%</td>
<td align="right">300</td>
<td align="right">5.3%</td>
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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">220</td>
<td align="right">6.1%</td>
<td align="right">180</td>
<td align="right">3.2%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">180</td>
<td align="right">5.0%</td>
<td align="right">660</td>
<td align="right">11.7%</td>
<td align="right">266.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">260</td>
<td align="right">7.3%</td>
<td align="right">340</td>
<td align="right">6.0%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">700</td>
<td align="right">19.6%</td>
<td align="right">880</td>
<td align="right">15.5%</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">800</td>
<td align="right">22.3%</td>
<td align="right">1,100</td>
<td align="right">19.4%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">260</td>
<td align="right">7.3%</td>
<td align="right">380</td>
<td align="right">6.7%</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">640</td>
<td align="right">17.9%</td>
<td align="right">1,140</td>
<td align="right">20.1%</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">260</td>
<td align="right">7.3%</td>
<td align="right">400</td>
<td align="right">7.1%</td>
<td align="right">53.8%</td>
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
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">512,620</td>
<td align="right">7,131,600</td>
<td align="right">1,291.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">496,140</td>
<td align="right">3,333,800</td>
<td align="right">571.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">508,820</td>
<td align="right">1,579,680</td>
<td align="right">210.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">251,820</td>
<td align="right">746,260</td>
<td align="right">196.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">752,060</td>
<td align="right">2,107,960</td>
<td align="right">180.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">867,240</td>
<td align="right">1,930,620</td>
<td align="right">122.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,256,200</td>
<td align="right">2,748,760</td>
<td align="right">118.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">2,748,000</td>
<td align="right">5,389,880</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,526,020</td>
<td align="right">2,772,140</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,674,080</td>
<td align="right">6,570,340</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">7,965,300</td>
<td align="right">13,677,560</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,005,400</td>
<td align="right">1,688,280</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">7,800,540</td>
<td align="right">13,029,860</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">515,660</td>
<td align="right">808,980</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">3,364,180</td>
<td align="right">5,192,920</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,997,940</td>
<td align="right">2,941,340</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">1,772,240</td>
<td align="right">2,549,660</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">1,772,240</td>
<td align="right">2,549,660</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,946,520</td>
<td align="right">8,458,720</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">2,875,000</td>
<td align="right">3,941,720</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,498,680</td>
<td align="right">3,308,300</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,498,680</td>
<td align="right">3,308,300</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">761,640</td>
<td align="right">976,520</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">761,660</td>
<td align="right">976,520</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,531,680</td>
<td align="right">9,627,720</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">4,047,300</td>
<td align="right">5,043,480</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">37,709,980</td>
<td align="right">46,660,080</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">4,493,480</td>
<td align="right">5,556,820</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">3,349,080</td>
<td align="right">4,137,100</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">3,351,740</td>
<td align="right">4,139,760</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">38,677,860</td>
<td align="right">47,623,440</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">38,466,900</td>
<td align="right">46,385,520</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">9,457,780</td>
<td align="right">11,299,660</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,953,040</td>
<td align="right">4,689,460</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">5,543,680</td>
<td align="right">6,547,740</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">91,433,020</td>
<td align="right">105,585,740</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">91,381,260</td>
<td align="right">104,677,780</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">92,590,960</td>
<td align="right">105,887,480</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">157,106,460</td>
<td align="right">175,406,660</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">94,369,860</td>
<td align="right">105,155,100</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">94,369,860</td>
<td align="right">105,155,100</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">94,369,860</td>
<td align="right">105,155,100</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">70,963,200</td>
<td align="right">78,898,440</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">92,921,580</td>
<td align="right">103,193,700</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">92,915,400</td>
<td align="right">102,940,880</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">92,915,400</td>
<td align="right">102,940,880</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">93,428,020</td>
<td align="right">103,455,120</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">93,677,060</td>
<td align="right">103,703,040</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">34,877,520</td>
<td align="right">38,588,520</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">56,140,580</td>
<td align="right">62,070,000</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">380</td>
<td align="right">420</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">66,915,900</td>
<td align="right">73,854,960</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">67,628,300</td>
<td align="right">74,358,480</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">250,468,660</td>
<td align="right">273,349,340</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">65,838,360</td>
<td align="right">71,816,780</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">207,450,980</td>
<td align="right">226,206,880</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">70,380,400</td>
<td align="right">76,358,820</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">79,220</td>
<td align="right">85,940</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">39,805,060</td>
<td align="right">43,090,720</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">39,805,060</td>
<td align="right">43,090,720</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">199,424,360</td>
<td align="right">215,509,100</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">199,424,360</td>
<td align="right">215,509,100</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">63,083,960</td>
<td align="right">67,838,580</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">63,083,960</td>
<td align="right">67,838,580</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">90,868,260</td>
<td align="right">97,545,760</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">88,911,200</td>
<td align="right">94,802,240</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">34,498,820</td>
<td align="right">35,562,200</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">38,519,140</td>
<td align="right">39,585,520</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">38,519,140</td>
<td align="right">39,585,520</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">44,438,700</td>
<td align="right">45,230,760</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">522,240</td>
<td align="right">529,720</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">31,618,600</td>
<td align="right">32,032,720</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,038,800</td>
<td align="right">1,046,280</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">512,620</td>
<td align="right">514,240</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">512,620</td>
<td align="right">514,240</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,248,280</td>
<td align="right">1,249,920</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,462,660</td>
<td align="right">2,463,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,215,440</td>
<td align="right">6,217,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">76,040</td>
<td align="right">76,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">253,120</td>
<td align="right">253,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">584,880</td>
<td align="right">584,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">5,714,280</td>
<td align="right">5,714,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">6,215,440</td>
<td align="right">6,215,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,380,280</td>
<td align="right">1,380,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,380,280</td>
<td align="right">1,380,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">1,357,180</td>
<td align="right">1,357,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1,209,700</td>
<td align="right">1,209,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">501,160</td>
<td align="right">501,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,180</td>
<td align="right">2,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">2,180</td>
<td align="right">2,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">109,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">69,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right"></td>
<td align="right">44,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">7,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">7,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right"></td>
<td align="right">1,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">1,000</td>
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
<td align="right">840</td>
<td align="right">1,540</td>
<td align="right">83.3%</td>
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
Stats gathered on: 2024-10-05
