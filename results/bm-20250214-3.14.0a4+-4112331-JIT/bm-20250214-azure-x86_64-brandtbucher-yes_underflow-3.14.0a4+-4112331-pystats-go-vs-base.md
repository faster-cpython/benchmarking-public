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
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">796,020</td>
<td align="right">60</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">28,687,980</td>
<td align="right">124,700</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">34,928,800</td>
<td align="right">287,240</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">8,308,820</td>
<td align="right">122,180</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">7,740,520</td>
<td align="right">131,560</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">19,736,860</td>
<td align="right">377,120</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">15,065,940</td>
<td align="right">458,680</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,050,040</td>
<td align="right">67,900</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">42,263,380</td>
<td align="right">1,815,040</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,975,260</td>
<td align="right">87,720</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,008,660</td>
<td align="right">50,940</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">49,487,580</td>
<td align="right">2,659,020</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">55,358,040</td>
<td align="right">3,027,720</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">56,339,400</td>
<td align="right">3,745,740</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">17,767,580</td>
<td align="right">1,336,560</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">35,308,220</td>
<td align="right">3,691,920</td>
<td align="right">-89.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">31,534,660</td>
<td align="right">3,314,600</td>
<td align="right">-89.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">189,780,820</td>
<td align="right">21,801,820</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">111,055,680</td>
<td align="right">12,839,180</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">30,517,080</td>
<td align="right">4,225,200</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">16,887,940</td>
<td align="right">2,373,020</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">4,426,440</td>
<td align="right">636,600</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">8,497,080</td>
<td align="right">1,257,520</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">13,526,300</td>
<td align="right">2,091,580</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">22,576,100</td>
<td align="right">3,560,260</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">566,940</td>
<td align="right">1,042,400</td>
<td align="right">83.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">4,529,480</td>
<td align="right">739,560</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">920,100</td>
<td align="right">155,520</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">959,100</td>
<td align="right">194,520</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,572,100</td>
<td align="right">757,660</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,296,120</td>
<td align="right">332,580</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">23,909,920</td>
<td align="right">6,630,240</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">13,737,740</td>
<td align="right">4,099,600</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">15,999,120</td>
<td align="right">4,806,320</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,887,620</td>
<td align="right">610,360</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">22,045,160</td>
<td align="right">7,482,500</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,982,940</td>
<td align="right">705,700</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">9,438,700</td>
<td align="right">3,519,020</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,265,880</td>
<td align="right">1,218,180</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">14,359,940</td>
<td align="right">5,913,860</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,858,800</td>
<td align="right">774,660</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">105,420</td>
<td align="right">123,720</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">340</td>
<td align="right">320</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">12,040</td>
<td align="right">12,100</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">41,440</td>
<td align="right">41,500</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">90,880</td>
<td align="right">90,940</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">70,980</td>
<td align="right">71,020</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">90,300</td>
<td align="right">90,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">57,680</td>
<td align="right">57,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">285,720</td>
<td align="right">285,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">94,600</td>
<td align="right">94,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">742,560</td>
<td align="right">742,540</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,568,160</td>
<td align="right">2,568,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">1,887,540</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">162,420</td>
<td align="right">162,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">126,920</td>
<td align="right">126,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">84,840</td>
<td align="right">84,840</td>
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
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">24,060</td>
<td align="right">24,060</td>
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
<td align="left">CONTAINS_OP_SET</td>
<td align="right">40</td>
<td align="right">40</td>
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
<td align="right">40</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">40</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,301,520</td>
<td align="right">17.7%</td>
<td align="right">116,880</td>
<td align="right">0.3%</td>
<td align="right">-98.6%</td>
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
<td align="right">38,584,560</td>
<td align="right">99.4%</td>
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
<td align="right">95,780</td>
<td align="right">0.2%</td>
<td align="right">95,780</td>
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
<td align="left">Failure</td>
<td align="right">7,300</td>
<td align="right">80.0%</td>
<td align="right">5,300</td>
<td align="right">74.4%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,820</td>
<td align="right">20.0%</td>
<td align="right">1,820</td>
<td align="right">25.6%</td>
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
<td align="left">add different types</td>
<td align="right">5,220</td>
<td align="right">71.5%</td>
<td align="right">5,220</td>
<td align="right">98.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">2,000</td>
<td align="right">27.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,440</td>
<td align="right">0.0%</td>
<td align="right">6,420</td>
<td align="right">0.0%</td>
<td align="right">-74.8%</td>
</tr>
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
<td align="right">122,480</td>
<td align="right">0.2%</td>
<td align="right">17.9%</td>
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
<td align="right">79,657,500</td>
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
<td align="right">520</td>
<td align="right">26.3%</td>
<td align="right">160</td>
<td align="right">11.6%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,460</td>
<td align="right">73.7%</td>
<td align="right">1,220</td>
<td align="right">88.4%</td>
<td align="right">-16.4%</td>
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
<td align="right">28.8%</td>
<td align="right">180</td>
<td align="right">14.8%</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">960</td>
<td align="right">65.8%</td>
<td align="right">960</td>
<td align="right">78.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">40</td>
<td align="right">2.7%</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">40</td>
<td align="right">2.7%</td>
<td align="right">40</td>
<td align="right">3.3%</td>
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
<td align="right">873,000</td>
<td align="right">100.0%</td>
<td align="right">-81.3%</td>
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
<td align="right">50,880,520</td>
<td align="right">100.0%</td>
<td align="right">-2.4%</td>
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
<td align="right">224,180</td>
<td align="right">0.6%</td>
<td align="right">-84.0%</td>
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
<td align="right">38,463,540</td>
<td align="right">99.4%</td>
<td align="right">-13.1%</td>
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
<td align="right">4,260</td>
<td align="right">99.5%</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.5%</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,459,020</td>
<td align="right">0.9%</td>
<td align="right">290,680</td>
<td align="right">0.3%</td>
<td align="right">-96.6%</td>
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
<td align="right">58,446,460</td>
<td align="right">51.2%</td>
<td align="right">-89.4%</td>
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
<td align="right">55,077,840</td>
<td align="right">48.2%</td>
<td align="right">-85.2%</td>
</tr>
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
<td align="right">371,360</td>
<td align="right">0.3%</td>
<td align="right">-76.3%</td>
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
<td align="right">116,880</td>
<td align="right">41.4%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,920</td>
<td align="right">1.2%</td>
<td align="right">122,480</td>
<td align="right">43.4%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">41,220</td>
<td align="right">0.5%</td>
<td align="right">41,220</td>
<td align="right">14.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,300</td>
<td align="right">0.0%</td>
<td align="right">1,300</td>
<td align="right">0.5%</td>
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
<td align="left">TO_BOOL_BOOL</td>
<td align="right">636,000</td>
<td align="right">40.5%</td>
<td align="right">46,640</td>
<td align="right">12.5%</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">636,000</td>
<td align="right">40.5%</td>
<td align="right">46,640</td>
<td align="right">12.5%</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">500</td>
<td align="right">0.0%</td>
<td align="right">820</td>
<td align="right">0.2%</td>
<td align="right">64.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">95,780</td>
<td align="right">6.1%</td>
<td align="right">95,780</td>
<td align="right">25.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">66,140</td>
<td align="right">4.2%</td>
<td align="right">66,140</td>
<td align="right">17.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">64,760</td>
<td align="right">4.1%</td>
<td align="right">64,760</td>
<td align="right">17.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">43,040</td>
<td align="right">2.7%</td>
<td align="right">43,040</td>
<td align="right">11.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">19,080</td>
<td align="right">1.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,360</td>
<td align="right">0.4%</td>
<td align="right">6,360</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,060</td>
<td align="right">0.1%</td>
<td align="right">1,060</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">820</td>
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
<td align="left">Mortal decrefs</td>
<td align="right">337,865,012</td>
<td align="right">26.2%</td>
<td align="right">661,256,483</td>
<td align="right">49.2%</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">175,668,411</td>
<td align="right">14.9%</td>
<td align="right">328,126,563</td>
<td align="right">26.4%</td>
<td align="right">86.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">177,851,480</td>
<td align="right">15.1%</td>
<td align="right">25,394,280</td>
<td align="right">2.0%</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">344,985,900</td>
<td align="right">29.3%</td>
<td align="right">62,578,000</td>
<td align="right">5.0%</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">180,507,430</td>
<td align="right">14.0%</td>
<td align="right">328,045,923</td>
<td align="right">24.4%</td>
<td align="right">81.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">477,707,291</td>
<td align="right">40.6%</td>
<td align="right">824,924,223</td>
<td align="right">66.5%</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">253,025,200</td>
<td align="right">19.6%</td>
<td align="right">96,542,140</td>
<td align="right">7.2%</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">517,012,060</td>
<td align="right">40.1%</td>
<td align="right">258,430,200</td>
<td align="right">19.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">28</td>
<td align="right"></td>
<td align="right">40</td>
<td align="right"></td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">30</td>
<td align="right"></td>
<td align="right">42</td>
<td align="right"></td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">48,600</td>
<td align="right">0.1%</td>
<td align="right">49,000</td>
<td align="right">0.2%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">42,570</td>
<td align="right"></td>
<td align="right">42,558</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">9,571,420</td>
<td align="right">29.5%</td>
<td align="right">9,572,060</td>
<td align="right">29.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">22,852,300</td>
<td align="right"></td>
<td align="right">22,853,080</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">22,853,720</td>
<td align="right">70.5%</td>
<td align="right">22,854,500</td>
<td align="right">70.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">9,510,820</td>
<td align="right">29.3%</td>
<td align="right">9,511,060</td>
<td align="right">29.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">12,000</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">9,525,400</td>
<td align="right"></td>
<td align="right">9,525,400</td>
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
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">299</td>
<td align="right"></td>
<td align="right">299</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
<td align="right">0.0%</td>
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
<td align="right">20</td>
<td align="right">22,100</td>
<td align="right">2,562,520</td>
<td align="right">20</td>
<td align="right">22,100</td>
<td align="right">2,559,720</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">580</td>
<td align="right">11.2%</td>
<td align="right">1,220</td>
<td align="right">83.6%</td>
<td align="right">110.3%</td>
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
<td align="right">161,126,500</td>
<td align="right"></td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">4,600</td>
<td align="right">88.8%</td>
<td align="right">240</td>
<td align="right">16.4%</td>
<td align="right">-94.8%</td>
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
<td align="right">380</td>
<td align="right">26.0%</td>
<td align="right">-92.0%</td>
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
<td align="right">4,305,167,760</td>
<td align="right">2,671.9%</td>
<td align="right">83.9%</td>
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
<td align="right">1,460</td>
<td align="right"></td>
<td align="right">-71.8%</td>
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
<td align="right">580</td>
<td align="right"></td>
<td align="right">1,220</td>
<td align="right"></td>
<td align="right">110.3%</td>
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
<td align="right">1,220</td>
<td align="right">100.0%</td>
<td align="right">110.3%</td>
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
<td align="right">200</td>
<td align="right">34.5%</td>
<td align="right">280</td>
<td align="right">23.0%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">120</td>
<td align="right">20.7%</td>
<td align="right">300</td>
<td align="right">24.6%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">120</td>
<td align="right">20.7%</td>
<td align="right">300</td>
<td align="right">24.6%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">140</td>
<td align="right">24.1%</td>
<td align="right">300</td>
<td align="right">24.6%</td>
<td align="right">114.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">40</td>
<td align="right">3.3%</td>
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
<td align="right">80</td>
<td align="right">13.8%</td>
<td align="right">180</td>
<td align="right">14.8%</td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">140</td>
<td align="right">24.1%</td>
<td align="right">280</td>
<td align="right">23.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">100</td>
<td align="right">17.2%</td>
<td align="right">140</td>
<td align="right">11.5%</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">180</td>
<td align="right">31.0%</td>
<td align="right">380</td>
<td align="right">31.1%</td>
<td align="right">111.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">80</td>
<td align="right">13.8%</td>
<td align="right">240</td>
<td align="right">19.7%</td>
<td align="right">200.0%</td>
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
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">178,760</td>
<td align="right">10,742,300</td>
<td align="right">5,909.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,386,760</td>
<td align="right">37,028,320</td>
<td align="right">1,451.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">4,325,960</td>
<td align="right">44,774,300</td>
<td align="right">935.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">4,325,960</td>
<td align="right">44,774,300</td>
<td align="right">935.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,325,960</td>
<td align="right">44,774,300</td>
<td align="right">935.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,386,760</td>
<td align="right">21,746,500</td>
<td align="right">811.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">638,220</td>
<td align="right">4,185,320</td>
<td align="right">555.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">689,340</td>
<td align="right">4,236,440</td>
<td align="right">514.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,610,480</td>
<td align="right">9,795,120</td>
<td align="right">508.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">4,887,540</td>
<td align="right">28,219,900</td>
<td align="right">477.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">12,275,060</td>
<td align="right">65,799,580</td>
<td align="right">436.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">5,600,420</td>
<td align="right">28,720,740</td>
<td align="right">412.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,949,000</td>
<td align="right">14,283,460</td>
<td align="right">384.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">970,260</td>
<td align="right">4,585,740</td>
<td align="right">372.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,962,220</td>
<td align="right">8,722,540</td>
<td align="right">344.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">13,252,420</td>
<td align="right">56,899,220</td>
<td align="right">329.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">6,305,020</td>
<td align="right">22,033,400</td>
<td align="right">249.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">8,518,420</td>
<td align="right">27,534,280</td>
<td align="right">223.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">970,260</td>
<td align="right">2,904,180</td>
<td align="right">199.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,969,640</td>
<td align="right">26,530,140</td>
<td align="right">195.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">36,586,260</td>
<td align="right">101,417,520</td>
<td align="right">177.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">3,502,820</td>
<td align="right">9,346,920</td>
<td align="right">166.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,238,560</td>
<td align="right">3,286,260</td>
<td align="right">165.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,326,140</td>
<td align="right">6,115,980</td>
<td align="right">162.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">7,170,760</td>
<td align="right">18,605,480</td>
<td align="right">159.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,243,740</td>
<td align="right">23,758,660</td>
<td align="right">157.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">41,904,720</td>
<td align="right">93,205,100</td>
<td align="right">122.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">257,336,820</td>
<td align="right">518,898,240</td>
<td align="right">101.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">964,800</td>
<td align="right">1,922,520</td>
<td align="right">99.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">81,754,900</td>
<td align="right">161,126,500</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">837,900</td>
<td align="right">1,634,060</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">214,836,180</td>
<td align="right">409,991,880</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">88,318,700</td>
<td align="right">167,690,280</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,538,020</td>
<td align="right">2,815,280</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">8,119,300</td>
<td align="right">14,038,980</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">141,933,780</td>
<td align="right">240,150,280</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">141,933,780</td>
<td align="right">240,150,280</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">89,025,960</td>
<td align="right">149,655,660</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">26,264,900</td>
<td align="right">43,544,580</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">26,264,900</td>
<td align="right">43,544,580</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">109,075,280</td>
<td align="right">175,532,920</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">47,352,140</td>
<td align="right">75,572,200</td>
<td align="right">59.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">16,894,980</td>
<td align="right">26,894,080</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">75,595,560</td>
<td align="right">119,355,900</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">64,467,400</td>
<td align="right">100,522,260</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">49,200,200</td>
<td align="right">74,826,900</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">4,282,780</td>
<td align="right">6,264,920</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">460</td>
<td align="right">660</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">1,801,920</td>
<td align="right">2,566,500</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,801,920</td>
<td align="right">2,566,500</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">1,801,920</td>
<td align="right">2,566,500</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">44,721,240</td>
<td align="right">62,855,720</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,689,500</td>
<td align="right">4,966,720</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">45,168,180</td>
<td align="right">59,708,320</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">30,501,560</td>
<td align="right">40,255,780</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">12,303,000</td>
<td align="right">16,092,800</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">37,894,400</td>
<td align="right">49,087,200</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">37,894,400</td>
<td align="right">49,087,200</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">36,092,480</td>
<td align="right">46,520,700</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">39,190,520</td>
<td align="right">50,383,320</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">39,190,520</td>
<td align="right">50,383,320</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">39,190,520</td>
<td align="right">50,383,320</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">40,266,480</td>
<td align="right">51,212,960</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">31,809,700</td>
<td align="right">40,255,780</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">4,997,640</td>
<td align="right">6,274,880</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">4,997,640</td>
<td align="right">6,274,880</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">5,026,100</td>
<td align="right">6,290,480</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">43,467,440</td>
<td align="right">53,202,500</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">20,812,400</td>
<td align="right">24,602,300</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">25,756,720</td>
<td align="right">29,546,640</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">25,756,720</td>
<td align="right">29,546,640</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">9,295,160</td>
<td align="right">10,572,340</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">25,646,100</td>
<td align="right">27,538,820</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">36,352,020</td>
<td align="right">37,315,580</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">837,900</td>
<td align="right">837,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">837,900</td>
<td align="right">837,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">837,900</td>
<td align="right">837,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">837,900</td>
<td align="right">837,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">837,900</td>
<td align="right">837,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">665,640</td>
<td align="right">665,620</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,238,560</td>
<td align="right">1,238,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">4,297,520</td>
<td align="right">4,297,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">4,297,520</td>
<td align="right">4,297,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">4,297,520</td>
<td align="right">4,297,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">4,297,520</td>
<td align="right">4,297,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,621,720</td>
<td align="right">2,621,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,621,720</td>
<td align="right">2,621,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">6,163,600</td>
<td align="right">6,163,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,459,620</td>
<td align="right">3,459,600</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,579,440</td>
<td align="right">3,579,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">6,563,800</td>
<td align="right">6,563,780</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">2,284,980</td>
<td align="right">2,284,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">2,284,980</td>
<td align="right">2,284,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,272,920</td>
<td align="right">2,272,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,887,500</td>
<td align="right">1,887,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,308,140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,308,140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">754,700</td>
<td align="right">754,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">52,330,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right"></td>
<td align="right">14,607,260</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">7,239,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">6,973,540</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right"></td>
<td align="right">6,553,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right"></td>
<td align="right">3,378,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right"></td>
<td align="right">3,378,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">1,887,540</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right"></td>
<td align="right">1,084,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right">963,540</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right"></td>
<td align="right">777,060</td>
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
<td align="right"></td>
<td align="right">240</td>
<td align="right"></td>
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
Stats gathered on: 2025-05-05
