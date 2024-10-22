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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,111,280</td>
<td align="right">10,480</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,366,480</td>
<td align="right">17,880</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,936,820</td>
<td align="right">110,600</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,214,260</td>
<td align="right">53,620</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,187,800</td>
<td align="right">62,080</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,480,900</td>
<td align="right">148,880</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,529,800</td>
<td align="right">104,900</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,063,100</td>
<td align="right">668,720</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,047,100</td>
<td align="right">121,540</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,030,440</td>
<td align="right">179,620</td>
<td align="right">-82.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">5,151,440</td>
<td align="right">926,280</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,543,320</td>
<td align="right">1,772,120</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">699,780</td>
<td align="right">131,280</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,142,020</td>
<td align="right">223,580</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">588,640</td>
<td align="right">117,400</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">30,530,440</td>
<td align="right">6,307,580</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">71,640</td>
<td align="right">20,220</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">11,260</td>
<td align="right">3,500</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">28,827,440</td>
<td align="right">8,967,700</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">22,217,240</td>
<td align="right">7,441,300</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">174,080</td>
<td align="right">61,740</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">17,388,060</td>
<td align="right">6,179,000</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">46,353,240</td>
<td align="right">17,150,360</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,532,320</td>
<td align="right">1,686,620</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">12,433,120</td>
<td align="right">5,092,900</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,023,860</td>
<td align="right">3,773,660</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,912,120</td>
<td align="right">1,672,380</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">17,076,640</td>
<td align="right">7,374,600</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">4,935,920</td>
<td align="right">2,200,900</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">62,702,940</td>
<td align="right">28,029,960</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">7,260</td>
<td align="right">3,440</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">16,691,220</td>
<td align="right">7,910,340</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">24,748,180</td>
<td align="right">11,760,320</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,686,880</td>
<td align="right">1,298,640</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,773,560</td>
<td align="right">866,640</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">165,807,880</td>
<td align="right">82,548,320</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">22,734,820</td>
<td align="right">11,325,860</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,323,260</td>
<td align="right">1,661,180</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,323,340</td>
<td align="right">1,661,260</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">37,732,100</td>
<td align="right">19,275,020</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">10,327,740</td>
<td align="right">5,469,160</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">61,440</td>
<td align="right">32,720</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">20,460</td>
<td align="right">11,140</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">13,157,820</td>
<td align="right">7,176,500</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,396,640</td>
<td align="right">2,407,180</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">34,947,060</td>
<td align="right">20,049,620</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">20,480</td>
<td align="right">12,160</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">20,480</td>
<td align="right">12,160</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">51,120</td>
<td align="right">30,500</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">30,995,560</td>
<td align="right">18,834,060</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">3,703,560</td>
<td align="right">2,267,480</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">7,631,160</td>
<td align="right">4,812,020</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">962,180</td>
<td align="right">607,360</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,119,440</td>
<td align="right">1,353,980</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">18,200</td>
<td align="right">11,700</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,014,580</td>
<td align="right">2,610,060</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">4,064,320</td>
<td align="right">2,657,180</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">995,220</td>
<td align="right">652,200</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,036,180</td>
<td align="right">680,120</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">52,939,160</td>
<td align="right">35,450,920</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">82,000</td>
<td align="right">56,920</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">10,220</td>
<td align="right">7,140</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">228,600</td>
<td align="right">161,500</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">15,782,580</td>
<td align="right">11,159,180</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">51,420</td>
<td align="right">36,560</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,180,400</td>
<td align="right">2,996,360</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">30,380</td>
<td align="right">21,920</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,241,140</td>
<td align="right">3,077,800</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,360,760</td>
<td align="right">2,492,540</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">155,280</td>
<td align="right">115,980</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">839,680</td>
<td align="right">668,300</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,986,680</td>
<td align="right">3,174,960</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">16,640</td>
<td align="right">13,540</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,333,560</td>
<td align="right">1,095,800</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">61,440</td>
<td align="right">50,640</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">645,000</td>
<td align="right">585,440</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">3,673,640</td>
<td align="right">3,354,580</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">58,420</td>
<td align="right">55,160</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">15,654,560</td>
<td align="right">15,240,700</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,501,340</td>
<td align="right">1,468,820</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">12,500</td>
<td align="right">12,280</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,220</td>
<td align="right">10,240</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,120,760</td>
<td align="right">11,120,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">6,922,260</td>
<td align="right">6,922,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">6,860,800</td>
<td align="right">6,860,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,715,180</td>
<td align="right">1,715,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,413,100</td>
<td align="right">1,413,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,208,280</td>
<td align="right">1,208,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,013,920</td>
<td align="right">1,013,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">604,160</td>
<td align="right">604,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">80,000</td>
<td align="right">80,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">61,440</td>
<td align="right">61,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">40,940</td>
<td align="right">40,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">30,720</td>
<td align="right">30,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">30,720</td>
<td align="right">30,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">30,720</td>
<td align="right">30,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">11,420</td>
<td align="right">11,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">10,920</td>
<td align="right">10,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">10,240</td>
<td align="right">10,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">10,220</td>
<td align="right">10,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">10,220</td>
<td align="right">10,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">6,600</td>
<td align="right">6,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,040</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,720</td>
<td align="right">1,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,000</td>
<td align="right">1,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">760</td>
<td align="right">760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
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
<td align="right">380</td>
<td align="right">0.0%</td>
<td align="right">380</td>
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
<td align="right">51,844,680</td>
<td align="right">100.0%</td>
<td align="right">51,844,680</td>
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
<td align="right">380</td>
<td align="right">100.0%</td>
<td align="right">380</td>
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
<td align="right">10,220</td>
<td align="right">100.0%</td>
<td align="right">10,240</td>
<td align="right">100.0%</td>
<td align="right">0.2%</td>
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
<td align="right">10,820</td>
<td align="right">0.0%</td>
<td align="right">3,100</td>
<td align="right">0.0%</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,539,240</td>
<td align="right">99.9%</td>
<td align="right">34,539,240</td>
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
<td align="right">31,300</td>
<td align="right">0.1%</td>
<td align="right">31,300</td>
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
<td align="left">Failure</td>
<td align="right">160</td>
<td align="right">15.7%</td>
<td align="right">120</td>
<td align="right">12.2%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">860</td>
<td align="right">84.3%</td>
<td align="right">860</td>
<td align="right">87.8%</td>
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
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">-25.0%</td>
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
<td align="right">1,937,380</td>
<td align="right">2.2%</td>
<td align="right">1,833,740</td>
<td align="right">2.0%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">87,782,000</td>
<td align="right">97.8%</td>
<td align="right">87,952,100</td>
<td align="right">97.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,460</td>
<td align="right">0.0%</td>
<td align="right">5,460</td>
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
<td align="right">42,460</td>
<td align="right">100.0%</td>
<td align="right">40,520</td>
<td align="right">100.0%</td>
<td align="right">-4.6%</td>
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
<td align="left">init not inline values</td>
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
<td align="right">0.0%</td>
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
<td align="right">500</td>
<td align="right">50.0%</td>
<td align="right">500</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
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
<td align="right">7,627,260</td>
<td align="right">17.0%</td>
<td align="right">4,808,920</td>
<td align="right">11.4%</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">37,191,220</td>
<td align="right">83.0%</td>
<td align="right">37,191,220</td>
<td align="right">88.5%</td>
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
<td align="right">3,440</td>
<td align="right">88.2%</td>
<td align="right">2,640</td>
<td align="right">85.2%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">460</td>
<td align="right">11.8%</td>
<td align="right">460</td>
<td align="right">14.8%</td>
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
<td align="left">baseobject</td>
<td align="right">3,280</td>
<td align="right">95.3%</td>
<td align="right">2,480</td>
<td align="right">93.9%</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">160</td>
<td align="right">4.7%</td>
<td align="right">160</td>
<td align="right">6.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,627,880</td>
<td align="right">8.6%</td>
<td align="right">324,360</td>
<td align="right">1.7%</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,740</td>
<td align="right">0.0%</td>
<td align="right">2,960</td>
<td align="right">0.0%</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,356,780</td>
<td align="right">91.4%</td>
<td align="right">18,635,720</td>
<td align="right">98.3%</td>
<td align="right">7.4%</td>
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
<td align="right">30,980</td>
<td align="right">99.2%</td>
<td align="right">6,400</td>
<td align="right">97.0%</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">240</td>
<td align="right">0.8%</td>
<td align="right">200</td>
<td align="right">3.0%</td>
<td align="right">-16.7%</td>
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
<td align="right">140</td>
<td align="right">58.3%</td>
<td align="right">100</td>
<td align="right">50.0%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">100</td>
<td align="right">41.7%</td>
<td align="right">100</td>
<td align="right">50.0%</td>
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
<td align="right">4,012,640</td>
<td align="right">98.5%</td>
<td align="right">2,608,560</td>
<td align="right">97.9%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">58,780</td>
<td align="right">1.4%</td>
<td align="right">55,520</td>
<td align="right">2.1%</td>
<td align="right">-5.5%</td>
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
<td align="right">94.8%</td>
<td align="right">1,400</td>
<td align="right">93.3%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">100</td>
<td align="right">5.2%</td>
<td align="right">100</td>
<td align="right">6.7%</td>
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
<td align="left">ascii string</td>
<td align="right">540</td>
<td align="right">29.3%</td>
<td align="right">140</td>
<td align="right">10.0%</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">160</td>
<td align="right">8.7%</td>
<td align="right">120</td>
<td align="right">8.6%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">720</td>
<td align="right">39.1%</td>
<td align="right">720</td>
<td align="right">51.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">420</td>
<td align="right">22.8%</td>
<td align="right">420</td>
<td align="right">30.0%</td>
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
<td align="right">16,659,500</td>
<td align="right">3.9%</td>
<td align="right">7,881,840</td>
<td align="right">1.9%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">403,577,540</td>
<td align="right">95.5%</td>
<td align="right">401,995,980</td>
<td align="right">97.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,217,160</td>
<td align="right">0.5%</td>
<td align="right">2,217,160</td>
<td align="right">0.5%</td>
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
<td align="right">22,920</td>
<td align="right">31.2%</td>
<td align="right">19,700</td>
<td align="right">28.0%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">50,620</td>
<td align="right">68.8%</td>
<td align="right">50,620</td>
<td align="right">72.0%</td>
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
<td align="left">class method obj</td>
<td align="right">420</td>
<td align="right">1.8%</td>
<td align="right">340</td>
<td align="right">1.7%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">19,340</td>
<td align="right">84.4%</td>
<td align="right">16,340</td>
<td align="right">82.9%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,160</td>
<td align="right">13.8%</td>
<td align="right">3,020</td>
<td align="right">15.3%</td>
<td align="right">-4.4%</td>
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
<td align="right">40,398,500</td>
<td align="right">100.0%</td>
<td align="right">26,996,780</td>
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
<td align="right">3,300</td>
<td align="right">0.0%</td>
<td align="right">3,300</td>
<td align="right">0.0%</td>
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
<td align="right">4,240</td>
<td align="right">0.0%</td>
<td align="right">4,240</td>
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
<td align="right">3,380</td>
<td align="right">100.0%</td>
<td align="right">3,380</td>
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
<td align="right">4,170,480</td>
<td align="right">4.3%</td>
<td align="right">1,480,740</td>
<td align="right">1.6%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">91,798,120</td>
<td align="right">95.7%</td>
<td align="right">92,866,000</td>
<td align="right">98.4%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">860</td>
<td align="right">0.0%</td>
<td align="right">860</td>
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
<td align="right">79,540</td>
<td align="right">100.0%</td>
<td align="right">28,780</td>
<td align="right">100.0%</td>
<td align="right">-63.8%</td>
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
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">99.6%</td>
<td align="right">10,220</td>
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
<td align="right">2,155,820</td>
<td align="right">2.8%</td>
<td align="right">979,540</td>
<td align="right">1.5%</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,360</td>
<td align="right">0.0%</td>
<td align="right">10,280</td>
<td align="right">0.0%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">74,491,880</td>
<td align="right">97.2%</td>
<td align="right">64,090,820</td>
<td align="right">98.5%</td>
<td align="right">-14.0%</td>
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
<td align="right">43,520</td>
<td align="right">99.6%</td>
<td align="right">21,400</td>
<td align="right">99.4%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">160</td>
<td align="right">0.4%</td>
<td align="right">140</td>
<td align="right">0.6%</td>
<td align="right">-12.5%</td>
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
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">-12.5%</td>
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
<td align="right">9,512,880</td>
<td align="right">100.0%</td>
<td align="right">7,858,580</td>
<td align="right">100.0%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">80</td>
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
<td align="right">435,097,000</td>
<td align="right">52.1%</td>
<td align="right">201,423,560</td>
<td align="right">47.8%</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">28,403,540</td>
<td align="right">3.4%</td>
<td align="right">15,384,340</td>
<td align="right">3.7%</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">359,064,500</td>
<td align="right">43.0%</td>
<td align="right">197,435,880</td>
<td align="right">46.9%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">12,145,080</td>
<td align="right">1.5%</td>
<td align="right">6,872,080</td>
<td align="right">1.6%</td>
<td align="right">-43.4%</td>
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
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,820</td>
<td align="right">0.0%</td>
<td align="right">3,100</td>
<td align="right">0.0%</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">6,740</td>
<td align="right">0.0%</td>
<td align="right">2,960</td>
<td align="right">0.0%</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">16,659,500</td>
<td align="right">58.8%</td>
<td align="right">7,881,840</td>
<td align="right">51.4%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">7,627,260</td>
<td align="right">26.9%</td>
<td align="right">4,808,920</td>
<td align="right">31.4%</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,012,640</td>
<td align="right">14.2%</td>
<td align="right">2,608,560</td>
<td align="right">17.0%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">13,360</td>
<td align="right">0.0%</td>
<td align="right">10,280</td>
<td align="right">0.1%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,220</td>
<td align="right">0.0%</td>
<td align="right">10,240</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,460</td>
<td align="right">0.0%</td>
<td align="right">5,460</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,300</td>
<td align="right">0.0%</td>
<td align="right">3,300</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">860</td>
<td align="right">0.0%</td>
<td align="right">860</td>
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
<td align="left">CONTAINS_OP_SET</td>
<td align="right">814,080</td>
<td align="right">6.7%</td>
<td align="right">162,180</td>
<td align="right">2.4%</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">813,800</td>
<td align="right">6.7%</td>
<td align="right">162,180</td>
<td align="right">2.4%</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">4,170,480</td>
<td align="right">34.3%</td>
<td align="right">1,480,740</td>
<td align="right">21.5%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">640,060</td>
<td align="right">5.3%</td>
<td align="right">282,180</td>
<td align="right">4.1%</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,047,800</td>
<td align="right">8.6%</td>
<td align="right">482,260</td>
<td align="right">7.0%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">464,780</td>
<td align="right">3.8%</td>
<td align="right">215,100</td>
<td align="right">3.1%</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">945,960</td>
<td align="right">7.8%</td>
<td align="right">828,820</td>
<td align="right">12.1%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">976,580</td>
<td align="right">8.0%</td>
<td align="right">988,880</td>
<td align="right">14.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,357,340</td>
<td align="right">11.2%</td>
<td align="right">1,357,340</td>
<td align="right">19.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">828,500</td>
<td align="right">6.8%</td>
<td align="right">828,500</td>
<td align="right">12.1%</td>
<td align="right">0.0%</td>
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
<td align="right">11,120,760</td>
<td align="right">14.4%</td>
<td align="right">11,120,760</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">66,232,360</td>
<td align="right">85.6%</td>
<td align="right">66,232,360</td>
<td align="right">85.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">11,120,760</td>
<td align="right">14.4%</td>
<td align="right">11,120,760</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">11,120,760</td>
<td align="right">14.4%</td>
<td align="right">11,120,760</td>
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
<td align="right">11,120,760</td>
<td align="right">14.4%</td>
<td align="right">11,120,760</td>
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
<td align="right">1,126,420</td>
<td align="right">1.5%</td>
<td align="right">1,126,420</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">6,860,900</td>
<td align="right">8.9%</td>
<td align="right">6,860,900</td>
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
<td align="right">30,720</td>
<td align="right">0.0%</td>
<td align="right">30,720</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">77,353,120</td>
<td align="right">100.0%</td>
<td align="right">77,353,120</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,080</td>
<td align="right">0.0%</td>
<td align="right">4,000</td>
<td align="right">0.0%</td>
<td align="right">270.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">138,040,700</td>
<td align="right">7.8%</td>
<td align="right">70,943,120</td>
<td align="right">4.0%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,157,433</td>
<td align="right"></td>
<td align="right">656,011</td>
<td align="right"></td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">441,791,880</td>
<td align="right">24.8%</td>
<td align="right">263,971,760</td>
<td align="right">15.0%</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,271,816</td>
<td align="right"></td>
<td align="right">803,537</td>
<td align="right"></td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">136,160,880</td>
<td align="right">7.3%</td>
<td align="right">89,810,980</td>
<td align="right">4.7%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">115,854</td>
<td align="right"></td>
<td align="right">149,013</td>
<td align="right"></td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">821,925,775</td>
<td align="right">46.2%</td>
<td align="right">1,018,870,823</td>
<td align="right">57.8%</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">533,669,760</td>
<td align="right">28.5%</td>
<td align="right">417,325,480</td>
<td align="right">22.0%</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">802,546,592</td>
<td align="right">42.8%</td>
<td align="right">939,668,945</td>
<td align="right">49.5%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">400,896,498</td>
<td align="right">21.4%</td>
<td align="right">451,399,471</td>
<td align="right">23.8%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">376,574,477</td>
<td align="right">21.2%</td>
<td align="right">408,877,399</td>
<td align="right">23.2%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">59,907,869</td>
<td align="right"></td>
<td align="right">61,563,745</td>
<td align="right"></td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">60,702,820</td>
<td align="right">76.1%</td>
<td align="right">62,362,840</td>
<td align="right">76.6%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">60,701,580</td>
<td align="right">76.1%</td>
<td align="right">62,358,440</td>
<td align="right">76.6%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">61,104,887</td>
<td align="right"></td>
<td align="right">61,297,489</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">20,128,726</td>
<td align="right"></td>
<td align="right">20,095,567</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">19,020,540</td>
<td align="right"></td>
<td align="right">19,019,400</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">19,022,100</td>
<td align="right">23.9%</td>
<td align="right">19,020,960</td>
<td align="right">23.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,617,920</td>
<td align="right"></td>
<td align="right">1,617,920</td>
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
<td align="right">1,520</td>
<td align="right">2,127,420</td>
<td align="right">30,859,640</td>
<td align="right">1,520</td>
<td align="right">2,127,420</td>
<td align="right">30,859,320</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">740</td>
<td align="right">7.1%</td>
<td align="right">1,750.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,280</td>
<td align="right">30.8%</td>
<td align="right">6,600</td>
<td align="right">63.5%</td>
<td align="right">189.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">5,500</td>
<td align="right">74.3%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">180</td>
<td align="right">2.4%</td>
<td align="right">360</td>
<td align="right">3.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">66,159,880</td>
<td align="right"></td>
<td align="right">93,029,720</td>
<td align="right"></td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">7,400</td>
<td align="right"></td>
<td align="right">10,400</td>
<td align="right"></td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">5,080</td>
<td align="right">68.6%</td>
<td align="right">3,060</td>
<td align="right">29.4%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">2,412,339,880</td>
<td align="right">3,646.2%</td>
<td align="right">3,184,332,520</td>
<td align="right">3,422.9%</td>
<td align="right">32.0%</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">2,160</td>
<td align="right">94.7%</td>
<td align="right">6,480</td>
<td align="right">98.2%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,280</td>
<td align="right"></td>
<td align="right">6,600</td>
<td align="right"></td>
<td align="right">189.5%</td>
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
<td align="right">60</td>
<td align="right">2.6%</td>
<td align="right">60</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
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
<td align="right">280</td>
<td align="right">12.3%</td>
<td align="right">460</td>
<td align="right">7.0%</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">520</td>
<td align="right">22.8%</td>
<td align="right">1,420</td>
<td align="right">21.5%</td>
<td align="right">173.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">400</td>
<td align="right">17.5%</td>
<td align="right">1,240</td>
<td align="right">18.8%</td>
<td align="right">210.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">600</td>
<td align="right">26.3%</td>
<td align="right">1,880</td>
<td align="right">28.5%</td>
<td align="right">213.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">160</td>
<td align="right">7.0%</td>
<td align="right">800</td>
<td align="right">12.1%</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">260</td>
<td align="right">11.4%</td>
<td align="right">700</td>
<td align="right">10.6%</td>
<td align="right">169.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">60</td>
<td align="right">2.6%</td>
<td align="right">100</td>
<td align="right">1.5%</td>
<td align="right">66.7%</td>
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
<td align="right">140</td>
<td align="right">6.1%</td>
<td align="right">100</td>
<td align="right">1.5%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">320</td>
<td align="right">14.0%</td>
<td align="right">740</td>
<td align="right">11.2%</td>
<td align="right">131.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">580</td>
<td align="right">25.4%</td>
<td align="right">1,420</td>
<td align="right">21.5%</td>
<td align="right">144.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">440</td>
<td align="right">19.3%</td>
<td align="right">1,760</td>
<td align="right">26.7%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">340</td>
<td align="right">14.9%</td>
<td align="right">1,460</td>
<td align="right">22.1%</td>
<td align="right">329.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">140</td>
<td align="right">6.1%</td>
<td align="right">500</td>
<td align="right">7.6%</td>
<td align="right">257.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">200</td>
<td align="right">8.8%</td>
<td align="right">500</td>
<td align="right">7.6%</td>
<td align="right">150.0%</td>
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
<td align="left">_DEOPT</td>
<td align="right">10,020</td>
<td align="right">836,440</td>
<td align="right">8,247.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,860</td>
<td align="right">388,060</td>
<td align="right">3,835.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,860</td>
<td align="right">347,600</td>
<td align="right">3,425.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">18,540</td>
<td align="right">374,600</td>
<td align="right">1,920.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">18,540</td>
<td align="right">361,560</td>
<td align="right">1,850.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">77,340</td>
<td align="right">1,425,940</td>
<td align="right">1,743.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">77,340</td>
<td align="right">1,425,940</td>
<td align="right">1,743.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">48,120</td>
<td align="right">859,840</td>
<td align="right">1,686.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">275,360</td>
<td align="right">3,908,040</td>
<td align="right">1,319.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">134,380</td>
<td align="right">1,510,060</td>
<td align="right">1,023.7%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">2,707,060</td>
<td align="right">26,116,440</td>
<td align="right">864.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">2,166,720</td>
<td align="right">12,478,300</td>
<td align="right">475.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">1,823,380</td>
<td align="right">10,151,120</td>
<td align="right">456.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">858,340</td>
<td align="right">3,972,400</td>
<td align="right">362.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,340,860</td>
<td align="right">5,269,940</td>
<td align="right">293.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">11,798,000</td>
<td align="right">43,125,840</td>
<td align="right">265.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">465,640</td>
<td align="right">1,566,440</td>
<td align="right">236.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">6,526,840</td>
<td align="right">21,638,420</td>
<td align="right">231.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,957,640</td>
<td align="right">5,925,680</td>
<td align="right">202.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">17,530,120</td>
<td align="right">49,551,360</td>
<td align="right">182.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">1,402,580</td>
<td align="right">3,939,420</td>
<td align="right">180.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">4,362,620</td>
<td align="right">11,837,560</td>
<td align="right">171.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">8,940</td>
<td align="right">23,800</td>
<td align="right">166.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">737,200</td>
<td align="right">1,862,920</td>
<td align="right">152.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">550,340</td>
<td align="right">1,342,280</td>
<td align="right">143.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">2,463,800</td>
<td align="right">5,937,720</td>
<td align="right">141.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,114,280</td>
<td align="right">2,555,920</td>
<td align="right">129.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,972,340</td>
<td align="right">4,292,220</td>
<td align="right">117.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">2,145,720</td>
<td align="right">4,535,080</td>
<td align="right">111.4%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">7,929,780</td>
<td align="right">16,635,660</td>
<td align="right">109.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,214,400</td>
<td align="right">4,625,040</td>
<td align="right">108.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,503,760</td>
<td align="right">5,187,540</td>
<td align="right">107.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,449,960</td>
<td align="right">2,874,860</td>
<td align="right">98.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,614,500</td>
<td align="right">3,185,600</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,982,540</td>
<td align="right">7,623,720</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">981,240</td>
<td align="right">1,849,460</td>
<td align="right">88.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">11,452,660</td>
<td align="right">21,256,220</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">20,848,420</td>
<td align="right">38,550,440</td>
<td align="right">84.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">11,264,600</td>
<td align="right">20,749,940</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">20,848,420</td>
<td align="right">38,328,760</td>
<td align="right">83.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">6,200,880</td>
<td align="right">11,199,700</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">23,555,480</td>
<td align="right">41,899,660</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">23,555,480</td>
<td align="right">41,890,340</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">5,191,440</td>
<td align="right">9,150,020</td>
<td align="right">76.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">13,857,060</td>
<td align="right">24,194,400</td>
<td align="right">74.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">13,259,120</td>
<td align="right">22,852,880</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">5,805,580</td>
<td align="right">9,777,180</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">3,719,120</td>
<td align="right">6,242,460</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,120,720</td>
<td align="right">3,527,860</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,480,960</td>
<td align="right">5,720,700</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">10,100,300</td>
<td align="right">16,308,920</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">21,986,160</td>
<td align="right">35,416,580</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">6,320,300</td>
<td align="right">9,733,160</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">25,065,900</td>
<td align="right">37,790,840</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">75,440</td>
<td align="right">107,960</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">41,510,400</td>
<td align="right">59,151,380</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">66,159,880</td>
<td align="right">93,029,720</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">52,357,680</td>
<td align="right">72,382,060</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">72,403,580</td>
<td align="right">99,273,720</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">138,763,260</td>
<td align="right">188,753,660</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">56,909,680</td>
<td align="right">76,373,920</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">25,865,960</td>
<td align="right">34,624,040</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">13,437,160</td>
<td align="right">17,785,400</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">16,329,640</td>
<td align="right">21,579,840</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">2,707,060</td>
<td align="right">3,557,880</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">3,599,240</td>
<td align="right">4,708,500</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,962,620</td>
<td align="right">2,531,120</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">9,663,060</td>
<td align="right">12,396,440</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">44,660,500</td>
<td align="right">57,045,600</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">124,475,120</td>
<td align="right">157,017,720</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">16,041,440</td>
<td align="right">18,944,880</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">318,396,760</td>
<td align="right">375,448,960</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">15,792,080</td>
<td align="right">18,610,420</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">307,675,340</td>
<td align="right">360,366,120</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">222,798,960</td>
<td align="right">257,471,940</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,145,200</td>
<td align="right">1,318,120</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">28,875,800</td>
<td align="right">33,100,960</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">14,321,580</td>
<td align="right">16,339,220</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">12,064,260</td>
<td align="right">13,468,340</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">17,272,380</td>
<td align="right">19,204,480</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">2,961,680</td>
<td align="right">3,280,740</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">13,868,140</td>
<td align="right">15,304,220</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">45,084,360</td>
<td align="right">49,713,140</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">28,249,580</td>
<td align="right">31,134,780</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">28,143,360</td>
<td align="right">30,989,060</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,308,060</td>
<td align="right">2,531,580</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,153,880</td>
<td align="right">1,220,980</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">16,204,340</td>
<td align="right">17,122,780</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">85,700</td>
<td align="right">89,480</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">27,078,800</td>
<td align="right">28,239,440</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">27,810,060</td>
<td align="right">28,973,400</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">63,442,800</td>
<td align="right">66,076,840</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">80,186,020</td>
<td align="right">83,187,560</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">28,659,720</td>
<td align="right">29,566,640</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">3,909,200</td>
<td align="right">3,997,700</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">68,929,660</td>
<td align="right">70,155,860</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">191,300</td>
<td align="right">194,560</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">310,140</td>
<td align="right">313,400</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">310,140</td>
<td align="right">313,400</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,392,340</td>
<td align="right">1,400,060</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">3,133,600</td>
<td align="right">3,142,060</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">3,563,540</td>
<td align="right">3,571,600</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,189,620</td>
<td align="right">6,197,400</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">6,243,700</td>
<td align="right">6,244,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">3,563,540</td>
<td align="right">3,563,520</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">8,938,320</td>
<td align="right">8,938,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,071,300</td>
<td align="right">1,071,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,071,300</td>
<td align="right">1,071,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,071,300</td>
<td align="right">1,071,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">9,940</td>
<td align="right">9,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">9,940</td>
<td align="right">9,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">9,860</td>
<td align="right">9,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right"></td>
<td align="right">2,735,020</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">1,654,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right"></td>
<td align="right">1,104,840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">354,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">354,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right"></td>
<td align="right">171,380</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">112,340</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right"></td>
<td align="right">62,220</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">59,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">59,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">51,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right"></td>
<td align="right">36,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">28,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">25,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">20,620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right"></td>
<td align="right">20,620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">10,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right"></td>
<td align="right">9,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right"></td>
<td align="right">9,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right"></td>
<td align="right">8,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">8,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">3,080</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">140</td>
<td align="right">1,040</td>
<td align="right">642.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right"></td>
<td align="right">460</td>
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
Stats gathered on: 2024-10-21
