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
<td align="left">NOT_TAKEN</td>
<td align="right">85,435</td>
<td align="right">104,920</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">331,541</td>
<td align="right">313,185</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,340,812</td>
<td align="right">1,314,620</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,413,235</td>
<td align="right">1,389,326</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">960,080</td>
<td align="right">945,776</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">4,655,247</td>
<td align="right">4,604,444</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,244,526</td>
<td align="right">2,227,270</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">504,395</td>
<td align="right">506,990</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,825,688</td>
<td align="right">1,833,029</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,339,209</td>
<td align="right">1,334,325</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,484,169</td>
<td align="right">1,479,285</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">969,285</td>
<td align="right">972,244</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,248,792</td>
<td align="right">1,251,880</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,345,812</td>
<td align="right">1,348,900</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,461,192</td>
<td align="right">1,464,280</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,368,109</td>
<td align="right">3,363,225</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">16,609,315</td>
<td align="right">16,591,104</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,885,652</td>
<td align="right">2,888,680</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">6,397,381</td>
<td align="right">6,402,929</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">3,806,232</td>
<td align="right">3,809,320</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,149,152</td>
<td align="right">3,151,310</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">9,809,363</td>
<td align="right">9,813,675</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,517,849</td>
<td align="right">14,522,568</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">84,394,002</td>
<td align="right">84,388,434</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">977,800</td>
<td align="right">977,845</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">482,880</td>
<td align="right">482,883</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,160,687</td>
<td align="right">1,160,694</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,506,200</td>
<td align="right">2,506,209</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,206,460</td>
<td align="right">1,206,463</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,290,440</td>
<td align="right">1,290,443</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">9,462,480</td>
<td align="right">9,462,489</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,411,420</td>
<td align="right">11,411,429</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">18,900,760</td>
<td align="right">18,900,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">15,219,300</td>
<td align="right">15,219,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">14,638,500</td>
<td align="right">14,638,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">13,957,080</td>
<td align="right">13,957,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,768,080</td>
<td align="right">8,768,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">7,100,480</td>
<td align="right">7,100,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">6,226,840</td>
<td align="right">6,226,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,897,920</td>
<td align="right">5,897,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">5,701,740</td>
<td align="right">5,701,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">5,673,120</td>
<td align="right">5,673,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">5,604,160</td>
<td align="right">5,604,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,821,240</td>
<td align="right">4,821,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">4,396,740</td>
<td align="right">4,396,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,625,080</td>
<td align="right">3,625,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,576,960</td>
<td align="right">3,576,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,404,180</td>
<td align="right">3,404,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,900,160</td>
<td align="right">2,900,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,492,780</td>
<td align="right">2,492,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">2,317,620</td>
<td align="right">2,317,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,218,560</td>
<td align="right">2,218,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,200,400</td>
<td align="right">2,200,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,174,580</td>
<td align="right">2,174,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,118,720</td>
<td align="right">2,118,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,027,580</td>
<td align="right">2,027,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,930,620</td>
<td align="right">1,930,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,737,600</td>
<td align="right">1,737,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,546,080</td>
<td align="right">1,546,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,545,720</td>
<td align="right">1,545,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,449,660</td>
<td align="right">1,449,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,401,600</td>
<td align="right">1,401,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,206,780</td>
<td align="right">1,206,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,159,680</td>
<td align="right">1,159,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">991,700</td>
<td align="right">991,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">963,900</td>
<td align="right">963,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">887,380</td>
<td align="right">887,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">868,260</td>
<td align="right">868,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">724,800</td>
<td align="right">724,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">724,800</td>
<td align="right">724,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">677,000</td>
<td align="right">677,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">629,760</td>
<td align="right">629,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">627,840</td>
<td align="right">627,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">624,960</td>
<td align="right">624,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">579,900</td>
<td align="right">579,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">579,900</td>
<td align="right">579,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">549,400</td>
<td align="right">549,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">530,940</td>
<td align="right">530,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">482,880</td>
<td align="right">482,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">481,580</td>
<td align="right">481,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">434,880</td>
<td align="right">434,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">434,880</td>
<td align="right">434,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">434,400</td>
<td align="right">434,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">433,920</td>
<td align="right">433,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">433,660</td>
<td align="right">433,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">385,980</td>
<td align="right">385,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">385,980</td>
<td align="right">385,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">338,840</td>
<td align="right">338,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">336,960</td>
<td align="right">336,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">241,980</td>
<td align="right">241,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">240,960</td>
<td align="right">240,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">240,960</td>
<td align="right">240,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">192,960</td>
<td align="right">192,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">192,000</td>
<td align="right">192,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">172,580</td>
<td align="right">172,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">145,380</td>
<td align="right">145,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">145,020</td>
<td align="right">145,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">145,020</td>
<td align="right">145,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">145,000</td>
<td align="right">145,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">144,000</td>
<td align="right">144,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">144,000</td>
<td align="right">144,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">144,000</td>
<td align="right">144,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">120,960</td>
<td align="right">120,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">97,500</td>
<td align="right">97,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">96,960</td>
<td align="right">96,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">96,080</td>
<td align="right">96,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">96,000</td>
<td align="right">96,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">48,060</td>
<td align="right">48,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">48,000</td>
<td align="right">48,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">48,000</td>
<td align="right">48,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,000</td>
<td align="right">48,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">867,840</td>
<td align="right">16.8%</td>
<td align="right">867,840</td>
<td align="right">16.8%</td>
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
<td align="right">4,295,100</td>
<td align="right">83.2%</td>
<td align="right">4,295,100</td>
<td align="right">83.2%</td>
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
<td align="right">4.8%</td>
<td align="right">20</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">400</td>
<td align="right">95.2%</td>
<td align="right">400</td>
<td align="right">95.2%</td>
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
<td align="left">or different types</td>
<td align="right">160</td>
<td align="right">40.0%</td>
<td align="right">160</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">120</td>
<td align="right">30.0%</td>
<td align="right">120</td>
<td align="right">30.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">80</td>
<td align="right">20.0%</td>
<td align="right">80</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">40</td>
<td align="right">10.0%</td>
<td align="right">40</td>
<td align="right">10.0%</td>
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
<td align="right">1,405,120</td>
<td align="right">10.9%</td>
<td align="right">1,405,120</td>
<td align="right">10.9%</td>
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
<td align="right">11,464,100</td>
<td align="right">88.9%</td>
<td align="right">11,464,100</td>
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
<td align="right">1,284,340</td>
<td align="right">10.0%</td>
<td align="right">1,284,340</td>
<td align="right">10.0%</td>
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
<td align="right">24,400</td>
<td align="right">99.2%</td>
<td align="right">24,400</td>
<td align="right">99.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">200</td>
<td align="right">0.8%</td>
<td align="right">200</td>
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
<td align="left">out of versions</td>
<td align="right">280</td>
<td align="right">140.0%</td>
<td align="right">280</td>
<td align="right">140.0%</td>
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
<td align="right">96,000</td>
<td align="right">99.9%</td>
<td align="right">96,000</td>
<td align="right">99.9%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">80</td>
<td align="right">100.0%</td>
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
<td align="right">504,243</td>
<td align="right">53.7%</td>
<td align="right">506,836</td>
<td align="right">53.9%</td>
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
<td align="right">433,920</td>
<td align="right">46.2%</td>
<td align="right">433,920</td>
<td align="right">46.1%</td>
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
<td align="right">152</td>
<td align="right">100.0%</td>
<td align="right">154</td>
<td align="right">100.0%</td>
<td align="right">1.3%</td>
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
<td align="left">bool</td>
<td align="right">32</td>
<td align="right">21.1%</td>
<td align="right">34</td>
<td align="right">22.1%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">80</td>
<td align="right">52.6%</td>
<td align="right">80</td>
<td align="right">51.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">40</td>
<td align="right">26.3%</td>
<td align="right">40</td>
<td align="right">26.0%</td>
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
<td align="right">676,800</td>
<td align="right">58.4%</td>
<td align="right">676,800</td>
<td align="right">58.4%</td>
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
<td align="right">481,920</td>
<td align="right">41.6%</td>
<td align="right">481,920</td>
<td align="right">41.6%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">200</td>
<td align="right">100.0%</td>
<td align="right">200</td>
<td align="right">100.0%</td>
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
<td align="right">80.0%</td>
<td align="right">160</td>
<td align="right">80.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">40</td>
<td align="right">20.0%</td>
<td align="right">40</td>
<td align="right">20.0%</td>
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
<td align="right">959,791</td>
<td align="right">36.4%</td>
<td align="right">945,491</td>
<td align="right">36.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,676,900</td>
<td align="right">63.6%</td>
<td align="right">1,676,903</td>
<td align="right">63.9%</td>
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
<td align="right">289</td>
<td align="right">100.0%</td>
<td align="right">285</td>
<td align="right">100.0%</td>
<td align="right">-1.4%</td>
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
<td align="left">set</td>
<td align="right">109</td>
<td align="right">37.7%</td>
<td align="right">105</td>
<td align="right">36.8%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">80</td>
<td align="right">27.7%</td>
<td align="right">80</td>
<td align="right">28.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">80</td>
<td align="right">27.7%</td>
<td align="right">80</td>
<td align="right">28.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">20</td>
<td align="right">6.9%</td>
<td align="right">20</td>
<td align="right">7.0%</td>
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
<td align="right">18,872,640</td>
<td align="right">33.0%</td>
<td align="right">18,872,640</td>
<td align="right">33.0%</td>
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
<td align="right">32,370,880</td>
<td align="right">56.6%</td>
<td align="right">32,370,880</td>
<td align="right">56.6%</td>
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
<td align="right">5,887,740</td>
<td align="right">10.3%</td>
<td align="right">5,887,740</td>
<td align="right">10.3%</td>
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
<td align="right">111,300</td>
<td align="right">82.7%</td>
<td align="right">111,300</td>
<td align="right">82.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">23,300</td>
<td align="right">17.3%</td>
<td align="right">23,300</td>
<td align="right">17.3%</td>
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
<td align="left">mutable class</td>
<td align="right">5,440</td>
<td align="right">23.3%</td>
<td align="right">5,440</td>
<td align="right">23.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,880</td>
<td align="right">20.9%</td>
<td align="right">4,880</td>
<td align="right">20.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">4,360</td>
<td align="right">18.7%</td>
<td align="right">4,360</td>
<td align="right">18.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">340</td>
<td align="right">1.5%</td>
<td align="right">340</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">280</td>
<td align="right">1.2%</td>
<td align="right">280</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">160</td>
<td align="right">0.7%</td>
<td align="right">160</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">160</td>
<td align="right">0.7%</td>
<td align="right">160</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
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
<td align="right">13,268,712</td>
<td align="right">100.0%</td>
<td align="right">13,271,809</td>
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
<td align="right">192,960</td>
<td align="right">100.0%</td>
<td align="right">192,960</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,671,080</td>
<td align="right">46.1%</td>
<td align="right">5,671,080</td>
<td align="right">46.1%</td>
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
<td align="right">6,614,360</td>
<td align="right">53.8%</td>
<td align="right">6,614,360</td>
<td align="right">53.8%</td>
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
<td align="right">940</td>
<td align="right">0.0%</td>
<td align="right">940</td>
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
<td align="right">1.0%</td>
<td align="right">20</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,040</td>
<td align="right">99.0%</td>
<td align="right">2,040</td>
<td align="right">99.0%</td>
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
<td align="right">7,380</td>
<td align="right">361.8%</td>
<td align="right">7,380</td>
<td align="right">361.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,400</td>
<td align="right">68.6%</td>
<td align="right">1,400</td>
<td align="right">68.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">200</td>
<td align="right">9.8%</td>
<td align="right">200</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">200</td>
<td align="right">9.8%</td>
<td align="right">200</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">160</td>
<td align="right">7.8%</td>
<td align="right">160</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">40</td>
<td align="right">2.0%</td>
<td align="right">40</td>
<td align="right">2.0%</td>
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
<td align="right">144,960</td>
<td align="right">11.1%</td>
<td align="right">144,960</td>
<td align="right">11.1%</td>
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
<td align="right">1,159,680</td>
<td align="right">88.9%</td>
<td align="right">1,159,680</td>
<td align="right">88.9%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
<td align="right">100.0%</td>
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
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,857,892</td>
<td align="right">16.0%</td>
<td align="right">2,860,929</td>
<td align="right">16.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">427,980</td>
<td align="right">2.4%</td>
<td align="right">428,010</td>
<td align="right">2.4%</td>
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
<td align="right">14,521,460</td>
<td align="right">81.4%</td>
<td align="right">14,521,484</td>
<td align="right">81.4%</td>
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
<td align="right">27,760</td>
<td align="right">77.5%</td>
<td align="right">27,748</td>
<td align="right">77.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,080</td>
<td align="right">22.5%</td>
<td align="right">8,083</td>
<td align="right">22.6%</td>
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
<td align="left">tuple</td>
<td align="right">17,920</td>
<td align="right">64.6%</td>
<td align="right">17,908</td>
<td align="right">64.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,840</td>
<td align="right">21.0%</td>
<td align="right">5,840</td>
<td align="right">21.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">3,520</td>
<td align="right">12.7%</td>
<td align="right">3,520</td>
<td align="right">12.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">180</td>
<td align="right">0.6%</td>
<td align="right">180</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.2%</td>
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
<td align="right">144,960</td>
<td align="right">4.2%</td>
<td align="right">144,960</td>
<td align="right">4.2%</td>
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
<td align="right">3,321,660</td>
<td align="right">95.8%</td>
<td align="right">3,321,660</td>
<td align="right">95.8%</td>
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
<td align="right">33.3%</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">40</td>
<td align="right">66.7%</td>
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
<td align="left">sequence</td>
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">209,105,771</td>
<td align="right">56.2%</td>
<td align="right">208,985,421</td>
<td align="right">56.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">31,000,827</td>
<td align="right">8.3%</td>
<td align="right">30,992,146</td>
<td align="right">8.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">124,155,823</td>
<td align="right">33.4%</td>
<td align="right">124,160,159</td>
<td align="right">33.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">7,601,219</td>
<td align="right">2.0%</td>
<td align="right">7,601,248</td>
<td align="right">2.0%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">959,791</td>
<td align="right">3.0%</td>
<td align="right">945,491</td>
<td align="right">2.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">504,243</td>
<td align="right">1.6%</td>
<td align="right">506,836</td>
<td align="right">1.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,857,892</td>
<td align="right">8.9%</td>
<td align="right">2,860,929</td>
<td align="right">8.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">18,872,640</td>
<td align="right">58.6%</td>
<td align="right">18,872,640</td>
<td align="right">58.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">5,671,080</td>
<td align="right">17.6%</td>
<td align="right">5,671,080</td>
<td align="right">17.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,405,120</td>
<td align="right">4.4%</td>
<td align="right">1,405,120</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">867,840</td>
<td align="right">2.7%</td>
<td align="right">867,840</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">676,800</td>
<td align="right">2.1%</td>
<td align="right">676,800</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">144,960</td>
<td align="right">0.5%</td>
<td align="right">144,960</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">144,960</td>
<td align="right">0.5%</td>
<td align="right">144,960</td>
<td align="right">0.5%</td>
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
<td align="left">TO_BOOL_LIST</td>
<td align="right">130,260</td>
<td align="right">1.7%</td>
<td align="right">130,290</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,498,920</td>
<td align="right">32.9%</td>
<td align="right">2,498,920</td>
<td align="right">32.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,308,000</td>
<td align="right">17.2%</td>
<td align="right">1,308,000</td>
<td align="right">17.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,284,720</td>
<td align="right">16.9%</td>
<td align="right">1,284,720</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">985,260</td>
<td align="right">13.0%</td>
<td align="right">985,260</td>
<td align="right">13.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">566,400</td>
<td align="right">7.5%</td>
<td align="right">566,400</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">224,720</td>
<td align="right">3.0%</td>
<td align="right">224,720</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">169,460</td>
<td align="right">2.2%</td>
<td align="right">169,460</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">102,820</td>
<td align="right">1.4%</td>
<td align="right">102,820</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">101,760</td>
<td align="right">1.3%</td>
<td align="right">101,760</td>
<td align="right">1.3%</td>
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
<td align="right">2,900,220</td>
<td align="right">19.6%</td>
<td align="right">2,900,220</td>
<td align="right">19.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">11,882,280</td>
<td align="right">80.4%</td>
<td align="right">11,882,280</td>
<td align="right">80.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,900,220</td>
<td align="right">19.6%</td>
<td align="right">2,900,220</td>
<td align="right">19.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">2,708,220</td>
<td align="right">18.3%</td>
<td align="right">2,708,220</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">192,000</td>
<td align="right">1.3%</td>
<td align="right">192,000</td>
<td align="right">1.3%</td>
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
<td align="right">2,708,220</td>
<td align="right">18.3%</td>
<td align="right">2,708,220</td>
<td align="right">18.3%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">820,860</td>
<td align="right">5.6%</td>
<td align="right">820,860</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">580,800</td>
<td align="right">3.9%</td>
<td align="right">580,800</td>
<td align="right">3.9%</td>
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
<td align="right">144,960</td>
<td align="right">1.0%</td>
<td align="right">144,960</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">15,267,300</td>
<td align="right">103.3%</td>
<td align="right">15,267,300</td>
<td align="right">103.3%</td>
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
<td align="right">225,257</td>
<td align="right"></td>
<td align="right">145,431</td>
<td align="right"></td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,418,048</td>
<td align="right"></td>
<td align="right">1,360,480</td>
<td align="right"></td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,192,791</td>
<td align="right"></td>
<td align="right">1,215,049</td>
<td align="right"></td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">5,784,083</td>
<td align="right"></td>
<td align="right">5,863,909</td>
<td align="right"></td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">28,891,069</td>
<td align="right"></td>
<td align="right">28,868,811</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">96,723,270</td>
<td align="right">22.5%</td>
<td align="right">96,661,250</td>
<td align="right">22.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">40,159,795</td>
<td align="right">9.3%</td>
<td align="right">40,182,499</td>
<td align="right">9.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">168,797,414</td>
<td align="right">42.9%</td>
<td align="right">168,715,956</td>
<td align="right">42.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">191,668,432</td>
<td align="right">44.6%</td>
<td align="right">191,576,723</td>
<td align="right">44.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">95,342,380</td>
<td align="right">24.2%</td>
<td align="right">95,306,418</td>
<td align="right">24.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">101,538,587</td>
<td align="right">23.6%</td>
<td align="right">101,512,877</td>
<td align="right">23.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">34,675,141</td>
<td align="right">8.8%</td>
<td align="right">34,667,217</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">94,858,482</td>
<td align="right">24.1%</td>
<td align="right">94,841,017</td>
<td align="right">24.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">145,249</td>
<td align="right">0.4%</td>
<td align="right">145,248</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">12,793,398</td>
<td align="right"></td>
<td align="right">12,793,389</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,991,843</td>
<td align="right">34.9%</td>
<td align="right">11,991,839</td>
<td align="right">34.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,846,594</td>
<td align="right">34.5%</td>
<td align="right">11,846,591</td>
<td align="right">34.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">22,324,232</td>
<td align="right"></td>
<td align="right">22,324,236</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">22,324,209</td>
<td align="right">65.1%</td>
<td align="right">22,324,212</td>
<td align="right">65.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,304,640</td>
<td align="right"></td>
<td align="right">1,304,640</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">338,880</td>
<td align="right">26.0%</td>
<td align="right">338,880</td>
<td align="right">26.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">144,960</td>
<td align="right">11.1%</td>
<td align="right">144,960</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
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
<td align="right">420</td>
<td align="right">1,052,700</td>
<td align="right">6,503,714</td>
<td align="right">23,705</td>
<td align="right">1,203,322</td>
<td align="right">420</td>
<td align="right">1,052,700</td>
<td align="right">6,504,067</td>
<td align="right">23,799</td>
<td align="right">1,203,306</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">49</td>
<td align="right">11.3%</td>
<td align="right">45</td>
<td align="right">10.4%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">2,455,264</td>
<td align="right"></td>
<td align="right">2,448,433</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">372</td>
<td align="right">86.1%</td>
<td align="right">371</td>
<td align="right">86.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">432</td>
<td align="right"></td>
<td align="right">431</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">102,904,902</td>
<td align="right">4,191.2%</td>
<td align="right">103,112,798</td>
<td align="right">4,211.4%</td>
<td align="right">0.2%</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">80</td>
<td align="right">18.5%</td>
<td align="right">80</td>
<td align="right">18.6%</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">2</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">60</td>
<td align="right">13.9%</td>
<td align="right">60</td>
<td align="right">13.9%</td>
<td align="right">0.0%</td>
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
<td align="right">372</td>
<td align="right"></td>
<td align="right">371</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">372</td>
<td align="right">100.0%</td>
<td align="right">371</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
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
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">358,376</td>
<td align="right">13.0%</td>
<td align="right">348,120</td>
<td align="right">13.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">1,822,202</td>
<td align="right">66.3%</td>
<td align="right">1,770,695</td>
<td align="right">66.0%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">2,748,416</td>
<td align="right"></td>
<td align="right">2,682,880</td>
<td align="right"></td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">567,838</td>
<td align="right">20.7%</td>
<td align="right">564,065</td>
<td align="right">21.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">573,440</td>
<td align="right">20.9%</td>
<td align="right">573,440</td>
<td align="right">21.4%</td>
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
<td align="left">183</td>
<td align="right">49.2%</td>
<td align="left">186</td>
<td align="right">50.1%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">100</td>
<td align="right">26.9%</td>
<td align="left">100</td>
<td align="right">27.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">80</td>
<td align="right">21.5%</td>
<td align="left">80</td>
<td align="right">21.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">9</td>
<td align="right">2.4%</td>
<td align="left">5</td>
<td align="right">1.3%</td>
<td align="right">-44.4%</td>
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
<td align="right">43</td>
<td align="right">11.6%</td>
<td align="right">43</td>
<td align="right">11.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">89</td>
<td align="right">23.9%</td>
<td align="right">88</td>
<td align="right">23.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">131</td>
<td align="right">35.2%</td>
<td align="right">135</td>
<td align="right">36.4%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">100</td>
<td align="right">26.9%</td>
<td align="right">100</td>
<td align="right">27.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">9</td>
<td align="right">2.4%</td>
<td align="right">5</td>
<td align="right">1.3%</td>
<td align="right">-44.4%</td>
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
<td align="right">21</td>
<td align="right">5.6%</td>
<td align="right">21</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">62</td>
<td align="right">16.7%</td>
<td align="right">62</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">80</td>
<td align="right">21.5%</td>
<td align="right">83</td>
<td align="right">22.4%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">122</td>
<td align="right">32.8%</td>
<td align="right">122</td>
<td align="right">32.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">87</td>
<td align="right">23.4%</td>
<td align="right">83</td>
<td align="right">22.4%</td>
<td align="right">-4.6%</td>
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
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">14,031</td>
<td align="right">7,795</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">6,948</td>
<td align="right">3,860</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">6,948</td>
<td align="right">3,860</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,948</td>
<td align="right">3,860</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">6,948</td>
<td align="right">3,860</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">13,431</td>
<td align="right">18,315</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">13,431</td>
<td align="right">18,315</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">68,174</td>
<td align="right">85,430</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">102,379</td>
<td align="right">120,735</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">42,911</td>
<td align="right">47,795</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">250,988</td>
<td align="right">277,180</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">29,968</td>
<td align="right">26,880</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">20,379</td>
<td align="right">22,175</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">83,951</td>
<td align="right">88,835</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,181,673</td>
<td align="right">1,232,476</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">74,637</td>
<td align="right">72,044</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">871,949</td>
<td align="right">886,249</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">1,792,712</td>
<td align="right">1,766,996</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,765,716</td>
<td align="right">1,789,274</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">5,763,869</td>
<td align="right">5,831,118</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,196,800</td>
<td align="right">2,214,674</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">621,491</td>
<td align="right">616,775</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">1,438,934</td>
<td align="right">1,428,641</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,309,672</td>
<td align="right">1,302,331</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">514,856</td>
<td align="right">512,340</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,721,153</td>
<td align="right">6,740,052</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">2,455,264</td>
<td align="right">2,448,433</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">2,455,264</td>
<td align="right">2,448,433</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,843,111</td>
<td align="right">3,833,976</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">4,652,064</td>
<td align="right">4,663,107</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,550,628</td>
<td align="right">1,547,537</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,662,128</td>
<td align="right">1,659,037</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">12,337,015</td>
<td align="right">12,351,209</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,304,271</td>
<td align="right">11,314,995</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">4,965,540</td>
<td align="right">4,965,531</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">4,965,540</td>
<td align="right">4,965,531</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,013,420</td>
<td align="right">9,013,405</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,358,720</td>
<td align="right">2,358,717</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">7,099,180</td>
<td align="right">7,099,171</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,382,100</td>
<td align="right">2,382,097</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,706,040</td>
<td align="right">2,706,037</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,706,040</td>
<td align="right">2,706,037</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">295,680</td>
<td align="right">295,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">289,920</td>
<td align="right">289,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">289,920</td>
<td align="right">289,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">144,960</td>
<td align="right">144,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">65,520</td>
<td align="right">65,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">52,500</td>
<td align="right">52,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">46,420</td>
<td align="right">46,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">46,420</td>
<td align="right">46,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">46,400</td>
<td align="right">46,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">29,480</td>
<td align="right">29,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">29,480</td>
<td align="right">29,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">29,480</td>
<td align="right">29,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">23,380</td>
<td align="right">23,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">23,020</td>
<td align="right">23,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">23,020</td>
<td align="right">23,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">23,020</td>
<td align="right">23,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">23,020</td>
<td align="right">23,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">23,020</td>
<td align="right">23,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">23,020</td>
<td align="right">23,020</td>
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
<td align="right">11</td>
<td align="right">15</td>
<td align="right">36.4%</td>
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
Stats gathered on: 2025-02-22
