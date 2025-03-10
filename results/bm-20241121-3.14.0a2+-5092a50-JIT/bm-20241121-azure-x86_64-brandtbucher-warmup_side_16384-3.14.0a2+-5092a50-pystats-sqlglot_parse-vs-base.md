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
<td align="left">BINARY_SLICE</td>
<td align="right">80</td>
<td align="right">1,688,280</td>
<td align="right">2,110,250.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">30,720</td>
<td align="right">2,154,160</td>
<td align="right">6,912.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">107,520</td>
<td align="right">930,140</td>
<td align="right">765.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">161,880</td>
<td align="right">991,640</td>
<td align="right">512.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">34,300</td>
<td align="right">143,440</td>
<td align="right">318.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">207,360</td>
<td align="right">727,560</td>
<td align="right">250.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,505,280</td>
<td align="right">2,888,540</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,136,640</td>
<td align="right">1,941,120</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">530,040</td>
<td align="right">892,980</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">30,720</td>
<td align="right">15,360</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,274,160</td>
<td align="right">9,359,280</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,918,460</td>
<td align="right">4,035,500</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,202,400</td>
<td align="right">2,993,760</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">7,350,540</td>
<td align="right">9,905,320</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,004,840</td>
<td align="right">3,809,340</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">261,300</td>
<td align="right">330,820</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,994,440</td>
<td align="right">3,774,820</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">17,390,220</td>
<td align="right">21,694,940</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,113,700</td>
<td align="right">3,872,060</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,113,700</td>
<td align="right">3,872,060</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,324,460</td>
<td align="right">7,816,820</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,078,880</td>
<td align="right">9,955,000</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">38,400</td>
<td align="right">46,040</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">16,230,380</td>
<td align="right">18,873,160</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">10,015,920</td>
<td align="right">11,498,700</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,980,380</td>
<td align="right">3,403,380</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,698,180</td>
<td align="right">12,194,580</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">61,480</td>
<td align="right">69,200</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">31,927,460</td>
<td align="right">35,822,100</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">66,516,540</td>
<td align="right">74,584,660</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">156,775,360</td>
<td align="right">174,334,360</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">10,024,900</td>
<td align="right">11,116,580</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,501,620</td>
<td align="right">4,953,780</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">23,948,960</td>
<td align="right">26,298,560</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">18,520,640</td>
<td align="right">19,790,940</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">8,947,180</td>
<td align="right">9,461,860</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">14,293,300</td>
<td align="right">15,064,840</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">43,772,120</td>
<td align="right">46,042,480</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,831,260</td>
<td align="right">5,076,060</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">43,433,560</td>
<td align="right">45,623,900</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">5,292,600</td>
<td align="right">5,544,540</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">28,495,240</td>
<td align="right">29,834,700</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,144,380</td>
<td align="right">1,198,140</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,036,980</td>
<td align="right">1,083,060</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,144,320</td>
<td align="right">1,190,400</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">606,700</td>
<td align="right">583,660</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,985,000</td>
<td align="right">13,307,700</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">19,766,180</td>
<td align="right">20,250,780</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,069,760</td>
<td align="right">2,115,840</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,496,060</td>
<td align="right">2,542,140</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">28,668,700</td>
<td align="right">29,163,700</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,190,620</td>
<td align="right">6,289,920</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,167,360</td>
<td align="right">1,182,720</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,319,360</td>
<td align="right">2,304,000</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,221,240</td>
<td align="right">1,228,920</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,234,800</td>
<td align="right">3,249,080</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,881,260</td>
<td align="right">2,873,580</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,570,200</td>
<td align="right">4,577,340</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">48,186,880</td>
<td align="right">48,253,840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">13,371,040</td>
<td align="right">13,371,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">8,340,480</td>
<td align="right">8,340,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,191,920</td>
<td align="right">5,191,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">5,145,600</td>
<td align="right">5,145,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">3,717,120</td>
<td align="right">3,717,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,701,880</td>
<td align="right">3,701,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,026,220</td>
<td align="right">3,026,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,597,560</td>
<td align="right">1,597,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,286,520</td>
<td align="right">1,286,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,251,840</td>
<td align="right">1,251,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,059,840</td>
<td align="right">1,059,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,008,220</td>
<td align="right">1,008,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">906,240</td>
<td align="right">906,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">875,520</td>
<td align="right">875,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">791,040</td>
<td align="right">791,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">760,440</td>
<td align="right">760,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">760,320</td>
<td align="right">760,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">721,920</td>
<td align="right">721,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">629,820</td>
<td align="right">629,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">483,840</td>
<td align="right">483,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">453,180</td>
<td align="right">453,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">130,620</td>
<td align="right">130,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">61,500</td>
<td align="right">61,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">53,760</td>
<td align="right">53,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">46,140</td>
<td align="right">46,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">46,080</td>
<td align="right">46,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">46,080</td>
<td align="right">46,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">38,400</td>
<td align="right">38,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">30,720</td>
<td align="right">30,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">23,040</td>
<td align="right">23,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">23,040</td>
<td align="right">23,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">23,040</td>
<td align="right">23,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">15,420</td>
<td align="right">15,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">15,420</td>
<td align="right">15,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">15,360</td>
<td align="right">15,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">13,000</td>
<td align="right">13,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">7,820</td>
<td align="right">7,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">7,740</td>
<td align="right">7,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">7,700</td>
<td align="right">7,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">7,680</td>
<td align="right">7,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">7,680</td>
<td align="right">7,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">7,680</td>
<td align="right">7,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">7,680</td>
<td align="right">7,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">220</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
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
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,883,780</td>
<td align="right">100.0%</td>
<td align="right">38,883,780</td>
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
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">1,688,280</td>
<td align="right">100.0%</td>
<td align="right">2,110,250.0%</td>
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
<td align="right">7,680</td>
<td align="right">0.0%</td>
<td align="right">7,680</td>
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
<td align="right">25,904,700</td>
<td align="right">99.9%</td>
<td align="right">25,904,700</td>
<td align="right">99.9%</td>
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
<td align="right">23,480</td>
<td align="right">0.1%</td>
<td align="right">23,480</td>
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
<td align="right">460</td>
<td align="right">100.0%</td>
<td align="right">460</td>
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
<td align="right">65,840,800</td>
<td align="right">97.8%</td>
<td align="right">65,840,800</td>
<td align="right">97.8%</td>
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
<td align="right">1,453,280</td>
<td align="right">2.2%</td>
<td align="right">1,453,280</td>
<td align="right">2.2%</td>
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
<td align="right">27,620</td>
<td align="right">100.0%</td>
<td align="right">27,620</td>
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
<td align="right">10,022,400</td>
<td align="right">26.4%</td>
<td align="right">11,113,820</td>
<td align="right">28.5%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">27,893,760</td>
<td align="right">73.6%</td>
<td align="right">27,893,760</td>
<td align="right">71.5%</td>
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
<td align="right">2,500</td>
<td align="right">100.0%</td>
<td align="right">2,760</td>
<td align="right">100.0%</td>
<td align="right">10.4%</td>
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
<td align="left">baseobject</td>
<td align="right">2,500</td>
<td align="right">100.0%</td>
<td align="right">2,560</td>
<td align="right">92.8%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">200</td>
<td align="right">7.2%</td>
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
<td align="right">61,440</td>
<td align="right">0.4%</td>
<td align="right">69,120</td>
<td align="right">0.5%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,017,600</td>
<td align="right">91.0%</td>
<td align="right">13,017,600</td>
<td align="right">91.0%</td>
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
<td align="right">1,221,120</td>
<td align="right">8.5%</td>
<td align="right">1,221,120</td>
<td align="right">8.5%</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
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
<td align="left">list</td>
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">40</td>
<td align="right">50.0%</td>
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
<td align="right">42,040</td>
<td align="right">1.4%</td>
<td align="right">151,180</td>
<td align="right">3.9%</td>
<td align="right">259.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,993,700</td>
<td align="right">98.6%</td>
<td align="right">3,773,900</td>
<td align="right">96.1%</td>
<td align="right">26.1%</td>
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
<td align="right">740</td>
<td align="right">100.0%</td>
<td align="right">920</td>
<td align="right">100.0%</td>
<td align="right">24.3%</td>
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
<td align="left">dict items</td>
<td align="right">300</td>
<td align="right">40.5%</td>
<td align="right">480</td>
<td align="right">52.2%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">260</td>
<td align="right">35.1%</td>
<td align="right">260</td>
<td align="right">28.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">180</td>
<td align="right">24.3%</td>
<td align="right">180</td>
<td align="right">19.6%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,628,160</td>
<td align="right">0.5%</td>
<td align="right">4,519,420</td>
<td align="right">1.4%</td>
<td align="right">177.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,979,260</td>
<td align="right">4.1%</td>
<td align="right">13,301,820</td>
<td align="right">4.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">302,554,200</td>
<td align="right">95.4%</td>
<td align="right">302,620,520</td>
<td align="right">94.4%</td>
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
<td align="right">30,900</td>
<td align="right">84.8%</td>
<td align="right">85,440</td>
<td align="right">93.7%</td>
<td align="right">176.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,560</td>
<td align="right">15.2%</td>
<td align="right">5,700</td>
<td align="right">6.3%</td>
<td align="right">2.5%</td>
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
<td align="right">4,660</td>
<td align="right">83.8%</td>
<td align="right">4,800</td>
<td align="right">84.2%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">760</td>
<td align="right">13.7%</td>
<td align="right">760</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">120</td>
<td align="right">2.2%</td>
<td align="right">120</td>
<td align="right">2.1%</td>
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
<td align="right">30,464,360</td>
<td align="right">100.0%</td>
<td align="right">32,445,360</td>
<td align="right">100.0%</td>
<td align="right">6.5%</td>
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
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">80</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,053,940</td>
<td align="right">4.3%</td>
<td align="right">4,654,360</td>
<td align="right">6.4%</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">68,713,260</td>
<td align="right">95.7%</td>
<td align="right">68,562,400</td>
<td align="right">93.6%</td>
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
<td align="left">Success</td>
<td align="right">57,620</td>
<td align="right">100.0%</td>
<td align="right">87,800</td>
<td align="right">100.0%</td>
<td align="right">52.4%</td>
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
<td align="right">7,680</td>
<td align="right">100.0%</td>
<td align="right">7,680</td>
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
<td align="right">1,881,080</td>
<td align="right">3.2%</td>
<td align="right">1,918,460</td>
<td align="right">3.3%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">56,444,300</td>
<td align="right">96.8%</td>
<td align="right">56,420,620</td>
<td align="right">96.7%</td>
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
<td align="right">7,740</td>
<td align="right">0.0%</td>
<td align="right">7,740</td>
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
<td align="right">35,520</td>
<td align="right">99.8%</td>
<td align="right">36,200</td>
<td align="right">99.8%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">60</td>
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
<td align="left">other</td>
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
<td align="right">7,134,780</td>
<td align="right">100.0%</td>
<td align="right">7,134,780</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">9,261,800</td>
<td align="right">1.2%</td>
<td align="right">13,790,740</td>
<td align="right">1.6%</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">26,081,740</td>
<td align="right">3.4%</td>
<td align="right">29,972,420</td>
<td align="right">3.6%</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">376,779,480</td>
<td align="right">49.4%</td>
<td align="right">415,896,580</td>
<td align="right">49.5%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">351,360,620</td>
<td align="right">46.0%</td>
<td align="right">380,879,280</td>
<td align="right">45.3%</td>
<td align="right">8.4%</td>
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
<td align="left">BINARY_SLICE</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">1,688,280</td>
<td align="right">5.6%</td>
<td align="right">2,110,250.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,993,700</td>
<td align="right">11.5%</td>
<td align="right">3,773,900</td>
<td align="right">12.6%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">61,440</td>
<td align="right">0.2%</td>
<td align="right">69,120</td>
<td align="right">0.2%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">10,022,400</td>
<td align="right">38.4%</td>
<td align="right">11,113,820</td>
<td align="right">37.1%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,979,260</td>
<td align="right">49.8%</td>
<td align="right">13,301,820</td>
<td align="right">44.4%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">7,740</td>
<td align="right">0.0%</td>
<td align="right">7,740</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">7,680</td>
<td align="right">0.0%</td>
<td align="right">7,680</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">610,560</td>
<td align="right">6.6%</td>
<td align="right">1,670,480</td>
<td align="right">12.1%</td>
<td align="right">173.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,053,940</td>
<td align="right">33.0%</td>
<td align="right">4,654,360</td>
<td align="right">33.7%</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">915,040</td>
<td align="right">9.9%</td>
<td align="right">933,660</td>
<td align="right">6.8%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">501,860</td>
<td align="right">5.4%</td>
<td align="right">500,060</td>
<td align="right">3.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,017,600</td>
<td align="right">11.0%</td>
<td align="right">1,017,600</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">732,640</td>
<td align="right">7.9%</td>
<td align="right">732,640</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">710,040</td>
<td align="right">7.7%</td>
<td align="right">710,040</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">610,560</td>
<td align="right">6.6%</td>
<td align="right">610,560</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">610,560</td>
<td align="right">6.6%</td>
<td align="right">610,560</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">405,880</td>
<td align="right">4.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,831,340</td>
<td align="right">13.3%</td>
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
<td align="right">8,340,540</td>
<td align="right">14.4%</td>
<td align="right">8,340,540</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">49,674,600</td>
<td align="right">85.6%</td>
<td align="right">49,674,600</td>
<td align="right">85.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,340,540</td>
<td align="right">14.4%</td>
<td align="right">8,340,540</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">8,340,540</td>
<td align="right">14.4%</td>
<td align="right">8,340,540</td>
<td align="right">14.4%</td>
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
<td align="right">8,340,540</td>
<td align="right">14.4%</td>
<td align="right">8,340,540</td>
<td align="right">14.4%</td>
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
<td align="right">844,800</td>
<td align="right">1.5%</td>
<td align="right">844,800</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
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
<td align="right">5,145,600</td>
<td align="right">8.9%</td>
<td align="right">5,145,600</td>
<td align="right">8.9%</td>
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
<td align="right">23,040</td>
<td align="right">0.0%</td>
<td align="right">23,040</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">58,015,140</td>
<td align="right">100.0%</td>
<td align="right">58,015,140</td>
<td align="right">100.0%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,401,999</td>
<td align="right"></td>
<td align="right">896,397</td>
<td align="right"></td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,448,218</td>
<td align="right"></td>
<td align="right">941,059</td>
<td align="right"></td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">77,782,980</td>
<td align="right">6.2%</td>
<td align="right">87,027,800</td>
<td align="right">7.0%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">541,670,121</td>
<td align="right">39.0%</td>
<td align="right">492,305,538</td>
<td align="right">35.7%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">384,058,420</td>
<td align="right">30.4%</td>
<td align="right">415,649,020</td>
<td align="right">33.2%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">550,545,944</td>
<td align="right">43.6%</td>
<td align="right">505,722,740</td>
<td align="right">40.4%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">447,349,140</td>
<td align="right">32.2%</td>
<td align="right">483,481,180</td>
<td align="right">35.1%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">122,176,880</td>
<td align="right">8.8%</td>
<td align="right">131,942,820</td>
<td align="right">9.6%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">46,219</td>
<td align="right"></td>
<td align="right">44,663</td>
<td align="right"></td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">250,290,012</td>
<td align="right">19.8%</td>
<td align="right">241,904,640</td>
<td align="right">19.3%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">277,331,555</td>
<td align="right">20.0%</td>
<td align="right">270,065,322</td>
<td align="right">19.6%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">45,536,821</td>
<td align="right"></td>
<td align="right">46,211,963</td>
<td align="right"></td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">15,137,141</td>
<td align="right"></td>
<td align="right">15,138,697</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,264,960</td>
<td align="right"></td>
<td align="right">14,264,200</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,268,000</td>
<td align="right">23.9%</td>
<td align="right">14,267,300</td>
<td align="right">23.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">45,524,580</td>
<td align="right">76.1%</td>
<td align="right">45,525,200</td>
<td align="right">76.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">44,961,777</td>
<td align="right"></td>
<td align="right">44,962,378</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">45,524,360</td>
<td align="right">76.1%</td>
<td align="right">45,524,940</td>
<td align="right">76.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,213,440</td>
<td align="right"></td>
<td align="right">1,213,440</td>
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
<td align="right">1,140</td>
<td align="right">2,001,240</td>
<td align="right">25,342,931</td>
<td align="right">1,140</td>
<td align="right">2,001,240</td>
<td align="right">25,369,780</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">20</td>
<td align="right">0.9%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,820</td>
<td align="right">85.8%</td>
<td align="right">140</td>
<td align="right">25.9%</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,920</td>
<td align="right">90.6%</td>
<td align="right">300</td>
<td align="right">55.6%</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">2,120</td>
<td align="right"></td>
<td align="right">540</td>
<td align="right"></td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">39,441,660</td>
<td align="right"></td>
<td align="right">23,554,900</td>
<td align="right"></td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">280</td>
<td align="right">13.2%</td>
<td align="right">380</td>
<td align="right">70.4%</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,390,052,040</td>
<td align="right">3,524.3%</td>
<td align="right">1,216,812,820</td>
<td align="right">5,165.9%</td>
<td align="right">-12.5%</td>
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
<td align="right">0.9%</td>
<td align="right">20</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
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
<td align="right">280</td>
<td align="right"></td>
<td align="right">380</td>
<td align="right"></td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">280</td>
<td align="right">100.0%</td>
<td align="right">340</td>
<td align="right">89.5%</td>
<td align="right">21.4%</td>
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
<td align="right">40</td>
<td align="right">14.3%</td>
<td align="right">40</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20</td>
<td align="right">7.1%</td>
<td align="right">80</td>
<td align="right">21.1%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">160</td>
<td align="right">57.1%</td>
<td align="right">80</td>
<td align="right">21.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">40</td>
<td align="right">14.3%</td>
<td align="right">160</td>
<td align="right">42.1%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">5.3%</td>
<td align="right">20 / 0 !!</td>
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
<td align="right">7.1%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">60</td>
<td align="right">21.4%</td>
<td align="right">80</td>
<td align="right">21.1%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20</td>
<td align="right">7.1%</td>
<td align="right">120</td>
<td align="right">31.6%</td>
<td align="right">500.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">140</td>
<td align="right">50.0%</td>
<td align="right">60</td>
<td align="right">15.8%</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">40</td>
<td align="right">14.3%</td>
<td align="right">80</td>
<td align="right">21.1%</td>
<td align="right">100.0%</td>
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
<td align="right">20</td>
<td align="right">7.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_BUILD_LIST</td>
<td align="right">874,980</td>
<td align="right">45,220</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,743,360</td>
<td align="right">90,440</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">867,840</td>
<td align="right">45,220</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">337,920</td>
<td align="right">92,240</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">337,920</td>
<td align="right">92,240</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">337,920</td>
<td align="right">92,240</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">2,680,320</td>
<td align="right">992,040</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">2,680,240</td>
<td align="right">992,040</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,069,900</td>
<td align="right">1,417,580</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,803,200</td>
<td align="right">1,412,260</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,633,940</td>
<td align="right">829,440</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,666,560</td>
<td align="right">862,080</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,666,560</td>
<td align="right">862,080</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">242,180</td>
<td align="right">133,040</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">242,180</td>
<td align="right">133,040</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">167,380</td>
<td align="right">95,000</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,626,560</td>
<td align="right">1,509,520</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,911,280</td>
<td align="right">1,124,120</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">39,441,660</td>
<td align="right">23,554,900</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">37,652,120</td>
<td align="right">22,569,920</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">8,847,620</td>
<td align="right">5,556,300</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">44,402,680</td>
<td align="right">28,523,280</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,052,160</td>
<td align="right">677,880</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">9,630,720</td>
<td align="right">6,405,120</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,588,720</td>
<td align="right">1,108,000</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">2,774,240</td>
<td align="right">1,982,880</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">2,526,180</td>
<td align="right">1,833,480</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">168,980</td>
<td align="right">122,900</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">5,798,420</td>
<td align="right">4,306,060</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,466,880</td>
<td align="right">1,103,940</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,165,760</td>
<td align="right">1,645,560</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">60,176,100</td>
<td align="right">47,150,120</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">2,472,960</td>
<td align="right">1,952,760</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">7,173,120</td>
<td align="right">5,687,540</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">13,411,040</td>
<td align="right">10,856,660</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,021,080</td>
<td align="right">3,262,720</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">4,620,120</td>
<td align="right">3,769,580</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">70,467,260</td>
<td align="right">57,652,520</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,364,940</td>
<td align="right">1,937,440</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">62,438,960</td>
<td align="right">51,268,080</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">15,448,080</td>
<td align="right">12,742,040</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">24,151,780</td>
<td align="right">20,185,800</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">18,547,400</td>
<td align="right">15,518,320</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">7,541,760</td>
<td align="right">6,450,340</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">27,508,180</td>
<td align="right">23,613,540</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">18,201,520</td>
<td align="right">15,677,520</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">15,310,440</td>
<td align="right">13,281,300</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">490,480</td>
<td align="right">430,120</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">9,693,040</td>
<td align="right">8,511,000</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,504,640</td>
<td align="right">10,121,380</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,120,200</td>
<td align="right">2,812,320</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">13,567,900</td>
<td align="right">12,261,280</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">13,567,900</td>
<td align="right">12,261,280</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,131,840</td>
<td align="right">3,757,560</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">9,063,960</td>
<td align="right">8,283,760</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">32,916,400</td>
<td align="right">30,300,540</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">889,800</td>
<td align="right">829,440</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">11,219,940</td>
<td align="right">10,491,300</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">30,548,400</td>
<td align="right">28,846,120</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">8,113,480</td>
<td align="right">7,681,560</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,068,500</td>
<td align="right">9,553,820</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">38,541,340</td>
<td align="right">36,703,580</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">147,928,260</td>
<td align="right">140,939,960</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">206,195,320</td>
<td align="right">196,925,700</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">10,011,480</td>
<td align="right">9,562,360</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">11,057,620</td>
<td align="right">10,569,760</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,090,560</td>
<td align="right">1,044,480</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">11,901,340</td>
<td align="right">11,399,200</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">55,536,820</td>
<td align="right">54,343,600</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">19,844,580</td>
<td align="right">19,421,580</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">19,629,000</td>
<td align="right">19,269,540</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">843,720</td>
<td align="right">829,440</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">19,214,280</td>
<td align="right">18,962,340</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">19,207,140</td>
<td align="right">18,962,340</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">9,828,260</td>
<td align="right">9,761,300</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">19,330,020</td>
<td align="right">19,230,720</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">6,681,600</td>
<td align="right">6,696,960</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,961,020</td>
<td align="right">4,968,380</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">18,900,480</td>
<td align="right">18,915,840</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">9,468,900</td>
<td align="right">9,461,760</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">11,412,480</td>
<td align="right">11,420,160</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">122,980</td>
<td align="right">122,900</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">28,377,060</td>
<td align="right">28,385,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">9,461,760</td>
<td align="right">9,461,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">5,744,680</td>
<td align="right">5,744,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,926,080</td>
<td align="right">2,926,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,419,380</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">1,052,160</td>
<td align="right">1,052,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,044,480</td>
<td align="right">1,044,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">829,440</td>
<td align="right">829,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">559,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">307,200</td>
<td align="right">307,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">192,000</td>
<td align="right">192,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">61,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">53,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">46,080</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">46,080</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">15,360</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">14,280</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">7,680</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">7,680</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">7,140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">7,140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">7,140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">20</td>
<td align="right">20</td>
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
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-21
