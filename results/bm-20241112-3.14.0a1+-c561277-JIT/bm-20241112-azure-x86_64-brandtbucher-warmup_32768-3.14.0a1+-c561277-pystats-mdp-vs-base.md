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
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">120</td>
<td align="right">690,720</td>
<td align="right">575,500.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,860</td>
<td align="right">3,403,800</td>
<td align="right">182,900.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">7,800</td>
<td align="right">739,260</td>
<td align="right">9,377.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">7,740</td>
<td align="right">277,900</td>
<td align="right">3,490.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">180</td>
<td align="right">3,960</td>
<td align="right">2,100.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">23,280</td>
<td align="right">274,580</td>
<td align="right">1,079.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">238,860</td>
<td align="right">1,086,200</td>
<td align="right">354.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">11,700</td>
<td align="right">51,180</td>
<td align="right">337.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">219,640</td>
<td align="right">941,300</td>
<td align="right">328.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">219,600</td>
<td align="right">910,220</td>
<td align="right">314.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">23,040</td>
<td align="right">94,620</td>
<td align="right">310.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">401,100</td>
<td align="right">1,360,780</td>
<td align="right">239.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">298,340</td>
<td align="right">966,320</td>
<td align="right">223.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">176,820</td>
<td align="right">494,060</td>
<td align="right">179.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,199,860</td>
<td align="right">3,248,640</td>
<td align="right">170.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">7,680</td>
<td align="right">17,280</td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">242,700</td>
<td align="right">494,300</td>
<td align="right">103.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">409,360</td>
<td align="right">766,580</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">455,700</td>
<td align="right">842,840</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">505,980</td>
<td align="right">916,740</td>
<td align="right">81.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">427,860</td>
<td align="right">718,600</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">297,120</td>
<td align="right">486,740</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">495,920</td>
<td align="right">806,440</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,725,620</td>
<td align="right">4,301,240</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">4,454,280</td>
<td align="right">6,863,220</td>
<td align="right">54.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">2,068,860</td>
<td align="right">3,141,980</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">762,840</td>
<td align="right">1,032,060</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">562,260</td>
<td align="right">760,080</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,661,560</td>
<td align="right">7,106,940</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">3,671,120</td>
<td align="right">4,524,540</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">293,040</td>
<td align="right">358,980</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">3,758,380</td>
<td align="right">4,465,780</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">382,260</td>
<td align="right">453,660</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">373,260</td>
<td align="right">439,200</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">373,440</td>
<td align="right">439,380</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">9,499,860</td>
<td align="right">11,094,380</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,943,520</td>
<td align="right">9,186,560</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">60,832,940</td>
<td align="right">68,416,760</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,334,140</td>
<td align="right">33,348,760</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,072,220</td>
<td align="right">2,258,120</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">812,700</td>
<td align="right">878,640</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">32,696,160</td>
<td align="right">35,108,920</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,175,520</td>
<td align="right">1,241,460</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">43,945,760</td>
<td align="right">46,396,740</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">48,396,000</td>
<td align="right">51,006,580</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">77,922,760</td>
<td align="right">82,105,140</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">26,440,740</td>
<td align="right">27,364,640</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">467,162,540</td>
<td align="right">481,616,240</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">23,243,760</td>
<td align="right">23,790,180</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">64,154,780</td>
<td align="right">65,575,760</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">51,149,760</td>
<td align="right">52,128,680</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">75,563,520</td>
<td align="right">76,688,220</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">226,922,720</td>
<td align="right">229,751,000</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">193,446,220</td>
<td align="right">195,771,280</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">25,651,200</td>
<td align="right">25,914,960</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">224,120</td>
<td align="right">226,080</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">22,957,580</td>
<td align="right">23,137,640</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">73,062,420</td>
<td align="right">73,458,060</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">125,619,480</td>
<td align="right">126,282,660</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">249,009,880</td>
<td align="right">247,757,540</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,700</td>
<td align="right">4,720</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">50,142,840</td>
<td align="right">50,351,820</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">32,307,680</td>
<td align="right">32,439,600</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">65,005,380</td>
<td align="right">65,185,520</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">378,329,920</td>
<td align="right">379,362,340</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">69,818,320</td>
<td align="right">70,007,280</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">47,024,840</td>
<td align="right">47,106,340</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">53,024,600</td>
<td align="right">53,096,040</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">291,433,700</td>
<td align="right">291,605,200</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">7,086,420</td>
<td align="right">7,090,140</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">142,305,680</td>
<td align="right">142,377,120</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">326,917,780</td>
<td align="right">326,917,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">243,371,880</td>
<td align="right">243,371,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">97,512,480</td>
<td align="right">97,512,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">60,078,600</td>
<td align="right">60,078,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">44,122,020</td>
<td align="right">44,122,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">43,683,180</td>
<td align="right">43,683,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">31,287,480</td>
<td align="right">31,287,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">30,039,300</td>
<td align="right">30,039,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">24,817,200</td>
<td align="right">24,817,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">7,584,840</td>
<td align="right">7,584,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,584,780</td>
<td align="right">7,584,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">7,086,420</td>
<td align="right">7,086,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,436,160</td>
<td align="right">2,436,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">1,425,180</td>
<td align="right">1,425,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,211,860</td>
<td align="right">1,211,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">540,600</td>
<td align="right">540,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">289,260</td>
<td align="right">289,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">289,260</td>
<td align="right">289,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">289,260</td>
<td align="right">289,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">289,260</td>
<td align="right">289,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">219,720</td>
<td align="right">219,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">219,600</td>
<td align="right">219,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">219,540</td>
<td align="right">219,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">219,540</td>
<td align="right">219,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">219,540</td>
<td align="right">219,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">660</td>
<td align="right">660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">580</td>
<td align="right">580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
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
<td align="left">LIST_EXTEND</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
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
<td align="right">64,138,860</td>
<td align="right">16.4%</td>
<td align="right">65,559,540</td>
<td align="right">16.7%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">328,080,360</td>
<td align="right">83.6%</td>
<td align="right">328,080,360</td>
<td align="right">83.3%</td>
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
<td align="right">15,840</td>
<td align="right">100.0%</td>
<td align="right">16,140</td>
<td align="right">100.0%</td>
<td align="right">1.9%</td>
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
<td align="left">multiply other</td>
<td align="right">60</td>
<td align="right">0.4%</td>
<td align="right">140</td>
<td align="right">0.9%</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">80</td>
<td align="right">0.5%</td>
<td align="right">120</td>
<td align="right">0.7%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">120</td>
<td align="right">0.8%</td>
<td align="right">80</td>
<td align="right">0.5%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">920</td>
<td align="right">5.8%</td>
<td align="right">1,080</td>
<td align="right">6.7%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">14,300</td>
<td align="right">90.3%</td>
<td align="right">14,360</td>
<td align="right">89.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">300</td>
<td align="right">1.9%</td>
<td align="right">300</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">60</td>
<td align="right">0.4%</td>
<td align="right">60</td>
<td align="right">0.4%</td>
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
<td align="right">51,137,100</td>
<td align="right">38.8%</td>
<td align="right">52,115,740</td>
<td align="right">39.2%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">80,670,360</td>
<td align="right">61.2%</td>
<td align="right">80,670,360</td>
<td align="right">60.7%</td>
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
<td align="right">12,640</td>
<td align="right">99.8%</td>
<td align="right">12,920</td>
<td align="right">99.8%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
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
<td align="left">buffer int</td>
<td align="right">220</td>
<td align="right">1.7%</td>
<td align="right">300</td>
<td align="right">2.3%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,420</td>
<td align="right">98.3%</td>
<td align="right">12,620</td>
<td align="right">97.7%</td>
<td align="right">1.6%</td>
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
<td align="right">320,680,740</td>
<td align="right">99.4%</td>
<td align="right">320,680,740</td>
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
<td align="right">1,936,900</td>
<td align="right">0.6%</td>
<td align="right">1,936,900</td>
<td align="right">0.6%</td>
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
<td align="right">37,180</td>
<td align="right">100.0%</td>
<td align="right">37,180</td>
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
<td align="right">219,540</td>
<td align="right">0.2%</td>
<td align="right">941,040</td>
<td align="right">0.9%</td>
<td align="right">328.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">99,141,480</td>
<td align="right">99.8%</td>
<td align="right">99,141,480</td>
<td align="right">99.1%</td>
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
<td align="right">80</td>
<td align="right">80.0%</td>
<td align="right">240</td>
<td align="right">92.3%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">20.0%</td>
<td align="right">20</td>
<td align="right">7.7%</td>
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
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">240</td>
<td align="right">100.0%</td>
<td align="right">200.0%</td>
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
<td align="right">33,755,700</td>
<td align="right">100.0%</td>
<td align="right">33,755,700</td>
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
<td align="right">1,199,500</td>
<td align="right">2.5%</td>
<td align="right">3,247,840</td>
<td align="right">6.3%</td>
<td align="right">170.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,840</td>
<td align="right">0.1%</td>
<td align="right">121,820</td>
<td align="right">0.2%</td>
<td align="right">144.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,646,600</td>
<td align="right">97.4%</td>
<td align="right">48,390,040</td>
<td align="right">93.5%</td>
<td align="right">1.6%</td>
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
<td align="right">940</td>
<td align="right">72.3%</td>
<td align="right">2,300</td>
<td align="right">74.2%</td>
<td align="right">144.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">360</td>
<td align="right">27.7%</td>
<td align="right">800</td>
<td align="right">25.8%</td>
<td align="right">122.2%</td>
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
<td align="right">280</td>
<td align="right">77.8%</td>
<td align="right">740</td>
<td align="right">92.5%</td>
<td align="right">164.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">80</td>
<td align="right">22.2%</td>
<td align="right">60</td>
<td align="right">7.5%</td>
<td align="right">-25.0%</td>
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
<td align="right">30,323,320</td>
<td align="right">10.9%</td>
<td align="right">33,337,180</td>
<td align="right">11.9%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">247,476,020</td>
<td align="right">89.1%</td>
<td align="right">247,476,020</td>
<td align="right">88.1%</td>
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
<td align="right">59,360</td>
<td align="right">0.0%</td>
<td align="right">59,360</td>
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
<td align="left">Failure</td>
<td align="right">10,360</td>
<td align="right">86.8%</td>
<td align="right">11,120</td>
<td align="right">87.6%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,580</td>
<td align="right">13.2%</td>
<td align="right">1,580</td>
<td align="right">12.4%</td>
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
<td align="right">0.4%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,660</td>
<td align="right">45.0%</td>
<td align="right">5,460</td>
<td align="right">49.1%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">5,620</td>
<td align="right">54.2%</td>
<td align="right">5,620</td>
<td align="right">50.5%</td>
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
<td align="right">224,554,080</td>
<td align="right">100.0%</td>
<td align="right">226,306,260</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
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
<td align="right">580</td>
<td align="right">100.0%</td>
<td align="right">580</td>
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
<td align="right">30,039,300</td>
<td align="right">100.0%</td>
<td align="right">30,039,300</td>
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
<td align="right">60,078,960</td>
<td align="right">100.0%</td>
<td align="right">60,078,960</td>
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
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">120</td>
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
<td align="right">3,757,260</td>
<td align="right">92.8%</td>
<td align="right">4,464,580</td>
<td align="right">93.9%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">289,260</td>
<td align="right">7.1%</td>
<td align="right">289,260</td>
<td align="right">6.1%</td>
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
<td align="right">1,120</td>
<td align="right">100.0%</td>
<td align="right">1,200</td>
<td align="right">100.0%</td>
<td align="right">7.1%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">1,120</td>
<td align="right">100.0%</td>
<td align="right">1,200</td>
<td align="right">100.0%</td>
<td align="right">7.1%</td>
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
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">4,680</td>
<td align="right">0.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">27,769,320</td>
<td align="right">100.0%</td>
<td align="right">27,769,320</td>
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
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">20</td>
<td align="right">50.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">20</td>
<td align="right">50.0%</td>
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
<td align="right">20</td>
<td align="right">50.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">50.0%</td>
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
<td align="right">220,937,100</td>
<td align="right">100.0%</td>
<td align="right">220,937,100</td>
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
<td align="right">150,822,640</td>
<td align="right">3.7%</td>
<td align="right">159,715,020</td>
<td align="right">3.9%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">2,046,420</td>
<td align="right">0.1%</td>
<td align="right">2,118,300</td>
<td align="right">0.1%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,622,161,040</td>
<td align="right">64.9%</td>
<td align="right">2,667,693,840</td>
<td align="right">64.8%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,264,410,900</td>
<td align="right">31.3%</td>
<td align="right">1,285,041,520</td>
<td align="right">31.2%</td>
<td align="right">1.6%</td>
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
<td align="right">219,540</td>
<td align="right">0.1%</td>
<td align="right">941,040</td>
<td align="right">0.6%</td>
<td align="right">328.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,199,500</td>
<td align="right">0.8%</td>
<td align="right">3,247,840</td>
<td align="right">2.0%</td>
<td align="right">170.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">3,757,260</td>
<td align="right">2.5%</td>
<td align="right">4,464,580</td>
<td align="right">2.8%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,323,320</td>
<td align="right">20.1%</td>
<td align="right">33,337,180</td>
<td align="right">20.9%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">64,138,860</td>
<td align="right">42.5%</td>
<td align="right">65,559,540</td>
<td align="right">41.1%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">51,137,100</td>
<td align="right">33.9%</td>
<td align="right">52,115,740</td>
<td align="right">32.6%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">4,680</td>
<td align="right">0.0%</td>
<td align="right">0.9%</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">24,520</td>
<td align="right">1.2%</td>
<td align="right">60,640</td>
<td align="right">2.9%</td>
<td align="right">147.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">25,320</td>
<td align="right">1.2%</td>
<td align="right">61,180</td>
<td align="right">2.9%</td>
<td align="right">141.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,265,640</td>
<td align="right">61.8%</td>
<td align="right">1,265,640</td>
<td align="right">59.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">671,260</td>
<td align="right">32.8%</td>
<td align="right">671,260</td>
<td align="right">31.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">38,160</td>
<td align="right">1.9%</td>
<td align="right">38,160</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,200</td>
<td align="right">1.0%</td>
<td align="right">21,200</td>
<td align="right">1.0%</td>
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
<td align="left">CHECK_EXC_MATCH</td>
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
<td align="right">326,917,840</td>
<td align="right">67.7%</td>
<td align="right">326,917,840</td>
<td align="right">67.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">155,887,460</td>
<td align="right">32.3%</td>
<td align="right">155,887,460</td>
<td align="right">32.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">326,917,840</td>
<td align="right">67.7%</td>
<td align="right">326,917,840</td>
<td align="right">67.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">36,421,540</td>
<td align="right">7.5%</td>
<td align="right">36,421,540</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">290,496,300</td>
<td align="right">60.2%</td>
<td align="right">290,496,300</td>
<td align="right">60.2%</td>
<td align="right">0.0%</td>
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
<td align="right">36,421,540</td>
<td align="right">7.5%</td>
<td align="right">36,421,540</td>
<td align="right">7.5%</td>
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
<td align="right">25,583,760</td>
<td align="right">5.3%</td>
<td align="right">25,583,760</td>
<td align="right">5.3%</td>
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
<td align="right">1,667,020</td>
<td align="right">0.3%</td>
<td align="right">1,667,020</td>
<td align="right">0.3%</td>
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
<td align="right">289,260</td>
<td align="right">0.1%</td>
<td align="right">289,260</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">192,309,060</td>
<td align="right">39.8%</td>
<td align="right">192,309,060</td>
<td align="right">39.8%</td>
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
<td align="left">Method cache misses</td>
<td align="right">197,320</td>
<td align="right"></td>
<td align="right">153,422</td>
<td align="right"></td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">350,890</td>
<td align="right"></td>
<td align="right">285,031</td>
<td align="right"></td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">153,586</td>
<td align="right"></td>
<td align="right">131,622</td>
<td align="right"></td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">825,029,700</td>
<td align="right">9.0%</td>
<td align="right">839,089,820</td>
<td align="right">9.2%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,815,186,980</td>
<td align="right">24.8%</td>
<td align="right">1,845,323,560</td>
<td align="right">25.2%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,352,812,140</td>
<td align="right">25.7%</td>
<td align="right">2,381,678,060</td>
<td align="right">26.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">4,107,723,063</td>
<td align="right">56.1%</td>
<td align="right">4,063,907,761</td>
<td align="right">55.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">4,305,192,407</td>
<td align="right">47.0%</td>
<td align="right">4,262,645,947</td>
<td align="right">46.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,668,665,465</td>
<td align="right">18.2%</td>
<td align="right">1,653,282,661</td>
<td align="right">18.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">645,254,980</td>
<td align="right">8.8%</td>
<td align="right">650,634,440</td>
<td align="right">8.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">756,567,489</td>
<td align="right">10.3%</td>
<td align="right">751,970,467</td>
<td align="right">10.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">456,420</td>
<td align="right">0.1%</td>
<td align="right">455,560</td>
<td align="right">0.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">76,572,560</td>
<td align="right"></td>
<td align="right">76,617,218</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">53,250,974</td>
<td align="right"></td>
<td align="right">53,273,218</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">359,582,384</td>
<td align="right"></td>
<td align="right">359,580,586</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">358,922,860</td>
<td align="right">48.4%</td>
<td align="right">358,921,600</td>
<td align="right">48.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">358,464,820</td>
<td align="right">48.4%</td>
<td align="right">358,464,420</td>
<td align="right">48.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">382,388,200</td>
<td align="right">51.6%</td>
<td align="right">382,388,100</td>
<td align="right">51.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">382,388,220</td>
<td align="right"></td>
<td align="right">382,388,120</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">1,620</td>
<td align="right">0.0%</td>
<td align="right">1,620</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">60</td>
<td align="right"></td>
<td align="right">60</td>
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
<td align="right">2,280</td>
<td align="right">160</td>
<td align="right">56,510,700</td>
<td align="right">2,280</td>
<td align="right">160</td>
<td align="right">56,505,860</td>
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
<td align="right">60</td>
<td align="right">0.1%</td>
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
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">3,960</td>
<td align="right">5.6%</td>
<td align="right">2,700</td>
<td align="right">4.0%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">71,000</td>
<td align="right"></td>
<td align="right">67,780</td>
<td align="right"></td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">329,823,660</td>
<td align="right"></td>
<td align="right">317,469,040</td>
<td align="right"></td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">67,040</td>
<td align="right">94.4%</td>
<td align="right">65,080</td>
<td align="right">96.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">67,760</td>
<td align="right">95.4%</td>
<td align="right">66,160</td>
<td align="right">97.6%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">9,683,443,380</td>
<td align="right">2,935.9%</td>
<td align="right">9,518,348,640</td>
<td align="right">2,998.2%</td>
<td align="right">-1.7%</td>
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
<td align="right">3,960</td>
<td align="right"></td>
<td align="right">2,700</td>
<td align="right"></td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">3,960</td>
<td align="right">100.0%</td>
<td align="right">2,700</td>
<td align="right">100.0%</td>
<td align="right">-31.8%</td>
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
<td align="right">720</td>
<td align="right">18.2%</td>
<td align="right">520</td>
<td align="right">19.3%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">420</td>
<td align="right">10.6%</td>
<td align="right">280</td>
<td align="right">10.4%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">780</td>
<td align="right">19.7%</td>
<td align="right">560</td>
<td align="right">20.7%</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,020</td>
<td align="right">25.8%</td>
<td align="right">520</td>
<td align="right">19.3%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">4.5%</td>
<td align="right">180</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">720</td>
<td align="right">18.2%</td>
<td align="right">640</td>
<td align="right">23.7%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">120</td>
<td align="right">3.0%</td>
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
<td align="right">120</td>
<td align="right">3.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">840</td>
<td align="right">21.2%</td>
<td align="right">680</td>
<td align="right">25.2%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">440</td>
<td align="right">11.1%</td>
<td align="right">240</td>
<td align="right">8.9%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">700</td>
<td align="right">17.7%</td>
<td align="right">620</td>
<td align="right">23.0%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">960</td>
<td align="right">24.2%</td>
<td align="right">460</td>
<td align="right">17.0%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">540</td>
<td align="right">13.6%</td>
<td align="right">340</td>
<td align="right">12.6%</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">300</td>
<td align="right">7.6%</td>
<td align="right">360</td>
<td align="right">13.3%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">60</td>
<td align="right">1.5%</td>
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
<td align="left">_LOAD_FAST_4</td>
<td align="right">1,018,500</td>
<td align="right">117,940</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">590,580</td>
<td align="right">79,200</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,117,980</td>
<td align="right">264,600</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">986,100</td>
<td align="right">264,600</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">200</td>
<td align="right">60</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">6,744,840</td>
<td align="right">11,318,180</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">289,200</td>
<td align="right">109,300</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">6,660</td>
<td align="right">2,880</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">6,660</td>
<td align="right">2,880</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,979,100</td>
<td align="right">2,224,300</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,103,600</td>
<td align="right">943,860</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,596,500</td>
<td align="right">1,181,720</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">361,020</td>
<td align="right">171,400</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">1,917,600</td>
<td align="right">957,920</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">571,020</td>
<td align="right">300,860</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">1,603,380</td>
<td align="right">873,360</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,634,460</td>
<td align="right">943,860</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,634,520</td>
<td align="right">943,900</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">1,622,700</td>
<td align="right">1,021,300</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">1,979,420</td>
<td align="right">1,269,980</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">5,706,600</td>
<td align="right">3,949,780</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">1,194,160</td>
<td align="right">836,840</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">7,517,500</td>
<td align="right">5,341,380</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,036,780</td>
<td align="right">4,461,160</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">4,379,200</td>
<td align="right">3,525,780</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">19,030,640</td>
<td align="right">16,016,780</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,456,060</td>
<td align="right">2,909,640</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">24,468,780</td>
<td align="right">20,620,420</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">71,700</td>
<td align="right">62,100</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">21,205,920</td>
<td align="right">18,557,220</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">87,547,820</td>
<td align="right">77,944,760</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">21,257,160</td>
<td align="right">19,153,760</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">28,722,420</td>
<td align="right">26,313,480</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">58,817,860</td>
<td align="right">54,020,440</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">30,889,540</td>
<td align="right">28,438,560</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">3,104,640</td>
<td align="right">2,906,820</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">61,275,600</td>
<td align="right">57,787,660</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">44,308,620</td>
<td align="right">41,865,240</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,550,540</td>
<td align="right">3,370,480</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,550,540</td>
<td align="right">3,370,480</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">30,987,780</td>
<td align="right">29,631,240</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">36,775,980</td>
<td align="right">35,181,460</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">6,446,920</td>
<td align="right">6,168,000</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">35,811,840</td>
<td align="right">34,391,160</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,393,100</td>
<td align="right">3,261,180</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,393,100</td>
<td align="right">3,261,180</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">329,823,660</td>
<td align="right">317,469,040</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">326,561,500</td>
<td align="right">314,452,860</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">35,890,740</td>
<td align="right">34,647,700</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">381,318,900</td>
<td align="right">369,891,680</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">17,304,060</td>
<td align="right">16,794,340</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">50,267,080</td>
<td align="right">48,821,700</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">76,634,100</td>
<td align="right">74,596,200</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">33,106,320</td>
<td align="right">32,273,460</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">17,080,680</td>
<td align="right">16,685,040</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">50,825,940</td>
<td align="right">49,686,880</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">2,972,760</td>
<td align="right">2,906,820</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">2,972,760</td>
<td align="right">2,906,820</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">2,972,760</td>
<td align="right">2,906,820</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">33,747,900</td>
<td align="right">33,016,440</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">210,886,620</td>
<td align="right">206,694,780</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">51,495,240</td>
<td align="right">52,422,640</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">57,351,160</td>
<td align="right">56,318,600</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">49,631,720</td>
<td align="right">48,740,480</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">10,072,980</td>
<td align="right">9,892,840</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">381,444,700</td>
<td align="right">375,907,320</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">30,030,220</td>
<td align="right">29,612,680</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">336,562,200</td>
<td align="right">331,914,120</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">187,480,860</td>
<td align="right">185,068,100</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">1,201,787,040</td>
<td align="right">1,187,010,780</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">103,804,840</td>
<td align="right">102,634,940</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">103,804,840</td>
<td align="right">102,634,940</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">113,355,180</td>
<td align="right">112,083,720</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">100,832,080</td>
<td align="right">99,728,120</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">100,832,080</td>
<td align="right">99,728,120</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">64,795,080</td>
<td align="right">64,087,760</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">1,076,034,680</td>
<td align="right">1,065,182,340</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">50,582,080</td>
<td align="right">50,150,540</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">47,167,200</td>
<td align="right">46,780,060</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">47,167,200</td>
<td align="right">46,780,060</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">47,167,200</td>
<td align="right">46,780,060</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">47,433,680</td>
<td align="right">47,076,460</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">47,097,300</td>
<td align="right">46,780,060</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">257,607,700</td>
<td align="right">255,901,020</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">47,090,400</td>
<td align="right">46,799,660</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">47,090,400</td>
<td align="right">46,799,660</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,031,660</td>
<td align="right">46,780,060</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">52,753,620</td>
<td align="right">52,484,400</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">193,411,440</td>
<td align="right">192,526,120</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">47,100,180</td>
<td align="right">46,891,200</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">16,750,980</td>
<td align="right">16,685,040</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">16,750,980</td>
<td align="right">16,685,040</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">17,190,060</td>
<td align="right">17,124,120</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">17,190,060</td>
<td align="right">17,124,120</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">260,194,200</td>
<td align="right">259,215,560</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">23,377,740</td>
<td align="right">23,338,260</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">196,410,340</td>
<td align="right">196,099,820</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">46,742,340</td>
<td align="right">46,670,760</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">46,742,160</td>
<td align="right">46,670,760</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">46,742,160</td>
<td align="right">46,670,760</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">23,371,080</td>
<td align="right">23,335,380</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">23,371,080</td>
<td align="right">23,335,380</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">23,371,080</td>
<td align="right">23,335,380</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">291,807,160</td>
<td align="right">291,386,340</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">50,003,380</td>
<td align="right">49,931,940</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">53,264,620</td>
<td align="right">53,193,180</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">189,271,280</td>
<td align="right">189,073,380</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">305,212,580</td>
<td align="right">305,023,620</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">3,480,760</td>
<td align="right">3,478,800</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">203,093,640</td>
<td align="right">203,044,560</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">244,170,980</td>
<td align="right">244,141,360</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">291,405,280</td>
<td align="right">291,386,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">3,261,220</td>
<td align="right">3,261,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">179,644,200</td>
<td align="right">179,644,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">2,906,820</td>
<td align="right">2,906,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">410,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">271,320</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">267,540</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">267,540</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">263,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">263,760</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">197,820</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">197,820</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">135,660</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">131,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">131,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">65,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">65,940</td>
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
<td align="right">720</td>
<td align="right">80</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180</td>
<td align="right">120</td>
<td align="right">-33.3%</td>
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
Stats gathered on: 2024-11-13
