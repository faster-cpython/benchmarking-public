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
<td align="right">8,640</td>
<td align="right">110,072,840</td>
<td align="right">1,273,891.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">5,060</td>
<td align="right">35,951,200</td>
<td align="right">710,398.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">12,440</td>
<td align="right">50,180,820</td>
<td align="right">403,282.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">6,640</td>
<td align="right">25,100,020</td>
<td align="right">377,912.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">15,720</td>
<td align="right">50,567,400</td>
<td align="right">321,575.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,080</td>
<td align="right">2,159,240</td>
<td align="right">199,829.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">216,800</td>
<td align="right">50,859,800</td>
<td align="right">23,359.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">3,540</td>
<td align="right">767,480</td>
<td align="right">21,580.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">305,900</td>
<td align="right">50,855,300</td>
<td align="right">16,524.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">491,240</td>
<td align="right">50,660,920</td>
<td align="right">10,212.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">544,960</td>
<td align="right">51,184,860</td>
<td align="right">9,292.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">303,600</td>
<td align="right">27,059,000</td>
<td align="right">8,812.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">587,420</td>
<td align="right">51,322,020</td>
<td align="right">8,636.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,089,360</td>
<td align="right">78,574,140</td>
<td align="right">7,112.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">993,460</td>
<td align="right">59,005,080</td>
<td align="right">5,839.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">3,020</td>
<td align="right">99,560</td>
<td align="right">3,196.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,805,580</td>
<td align="right">57,107,320</td>
<td align="right">1,935.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">500</td>
<td align="right">9,040</td>
<td align="right">1,708.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,066,040</td>
<td align="right">53,619,080</td>
<td align="right">1,648.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,780,800</td>
<td align="right">62,198,420</td>
<td align="right">1,545.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,870,960</td>
<td align="right">59,802,240</td>
<td align="right">1,127.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">388,680</td>
<td align="right">4,265,220</td>
<td align="right">997.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">389,420</td>
<td align="right">4,266,920</td>
<td align="right">995.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">293,720</td>
<td align="right">2,451,960</td>
<td align="right">734.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">681,540</td>
<td align="right">4,844,080</td>
<td align="right">610.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,603,780</td>
<td align="right">11,045,660</td>
<td align="right">588.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">5,938,660</td>
<td align="right">37,462,200</td>
<td align="right">530.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">535,560</td>
<td align="right">3,028,120</td>
<td align="right">465.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">294,920</td>
<td align="right">1,583,960</td>
<td align="right">437.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">575,280</td>
<td align="right">2,683,500</td>
<td align="right">366.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,737,280</td>
<td align="right">12,444,060</td>
<td align="right">354.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">35,197,760</td>
<td align="right">140,524,320</td>
<td align="right">299.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,608,880</td>
<td align="right">11,554,640</td>
<td align="right">220.2%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">1,900,540</td>
<td align="right">5,686,840</td>
<td align="right">199.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">883,920</td>
<td align="right">2,346,480</td>
<td align="right">165.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">62,744,220</td>
<td align="right">159,344,460</td>
<td align="right">154.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">64,277,040</td>
<td align="right">162,167,240</td>
<td align="right">152.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">84,392,800</td>
<td align="right">211,201,600</td>
<td align="right">150.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">94,939,700</td>
<td align="right">235,092,980</td>
<td align="right">147.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">389,420</td>
<td align="right">866,980</td>
<td align="right">122.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,275,560</td>
<td align="right">10,618,640</td>
<td align="right">101.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">666,740</td>
<td align="right">1,217,020</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">71,446,240</td>
<td align="right">129,369,000</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">621,287,500</td>
<td align="right">1,121,937,420</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">104,649,260</td>
<td align="right">180,838,600</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">100,725,860</td>
<td align="right">160,488,720</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">41,190,380</td>
<td align="right">65,303,800</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">58,971,600</td>
<td align="right">93,011,800</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">118,934,200</td>
<td align="right">180,733,500</td>
<td align="right">52.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">254,662,000</td>
<td align="right">350,205,640</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">737,520</td>
<td align="right">1,012,620</td>
<td align="right">37.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">81,641,940</td>
<td align="right">110,355,560</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">295,054,660</td>
<td align="right">371,939,040</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">43,597,560</td>
<td align="right">53,822,460</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">496,920</td>
<td align="right">585,820</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">497,200</td>
<td align="right">586,100</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">64,518,660</td>
<td align="right">75,018,660</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">30,987,300</td>
<td align="right">35,505,400</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">630,560</td>
<td align="right">720,800</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">30,993,120</td>
<td align="right">35,250,680</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">87,822,040</td>
<td align="right">99,832,680</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">327,387,160</td>
<td align="right">285,412,380</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">505,167,000</td>
<td align="right">568,459,280</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">43,366,400</td>
<td align="right">47,510,900</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,082,560</td>
<td align="right">1,171,460</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,566,320</td>
<td align="right">1,655,220</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">167,377,940</td>
<td align="right">172,159,500</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">34,192,080</td>
<td align="right">34,552,440</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">97,410,180</td>
<td align="right">97,943,420</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">388,499,920</td>
<td align="right">389,401,120</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">9,448,820</td>
<td align="right">9,457,340</td>
<td align="right">0.1%</td>
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
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">41,716,800</td>
<td align="right">41,716,800</td>
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
<td align="right">81,616,040</td>
<td align="right">15.7%</td>
<td align="right">110,322,580</td>
<td align="right">20.1%</td>
<td align="right">35.2%</td>
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
<td align="right">84.3%</td>
<td align="right">437,439,660</td>
<td align="right">79.9%</td>
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
<td align="right">25,080</td>
<td align="right">96.8%</td>
<td align="right">32,160</td>
<td align="right">97.5%</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">820</td>
<td align="right">3.2%</td>
<td align="right">820</td>
<td align="right">2.5%</td>
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
<td align="right">1,020</td>
<td align="right">4.1%</td>
<td align="right">7,640</td>
<td align="right">23.8%</td>
<td align="right">649.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">400</td>
<td align="right">1.6%</td>
<td align="right">580</td>
<td align="right">1.8%</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">280</td>
<td align="right">1.1%</td>
<td align="right">400</td>
<td align="right">1.2%</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">480</td>
<td align="right">1.9%</td>
<td align="right">560</td>
<td align="right">1.7%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">22,060</td>
<td align="right">88.0%</td>
<td align="right">22,140</td>
<td align="right">68.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">580</td>
<td align="right">2.3%</td>
<td align="right">580</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">260</td>
<td align="right">1.0%</td>
<td align="right">260</td>
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
<td align="right">64,258,060</td>
<td align="right">37.4%</td>
<td align="right">162,123,920</td>
<td align="right">60.1%</td>
<td align="right">152.3%</td>
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
<td align="right">62.6%</td>
<td align="right">107,560,040</td>
<td align="right">39.9%</td>
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
<td align="right">18,620</td>
<td align="right">98.1%</td>
<td align="right">42,960</td>
<td align="right">99.2%</td>
<td align="right">130.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">360</td>
<td align="right">1.9%</td>
<td align="right">360</td>
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
<td align="left">buffer int</td>
<td align="right">1,220</td>
<td align="right">6.6%</td>
<td align="right">6,680</td>
<td align="right">15.5%</td>
<td align="right">447.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,400</td>
<td align="right">93.4%</td>
<td align="right">36,280</td>
<td align="right">84.5%</td>
<td align="right">108.5%</td>
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
<td align="right">293,820</td>
<td align="right">0.2%</td>
<td align="right">1,582,560</td>
<td align="right">1.2%</td>
<td align="right">438.6%</td>
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
<td align="right">99.8%</td>
<td align="right">132,188,000</td>
<td align="right">98.8%</td>
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
<td align="right">460</td>
<td align="right">41.8%</td>
<td align="right">760</td>
<td align="right">54.3%</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">640</td>
<td align="right">58.2%</td>
<td align="right">640</td>
<td align="right">45.7%</td>
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
<td align="right">100.0%</td>
<td align="right">760</td>
<td align="right">100.0%</td>
<td align="right">65.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,601,760</td>
<td align="right">2.4%</td>
<td align="right">11,041,340</td>
<td align="right">6.4%</td>
<td align="right">589.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">141,900</td>
<td align="right">0.2%</td>
<td align="right">474,660</td>
<td align="right">0.3%</td>
<td align="right">234.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">63,674,520</td>
<td align="right">97.3%</td>
<td align="right">162,139,120</td>
<td align="right">93.4%</td>
<td align="right">154.6%</td>
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
<td align="right">2,900</td>
<td align="right">62.0%</td>
<td align="right">9,180</td>
<td align="right">69.2%</td>
<td align="right">216.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,780</td>
<td align="right">38.0%</td>
<td align="right">4,080</td>
<td align="right">30.8%</td>
<td align="right">129.2%</td>
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
<td align="right">1,460</td>
<td align="right">82.0%</td>
<td align="right">3,620</td>
<td align="right">88.7%</td>
<td align="right">147.9%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">320</td>
<td align="right">18.0%</td>
<td align="right">460</td>
<td align="right">11.3%</td>
<td align="right">43.8%</td>
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
<td align="right">41,168,200</td>
<td align="right">11.1%</td>
<td align="right">65,275,720</td>
<td align="right">16.5%</td>
<td align="right">58.6%</td>
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
<td align="right">88.9%</td>
<td align="right">329,965,180</td>
<td align="right">83.5%</td>
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
<td align="right">20,580</td>
<td align="right">87.1%</td>
<td align="right">26,480</td>
<td align="right">89.6%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,060</td>
<td align="right">12.9%</td>
<td align="right">3,060</td>
<td align="right">10.4%</td>
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
<td align="right">300</td>
<td align="right">1.5%</td>
<td align="right">1,260</td>
<td align="right">4.8%</td>
<td align="right">320.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">11,380</td>
<td align="right">55.3%</td>
<td align="right">15,360</td>
<td align="right">58.0%</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">8,620</td>
<td align="right">41.9%</td>
<td align="right">8,620</td>
<td align="right">32.6%</td>
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
<td align="right">299,274,460</td>
<td align="right">100.0%</td>
<td align="right">338,734,040</td>
<td align="right">100.0%</td>
<td align="right">13.2%</td>
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
<td align="right">1,087,600</td>
<td align="right">73.7%</td>
<td align="right">78,552,960</td>
<td align="right">99.5%</td>
<td align="right">7,122.6%</td>
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
<td align="right">26.1%</td>
<td align="right">385,660</td>
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
<td align="right">1,740</td>
<td align="right">98.9%</td>
<td align="right">21,160</td>
<td align="right">99.9%</td>
<td align="right">1,116.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">1.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">1,740</td>
<td align="right">100.0%</td>
<td align="right">21,160</td>
<td align="right">100.0%</td>
<td align="right">1,116.1%</td>
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
<td align="right">388,920</td>
<td align="right">1.0%</td>
<td align="right">4,265,460</td>
<td align="right">10.3%</td>
<td align="right">996.7%</td>
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
<td align="right">99.0%</td>
<td align="right">37,025,460</td>
<td align="right">89.7%</td>
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
<td align="right">280</td>
<td align="right">56.0%</td>
<td align="right">1,240</td>
<td align="right">84.9%</td>
<td align="right">342.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">220</td>
<td align="right">44.0%</td>
<td align="right">220</td>
<td align="right">15.1%</td>
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
<td align="right">280</td>
<td align="right">100.0%</td>
<td align="right">1,240</td>
<td align="right">100.0%</td>
<td align="right">342.9%</td>
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
<td align="right">190,497,680</td>
<td align="right">3.6%</td>
<td align="right">433,308,120</td>
<td align="right">5.5%</td>
<td align="right">127.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,393,469,820</td>
<td align="right">64.3%</td>
<td align="right">5,085,134,380</td>
<td align="right">64.1%</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,687,637,180</td>
<td align="right">32.0%</td>
<td align="right">2,407,748,200</td>
<td align="right">30.4%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">2,801,820</td>
<td align="right">0.1%</td>
<td align="right">3,138,740</td>
<td align="right">0.0%</td>
<td align="right">12.0%</td>
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
<td align="right">1,087,600</td>
<td align="right">0.6%</td>
<td align="right">78,552,960</td>
<td align="right">18.1%</td>
<td align="right">7,122.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">388,920</td>
<td align="right">0.2%</td>
<td align="right">4,265,460</td>
<td align="right">1.0%</td>
<td align="right">996.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,601,760</td>
<td align="right">0.8%</td>
<td align="right">11,041,340</td>
<td align="right">2.5%</td>
<td align="right">589.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">293,820</td>
<td align="right">0.2%</td>
<td align="right">1,582,560</td>
<td align="right">0.4%</td>
<td align="right">438.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">64,258,060</td>
<td align="right">33.7%</td>
<td align="right">162,123,920</td>
<td align="right">37.4%</td>
<td align="right">152.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">41,168,200</td>
<td align="right">21.6%</td>
<td align="right">65,275,720</td>
<td align="right">15.1%</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">81,616,040</td>
<td align="right">42.9%</td>
<td align="right">110,322,580</td>
<td align="right">25.5%</td>
<td align="right">35.2%</td>
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
<td align="left">RESUME</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">4,520</td>
<td align="right">0.1%</td>
<td align="right">1,155.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">4,520</td>
<td align="right">0.1%</td>
<td align="right">1,155.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">70,880</td>
<td align="right">2.5%</td>
<td align="right">237,220</td>
<td align="right">7.5%</td>
<td align="right">234.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">71,020</td>
<td align="right">2.5%</td>
<td align="right">237,440</td>
<td align="right">7.6%</td>
<td align="right">234.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,686,380</td>
<td align="right">60.2%</td>
<td align="right">1,686,380</td>
<td align="right">53.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">894,900</td>
<td align="right">31.9%</td>
<td align="right">894,900</td>
<td align="right">28.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">50,720</td>
<td align="right">1.8%</td>
<td align="right">50,720</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">27,560</td>
<td align="right">1.0%</td>
<td align="right">27,560</td>
<td align="right">0.9%</td>
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
<td align="left">Method cache misses</td>
<td align="right">10,906</td>
<td align="right"></td>
<td align="right">74,083</td>
<td align="right"></td>
<td align="right">579.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">20,991</td>
<td align="right"></td>
<td align="right">117,976</td>
<td align="right"></td>
<td align="right">462.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">10,602</td>
<td align="right"></td>
<td align="right">44,523</td>
<td align="right"></td>
<td align="right">319.9%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">2,399,414,320</td>
<td align="right">2,399,414,320 / 0 !!</td>
<td align="right">3,630,054,820</td>
<td align="right">3,630,054,820 / 0 !!</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">3,124,690,480</td>
<td align="right">3,124,690,480 / 0 !!</td>
<td align="right">4,256,963,680</td>
<td align="right">4,256,963,680 / 0 !!</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">5,354,606,661</td>
<td align="right">5,354,606,661 / 0 !!</td>
<td align="right">3,983,739,804</td>
<td align="right">3,983,739,804 / 0 !!</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">5,609,451,295</td>
<td align="right">5,609,451,295 / 0 !!</td>
<td align="right">4,340,585,572</td>
<td align="right">4,340,585,572 / 0 !!</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">606,140</td>
<td align="right">0.1%</td>
<td align="right">686,400</td>
<td align="right">0.1%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">1,960</td>
<td align="right">0.0%</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">509,725,160</td>
<td align="right">51.6%</td>
<td align="right">513,268,900</td>
<td align="right">51.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">509,887,100</td>
<td align="right"></td>
<td align="right">513,430,840</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">102,360,114</td>
<td align="right"></td>
<td align="right">102,302,837</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">479,398,189</td>
<td align="right"></td>
<td align="right">479,531,313</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">478,681,140</td>
<td align="right">48.4%</td>
<td align="right">478,769,220</td>
<td align="right">48.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">71,197,638</td>
<td align="right"></td>
<td align="right">71,188,057</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">478,073,040</td>
<td align="right">48.4%</td>
<td align="right">478,080,660</td>
<td align="right">48.2%</td>
<td align="right">0.0%</td>
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
<td align="right">1,920</td>
<td align="right">73,409,420</td>
<td align="right">3,120</td>
<td align="right">1,920</td>
<td align="right">73,464,340</td>
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
<td align="right">1,360</td>
<td align="right">1.6%</td>
<td align="right">89,440</td>
<td align="right">54.1%</td>
<td align="right">6,476.5%</td>
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
<td align="right">0.2%</td>
<td align="right">8,160</td>
<td align="right">4.9%</td>
<td align="right">4,433.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">83,440</td>
<td align="right"></td>
<td align="right">165,180</td>
<td align="right"></td>
<td align="right">98.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">12,455,676,780</td>
<td align="right">2,907.6%</td>
<td align="right">7,198,827,120</td>
<td align="right">2,183.8%</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">428,384,440</td>
<td align="right"></td>
<td align="right">329,644,840</td>
<td align="right"></td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">82,160</td>
<td align="right">98.5%</td>
<td align="right">99,240</td>
<td align="right">60.1%</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">82,080</td>
<td align="right">98.4%</td>
<td align="right">75,740</td>
<td align="right">45.9%</td>
<td align="right">-7.7%</td>
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
<td align="right">1,360</td>
<td align="right"></td>
<td align="right">89,440</td>
<td align="right"></td>
<td align="right">6,476.5%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,360</td>
<td align="right">100.0%</td>
<td align="right">89,440</td>
<td align="right">100.0%</td>
<td align="right">6,476.5%</td>
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
<td align="right">40</td>
<td align="right">2.9%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">200</td>
<td align="right">14.7%</td>
<td align="right">2,740</td>
<td align="right">3.1%</td>
<td align="right">1,270.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">120</td>
<td align="right">8.8%</td>
<td align="right">140</td>
<td align="right">0.2%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">280</td>
<td align="right">20.6%</td>
<td align="right">30,180</td>
<td align="right">33.7%</td>
<td align="right">10,678.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">300</td>
<td align="right">22.1%</td>
<td align="right">14,500</td>
<td align="right">16.2%</td>
<td align="right">4,733.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">140</td>
<td align="right">10.3%</td>
<td align="right">11,620</td>
<td align="right">13.0%</td>
<td align="right">8,200.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">260</td>
<td align="right">19.1%</td>
<td align="right">30,060</td>
<td align="right">33.6%</td>
<td align="right">11,461.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">1.5%</td>
<td align="right">200</td>
<td align="right">0.2%</td>
<td align="right">900.0%</td>
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
<td align="right">240</td>
<td align="right">17.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">80</td>
<td align="right">5.9%</td>
<td align="right">2,840</td>
<td align="right">3.2%</td>
<td align="right">3,450.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">160</td>
<td align="right">11.8%</td>
<td align="right">16,800</td>
<td align="right">18.8%</td>
<td align="right">10,400.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">220</td>
<td align="right">16.2%</td>
<td align="right">23,140</td>
<td align="right">25.9%</td>
<td align="right">10,418.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">340</td>
<td align="right">25.0%</td>
<td align="right">11,520</td>
<td align="right">12.9%</td>
<td align="right">3,288.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">160</td>
<td align="right">11.8%</td>
<td align="right">15,360</td>
<td align="right">17.2%</td>
<td align="right">9,500.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">160</td>
<td align="right">11.8%</td>
<td align="right">19,580</td>
<td align="right">21.9%</td>
<td align="right">12,137.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">200</td>
<td align="right">0.2%</td>
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
<td align="right">88,960</td>
<td align="right">60</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">88,960</td>
<td align="right">60</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">444,800</td>
<td align="right">420</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">382,480</td>
<td align="right">480</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">360,960</td>
<td align="right">600</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">183,040</td>
<td align="right">420</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">8,560</td>
<td align="right">20</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">8,560</td>
<td align="right">20</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">275,840</td>
<td align="right">740</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">275,840</td>
<td align="right">740</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">363,520</td>
<td align="right">1,580</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">768,100</td>
<td align="right">4,160</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">185,600</td>
<td align="right">1,380</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">369,920</td>
<td align="right">2,880</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,811,280</td>
<td align="right">23,020</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">2,178,400</td>
<td align="right">20,160</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,178,320</td>
<td align="right">20,160</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">555,520</td>
<td align="right">5,240</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">6,668,680</td>
<td align="right">66,560</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">8,073,800</td>
<td align="right">128,040</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">7,720,080</td>
<td align="right">124,120</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,492,260</td>
<td align="right">25,720</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">368,640</td>
<td align="right">7,120</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">1,314,340</td>
<td align="right">25,600</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">4,612,260</td>
<td align="right">94,160</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">5,457,960</td>
<td align="right">114,880</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">4,233,860</td>
<td align="right">89,360</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,233,860</td>
<td align="right">89,360</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">487,960</td>
<td align="right">10,400</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,350,880</td>
<td align="right">93,320</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,350,880</td>
<td align="right">93,320</td>
<td align="right">-97.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">24,639,960</td>
<td align="right">532,440</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">4,150,020</td>
<td align="right">89,680</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,338,340</td>
<td align="right">117,520</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">12,282,280</td>
<td align="right">271,640</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">8,212,360</td>
<td align="right">183,040</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">4,258,260</td>
<td align="right">95,720</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">3,965,700</td>
<td align="right">89,160</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">3,965,700</td>
<td align="right">89,160</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">3,965,700</td>
<td align="right">89,160</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">3,965,700</td>
<td align="right">89,160</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">3,965,700</td>
<td align="right">89,160</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">3,875,460</td>
<td align="right">89,160</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">55,640,100</td>
<td align="right">1,338,360</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,556,040</td>
<td align="right">63,480</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">9,680,320</td>
<td align="right">240,740</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">1,591,860</td>
<td align="right">40,860</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">2,162,760</td>
<td align="right">57,600</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">2,162,760</td>
<td align="right">62,680</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">56,830,160</td>
<td align="right">1,898,880</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">28,195,240</td>
<td align="right">1,296,180</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">102,780</td>
<td align="right">6,240</td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">85,601,240</td>
<td align="right">10,049,160</td>
<td align="right">-88.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">90,315,540</td>
<td align="right">12,850,180</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">44,265,280</td>
<td align="right">6,363,560</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">41,437,280</td>
<td align="right">6,299,860</td>
<td align="right">-84.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">460,529,780</td>
<td align="right">75,615,380</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">75,739,520</td>
<td align="right">12,448,540</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">150,062,260</td>
<td align="right">24,883,200</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">40,808,280</td>
<td align="right">6,768,080</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">74,238,420</td>
<td align="right">12,439,120</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">36,123,340</td>
<td align="right">6,181,820</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">70,790,560</td>
<td align="right">12,372,940</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">70,361,680</td>
<td align="right">12,350,060</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">70,272,720</td>
<td align="right">12,349,960</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">38,296,560</td>
<td align="right">6,773,020</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">138,080,840</td>
<td align="right">24,620,180</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">138,080,840</td>
<td align="right">24,620,180</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">102,477,880</td>
<td align="right">18,388,740</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">67,799,400</td>
<td align="right">12,276,520</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">67,074,680</td>
<td align="right">12,266,740</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">134,115,140</td>
<td align="right">24,531,020</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">134,115,140</td>
<td align="right">24,531,020</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">62,909,400</td>
<td align="right">12,174,800</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">62,909,400</td>
<td align="right">12,174,800</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">62,909,400</td>
<td align="right">12,174,800</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">62,815,320</td>
<td align="right">12,172,320</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">62,812,100</td>
<td align="right">12,172,200</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">62,812,100</td>
<td align="right">12,172,200</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">62,726,500</td>
<td align="right">12,177,100</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">62,731,320</td>
<td align="right">12,178,280</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">31,179,220</td>
<td align="right">6,085,840</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">62,341,320</td>
<td align="right">12,171,640</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">62,341,320</td>
<td align="right">12,171,640</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">31,170,660</td>
<td align="right">6,085,820</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">31,170,660</td>
<td align="right">6,085,820</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">31,170,660</td>
<td align="right">6,085,820</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">62,341,320</td>
<td align="right">12,172,940</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">45,002,480</td>
<td align="right">9,056,340</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">96,790,780</td>
<td align="right">20,745,100</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">107,180,280</td>
<td align="right">35,893,280</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">76,374,260</td>
<td align="right">28,273,020</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">1,610,966,180</td>
<td align="right">601,079,400</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">51,652,380</td>
<td align="right">22,945,840</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">59,265,140</td>
<td align="right">28,922,980</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">66,258,420</td>
<td align="right">42,548,820</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">507,943,140</td>
<td align="right">327,806,660</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">1,443,691,580</td>
<td align="right">933,694,120</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">405,101,580</td>
<td align="right">264,948,300</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">32,634,260</td>
<td align="right">22,466,380</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">350,850,700</td>
<td align="right">252,984,840</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">342,141,560</td>
<td align="right">252,708,220</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">390,268,480</td>
<td align="right">292,074,140</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">388,661,240</td>
<td align="right">292,064,220</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">325,620,980</td>
<td align="right">249,722,120</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">428,384,440</td>
<td align="right">329,644,840</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">428,001,960</td>
<td align="right">329,643,060</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">28,317,480</td>
<td align="right">22,306,860</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">28,353,700</td>
<td align="right">22,901,240</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">342,170,680</td>
<td align="right">376,141,520</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">270,807,400</td>
<td align="right">245,617,480</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">261,657,560</td>
<td align="right">240,167,060</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">260,730,740</td>
<td align="right">239,973,700</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">251,697,060</td>
<td align="right">239,793,400</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">249,971,460</td>
<td align="right">239,746,560</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">22,780,160</td>
<td align="right">22,246,920</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">22,335,360</td>
<td align="right">22,246,460</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">22,335,360</td>
<td align="right">22,246,460</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">22,920,800</td>
<td align="right">22,831,900</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">22,920,800</td>
<td align="right">22,831,900</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">239,525,400</td>
<td align="right">239,525,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">854,100</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">90,240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">90,240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right"></td>
<td align="right">357,917,860</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">1,300</td>
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
<td align="right">360</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40</td>
<td align="right"></td>
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
