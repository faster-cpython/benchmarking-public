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
<td align="left">CALL_TUPLE_1</td>
<td align="right">223,920</td>
<td align="right">5,780</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">448,960</td>
<td align="right">15,200</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,111,200</td>
<td align="right">73,580</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">226,040</td>
<td align="right">9,180</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">708,480</td>
<td align="right">44,520</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">7,317,420</td>
<td align="right">877,400</td>
<td align="right">-88.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,662,780</td>
<td align="right">205,760</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">79,840</td>
<td align="right">10,860</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">46,240</td>
<td align="right">6,340</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,854,040</td>
<td align="right">597,940</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">336,480</td>
<td align="right">70,540</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">59,420</td>
<td align="right">106,100</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,304,800</td>
<td align="right">285,000</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,131,580</td>
<td align="right">265,920</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,124,580</td>
<td align="right">524,260</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">461,700</td>
<td align="right">117,680</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">465,100</td>
<td align="right">124,940</td>
<td align="right">-73.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,528,520</td>
<td align="right">1,260,860</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,314,500</td>
<td align="right">1,092,020</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,321,720</td>
<td align="right">437,260</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">9,577,400</td>
<td align="right">3,205,800</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,185,040</td>
<td align="right">2,763,100</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">32,960</td>
<td align="right">54,480</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">9,654,540</td>
<td align="right">3,365,260</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,280,180</td>
<td align="right">800,520</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">24,198,980</td>
<td align="right">8,509,780</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">29,394,120</td>
<td align="right">10,476,520</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">553,660</td>
<td align="right">198,240</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">216,040</td>
<td align="right">77,620</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">18,317,420</td>
<td align="right">6,778,160</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,977,200</td>
<td align="right">732,320</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">16,911,160</td>
<td align="right">6,308,560</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,804,980</td>
<td align="right">2,177,640</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,864,300</td>
<td align="right">711,780</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">702,380</td>
<td align="right">283,480</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,671,500</td>
<td align="right">688,340</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,833,640</td>
<td align="right">2,053,020</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,440,960</td>
<td align="right">640,520</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,087,320</td>
<td align="right">938,900</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">5,040</td>
<td align="right">7,800</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">5,040</td>
<td align="right">7,800</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">5,040</td>
<td align="right">7,800</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">53,660</td>
<td align="right">25,260</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,071,900</td>
<td align="right">512,360</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,387,620</td>
<td align="right">1,141,900</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">8,989,720</td>
<td align="right">4,494,040</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,439,920</td>
<td align="right">2,223,400</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,905,180</td>
<td align="right">1,496,640</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">31,172,080</td>
<td align="right">16,484,080</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">11,018,080</td>
<td align="right">5,863,360</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">41,570,980</td>
<td align="right">22,540,620</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">6,080</td>
<td align="right">8,840</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,650,380</td>
<td align="right">1,452,600</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">118,870,280</td>
<td align="right">65,624,240</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">2,194,500</td>
<td align="right">1,267,240</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">28,437,860</td>
<td align="right">16,443,020</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">18,299,260</td>
<td align="right">10,652,700</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">16,530,140</td>
<td align="right">9,741,980</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">7,684,920</td>
<td align="right">4,553,860</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,456,220</td>
<td align="right">897,320</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">664,480</td>
<td align="right">431,660</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">293,680</td>
<td align="right">193,200</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,858,980</td>
<td align="right">3,208,400</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">8,871,160</td>
<td align="right">6,044,360</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">4,387,640</td>
<td align="right">3,062,440</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">23,290,540</td>
<td align="right">16,257,820</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">16,429,860</td>
<td align="right">11,602,440</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">790,760</td>
<td align="right">565,420</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">216,780</td>
<td align="right">157,660</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">18,550,320</td>
<td align="right">13,576,380</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">636,280</td>
<td align="right">468,680</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">565,900</td>
<td align="right">421,680</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">973,620</td>
<td align="right">726,900</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,299,400</td>
<td align="right">4,078,500</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">4,493,060</td>
<td align="right">3,482,100</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">276,780</td>
<td align="right">221,840</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,305,420</td>
<td align="right">3,548,140</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">962,440</td>
<td align="right">801,160</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,604,520</td>
<td align="right">5,597,520</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">24,000</td>
<td align="right">27,560</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">443,720</td>
<td align="right">378,020</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,015,260</td>
<td align="right">1,726,900</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,372,600</td>
<td align="right">2,065,060</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">5,161,120</td>
<td align="right">4,663,460</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,912,020</td>
<td align="right">1,747,640</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">93,000</td>
<td align="right">100,760</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">11,480</td>
<td align="right">12,120</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">295,600</td>
<td align="right">288,940</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">149,820</td>
<td align="right">148,900</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">7,953,660</td>
<td align="right">7,993,280</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">154,980</td>
<td align="right">155,700</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">230,960</td>
<td align="right">231,700</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">450,360</td>
<td align="right">449,100</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">6,657,440</td>
<td align="right">6,657,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,946,880</td>
<td align="right">1,946,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">671,760</td>
<td align="right">671,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">572,120</td>
<td align="right">572,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">566,480</td>
<td align="right">566,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">566,480</td>
<td align="right">566,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">566,480</td>
<td align="right">566,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">448,880</td>
<td align="right">448,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">52,420</td>
<td align="right">52,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">3,800</td>
<td align="right">3,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
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
<td align="left">COPY_FREE_VARS</td>
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
<td align="left">RESUME</td>
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
<td align="right">4,829,220</td>
<td align="right">19.8%</td>
<td align="right">2,049,540</td>
<td align="right">9.5%</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">19,568,780</td>
<td align="right">80.2%</td>
<td align="right">19,568,780</td>
<td align="right">90.5%</td>
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
<td align="right">4,400</td>
<td align="right">99.5%</td>
<td align="right">3,460</td>
<td align="right">99.4%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">0.5%</td>
<td align="right">20</td>
<td align="right">0.6%</td>
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
<td align="left">and different types</td>
<td align="right">100</td>
<td align="right">2.3%</td>
<td align="right">20</td>
<td align="right">0.6%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">260</td>
<td align="right">5.9%</td>
<td align="right">140</td>
<td align="right">4.0%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">780</td>
<td align="right">17.7%</td>
<td align="right">580</td>
<td align="right">16.8%</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2,700</td>
<td align="right">61.4%</td>
<td align="right">2,160</td>
<td align="right">62.4%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">360</td>
<td align="right">8.2%</td>
<td align="right">360</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">100</td>
<td align="right">2.3%</td>
<td align="right">100</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">100</td>
<td align="right">2.3%</td>
<td align="right">100</td>
<td align="right">2.9%</td>
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
<td align="right">216,040</td>
<td align="right">100.0%</td>
<td align="right">77,620</td>
<td align="right">100.0%</td>
<td align="right">-64.1%</td>
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
<td align="right">154,760</td>
<td align="right">0.5%</td>
<td align="right">155,480</td>
<td align="right">0.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">27,746,400</td>
<td align="right">94.3%</td>
<td align="right">27,746,400</td>
<td align="right">94.3%</td>
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
<td align="right">1,509,180</td>
<td align="right">5.1%</td>
<td align="right">1,509,180</td>
<td align="right">5.1%</td>
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
<td align="right">28,460</td>
<td align="right">99.2%</td>
<td align="right">28,460</td>
<td align="right">99.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">220</td>
<td align="right">0.8%</td>
<td align="right">220</td>
<td align="right">0.8%</td>
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
<td align="right">80</td>
<td align="right">36.4%</td>
<td align="right">80</td>
<td align="right">36.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">27.3%</td>
<td align="right">60</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">60</td>
<td align="right">27.3%</td>
<td align="right">60</td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">20</td>
<td align="right">9.1%</td>
<td align="right">20</td>
<td align="right">9.1%</td>
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
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">180</td>
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
<td align="right">96,241,640</td>
<td align="right">99.9%</td>
<td align="right">96,241,640</td>
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
<td align="right">52,420</td>
<td align="right">0.1%</td>
<td align="right">52,420</td>
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
<td align="right">1,220</td>
<td align="right">100.0%</td>
<td align="right">1,220</td>
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
<td align="right">1,124,180</td>
<td align="right">6.5%</td>
<td align="right">259,020</td>
<td align="right">1.6%</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">170,160</td>
<td align="right">1.0%</td>
<td align="right">167,500</td>
<td align="right">1.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,085,980</td>
<td align="right">92.5%</td>
<td align="right">16,085,780</td>
<td align="right">97.4%</td>
<td align="right">-0.0%</td>
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
<td align="right">7,400</td>
<td align="right">69.8%</td>
<td align="right">6,900</td>
<td align="right">68.6%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,200</td>
<td align="right">30.2%</td>
<td align="right">3,160</td>
<td align="right">31.4%</td>
<td align="right">-1.2%</td>
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
<td align="right">200</td>
<td align="right">2.7%</td>
<td align="right">80</td>
<td align="right">1.2%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">260</td>
<td align="right">3.5%</td>
<td align="right">140</td>
<td align="right">2.0%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">220</td>
<td align="right">3.0%</td>
<td align="right">140</td>
<td align="right">2.0%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">140</td>
<td align="right">1.9%</td>
<td align="right">100</td>
<td align="right">1.4%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">6,580</td>
<td align="right">88.9%</td>
<td align="right">6,440</td>
<td align="right">93.3%</td>
<td align="right">-2.1%</td>
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
<td align="right">2,904,100</td>
<td align="right">19.2%</td>
<td align="right">1,495,920</td>
<td align="right">10.9%</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,221,840</td>
<td align="right">80.8%</td>
<td align="right">12,221,840</td>
<td align="right">89.1%</td>
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
<td align="right">1,080</td>
<td align="right">100.0%</td>
<td align="right">720</td>
<td align="right">100.0%</td>
<td align="right">-33.3%</td>
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
<td align="right">1,020</td>
<td align="right">94.4%</td>
<td align="right">660</td>
<td align="right">91.7%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">60</td>
<td align="right">5.6%</td>
<td align="right">60</td>
<td align="right">8.3%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">31,540</td>
<td align="right">1.3%</td>
<td align="right">1,860</td>
<td align="right">0.2%</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">460,080</td>
<td align="right">19.6%</td>
<td align="right">117,200</td>
<td align="right">10.2%</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,857,160</td>
<td align="right">79.0%</td>
<td align="right">1,028,020</td>
<td align="right">89.6%</td>
<td align="right">-44.6%</td>
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
<td align="right">620</td>
<td align="right">27.9%</td>
<td align="right">60</td>
<td align="right">11.5%</td>
<td align="right">-90.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,600</td>
<td align="right">72.1%</td>
<td align="right">460</td>
<td align="right">88.5%</td>
<td align="right">-71.2%</td>
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
<td align="right">100</td>
<td align="right">6.2%</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,380</td>
<td align="right">86.2%</td>
<td align="right">360</td>
<td align="right">78.3%</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">100</td>
<td align="right">6.2%</td>
<td align="right">60</td>
<td align="right">13.0%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">20</td>
<td align="right">1.2%</td>
<td align="right">20</td>
<td align="right">4.3%</td>
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
<td align="right">6,596,520</td>
<td align="right">8.8%</td>
<td align="right">5,589,880</td>
<td align="right">7.6%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">68,273,500</td>
<td align="right">91.2%</td>
<td align="right">68,026,780</td>
<td align="right">92.4%</td>
<td align="right">-0.4%</td>
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
<td align="right">2,780</td>
<td align="right">34.8%</td>
<td align="right">2,440</td>
<td align="right">31.9%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,220</td>
<td align="right">65.2%</td>
<td align="right">5,200</td>
<td align="right">68.1%</td>
<td align="right">-0.4%</td>
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
<td align="left">builtin class method</td>
<td align="right">80</td>
<td align="right">2.9%</td>
<td align="right">60</td>
<td align="right">2.5%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,060</td>
<td align="right">74.1%</td>
<td align="right">1,740</td>
<td align="right">71.3%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">300</td>
<td align="right">10.8%</td>
<td align="right">300</td>
<td align="right">12.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">200</td>
<td align="right">7.2%</td>
<td align="right">200</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">120</td>
<td align="right">4.3%</td>
<td align="right">120</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">20</td>
<td align="right">0.7%</td>
<td align="right">20</td>
<td align="right">0.8%</td>
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
<td align="right">45,823,980</td>
<td align="right">100.0%</td>
<td align="right">22,078,960</td>
<td align="right">100.0%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">180</td>
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
<td align="right">19,073,120</td>
<td align="right">100.0%</td>
<td align="right">19,073,120</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>

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
<td align="right">46,240</td>
<td align="right">100.0%</td>
<td align="right">6,340</td>
<td align="right">100.0%</td>
<td align="right">-86.3%</td>
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
<td align="right">443,080</td>
<td align="right">12.1%</td>
<td align="right">377,420</td>
<td align="right">10.5%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,216,080</td>
<td align="right">87.9%</td>
<td align="right">3,216,080</td>
<td align="right">89.5%</td>
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
<td align="right">640</td>
<td align="right">100.0%</td>
<td align="right">600</td>
<td align="right">100.0%</td>
<td align="right">-6.2%</td>
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
<td align="left">py simple</td>
<td align="right">160</td>
<td align="right">25.0%</td>
<td align="right">140</td>
<td align="right">23.3%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">380</td>
<td align="right">59.4%</td>
<td align="right">360</td>
<td align="right">60.0%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">80</td>
<td align="right">12.5%</td>
<td align="right">80</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">20</td>
<td align="right">3.1%</td>
<td align="right">20</td>
<td align="right">3.3%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,069,200</td>
<td align="right">2.9%</td>
<td align="right">510,360</td>
<td align="right">1.4%</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">90,040</td>
<td align="right">0.2%</td>
<td align="right">44,560</td>
<td align="right">0.1%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,310,380</td>
<td align="right">96.9%</td>
<td align="right">35,744,620</td>
<td align="right">98.5%</td>
<td align="right">-1.6%</td>
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
<td align="right">1,700</td>
<td align="right">38.6%</td>
<td align="right">820</td>
<td align="right">28.9%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,700</td>
<td align="right">61.4%</td>
<td align="right">2,020</td>
<td align="right">71.1%</td>
<td align="right">-25.2%</td>
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
<td align="left">number</td>
<td align="right">100</td>
<td align="right">3.7%</td>
<td align="right">20</td>
<td align="right">1.0%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,040</td>
<td align="right">38.5%</td>
<td align="right">600</td>
<td align="right">29.7%</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">460</td>
<td align="right">17.0%</td>
<td align="right">380</td>
<td align="right">18.8%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">800</td>
<td align="right">29.6%</td>
<td align="right">680</td>
<td align="right">33.7%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">300</td>
<td align="right">11.1%</td>
<td align="right">340</td>
<td align="right">16.8%</td>
<td align="right">13.3%</td>
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
<td align="right">16,319,340</td>
<td align="right">100.0%</td>
<td align="right">10,434,300</td>
<td align="right">100.0%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">385,118,460</td>
<td align="right">63.6%</td>
<td align="right">202,718,900</td>
<td align="right">61.6%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">201,137,180</td>
<td align="right">33.2%</td>
<td align="right">113,675,480</td>
<td align="right">34.6%</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">17,870,400</td>
<td align="right">2.9%</td>
<td align="right">10,661,720</td>
<td align="right">3.2%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,853,560</td>
<td align="right">0.3%</td>
<td align="right">1,775,780</td>
<td align="right">0.5%</td>
<td align="right">-4.2%</td>
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
<td align="left">STORE_SLICE</td>
<td align="right">46,240</td>
<td align="right">0.3%</td>
<td align="right">6,340</td>
<td align="right">0.1%</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,124,180</td>
<td align="right">6.3%</td>
<td align="right">259,020</td>
<td align="right">2.4%</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">460,080</td>
<td align="right">2.6%</td>
<td align="right">117,200</td>
<td align="right">1.1%</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">216,040</td>
<td align="right">1.2%</td>
<td align="right">77,620</td>
<td align="right">0.7%</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,829,220</td>
<td align="right">27.1%</td>
<td align="right">2,049,540</td>
<td align="right">19.3%</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,069,200</td>
<td align="right">6.0%</td>
<td align="right">510,360</td>
<td align="right">4.8%</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,904,100</td>
<td align="right">16.3%</td>
<td align="right">1,495,920</td>
<td align="right">14.1%</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,596,520</td>
<td align="right">37.0%</td>
<td align="right">5,589,880</td>
<td align="right">52.5%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">443,080</td>
<td align="right">2.5%</td>
<td align="right">377,420</td>
<td align="right">3.5%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">154,760</td>
<td align="right">0.9%</td>
<td align="right">155,480</td>
<td align="right">1.5%</td>
<td align="right">0.5%</td>
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
<td align="right">31,540</td>
<td align="right">1.7%</td>
<td align="right">1,860</td>
<td align="right">0.1%</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">25,440</td>
<td align="right">1.4%</td>
<td align="right">9,540</td>
<td align="right">0.5%</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">8,160</td>
<td align="right">0.4%</td>
<td align="right">4,100</td>
<td align="right">0.2%</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">56,440</td>
<td align="right">3.0%</td>
<td align="right">30,920</td>
<td align="right">1.7%</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">170,160</td>
<td align="right">9.2%</td>
<td align="right">167,500</td>
<td align="right">9.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,276,900</td>
<td align="right">68.9%</td>
<td align="right">1,276,900</td>
<td align="right">71.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">232,280</td>
<td align="right">12.5%</td>
<td align="right">232,280</td>
<td align="right">13.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">52,420</td>
<td align="right">2.8%</td>
<td align="right">52,420</td>
<td align="right">3.0%</td>
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
<td align="right">7,910,240</td>
<td align="right">19.0%</td>
<td align="right">7,910,240</td>
<td align="right">19.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">33,814,880</td>
<td align="right">81.0%</td>
<td align="right">33,814,880</td>
<td align="right">81.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,910,240</td>
<td align="right">19.0%</td>
<td align="right">7,910,240</td>
<td align="right">19.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,910,240</td>
<td align="right">19.0%</td>
<td align="right">7,910,240</td>
<td align="right">19.0%</td>
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
<td align="right">7,910,240</td>
<td align="right">19.0%</td>
<td align="right">7,910,240</td>
<td align="right">19.0%</td>
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
<td align="right">7,649,360</td>
<td align="right">18.3%</td>
<td align="right">7,649,360</td>
<td align="right">18.3%</td>
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
<td align="right">3,072,080</td>
<td align="right">7.4%</td>
<td align="right">3,072,080</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">43,672,000</td>
<td align="right">104.7%</td>
<td align="right">43,672,000</td>
<td align="right">104.7%</td>
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
<td align="left">Interpreter immortal increfs</td>
<td align="right">127,539,780</td>
<td align="right">11.7%</td>
<td align="right">71,446,000</td>
<td align="right">6.6%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">250,914,200</td>
<td align="right">22.9%</td>
<td align="right">153,755,720</td>
<td align="right">14.1%</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">173,795,020</td>
<td align="right">13.4%</td>
<td align="right">114,376,420</td>
<td align="right">8.8%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">472,633,052</td>
<td align="right">43.2%</td>
<td align="right">578,715,826</td>
<td align="right">53.1%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">338,656,400</td>
<td align="right">26.1%</td>
<td align="right">265,358,000</td>
<td align="right">20.3%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">457,746,081</td>
<td align="right">35.3%</td>
<td align="right">545,860,274</td>
<td align="right">41.8%</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">243,067,432</td>
<td align="right">22.2%</td>
<td align="right">285,164,208</td>
<td align="right">26.2%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">325,698,983</td>
<td align="right">25.1%</td>
<td align="right">378,900,640</td>
<td align="right">29.0%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">56,200</td>
<td align="right">0.1%</td>
<td align="right">63,680</td>
<td align="right">0.1%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">80</td>
<td align="right"></td>
<td align="right">71</td>
<td align="right"></td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">56,680,020</td>
<td align="right">75.7%</td>
<td align="right">62,573,580</td>
<td align="right">77.5%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">56,621,740</td>
<td align="right">75.6%</td>
<td align="right">62,507,720</td>
<td align="right">77.4%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">59,423,669</td>
<td align="right"></td>
<td align="right">65,315,945</td>
<td align="right"></td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">2,080</td>
<td align="right">0.0%</td>
<td align="right">2,180</td>
<td align="right">0.0%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,153</td>
<td align="right"></td>
<td align="right">2,129</td>
<td align="right"></td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,092</td>
<td align="right"></td>
<td align="right">2,086</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">9,368,600</td>
<td align="right"></td>
<td align="right">9,368,229</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">18,212,640</td>
<td align="right">24.3%</td>
<td align="right">18,212,760</td>
<td align="right">22.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">18,221,620</td>
<td align="right"></td>
<td align="right">18,221,740</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">19,044,748</td>
<td align="right"></td>
<td align="right">19,044,734</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,946,880</td>
<td align="right"></td>
<td align="right">1,946,880</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">360</td>
<td align="right">1.2%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">15,080</td>
<td align="right">47.9%</td>
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
<td align="right">11,380</td>
<td align="right">36.1%</td>
<td align="right">1,360</td>
<td align="right">4.5%</td>
<td align="right">-88.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">900</td>
<td align="right">2.9%</td>
<td align="right">1,600</td>
<td align="right">5.3%</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">20,100</td>
<td align="right">63.9%</td>
<td align="right">28,620</td>
<td align="right">95.5%</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,779,139,300</td>
<td align="right">3,270.5%</td>
<td align="right">2,238,940,600</td>
<td align="right">3,428.8%</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">3,960</td>
<td align="right">12.6%</td>
<td align="right">3,020</td>
<td align="right">10.1%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">54,399,000</td>
<td align="right"></td>
<td align="right">65,298,720</td>
<td align="right"></td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">31,480</td>
<td align="right"></td>
<td align="right">29,980</td>
<td align="right"></td>
<td align="right">-4.8%</td>
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
<td align="right">20,100</td>
<td align="right"></td>
<td align="right">28,620</td>
<td align="right"></td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">20,100</td>
<td align="right">100.0%</td>
<td align="right">28,620</td>
<td align="right">100.0%</td>
<td align="right">42.4%</td>
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
<td align="right">1,820</td>
<td align="right">9.1%</td>
<td align="right">1,240</td>
<td align="right">4.3%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">800</td>
<td align="right">4.0%</td>
<td align="right">1,820</td>
<td align="right">6.4%</td>
<td align="right">127.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">4,120</td>
<td align="right">20.5%</td>
<td align="right">5,960</td>
<td align="right">20.8%</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">6,700</td>
<td align="right">33.3%</td>
<td align="right">9,260</td>
<td align="right">32.4%</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,940</td>
<td align="right">19.6%</td>
<td align="right">7,920</td>
<td align="right">27.7%</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,720</td>
<td align="right">13.5%</td>
<td align="right">2,320</td>
<td align="right">8.1%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">100</td>
<td align="right">0.3%</td>
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
<td align="right">440</td>
<td align="right">2.2%</td>
<td align="right">160</td>
<td align="right">0.6%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,780</td>
<td align="right">8.9%</td>
<td align="right">1,840</td>
<td align="right">6.4%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">2,440</td>
<td align="right">12.1%</td>
<td align="right">3,920</td>
<td align="right">13.7%</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,040</td>
<td align="right">35.0%</td>
<td align="right">9,920</td>
<td align="right">34.7%</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">4,820</td>
<td align="right">24.0%</td>
<td align="right">7,320</td>
<td align="right">25.6%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,100</td>
<td align="right">15.4%</td>
<td align="right">4,980</td>
<td align="right">17.4%</td>
<td align="right">60.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">480</td>
<td align="right">2.4%</td>
<td align="right">480</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
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
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">2,400</td>
<td align="right">436,160</td>
<td align="right">18,073.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">97,140</td>
<td align="right">525,180</td>
<td align="right">440.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,482,400</td>
<td align="right">25,307,680</td>
<td align="right">361.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">299,740</td>
<td align="right">1,227,000</td>
<td align="right">309.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">7,202,140</td>
<td align="right">28,046,060</td>
<td align="right">289.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">108,560</td>
<td align="right">374,500</td>
<td align="right">245.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,572,720</td>
<td align="right">3,845,260</td>
<td align="right">144.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">133,620</td>
<td align="right">322,860</td>
<td align="right">141.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,681,560</td>
<td align="right">3,937,660</td>
<td align="right">134.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,101,940</td>
<td align="right">2,558,960</td>
<td align="right">132.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,866,020</td>
<td align="right">4,305,200</td>
<td align="right">130.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">126,320</td>
<td align="right">286,340</td>
<td align="right">126.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">3,691,720</td>
<td align="right">8,187,400</td>
<td align="right">121.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,079,400</td>
<td align="right">11,205,100</td>
<td align="right">120.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">922,180</td>
<td align="right">1,885,480</td>
<td align="right">104.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,164,660</td>
<td align="right">4,309,880</td>
<td align="right">99.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,823,100</td>
<td align="right">3,621,740</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">704,320</td>
<td align="right">1,371,320</td>
<td align="right">94.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">2,296,240</td>
<td align="right">4,407,120</td>
<td align="right">91.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,051,680</td>
<td align="right">2,009,060</td>
<td align="right">91.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">2,127,740</td>
<td align="right">3,728,060</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,332,980</td>
<td align="right">2,316,140</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,799,120</td>
<td align="right">4,836,740</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,861,120</td>
<td align="right">3,106,000</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,088,780</td>
<td align="right">1,810,500</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,189,300</td>
<td align="right">5,279,900</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,421,060</td>
<td align="right">5,643,540</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,788,920</td>
<td align="right">2,937,340</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">10,288,600</td>
<td align="right">16,660,200</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">18,223,400</td>
<td align="right">28,826,000</td>
<td align="right">58.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">22,686,600</td>
<td align="right">35,757,220</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">5,566,740</td>
<td align="right">8,694,940</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">138,800</td>
<td align="right">214,980</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,416,780</td>
<td align="right">2,186,980</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">4,095,600</td>
<td align="right">6,312,120</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">9,985,140</td>
<td align="right">15,194,280</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">12,892,660</td>
<td align="right">19,181,940</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,029,900</td>
<td align="right">7,383,680</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">6,451,140</td>
<td align="right">9,433,080</td>
<td align="right">46.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">6,057,280</td>
<td align="right">8,836,960</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">11,682,440</td>
<td align="right">16,958,400</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">26,180</td>
<td align="right">38,000</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">5,358,120</td>
<td align="right">7,769,520</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">31,449,280</td>
<td align="right">45,446,320</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">8,291,580</td>
<td align="right">11,918,920</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">11,844,860</td>
<td align="right">16,992,860</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">583,280</td>
<td align="right">816,100</td>
<td align="right">39.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">11,687,260</td>
<td align="right">16,164,640</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">11,663,500</td>
<td align="right">16,091,560</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">11,844,860</td>
<td align="right">16,328,900</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,372,140</td>
<td align="right">6,022,720</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,372,140</td>
<td align="right">6,022,720</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,712,740</td>
<td align="right">3,719,380</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">39,121,360</td>
<td align="right">53,508,080</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">18,771,820</td>
<td align="right">25,294,300</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,820,700</td>
<td align="right">5,066,420</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">27,345,020</td>
<td align="right">36,208,440</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">17,327,260</td>
<td align="right">22,861,880</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">45,692,840</td>
<td align="right">59,272,560</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,586,360</td>
<td align="right">3,296,700</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">6,132,900</td>
<td align="right">7,776,580</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">23,850,140</td>
<td align="right">30,212,780</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">72,607,080</td>
<td align="right">91,924,300</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">25,977,160</td>
<td align="right">32,877,240</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">26,865,940</td>
<td align="right">33,898,660</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">26,865,940</td>
<td align="right">33,898,660</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">114,126,740</td>
<td align="right">143,519,540</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">5,142,560</td>
<td align="right">6,461,760</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">5,626,380</td>
<td align="right">7,034,560</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">11,481,280</td>
<td align="right">14,322,220</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">50,439,660</td>
<td align="right">62,713,500</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">80,239,780</td>
<td align="right">99,708,240</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">8,012,400</td>
<td align="right">9,910,480</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">54,986,400</td>
<td align="right">67,408,140</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">637,240</td>
<td align="right">775,660</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,023,420</td>
<td align="right">1,240,280</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">161,351,880</td>
<td align="right">195,498,660</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">54,399,000</td>
<td align="right">65,298,720</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">40,806,440</td>
<td align="right">48,954,020</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">3,826,500</td>
<td align="right">4,583,780</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">3,826,500</td>
<td align="right">4,583,780</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,826,500</td>
<td align="right">4,583,780</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">824,280</td>
<td align="right">985,580</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">3,854,220</td>
<td align="right">4,606,700</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">47,183,420</td>
<td align="right">38,251,940</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">773,540</td>
<td align="right">917,760</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,689,340</td>
<td align="right">2,004,140</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">129,840</td>
<td align="right">108,320</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">129,840</td>
<td align="right">108,320</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">984,440</td>
<td align="right">1,145,720</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">984,440</td>
<td align="right">1,145,720</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">83,090,860</td>
<td align="right">95,291,660</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">65,832,520</td>
<td align="right">75,093,560</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">9,245,740</td>
<td align="right">10,305,940</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">9,015,760</td>
<td align="right">10,031,640</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">1,601,400</td>
<td align="right">1,769,000</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">9,802,060</td>
<td align="right">10,813,020</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">27,760</td>
<td align="right">25,000</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">27,760</td>
<td align="right">25,000</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">27,760</td>
<td align="right">25,000</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">6,647,320</td>
<td align="right">7,303,780</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">31,397,120</td>
<td align="right">34,391,180</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">8,890,880</td>
<td align="right">9,677,420</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,403,200</td>
<td align="right">9,109,100</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,440,440</td>
<td align="right">4,804,980</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">347,720</td>
<td align="right">376,120</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">347,720</td>
<td align="right">376,120</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">11,224,820</td>
<td align="right">12,003,040</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">11,653,460</td>
<td align="right">12,350,460</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">9,837,140</td>
<td align="right">10,396,040</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">869,060</td>
<td align="right">822,380</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">4,497,960</td>
<td align="right">4,723,300</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">4,497,960</td>
<td align="right">4,723,300</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">11,511,400</td>
<td align="right">12,057,300</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,965,380</td>
<td align="right">2,057,380</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">28,691,860</td>
<td align="right">29,992,940</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">83,280</td>
<td align="right">79,720</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">157,600</td>
<td align="right">164,260</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">13,607,320</td>
<td align="right">14,113,440</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,479,200</td>
<td align="right">1,534,140</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">9,959,540</td>
<td align="right">10,247,880</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">10,312,540</td>
<td align="right">10,476,920</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">277,200</td>
<td align="right">274,440</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">1,181,480</td>
<td align="right">1,173,720</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">143,140</td>
<td align="right">144,060</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">221,400</td>
<td align="right">222,660</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">1,398,160</td>
<td align="right">1,403,980</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">11,119,460</td>
<td align="right">11,079,840</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">11,119,460</td>
<td align="right">11,079,840</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">230,580</td>
<td align="right">229,840</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">27,847,000</td>
<td align="right">27,912,660</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">32,335,360</td>
<td align="right">32,394,480</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">32,335,360</td>
<td align="right">32,394,480</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">461,360</td>
<td align="right">460,620</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">461,360</td>
<td align="right">460,620</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">30,945,120</td>
<td align="right">30,989,900</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,415,000</td>
<td align="right">1,414,280</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">335,020</td>
<td align="right">335,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">334,840</td>
<td align="right">334,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">249,440</td>
<td align="right">249,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">223,920</td>
<td align="right">223,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">1,640</td>
<td align="right">1,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">5,885,040</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">867,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">663,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">218,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">160,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">125,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">100,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">99,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">68,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right"></td>
<td align="right">39,900</td>
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
<td align="right">1,200</td>
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
