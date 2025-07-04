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
<td align="right">737,180</td>
<td align="right">368,540</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,489,020</td>
<td align="right">840,660</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,758,360</td>
<td align="right">992,920</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">751,200</td>
<td align="right">427,040</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">833,160</td>
<td align="right">476,740</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,474,320</td>
<td align="right">866,580</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,977,800</td>
<td align="right">1,204,080</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,978,080</td>
<td align="right">1,212,600</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">956,660</td>
<td align="right">588,020</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">1,848,060</td>
<td align="right">1,199,740</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,221,600</td>
<td align="right">1,456,160</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,645,740</td>
<td align="right">1,081,100</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,315,320</td>
<td align="right">1,544,320</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">3,441,580</td>
<td align="right">2,331,700</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">613,580</td>
<td align="right">417,880</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,883,160</td>
<td align="right">1,998,080</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,000,320</td>
<td align="right">702,000</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,922,000</td>
<td align="right">2,061,660</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">558,800</td>
<td align="right">396,860</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,159,860</td>
<td align="right">3,237,300</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">587,380</td>
<td align="right">473,140</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">588,180</td>
<td align="right">473,900</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">929,800</td>
<td align="right">754,120</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">638,140</td>
<td align="right">521,020</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">684,860</td>
<td align="right">561,980</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">678,780</td>
<td align="right">559,080</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">6,612,900</td>
<td align="right">5,456,340</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,126,480</td>
<td align="right">4,247,420</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">6,785,200</td>
<td align="right">5,790,820</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,601,440</td>
<td align="right">5,678,880</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,817,500</td>
<td align="right">3,334,940</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,740,380</td>
<td align="right">2,504,380</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">1,653,600</td>
<td align="right">1,539,360</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,777,880</td>
<td align="right">4,467,980</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">2,023,620</td>
<td align="right">1,903,920</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">30,448,380</td>
<td align="right">28,884,460</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">69,415,260</td>
<td align="right">66,598,020</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">7,756,440</td>
<td align="right">7,486,820</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">34,648,040</td>
<td align="right">33,574,020</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">83,931,660</td>
<td align="right">81,677,940</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">47,036,020</td>
<td align="right">45,863,980</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">760,000</td>
<td align="right">743,440</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">894,600</td>
<td align="right">875,280</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">50,768,160</td>
<td align="right">49,724,160</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">52,653,060</td>
<td align="right">51,734,700</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">55,656,060</td>
<td align="right">54,779,260</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">78,330,440</td>
<td align="right">77,188,220</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">820,816,800</td>
<td align="right">809,673,040</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">23,809,660</td>
<td align="right">23,578,300</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">138,997,560</td>
<td align="right">138,006,520</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">247,155,720</td>
<td align="right">245,412,440</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">225,567,500</td>
<td align="right">223,978,160</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">271,086,180</td>
<td align="right">269,218,340</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">67,242,960</td>
<td align="right">66,783,120</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">309,558,540</td>
<td align="right">307,691,020</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">23,999,140</td>
<td align="right">23,865,580</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,033,640</td>
<td align="right">2,022,520</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">214,514,420</td>
<td align="right">213,486,980</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">33,021,740</td>
<td align="right">32,890,940</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">382,306,440</td>
<td align="right">381,045,280</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">49,161,000</td>
<td align="right">49,034,940</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">570,784,140</td>
<td align="right">569,583,780</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">73,697,000</td>
<td align="right">73,569,020</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">290,030,980</td>
<td align="right">289,588,960</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">49,627,620</td>
<td align="right">49,557,900</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">126,498,700</td>
<td align="right">126,329,260</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">49,251,360</td>
<td align="right">49,189,920</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">25,914,780</td>
<td align="right">25,889,940</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">291,703,000</td>
<td align="right">291,585,880</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">326,917,360</td>
<td align="right">326,917,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">243,371,880</td>
<td align="right">243,371,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">210,931,640</td>
<td align="right">210,931,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">97,512,080</td>
<td align="right">97,512,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">60,078,480</td>
<td align="right">60,078,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">44,121,920</td>
<td align="right">44,121,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">43,682,860</td>
<td align="right">43,682,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">30,039,260</td>
<td align="right">30,039,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">24,817,120</td>
<td align="right">24,817,120</td>
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
<td align="right">7,584,720</td>
<td align="right">7,584,720</td>
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
<td align="right">2,443,040</td>
<td align="right">2,443,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,241,460</td>
<td align="right">1,241,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,211,680</td>
<td align="right">1,211,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">878,640</td>
<td align="right">878,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">540,600</td>
<td align="right">540,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">289,320</td>
<td align="right">289,320</td>
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
<td align="right">289,240</td>
<td align="right">289,240</td>
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
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">219,520</td>
<td align="right">219,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">219,520</td>
<td align="right">219,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">219,520</td>
<td align="right">219,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">79,340</td>
<td align="right">79,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">79,340</td>
<td align="right">79,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">6,780</td>
<td align="right">6,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,220</td>
<td align="right">5,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4,380</td>
<td align="right">4,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">1,040</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">560</td>
<td align="right">560</td>
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
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">220</td>
<td align="right">220</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
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
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
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
<td align="right">309,473,380</td>
<td align="right">43.1%</td>
<td align="right">307,606,340</td>
<td align="right">42.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">409,048,380</td>
<td align="right">56.9%</td>
<td align="right">409,048,380</td>
<td align="right">57.1%</td>
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
<td align="right">83,920</td>
<td align="right">98.5%</td>
<td align="right">83,440</td>
<td align="right">98.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,240</td>
<td align="right">1.5%</td>
<td align="right">1,240</td>
<td align="right">1.5%</td>
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
<td align="right">1,200</td>
<td align="right">1.4%</td>
<td align="right">1,080</td>
<td align="right">1.3%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">280</td>
<td align="right">0.3%</td>
<td align="right">260</td>
<td align="right">0.3%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">300</td>
<td align="right">0.4%</td>
<td align="right">280</td>
<td align="right">0.3%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">62,480</td>
<td align="right">74.5%</td>
<td align="right">62,200</td>
<td align="right">74.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">17,460</td>
<td align="right">20.8%</td>
<td align="right">17,420</td>
<td align="right">20.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">960</td>
<td align="right">1.1%</td>
<td align="right">960</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">520</td>
<td align="right">0.6%</td>
<td align="right">520</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">480</td>
<td align="right">0.6%</td>
<td align="right">480</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">240</td>
<td align="right">0.3%</td>
<td align="right">240</td>
<td align="right">0.3%</td>
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
<td align="right">1,901,800</td>
<td align="right">0.6%</td>
<td align="right">1,901,800</td>
<td align="right">0.6%</td>
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
<td align="right">320,679,920</td>
<td align="right">99.4%</td>
<td align="right">320,679,920</td>
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
<td align="right">1,935,660</td>
<td align="right">0.6%</td>
<td align="right">1,935,660</td>
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
<td align="right">39,080</td>
<td align="right">100.0%</td>
<td align="right">39,080</td>
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
<td align="right">612,440</td>
<td align="right">0.6%</td>
<td align="right">416,780</td>
<td align="right">0.4%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">99,129,820</td>
<td align="right">99.4%</td>
<td align="right">99,124,300</td>
<td align="right">99.6%</td>
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
<td align="right">520</td>
<td align="right">45.6%</td>
<td align="right">480</td>
<td align="right">43.6%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">620</td>
<td align="right">54.4%</td>
<td align="right">620</td>
<td align="right">56.4%</td>
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
<td align="right">520</td>
<td align="right">100.0%</td>
<td align="right">480</td>
<td align="right">100.0%</td>
<td align="right">-7.7%</td>
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
<td align="right">33,755,640</td>
<td align="right">100.0%</td>
<td align="right">33,755,640</td>
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
<td align="right">2,919,660</td>
<td align="right">1.0%</td>
<td align="right">2,059,500</td>
<td align="right">0.7%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">292,393,540</td>
<td align="right">98.9%</td>
<td align="right">291,817,520</td>
<td align="right">99.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">355,940</td>
<td align="right">0.1%</td>
<td align="right">355,940</td>
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
<td align="right">2,100</td>
<td align="right">23.2%</td>
<td align="right">1,920</td>
<td align="right">21.7%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,940</td>
<td align="right">76.8%</td>
<td align="right">6,940</td>
<td align="right">78.3%</td>
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
<td align="left">dict items</td>
<td align="right">1,720</td>
<td align="right">81.9%</td>
<td align="right">1,560</td>
<td align="right">81.2%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">360</td>
<td align="right">17.1%</td>
<td align="right">340</td>
<td align="right">17.7%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">20</td>
<td align="right">1.0%</td>
<td align="right">20</td>
<td align="right">1.0%</td>
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
<td align="left">list</td>
<td align="right">47,280,960</td>
<td align="right">47,280,960 / 0 !!</td>
<td align="right">47,280,960</td>
<td align="right">47,280,960 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,418,760</td>
<td align="right">1,418,760 / 0 !!</td>
<td align="right">1,418,760</td>
<td align="right">1,418,760 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">428,700</td>
<td align="right">428,700 / 0 !!</td>
<td align="right">428,700</td>
<td align="right">428,700 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">219,600</td>
<td align="right">219,600 / 0 !!</td>
<td align="right">219,600</td>
<td align="right">219,600 / 0 !!</td>
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
<td align="right">34,627,520</td>
<td align="right">14.8%</td>
<td align="right">33,553,760</td>
<td align="right">14.5%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">198,552,020</td>
<td align="right">85.1%</td>
<td align="right">197,063,900</td>
<td align="right">85.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">65,560</td>
<td align="right">0.0%</td>
<td align="right">65,560</td>
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
<td align="right">18,760</td>
<td align="right">86.3%</td>
<td align="right">18,500</td>
<td align="right">86.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,980</td>
<td align="right">13.7%</td>
<td align="right">2,980</td>
<td align="right">13.9%</td>
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
<td align="right">240</td>
<td align="right">1.3%</td>
<td align="right">200</td>
<td align="right">1.1%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">11,500</td>
<td align="right">61.3%</td>
<td align="right">11,320</td>
<td align="right">61.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">6,780</td>
<td align="right">36.1%</td>
<td align="right">6,780</td>
<td align="right">36.6%</td>
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
<td align="right">227,467,320</td>
<td align="right">100.0%</td>
<td align="right">226,479,820</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,180</td>
<td align="right">0.0%</td>
<td align="right">2,180</td>
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
<td align="right">2,200</td>
<td align="right">100.0%</td>
<td align="right">2,200</td>
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
<td align="right">30,039,260</td>
<td align="right">100.0%</td>
<td align="right">30,039,260</td>
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
<td align="right">60,078,720</td>
<td align="right">100.0%</td>
<td align="right">60,078,720</td>
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
<td align="right">3,438,800</td>
<td align="right">92.2%</td>
<td align="right">2,329,200</td>
<td align="right">88.9%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">289,240</td>
<td align="right">7.8%</td>
<td align="right">289,240</td>
<td align="right">11.0%</td>
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
<td align="right">2,760</td>
<td align="right">99.3%</td>
<td align="right">2,480</td>
<td align="right">99.2%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">0.7%</td>
<td align="right">20</td>
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
<td align="left">dict subclass no override</td>
<td align="right">2,760</td>
<td align="right">100.0%</td>
<td align="right">2,480</td>
<td align="right">100.0%</td>
<td align="right">-10.1%</td>
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
<td align="right">587,700</td>
<td align="right">2.1%</td>
<td align="right">473,460</td>
<td align="right">1.7%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">27,769,080</td>
<td align="right">97.9%</td>
<td align="right">27,769,080</td>
<td align="right">98.3%</td>
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
<td align="right">240</td>
<td align="right">50.0%</td>
<td align="right">200</td>
<td align="right">45.5%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">240</td>
<td align="right">50.0%</td>
<td align="right">240</td>
<td align="right">54.5%</td>
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
<td align="right">220</td>
<td align="right">91.7%</td>
<td align="right">180</td>
<td align="right">90.0%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">8.3%</td>
<td align="right">20</td>
<td align="right">10.0%</td>
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
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">360</td>
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
<td align="right">220,936,740</td>
<td align="right">100.0%</td>
<td align="right">220,936,740</td>
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
<td align="right">401,034,360</td>
<td align="right">6.7%</td>
<td align="right">395,751,180</td>
<td align="right">6.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,433,227,960</td>
<td align="right">57.3%</td>
<td align="right">3,399,362,280</td>
<td align="right">57.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">2,155,036,920</td>
<td align="right">36.0%</td>
<td align="right">2,138,080,180</td>
<td align="right">36.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">2,357,160</td>
<td align="right">0.0%</td>
<td align="right">2,357,220</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">3,438,800</td>
<td align="right">1.0%</td>
<td align="right">2,329,200</td>
<td align="right">0.7%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">612,440</td>
<td align="right">0.2%</td>
<td align="right">416,780</td>
<td align="right">0.1%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,919,660</td>
<td align="right">0.8%</td>
<td align="right">2,059,500</td>
<td align="right">0.6%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">587,700</td>
<td align="right">0.2%</td>
<td align="right">473,460</td>
<td align="right">0.1%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">34,627,520</td>
<td align="right">9.8%</td>
<td align="right">33,553,760</td>
<td align="right">9.6%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">309,473,380</td>
<td align="right">87.5%</td>
<td align="right">307,606,340</td>
<td align="right">88.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,901,800</td>
<td align="right">0.5%</td>
<td align="right">1,901,800</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,180</td>
<td align="right">0.0%</td>
<td align="right">2,180</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,264,500</td>
<td align="right">53.6%</td>
<td align="right">1,264,500</td>
<td align="right">53.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">671,160</td>
<td align="right">28.5%</td>
<td align="right">671,160</td>
<td align="right">28.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">178,080</td>
<td align="right">7.6%</td>
<td align="right">178,080</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">177,860</td>
<td align="right">7.5%</td>
<td align="right">177,860</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">38,000</td>
<td align="right">1.6%</td>
<td align="right">38,000</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">27,560</td>
<td align="right">1.2%</td>
<td align="right">27,560</td>
<td align="right">1.2%</td>
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
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">60</td>
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
<td align="right">326,917,420</td>
<td align="right">67.7%</td>
<td align="right">326,917,420</td>
<td align="right">67.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">155,887,960</td>
<td align="right">32.3%</td>
<td align="right">155,887,960</td>
<td align="right">32.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">326,917,420</td>
<td align="right">67.7%</td>
<td align="right">326,917,420</td>
<td align="right">67.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">36,421,120</td>
<td align="right">7.5%</td>
<td align="right">36,421,120</td>
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
<td align="right">36,421,120</td>
<td align="right">7.5%</td>
<td align="right">36,421,120</td>
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
<td align="right">1,666,500</td>
<td align="right">0.3%</td>
<td align="right">1,666,500</td>
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
<td align="right">192,309,120</td>
<td align="right">39.8%</td>
<td align="right">192,309,120</td>
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
<td align="left">Allocations over 4 kbytes</td>
<td align="right">1,780</td>
<td align="right">0.0%</td>
<td align="right">1,940</td>
<td align="right">0.0%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,383</td>
<td align="right"></td>
<td align="right">1,299</td>
<td align="right"></td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">599</td>
<td align="right"></td>
<td align="right">583</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,164</td>
<td align="right"></td>
<td align="right">1,148</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,999,114,228</td>
<td align="right">43.4%</td>
<td align="right">2,010,944,009</td>
<td align="right">43.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,227,917,036</td>
<td align="right">41.4%</td>
<td align="right">2,239,416,780</td>
<td align="right">41.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,042,189,480</td>
<td align="right">44.3%</td>
<td align="right">2,033,952,660</td>
<td align="right">44.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,500,787,080</td>
<td align="right">46.5%</td>
<td align="right">2,492,880,400</td>
<td align="right">46.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">124,291,260</td>
<td align="right">2.7%</td>
<td align="right">123,943,080</td>
<td align="right">2.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">94,861,240</td>
<td align="right">1.8%</td>
<td align="right">94,665,580</td>
<td align="right">1.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">440,467,518</td>
<td align="right">9.6%</td>
<td align="right">440,817,953</td>
<td align="right">9.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">558,460,110</td>
<td align="right">10.4%</td>
<td align="right">558,657,942</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">50,252,801</td>
<td align="right"></td>
<td align="right">50,252,257</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">143,421,260</td>
<td align="right">20.7%</td>
<td align="right">143,421,420</td>
<td align="right">20.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">76,781,856</td>
<td align="right"></td>
<td align="right">76,781,912</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">143,963,845</td>
<td align="right"></td>
<td align="right">143,963,889</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">550,175,420</td>
<td align="right">79.3%</td>
<td align="right">550,175,440</td>
<td align="right">79.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">550,298,200</td>
<td align="right"></td>
<td align="right">550,298,220</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">142,964,980</td>
<td align="right">20.6%</td>
<td align="right">142,964,980</td>
<td align="right">20.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">454,500</td>
<td align="right">0.1%</td>
<td align="right">454,500</td>
<td align="right">0.1%</td>
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
<td align="right">2,360</td>
<td align="right">6,280</td>
<td align="right">40,876,738</td>
<td align="right">1,726,340</td>
<td align="right">4,744,320</td>
<td align="right">2,360</td>
<td align="right">6,280</td>
<td align="right">40,879,168</td>
<td align="right">1,725,160</td>
<td align="right">4,745,600</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">120</td>
<td align="right">0.2%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,120</td>
<td align="right">1.9%</td>
<td align="right">1,280</td>
<td align="right">2.1%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">27,874,840</td>
<td align="right"></td>
<td align="right">29,218,800</td>
<td align="right"></td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">5,373,947,420</td>
<td align="right">19,278.8%</td>
<td align="right">5,505,641,780</td>
<td align="right">18,842.8%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">60,520</td>
<td align="right"></td>
<td align="right">61,040</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">59,400</td>
<td align="right">98.1%</td>
<td align="right">59,760</td>
<td align="right">97.9%</td>
<td align="right">0.6%</td>
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
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">60 / 0 !!</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it is too short.
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20 / 0 !!</td>
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
<td align="right">1,120</td>
<td align="right"></td>
<td align="right">1,280</td>
<td align="right"></td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,120</td>
<td align="right">100.0%</td>
<td align="right">1,280</td>
<td align="right">100.0%</td>
<td align="right">14.3%</td>
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
<td align="right">15,256,880</td>
<td align="right">81.7%</td>
<td align="right">21,497,700</td>
<td align="right">84.1%</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">375,840</td>
<td align="right">2.0%</td>
<td align="right">523,200</td>
<td align="right">2.0%</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">18,677,760</td>
<td align="right"></td>
<td align="right">25,559,040</td>
<td align="right"></td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">3,045,040</td>
<td align="right">16.3%</td>
<td align="right">3,538,140</td>
<td align="right">13.8%</td>
<td align="right">16.2%</td>
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
<td align="right">81,920</td>
<td align="right">0.4%</td>
<td align="right">81,920</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
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
<td align="left"><= 4,096</td>
<td align="left">180</td>
<td align="right">16.1%</td>
<td align="left">180</td>
<td align="right">14.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">300</td>
<td align="right">26.8%</td>
<td align="left">360</td>
<td align="right">28.1%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">300</td>
<td align="right">26.8%</td>
<td align="left">240</td>
<td align="right">18.8%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">160</td>
<td align="right">14.3%</td>
<td align="left">240</td>
<td align="right">18.8%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">180</td>
<td align="right">16.1%</td>
<td align="left">260</td>
<td align="right">20.3%</td>
<td align="right">44.4%</td>
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
<td align="left"><= 8</td>
<td align="right">180</td>
<td align="right">16.1%</td>
<td align="right">180</td>
<td align="right">14.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">60</td>
<td align="right">5.4%</td>
<td align="right">120</td>
<td align="right">9.4%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">240</td>
<td align="right">21.4%</td>
<td align="right">240</td>
<td align="right">18.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">300</td>
<td align="right">26.8%</td>
<td align="right">240</td>
<td align="right">18.8%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">160</td>
<td align="right">14.3%</td>
<td align="right">180</td>
<td align="right">14.1%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">180</td>
<td align="right">16.1%</td>
<td align="right">260</td>
<td align="right">20.3%</td>
<td align="right">44.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">60</td>
<td align="right">4.7%</td>
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
<td align="left"><= 4</td>
<td align="right">120</td>
<td align="right">10.7%</td>
<td align="right">120</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">60</td>
<td align="right">5.4%</td>
<td align="right">60</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">120</td>
<td align="right">10.7%</td>
<td align="right">180</td>
<td align="right">14.1%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">420</td>
<td align="right">37.5%</td>
<td align="right">360</td>
<td align="right">28.1%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">160</td>
<td align="right">14.3%</td>
<td align="right">180</td>
<td align="right">14.1%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">240</td>
<td align="right">21.4%</td>
<td align="right">320</td>
<td align="right">25.0%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">60</td>
<td align="right">4.7%</td>
<td align="right"></td>
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
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">19,920</td>
<td align="right">181,860</td>
<td align="right">813.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">19,920</td>
<td align="right">181,860</td>
<td align="right">813.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">19,920</td>
<td align="right">137,040</td>
<td align="right">588.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">19,920</td>
<td align="right">137,040</td>
<td align="right">588.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">19,920</td>
<td align="right">137,040</td>
<td align="right">588.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">11,040</td>
<td align="right">33,120</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">11,040</td>
<td align="right">24,840</td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">22,080</td>
<td align="right">41,400</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">187,080</td>
<td align="right">313,140</td>
<td align="right">67.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">1,424,760</td>
<td align="right">2,375,580</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">96,660</td>
<td align="right">158,100</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">96,660</td>
<td align="right">158,100</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">2,061,000</td>
<td align="right">3,158,580</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">22,120</td>
<td align="right">33,240</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">22,120</td>
<td align="right">33,240</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">11,040</td>
<td align="right">16,560</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">11,040</td>
<td align="right">16,560</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">908,400</td>
<td align="right">1,299,120</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">897,360</td>
<td align="right">1,266,000</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">897,420</td>
<td align="right">1,266,060</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">897,420</td>
<td align="right">1,266,060</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">593,820</td>
<td align="right">789,480</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">1,318,380</td>
<td align="right">1,616,700</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">5,662,320</td>
<td align="right">6,689,760</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,662,320</td>
<td align="right">6,689,760</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">3,479,940</td>
<td align="right">4,108,320</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">8,407,740</td>
<td align="right">9,742,800</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">5,542,020</td>
<td align="right">6,402,180</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">3,272,220</td>
<td align="right">3,582,120</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,698,320</td>
<td align="right">2,929,680</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,698,320</td>
<td align="right">2,929,680</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">14,721,420</td>
<td align="right">15,795,180</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">2,926,860</td>
<td align="right">3,136,800</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">21,325,740</td>
<td align="right">22,707,780</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,775,060</td>
<td align="right">2,950,740</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">26,304,660</td>
<td align="right">27,630,560</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">13,403,040</td>
<td align="right">14,074,260</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,700,480</td>
<td align="right">2,834,040</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,678,400</td>
<td align="right">2,809,200</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">2,678,400</td>
<td align="right">2,809,200</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">27,874,840</td>
<td align="right">29,218,800</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">5,378,880</td>
<td align="right">5,626,680</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">2,678,400</td>
<td align="right">2,800,920</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">27,854,920</td>
<td align="right">29,081,720</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">8,035,200</td>
<td align="right">8,386,200</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">18,672,420</td>
<td align="right">19,472,880</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">2,678,400</td>
<td align="right">2,792,640</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">2,678,400</td>
<td align="right">2,792,640</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">2,678,400</td>
<td align="right">2,792,640</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">2,678,400</td>
<td align="right">2,792,640</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right">2,678,400</td>
<td align="right">2,792,640</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NULL</td>
<td align="right">2,678,400</td>
<td align="right">2,792,640</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">2,678,400</td>
<td align="right">2,792,640</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,678,400</td>
<td align="right">2,792,640</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">27,787,740</td>
<td align="right">28,954,260</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">26,391,180</td>
<td align="right">27,385,560</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">120,484,020</td>
<td align="right">124,407,000</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">48,922,920</td>
<td align="right">50,411,040</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">59,689,260</td>
<td align="right">61,497,180</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">46,917,300</td>
<td align="right">48,320,520</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">28,696,500</td>
<td align="right">29,536,640</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">56,080,680</td>
<td align="right">57,693,080</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">81,395,740</td>
<td align="right">83,735,820</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">62,068,200</td>
<td align="right">63,831,420</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">129,269,920</td>
<td align="right">132,824,840</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">30,781,080</td>
<td align="right">31,572,920</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">24,306,240</td>
<td align="right">24,921,060</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">843,353,920</td>
<td align="right">863,904,660</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">959,217,100</td>
<td align="right">982,589,480</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">53,373,480</td>
<td align="right">54,634,680</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">49,315,740</td>
<td align="right">50,472,300</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_COPY_2</td>
<td align="right">39,674,400</td>
<td align="right">40,596,960</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">19,837,200</td>
<td align="right">20,298,480</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right">19,837,200</td>
<td align="right">20,298,480</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">25,347,540</td>
<td align="right">25,908,620</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">106,674,000</td>
<td align="right">108,920,720</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">47,994,600</td>
<td align="right">48,991,440</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">98,649,840</td>
<td align="right">100,559,360</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">98,649,840</td>
<td align="right">100,559,360</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">47,996,760</td>
<td align="right">48,912,360</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">32,281,320</td>
<td align="right">32,889,060</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">32,281,320</td>
<td align="right">32,889,060</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">78,469,140</td>
<td align="right">79,944,160</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">95,971,440</td>
<td align="right">97,766,720</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">53,520,900</td>
<td align="right">54,517,020</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">53,311,560</td>
<td align="right">54,302,600</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">101,730,480</td>
<td align="right">103,597,520</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">47,974,680</td>
<td align="right">48,854,360</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">47,974,680</td>
<td align="right">48,854,360</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">103,944,720</td>
<td align="right">105,812,560</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">50,633,160</td>
<td align="right">51,518,240</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">50,633,160</td>
<td align="right">51,509,960</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">45,296,280</td>
<td align="right">46,070,000</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">65,113,560</td>
<td align="right">66,223,160</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">45,307,320</td>
<td align="right">46,078,320</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">45,307,320</td>
<td align="right">46,078,320</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">45,296,280</td>
<td align="right">46,061,760</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">45,296,280</td>
<td align="right">46,061,720</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">45,296,280</td>
<td align="right">46,061,720</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">45,296,280</td>
<td align="right">46,061,720</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">331,708,440</td>
<td align="right">337,226,260</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">45,276,360</td>
<td align="right">45,924,720</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">45,276,360</td>
<td align="right">45,924,680</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">45,276,360</td>
<td align="right">45,924,680</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">22,638,180</td>
<td align="right">22,962,340</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">22,638,180</td>
<td align="right">22,962,340</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">22,638,180</td>
<td align="right">22,962,340</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">22,638,180</td>
<td align="right">22,962,340</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">22,638,180</td>
<td align="right">22,962,340</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">48,086,160</td>
<td align="right">48,524,940</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">48,525,540</td>
<td align="right">48,967,560</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">48,525,540</td>
<td align="right">48,967,560</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">16,445,640</td>
<td align="right">16,573,620</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">16,878,420</td>
<td align="right">17,001,300</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">16,878,420</td>
<td align="right">17,001,300</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">16,445,640</td>
<td align="right">16,565,340</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_OVERFLOWED</td>
<td align="right">16,445,640</td>
<td align="right">16,565,340</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">16,445,640</td>
<td align="right">16,565,340</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">16,445,640</td>
<td align="right">16,565,340</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right"></td>
<td align="right">44,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right"></td>
<td align="right">44,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right"></td>
<td align="right">44,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right"></td>
<td align="right">24,840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right"></td>
<td align="right">16,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right"></td>
<td align="right">16,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right"></td>
<td align="right">16,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right"></td>
<td align="right">16,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_OVERFLOWED</td>
<td align="right"></td>
<td align="right">8,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right"></td>
<td align="right">8,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right"></td>
<td align="right">8,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">40</td>
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
Stats gathered on: 2025-06-30
