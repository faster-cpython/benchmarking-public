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
<td align="right">4,580</td>
<td align="right">6,323,620</td>
<td align="right">137,970.3%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">14,640</td>
<td align="right">711,720</td>
<td align="right">4,761.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">129,420</td>
<td align="right">2,573,820</td>
<td align="right">1,888.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">52,000</td>
<td align="right">799,500</td>
<td align="right">1,437.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">34,260</td>
<td align="right">399,740</td>
<td align="right">1,066.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">14,800</td>
<td align="right">111,460</td>
<td align="right">653.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">1,440</td>
<td align="right">9,420</td>
<td align="right">554.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,440</td>
<td align="right">9,420</td>
<td align="right">554.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,440</td>
<td align="right">9,420</td>
<td align="right">554.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">453,380</td>
<td align="right">2,945,240</td>
<td align="right">549.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">46,540</td>
<td align="right">273,300</td>
<td align="right">487.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">186,700</td>
<td align="right">915,780</td>
<td align="right">390.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,757,880</td>
<td align="right">8,553,360</td>
<td align="right">386.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">592,260</td>
<td align="right">2,632,720</td>
<td align="right">344.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,480</td>
<td align="right">10,460</td>
<td align="right">321.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,049,240</td>
<td align="right">3,688,740</td>
<td align="right">251.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">46,560</td>
<td align="right">147,780</td>
<td align="right">217.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">12,300</td>
<td align="right">37,140</td>
<td align="right">202.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,267,180</td>
<td align="right">2,819,700</td>
<td align="right">122.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">345,600</td>
<td align="right">764,660</td>
<td align="right">121.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">111,080</td>
<td align="right">238,020</td>
<td align="right">114.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,843,640</td>
<td align="right">5,716,340</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,450,220</td>
<td align="right">8,904,600</td>
<td align="right">100.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,090,620</td>
<td align="right">4,179,320</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,240,700</td>
<td align="right">6,117,720</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">3,735,080</td>
<td align="right">7,028,940</td>
<td align="right">88.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">545,520</td>
<td align="right">1,019,260</td>
<td align="right">86.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,363,620</td>
<td align="right">4,227,920</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,673,400</td>
<td align="right">9,919,380</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,652,860</td>
<td align="right">8,033,100</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">24,491,840</td>
<td align="right">42,045,680</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,536,140</td>
<td align="right">5,925,400</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">26,876,600</td>
<td align="right">44,581,180</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">6,495,220</td>
<td align="right">10,618,620</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,753,180</td>
<td align="right">10,960,400</td>
<td align="right">62.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">9,331,460</td>
<td align="right">14,704,600</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">109,429,640</td>
<td align="right">172,113,260</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,215,260</td>
<td align="right">3,482,640</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,250,440</td>
<td align="right">6,677,080</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">38,606,980</td>
<td align="right">60,249,780</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">736,380</td>
<td align="right">1,140,740</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">2,090,620</td>
<td align="right">3,178,640</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">16,691,820</td>
<td align="right">25,144,420</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">27,498,300</td>
<td align="right">41,144,800</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,331,180</td>
<td align="right">3,471,160</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">17,467,640</td>
<td align="right">25,854,240</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,830,640</td>
<td align="right">7,050,280</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">555,600</td>
<td align="right">807,520</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">21,481,100</td>
<td align="right">30,814,000</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,168,100</td>
<td align="right">4,516,020</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">7,998,440</td>
<td align="right">11,314,980</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">15,633,520</td>
<td align="right">21,763,860</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">273,840</td>
<td align="right">375,920</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">7,504,120</td>
<td align="right">10,176,200</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">17,529,860</td>
<td align="right">23,758,660</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,217,720</td>
<td align="right">5,602,340</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">8,168,600</td>
<td align="right">10,783,720</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">7,154,880</td>
<td align="right">9,429,500</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,481,980</td>
<td align="right">1,936,120</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,655,420</td>
<td align="right">2,127,700</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">10,469,920</td>
<td align="right">13,349,560</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">548,140</td>
<td align="right">687,980</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,204,720</td>
<td align="right">1,510,980</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">322,920</td>
<td align="right">402,420</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">9,062,680</td>
<td align="right">11,153,120</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">15,821,920</td>
<td align="right">19,282,360</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">450,720</td>
<td align="right">544,820</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,555,960</td>
<td align="right">1,857,700</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">420,020</td>
<td align="right">496,060</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,856,460</td>
<td align="right">2,175,600</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,525,720</td>
<td align="right">7,618,040</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,942,540</td>
<td align="right">2,253,240</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">19,290,560</td>
<td align="right">16,310,400</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">954,540</td>
<td align="right">1,093,140</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">2,082,040</td>
<td align="right">2,380,900</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,298,780</td>
<td align="right">1,426,100</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,053,480</td>
<td align="right">2,205,760</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">23,910,000</td>
<td align="right">25,479,140</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,279,780</td>
<td align="right">5,601,980</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,909,360</td>
<td align="right">2,010,940</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">227,920</td>
<td align="right">237,560</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,011,200</td>
<td align="right">2,092,920</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">947,120</td>
<td align="right">978,880</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">567,120</td>
<td align="right">578,080</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">447,840</td>
<td align="right">454,960</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,131,680</td>
<td align="right">1,149,520</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">631,040</td>
<td align="right">636,580</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">449,200</td>
<td align="right">448,880</td>
<td align="right">-0.1%</td>
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
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">708,480</td>
<td align="right">708,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">671,760</td>
<td align="right">671,760</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">293,680</td>
<td align="right">293,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">226,100</td>
<td align="right">226,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">223,920</td>
<td align="right">223,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">79,840</td>
<td align="right">79,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">52,420</td>
<td align="right">52,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">46,240</td>
<td align="right">46,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">3,820</td>
<td align="right">3,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">540</td>
<td align="right">540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">540</td>
<td align="right">540</td>
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
<td align="right">4,648,780</td>
<td align="right">19.2%</td>
<td align="right">8,027,600</td>
<td align="right">29.1%</td>
<td align="right">72.7%</td>
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
<td align="right">80.8%</td>
<td align="right">19,568,780</td>
<td align="right">70.9%</td>
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
<td align="right">4,040</td>
<td align="right">99.0%</td>
<td align="right">5,460</td>
<td align="right">99.3%</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">40</td>
<td align="right">1.0%</td>
<td align="right">40</td>
<td align="right">0.7%</td>
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
<td align="left">and int</td>
<td align="right">2,440</td>
<td align="right">60.4%</td>
<td align="right">3,700</td>
<td align="right">67.8%</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">60</td>
<td align="right">1.5%</td>
<td align="right">80</td>
<td align="right">1.5%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">320</td>
<td align="right">7.9%</td>
<td align="right">400</td>
<td align="right">7.3%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">760</td>
<td align="right">18.8%</td>
<td align="right">820</td>
<td align="right">15.0%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">260</td>
<td align="right">6.4%</td>
<td align="right">260</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">100</td>
<td align="right">2.5%</td>
<td align="right">100</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">100</td>
<td align="right">2.5%</td>
<td align="right">100</td>
<td align="right">1.8%</td>
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
<td align="right">46,540</td>
<td align="right">100.0%</td>
<td align="right">273,300</td>
<td align="right">100.0%</td>
<td align="right">487.2%</td>
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
<td align="right">51,860</td>
<td align="right">0.2%</td>
<td align="right">799,080</td>
<td align="right">2.7%</td>
<td align="right">1,440.8%</td>
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
<td align="right">94.7%</td>
<td align="right">27,746,400</td>
<td align="right">92.3%</td>
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
<td align="right">5.0%</td>
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
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">400</td>
<td align="right">1.4%</td>
<td align="right">233.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,480</td>
<td align="right">99.6%</td>
<td align="right">28,480</td>
<td align="right">98.6%</td>
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
<td align="right">20</td>
<td align="right">16.7%</td>
<td align="right">200</td>
<td align="right">50.0%</td>
<td align="right">900.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">20</td>
<td align="right">16.7%</td>
<td align="right">80</td>
<td align="right">20.0%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">80</td>
<td align="right">66.7%</td>
<td align="right">80</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">40</td>
<td align="right">10.0%</td>
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
<td align="right">1,340</td>
<td align="right">100.0%</td>
<td align="right">1,340</td>
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
<td align="right">1,142,060</td>
<td align="right">6.6%</td>
<td align="right">1.6%</td>
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
<td align="right">167,900</td>
<td align="right">1.0%</td>
<td align="right">-1.3%</td>
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
<td align="right">16,070,320</td>
<td align="right">92.4%</td>
<td align="right">-0.1%</td>
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
<td align="right">3,260</td>
<td align="right">30.5%</td>
<td align="right">3,220</td>
<td align="right">30.3%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,440</td>
<td align="right">69.5%</td>
<td align="right">7,400</td>
<td align="right">69.7%</td>
<td align="right">-0.5%</td>
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
<td align="right">6,620</td>
<td align="right">89.0%</td>
<td align="right">6,580</td>
<td align="right">88.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">260</td>
<td align="right">3.5%</td>
<td align="right">260</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">220</td>
<td align="right">3.0%</td>
<td align="right">220</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">200</td>
<td align="right">2.7%</td>
<td align="right">200</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">140</td>
<td align="right">1.9%</td>
<td align="right">140</td>
<td align="right">1.9%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,842,600</td>
<td align="right">18.9%</td>
<td align="right">5,714,560</td>
<td align="right">31.9%</td>
<td align="right">101.0%</td>
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
<td align="right">81.1%</td>
<td align="right">12,221,840</td>
<td align="right">68.1%</td>
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
<td align="right">1,040</td>
<td align="right">100.0%</td>
<td align="right">1,780</td>
<td align="right">100.0%</td>
<td align="right">71.2%</td>
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
<td align="right">980</td>
<td align="right">94.2%</td>
<td align="right">1,720</td>
<td align="right">96.6%</td>
<td align="right">75.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">60</td>
<td align="right">5.8%</td>
<td align="right">60</td>
<td align="right">3.4%</td>
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
<td align="right">452,360</td>
<td align="right">21.8%</td>
<td align="right">2,938,680</td>
<td align="right">34.3%</td>
<td align="right">549.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">19,320</td>
<td align="right">0.9%</td>
<td align="right">92,220</td>
<td align="right">1.1%</td>
<td align="right">377.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,605,200</td>
<td align="right">77.3%</td>
<td align="right">5,538,860</td>
<td align="right">64.6%</td>
<td align="right">245.1%</td>
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
<td align="right">980</td>
<td align="right">71.0%</td>
<td align="right">6,520</td>
<td align="right">78.6%</td>
<td align="right">565.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">400</td>
<td align="right">29.0%</td>
<td align="right">1,780</td>
<td align="right">21.4%</td>
<td align="right">345.0%</td>
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
<td align="left">seq iter</td>
<td align="right">760</td>
<td align="right">77.6%</td>
<td align="right">6,300</td>
<td align="right">96.6%</td>
<td align="right">728.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">100</td>
<td align="right">10.2%</td>
<td align="right">100</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">100</td>
<td align="right">10.2%</td>
<td align="right">100</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">20</td>
<td align="right">2.0%</td>
<td align="right">20</td>
<td align="right">0.3%</td>
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
<td align="right">6,517,760</td>
<td align="right">8.7%</td>
<td align="right">7,609,660</td>
<td align="right">10.0%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">68,254,420</td>
<td align="right">91.3%</td>
<td align="right">68,393,020</td>
<td align="right">90.0%</td>
<td align="right">0.2%</td>
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
<td align="right">2,760</td>
<td align="right">34.7%</td>
<td align="right">3,060</td>
<td align="right">36.5%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,200</td>
<td align="right">65.3%</td>
<td align="right">5,320</td>
<td align="right">63.5%</td>
<td align="right">2.3%</td>
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
<td align="right">20</td>
<td align="right">0.7%</td>
<td align="right">40</td>
<td align="right">1.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">60</td>
<td align="right">2.2%</td>
<td align="right">100</td>
<td align="right">3.3%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">240</td>
<td align="right">8.7%</td>
<td align="right">200</td>
<td align="right">6.5%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,020</td>
<td align="right">73.2%</td>
<td align="right">2,300</td>
<td align="right">75.2%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">300</td>
<td align="right">10.9%</td>
<td align="right">300</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">120</td>
<td align="right">4.3%</td>
<td align="right">120</td>
<td align="right">3.9%</td>
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
<td align="right">43,320,220</td>
<td align="right">100.0%</td>
<td align="right">60,427,160</td>
<td align="right">100.0%</td>
<td align="right">39.5%</td>
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
<td align="right">360</td>
<td align="right">100.0%</td>
<td align="right">360</td>
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
<td align="right">46,240</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">419,460</td>
<td align="right">11.5%</td>
<td align="right">495,440</td>
<td align="right">13.3%</td>
<td align="right">18.1%</td>
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
<td align="right">88.4%</td>
<td align="right">3,216,080</td>
<td align="right">86.6%</td>
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
<td align="right">560</td>
<td align="right">100.0%</td>
<td align="right">620</td>
<td align="right">100.0%</td>
<td align="right">10.7%</td>
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
<td align="left">bytearray int</td>
<td align="right">300</td>
<td align="right">53.6%</td>
<td align="right">360</td>
<td align="right">58.1%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">160</td>
<td align="right">28.6%</td>
<td align="right">160</td>
<td align="right">25.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">100</td>
<td align="right">17.9%</td>
<td align="right">100</td>
<td align="right">16.1%</td>
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
<td align="right">91,200</td>
<td align="right">0.2%</td>
<td align="right">166,180</td>
<td align="right">0.4%</td>
<td align="right">82.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">733,340</td>
<td align="right">2.0%</td>
<td align="right">1,133,780</td>
<td align="right">3.0%</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">36,159,820</td>
<td align="right">97.8%</td>
<td align="right">36,399,080</td>
<td align="right">96.5%</td>
<td align="right">0.7%</td>
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
<td align="right">2,960</td>
<td align="right">62.7%</td>
<td align="right">6,880</td>
<td align="right">68.3%</td>
<td align="right">132.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,760</td>
<td align="right">37.3%</td>
<td align="right">3,200</td>
<td align="right">31.7%</td>
<td align="right">81.8%</td>
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
<td align="right">1,020</td>
<td align="right">34.5%</td>
<td align="right">4,600</td>
<td align="right">66.9%</td>
<td align="right">351.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">300</td>
<td align="right">10.1%</td>
<td align="right">380</td>
<td align="right">5.5%</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">380</td>
<td align="right">12.8%</td>
<td align="right">460</td>
<td align="right">6.7%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,160</td>
<td align="right">39.2%</td>
<td align="right">1,340</td>
<td align="right">19.5%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">100</td>
<td align="right">3.4%</td>
<td align="right">100</td>
<td align="right">1.5%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">16,319,340</td>
<td align="right">100.0%</td>
<td align="right">16,319,340</td>
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
<td align="right">16,909,580</td>
<td align="right">3.0%</td>
<td align="right">28,219,200</td>
<td align="right">3.4%</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">358,242,180</td>
<td align="right">63.7%</td>
<td align="right">535,906,620</td>
<td align="right">63.9%</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">185,617,520</td>
<td align="right">33.0%</td>
<td align="right">272,234,140</td>
<td align="right">32.5%</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,842,280</td>
<td align="right">0.3%</td>
<td align="right">1,989,500</td>
<td align="right">0.2%</td>
<td align="right">8.0%</td>
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
<td align="right">51,860</td>
<td align="right">0.3%</td>
<td align="right">799,080</td>
<td align="right">2.8%</td>
<td align="right">1,440.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">452,360</td>
<td align="right">2.7%</td>
<td align="right">2,938,680</td>
<td align="right">10.4%</td>
<td align="right">549.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">46,540</td>
<td align="right">0.3%</td>
<td align="right">273,300</td>
<td align="right">1.0%</td>
<td align="right">487.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,842,600</td>
<td align="right">16.8%</td>
<td align="right">5,714,560</td>
<td align="right">20.3%</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">4,648,780</td>
<td align="right">27.5%</td>
<td align="right">8,027,600</td>
<td align="right">28.5%</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">733,340</td>
<td align="right">4.3%</td>
<td align="right">1,133,780</td>
<td align="right">4.0%</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">419,460</td>
<td align="right">2.5%</td>
<td align="right">495,440</td>
<td align="right">1.8%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,517,760</td>
<td align="right">38.6%</td>
<td align="right">7,609,660</td>
<td align="right">27.0%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,124,180</td>
<td align="right">6.7%</td>
<td align="right">1,142,060</td>
<td align="right">4.1%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">46,240</td>
<td align="right">0.3%</td>
<td align="right">46,240</td>
<td align="right">0.2%</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">19,320</td>
<td align="right">1.0%</td>
<td align="right">92,220</td>
<td align="right">4.6%</td>
<td align="right">377.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">61,000</td>
<td align="right">3.3%</td>
<td align="right">132,580</td>
<td align="right">6.7%</td>
<td align="right">117.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,760</td>
<td align="right">0.3%</td>
<td align="right">8,160</td>
<td align="right">0.4%</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">170,160</td>
<td align="right">9.2%</td>
<td align="right">167,900</td>
<td align="right">8.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,276,900</td>
<td align="right">69.3%</td>
<td align="right">1,276,900</td>
<td align="right">64.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">232,280</td>
<td align="right">12.6%</td>
<td align="right">232,280</td>
<td align="right">11.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">52,420</td>
<td align="right">2.8%</td>
<td align="right">52,420</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">25,440</td>
<td align="right">1.4%</td>
<td align="right">25,440</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CACHE</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">RESUME</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,600</td>
<td align="right">0.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,600</td>
<td align="right">0.1%</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">5</td>
<td align="right"></td>
<td align="right">12</td>
<td align="right"></td>
<td align="right">140.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">43,340</td>
<td align="right">0.1%</td>
<td align="right">71,920</td>
<td align="right">0.1%</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">239,189,940</td>
<td align="right">239,189,940 / 0 !!</td>
<td align="right">323,162,140</td>
<td align="right">323,162,140 / 0 !!</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">489,718,524</td>
<td align="right">489,718,524 / 0 !!</td>
<td align="right">380,307,171</td>
<td align="right">380,307,171 / 0 !!</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">45</td>
<td align="right"></td>
<td align="right">54</td>
<td align="right"></td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">471,857,210</td>
<td align="right">471,857,210 / 0 !!</td>
<td align="right">389,060,381</td>
<td align="right">389,060,381 / 0 !!</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">329,885,440</td>
<td align="right">329,885,440 / 0 !!</td>
<td align="right">387,289,900</td>
<td align="right">387,289,900 / 0 !!</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">70</td>
<td align="right"></td>
<td align="right">68</td>
<td align="right"></td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">59,404,306</td>
<td align="right"></td>
<td align="right">59,443,809</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">56,664,340</td>
<td align="right">75.7%</td>
<td align="right">56,697,160</td>
<td align="right">75.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">18,211,800</td>
<td align="right">24.3%</td>
<td align="right">18,218,380</td>
<td align="right">24.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">18,220,800</td>
<td align="right"></td>
<td align="right">18,227,380</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">56,618,920</td>
<td align="right">75.6%</td>
<td align="right">56,623,160</td>
<td align="right">75.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">9,368,550</td>
<td align="right"></td>
<td align="right">9,369,012</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">19,046,755</td>
<td align="right"></td>
<td align="right">19,046,988</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">2,080</td>
<td align="right">0.0%</td>
<td align="right">2,080</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">600</td>
<td align="right">4.7%</td>
<td align="right">8,660</td>
<td align="right">18.0%</td>
<td align="right">1,343.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">4,420</td>
<td align="right">34.9%</td>
<td align="right">37,240</td>
<td align="right">77.5%</td>
<td align="right">742.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">12,660</td>
<td align="right"></td>
<td align="right">48,060</td>
<td align="right"></td>
<td align="right">279.6%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">560</td>
<td align="right">4.4%</td>
<td align="right">1,880</td>
<td align="right">3.9%</td>
<td align="right">235.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">9,160</td>
<td align="right">72.4%</td>
<td align="right">16,400</td>
<td align="right">34.1%</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">58,861,080</td>
<td align="right"></td>
<td align="right">36,096,880</td>
<td align="right"></td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">8,240</td>
<td align="right">65.1%</td>
<td align="right">10,820</td>
<td align="right">22.5%</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,777,433,280</td>
<td align="right">3,019.7%</td>
<td align="right">1,344,782,300</td>
<td align="right">3,725.5%</td>
<td align="right">-24.3%</td>
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
<td align="right">620</td>
<td align="right">1.3%</td>
<td align="right">620 / 0 !!</td>
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
<td align="right">4,420</td>
<td align="right"></td>
<td align="right">37,240</td>
<td align="right"></td>
<td align="right">742.5%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">4,420</td>
<td align="right">100.0%</td>
<td align="right">37,240</td>
<td align="right">100.0%</td>
<td align="right">742.5%</td>
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
<td align="right">140</td>
<td align="right">3.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">260</td>
<td align="right">5.9%</td>
<td align="right">2,120</td>
<td align="right">5.7%</td>
<td align="right">715.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">480</td>
<td align="right">10.9%</td>
<td align="right">940</td>
<td align="right">2.5%</td>
<td align="right">95.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">900</td>
<td align="right">20.4%</td>
<td align="right">8,060</td>
<td align="right">21.6%</td>
<td align="right">795.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,520</td>
<td align="right">34.4%</td>
<td align="right">11,240</td>
<td align="right">30.2%</td>
<td align="right">639.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">980</td>
<td align="right">22.2%</td>
<td align="right">10,820</td>
<td align="right">29.1%</td>
<td align="right">1,004.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">140</td>
<td align="right">3.2%</td>
<td align="right">4,060</td>
<td align="right">10.9%</td>
<td align="right">2,800.0%</td>
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
<td align="right">400</td>
<td align="right">9.0%</td>
<td align="right">1,020</td>
<td align="right">2.7%</td>
<td align="right">155.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">280</td>
<td align="right">6.3%</td>
<td align="right">1,700</td>
<td align="right">4.6%</td>
<td align="right">507.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">740</td>
<td align="right">16.7%</td>
<td align="right">3,980</td>
<td align="right">10.7%</td>
<td align="right">437.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,600</td>
<td align="right">36.2%</td>
<td align="right">12,700</td>
<td align="right">34.1%</td>
<td align="right">693.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,000</td>
<td align="right">22.6%</td>
<td align="right">12,540</td>
<td align="right">33.7%</td>
<td align="right">1,154.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">400</td>
<td align="right">9.0%</td>
<td align="right">4,800</td>
<td align="right">12.9%</td>
<td align="right">1,100.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">500</td>
<td align="right">1.3%</td>
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
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">42,540</td>
<td align="right">6,400</td>
<td align="right">-85.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">221,680</td>
<td align="right">34,860</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">412,200</td>
<td align="right">113,340</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">130,900</td>
<td align="right">36,800</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">148,000</td>
<td align="right">43,380</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">181,880</td>
<td align="right">54,940</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">148,000</td>
<td align="right">51,340</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">122,120</td>
<td align="right">42,620</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">148,000</td>
<td align="right">53,900</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">6,756,440</td>
<td align="right">2,615,120</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">6,190,440</td>
<td align="right">2,521,560</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">5,832,240</td>
<td align="right">2,432,360</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">4,512,840</td>
<td align="right">1,897,720</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">179,360</td>
<td align="right">77,280</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,128,880</td>
<td align="right">488,880</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,872,520</td>
<td align="right">812,660</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">2,210,900</td>
<td align="right">972,880</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,928,160</td>
<td align="right">853,480</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">8,039,280</td>
<td align="right">3,590,500</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">1,259,840</td>
<td align="right">562,760</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,320,340</td>
<td align="right">1,052,960</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">6,237,720</td>
<td align="right">2,858,900</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">14,251,220</td>
<td align="right">6,748,700</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">4,595,780</td>
<td align="right">2,206,520</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">4,595,780</td>
<td align="right">2,206,520</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,595,780</td>
<td align="right">2,206,520</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">4,083,080</td>
<td align="right">1,993,520</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">10,534,540</td>
<td align="right">5,161,400</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">4,117,700</td>
<td align="right">2,029,000</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">5,687,880</td>
<td align="right">2,815,920</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,400,480</td>
<td align="right">2,180,840</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,400,480</td>
<td align="right">2,180,840</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">8,423,160</td>
<td align="right">4,177,180</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">2,161,700</td>
<td align="right">1,073,680</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">7,318,540</td>
<td align="right">3,697,880</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,517,900</td>
<td align="right">770,680</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">7,413,460</td>
<td align="right">3,801,840</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">2,366,900</td>
<td align="right">1,216,040</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,226,820</td>
<td align="right">1,152,140</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,801,760</td>
<td align="right">939,460</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,415,120</td>
<td align="right">2,327,400</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">11,891,720</td>
<td align="right">6,271,820</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,569,280</td>
<td align="right">840,200</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">18,442,740</td>
<td align="right">9,990,140</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,246,760</td>
<td align="right">1,790,540</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">12,767,680</td>
<td align="right">7,129,420</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">12,767,680</td>
<td align="right">7,129,420</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">12,588,320</td>
<td align="right">7,052,140</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">12,576,300</td>
<td align="right">7,055,280</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">4,696,460</td>
<td align="right">2,656,000</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">4,696,460</td>
<td align="right">2,656,000</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,109,300</td>
<td align="right">637,020</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">23,744,520</td>
<td align="right">13,671,560</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">18,463,900</td>
<td align="right">10,753,420</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">894,220</td>
<td align="right">528,740</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">11,086,020</td>
<td align="right">6,576,800</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">51,372,960</td>
<td align="right">30,846,660</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,791,500</td>
<td align="right">1,699,600</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">58,861,080</td>
<td align="right">36,096,880</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">10,310,480</td>
<td align="right">6,341,540</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">15,691,640</td>
<td align="right">9,761,840</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,567,460</td>
<td align="right">2,219,540</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,905,640</td>
<td align="right">1,192,240</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">25,565,020</td>
<td align="right">16,103,640</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">692,160</td>
<td align="right">440,240</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,696,220</td>
<td align="right">3,624,000</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">54,368,900</td>
<td align="right">34,977,940</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">12,319,940</td>
<td align="right">8,112,720</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">12,319,940</td>
<td align="right">8,112,720</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">2,070,060</td>
<td align="right">1,380,640</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,752,480</td>
<td align="right">3,868,940</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">28,675,380</td>
<td align="right">19,342,480</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">28,675,380</td>
<td align="right">19,342,480</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">4,317,800</td>
<td align="right">2,933,180</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">40,844,200</td>
<td align="right">28,562,700</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">73,804,840</td>
<td align="right">51,844,480</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">9,942,940</td>
<td align="right">7,032,120</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">354,820</td>
<td align="right">253,600</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">354,820</td>
<td align="right">253,600</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">34,297,180</td>
<td align="right">24,569,080</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">9,021,760</td>
<td align="right">6,469,520</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">29,272,640</td>
<td align="right">21,042,440</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">806,740</td>
<td align="right">579,980</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">8,565,740</td>
<td align="right">6,291,120</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">116,833,740</td>
<td align="right">85,981,720</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">47,905,100</td>
<td align="right">35,271,540</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">94,980</td>
<td align="right">70,140</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">55,711,380</td>
<td align="right">41,158,580</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">11,054,420</td>
<td align="right">8,177,400</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">10,244,120</td>
<td align="right">7,604,620</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">84,809,760</td>
<td align="right">63,005,180</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">156,800</td>
<td align="right">116,900</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">31,360</td>
<td align="right">23,380</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,360</td>
<td align="right">23,380</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">31,360</td>
<td align="right">23,380</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">5,303,560</td>
<td align="right">4,000,280</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">164,947,280</td>
<td align="right">124,929,360</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">1,341,500</td>
<td align="right">1,037,900</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">6,414,740</td>
<td align="right">5,031,400</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,448,520</td>
<td align="right">1,146,780</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">42,904,300</td>
<td align="right">33,976,900</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">27,045,300</td>
<td align="right">21,719,840</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">66,345,360</td>
<td align="right">53,436,020</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">9,054,640</td>
<td align="right">7,293,480</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">791,300</td>
<td align="right">651,460</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">11,431,400</td>
<td align="right">9,481,660</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,895,780</td>
<td align="right">1,585,080</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,019,780</td>
<td align="right">1,700,640</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">13,484,520</td>
<td align="right">11,394,080</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">2,160</td>
<td align="right">2,480</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">945,120</td>
<td align="right">817,800</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">19,283,380</td>
<td align="right">16,794,380</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">1,451,500</td>
<td align="right">1,297,340</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,744,320</td>
<td align="right">2,524,320</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">32,422,720</td>
<td align="right">29,978,320</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">32,422,720</td>
<td align="right">29,978,320</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">11,618,900</td>
<td align="right">10,912,580</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">31,032,480</td>
<td align="right">29,203,260</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,856,840</td>
<td align="right">2,704,560</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">11,930,540</td>
<td align="right">11,354,340</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">31,485,800</td>
<td align="right">30,101,860</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">340,400</td>
<td align="right">328,880</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">339,840</td>
<td align="right">328,880</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">223,920</td>
<td align="right">216,800</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">999,760</td>
<td align="right">968,000</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">999,760</td>
<td align="right">968,000</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">233,640</td>
<td align="right">226,920</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">280,800</td>
<td align="right">272,820</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">713,620</td>
<td align="right">694,120</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">834,560</td>
<td align="right">814,460</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">28,998,340</td>
<td align="right">29,687,540</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">464,400</td>
<td align="right">454,760</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">464,400</td>
<td align="right">454,760</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">10,315,200</td>
<td align="right">10,213,620</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">9,963,620</td>
<td align="right">9,868,440</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">1,606,640</td>
<td align="right">1,601,100</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">27,870,620</td>
<td align="right">27,794,640</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,023,360</td>
<td align="right">1,023,360</td>
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
<td align="left">_LOAD_GLOBAL</td>
<td align="right">63,140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">1,620</td>
<td align="right">1,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right"></td>
<td align="right">65,784,420</td>
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
Stats gathered on: 2024-09-23
