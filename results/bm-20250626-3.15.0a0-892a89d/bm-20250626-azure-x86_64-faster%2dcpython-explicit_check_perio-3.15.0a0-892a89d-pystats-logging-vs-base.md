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
<td align="left">RESUME</td>
<td align="right">83</td>
<td align="right">1,743</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">14</td>
<td align="right">294</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">3</td>
<td align="right">63</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3</td>
<td align="right">63</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3</td>
<td align="right">63</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3</td>
<td align="right">63</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3</td>
<td align="right">63</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">3</td>
<td align="right">63</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">794</td>
<td align="right">4,400</td>
<td align="right">454.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,529</td>
<td align="right">8,075</td>
<td align="right">428.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">70</td>
<td align="right">210</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">246</td>
<td align="right">583</td>
<td align="right">137.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">240</td>
<td align="right">517</td>
<td align="right">115.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,096</td>
<td align="right">2,039</td>
<td align="right">86.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">146</td>
<td align="right">104</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">146</td>
<td align="right">104</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">223</td>
<td align="right">160</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">223</td>
<td align="right">160</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">229</td>
<td align="right">286</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,145</td>
<td align="right">1,305</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">5,338,946</td>
<td align="right">5,253,290</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,357,232</td>
<td align="right">1,336,152</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">665,812</td>
<td align="right">655,489</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">2,663,025</td>
<td align="right">2,621,796</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,331,401</td>
<td align="right">1,310,818</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,996,990</td>
<td align="right">1,966,147</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">11,980,963</td>
<td align="right">11,795,980</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">11,981,719</td>
<td align="right">11,796,764</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,198,300</td>
<td align="right">1,179,805</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,687,964</td>
<td align="right">2,646,490</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,318,844</td>
<td align="right">9,175,156</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">29,285,916</td>
<td align="right">28,834,476</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">2,662,356</td>
<td align="right">2,621,316</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">1,331,178</td>
<td align="right">1,310,658</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,331,178</td>
<td align="right">1,310,658</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">1,331,178</td>
<td align="right">1,310,658</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,331,178</td>
<td align="right">1,310,658</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,331,178</td>
<td align="right">1,310,658</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,331,178</td>
<td align="right">1,310,658</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">9,318,698</td>
<td align="right">9,175,052</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">59,903,924</td>
<td align="right">58,980,758</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">31,949,184</td>
<td align="right">31,456,852</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">65,229,179</td>
<td align="right">64,224,224</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">12,646,424</td>
<td align="right">12,451,621</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">59,264,919</td>
<td align="right">58,352,038</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,655,894</td>
<td align="right">6,553,374</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">5,990,305</td>
<td align="right">5,898,045</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">5,324,716</td>
<td align="right">5,242,716</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">69,223,114</td>
<td align="right">68,157,092</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">67,225,221</td>
<td align="right">66,190,078</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">81,869,779</td>
<td align="right">80,609,255</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">18,636,659</td>
<td align="right">18,349,719</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">5,324,718</td>
<td align="right">5,242,758</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">5,324,718</td>
<td align="right">5,242,758</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">13,311,947</td>
<td align="right">13,107,087</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">6,655,900</td>
<td align="right">6,553,500</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">5,324,720</td>
<td align="right">5,242,800</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,993,540</td>
<td align="right">3,932,100</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,331,180</td>
<td align="right">1,310,700</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,331,180</td>
<td align="right">1,310,700</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">19,968,378</td>
<td align="right">19,661,169</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">5,324,946</td>
<td align="right">5,243,023</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">7,854,203</td>
<td align="right">7,733,368</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">23,961,616</td>
<td align="right">23,592,973</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,993,766</td>
<td align="right">3,932,323</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">19,968,076</td>
<td align="right">19,660,873</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,662,586</td>
<td align="right">2,621,623</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">3,993,992</td>
<td align="right">3,932,546</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,993,992</td>
<td align="right">3,932,546</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">15,976,194</td>
<td align="right">15,730,407</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,331,632</td>
<td align="right">1,311,146</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">61,769,930</td>
<td align="right">60,819,676</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">302,851,815</td>
<td align="right">298,193,516</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">26,625,117</td>
<td align="right">26,215,594</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">42,599,877</td>
<td align="right">41,944,673</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">89,193,393</td>
<td align="right">87,821,599</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">22,630,216</td>
<td align="right">22,282,176</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">17,971,085</td>
<td align="right">17,694,705</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">36,608,368</td>
<td align="right">36,045,436</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">81,869,862</td>
<td align="right">80,610,998</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">78,541,333</td>
<td align="right">77,333,753</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,993,769</td>
<td align="right">3,932,386</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">5,324,726</td>
<td align="right">5,242,926</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">9,318,950</td>
<td align="right">9,175,821</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,324,729</td>
<td align="right">5,242,989</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">3,327,983</td>
<td align="right">3,277,443</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">11,991,722</td>
<td align="right">11,810,306</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,331,544</td>
<td align="right">1,311,420</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,993,158</td>
<td align="right">5,903,723</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">17,311,601</td>
<td align="right">17,057,348</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,663,177</td>
<td align="right">2,624,688</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,663,584</td>
<td align="right">2,626,151</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">452</td>
<td align="right">446</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">226</td>
<td align="right">223</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">226</td>
<td align="right">223</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">226</td>
<td align="right">223</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">226</td>
<td align="right">223</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">226</td>
<td align="right">223</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">226</td>
<td align="right">223</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">226</td>
<td align="right">223</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">226</td>
<td align="right">223</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right"></td>
<td align="right">49,158,344</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,356,786</td>
<td align="right">4.1%</td>
<td align="right">1,335,832</td>
<td align="right">4.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">25,958,736</td>
<td align="right">77.9%</td>
<td align="right">25,558,888</td>
<td align="right">77.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,991,271</td>
<td align="right">18.0%</td>
<td align="right">5,899,857</td>
<td align="right">18.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">1,701</td>
<td align="right">6.2%</td>
<td align="right">3,320</td>
<td align="right">11.4%</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">25,794</td>
<td align="right">93.8%</td>
<td align="right">25,720</td>
<td align="right">88.6%</td>
<td align="right">-0.3%</td>
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
<td align="right">910</td>
<td align="right">53.5%</td>
<td align="right">1,800</td>
<td align="right">54.2%</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">364</td>
<td align="right">21.4%</td>
<td align="right">720</td>
<td align="right">21.7%</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">427</td>
<td align="right">25.1%</td>
<td align="right">800</td>
<td align="right">24.1%</td>
<td align="right">87.4%</td>
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
<td align="right">5,324,720</td>
<td align="right">100.0%</td>
<td align="right">5,242,800</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">1,356,786</td>
<td align="right">1.2%</td>
<td align="right">1,335,832</td>
<td align="right">1.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">108,495,295</td>
<td align="right">98.8%</td>
<td align="right">106,824,220</td>
<td align="right">98.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,331,387</td>
<td align="right">1.2%</td>
<td align="right">1,314,790</td>
<td align="right">1.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,335,832</td>
<td align="right">1.2%</td>
<td align="right"></td>
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
<td align="right">26,928</td>
<td align="right">100.0%</td>
<td align="right">29,117</td>
<td align="right">100.0%</td>
<td align="right">8.1%</td>
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
<td align="left">init not simple</td>
<td align="right">2</td>
<td align="right">2 / 0 !!</td>
<td align="right">42</td>
<td align="right">42 / 0 !!</td>
<td align="right">2,000.0%</td>
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
<td align="right">957</td>
<td align="right">0.0%</td>
<td align="right">1,623</td>
<td align="right">0.0%</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">19,302,320</td>
<td align="right">100.0%</td>
<td align="right">19,005,037</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">76</td>
<td align="right">54.7%</td>
<td align="right">336</td>
<td align="right">80.8%</td>
<td align="right">342.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">63</td>
<td align="right">45.3%</td>
<td align="right">80</td>
<td align="right">19.2%</td>
<td align="right">27.0%</td>
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
<td align="left">big int</td>
<td align="right">63</td>
<td align="right">100.0%</td>
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">27.0%</td>
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
<td align="right">1,331,180</td>
<td align="right">100.0%</td>
<td align="right">1,310,700</td>
<td align="right">99.9%</td>
<td align="right">-1.5%</td>
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
<td align="right">364</td>
<td align="right">100.0%</td>
<td align="right">720</td>
<td align="right">100.0%</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">str</td>
<td align="right">364</td>
<td align="right">100.0%</td>
<td align="right">720</td>
<td align="right">100.0%</td>
<td align="right">97.8%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">233</td>
<td align="right">0.0%</td>
<td align="right">370</td>
<td align="right">0.0%</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,523,016</td>
<td align="right">100.0%</td>
<td align="right">6,422,521</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">53.8%</td>
<td align="right">147</td>
<td align="right">69.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6</td>
<td align="right">46.2%</td>
<td align="right">66</td>
<td align="right">31.0%</td>
<td align="right">1,000.0%</td>
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
<td align="right">6</td>
<td align="right">100.0%</td>
<td align="right">66</td>
<td align="right">100.0%</td>
<td align="right">1,000.0%</td>
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
<td align="right">3,993,540</td>
<td align="right">3,993,540 / 0 !!</td>
<td align="right">3,932,100</td>
<td align="right">3,932,100 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">226</td>
<td align="right">226 / 0 !!</td>
<td align="right">223</td>
<td align="right">223 / 0 !!</td>
<td align="right">-1.3%</td>
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
<td align="right">188,379,793</td>
<td align="right">91.0%</td>
<td align="right">185,477,193</td>
<td align="right">91.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,343,834</td>
<td align="right">0.6%</td>
<td align="right">1,323,158</td>
<td align="right">0.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">17,305,833</td>
<td align="right">8.4%</td>
<td align="right">17,044,673</td>
<td align="right">8.4%</td>
<td align="right">-1.5%</td>
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
<td align="right">4,645</td>
<td align="right">14.9%</td>
<td align="right">7,829</td>
<td align="right">20.8%</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">26,473</td>
<td align="right">85.1%</td>
<td align="right">29,804</td>
<td align="right">79.2%</td>
<td align="right">12.6%</td>
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
<td align="right">364</td>
<td align="right">7.8%</td>
<td align="right">720</td>
<td align="right">9.2%</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,120</td>
<td align="right">67.2%</td>
<td align="right">4,880</td>
<td align="right">62.3%</td>
<td align="right">56.4%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">588</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">2,263</td>
<td align="right">0.0%</td>
<td align="right">1,785.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">95,848,203</td>
<td align="right">100.0%</td>
<td align="right">94,372,098</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">674</td>
<td align="right">100.0%</td>
<td align="right">2,137</td>
<td align="right">100.0%</td>
<td align="right">217.1%</td>
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
<td align="right">29,285,916</td>
<td align="right">91.7%</td>
<td align="right">28,834,476</td>
<td align="right">91.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,662,405</td>
<td align="right">8.3%</td>
<td align="right">2,622,324</td>
<td align="right">8.3%</td>
<td align="right">-1.5%</td>
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
<td align="right">44</td>
<td align="right">5.7%</td>
<td align="right">924</td>
<td align="right">39.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">728</td>
<td align="right">94.3%</td>
<td align="right">1,440</td>
<td align="right">60.9%</td>
<td align="right">97.8%</td>
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
<td align="left">other</td>
<td align="right">1,092</td>
<td align="right">150.0%</td>
<td align="right">2,160</td>
<td align="right">150.0%</td>
<td align="right">97.8%</td>
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
<td align="right">3</td>
<td align="right">100.0%</td>
<td align="right">63</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">1,343,834</td>
<td align="right">1.6%</td>
<td align="right">1,323,158</td>
<td align="right">1.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">79,876,993</td>
<td align="right">95.2%</td>
<td align="right">78,648,542</td>
<td align="right">95.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,662,661</td>
<td align="right">3.2%</td>
<td align="right">2,623,198</td>
<td align="right">3.2%</td>
<td align="right">-1.5%</td>
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
<td align="right">794</td>
<td align="right">3.0%</td>
<td align="right">1,504</td>
<td align="right">5.4%</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">25,479</td>
<td align="right">97.0%</td>
<td align="right">26,407</td>
<td align="right">94.6%</td>
<td align="right">3.6%</td>
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
<td align="right">728</td>
<td align="right">91.7%</td>
<td align="right">1,440</td>
<td align="right">95.7%</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">66</td>
<td align="right">8.3%</td>
<td align="right">64</td>
<td align="right">4.3%</td>
<td align="right">-3.0%</td>
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
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">105</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,331,401</td>
<td align="right">100.0%</td>
<td align="right">1,310,818</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
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
<td align="right">65</td>
<td align="right">100.0%</td>
<td align="right">105</td>
<td align="right">100.0%</td>
<td align="right">61.5%</td>
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
<td align="right">847,195,104</td>
<td align="right">54.1%</td>
<td align="right">883,326,927</td>
<td align="right">55.5%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">673,354,577</td>
<td align="right">43.0%</td>
<td align="right">662,981,792</td>
<td align="right">41.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">5,401,268</td>
<td align="right">0.3%</td>
<td align="right">5,318,568</td>
<td align="right">0.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">39,285,288</td>
<td align="right">2.5%</td>
<td align="right">38,713,823</td>
<td align="right">2.4%</td>
<td align="right">-1.5%</td>
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
<td align="left">LOAD_GLOBAL</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">2,263</td>
<td align="right">0.0%</td>
<td align="right">1,785.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">957</td>
<td align="right">0.0%</td>
<td align="right">1,623</td>
<td align="right">0.0%</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">233</td>
<td align="right">0.0%</td>
<td align="right">370</td>
<td align="right">0.0%</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">5,324,720</td>
<td align="right">14.5%</td>
<td align="right">5,242,800</td>
<td align="right">14.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,331,180</td>
<td align="right">3.6%</td>
<td align="right">1,310,700</td>
<td align="right">3.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,991,271</td>
<td align="right">16.4%</td>
<td align="right">5,899,857</td>
<td align="right">16.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">17,305,833</td>
<td align="right">47.3%</td>
<td align="right">17,044,673</td>
<td align="right">47.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,662,405</td>
<td align="right">7.3%</td>
<td align="right">2,622,324</td>
<td align="right">7.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,662,661</td>
<td align="right">7.3%</td>
<td align="right">2,623,198</td>
<td align="right">7.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,331,387</td>
<td align="right">3.6%</td>
<td align="right">1,314,790</td>
<td align="right">3.6%</td>
<td align="right">-1.2%</td>
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
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">14</td>
<td align="right">0.0%</td>
<td align="right">294</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14</td>
<td align="right">0.0%</td>
<td align="right">294</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">672,706</td>
<td align="right">12.5%</td>
<td align="right">660,658</td>
<td align="right">12.4%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,356,786</td>
<td align="right">25.1%</td>
<td align="right">1,335,832</td>
<td align="right">25.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,356,786</td>
<td align="right">25.1%</td>
<td align="right">1,335,832</td>
<td align="right">25.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,343,834</td>
<td align="right">24.9%</td>
<td align="right">1,323,158</td>
<td align="right">24.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">671,128</td>
<td align="right">12.4%</td>
<td align="right">662,500</td>
<td align="right">12.5%</td>
<td align="right">-1.3%</td>
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
<td align="left">INTERPRETER_EXIT</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">105</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">78,541,653</td>
<td align="right">95.9%</td>
<td align="right">77,333,332</td>
<td align="right">95.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">81,869,862</td>
<td align="right">100.0%</td>
<td align="right">80,610,998</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">3,993,691</td>
<td align="right">4.9%</td>
<td align="right">3,932,309</td>
<td align="right">4.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">3,328,209</td>
<td align="right">4.1%</td>
<td align="right">3,277,666</td>
<td align="right">4.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">3,328,209</td>
<td align="right">4.1%</td>
<td align="right">3,277,666</td>
<td align="right">4.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">3,328,209</td>
<td align="right">4.1%</td>
<td align="right">3,277,666</td>
<td align="right">4.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">3,328,209</td>
<td align="right">4.1%</td>
<td align="right">3,277,666</td>
<td align="right">4.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">226</td>
<td align="right">0.0%</td>
<td align="right">223</td>
<td align="right">0.0%</td>
<td align="right">-1.3%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
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
<td align="right">73</td>
<td align="right"></td>
<td align="right">1,054</td>
<td align="right"></td>
<td align="right">1,343.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">431</td>
<td align="right"></td>
<td align="right">4,087</td>
<td align="right"></td>
<td align="right">848.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">418</td>
<td align="right"></td>
<td align="right">3,822</td>
<td align="right"></td>
<td align="right">814.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">950</td>
<td align="right">0.0%</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">43,787,570</td>
<td align="right"></td>
<td align="right">42,927,561</td>
<td align="right"></td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">43,789,308</td>
<td align="right">45.0%</td>
<td align="right">42,930,295</td>
<td align="right">44.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">43,789,456</td>
<td align="right">45.0%</td>
<td align="right">42,930,441</td>
<td align="right">44.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">246,120,578</td>
<td align="right">30.6%</td>
<td align="right">242,161,156</td>
<td align="right">30.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">350,125,015</td>
<td align="right">43.6%</td>
<td align="right">344,735,030</td>
<td align="right">43.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,331,180</td>
<td align="right"></td>
<td align="right">1,310,700</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">1,331,180</td>
<td align="right">100.0%</td>
<td align="right">1,310,700</td>
<td align="right">100.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">27,955,018</td>
<td align="right">3.5%</td>
<td align="right">27,525,175</td>
<td align="right">3.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">229,620,047</td>
<td align="right">26.9%</td>
<td align="right">226,098,946</td>
<td align="right">26.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">408,810,930</td>
<td align="right">48.0%</td>
<td align="right">402,550,308</td>
<td align="right">48.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">11,980,990</td>
<td align="right"></td>
<td align="right">11,797,625</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">213,666,019</td>
<td align="right">25.1%</td>
<td align="right">210,397,221</td>
<td align="right">25.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">179,042,394</td>
<td align="right">22.3%</td>
<td align="right">176,311,178</td>
<td align="right">22.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">57,259,159</td>
<td align="right"></td>
<td align="right">56,388,297</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">141</td>
<td align="right">0.0%</td>
<td align="right">139</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">53,515,121</td>
<td align="right">55.0%</td>
<td align="right">52,905,699</td>
<td align="right">55.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">53,516,461</td>
<td align="right"></td>
<td align="right">52,907,033</td>
<td align="right"></td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">7</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-27
