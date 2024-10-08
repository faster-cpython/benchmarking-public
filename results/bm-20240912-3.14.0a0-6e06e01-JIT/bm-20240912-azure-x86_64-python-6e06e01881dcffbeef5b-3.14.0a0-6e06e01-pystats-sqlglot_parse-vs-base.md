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
<td align="left">JUMP_BACKWARD</td>
<td align="right">25,333,760</td>
<td align="right">30,860</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">8,949,740</td>
<td align="right">11,500</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,573,760</td>
<td align="right">10,380</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,403,980</td>
<td align="right">11,280</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">3,163,980</td>
<td align="right">27,020</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,995,020</td>
<td align="right">80,240</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">20,510,720</td>
<td align="right">670,500</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">10,300</td>
<td align="right">380</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">28,293,060</td>
<td align="right">1,206,660</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">30,433,280</td>
<td align="right">1,953,160</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">17,346,360</td>
<td align="right">1,139,160</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">93,100</td>
<td align="right">6,140</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,300,480</td>
<td align="right">155,360</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">32,051,200</td>
<td align="right">4,420,720</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">32,675,680</td>
<td align="right">4,899,040</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">19,057,820</td>
<td align="right">2,933,440</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">34,027,240</td>
<td align="right">5,329,100</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">368,560</td>
<td align="right">58,460</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,382,480</td>
<td align="right">228,720</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">97,633,220</td>
<td align="right">16,469,860</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">17,571,700</td>
<td align="right">3,885,680</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">18,718,220</td>
<td align="right">4,575,520</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">16,081,860</td>
<td align="right">4,014,820</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">287,371,460</td>
<td align="right">74,431,660</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,662,400</td>
<td align="right">699,880</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,737,500</td>
<td align="right">1,026,520</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">552,458,560</td>
<td align="right">179,623,160</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">9,512,880</td>
<td align="right">3,323,420</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">9,512,960</td>
<td align="right">3,323,500</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">25,353,500</td>
<td align="right">9,006,800</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">27,676,600</td>
<td align="right">10,324,260</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">16,163,420</td>
<td align="right">6,136,340</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">24,207,520</td>
<td align="right">9,725,700</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">11,427,920</td>
<td align="right">4,737,580</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">117,790,720</td>
<td align="right">51,813,920</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">49,766,400</td>
<td align="right">22,279,060</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">46,919,760</td>
<td align="right">22,769,880</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">79,242,500</td>
<td align="right">38,480,680</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,979,760</td>
<td align="right">1,529,880</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,393,080</td>
<td align="right">3,912,340</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">23,427,220</td>
<td align="right">12,763,420</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">6,635,320</td>
<td align="right">3,672,500</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">53,934,200</td>
<td align="right">30,521,960</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,925,000</td>
<td align="right">1,182,460</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">26,319,120</td>
<td align="right">16,704,060</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,597,440</td>
<td align="right">1,043,100</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,185,040</td>
<td align="right">4,064,360</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">38,346,220</td>
<td align="right">25,321,380</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">34,560,000</td>
<td align="right">23,269,040</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">43,028,480</td>
<td align="right">29,094,840</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">25,505,740</td>
<td align="right">17,571,900</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,351,080</td>
<td align="right">54,250,560</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,576,920</td>
<td align="right">1,110,480</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">3,389,440</td>
<td align="right">2,482,240</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">19,844,640</td>
<td align="right">15,651,400</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">21,500,360</td>
<td align="right">17,542,740</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">60,880</td>
<td align="right">51,440</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,464,040</td>
<td align="right">36,079,440</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,332,020</td>
<td align="right">3,919,740</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">34,324,640</td>
<td align="right">32,112,760</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,443,820</td>
<td align="right">1,366,580</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,576,780</td>
<td align="right">1,500,540</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,821,240</td>
<td align="right">2,685,820</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,013,760</td>
<td align="right">995,280</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,054,720</td>
<td align="right">1,036,240</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,034,800</td>
<td align="right">3,986,800</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,343,420</td>
<td align="right">1,333,580</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,129,300</td>
<td align="right">2,119,460</td>
<td align="right">-0.5%</td>
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
<td align="left">LOAD_DEREF</td>
<td align="right">4,935,920</td>
<td align="right">4,935,920</td>
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
<td align="left">CALL_KW_PY</td>
<td align="right">962,180</td>
<td align="right">962,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">839,680</td>
<td align="right">839,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">645,000</td>
<td align="right">645,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">604,160</td>
<td align="right">604,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">174,080</td>
<td align="right">174,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">82,000</td>
<td align="right">82,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">71,640</td>
<td align="right">71,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">61,440</td>
<td align="right">61,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">61,440</td>
<td align="right">61,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">61,440</td>
<td align="right">61,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">51,120</td>
<td align="right">51,120</td>
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
<td align="left">MAKE_FUNCTION</td>
<td align="right">20,480</td>
<td align="right">20,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">20,480</td>
<td align="right">20,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">20,460</td>
<td align="right">20,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">18,200</td>
<td align="right">18,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">16,640</td>
<td align="right">16,640</td>
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
<td align="left">STORE_SUBSCR_DICT</td>
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
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">7,952,100</td>
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
<td align="right">3,573,760</td>
<td align="right">100.0%</td>
<td align="right">10,380</td>
<td align="right">100.0%</td>
<td align="right">-99.7%</td>
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
<td align="right">1,403,160</td>
<td align="right">3.9%</td>
<td align="right">10,840</td>
<td align="right">0.0%</td>
<td align="right">-99.2%</td>
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
<td align="right">96.0%</td>
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
<td align="right">540</td>
<td align="right">38.6%</td>
<td align="right">160</td>
<td align="right">15.7%</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">860</td>
<td align="right">61.4%</td>
<td align="right">860</td>
<td align="right">84.3%</td>
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
<td align="right">540</td>
<td align="right">100.0%</td>
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">-70.4%</td>
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
<td align="right">5,460</td>
<td align="right">0.0%</td>
<td align="right">5,460</td>
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
<td align="right">87,782,000</td>
<td align="right">97.8%</td>
<td align="right">87,782,000</td>
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
<td align="right">1,937,380</td>
<td align="right">2.2%</td>
<td align="right">1,937,380</td>
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
<td align="right">42,460</td>
<td align="right">100.0%</td>
<td align="right">42,460</td>
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
<td align="right">23,419,340</td>
<td align="right">38.6%</td>
<td align="right">12,758,260</td>
<td align="right">25.5%</td>
<td align="right">-45.5%</td>
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
<td align="right">61.4%</td>
<td align="right">37,191,220</td>
<td align="right">74.4%</td>
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
<td align="right">7,420</td>
<td align="right">94.2%</td>
<td align="right">4,700</td>
<td align="right">91.1%</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">460</td>
<td align="right">5.8%</td>
<td align="right">460</td>
<td align="right">8.9%</td>
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
<td align="right">460</td>
<td align="right">6.2%</td>
<td align="right">160</td>
<td align="right">3.4%</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,940</td>
<td align="right">93.5%</td>
<td align="right">4,540</td>
<td align="right">96.6%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">92,440</td>
<td align="right">0.5%</td>
<td align="right">5,640</td>
<td align="right">0.0%</td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,627,900</td>
<td align="right">8.5%</td>
<td align="right">1,627,880</td>
<td align="right">8.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,356,760</td>
<td align="right">91.0%</td>
<td align="right">17,356,780</td>
<td align="right">91.4%</td>
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
<td align="right">380</td>
<td align="right">1.2%</td>
<td align="right">220</td>
<td align="right">0.7%</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,980</td>
<td align="right">98.8%</td>
<td align="right">30,980</td>
<td align="right">99.3%</td>
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
<td align="right">220</td>
<td align="right">57.9%</td>
<td align="right">120</td>
<td align="right">54.5%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">160</td>
<td align="right">42.1%</td>
<td align="right">100</td>
<td align="right">45.5%</td>
<td align="right">-37.5%</td>
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
<td align="right">378,860</td>
<td align="right">2.3%</td>
<td align="right">58,840</td>
<td align="right">1.4%</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">16,076,900</td>
<td align="right">97.7%</td>
<td align="right">4,012,880</td>
<td align="right">98.5%</td>
<td align="right">-75.0%</td>
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
<td align="right">4,860</td>
<td align="right">98.0%</td>
<td align="right">1,840</td>
<td align="right">94.8%</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">100</td>
<td align="right">2.0%</td>
<td align="right">100</td>
<td align="right">5.2%</td>
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
<td align="right">540</td>
<td align="right">11.1%</td>
<td align="right">160</td>
<td align="right">8.7%</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">2,340</td>
<td align="right">48.1%</td>
<td align="right">720</td>
<td align="right">39.1%</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">900</td>
<td align="right">18.5%</td>
<td align="right">420</td>
<td align="right">22.8%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,080</td>
<td align="right">22.2%</td>
<td align="right">540</td>
<td align="right">29.3%</td>
<td align="right">-50.0%</td>
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
<td align="right">6,421,100</td>
<td align="right">1.5%</td>
<td align="right">2,217,380</td>
<td align="right">0.5%</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">26,284,640</td>
<td align="right">6.0%</td>
<td align="right">16,672,340</td>
<td align="right">3.9%</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">403,096,740</td>
<td align="right">92.5%</td>
<td align="right">403,577,580</td>
<td align="right">95.5%</td>
<td align="right">0.1%</td>
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
<td align="right">129,920</td>
<td align="right">83.5%</td>
<td align="right">50,620</td>
<td align="right">68.8%</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">25,680</td>
<td align="right">16.5%</td>
<td align="right">22,920</td>
<td align="right">31.2%</td>
<td align="right">-10.7%</td>
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
<td align="right">520</td>
<td align="right">2.0%</td>
<td align="right">420</td>
<td align="right">1.8%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">21,900</td>
<td align="right">85.3%</td>
<td align="right">19,340</td>
<td align="right">84.4%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,260</td>
<td align="right">12.7%</td>
<td align="right">3,160</td>
<td align="right">13.8%</td>
<td align="right">-3.1%</td>
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
<td align="right">58,186,620</td>
<td align="right">100.0%</td>
<td align="right">40,968,540</td>
<td align="right">100.0%</td>
<td align="right">-29.6%</td>
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
<td align="right">6,827,580</td>
<td align="right">7.0%</td>
<td align="right">4,145,600</td>
<td align="right">4.3%</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">90,805,640</td>
<td align="right">93.0%</td>
<td align="right">91,891,340</td>
<td align="right">95.7%</td>
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
<td align="right">129,660</td>
<td align="right">100.0%</td>
<td align="right">79,060</td>
<td align="right">100.0%</td>
<td align="right">-39.0%</td>
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
<td align="right">4,680,840</td>
<td align="right">5.9%</td>
<td align="right">2,291,600</td>
<td align="right">3.0%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">74,180,980</td>
<td align="right">94.0%</td>
<td align="right">74,581,500</td>
<td align="right">97.0%</td>
<td align="right">0.5%</td>
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
<td align="right">13,360</td>
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
<td align="right">91,140</td>
<td align="right">99.8%</td>
<td align="right">46,100</td>
<td align="right">99.7%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">160</td>
<td align="right">0.3%</td>
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
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">160</td>
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
<td align="right">9,512,880</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">986,588,460</td>
<td align="right">44.7%</td>
<td align="right">381,913,120</td>
<td align="right">43.1%</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,127,919,640</td>
<td align="right">51.1%</td>
<td align="right">458,029,680</td>
<td align="right">51.7%</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">70,936,880</td>
<td align="right">3.2%</td>
<td align="right">33,547,940</td>
<td align="right">3.8%</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">21,531,180</td>
<td align="right">1.0%</td>
<td align="right">12,256,120</td>
<td align="right">1.4%</td>
<td align="right">-43.1%</td>
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
<td align="right">3,573,760</td>
<td align="right">5.0%</td>
<td align="right">10,380</td>
<td align="right">0.0%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,403,160</td>
<td align="right">2.0%</td>
<td align="right">10,840</td>
<td align="right">0.0%</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">92,440</td>
<td align="right">0.1%</td>
<td align="right">5,640</td>
<td align="right">0.0%</td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">16,076,900</td>
<td align="right">22.7%</td>
<td align="right">4,012,880</td>
<td align="right">12.0%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">23,419,340</td>
<td align="right">33.0%</td>
<td align="right">12,758,260</td>
<td align="right">38.1%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">26,284,640</td>
<td align="right">37.1%</td>
<td align="right">16,672,340</td>
<td align="right">49.8%</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">13,360</td>
<td align="right">0.0%</td>
<td align="right">13,360</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,622,520</td>
<td align="right">12.2%</td>
<td align="right">828,600</td>
<td align="right">6.8%</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,616,420</td>
<td align="right">7.5%</td>
<td align="right">531,560</td>
<td align="right">4.3%</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,310,220</td>
<td align="right">10.7%</td>
<td align="right">1,115,700</td>
<td align="right">9.1%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,827,580</td>
<td align="right">31.7%</td>
<td align="right">4,145,600</td>
<td align="right">33.8%</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">813,820</td>
<td align="right">3.8%</td>
<td align="right">813,800</td>
<td align="right">6.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,440,860</td>
<td align="right">11.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,357,340</td>
<td align="right">6.3%</td>
<td align="right">1,357,340</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">976,580</td>
<td align="right">4.5%</td>
<td align="right">976,580</td>
<td align="right">8.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">945,960</td>
<td align="right">4.4%</td>
<td align="right">945,960</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">814,080</td>
<td align="right">3.8%</td>
<td align="right">814,080</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">642,220</td>
<td align="right">5.2%</td>
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
<td align="left">Decrefs</td>
<td align="right">117,303,879</td>
<td align="right">9.3%</td>
<td align="right">763,092,203</td>
<td align="right">57.8%</td>
<td align="right">550.5%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">137,128,434</td>
<td align="right">11.6%</td>
<td align="right">783,856,622</td>
<td align="right">62.8%</td>
<td align="right">471.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">327,126</td>
<td align="right"></td>
<td align="right">89,678</td>
<td align="right"></td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">1,049,236,740</td>
<td align="right">88.4%</td>
<td align="right">464,193,060</td>
<td align="right">37.2%</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,115,846</td>
<td align="right"></td>
<td align="right">540,685</td>
<td align="right"></td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">1,141,596,960</td>
<td align="right">90.7%</td>
<td align="right">557,478,920</td>
<td align="right">42.2%</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">790,365</td>
<td align="right"></td>
<td align="right">452,572</td>
<td align="right"></td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">63,089,935</td>
<td align="right"></td>
<td align="right">61,716,028</td>
<td align="right"></td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">19,917,454</td>
<td align="right"></td>
<td align="right">20,154,902</td>
<td align="right"></td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">59,935,809</td>
<td align="right"></td>
<td align="right">59,926,086</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">60,700,400</td>
<td align="right">76.1%</td>
<td align="right">60,703,100</td>
<td align="right">76.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">19,020,600</td>
<td align="right"></td>
<td align="right">19,019,900</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">19,021,640</td>
<td align="right">23.9%</td>
<td align="right">19,021,040</td>
<td align="right">23.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">60,700,400</td>
<td align="right">76.1%</td>
<td align="right">60,701,940</td>
<td align="right">76.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
<td align="right">1,040 / 0 !!</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">120 / 0 !!</td>
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
<td align="right">2,142,280</td>
<td align="right">30,855,880</td>
<td align="right">1,520</td>
<td align="right">2,137,360</td>
<td align="right">30,853,940</td>
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
Stats gathered on: 2024-09-22
