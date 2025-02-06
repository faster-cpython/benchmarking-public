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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">12,040</td>
<td align="right">1,558,160</td>
<td align="right">12,841.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">41,440</td>
<td align="right">1,587,560</td>
<td align="right">3,731.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">90,880</td>
<td align="right">1,637,000</td>
<td align="right">1,701.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">285,720</td>
<td align="right">4,622,380</td>
<td align="right">1,517.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">70,980</td>
<td align="right">844,000</td>
<td align="right">1,089.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">24,060</td>
<td align="right">266,720</td>
<td align="right">1,008.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">40</td>
<td align="right">400</td>
<td align="right">900.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">90,300</td>
<td align="right">863,320</td>
<td align="right">856.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">94,600</td>
<td align="right">867,700</td>
<td align="right">817.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">126,920</td>
<td align="right">711,960</td>
<td align="right">461.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">84,840</td>
<td align="right">412,440</td>
<td align="right">386.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">162,420</td>
<td align="right">573,220</td>
<td align="right">252.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">57,680</td>
<td align="right">178,700</td>
<td align="right">209.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,529,480</td>
<td align="right">8,716,420</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">566,940</td>
<td align="right">898,600</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,982,940</td>
<td align="right">2,986,000</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">742,560</td>
<td align="right">1,023,640</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,438,700</td>
<td align="right">12,492,780</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,008,660</td>
<td align="right">1,332,260</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">340</td>
<td align="right">420</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">17,767,580</td>
<td align="right">21,128,760</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">56,339,400</td>
<td align="right">65,027,580</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">23,909,920</td>
<td align="right">26,925,280</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,887,620</td>
<td align="right">2,117,580</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">7,740,520</td>
<td align="right">8,513,620</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">111,055,680</td>
<td align="right">121,560,140</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">31,534,660</td>
<td align="right">34,368,500</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">189,780,820</td>
<td align="right">206,824,720</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,308,820</td>
<td align="right">8,993,700</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">30,517,080</td>
<td align="right">32,528,840</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">13,737,740</td>
<td align="right">14,635,160</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">16,887,940</td>
<td align="right">17,808,800</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">14,359,940</td>
<td align="right">15,084,520</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">15,999,120</td>
<td align="right">16,724,240</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">4,426,440</td>
<td align="right">4,605,320</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,265,880</td>
<td align="right">3,386,900</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">22,045,160</td>
<td align="right">21,272,680</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">35,308,220</td>
<td align="right">36,538,020</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">42,263,380</td>
<td align="right">43,559,020</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">13,526,300</td>
<td align="right">13,915,860</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">49,487,580</td>
<td align="right">50,720,400</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">19,736,860</td>
<td align="right">20,188,300</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">34,928,800</td>
<td align="right">35,380,240</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">22,576,100</td>
<td align="right">22,750,980</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,050,040</td>
<td align="right">2,050,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">920,100</td>
<td align="right">920,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">959,100</td>
<td align="right">959,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,568,160</td>
<td align="right">2,568,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">28,687,980</td>
<td align="right">28,688,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">55,358,040</td>
<td align="right">55,358,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">15,065,940</td>
<td align="right">15,065,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">8,497,080</td>
<td align="right">8,497,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,572,100</td>
<td align="right">3,572,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,975,260</td>
<td align="right">1,975,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">1,887,540</td>
<td align="right">1,887,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,858,800</td>
<td align="right">1,858,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,296,120</td>
<td align="right">1,296,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">796,020</td>
<td align="right">796,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">105,420</td>
<td align="right">105,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">67,800</td>
<td align="right">67,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">53,340</td>
<td align="right">53,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">48,600</td>
<td align="right">48,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">46,140</td>
<td align="right">46,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">46,140</td>
<td align="right">46,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">41,600</td>
<td align="right">41,600</td>
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
<td align="right">41,220</td>
<td align="right">41,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">38,940</td>
<td align="right">38,940</td>
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
<td align="right">19,140</td>
<td align="right">19,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,300</td>
<td align="right">2,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">240</td>
<td align="right">240</td>
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
<td align="left">TO_BOOL</td>
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
<td align="left">FOR_ITER</td>
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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
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
<td align="left">STORE_ATTR</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right"></td>
<td align="right">773,020</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">773,020</td>
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
<td align="right">95,780</td>
<td align="right">0.2%</td>
<td align="right">244,860</td>
<td align="right">0.5%</td>
<td align="right">155.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,301,520</td>
<td align="right">17.7%</td>
<td align="right">8,973,900</td>
<td align="right">18.7%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,584,560</td>
<td align="right">82.1%</td>
<td align="right">38,727,560</td>
<td align="right">80.7%</td>
<td align="right">0.4%</td>
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
<td align="right">7,300</td>
<td align="right">80.0%</td>
<td align="right">19,780</td>
<td align="right">81.0%</td>
<td align="right">171.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,820</td>
<td align="right">20.0%</td>
<td align="right">4,640</td>
<td align="right">19.0%</td>
<td align="right">154.9%</td>
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
<td align="right">5,220</td>
<td align="right">71.5%</td>
<td align="right">17,620</td>
<td align="right">89.1%</td>
<td align="right">237.5%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">2,000</td>
<td align="right">27.4%</td>
<td align="right">2,080</td>
<td align="right">10.5%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
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
<td align="right">1,300</td>
<td align="right">0.0%</td>
<td align="right">1,300</td>
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
<td align="right">20,654,080</td>
<td align="right">99.8%</td>
<td align="right">20,654,080</td>
<td align="right">99.8%</td>
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
<td align="right">43,040</td>
<td align="right">0.2%</td>
<td align="right">43,040</td>
<td align="right">0.2%</td>
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
<td align="right">840</td>
<td align="right">46.2%</td>
<td align="right">840</td>
<td align="right">46.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">980</td>
<td align="right">53.8%</td>
<td align="right">980</td>
<td align="right">53.8%</td>
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
<td align="left">out of range</td>
<td align="right">980</td>
<td align="right">100.0%</td>
<td align="right">980</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">59,466,360</td>
<td align="right">100.0%</td>
<td align="right">59,466,360</td>
<td align="right">100.0%</td>
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
<td align="right">440</td>
<td align="right">100.0%</td>
<td align="right">440</td>
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
<td align="right">103,920</td>
<td align="right">0.1%</td>
<td align="right">103,920</td>
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
<td align="right">79,657,380</td>
<td align="right">99.8%</td>
<td align="right">79,657,380</td>
<td align="right">99.8%</td>
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
<td align="right">25,440</td>
<td align="right">0.0%</td>
<td align="right">25,440</td>
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
<td align="right">26.3%</td>
<td align="right">520</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,460</td>
<td align="right">73.7%</td>
<td align="right">1,460</td>
<td align="right">73.7%</td>
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
<td align="left">big int</td>
<td align="right">960</td>
<td align="right">65.8%</td>
<td align="right">960</td>
<td align="right">65.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">420</td>
<td align="right">28.8%</td>
<td align="right">420</td>
<td align="right">28.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">40</td>
<td align="right">2.7%</td>
<td align="right">40</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">40</td>
<td align="right">2.7%</td>
<td align="right">40</td>
<td align="right">2.7%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,887,540</td>
<td align="right">100.0%</td>
<td align="right">1,887,540</td>
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
<td align="right">4,662,920</td>
<td align="right">100.0%</td>
<td align="right">9,177,460</td>
<td align="right">100.0%</td>
<td align="right">96.8%</td>
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
<td align="right">41,220</td>
<td align="right">0.0%</td>
<td align="right">41,220</td>
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
<td align="right">317,021,440</td>
<td align="right">100.0%</td>
<td align="right">317,021,440</td>
<td align="right">100.0%</td>
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
<td align="right">1,060</td>
<td align="right">0.0%</td>
<td align="right">1,060</td>
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
<td align="right">340</td>
<td align="right">85.0%</td>
<td align="right">340</td>
<td align="right">85.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60</td>
<td align="right">15.0%</td>
<td align="right">60</td>
<td align="right">15.0%</td>
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
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">40</td>
<td align="right">66.7%</td>
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
<td align="right">52,157,760</td>
<td align="right">100.0%</td>
<td align="right">53,160,820</td>
<td align="right">100.0%</td>
<td align="right">1.9%</td>
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
<td align="right">100.0%</td>
<td align="right">240</td>
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
<td align="right">100.0%</td>
<td align="right">60</td>
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
<td align="right">46,589,340</td>
<td align="right">100.0%</td>
<td align="right">46,589,340</td>
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
<td align="right">8,497,080</td>
<td align="right">100.0%</td>
<td align="right">8,497,080</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,402,900</td>
<td align="right">3.1%</td>
<td align="right">1,880,820</td>
<td align="right">4.1%</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">44,280,600</td>
<td align="right">96.9%</td>
<td align="right">44,046,060</td>
<td align="right">95.9%</td>
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
<td align="right">26,500</td>
<td align="right">99.9%</td>
<td align="right">35,520</td>
<td align="right">99.9%</td>
<td align="right">34.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,940</td>
<td align="right">99.9%</td>
<td align="right">38,940</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,568,780</td>
<td align="right">0.2%</td>
<td align="right">2,199,580</td>
<td align="right">0.2%</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">371,957,280</td>
<td align="right">39.9%</td>
<td align="right">414,741,400</td>
<td align="right">40.9%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,459,020</td>
<td align="right">0.9%</td>
<td align="right">9,143,900</td>
<td align="right">0.9%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">550,958,560</td>
<td align="right">59.1%</td>
<td align="right">587,735,760</td>
<td align="right">58.0%</td>
<td align="right">6.7%</td>
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
<td align="right">8,301,520</td>
<td align="right">98.3%</td>
<td align="right">8,973,900</td>
<td align="right">98.4%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,920</td>
<td align="right">1.2%</td>
<td align="right">103,920</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">41,220</td>
<td align="right">0.5%</td>
<td align="right">41,220</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,300</td>
<td align="right">0.0%</td>
<td align="right">1,300</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="left">CALL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
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
<td align="right">500</td>
<td align="right">0.0%</td>
<td align="right">4,300</td>
<td align="right">0.2%</td>
<td align="right">760.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">64,760</td>
<td align="right">4.1%</td>
<td align="right">303,820</td>
<td align="right">13.8%</td>
<td align="right">369.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">66,140</td>
<td align="right">4.2%</td>
<td align="right">305,000</td>
<td align="right">13.8%</td>
<td align="right">361.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">95,780</td>
<td align="right">6.1%</td>
<td align="right">244,860</td>
<td align="right">11.1%</td>
<td align="right">155.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">636,000</td>
<td align="right">40.5%</td>
<td align="right">636,000</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">636,000</td>
<td align="right">40.5%</td>
<td align="right">636,000</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">43,040</td>
<td align="right">2.7%</td>
<td align="right">43,040</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">19,080</td>
<td align="right">1.2%</td>
<td align="right">19,080</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,360</td>
<td align="right">0.4%</td>
<td align="right">6,360</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,060</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">4,300</td>
<td align="right">0.2%</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">55,311,840</td>
<td align="right">100.0%</td>
<td align="right">55,311,840</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">55,358,040</td>
<td align="right">100.1%</td>
<td align="right">55,358,040</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">2</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">337,865,019</td>
<td align="right">26.2%</td>
<td align="right">289,276,779</td>
<td align="right">22.9%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">180,507,435</td>
<td align="right">14.0%</td>
<td align="right">156,398,911</td>
<td align="right">12.4%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">175,668,418</td>
<td align="right">14.9%</td>
<td align="right">157,430,975</td>
<td align="right">13.7%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">177,851,480</td>
<td align="right">15.1%</td>
<td align="right">196,090,560</td>
<td align="right">17.0%</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">477,707,296</td>
<td align="right">40.6%</td>
<td align="right">429,727,435</td>
<td align="right">37.3%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">253,025,200</td>
<td align="right">19.6%</td>
<td align="right">276,011,900</td>
<td align="right">21.9%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">35</td>
<td align="right"></td>
<td align="right">32</td>
<td align="right"></td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">28</td>
<td align="right"></td>
<td align="right">26</td>
<td align="right"></td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">344,985,900</td>
<td align="right">29.3%</td>
<td align="right">368,119,940</td>
<td align="right">32.0%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">517,012,060</td>
<td align="right">40.1%</td>
<td align="right">540,771,620</td>
<td align="right">42.8%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">48,600</td>
<td align="right">0.1%</td>
<td align="right">49,680</td>
<td align="right">0.2%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">298</td>
<td align="right"></td>
<td align="right">297</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">12,040</td>
<td align="right">0.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">22,852,300</td>
<td align="right"></td>
<td align="right">22,867,760</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">22,853,720</td>
<td align="right">70.5%</td>
<td align="right">22,869,180</td>
<td align="right">70.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">9,525,402</td>
<td align="right"></td>
<td align="right">9,527,402</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">9,571,420</td>
<td align="right">29.5%</td>
<td align="right">9,572,500</td>
<td align="right">29.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">42,565</td>
<td align="right"></td>
<td align="right">42,568</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">9,510,820</td>
<td align="right">29.3%</td>
<td align="right">9,510,780</td>
<td align="right">29.3%</td>
<td align="right">-0.0%</td>
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
<td align="right">20</td>
<td align="right">22,100</td>
<td align="right">2,562,520</td>
<td align="right">9,480</td>
<td align="right">32,320</td>
<td align="right">20</td>
<td align="right">22,100</td>
<td align="right">2,568,320</td>
<td align="right">10,120</td>
<td align="right">31,820</td>
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
<td align="right">580</td>
<td align="right">11.2%</td>
<td align="right">1,400</td>
<td align="right">24.5%</td>
<td align="right">141.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">81,754,900</td>
<td align="right"></td>
<td align="right">57,682,500</td>
<td align="right"></td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,341,321,440</td>
<td align="right">2,863.8%</td>
<td align="right">2,094,001,020</td>
<td align="right">3,630.2%</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">5,180</td>
<td align="right"></td>
<td align="right">5,720</td>
<td align="right"></td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">4,600</td>
<td align="right">88.8%</td>
<td align="right">4,320</td>
<td align="right">75.5%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">4,740</td>
<td align="right">91.5%</td>
<td align="right">4,480</td>
<td align="right">78.3%</td>
<td align="right">-5.5%</td>
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
<td align="right">40</td>
<td align="right">0.7%</td>
<td align="right">40 / 0 !!</td>
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
<td align="right">580</td>
<td align="right"></td>
<td align="right">1,400</td>
<td align="right"></td>
<td align="right">141.4%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">580</td>
<td align="right">100.0%</td>
<td align="right">1,400</td>
<td align="right">100.0%</td>
<td align="right">141.4%</td>
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
<td align="right">2,397,640</td>
<td align="right">59.7%</td>
<td align="right">11,684,500</td>
<td align="right">67.6%</td>
<td align="right">387.3%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">379,840</td>
<td align="right">9.5%</td>
<td align="right">1,844,480</td>
<td align="right">10.7%</td>
<td align="right">385.6%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">4,014,080</td>
<td align="right"></td>
<td align="right">17,285,120</td>
<td align="right"></td>
<td align="right">330.6%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">1,236,600</td>
<td align="right">30.8%</td>
<td align="right">3,756,140</td>
<td align="right">21.7%</td>
<td align="right">203.7%</td>
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
<td align="right">15,810,560</td>
<td align="right">91.5%</td>
<td align="right">15,810,560 / 0 !!</td>
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
<td align="left">320</td>
<td align="right">55.2%</td>
<td align="left">260</td>
<td align="right">15.9%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">120</td>
<td align="right">20.7%</td>
<td align="left">580</td>
<td align="right">35.4%</td>
<td align="right">383.3%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">140</td>
<td align="right">24.1%</td>
<td align="left">720</td>
<td align="right">43.9%</td>
<td align="right">414.3%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">80</td>
<td align="right">4.9%</td>
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
<td align="right">200</td>
<td align="right">34.5%</td>
<td align="right">160</td>
<td align="right">11.4%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">120</td>
<td align="right">20.7%</td>
<td align="right">100</td>
<td align="right">7.1%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">120</td>
<td align="right">20.7%</td>
<td align="right">500</td>
<td align="right">35.7%</td>
<td align="right">316.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">140</td>
<td align="right">24.1%</td>
<td align="right">620</td>
<td align="right">44.3%</td>
<td align="right">342.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">1.4%</td>
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
<td align="right">80</td>
<td align="right">13.8%</td>
<td align="right">40</td>
<td align="right">2.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">140</td>
<td align="right">24.1%</td>
<td align="right">120</td>
<td align="right">8.6%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">100</td>
<td align="right">17.2%</td>
<td align="right">260</td>
<td align="right">18.6%</td>
<td align="right">160.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">180</td>
<td align="right">31.0%</td>
<td align="right">780</td>
<td align="right">55.7%</td>
<td align="right">333.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">80</td>
<td align="right">13.8%</td>
<td align="right">180</td>
<td align="right">12.9%</td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">1.4%</td>
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
<td align="right">460</td>
<td align="right">4,020</td>
<td align="right">773.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">837,900</td>
<td align="right">64,880</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">837,900</td>
<td align="right">64,880</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">837,900</td>
<td align="right">64,880</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">837,900</td>
<td align="right">64,880</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">837,900</td>
<td align="right">64,880</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">837,900</td>
<td align="right">64,880</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">689,340</td>
<td align="right">128,040</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">638,220</td>
<td align="right">128,040</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">754,700</td>
<td align="right">167,120</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">970,260</td>
<td align="right">256,100</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">970,260</td>
<td align="right">256,100</td>
<td align="right">-73.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,949,000</td>
<td align="right">1,056,140</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,962,220</td>
<td align="right">725,940</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,610,480</td>
<td align="right">648,820</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">45,168,180</td>
<td align="right">21,817,260</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">665,640</td>
<td align="right">330,200</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">4,297,520</td>
<td align="right">2,751,400</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">4,297,520</td>
<td align="right">2,751,400</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">4,297,520</td>
<td align="right">2,751,400</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">4,297,520</td>
<td align="right">2,751,400</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">5,026,100</td>
<td align="right">3,264,640</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">8,119,300</td>
<td align="right">5,357,300</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">964,800</td>
<td align="right">641,200</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">6,563,800</td>
<td align="right">4,429,700</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">4,325,960</td>
<td align="right">3,030,320</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">4,325,960</td>
<td align="right">3,030,320</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,325,960</td>
<td align="right">3,030,320</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">81,754,900</td>
<td align="right">57,682,500</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">9,295,160</td>
<td align="right">6,745,980</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,689,500</td>
<td align="right">2,686,520</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">12,303,000</td>
<td align="right">9,375,300</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,459,620</td>
<td align="right">2,686,520</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">16,894,980</td>
<td align="right">13,129,620</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">3,502,820</td>
<td align="right">2,729,720</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">4,997,640</td>
<td align="right">3,994,580</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">4,997,640</td>
<td align="right">3,994,580</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,386,760</td>
<td align="right">1,935,320</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,386,760</td>
<td align="right">1,935,320</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">20,812,400</td>
<td align="right">16,889,120</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">36,352,020</td>
<td align="right">29,600,780</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">8,518,420</td>
<td align="right">7,075,640</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">6,305,020</td>
<td align="right">5,245,040</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">25,756,720</td>
<td align="right">21,569,780</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">25,756,720</td>
<td align="right">21,569,780</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,538,020</td>
<td align="right">1,308,060</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">2,284,980</td>
<td align="right">1,957,380</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">2,284,980</td>
<td align="right">1,957,380</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,272,920</td>
<td align="right">1,949,320</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">12,275,060</td>
<td align="right">10,705,820</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">26,264,900</td>
<td align="right">23,249,540</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">26,264,900</td>
<td align="right">23,249,540</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">214,836,180</td>
<td align="right">190,944,180</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">64,467,400</td>
<td align="right">57,834,320</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">257,336,820</td>
<td align="right">230,909,660</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,243,740</td>
<td align="right">8,322,880</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">49,200,200</td>
<td align="right">44,382,740</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,238,560</td>
<td align="right">1,117,540</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,238,560</td>
<td align="right">1,117,540</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">41,904,720</td>
<td align="right">38,098,680</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">6,163,600</td>
<td align="right">5,683,580</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,326,140</td>
<td align="right">2,147,260</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">5,600,420</td>
<td align="right">5,176,620</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">141,933,780</td>
<td align="right">131,429,320</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">141,933,780</td>
<td align="right">131,429,320</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">88,318,700</td>
<td align="right">81,912,120</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">89,025,960</td>
<td align="right">82,621,200</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">47,352,140</td>
<td align="right">44,518,300</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">109,075,280</td>
<td align="right">102,568,760</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,170,760</td>
<td align="right">6,781,200</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">43,467,440</td>
<td align="right">41,429,500</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">44,721,240</td>
<td align="right">42,941,060</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">75,595,560</td>
<td align="right">72,995,140</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">30,501,560</td>
<td align="right">29,777,060</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">31,809,700</td>
<td align="right">31,085,120</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">40,266,480</td>
<td align="right">39,372,680</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">36,092,480</td>
<td align="right">35,367,520</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">36,586,260</td>
<td align="right">35,861,220</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">37,894,400</td>
<td align="right">37,169,280</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">37,894,400</td>
<td align="right">37,169,280</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">39,190,520</td>
<td align="right">38,465,400</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">39,190,520</td>
<td align="right">38,465,400</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">39,190,520</td>
<td align="right">38,465,400</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">25,646,100</td>
<td align="right">25,401,540</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,887,500</td>
<td align="right">1,887,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,969,640</td>
<td align="right">8,968,760</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">13,252,420</td>
<td align="right">13,251,160</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">1,801,920</td>
<td align="right">1,801,760</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,801,920</td>
<td align="right">1,801,760</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">1,801,920</td>
<td align="right">1,801,760</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">4,282,780</td>
<td align="right">4,282,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,579,440</td>
<td align="right">3,579,160</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,308,140</td>
<td align="right">1,308,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,308,140</td>
<td align="right">1,308,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">4,887,540</td>
<td align="right">4,887,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,621,720</td>
<td align="right">2,621,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,621,720</td>
<td align="right">2,621,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">178,760</td>
<td align="right"></td>
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
Stats gathered on: 2025-02-06
