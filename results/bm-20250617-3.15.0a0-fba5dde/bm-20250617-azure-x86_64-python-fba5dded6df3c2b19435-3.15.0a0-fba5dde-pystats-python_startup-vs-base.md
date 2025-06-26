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
<td align="left">STORE_SUBSCR</td>
<td align="right">20</td>
<td align="right">40</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">800</td>
<td align="right">720</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">400</td>
<td align="right">360</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">400</td>
<td align="right">360</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">200</td>
<td align="right">180</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">200</td>
<td align="right">180</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">200</td>
<td align="right">180</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">200</td>
<td align="right">180</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">200</td>
<td align="right">180</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">4,100</td>
<td align="right">3,720</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">3,700</td>
<td align="right">3,360</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3,700</td>
<td align="right">3,360</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">10,900</td>
<td align="right">9,900</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">52,920</td>
<td align="right">48,080</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">70,000</td>
<td align="right">63,600</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">7,000</td>
<td align="right">6,360</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">3,500</td>
<td align="right">3,180</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">3,500</td>
<td align="right">3,180</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">7,220</td>
<td align="right">6,560</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">17,320</td>
<td align="right">15,740</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">34,000</td>
<td align="right">30,900</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">25,720</td>
<td align="right">23,380</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">6,820</td>
<td align="right">6,200</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">6,820</td>
<td align="right">6,200</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">3,520</td>
<td align="right">3,200</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">3,300</td>
<td align="right">3,000</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">101,320</td>
<td align="right">92,160</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">34,140</td>
<td align="right">31,060</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">61,540</td>
<td align="right">56,000</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">106,440</td>
<td align="right">96,860</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">86,700</td>
<td align="right">78,900</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">190,980</td>
<td align="right">173,840</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">86,020</td>
<td align="right">78,300</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">7,820</td>
<td align="right">7,120</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">15,220</td>
<td align="right">13,860</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">7,200</td>
<td align="right">6,560</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">116,360</td>
<td align="right">106,020</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">36,040</td>
<td align="right">32,840</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">25,540</td>
<td align="right">23,280</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">39,560</td>
<td align="right">36,060</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">140,120</td>
<td align="right">127,740</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">4,120</td>
<td align="right">3,760</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">4,120</td>
<td align="right">3,760</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">55,000</td>
<td align="right">50,200</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">14,460</td>
<td align="right">13,200</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">29,760</td>
<td align="right">27,200</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">14,880</td>
<td align="right">13,600</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">3,720</td>
<td align="right">3,400</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">3,720</td>
<td align="right">3,400</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">32,120</td>
<td align="right">29,360</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">48,560</td>
<td align="right">44,400</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">29,960</td>
<td align="right">27,400</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">26,460</td>
<td align="right">24,200</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">19,020</td>
<td align="right">17,400</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">19,020</td>
<td align="right">17,400</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">222,140</td>
<td align="right">203,220</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">15,080</td>
<td align="right">13,800</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">11,340</td>
<td align="right">10,380</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">331,700</td>
<td align="right">303,620</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,580</td>
<td align="right">10,600</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">11,360</td>
<td align="right">10,400</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">929,460</td>
<td align="right">851,060</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">41,980</td>
<td align="right">38,440</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">49,580</td>
<td align="right">45,400</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">7,840</td>
<td align="right">7,180</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">7,860</td>
<td align="right">7,200</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">7,860</td>
<td align="right">7,200</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">34,300</td>
<td align="right">31,420</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">104,180</td>
<td align="right">95,440</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">7,640</td>
<td align="right">7,000</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">143,020</td>
<td align="right">131,060</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">225,280</td>
<td align="right">206,480</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">31,420</td>
<td align="right">28,800</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">82,040</td>
<td align="right">75,200</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">65,660</td>
<td align="right">60,200</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">16,680</td>
<td align="right">15,300</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">35,580</td>
<td align="right">32,640</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">98,980</td>
<td align="right">90,860</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">23,960</td>
<td align="right">22,000</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">8,080</td>
<td align="right">7,420</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">11,760</td>
<td align="right">10,800</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">11,760</td>
<td align="right">10,800</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">7,840</td>
<td align="right">7,200</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">7,840</td>
<td align="right">7,200</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3,920</td>
<td align="right">3,600</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3,920</td>
<td align="right">3,600</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3,920</td>
<td align="right">3,600</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">3,920</td>
<td align="right">3,600</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">3,920</td>
<td align="right">3,600</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">12,020</td>
<td align="right">11,040</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">27,680</td>
<td align="right">25,440</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">32,400</td>
<td align="right">29,800</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">8,500</td>
<td align="right">7,820</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">8,300</td>
<td align="right">7,640</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">15,980</td>
<td align="right">14,860</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">41,200</td>
<td align="right">38,440</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">24,220</td>
<td align="right">22,760</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">14,060</td>
<td align="right">13,240</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,020</td>
<td align="right">1,920</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">33,400</td>
<td align="right">32,280</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,860</td>
<td align="right">1,800</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">620</td>
<td align="right">600</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">39,100</td>
<td align="right">38,120</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">880</td>
<td align="right">860</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">31,200</td>
<td align="right">30,540</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">6,820</td>
<td align="right">6,920</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2,580</td>
<td align="right">2,560</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,280</td>
<td align="right">1,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">200</td>
<td align="right">200</td>
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
<td align="right">33,980</td>
<td align="right">68.0%</td>
<td align="right">30,980</td>
<td align="right">67.6%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,280</td>
<td align="right">26.6%</td>
<td align="right">12,340</td>
<td align="right">26.9%</td>
<td align="right">-7.1%</td>
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
<td align="right">1,480</td>
<td align="right">54.8%</td>
<td align="right">1,380</td>
<td align="right">54.8%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,220</td>
<td align="right">45.2%</td>
<td align="right">1,140</td>
<td align="right">45.2%</td>
<td align="right">-6.6%</td>
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
<td align="right">80</td>
<td align="right">5.4%</td>
<td align="right">100</td>
<td align="right">7.2%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">700</td>
<td align="right">47.3%</td>
<td align="right">640</td>
<td align="right">46.4%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">700</td>
<td align="right">47.3%</td>
<td align="right">640</td>
<td align="right">46.4%</td>
<td align="right">-8.6%</td>
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
<td align="right">7,840</td>
<td align="right">100.0%</td>
<td align="right">7,200</td>
<td align="right">100.0%</td>
<td align="right">-8.2%</td>
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
<td align="right">224,460</td>
<td align="right">87.8%</td>
<td align="right">204,540</td>
<td align="right">87.0%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">15,620</td>
<td align="right">6.1%</td>
<td align="right">16,060</td>
<td align="right">6.8%</td>
<td align="right">2.8%</td>
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
<td align="right">15,580</td>
<td align="right">100.0%</td>
<td align="right">14,480</td>
<td align="right">100.0%</td>
<td align="right">-7.1%</td>
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
<td align="right">880</td>
<td align="right">47.3%</td>
<td align="right">900</td>
<td align="right">50.0%</td>
<td align="right">2.3%</td>
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
<td align="right">980</td>
<td align="right">100.0%</td>
<td align="right">900</td>
<td align="right">100.0%</td>
<td align="right">-8.2%</td>
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
<td align="right">80,740</td>
<td align="right">82.0%</td>
<td align="right">73,400</td>
<td align="right">81.5%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,720</td>
<td align="right">3.8%</td>
<td align="right">3,400</td>
<td align="right">3.8%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,340</td>
<td align="right">8.5%</td>
<td align="right">8,000</td>
<td align="right">8.9%</td>
<td align="right">-4.1%</td>
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
<td align="right">700</td>
<td align="right">12.2%</td>
<td align="right">640</td>
<td align="right">12.2%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,020</td>
<td align="right">87.8%</td>
<td align="right">4,600</td>
<td align="right">87.8%</td>
<td align="right">-8.4%</td>
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
<td align="right">700</td>
<td align="right">100.0%</td>
<td align="right">640</td>
<td align="right">100.0%</td>
<td align="right">-8.6%</td>
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
<td align="right">440</td>
<td align="right">100.0%</td>
<td align="right">440</td>
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
<td align="right">11,800</td>
<td align="right">85.4%</td>
<td align="right">10,840</td>
<td align="right">85.0%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,080</td>
<td align="right">7.8%</td>
<td align="right">1,040</td>
<td align="right">8.2%</td>
<td align="right">-3.7%</td>
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
<td align="right">700</td>
<td align="right">74.5%</td>
<td align="right">640</td>
<td align="right">72.7%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">240</td>
<td align="right">25.5%</td>
<td align="right">240</td>
<td align="right">27.3%</td>
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
<td align="right">240</td>
<td align="right">100.0%</td>
<td align="right">240</td>
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
<td align="left">other</td>
<td align="right">220</td>
<td align="right">220 / 0 !!</td>
<td align="right">200</td>
<td align="right">200 / 0 !!</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">7,440</td>
<td align="right">7,440 / 0 !!</td>
<td align="right">6,800</td>
<td align="right">6,800 / 0 !!</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">640</td>
<td align="right">640 / 0 !!</td>
<td align="right">640</td>
<td align="right">640 / 0 !!</td>
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
<td align="right">300,380</td>
<td align="right">86.6%</td>
<td align="right">273,320</td>
<td align="right">85.9%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,440</td>
<td align="right">2.1%</td>
<td align="right">6,800</td>
<td align="right">2.1%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,280</td>
<td align="right">6.1%</td>
<td align="right">21,540</td>
<td align="right">6.8%</td>
<td align="right">1.2%</td>
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
<td align="right">17,080</td>
<td align="right">95.8%</td>
<td align="right">15,880</td>
<td align="right">95.8%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">740</td>
<td align="right">4.2%</td>
<td align="right">700</td>
<td align="right">4.2%</td>
<td align="right">-5.4%</td>
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
<td align="right">299,700</td>
<td align="right">88.0%</td>
<td align="right">272,860</td>
<td align="right">87.4%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,640</td>
<td align="right">2.2%</td>
<td align="right">7,000</td>
<td align="right">2.2%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">16,280</td>
<td align="right">4.8%</td>
<td align="right">16,420</td>
<td align="right">5.3%</td>
<td align="right">0.9%</td>
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
<td align="right">17,120</td>
<td align="right">100.0%</td>
<td align="right">15,860</td>
<td align="right">100.0%</td>
<td align="right">-7.4%</td>
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
<td align="right">86,020</td>
<td align="right">78.0%</td>
<td align="right">78,300</td>
<td align="right">77.5%</td>
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
<td align="right">16,420</td>
<td align="right">14.9%</td>
<td align="right">15,500</td>
<td align="right">15.3%</td>
<td align="right">-5.6%</td>
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
<td align="right">2,100</td>
<td align="right">26.9%</td>
<td align="right">1,940</td>
<td align="right">26.7%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,700</td>
<td align="right">73.1%</td>
<td align="right">5,320</td>
<td align="right">73.3%</td>
<td align="right">-6.7%</td>
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
<td align="left">not managed dict</td>
<td align="right">700</td>
<td align="right">33.3%</td>
<td align="right">640</td>
<td align="right">33.0%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,400</td>
<td align="right">66.7%</td>
<td align="right">1,300</td>
<td align="right">67.0%</td>
<td align="right">-7.1%</td>
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
<td align="right">200</td>
<td align="right">90.9%</td>
<td align="right">180</td>
<td align="right">81.8%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">9.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">129,120</td>
<td align="right">74.2%</td>
<td align="right">117,500</td>
<td align="right">73.7%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,720</td>
<td align="right">2.1%</td>
<td align="right">3,400</td>
<td align="right">2.1%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">29,980</td>
<td align="right">17.2%</td>
<td align="right">28,120</td>
<td align="right">17.6%</td>
<td align="right">-6.2%</td>
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
<td align="right">7,460</td>
<td align="right">66.5%</td>
<td align="right">6,860</td>
<td align="right">66.5%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,760</td>
<td align="right">33.5%</td>
<td align="right">3,460</td>
<td align="right">33.5%</td>
<td align="right">-8.0%</td>
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
<td align="left">bytes</td>
<td align="right">1,400</td>
<td align="right">37.2%</td>
<td align="right">1,280</td>
<td align="right">37.0%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">700</td>
<td align="right">18.6%</td>
<td align="right">640</td>
<td align="right">18.5%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">700</td>
<td align="right">18.6%</td>
<td align="right">640</td>
<td align="right">18.5%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">920</td>
<td align="right">24.5%</td>
<td align="right">860</td>
<td align="right">24.9%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right">40</td>
<td align="right">1.2%</td>
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
<td align="right">18,920</td>
<td align="right">88.0%</td>
<td align="right">17,220</td>
<td align="right">87.1%</td>
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
<td align="right">1,320</td>
<td align="right">6.1%</td>
<td align="right">1,380</td>
<td align="right">7.0%</td>
<td align="right">4.5%</td>
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
<td align="right">1,260</td>
<td align="right">100.0%</td>
<td align="right">1,180</td>
<td align="right">100.0%</td>
<td align="right">-6.3%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,411,140</td>
<td align="right">31.3%</td>
<td align="right">1,284,920</td>
<td align="right">31.1%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">22,520</td>
<td align="right">0.5%</td>
<td align="right">20,600</td>
<td align="right">0.5%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,859,060</td>
<td align="right">63.3%</td>
<td align="right">2,619,300</td>
<td align="right">63.3%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">222,220</td>
<td align="right">4.9%</td>
<td align="right">211,840</td>
<td align="right">5.1%</td>
<td align="right">-4.7%</td>
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
<td align="right">7,840</td>
<td align="right">5.9%</td>
<td align="right">7,200</td>
<td align="right">5.6%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">13,280</td>
<td align="right">10.0%</td>
<td align="right">12,340</td>
<td align="right">9.6%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">29,980</td>
<td align="right">22.6%</td>
<td align="right">28,120</td>
<td align="right">21.8%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,420</td>
<td align="right">12.4%</td>
<td align="right">15,500</td>
<td align="right">12.0%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,320</td>
<td align="right">1.0%</td>
<td align="right">1,380</td>
<td align="right">1.1%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">8,340</td>
<td align="right">6.3%</td>
<td align="right">8,000</td>
<td align="right">6.2%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,080</td>
<td align="right">0.8%</td>
<td align="right">1,040</td>
<td align="right">0.8%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">15,620</td>
<td align="right">11.8%</td>
<td align="right">16,060</td>
<td align="right">12.5%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">21,280</td>
<td align="right">16.0%</td>
<td align="right">21,540</td>
<td align="right">16.7%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">16,280</td>
<td align="right">12.3%</td>
<td align="right">16,420</td>
<td align="right">12.7%</td>
<td align="right">0.9%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">7,440</td>
<td align="right">33.0%</td>
<td align="right">6,800</td>
<td align="right">33.0%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">3,720</td>
<td align="right">16.5%</td>
<td align="right">3,400</td>
<td align="right">16.5%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">3,720</td>
<td align="right">16.5%</td>
<td align="right">3,400</td>
<td align="right">16.5%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,640</td>
<td align="right">33.9%</td>
<td align="right">7,000</td>
<td align="right">34.0%</td>
<td align="right">-8.4%</td>
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
<td align="right"></td>
<td align="right"></td>
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
<td align="left">CHECK_EXC_MATCH</td>
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
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">11,360</td>
<td align="right">7.5%</td>
<td align="right">10,400</td>
<td align="right">7.5%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">122,760</td>
<td align="right">81.4%</td>
<td align="right">112,420</td>
<td align="right">81.3%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">143,020</td>
<td align="right">94.8%</td>
<td align="right">131,060</td>
<td align="right">94.8%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">7,840</td>
<td align="right">5.2%</td>
<td align="right">7,200</td>
<td align="right">5.2%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">3,920</td>
<td align="right">2.6%</td>
<td align="right">3,600</td>
<td align="right">2.6%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">3,920</td>
<td align="right">2.6%</td>
<td align="right">3,600</td>
<td align="right">2.6%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">28,100</td>
<td align="right">18.6%</td>
<td align="right">25,840</td>
<td align="right">18.7%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">28,100</td>
<td align="right">18.6%</td>
<td align="right">25,840</td>
<td align="right">18.7%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">20,260</td>
<td align="right">13.4%</td>
<td align="right">18,640</td>
<td align="right">13.5%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">20,260</td>
<td align="right">13.4%</td>
<td align="right">18,640</td>
<td align="right">13.5%</td>
<td align="right">-8.0%</td>
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
<td align="left">Interpreter mortal increfs</td>
<td align="right">806,440</td>
<td align="right">40.1%</td>
<td align="right">736,580</td>
<td align="right">39.7%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">115,280</td>
<td align="right">5.7%</td>
<td align="right">105,340</td>
<td align="right">5.7%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">3,720</td>
<td align="right">0.9%</td>
<td align="right">3,400</td>
<td align="right">0.9%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">78,735</td>
<td align="right"></td>
<td align="right">72,117</td>
<td align="right"></td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">11,560</td>
<td align="right"></td>
<td align="right">10,600</td>
<td align="right"></td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,095,480</td>
<td align="right">46.6%</td>
<td align="right">1,004,541</td>
<td align="right">46.4%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">212,640</td>
<td align="right"></td>
<td align="right">195,261</td>
<td align="right"></td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">209,180</td>
<td align="right">51.7%</td>
<td align="right">192,121</td>
<td align="right">51.7%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">194,349</td>
<td align="right"></td>
<td align="right">178,663</td>
<td align="right"></td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">195,200</td>
<td align="right">48.3%</td>
<td align="right">179,480</td>
<td align="right">48.3%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">187,360</td>
<td align="right">46.3%</td>
<td align="right">172,280</td>
<td align="right">46.4%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">4,120</td>
<td align="right">1.0%</td>
<td align="right">3,800</td>
<td align="right">1.0%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">671,727</td>
<td align="right">28.6%</td>
<td align="right">619,660</td>
<td align="right">28.6%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">38,640</td>
<td align="right">1.6%</td>
<td align="right">35,700</td>
<td align="right">1.7%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">543,131</td>
<td align="right">23.1%</td>
<td align="right">503,240</td>
<td align="right">23.3%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">599,578</td>
<td align="right">29.8%</td>
<td align="right">555,684</td>
<td align="right">30.0%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">489,874</td>
<td align="right">24.4%</td>
<td align="right">456,777</td>
<td align="right">24.6%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">84,589</td>
<td align="right"></td>
<td align="right">79,748</td>
<td align="right"></td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">4,005</td>
<td align="right"></td>
<td align="right">3,843</td>
<td align="right"></td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">12,667</td>
<td align="right"></td>
<td align="right">12,666</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">14,011</td>
<td align="right"></td>
<td align="right">14,012</td>
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
<td align="right">240</td>
<td align="right">220</td>
<td align="right">-8.3%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-26
