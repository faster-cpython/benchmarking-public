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
<td align="left">COPY_FREE_VARS</td>
<td align="right">51,860</td>
<td align="right">1,085,180</td>
<td align="right">1,992.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">33,880</td>
<td align="right">541,400</td>
<td align="right">1,498.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">100,940</td>
<td align="right">536,080</td>
<td align="right">431.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">128,100</td>
<td align="right">599,320</td>
<td align="right">367.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">162,440</td>
<td align="right">709,580</td>
<td align="right">336.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">214,800</td>
<td align="right">844,280</td>
<td align="right">293.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">65,240</td>
<td align="right">228,440</td>
<td align="right">250.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">839,920</td>
<td align="right">2,814,860</td>
<td align="right">235.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">711,600</td>
<td align="right">1,759,700</td>
<td align="right">147.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,075,180</td>
<td align="right">2,530,400</td>
<td align="right">135.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">866,420</td>
<td align="right">1,998,280</td>
<td align="right">130.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">289,880</td>
<td align="right">516,060</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">42,900</td>
<td align="right">74,940</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">42,900</td>
<td align="right">74,940</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">935,000</td>
<td align="right">1,482,140</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">650,220</td>
<td align="right">1,022,960</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">117,300</td>
<td align="right">175,920</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,074,020</td>
<td align="right">3,080,340</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,125,000</td>
<td align="right">1,662,720</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">7,594,080</td>
<td align="right">11,165,020</td>
<td align="right">47.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,196,600</td>
<td align="right">4,690,100</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">741,740</td>
<td align="right">1,078,260</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,421,600</td>
<td align="right">4,915,100</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">6,945,180</td>
<td align="right">9,883,960</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,472,420</td>
<td align="right">4,934,060</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,618,420</td>
<td align="right">2,271,340</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">12,155,220</td>
<td align="right">16,493,180</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,708,060</td>
<td align="right">7,733,960</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">13,982,540</td>
<td align="right">18,821,200</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">4,477,820</td>
<td align="right">5,939,720</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">517,860</td>
<td align="right">681,060</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">13,857,080</td>
<td align="right">18,136,680</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">106,440</td>
<td align="right">138,480</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">27,728,760</td>
<td align="right">35,615,380</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,014,420</td>
<td align="right">6,427,820</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,485,320</td>
<td align="right">13,381,980</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">66,741,860</td>
<td align="right">85,150,500</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,714,720</td>
<td align="right">12,177,460</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">18,183,500</td>
<td align="right">22,755,960</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">6,382,180</td>
<td align="right">7,920,500</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,212,180</td>
<td align="right">2,722,760</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">11,665,280</td>
<td align="right">14,286,360</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">5,402,860</td>
<td align="right">6,606,140</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,627,780</td>
<td align="right">3,176,540</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">19,607,460</td>
<td align="right">23,697,620</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,078,540</td>
<td align="right">13,384,400</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">445,220</td>
<td align="right">363,300</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">22,148,340</td>
<td align="right">26,134,840</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">813,400</td>
<td align="right">958,500</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">110,180</td>
<td align="right">129,240</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,530,700</td>
<td align="right">1,759,980</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,590,680</td>
<td align="right">1,820,900</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,559,400</td>
<td align="right">1,750,500</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,983,280</td>
<td align="right">2,212,560</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,503,560</td>
<td align="right">8,118,560</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">21,051,220</td>
<td align="right">22,615,520</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">436,620</td>
<td align="right">468,680</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">39,920</td>
<td align="right">42,360</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">456,020</td>
<td align="right">475,080</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,442,980</td>
<td align="right">1,384,140</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,491,980</td>
<td align="right">1,543,560</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,534,860</td>
<td align="right">3,643,080</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">146,640</td>
<td align="right">150,400</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,228,220</td>
<td align="right">1,259,160</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,716,240</td>
<td align="right">1,748,280</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">132,380</td>
<td align="right">134,820</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,076,620</td>
<td align="right">3,131,620</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">911,360</td>
<td align="right">919,740</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">4,482,120</td>
<td align="right">4,510,440</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">752,880</td>
<td align="right">755,320</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">2,406,100</td>
<td align="right">2,411,640</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,587,540</td>
<td align="right">2,587,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,819,020</td>
<td align="right">7,819,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">7,521,960</td>
<td align="right">7,521,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,900,700</td>
<td align="right">3,900,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,949,480</td>
<td align="right">2,949,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,743,400</td>
<td align="right">2,743,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,453,800</td>
<td align="right">1,453,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,432,680</td>
<td align="right">1,432,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,301,280</td>
<td align="right">1,301,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">997,800</td>
<td align="right">997,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">912,080</td>
<td align="right">912,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">772,560</td>
<td align="right">772,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">772,560</td>
<td align="right">772,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">771,960</td>
<td align="right">771,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">756,180</td>
<td align="right">756,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">610,080</td>
<td align="right">610,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">448,560</td>
<td align="right">448,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">411,120</td>
<td align="right">411,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">336,120</td>
<td align="right">336,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">328,560</td>
<td align="right">328,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">324,360</td>
<td align="right">324,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">292,600</td>
<td align="right">292,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">259,200</td>
<td align="right">259,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">238,140</td>
<td align="right">238,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">236,400</td>
<td align="right">236,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">218,520</td>
<td align="right">218,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">216,420</td>
<td align="right">216,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">210,000</td>
<td align="right">210,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">185,040</td>
<td align="right">185,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">154,280</td>
<td align="right">154,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">148,020</td>
<td align="right">148,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">145,320</td>
<td align="right">145,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">133,980</td>
<td align="right">133,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">124,920</td>
<td align="right">124,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">99,480</td>
<td align="right">99,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">70,800</td>
<td align="right">70,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">69,180</td>
<td align="right">69,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">57,360</td>
<td align="right">57,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">57,360</td>
<td align="right">57,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">57,360</td>
<td align="right">57,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">56,520</td>
<td align="right">56,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">55,200</td>
<td align="right">55,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">53,340</td>
<td align="right">53,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">45,480</td>
<td align="right">45,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">28,460</td>
<td align="right">28,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">23,940</td>
<td align="right">23,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">23,400</td>
<td align="right">23,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">19,080</td>
<td align="right">19,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">14,560</td>
<td align="right">14,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">13,440</td>
<td align="right">13,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,220</td>
<td align="right">11,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">2,280</td>
<td align="right">2,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">840</td>
<td align="right">840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">220</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">120</td>
<td align="right">120</td>
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
<td align="right">14,280</td>
<td align="right">2.1%</td>
<td align="right">14,280</td>
<td align="right">2.1%</td>
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
<td align="right">651,300</td>
<td align="right">97.8%</td>
<td align="right">651,300</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">280</td>
<td align="right">100.0%</td>
<td align="right">280</td>
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
<td align="left">add other</td>
<td align="right">260</td>
<td align="right">92.9%</td>
<td align="right">260</td>
<td align="right">92.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">20</td>
<td align="right">7.1%</td>
<td align="right">20</td>
<td align="right">7.1%</td>
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
<td align="right">45,480</td>
<td align="right">100.0%</td>
<td align="right">45,480</td>
<td align="right">100.0%</td>
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
<td align="right">53,040</td>
<td align="right">2.8%</td>
<td align="right">53,040</td>
<td align="right">2.8%</td>
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
<td align="right">1,839,300</td>
<td align="right">96.9%</td>
<td align="right">1,839,300</td>
<td align="right">96.9%</td>
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
<td align="right">4,760</td>
<td align="right">0.3%</td>
<td align="right">4,760</td>
<td align="right">0.3%</td>
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
<td align="right">100</td>
<td align="right">26.3%</td>
<td align="right">100</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">280</td>
<td align="right">73.7%</td>
<td align="right">280</td>
<td align="right">73.7%</td>
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
<td align="left">list slice</td>
<td align="right">140</td>
<td align="right">50.0%</td>
<td align="right">140</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">21.4%</td>
<td align="right">60</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">40</td>
<td align="right">14.3%</td>
<td align="right">40</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">40</td>
<td align="right">14.3%</td>
<td align="right">40</td>
<td align="right">14.3%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">431,500</td>
<td align="right">0.7%</td>
<td align="right">485,460</td>
<td align="right">0.7%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">65,096,380</td>
<td align="right">99.3%</td>
<td align="right">65,055,880</td>
<td align="right">99.3%</td>
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
<td align="right">8,360</td>
<td align="right">100.0%</td>
<td align="right">9,360</td>
<td align="right">100.0%</td>
<td align="right">12.0%</td>
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
<td align="right">751,680</td>
<td align="right">48.2%</td>
<td align="right">754,120</td>
<td align="right">48.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">806,640</td>
<td align="right">51.7%</td>
<td align="right">806,640</td>
<td align="right">51.6%</td>
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
<td align="right">1,200</td>
<td align="right">100.0%</td>
<td align="right">1,200</td>
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
<td align="left">baseobject</td>
<td align="right">560</td>
<td align="right">46.7%</td>
<td align="right">560</td>
<td align="right">46.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">420</td>
<td align="right">35.0%</td>
<td align="right">420</td>
<td align="right">35.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">5.0%</td>
<td align="right">60</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right">40</td>
<td align="right">3.3%</td>
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
<td align="right">146,260</td>
<td align="right">25.7%</td>
<td align="right">150,020</td>
<td align="right">26.2%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">396,000</td>
<td align="right">69.7%</td>
<td align="right">396,000</td>
<td align="right">69.3%</td>
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
<td align="right">25,440</td>
<td align="right">4.5%</td>
<td align="right">25,440</td>
<td align="right">4.4%</td>
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
<td align="right">380</td>
<td align="right">100.0%</td>
<td align="right">380</td>
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
<td align="left">tuple</td>
<td align="right">220</td>
<td align="right">57.9%</td>
<td align="right">220</td>
<td align="right">57.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">160</td>
<td align="right">42.1%</td>
<td align="right">160</td>
<td align="right">42.1%</td>
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
<td align="right">3,225,160</td>
<td align="right">48.2%</td>
<td align="right">4,680,380</td>
<td align="right">48.7%</td>
<td align="right">45.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,470,600</td>
<td align="right">51.8%</td>
<td align="right">4,931,880</td>
<td align="right">51.3%</td>
<td align="right">42.1%</td>
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
<td align="right">1,820</td>
<td align="right">100.0%</td>
<td align="right">2,180</td>
<td align="right">100.0%</td>
<td align="right">19.8%</td>
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
<td align="left">dict items</td>
<td align="right">960</td>
<td align="right">52.7%</td>
<td align="right">1,320</td>
<td align="right">60.6%</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">200</td>
<td align="right">11.0%</td>
<td align="right">200</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">160</td>
<td align="right">8.8%</td>
<td align="right">160</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">160</td>
<td align="right">8.8%</td>
<td align="right">160</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">120</td>
<td align="right">6.6%</td>
<td align="right">120</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">80</td>
<td align="right">4.4%</td>
<td align="right">80</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">60</td>
<td align="right">3.3%</td>
<td align="right">60</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">2.2%</td>
<td align="right">40</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">40</td>
<td align="right">2.2%</td>
<td align="right">40</td>
<td align="right">1.8%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,984,140</td>
<td align="right">11.7%</td>
<td align="right">7,105,240</td>
<td align="right">15.3%</td>
<td align="right">42.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">432,220</td>
<td align="right">1.0%</td>
<td align="right">464,260</td>
<td align="right">1.0%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">37,020,740</td>
<td align="right">87.2%</td>
<td align="right">38,836,420</td>
<td align="right">83.7%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">330,720</td>
<td align="right">0.8%</td>
<td align="right">330,720</td>
<td align="right">0.7%</td>
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
<td align="right">94,080</td>
<td align="right">95.7%</td>
<td align="right">134,100</td>
<td align="right">96.9%</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,220</td>
<td align="right">4.3%</td>
<td align="right">4,240</td>
<td align="right">3.1%</td>
<td align="right">0.5%</td>
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
<td align="right">640</td>
<td align="right">15.2%</td>
<td align="right">660</td>
<td align="right">15.6%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3,440</td>
<td align="right">81.5%</td>
<td align="right">3,440</td>
<td align="right">81.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">80</td>
<td align="right">1.9%</td>
<td align="right">80</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.9%</td>
<td align="right">40</td>
<td align="right">0.9%</td>
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
<td align="right">43,312,780</td>
<td align="right">100.0%</td>
<td align="right">55,690,340</td>
<td align="right">100.0%</td>
<td align="right">28.6%</td>
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

### SEND

<details>
<summary> specialization stats for SEND family </summary>

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
<td align="right">3,608,760</td>
<td align="right">100.0%</td>
<td align="right">3,608,760</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,423,200</td>
<td align="right">43.9%</td>
<td align="right">1,456,680</td>
<td align="right">44.5%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,820,020</td>
<td align="right">56.1%</td>
<td align="right">1,815,100</td>
<td align="right">55.5%</td>
<td align="right">-0.3%</td>
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
<td align="right">27,060</td>
<td align="right">100.0%</td>
<td align="right">27,700</td>
<td align="right">100.0%</td>
<td align="right">2.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,169,400</td>
<td align="right">100.0%</td>
<td align="right">1,169,400</td>
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
<td align="right">100,440</td>
<td align="right">0.3%</td>
<td align="right">535,480</td>
<td align="right">1.4%</td>
<td align="right">433.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,018,660</td>
<td align="right">5.3%</td>
<td align="right">2,298,020</td>
<td align="right">5.9%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">35,941,320</td>
<td align="right">94.4%</td>
<td align="right">36,166,480</td>
<td align="right">92.7%</td>
<td align="right">0.6%</td>
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
<td align="right">1.2%</td>
<td align="right">560</td>
<td align="right">1.3%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">37,980</td>
<td align="right">98.8%</td>
<td align="right">43,260</td>
<td align="right">98.7%</td>
<td align="right">13.9%</td>
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
<td align="right">60</td>
<td align="right">13.0%</td>
<td align="right">160</td>
<td align="right">28.6%</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">320</td>
<td align="right">69.6%</td>
<td align="right">320</td>
<td align="right">57.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">40</td>
<td align="right">8.7%</td>
<td align="right">40</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">20</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">20</td>
<td align="right">3.6%</td>
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
<td align="right">11,160</td>
<td align="right">0.1%</td>
<td align="right">11,160</td>
<td align="right">0.1%</td>
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
<td align="right">11,735,100</td>
<td align="right">99.9%</td>
<td align="right">11,735,100</td>
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
<td align="left">other</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">5,034,400</td>
<td align="right">1.2%</td>
<td align="right">6,969,440</td>
<td align="right">1.4%</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">8,887,960</td>
<td align="right">2.2%</td>
<td align="right">11,375,760</td>
<td align="right">2.2%</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">216,265,620</td>
<td align="right">53.1%</td>
<td align="right">269,590,300</td>
<td align="right">53.2%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">177,450,040</td>
<td align="right">43.5%</td>
<td align="right">218,909,460</td>
<td align="right">43.2%</td>
<td align="right">23.4%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">100,440</td>
<td align="right">2.0%</td>
<td align="right">535,480</td>
<td align="right">7.7%</td>
<td align="right">433.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,470,600</td>
<td align="right">69.1%</td>
<td align="right">4,931,880</td>
<td align="right">70.9%</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">432,220</td>
<td align="right">8.6%</td>
<td align="right">464,260</td>
<td align="right">6.7%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">146,260</td>
<td align="right">2.9%</td>
<td align="right">150,020</td>
<td align="right">2.2%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">751,680</td>
<td align="right">15.0%</td>
<td align="right">754,120</td>
<td align="right">10.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">53,040</td>
<td align="right">1.1%</td>
<td align="right">53,040</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">45,480</td>
<td align="right">0.9%</td>
<td align="right">45,480</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">14,280</td>
<td align="right">0.3%</td>
<td align="right">14,280</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,160</td>
<td align="right">0.2%</td>
<td align="right">11,160</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">460,700</td>
<td align="right">5.2%</td>
<td align="right">885,440</td>
<td align="right">7.8%</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,330,960</td>
<td align="right">37.5%</td>
<td align="right">5,027,320</td>
<td align="right">44.2%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,295,420</td>
<td align="right">14.6%</td>
<td align="right">1,572,660</td>
<td align="right">13.8%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">224,240</td>
<td align="right">2.5%</td>
<td align="right">265,500</td>
<td align="right">2.3%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,423,200</td>
<td align="right">16.0%</td>
<td align="right">1,456,680</td>
<td align="right">12.8%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">483,060</td>
<td align="right">5.4%</td>
<td align="right">485,180</td>
<td align="right">4.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,142,680</td>
<td align="right">12.9%</td>
<td align="right">1,142,680</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">226,480</td>
<td align="right">2.5%</td>
<td align="right">226,480</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">198,300</td>
<td align="right">2.2%</td>
<td align="right">198,300</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">36,720</td>
<td align="right">0.4%</td>
<td align="right">36,720</td>
<td align="right">0.3%</td>
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
<td align="right">7,819,080</td>
<td align="right">21.6%</td>
<td align="right">7,819,080</td>
<td align="right">21.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">28,297,620</td>
<td align="right">78.4%</td>
<td align="right">28,297,620</td>
<td align="right">78.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,819,080</td>
<td align="right">21.6%</td>
<td align="right">7,819,080</td>
<td align="right">21.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">3,384,840</td>
<td align="right">9.4%</td>
<td align="right">3,384,840</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">4,434,240</td>
<td align="right">12.3%</td>
<td align="right">4,434,240</td>
<td align="right">12.3%</td>
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
<td align="right">3,384,840</td>
<td align="right">9.4%</td>
<td align="right">3,384,840</td>
<td align="right">9.4%</td>
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
<td align="right">801,360</td>
<td align="right">2.2%</td>
<td align="right">801,360</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">62,940</td>
<td align="right">0.2%</td>
<td align="right">62,940</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,401,020</td>
<td align="right">6.6%</td>
<td align="right">2,401,020</td>
<td align="right">6.6%</td>
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
<td align="right">57,360</td>
<td align="right">0.2%</td>
<td align="right">57,360</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">26,183,940</td>
<td align="right">72.5%</td>
<td align="right">26,183,940</td>
<td align="right">72.5%</td>
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
<td align="right">16,316</td>
<td align="right"></td>
<td align="right">11,975</td>
<td align="right"></td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">179,450,960</td>
<td align="right">27.7%</td>
<td align="right">223,871,860</td>
<td align="right">34.5%</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">39,628,380</td>
<td align="right">6.1%</td>
<td align="right">48,279,840</td>
<td align="right">7.4%</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">289,473,665</td>
<td align="right">44.6%</td>
<td align="right">242,148,152</td>
<td align="right">37.3%</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">233,223,100</td>
<td align="right">32.4%</td>
<td align="right">269,126,700</td>
<td align="right">37.4%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">300,863,149</td>
<td align="right">41.8%</td>
<td align="right">262,043,128</td>
<td align="right">36.4%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">43,523,560</td>
<td align="right">6.1%</td>
<td align="right">46,721,460</td>
<td align="right">6.5%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">9,597,086</td>
<td align="right"></td>
<td align="right">8,969,337</td>
<td align="right"></td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">503,873</td>
<td align="right"></td>
<td align="right">481,423</td>
<td align="right"></td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">139,873,087</td>
<td align="right">21.6%</td>
<td align="right">134,381,467</td>
<td align="right">20.7%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">487,854</td>
<td align="right"></td>
<td align="right">469,743</td>
<td align="right"></td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">57,400</td>
<td align="right">0.1%</td>
<td align="right">56,880</td>
<td align="right">0.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">47,265,304</td>
<td align="right"></td>
<td align="right">47,426,565</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">141,440,915</td>
<td align="right">19.7%</td>
<td align="right">141,203,314</td>
<td align="right">19.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">46,279,911</td>
<td align="right"></td>
<td align="right">46,270,386</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">45,392,940</td>
<td align="right">63.2%</td>
<td align="right">45,391,680</td>
<td align="right">63.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">45,335,340</td>
<td align="right">63.1%</td>
<td align="right">45,334,600</td>
<td align="right">63.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">26,414,520</td>
<td align="right">36.8%</td>
<td align="right">26,414,760</td>
<td align="right">36.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">26,451,240</td>
<td align="right"></td>
<td align="right">26,451,460</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">113,880</td>
<td align="right"></td>
<td align="right">113,880</td>
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
<td align="right">140</td>
<td align="right">162,780</td>
<td align="right">1,609,320</td>
<td align="right">140</td>
<td align="right">157,460</td>
<td align="right">1,610,840</td>
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
<td align="right">80</td>
<td align="right">1.5%</td>
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
<td align="right">3,720</td>
<td align="right">68.9%</td>
<td align="right">640</td>
<td align="right">47.8%</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">3,920</td>
<td align="right">72.6%</td>
<td align="right">760</td>
<td align="right">56.7%</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">5,400</td>
<td align="right"></td>
<td align="right">1,340</td>
<td align="right"></td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,680</td>
<td align="right">31.1%</td>
<td align="right">700</td>
<td align="right">52.2%</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">597,498,300</td>
<td align="right">1,788.1%</td>
<td align="right">415,319,180</td>
<td align="right">1,595.0%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">33,414,780</td>
<td align="right"></td>
<td align="right">26,038,460</td>
<td align="right"></td>
<td align="right">-22.1%</td>
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
<td align="right">40</td>
<td align="right">3.0%</td>
<td align="right">40 / 0 !!</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">40</td>
<td align="right">2.4%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,680</td>
<td align="right"></td>
<td align="right">700</td>
<td align="right"></td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,640</td>
<td align="right">97.6%</td>
<td align="right">700</td>
<td align="right">100.0%</td>
<td align="right">-57.3%</td>
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
<td align="right">400</td>
<td align="right">23.8%</td>
<td align="right">140</td>
<td align="right">20.0%</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">320</td>
<td align="right">19.0%</td>
<td align="right">120</td>
<td align="right">17.1%</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">220</td>
<td align="right">13.1%</td>
<td align="right">200</td>
<td align="right">28.6%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">180</td>
<td align="right">10.7%</td>
<td align="right">100</td>
<td align="right">14.3%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">440</td>
<td align="right">26.2%</td>
<td align="right">60</td>
<td align="right">8.6%</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">120</td>
<td align="right">7.1%</td>
<td align="right">80</td>
<td align="right">11.4%</td>
<td align="right">-33.3%</td>
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
<td align="right">200</td>
<td align="right">11.9%</td>
<td align="right">100</td>
<td align="right">14.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">320</td>
<td align="right">19.0%</td>
<td align="right">160</td>
<td align="right">22.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">340</td>
<td align="right">20.2%</td>
<td align="right">120</td>
<td align="right">17.1%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">200</td>
<td align="right">11.9%</td>
<td align="right">120</td>
<td align="right">17.1%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">340</td>
<td align="right">20.2%</td>
<td align="right">80</td>
<td align="right">11.4%</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">200</td>
<td align="right">11.9%</td>
<td align="right">120</td>
<td align="right">17.1%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">40</td>
<td align="right">2.4%</td>
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
<td align="left">_LOAD_ATTR</td>
<td align="right">2,652,240</td>
<td align="right">1,160</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">22,060</td>
<td align="right">3,000</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">731,880</td>
<td align="right">137,160</td>
<td align="right">-81.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">23,560</td>
<td align="right">4,500</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">850,580</td>
<td align="right">184,660</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">687,920</td>
<td align="right">180,400</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,384,260</td>
<td align="right">377,940</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">475,240</td>
<td align="right">138,720</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">3,600</td>
<td align="right">1,160</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">701,640</td>
<td align="right">230,420</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">558,900</td>
<td align="right">186,160</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">954,600</td>
<td align="right">325,120</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">756,100</td>
<td align="right">269,740</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">41,680</td>
<td align="right">15,240</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">367,280</td>
<td align="right">138,000</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">364,180</td>
<td align="right">138,000</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,718,900</td>
<td align="right">1,413,040</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,692,160</td>
<td align="right">658,840</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,732,300</td>
<td align="right">1,496,900</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,455,360</td>
<td align="right">993,460</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">914,380</td>
<td align="right">376,900</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">5,024,640</td>
<td align="right">2,085,860</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">14,380</td>
<td align="right">6,000</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,182,880</td>
<td align="right">918,180</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">11,787,960</td>
<td align="right">5,225,960</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,130,520</td>
<td align="right">998,660</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">869,960</td>
<td align="right">438,340</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">6,321,320</td>
<td align="right">3,186,200</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,523,380</td>
<td align="right">1,842,980</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,183,780</td>
<td align="right">635,020</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">4,338,380</td>
<td align="right">2,363,440</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">5,102,520</td>
<td align="right">2,788,680</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">3,112,580</td>
<td align="right">1,719,680</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">7,964,160</td>
<td align="right">4,530,700</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,813,440</td>
<td align="right">1,604,400</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,455,260</td>
<td align="right">1,407,160</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">3,400,100</td>
<td align="right">1,949,060</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">3,399,000</td>
<td align="right">1,959,280</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">3,391,340</td>
<td align="right">1,968,620</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">8,105,120</td>
<td align="right">4,753,360</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">16,890,800</td>
<td align="right">9,917,520</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,296,480</td>
<td align="right">768,660</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">5,548,600</td>
<td align="right">3,370,900</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">7,226,660</td>
<td align="right">4,393,540</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">131,040</td>
<td align="right">82,860</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">5,549,260</td>
<td align="right">3,523,360</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,478,340</td>
<td align="right">2,246,100</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">37,049,640</td>
<td align="right">24,549,960</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">5,198,120</td>
<td align="right">3,447,940</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">4,866,820</td>
<td align="right">3,235,620</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">60</td>
<td align="right">40</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">12,083,300</td>
<td align="right">8,184,620</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,716,800</td>
<td align="right">1,847,260</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">18,584,460</td>
<td align="right">12,674,620</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">13,020,140</td>
<td align="right">8,942,520</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,694,100</td>
<td align="right">1,858,580</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,694,100</td>
<td align="right">1,858,580</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">13,906,480</td>
<td align="right">9,626,880</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5,132,720</td>
<td align="right">3,568,420</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">56,160,180</td>
<td align="right">39,162,900</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">14,902,440</td>
<td align="right">10,551,280</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">4,728,580</td>
<td align="right">3,363,160</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">307,140</td>
<td align="right">220,020</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">307,140</td>
<td align="right">220,020</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">307,140</td>
<td align="right">220,020</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,794,100</td>
<td align="right">10,648,160</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,330,120</td>
<td align="right">3,176,720</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,731,080</td>
<td align="right">1,274,880</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">744,600</td>
<td align="right">559,480</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">11,827,220</td>
<td align="right">8,900,360</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">550,400</td>
<td align="right">414,720</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">550,400</td>
<td align="right">414,720</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">999,280</td>
<td align="right">762,840</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">999,280</td>
<td align="right">762,840</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">29,295,500</td>
<td align="right">22,384,500</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,356,060</td>
<td align="right">4,862,560</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">12,177,040</td>
<td align="right">9,485,860</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">33,414,780</td>
<td align="right">26,038,460</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">14,354,100</td>
<td align="right">11,209,560</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">35,431,480</td>
<td align="right">27,822,560</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,721,640</td>
<td align="right">5,280,720</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">10,743,640</td>
<td align="right">8,479,220</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">2,673,760</td>
<td align="right">2,126,620</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">7,201,580</td>
<td align="right">5,746,360</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">7,201,580</td>
<td align="right">5,746,360</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">602,200</td>
<td align="right">490,920</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">602,200</td>
<td align="right">490,920</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">602,200</td>
<td align="right">490,920</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">921,720</td>
<td align="right">758,520</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">921,720</td>
<td align="right">758,520</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">6,309,860</td>
<td align="right">5,335,740</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">3,587,860</td>
<td align="right">3,083,860</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">10,901,740</td>
<td align="right">9,440,460</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,016,700</td>
<td align="right">1,784,100</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">4,119,220</td>
<td align="right">3,653,920</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">19,108,300</td>
<td align="right">17,191,300</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">51,260</td>
<td align="right">47,500</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">51,260</td>
<td align="right">47,500</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,570,300</td>
<td align="right">1,462,080</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">1,445,380</td>
<td align="right">1,527,300</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">1,527,340</td>
<td align="right">1,475,760</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,392,340</td>
<td align="right">4,350,360</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">728,640</td>
<td align="right">728,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">187,560</td>
<td align="right">187,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">187,560</td>
<td align="right">187,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">112,880</td>
<td align="right">112,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">111,380</td>
<td align="right">111,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">58,620</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">32,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">32,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">32,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">32,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">30,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">30,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">28,320</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">27,920</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">19,060</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">5,540</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">3,000</td>
<td align="right">3,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,000</td>
<td align="right">3,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,000</td>
<td align="right">3,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">2,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">2,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,500</td>
<td align="right">1,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,500</td>
<td align="right">1,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,500</td>
<td align="right">1,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,500</td>
<td align="right">1,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">1,500</td>
<td align="right">1,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">80</td>
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
<td align="right">140</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">80</td>
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
Stats gathered on: 2024-11-22
