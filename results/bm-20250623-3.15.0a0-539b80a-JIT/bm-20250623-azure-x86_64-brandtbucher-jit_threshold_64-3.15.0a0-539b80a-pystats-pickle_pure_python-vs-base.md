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
<td align="left">COMPARE_OP</td>
<td align="right">299,160</td>
<td align="right">1,028,960</td>
<td align="right">243.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">192,000</td>
<td align="right">556,800</td>
<td align="right">190.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">249,600</td>
<td align="right">614,400</td>
<td align="right">146.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">194,640</td>
<td align="right">1,340</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">76,800</td>
<td align="right">19,220</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">38,400</td>
<td align="right">19,200</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">402,100</td>
<td align="right">230,580</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">309,460</td>
<td align="right">193,080</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,537,140</td>
<td align="right">1,901,940</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,766,080</td>
<td align="right">3,189,780</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,649,660</td>
<td align="right">2,956,880</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">192,080</td>
<td align="right">172,860</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">192,080</td>
<td align="right">172,860</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">33,600,780</td>
<td align="right">35,726,760</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,529,880</td>
<td align="right">6,893,020</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">7,142,420</td>
<td align="right">7,484,560</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">25,307,100</td>
<td align="right">26,265,920</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">80,640</td>
<td align="right">78,060</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,932,900</td>
<td align="right">19,500,800</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">8,334,040</td>
<td align="right">8,582,480</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">8,391,580</td>
<td align="right">8,638,280</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">42,606,140</td>
<td align="right">43,851,160</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">33,313,640</td>
<td align="right">34,253,240</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,222,560</td>
<td align="right">6,064,300</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">14,456,900</td>
<td align="right">14,800,760</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">11,310,880</td>
<td align="right">11,540,300</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">11,425,200</td>
<td align="right">11,654,420</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,020</td>
<td align="right">1,000</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">96,000</td>
<td align="right">94,280</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">63,036,280</td>
<td align="right">63,814,200</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">7,142,660</td>
<td align="right">7,062,420</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">192,300</td>
<td align="right">190,580</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">166,873,520</td>
<td align="right">168,139,320</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">2,764,820</td>
<td align="right">2,745,600</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,033,680</td>
<td align="right">3,012,740</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,803,280</td>
<td align="right">2,784,060</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">5,664,040</td>
<td align="right">5,625,600</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,841,620</td>
<td align="right">2,822,400</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">5,702,500</td>
<td align="right">5,664,060</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">8,640,060</td>
<td align="right">8,582,400</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">29,553,620</td>
<td align="right">29,358,060</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">5,894,440</td>
<td align="right">5,856,000</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">29,416,060</td>
<td align="right">29,601,680</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,129,680</td>
<td align="right">3,110,460</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">8,121,760</td>
<td align="right">8,083,320</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">365,100</td>
<td align="right">363,380</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">10,329,700</td>
<td align="right">10,289,540</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">28,723,360</td>
<td align="right">28,625,540</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,142,480</td>
<td align="right">7,121,540</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">13,862,560</td>
<td align="right">13,822,400</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">58,800</td>
<td align="right">58,680</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">10,694,420</td>
<td align="right">10,675,200</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,818,500</td>
<td align="right">13,797,560</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">11,520,060</td>
<td align="right">11,518,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">6,451,200</td>
<td align="right">6,451,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,646,400</td>
<td align="right">4,646,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">3,840,000</td>
<td align="right">3,840,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,801,780</td>
<td align="right">3,801,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">3,782,400</td>
<td align="right">3,782,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,782,400</td>
<td align="right">3,782,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,342,400</td>
<td align="right">2,342,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,305,660</td>
<td align="right">1,305,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">1,228,800</td>
<td align="right">1,228,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">864,000</td>
<td align="right">864,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">403,960</td>
<td align="right">403,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">327,420</td>
<td align="right">327,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">153,660</td>
<td align="right">153,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">115,260</td>
<td align="right">115,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">115,200</td>
<td align="right">115,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">76,800</td>
<td align="right">76,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">76,800</td>
<td align="right">76,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">57,600</td>
<td align="right">57,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">57,600</td>
<td align="right">57,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">57,600</td>
<td align="right">57,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">38,540</td>
<td align="right">38,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">38,400</td>
<td align="right">38,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">38,400</td>
<td align="right">38,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">19,320</td>
<td align="right">19,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">19,260</td>
<td align="right">19,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">19,240</td>
<td align="right">19,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">19,200</td>
<td align="right">19,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
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
<td align="right">6,528,000</td>
<td align="right">81.5%</td>
<td align="right">6,891,080</td>
<td align="right">82.3%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,478,520</td>
<td align="right">18.5%</td>
<td align="right">1,478,520</td>
<td align="right">17.7%</td>
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
<td align="right">1,840</td>
<td align="right">97.9%</td>
<td align="right">1,900</td>
<td align="right">97.9%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">40</td>
<td align="right">2.1%</td>
<td align="right">40</td>
<td align="right">2.1%</td>
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
<td align="left">add other</td>
<td align="right">1,800</td>
<td align="right">97.8%</td>
<td align="right">1,860</td>
<td align="right">97.9%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">40</td>
<td align="right">2.2%</td>
<td align="right">40</td>
<td align="right">2.1%</td>
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
<td align="right">698,880</td>
<td align="right">0.7%</td>
<td align="right">698,880</td>
<td align="right">0.7%</td>
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
<td align="right">105,669,540</td>
<td align="right">99.3%</td>
<td align="right">105,669,540</td>
<td align="right">99.3%</td>
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
<td align="right">712,320</td>
<td align="right">0.7%</td>
<td align="right">712,320</td>
<td align="right">0.7%</td>
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
<td align="right">13,700</td>
<td align="right">100.0%</td>
<td align="right">13,700</td>
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
<td align="right">291,840</td>
<td align="right">1.4%</td>
<td align="right">1,021,440</td>
<td align="right">4.6%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">20,859,360</td>
<td align="right">97.8%</td>
<td align="right">20,859,360</td>
<td align="right">94.6%</td>
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
<td align="right">163,920</td>
<td align="right">0.8%</td>
<td align="right">163,920</td>
<td align="right">0.7%</td>
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
<td align="right">7,320</td>
<td align="right">70.1%</td>
<td align="right">7,520</td>
<td align="right">70.7%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,120</td>
<td align="right">29.9%</td>
<td align="right">3,120</td>
<td align="right">29.3%</td>
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
<td align="right">7,320</td>
<td align="right">100.0%</td>
<td align="right">7,520</td>
<td align="right">100.0%</td>
<td align="right">2.7%</td>
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
<td align="right">19,200</td>
<td align="right">0.5%</td>
<td align="right">19,200</td>
<td align="right">0.5%</td>
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
<td align="right">3,840,000</td>
<td align="right">99.5%</td>
<td align="right">3,840,000</td>
<td align="right">99.5%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">401,980</td>
<td align="right">77.0%</td>
<td align="right">230,460</td>
<td align="right">70.1%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">120,060</td>
<td align="right">23.0%</td>
<td align="right">98,260</td>
<td align="right">29.9%</td>
<td align="right">-18.2%</td>
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
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">120</td>
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
<td align="left">enumerate</td>
<td align="right">40</td>
<td align="right">33.3%</td>
<td align="right">60</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">80</td>
<td align="right">66.7%</td>
<td align="right">60</td>
<td align="right">50.0%</td>
<td align="right">-25.0%</td>
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
<td align="left">self</td>
<td align="right">134,400</td>
<td align="right">134,400 / 0 !!</td>
<td align="right">134,400</td>
<td align="right">134,400 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">96,000</td>
<td align="right">96,000 / 0 !!</td>
<td align="right">96,000</td>
<td align="right">96,000 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">77,760</td>
<td align="right">77,760 / 0 !!</td>
<td align="right">77,760</td>
<td align="right">77,760 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">19,200</td>
<td align="right">19,200 / 0 !!</td>
<td align="right">19,200</td>
<td align="right">19,200 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">60 / 0 !!</td>
<td align="right">60</td>
<td align="right">60 / 0 !!</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">126,280,480</td>
<td align="right">99.7%</td>
<td align="right">126,410,160</td>
<td align="right">99.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">403,320</td>
<td align="right">0.3%</td>
<td align="right">403,320</td>
<td align="right">0.3%</td>
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
<td align="right">38.7%</td>
<td align="right">240</td>
<td align="right">38.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">380</td>
<td align="right">61.3%</td>
<td align="right">380</td>
<td align="right">61.3%</td>
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
<td align="right">360</td>
<td align="right">94.7%</td>
<td align="right">360</td>
<td align="right">94.7%</td>
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
<td align="right">47,656,260</td>
<td align="right">100.0%</td>
<td align="right">48,126,340</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
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
<td align="right">180</td>
<td align="right">100.0%</td>
<td align="right">180</td>
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
<td align="right">864,000</td>
<td align="right">100.0%</td>
<td align="right">864,000</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">3,782,400</td>
<td align="right">100.0%</td>
<td align="right">3,782,400</td>
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
<td align="right">110,080</td>
<td align="right">0.5%</td>
<td align="right">114,480</td>
<td align="right">0.5%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">21,661,340</td>
<td align="right">99.3%</td>
<td align="right">21,659,100</td>
<td align="right">99.3%</td>
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
<td align="right">38,460</td>
<td align="right">0.2%</td>
<td align="right">38,460</td>
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
<td align="right">2,100</td>
<td align="right">97.2%</td>
<td align="right">2,180</td>
<td align="right">97.3%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60</td>
<td align="right">2.8%</td>
<td align="right">60</td>
<td align="right">2.7%</td>
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
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">20</td>
<td align="right">33.3%</td>
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
<td align="right">3,168,060</td>
<td align="right">100.0%</td>
<td align="right">3,168,060</td>
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
<td align="right">8,020,760</td>
<td align="right">1.1%</td>
<td align="right">8,942,180</td>
<td align="right">1.2%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">398,367,040</td>
<td align="right">56.0%</td>
<td align="right">406,019,940</td>
<td align="right">56.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">304,482,480</td>
<td align="right">42.8%</td>
<td align="right">306,939,880</td>
<td align="right">42.5%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">986,320</td>
<td align="right">0.1%</td>
<td align="right">990,740</td>
<td align="right">0.1%</td>
<td align="right">0.4%</td>
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
<td align="right">291,840</td>
<td align="right">3.5%</td>
<td align="right">1,021,440</td>
<td align="right">11.0%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">401,980</td>
<td align="right">4.8%</td>
<td align="right">230,460</td>
<td align="right">2.5%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,528,000</td>
<td align="right">77.9%</td>
<td align="right">6,891,080</td>
<td align="right">74.1%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">698,880</td>
<td align="right">8.3%</td>
<td align="right">698,880</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">403,320</td>
<td align="right">4.8%</td>
<td align="right">403,320</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">38,460</td>
<td align="right">0.5%</td>
<td align="right">38,460</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">19,200</td>
<td align="right">0.2%</td>
<td align="right">19,200</td>
<td align="right">0.2%</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">54,960</td>
<td align="right">5.6%</td>
<td align="right">57,240</td>
<td align="right">5.8%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">55,120</td>
<td align="right">5.6%</td>
<td align="right">57,240</td>
<td align="right">5.8%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">712,320</td>
<td align="right">72.2%</td>
<td align="right">712,320</td>
<td align="right">71.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">163,920</td>
<td align="right">16.6%</td>
<td align="right">163,920</td>
<td align="right">16.5%</td>
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
<td align="left">EXIT_INIT_CHECK</td>
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
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
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
<td align="right">76,860</td>
<td align="right">0.2%</td>
<td align="right">76,860</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">41,472,360</td>
<td align="right">99.8%</td>
<td align="right">41,472,360</td>
<td align="right">99.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">76,860</td>
<td align="right">0.2%</td>
<td align="right">76,860</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">76,860</td>
<td align="right">0.2%</td>
<td align="right">76,860</td>
<td align="right">0.2%</td>
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
<td align="right">76,860</td>
<td align="right">0.2%</td>
<td align="right">76,860</td>
<td align="right">0.2%</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">41,606,820</td>
<td align="right">100.1%</td>
<td align="right">41,606,820</td>
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
<td align="left">Interpreter immortal decrefs</td>
<td align="right">510,240</td>
<td align="right">0.1%</td>
<td align="right">1,239,840</td>
<td align="right">0.3%</td>
<td align="right">143.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,929</td>
<td align="right"></td>
<td align="right">3,258</td>
<td align="right"></td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">21,185</td>
<td align="right"></td>
<td align="right">24,654</td>
<td align="right"></td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">19,279</td>
<td align="right"></td>
<td align="right">21,496</td>
<td align="right"></td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">35,314,625</td>
<td align="right">9.0%</td>
<td align="right">34,590,617</td>
<td align="right">8.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">107,037,291</td>
<td align="right">27.2%</td>
<td align="right">105,236,791</td>
<td align="right">26.7%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">129,190,780</td>
<td align="right">34.7%</td>
<td align="right">127,094,577</td>
<td align="right">34.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">187,945,580</td>
<td align="right">50.5%</td>
<td align="right">190,471,300</td>
<td align="right">51.1%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">250,189,060</td>
<td align="right">63.7%</td>
<td align="right">252,419,800</td>
<td align="right">64.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">228,471</td>
<td align="right"></td>
<td align="right">227,142</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">5,031,261</td>
<td align="right"></td>
<td align="right">5,029,224</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">115,220</td>
<td align="right">0.3%</td>
<td align="right">115,200</td>
<td align="right">0.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">54,783,536</td>
<td align="right">14.7%</td>
<td align="right">54,788,611</td>
<td align="right">14.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">288,040</td>
<td align="right">0.7%</td>
<td align="right">288,060</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">28,223,839</td>
<td align="right"></td>
<td align="right">28,223,324</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,211,960</td>
<td align="right">30.2%</td>
<td align="right">12,211,960</td>
<td align="right">30.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,269,480</td>
<td align="right"></td>
<td align="right">12,269,480</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">28,281,940</td>
<td align="right">69.8%</td>
<td align="right">28,281,940</td>
<td align="right">69.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">27,878,680</td>
<td align="right">68.8%</td>
<td align="right">27,878,680</td>
<td align="right">68.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">115,200</td>
<td align="right"></td>
<td align="right">115,200</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">480,060</td>
<td align="right">0.1%</td>
<td align="right">480,060</td>
<td align="right">0.1%</td>
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
<td align="right">0</td>
<td align="right">4,960</td>
<td align="right">480</td>
<td align="right">220</td>
<td align="right">20</td>
<td align="right">0</td>
<td align="right">2,240</td>
<td align="right">420</td>
<td align="right">300</td>
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
<td align="right">20</td>
<td align="right">2.9%</td>
<td align="right">60</td>
<td align="right">5.9%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">680</td>
<td align="right"></td>
<td align="right">1,020</td>
<td align="right"></td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">620</td>
<td align="right">91.2%</td>
<td align="right">900</td>
<td align="right">88.2%</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">2,885,380</td>
<td align="right"></td>
<td align="right">3,515,860</td>
<td align="right"></td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">718,168,940</td>
<td align="right">24,889.9%</td>
<td align="right">697,748,700</td>
<td align="right">19,845.7%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">60</td>
<td align="right">8.8%</td>
<td align="right">60</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">5.9%</td>
<td align="right">60 / 0 !!</td>
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
<td align="right">60</td>
<td align="right"></td>
<td align="right">60</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">2,553,460</td>
<td align="right">94.5%</td>
<td align="right">4,147,100</td>
<td align="right">95.5%</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">2,703,360</td>
<td align="right"></td>
<td align="right">4,341,760</td>
<td align="right"></td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">52,800</td>
<td align="right">2.0%</td>
<td align="right">80,160</td>
<td align="right">1.8%</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">97,100</td>
<td align="right">3.6%</td>
<td align="right">114,500</td>
<td align="right">2.6%</td>
<td align="right">17.9%</td>
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
<td align="right">81,920</td>
<td align="right">1.9%</td>
<td align="right">81,920 / 0 !!</td>
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
<td align="left"><= 16,384</td>
<td align="left">20</td>
<td align="right">33.3%</td>
<td align="left"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="left"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">20</td>
<td align="right">33.3%</td>
<td align="left"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">20</td>
<td align="right">33.3%</td>
<td align="left">60</td>
<td align="right">100.0%</td>
<td align="right">200.0%</td>
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
<td align="left"><= 128</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">200.0%</td>
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
<td align="left"><= 64</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">50.0%</td>
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
<td align="left">_POP_ITER</td>
<td align="right">18,020</td>
<td align="right">134,400</td>
<td align="right">645.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">596,480</td>
<td align="right">768,000</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">2,885,380</td>
<td align="right">3,515,860</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,885,380</td>
<td align="right">3,515,840</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,611,620</td>
<td align="right">1,363,180</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,611,620</td>
<td align="right">1,364,920</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,611,620</td>
<td align="right">1,364,920</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,822,400</td>
<td align="right">2,459,320</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">9,904,800</td>
<td align="right">8,716,760</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">8,293,180</td>
<td align="right">7,353,580</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">3,340,780</td>
<td align="right">2,998,640</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">22,003,080</td>
<td align="right">19,936,480</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">3,250,180</td>
<td align="right">3,515,860</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">8,428,740</td>
<td align="right">7,756,800</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,460,080</td>
<td align="right">3,190,300</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">3,205,220</td>
<td align="right">2,958,520</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">6,527,980</td>
<td align="right">6,184,120</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">4,587,600</td>
<td align="right">4,358,380</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,587,600</td>
<td align="right">4,361,840</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">17,950,720</td>
<td align="right">17,070,500</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">2,994,000</td>
<td align="right">3,133,040</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,994,000</td>
<td align="right">3,131,320</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,747,180</td>
<td align="right">1,825,700</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">3,494,360</td>
<td align="right">3,649,680</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">12,651,540</td>
<td align="right">12,123,800</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">19,543,160</td>
<td align="right">18,765,240</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">19,543,160</td>
<td align="right">18,765,240</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">5,816,400</td>
<td align="right">5,590,640</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">108,011,580</td>
<td align="right">104,300,020</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">115,754,540</td>
<td align="right">111,963,900</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">9,868,760</td>
<td align="right">9,545,840</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">15,627,520</td>
<td align="right">15,120,720</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">23,919,540</td>
<td align="right">23,294,700</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">31,965,460</td>
<td align="right">31,287,080</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">2,265,560</td>
<td align="right">2,305,720</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,569,580</td>
<td align="right">4,648,100</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">19,987,200</td>
<td align="right">19,670,260</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">12,133,160</td>
<td align="right">11,947,560</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">13,361,960</td>
<td align="right">13,176,360</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">13,361,960</td>
<td align="right">13,176,360</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">13,361,960</td>
<td align="right">13,176,360</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">13,515,540</td>
<td align="right">13,345,700</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">3,494,360</td>
<td align="right">3,532,800</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">1,747,180</td>
<td align="right">1,766,400</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,747,180</td>
<td align="right">1,766,400</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">1,747,180</td>
<td align="right">1,766,400</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,747,180</td>
<td align="right">1,766,400</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,723,160</td>
<td align="right">4,761,600</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">4,723,160</td>
<td align="right">4,761,600</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">4,723,160</td>
<td align="right">4,761,600</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">4,723,160</td>
<td align="right">4,761,600</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,975,980</td>
<td align="right">2,996,920</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,951,960</td>
<td align="right">5,992,120</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">11,903,920</td>
<td align="right">11,982,520</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">11,903,920</td>
<td align="right">11,982,520</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,975,980</td>
<td align="right">2,995,200</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">2,975,980</td>
<td align="right">2,995,200</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,975,980</td>
<td align="right">2,995,200</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,975,980</td>
<td align="right">2,995,200</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,975,980</td>
<td align="right">2,995,200</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">2,975,980</td>
<td align="right">2,995,200</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,975,980</td>
<td align="right">2,995,200</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">7,180,760</td>
<td align="right">7,220,920</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">7,545,560</td>
<td align="right">7,585,720</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">8,409,560</td>
<td align="right">8,449,720</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,204,780</td>
<td align="right">4,224,000</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">4,204,780</td>
<td align="right">4,224,000</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">4,204,780</td>
<td align="right">4,224,000</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">4,204,780</td>
<td align="right">4,224,000</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">5,433,580</td>
<td align="right">5,454,520</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">2,534,400</td>
<td align="right">2,536,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">2,534,400</td>
<td align="right">2,536,980</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">2,457,600</td>
<td align="right">2,459,320</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">1,593,600</td>
<td align="right">1,593,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,228,800</td>
<td align="right">1,228,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,228,800</td>
<td align="right">1,228,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">729,600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">364,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">364,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">364,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">364,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right"></td>
<td align="right">57,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right"></td>
<td align="right">57,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right"></td>
<td align="right">19,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right"></td>
<td align="right">19,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">1,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">1,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">1,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">1,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right"></td>
<td align="right">20</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">20</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right"></td>
<td align="right">20</td>
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
<td align="right">60</td>
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
Stats gathered on: 2025-06-24
