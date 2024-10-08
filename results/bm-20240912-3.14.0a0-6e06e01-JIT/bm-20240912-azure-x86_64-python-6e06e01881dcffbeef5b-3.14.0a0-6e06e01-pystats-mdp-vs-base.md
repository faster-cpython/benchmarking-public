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
<td align="right">425,231,520</td>
<td align="right">8,640</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">45,007,540</td>
<td align="right">5,060</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">62,353,760</td>
<td align="right">12,440</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">31,185,860</td>
<td align="right">6,640</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">62,739,520</td>
<td align="right">15,720</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,179,400</td>
<td align="right">1,080</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">63,032,120</td>
<td align="right">216,800</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">771,640</td>
<td align="right">3,540</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">63,032,400</td>
<td align="right">305,900</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">62,832,560</td>
<td align="right">491,240</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">63,357,060</td>
<td align="right">544,960</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">33,170,240</td>
<td align="right">303,600</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">63,496,820</td>
<td align="right">587,420</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">91,427,380</td>
<td align="right">1,089,360</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">71,355,140</td>
<td align="right">993,460</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">23,417,720</td>
<td align="right">496,920</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">22,832,560</td>
<td align="right">497,200</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">105,800</td>
<td align="right">3,020</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">24,625,680</td>
<td align="right">883,920</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">65,797,360</td>
<td align="right">3,066,040</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">58,445,680</td>
<td align="right">2,805,580</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">74,571,360</td>
<td align="right">3,780,800</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">9,060</td>
<td align="right">500</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">61,701,120</td>
<td align="right">4,870,960</td>
<td align="right">-92.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,354,380</td>
<td align="right">388,680</td>
<td align="right">-91.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,356,100</td>
<td align="right">389,420</td>
<td align="right">-91.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,472,120</td>
<td align="right">293,720</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">44,235,220</td>
<td align="right">5,938,660</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">4,939,800</td>
<td align="right">681,540</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">451,408,680</td>
<td align="right">62,744,220</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">11,286,460</td>
<td align="right">1,603,780</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">281,242,200</td>
<td align="right">41,716,800</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">293,569,020</td>
<td align="right">43,597,560</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">415,213,780</td>
<td align="right">64,277,040</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,091,600</td>
<td align="right">535,560</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,609,580</td>
<td align="right">294,920</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">500,041,280</td>
<td align="right">94,939,700</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">13,320,640</td>
<td align="right">2,737,280</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,741,100</td>
<td align="right">575,280</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">164,962,020</td>
<td align="right">35,197,760</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">840,424,800</td>
<td align="right">254,662,000</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,682,680</td>
<td align="right">3,608,880</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">259,371,200</td>
<td align="right">84,392,800</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">5,776,000</td>
<td align="right">1,900,540</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,717,852,800</td>
<td align="right">621,287,500</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">877,380</td>
<td align="right">389,420</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">10,733,520</td>
<td align="right">5,275,560</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">141,718,960</td>
<td align="right">71,446,240</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">196,768,640</td>
<td align="right">104,649,260</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,222,260</td>
<td align="right">666,740</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">172,872,360</td>
<td align="right">100,725,860</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">99,779,880</td>
<td align="right">58,971,600</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">133,306,960</td>
<td align="right">81,641,940</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">193,172,620</td>
<td align="right">118,934,200</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">65,836,340</td>
<td align="right">41,190,380</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,013,360</td>
<td align="right">737,520</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">381,972,720</td>
<td align="right">295,054,660</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">120,190,340</td>
<td align="right">97,410,180</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">75,240,560</td>
<td align="right">64,518,660</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">580,906,520</td>
<td align="right">505,167,000</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">35,599,560</td>
<td align="right">30,987,300</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">720,800</td>
<td align="right">630,560</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,344,000</td>
<td align="right">30,993,120</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">100,104,320</td>
<td align="right">87,822,040</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">47,600,260</td>
<td align="right">43,366,400</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,171,520</td>
<td align="right">1,082,560</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,655,280</td>
<td align="right">1,566,320</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">172,251,160</td>
<td align="right">167,377,940</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">34,553,040</td>
<td align="right">34,192,080</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">388,963,560</td>
<td align="right">388,499,920</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9,457,360</td>
<td align="right">9,448,820</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">435,891,180</td>
<td align="right">435,891,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">324,495,840</td>
<td align="right">324,495,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">130,016,240</td>
<td align="right">130,016,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">80,104,680</td>
<td align="right">80,104,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">63,239,120</td>
<td align="right">63,239,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">58,829,240</td>
<td align="right">58,829,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">58,243,860</td>
<td align="right">58,243,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">40,052,360</td>
<td align="right">40,052,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">33,089,520</td>
<td align="right">33,089,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">10,113,040</td>
<td align="right">10,113,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,112,980</td>
<td align="right">10,112,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">9,448,480</td>
<td align="right">9,448,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,246,800</td>
<td align="right">3,246,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,615,560</td>
<td align="right">1,615,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">385,680</td>
<td align="right">385,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">385,680</td>
<td align="right">385,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">385,680</td>
<td align="right">385,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">385,660</td>
<td align="right">385,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">292,960</td>
<td align="right">292,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">292,800</td>
<td align="right">292,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">292,700</td>
<td align="right">292,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">292,700</td>
<td align="right">292,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">292,700</td>
<td align="right">292,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,060</td>
<td align="right">5,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4,340</td>
<td align="right">4,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,000</td>
<td align="right">1,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">680</td>
<td align="right">680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">480</td>
<td align="right">480</td>
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
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
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
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">327,387,160</td>
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
<td align="right">133,268,420</td>
<td align="right">23.3%</td>
<td align="right">81,616,040</td>
<td align="right">15.7%</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">437,439,660</td>
<td align="right">76.6%</td>
<td align="right">437,439,660</td>
<td align="right">84.3%</td>
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
<td align="right">37,720</td>
<td align="right">97.9%</td>
<td align="right">25,080</td>
<td align="right">96.8%</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">820</td>
<td align="right">2.1%</td>
<td align="right">820</td>
<td align="right">3.2%</td>
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
<td align="right">7,780</td>
<td align="right">20.6%</td>
<td align="right">1,020</td>
<td align="right">4.1%</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">580</td>
<td align="right">1.5%</td>
<td align="right">400</td>
<td align="right">1.6%</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">400</td>
<td align="right">1.1%</td>
<td align="right">280</td>
<td align="right">1.1%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">27,560</td>
<td align="right">73.1%</td>
<td align="right">22,060</td>
<td align="right">88.0%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">560</td>
<td align="right">1.5%</td>
<td align="right">480</td>
<td align="right">1.9%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">580</td>
<td align="right">1.5%</td>
<td align="right">580</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">260</td>
<td align="right">0.7%</td>
<td align="right">260</td>
<td align="right">1.0%</td>
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
<td align="right">415,108,760</td>
<td align="right">79.4%</td>
<td align="right">64,258,060</td>
<td align="right">37.4%</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">107,560,040</td>
<td align="right">20.6%</td>
<td align="right">107,560,040</td>
<td align="right">62.6%</td>
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
<td align="right">104,660</td>
<td align="right">99.7%</td>
<td align="right">18,620</td>
<td align="right">98.1%</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">360</td>
<td align="right">1.9%</td>
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
<td align="right">97,860</td>
<td align="right">93.5%</td>
<td align="right">17,400</td>
<td align="right">93.4%</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">6,800</td>
<td align="right">6.5%</td>
<td align="right">1,220</td>
<td align="right">6.6%</td>
<td align="right">-82.1%</td>
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
<td align="right">2,520</td>
<td align="right">0.0%</td>
<td align="right">2,520</td>
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
<td align="right">427,573,040</td>
<td align="right">99.4%</td>
<td align="right">427,573,040</td>
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
<td align="right">2,581,280</td>
<td align="right">0.6%</td>
<td align="right">2,581,280</td>
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
<td align="right">51,200</td>
<td align="right">100.0%</td>
<td align="right">51,200</td>
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
<td align="right">40</td>
<td align="right">50.0%</td>
<td align="right">40</td>
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
<td align="right">1,608,160</td>
<td align="right">1.2%</td>
<td align="right">293,820</td>
<td align="right">0.2%</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">132,188,000</td>
<td align="right">98.8%</td>
<td align="right">132,188,000</td>
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
<td align="left">Failure</td>
<td align="right">780</td>
<td align="right">54.9%</td>
<td align="right">460</td>
<td align="right">41.8%</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">640</td>
<td align="right">45.1%</td>
<td align="right">640</td>
<td align="right">58.2%</td>
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
<td align="right">780</td>
<td align="right">100.0%</td>
<td align="right">460</td>
<td align="right">100.0%</td>
<td align="right">-41.0%</td>
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
<td align="right">45,007,540</td>
<td align="right">100.0%</td>
<td align="right">45,007,540</td>
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
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">60</td>
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
<td align="right">477,092,840</td>
<td align="right">97.6%</td>
<td align="right">63,674,520</td>
<td align="right">97.3%</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11,282,080</td>
<td align="right">2.3%</td>
<td align="right">1,601,760</td>
<td align="right">2.4%</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">474,660</td>
<td align="right">0.1%</td>
<td align="right">141,900</td>
<td align="right">0.2%</td>
<td align="right">-70.1%</td>
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
<td align="right">9,180</td>
<td align="right">68.9%</td>
<td align="right">2,900</td>
<td align="right">62.0%</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,140</td>
<td align="right">31.1%</td>
<td align="right">1,780</td>
<td align="right">38.0%</td>
<td align="right">-57.0%</td>
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
<td align="right">3,680</td>
<td align="right">88.9%</td>
<td align="right">1,460</td>
<td align="right">82.0%</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">460</td>
<td align="right">11.1%</td>
<td align="right">320</td>
<td align="right">18.0%</td>
<td align="right">-30.4%</td>
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
<td align="right">65,808,160</td>
<td align="right">16.6%</td>
<td align="right">41,168,200</td>
<td align="right">11.1%</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">329,965,180</td>
<td align="right">83.3%</td>
<td align="right">329,965,180</td>
<td align="right">88.9%</td>
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
<td align="right">78,280</td>
<td align="right">0.0%</td>
<td align="right">78,280</td>
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
<td align="right">26,580</td>
<td align="right">89.7%</td>
<td align="right">20,580</td>
<td align="right">87.1%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,060</td>
<td align="right">10.3%</td>
<td align="right">3,060</td>
<td align="right">12.9%</td>
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
<td align="right">1,280</td>
<td align="right">4.8%</td>
<td align="right">300</td>
<td align="right">1.5%</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">15,420</td>
<td align="right">58.0%</td>
<td align="right">11,380</td>
<td align="right">55.3%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">8,620</td>
<td align="right">32.4%</td>
<td align="right">8,620</td>
<td align="right">41.9%</td>
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
<td align="right">345,123,520</td>
<td align="right">100.0%</td>
<td align="right">299,274,460</td>
<td align="right">100.0%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
<td align="right">2,160</td>
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
<td align="right">2,180</td>
<td align="right">100.0%</td>
<td align="right">2,180</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">40,052,360</td>
<td align="right">100.0%</td>
<td align="right">40,052,360</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
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
<td align="right">80,105,040</td>
<td align="right">100.0%</td>
<td align="right">80,105,040</td>
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
<td align="right">91,403,140</td>
<td align="right">99.6%</td>
<td align="right">1,087,600</td>
<td align="right">73.7%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">385,660</td>
<td align="right">0.4%</td>
<td align="right">385,660</td>
<td align="right">26.1%</td>
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
<td align="right">24,220</td>
<td align="right">99.9%</td>
<td align="right">1,740</td>
<td align="right">98.9%</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">1.1%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">24,220</td>
<td align="right">100.0%</td>
<td align="right">1,740</td>
<td align="right">100.0%</td>
<td align="right">-92.8%</td>
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
<td align="right">4,354,620</td>
<td align="right">10.5%</td>
<td align="right">388,920</td>
<td align="right">1.0%</td>
<td align="right">-91.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">37,025,460</td>
<td align="right">89.5%</td>
<td align="right">37,025,460</td>
<td align="right">99.0%</td>
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
<td align="right">1,260</td>
<td align="right">85.1%</td>
<td align="right">280</td>
<td align="right">56.0%</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">220</td>
<td align="right">14.9%</td>
<td align="right">220</td>
<td align="right">44.0%</td>
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
<td align="right">1,260</td>
<td align="right">100.0%</td>
<td align="right">280</td>
<td align="right">100.0%</td>
<td align="right">-77.8%</td>
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
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">340</td>
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
<td align="right">294,582,380</td>
<td align="right">100.0%</td>
<td align="right">294,582,380</td>
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
<td align="right">340</td>
<td align="right">100.0%</td>
<td align="right">340</td>
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
<td align="right">723,047,440</td>
<td align="right">6.7%</td>
<td align="right">190,497,680</td>
<td align="right">3.6%</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">3,351,910,240</td>
<td align="right">31.1%</td>
<td align="right">1,687,637,180</td>
<td align="right">32.0%</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">6,693,090,420</td>
<td align="right">62.1%</td>
<td align="right">3,393,469,820</td>
<td align="right">64.3%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">3,134,560</td>
<td align="right">0.0%</td>
<td align="right">2,801,820</td>
<td align="right">0.1%</td>
<td align="right">-10.6%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">91,403,140</td>
<td align="right">12.6%</td>
<td align="right">1,087,600</td>
<td align="right">0.6%</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">4,354,620</td>
<td align="right">0.6%</td>
<td align="right">388,920</td>
<td align="right">0.2%</td>
<td align="right">-91.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">11,282,080</td>
<td align="right">1.6%</td>
<td align="right">1,601,760</td>
<td align="right">0.8%</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">415,108,760</td>
<td align="right">57.4%</td>
<td align="right">64,258,060</td>
<td align="right">33.7%</td>
<td align="right">-84.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,608,160</td>
<td align="right">0.2%</td>
<td align="right">293,820</td>
<td align="right">0.2%</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">133,268,420</td>
<td align="right">18.4%</td>
<td align="right">81,616,040</td>
<td align="right">42.9%</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">65,808,160</td>
<td align="right">9.1%</td>
<td align="right">41,168,200</td>
<td align="right">21.6%</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,520</td>
<td align="right">0.0%</td>
<td align="right">2,520</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">340</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">237,220</td>
<td align="right">7.6%</td>
<td align="right">70,880</td>
<td align="right">2.5%</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">237,440</td>
<td align="right">7.6%</td>
<td align="right">71,020</td>
<td align="right">2.5%</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,686,380</td>
<td align="right">53.8%</td>
<td align="right">1,686,380</td>
<td align="right">60.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">894,900</td>
<td align="right">28.5%</td>
<td align="right">894,900</td>
<td align="right">31.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">50,720</td>
<td align="right">1.6%</td>
<td align="right">50,720</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">27,560</td>
<td align="right">0.9%</td>
<td align="right">27,560</td>
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
<td align="right">435,891,180</td>
<td align="right">67.7%</td>
<td align="right">435,891,180</td>
<td align="right">67.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">207,848,900</td>
<td align="right">32.3%</td>
<td align="right">207,848,900</td>
<td align="right">32.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">435,891,180</td>
<td align="right">67.7%</td>
<td align="right">435,891,180</td>
<td align="right">67.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">48,562,780</td>
<td align="right">7.5%</td>
<td align="right">48,562,780</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">387,328,400</td>
<td align="right">60.2%</td>
<td align="right">387,328,400</td>
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
<td align="right">48,562,780</td>
<td align="right">7.5%</td>
<td align="right">48,562,780</td>
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
<td align="right">34,111,680</td>
<td align="right">5.3%</td>
<td align="right">34,111,680</td>
<td align="right">5.3%</td>
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
<td align="right">2,223,400</td>
<td align="right">0.3%</td>
<td align="right">2,223,400</td>
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
<td align="right">385,680</td>
<td align="right">0.1%</td>
<td align="right">385,680</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">256,411,740</td>
<td align="right">39.8%</td>
<td align="right">256,411,740</td>
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
<td align="left">Decrefs</td>
<td align="right">2,025,198,136</td>
<td align="right">25.4%</td>
<td align="right">5,609,494,978</td>
<td align="right">64.2%</td>
<td align="right">177.0%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">1,982,406,113</td>
<td align="right">28.3%</td>
<td align="right">5,354,650,372</td>
<td align="right">69.1%</td>
<td align="right">170.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,354,453</td>
<td align="right"></td>
<td align="right">29,915</td>
<td align="right"></td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,533,268</td>
<td align="right"></td>
<td align="right">64,656</td>
<td align="right"></td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">179,388</td>
<td align="right"></td>
<td align="right">35,295</td>
<td align="right"></td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">5,018,406,320</td>
<td align="right">71.7%</td>
<td align="right">2,399,414,320</td>
<td align="right">30.9%</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">5,955,737,700</td>
<td align="right">74.6%</td>
<td align="right">3,124,690,480</td>
<td align="right">35.8%</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">68,939,827</td>
<td align="right"></td>
<td align="right">71,178,325</td>
<td align="right"></td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
<td align="right">1,960</td>
<td align="right">0.0%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">605,200</td>
<td align="right">0.1%</td>
<td align="right">606,140</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">102,197,632</td>
<td align="right"></td>
<td align="right">102,335,725</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">478,679,620</td>
<td align="right">48.4%</td>
<td align="right">478,681,140</td>
<td align="right">48.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">479,399,390</td>
<td align="right"></td>
<td align="right">479,398,176</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">478,072,500</td>
<td align="right">48.4%</td>
<td align="right">478,073,040</td>
<td align="right">48.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">509,887,540</td>
<td align="right"></td>
<td align="right">509,887,100</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">509,725,340</td>
<td align="right">51.6%</td>
<td align="right">509,725,160</td>
<td align="right">51.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">80</td>
<td align="right"></td>
<td align="right">80</td>
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
<td align="right">3,120</td>
<td align="right">2,400</td>
<td align="right">73,455,140</td>
<td align="right">3,120</td>
<td align="right">1,920</td>
<td align="right">73,409,420</td>
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
