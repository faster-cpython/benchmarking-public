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
<td align="right">19,052,901</td>
<td align="right">10,668</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">793,506</td>
<td align="right">9,282</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,070,811</td>
<td align="right">13,335</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">277,032</td>
<td align="right">3,780</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">363,132</td>
<td align="right">5,208</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">535,311</td>
<td align="right">8,043</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,221,276</td>
<td align="right">19,278</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">602,238</td>
<td align="right">9,534</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">516,474</td>
<td align="right">8,442</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,485,119</td>
<td align="right">41,979</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,226,966</td>
<td align="right">37,842</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,227,008</td>
<td align="right">37,884</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,227,050</td>
<td align="right">37,926</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,227,050</td>
<td align="right">37,926</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,227,134</td>
<td align="right">38,010</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,231,586</td>
<td align="right">41,685</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,982,774</td>
<td align="right">119,700</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,982,984</td>
<td align="right">119,910</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,456,496</td>
<td align="right">50,568</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,733,423</td>
<td align="right">56,679</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,733,465</td>
<td align="right">56,721</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,436,442</td>
<td align="right">30,933</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,106,826</td>
<td align="right">29,400</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">147,523,089</td>
<td align="right">101,297,784</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">187,526,241</td>
<td align="right">145,013,463</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">46,947,495</td>
<td align="right">37,953,321</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">461,483,169</td>
<td align="right">378,515,823</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">263,298,945</td>
<td align="right">220,613,883</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">127,119,237</td>
<td align="right">107,136,372</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">22,455,153</td>
<td align="right">18,951,744</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">22,455,405</td>
<td align="right">18,951,996</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">134,278,452</td>
<td align="right">113,436,351</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">7,456,428</td>
<td align="right">6,324,780</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">133,523,061</td>
<td align="right">113,436,288</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">359,558,178</td>
<td align="right">308,938,098</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">351,611,736</td>
<td align="right">302,622,852</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,011,166,317</td>
<td align="right">870,333,030</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">146,693,295</td>
<td align="right">126,352,212</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">171,323,523</td>
<td align="right">151,236,750</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">177,691,395</td>
<td align="right">157,539,186</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">487,547,466</td>
<td align="right">447,373,920</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">27,493,956</td>
<td align="right">25,229,043</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">61,766,397</td>
<td align="right">56,783,097</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">81,469,395</td>
<td align="right">75,705,483</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">240,697,884</td>
<td align="right">227,063,970</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">6,663,342</td>
<td align="right">6,305,418</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">26,356,512</td>
<td align="right">25,224,864</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">138,283,593</td>
<td align="right">132,422,073</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">78,610,749</td>
<td align="right">75,660,753</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">19,158,237</td>
<td align="right">18,904,221</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">76,135,437</td>
<td align="right">75,608,169</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">37,972,032</td>
<td align="right">37,802,688</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">37,972,032</td>
<td align="right">37,802,688</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">18,986,016</td>
<td align="right">18,901,344</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">37,972,095</td>
<td align="right">37,802,751</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">81,900,189</td>
<td align="right">81,900,189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">75,620,391</td>
<td align="right">75,620,391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">75,600,252</td>
<td align="right">75,600,252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">75,600,189</td>
<td align="right">75,600,189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">75,600,000</td>
<td align="right">75,600,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">75,599,958</td>
<td align="right">75,599,958</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">75,599,916</td>
<td align="right">75,599,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">75,599,916</td>
<td align="right">75,599,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">56,700,210</td>
<td align="right">56,700,210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">37,799,916</td>
<td align="right">37,799,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">12,600,210</td>
<td align="right">12,600,210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">6,300,105</td>
<td align="right">6,300,105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,864</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,856</td>
<td align="right">2,856</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">567</td>
<td align="right">567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">546</td>
<td align="right">546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">462</td>
<td align="right">462</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">336</td>
<td align="right">336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">336</td>
<td align="right">336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">294</td>
<td align="right">294</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">210</td>
<td align="right">210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">147</td>
<td align="right">147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">42</td>
<td align="right">42</td>
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
<td align="right">75,600,651</td>
<td align="right">31.6%</td>
<td align="right">75,600,651</td>
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
<td align="right">163,800,546</td>
<td align="right">68.4%</td>
<td align="right">163,800,546</td>
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
<td align="right">462</td>
<td align="right">2.3%</td>
<td align="right">462</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">19,278</td>
<td align="right">97.7%</td>
<td align="right">19,278</td>
<td align="right">97.7%</td>
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
<td align="right">19,257</td>
<td align="right">99.9%</td>
<td align="right">19,257</td>
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
<td align="right">1,932</td>
<td align="right">0.0%</td>
<td align="right">1,932</td>
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
<td align="right">2,123,101,155</td>
<td align="right">100.0%</td>
<td align="right">2,123,101,155</td>
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
<td align="right">1,932</td>
<td align="right">100.0%</td>
<td align="right">1,932</td>
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
<td align="right">42</td>
<td align="right">50.0%</td>
<td align="right">42</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
<td align="right">42</td>
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
<td align="right">168</td>
<td align="right">0.0%</td>
<td align="right">168</td>
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
<td align="right">63,000,084</td>
<td align="right">100.0%</td>
<td align="right">63,000,084</td>
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
<td align="right">168</td>
<td align="right">100.0%</td>
<td align="right">168</td>
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
<td align="right">147</td>
<td align="right">0.0%</td>
<td align="right">147</td>
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
<td align="right">327,600,168</td>
<td align="right">100.0%</td>
<td align="right">327,600,168</td>
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
<td align="right">147</td>
<td align="right">100.0%</td>
<td align="right">147</td>
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
<td align="right">836,892</td>
<td align="right">35.9%</td>
<td align="right">13,440</td>
<td align="right">27.4%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,491,210</td>
<td align="right">64.0%</td>
<td align="right">35,238</td>
<td align="right">71.9%</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">210</td>
<td align="right">0.0%</td>
<td align="right">210</td>
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
<td align="left">Success</td>
<td align="right">15,834</td>
<td align="right">99.7%</td>
<td align="right">336</td>
<td align="right">88.9%</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">42</td>
<td align="right">11.1%</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
<td align="right">42</td>
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
<td align="right">37,800,126</td>
<td align="right">37,800,126 / 0 !!</td>
<td align="right">37,800,126</td>
<td align="right">37,800,126 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">37,800,000</td>
<td align="right">37,800,000 / 0 !!</td>
<td align="right">37,800,000</td>
<td align="right">37,800,000 / 0 !!</td>
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
<td align="right">2,228,730</td>
<td align="right">0.6%</td>
<td align="right">39,606</td>
<td align="right">0.0%</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">356,297,046</td>
<td align="right">99.4%</td>
<td align="right">346,676,547</td>
<td align="right">100.0%</td>
<td align="right">-2.7%</td>
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
<td align="right">1,407</td>
<td align="right">49.3%</td>
<td align="right">630</td>
<td align="right">30.3%</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,449</td>
<td align="right">50.7%</td>
<td align="right">1,449</td>
<td align="right">69.7%</td>
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
<td align="right">1,365</td>
<td align="right">97.0%</td>
<td align="right">588</td>
<td align="right">93.3%</td>
<td align="right">-56.9%</td>
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
<td align="right">226,133,838</td>
<td align="right">100.0%</td>
<td align="right">176,958,537</td>
<td align="right">100.0%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,428</td>
<td align="right">0.0%</td>
<td align="right">1,428</td>
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
<td align="right">1,428</td>
<td align="right">100.0%</td>
<td align="right">1,428</td>
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
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
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
<td align="right">75,599,958</td>
<td align="right">100.0%</td>
<td align="right">75,599,958</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
<td align="right">42</td>
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
<td align="right">105</td>
<td align="right">0.0%</td>
<td align="right">105</td>
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
<td align="right">75,600,084</td>
<td align="right">100.0%</td>
<td align="right">75,600,084</td>
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
<td align="right">105</td>
<td align="right">100.0%</td>
<td align="right">105</td>
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
<td align="right">1,434,447</td>
<td align="right">0.1%</td>
<td align="right">29,547</td>
<td align="right">0.0%</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,054,164,489</td>
<td align="right">99.9%</td>
<td align="right">1,014,368,103</td>
<td align="right">100.0%</td>
<td align="right">-3.8%</td>
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
<td align="right">1,176</td>
<td align="right">58.9%</td>
<td align="right">567</td>
<td align="right">40.9%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">819</td>
<td align="right">41.1%</td>
<td align="right">819</td>
<td align="right">59.1%</td>
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
<td align="right">462</td>
<td align="right">39.3%</td>
<td align="right">210</td>
<td align="right">37.0%</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">672</td>
<td align="right">57.1%</td>
<td align="right">315</td>
<td align="right">55.6%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">42</td>
<td align="right">3.6%</td>
<td align="right">42</td>
<td align="right">7.4%</td>
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
<td align="right">231</td>
<td align="right">0.0%</td>
<td align="right">231</td>
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
<td align="right">283,499,958</td>
<td align="right">100.0%</td>
<td align="right">283,499,958</td>
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
<td align="right">231</td>
<td align="right">100.0%</td>
<td align="right">231</td>
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
<td align="right">837,228</td>
<td align="right">0.0%</td>
<td align="right">15,330</td>
<td align="right">0.0%</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,639,985,802</td>
<td align="right">27.6%</td>
<td align="right">1,425,724,440</td>
<td align="right">27.4%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">4,214,099,337</td>
<td align="right">71.0%</td>
<td align="right">3,701,123,013</td>
<td align="right">71.1%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">81,523,995</td>
<td align="right">1.4%</td>
<td align="right">75,739,461</td>
<td align="right">1.5%</td>
<td align="right">-7.1%</td>
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
<td align="right">2,228,730</td>
<td align="right">2.8%</td>
<td align="right">39,606</td>
<td align="right">0.1%</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,434,447</td>
<td align="right">1.8%</td>
<td align="right">29,547</td>
<td align="right">0.0%</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">75,600,651</td>
<td align="right">95.4%</td>
<td align="right">75,600,651</td>
<td align="right">99.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,932</td>
<td align="right">0.0%</td>
<td align="right">1,932</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,428</td>
<td align="right">0.0%</td>
<td align="right">1,428</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">231</td>
<td align="right">0.0%</td>
<td align="right">231</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">210</td>
<td align="right">0.0%</td>
<td align="right">210</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">168</td>
<td align="right">0.0%</td>
<td align="right">168</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">147</td>
<td align="right">0.0%</td>
<td align="right">147</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105</td>
<td align="right">0.0%</td>
<td align="right">105</td>
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
<td align="right">336</td>
<td align="right">0.0%</td>
<td align="right">1,890</td>
<td align="right">11.0%</td>
<td align="right">462.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">336</td>
<td align="right">0.0%</td>
<td align="right">1,890</td>
<td align="right">11.0%</td>
<td align="right">462.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">418,404</td>
<td align="right">50.0%</td>
<td align="right">6,678</td>
<td align="right">38.8%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">418,488</td>
<td align="right">50.0%</td>
<td align="right">6,762</td>
<td align="right">39.3%</td>
<td align="right">-98.4%</td>
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
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">56,700,336</td>
<td align="right">8.9%</td>
<td align="right">56,700,336</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">579,600,924</td>
<td align="right">91.1%</td>
<td align="right">579,600,924</td>
<td align="right">91.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">56,700,336</td>
<td align="right">8.9%</td>
<td align="right">56,700,336</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">56,700,336</td>
<td align="right">8.9%</td>
<td align="right">56,700,336</td>
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
<td align="right">56,700,336</td>
<td align="right">8.9%</td>
<td align="right">56,700,336</td>
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
<td align="right">18,900,000</td>
<td align="right">3.0%</td>
<td align="right">18,900,000</td>
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
<td align="right">37,800,000</td>
<td align="right">5.9%</td>
<td align="right">37,800,000</td>
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
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">711,901,176</td>
<td align="right">111.9%</td>
<td align="right">711,901,176</td>
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
<td align="left">Method cache collisions</td>
<td align="right">598</td>
<td align="right"></td>
<td align="right">693</td>
<td align="right"></td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">209</td>
<td align="right"></td>
<td align="right">235</td>
<td align="right"></td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,042,272,084</td>
<td align="right">14.8%</td>
<td align="right">945,761,166</td>
<td align="right">13.5%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">777</td>
<td align="right">0.0%</td>
<td align="right">735</td>
<td align="right">0.0%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,886,770,250</td>
<td align="right">37.5%</td>
<td align="right">2,803,995,474</td>
<td align="right">36.5%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">654</td>
<td align="right"></td>
<td align="right">638</td>
<td align="right"></td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">96,727,176</td>
<td align="right">1.4%</td>
<td align="right">94,538,052</td>
<td align="right">1.3%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">4,420,999,672</td>
<td align="right">62.8%</td>
<td align="right">4,497,493,127</td>
<td align="right">64.2%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">3,855,408,782</td>
<td align="right">50.1%</td>
<td align="right">3,918,167,923</td>
<td align="right">51.1%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,484,272,950</td>
<td align="right">21.1%</td>
<td align="right">1,467,888,025</td>
<td align="right">21.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">94,505,016</td>
<td align="right"></td>
<td align="right">94,504,465</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">592,206,657</td>
<td align="right"></td>
<td align="right">592,205,838</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">592,206,846</td>
<td align="right">45.6%</td>
<td align="right">592,206,027</td>
<td align="right">45.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">951,318,665</td>
<td align="right">12.4%</td>
<td align="right">951,317,540</td>
<td align="right">12.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">510,301,975</td>
<td align="right"></td>
<td align="right">510,301,781</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">705,601,953</td>
<td align="right">54.4%</td>
<td align="right">705,601,911</td>
<td align="right">54.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">800,101,442</td>
<td align="right"></td>
<td align="right">800,101,468</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">705,601,176</td>
<td align="right">54.4%</td>
<td align="right">705,601,176</td>
<td align="right">54.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">126</td>
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
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">126</td>
<td align="right">0.4%</td>
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
<td align="right">446,138,679</td>
<td align="right"></td>
<td align="right">361,134,711</td>
<td align="right"></td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">714</td>
<td align="right">2.2%</td>
<td align="right">630</td>
<td align="right">2.2%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">32,550</td>
<td align="right"></td>
<td align="right">29,274</td>
<td align="right"></td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">31,836</td>
<td align="right">97.8%</td>
<td align="right">28,644</td>
<td align="right">97.8%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">36,274,067,193</td>
<td align="right">8,130.7%</td>
<td align="right">37,155,619,242</td>
<td align="right">10,288.6%</td>
<td align="right">2.4%</td>
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
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="right">714</td>
<td align="right"></td>
<td align="right">630</td>
<td align="right"></td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">588</td>
<td align="right">82.4%</td>
<td align="right">546</td>
<td align="right">86.7%</td>
<td align="right">-7.1%</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">860,160</td>
<td align="right">3.7%</td>
<td align="right">172,032</td>
<td align="right">0.8%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">1,625,274</td>
<td align="right">7.0%</td>
<td align="right">1,141,203</td>
<td align="right">5.1%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">23,138,304</td>
<td align="right"></td>
<td align="right">22,536,192</td>
<td align="right"></td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">462,672</td>
<td align="right">2.0%</td>
<td align="right">451,752</td>
<td align="right">2.0%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">21,050,358</td>
<td align="right">91.0%</td>
<td align="right">20,943,237</td>
<td align="right">92.9%</td>
<td align="right">-0.5%</td>
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
<td align="left">315</td>
<td align="right">53.6%</td>
<td align="left">210</td>
<td align="right">38.5%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">273</td>
<td align="right">46.4%</td>
<td align="left">336</td>
<td align="right">61.5%</td>
<td align="right">23.1%</td>
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
<td align="right">147</td>
<td align="right">20.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">420</td>
<td align="right">58.8%</td>
<td align="right">483</td>
<td align="right">76.7%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">147</td>
<td align="right">20.6%</td>
<td align="right">147</td>
<td align="right">23.3%</td>
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
<td align="left"><= 128</td>
<td align="right">42</td>
<td align="right">5.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">357</td>
<td align="right">50.0%</td>
<td align="right">399</td>
<td align="right">63.3%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">189</td>
<td align="right">26.5%</td>
<td align="right">147</td>
<td align="right">23.3%</td>
<td align="right">-22.2%</td>
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
<td align="right">336</td>
<td align="right">1,890</td>
<td align="right">462.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">131,908,224</td>
<td align="right">201,569,928</td>
<td align="right">52.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">235,780,608</td>
<td align="right">144,879,630</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">68,898,564</td>
<td align="right">88,183,158</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">94,203,774</td>
<td align="right">113,371,398</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">446,138,280</td>
<td align="right">361,132,758</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">446,138,679</td>
<td align="right">361,134,711</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">106,593,606</td>
<td align="right">125,980,806</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">224,353,710</td>
<td align="right">264,527,256</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">112,176,855</td>
<td align="right">132,263,628</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">112,176,855</td>
<td align="right">132,263,628</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">483,833,553</td>
<td align="right">398,933,073</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">272,373,654</td>
<td align="right">314,886,432</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">131,908,224</td>
<td align="right">151,170,810</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">154,154,910</td>
<td align="right">176,326,899</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">478,592,058</td>
<td align="right">522,747,834</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">977,260,767</td>
<td align="right">1,051,737,708</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">4,942,881,531</td>
<td align="right">5,202,283,380</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">584,264,751</td>
<td align="right">613,016,397</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">1,162,712,313</td>
<td align="right">1,215,612,489</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">1,228,982,685</td>
<td align="right">1,284,844,533</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">18,106,578</td>
<td align="right">18,890,802</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">18,106,578</td>
<td align="right">18,890,802</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">12,083,778</td>
<td align="right">12,591,810</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,041,889</td>
<td align="right">6,295,905</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">6,041,889</td>
<td align="right">6,295,905</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">6,041,889</td>
<td align="right">6,295,905</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">6,041,889</td>
<td align="right">6,295,905</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">6,041,889</td>
<td align="right">6,295,905</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">6,041,889</td>
<td align="right">6,295,905</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">6,041,889</td>
<td align="right">6,295,905</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">818,248,494</td>
<td align="right">850,233,951</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,939,719,999</td>
<td align="right">2,009,127,057</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">54,750,150</td>
<td align="right">56,666,022</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,166,823,777</td>
<td align="right">1,202,976,012</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">36,643,572</td>
<td align="right">37,775,220</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">36,643,572</td>
<td align="right">37,775,220</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right">36,643,572</td>
<td align="right">37,775,220</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">79,414,965</td>
<td align="right">81,858,105</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">79,414,965</td>
<td align="right">81,858,105</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">79,414,965</td>
<td align="right">81,858,105</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">152,788,041</td>
<td align="right">157,420,305</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">73,373,076</td>
<td align="right">75,562,200</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">73,373,076</td>
<td align="right">75,562,200</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">73,373,076</td>
<td align="right">75,562,200</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">73,373,076</td>
<td align="right">75,562,200</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">73,373,076</td>
<td align="right">75,562,200</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">73,373,076</td>
<td align="right">75,562,200</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">73,373,076</td>
<td align="right">75,562,200</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">73,373,076</td>
<td align="right">75,562,200</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">55,266,498</td>
<td align="right">56,671,398</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">5,635,699,524</td>
<td align="right">5,762,860,425</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">24,664,815</td>
<td align="right">25,192,083</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">111,316,464</td>
<td align="right">113,367,828</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">210,386,736</td>
<td align="right">214,144,161</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">204,344,847</td>
<td align="right">207,848,256</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">204,344,847</td>
<td align="right">207,848,256</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">204,344,847</td>
<td align="right">207,848,256</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">374,221,974</td>
<td align="right">379,984,962</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">632,679,810</td>
<td align="right">642,413,100</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">608,052,627</td>
<td align="right">617,245,125</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">18,622,926</td>
<td align="right">18,896,178</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">18,622,926</td>
<td align="right">18,896,178</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">18,622,926</td>
<td align="right">18,896,178</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">639,752,946</td>
<td align="right">648,747,120</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">161,506,485</td>
<td align="right">163,771,398</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">161,506,485</td>
<td align="right">163,771,398</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">559,306,734</td>
<td align="right">566,850,900</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">888,761,433</td>
<td align="right">900,686,367</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">553,264,845</td>
<td align="right">560,554,995</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">230,194,902</td>
<td align="right">233,042,544</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">504,059,325</td>
<td align="right">510,176,415</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">641,736,123</td>
<td align="right">634,025,112</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">498,017,436</td>
<td align="right">503,880,510</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">498,017,436</td>
<td align="right">503,880,510</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">498,017,436</td>
<td align="right">503,880,510</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">498,017,436</td>
<td align="right">503,880,510</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">498,017,436</td>
<td align="right">503,880,510</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">498,017,436</td>
<td align="right">503,880,510</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">498,017,436</td>
<td align="right">503,880,510</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">647,440,143</td>
<td align="right">655,060,098</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">205,530,087</td>
<td align="right">207,850,461</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">485,933,658</td>
<td align="right">491,288,700</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">242,966,661</td>
<td align="right">245,643,405</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">242,966,661</td>
<td align="right">245,643,405</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">242,966,661</td>
<td align="right">245,643,405</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">37,436,910</td>
<td align="right">37,794,834</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">37,436,910</td>
<td align="right">37,794,834</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">205,978,962</td>
<td align="right">207,876,207</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">37,627,968</td>
<td align="right">37,797,312</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">37,627,968</td>
<td align="right">37,797,312</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">37,627,968</td>
<td align="right">37,797,312</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">18,813,984</td>
<td align="right">18,898,656</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">18,813,984</td>
<td align="right">18,898,656</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">37,694,874</td>
<td align="right">37,798,362</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">36,385,860</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">63</td>
<td align="right">63</td>
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
Stats gathered on: 2025-07-02
