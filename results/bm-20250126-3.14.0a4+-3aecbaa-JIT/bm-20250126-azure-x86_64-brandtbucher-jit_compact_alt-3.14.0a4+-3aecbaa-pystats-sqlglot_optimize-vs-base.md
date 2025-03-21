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
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">72,040</td>
<td align="right">925,400</td>
<td align="right">1,184.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,608,400</td>
<td align="right">6,339,140</td>
<td align="right">294.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,359,740</td>
<td align="right">3,389,480</td>
<td align="right">149.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">2,411,640</td>
<td align="right">320</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">216,420</td>
<td align="right">120</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,543,560</td>
<td align="right">1,920</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">411,120</td>
<td align="right">700</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">18,840</td>
<td align="right">40</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">238,140</td>
<td align="right">620</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">210,000</td>
<td align="right">720</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,127,380</td>
<td align="right">4,440</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">56,520</td>
<td align="right">520</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">193,920</td>
<td align="right">2,040</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,453,800</td>
<td align="right">15,480</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">23,940</td>
<td align="right">260</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">354,820</td>
<td align="right">4,440</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">175,920</td>
<td align="right">2,520</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">385,920</td>
<td align="right">9,460</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,513,580</td>
<td align="right">67,080</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">13,440</td>
<td align="right">820</td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">328,560</td>
<td align="right">20,280</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">448,560</td>
<td align="right">30,720</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">23,400</td>
<td align="right">1,800</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">463,040</td>
<td align="right">36,860</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,259,160</td>
<td align="right">105,680</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">783,700</td>
<td align="right">66,380</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">19,080</td>
<td align="right">1,920</td>
<td align="right">-89.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,886,080</td>
<td align="right">610,540</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,077,740</td>
<td align="right">114,800</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">475,080</td>
<td align="right">52,180</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,001,920</td>
<td align="right">222,000</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">150,400</td>
<td align="right">19,820</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">755,320</td>
<td align="right">112,100</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">524,660</td>
<td align="right">967,620</td>
<td align="right">84.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">14,560</td>
<td align="right">2,680</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,949,480</td>
<td align="right">574,320</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">99,480</td>
<td align="right">20,040</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">133,980</td>
<td align="right">27,720</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">958,500</td>
<td align="right">210,960</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">600,240</td>
<td align="right">138,920</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">236,400</td>
<td align="right">64,560</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">22,359,360</td>
<td align="right">6,216,460</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">124,920</td>
<td align="right">35,640</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,876,100</td>
<td align="right">830,400</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,756,020</td>
<td align="right">8,137,640</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,220</td>
<td align="right">3,280</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,432,680</td>
<td align="right">429,120</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">24,793,500</td>
<td align="right">8,611,200</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">2,280</td>
<td align="right">800</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">515,540</td>
<td align="right">189,340</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,647,600</td>
<td align="right">7,139,780</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">138,480</td>
<td align="right">56,680</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,940,060</td>
<td align="right">1,215,740</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,440</td>
<td align="right">600</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">644,620</td>
<td align="right">1,017,740</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">15,993,900</td>
<td align="right">6,869,820</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">7,521,960</td>
<td align="right">3,307,520</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">7,093,920</td>
<td align="right">3,406,000</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">53,340</td>
<td align="right">26,220</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">19,980</td>
<td align="right">10,240</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">6,217,780</td>
<td align="right">3,268,260</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">17,300,700</td>
<td align="right">9,260,600</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">259,200</td>
<td align="right">378,800</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">7,408,940</td>
<td align="right">4,008,880</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">80,611,300</td>
<td align="right">44,341,860</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">21,731,300</td>
<td align="right">11,994,740</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">771,960</td>
<td align="right">429,120</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">264,380</td>
<td align="right">148,620</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">10,287,900</td>
<td align="right">5,825,740</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">22,528,400</td>
<td align="right">12,773,480</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">74,940</td>
<td align="right">42,860</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">74,940</td>
<td align="right">42,860</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,131,620</td>
<td align="right">1,800,220</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">12,838,000</td>
<td align="right">7,542,720</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">756,180</td>
<td align="right">449,860</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">445,200</td>
<td align="right">624,360</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">33,975,620</td>
<td align="right">20,437,380</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,102,240</td>
<td align="right">7,929,340</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">494,220</td>
<td align="right">688,720</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">997,800</td>
<td align="right">612,340</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">33,600,620</td>
<td align="right">20,731,560</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">70,800</td>
<td align="right">44,160</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,693,080</td>
<td align="right">3,559,740</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">941,040</td>
<td align="right">590,760</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">919,740</td>
<td align="right">580,380</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">130,020</td>
<td align="right">82,300</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,471,220</td>
<td align="right">6,019,480</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">28,460</td>
<td align="right">18,860</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">13,786,340</td>
<td align="right">9,150,460</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,021,680</td>
<td align="right">5,433,600</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">154,280</td>
<td align="right">200,520</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,587,620</td>
<td align="right">1,817,900</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,696,220</td>
<td align="right">6,002,080</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">9,391,200</td>
<td align="right">6,897,220</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">2,212,040</td>
<td align="right">1,635,860</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,759,460</td>
<td align="right">1,324,900</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">324,360</td>
<td align="right">244,300</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,582,400</td>
<td align="right">1,199,300</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">129,240</td>
<td align="right">101,040</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,643,080</td>
<td align="right">2,884,040</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,557,420</td>
<td align="right">2,032,660</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,896,260</td>
<td align="right">3,181,860</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">134,820</td>
<td align="right">115,660</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,748,280</td>
<td align="right">1,506,820</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">292,600</td>
<td align="right">253,440</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,301,280</td>
<td align="right">1,147,440</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">42,360</td>
<td align="right">37,720</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">4,510,440</td>
<td align="right">4,179,680</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">2,240,080</td>
<td align="right">2,084,800</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,357,980</td>
<td align="right">2,511,820</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,579,000</td>
<td align="right">2,419,300</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">912,080</td>
<td align="right">863,440</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,362,140</td>
<td align="right">1,425,260</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,801,020</td>
<td align="right">8,083,800</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,743,400</td>
<td align="right">2,731,740</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">9,376,320</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">772,560</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">772,560</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">336,120</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">277,980</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">218,520</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">145,320</td>
<td align="right">145,320</td>
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
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">55,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">45,480</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">18,840</td>
<td align="right">18,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">720</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">2,520</td>
<td align="right">0.4%</td>
<td align="right">-82.4%</td>
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
<td align="right">646,740</td>
<td align="right">99.6%</td>
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
<td align="left">Failure</td>
<td align="right">280</td>
<td align="right">100.0%</td>
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">-42.9%</td>
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
<td align="left">add other</td>
<td align="right">260</td>
<td align="right">92.9%</td>
<td align="right">140</td>
<td align="right">87.5%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">20</td>
<td align="right">7.1%</td>
<td align="right">20</td>
<td align="right">12.5%</td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">26,040</td>
<td align="right">1.4%</td>
<td align="right">-50.9%</td>
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
<td align="right">98.3%</td>
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
<td align="left">Failure</td>
<td align="right">280</td>
<td align="right">73.7%</td>
<td align="right">160</td>
<td align="right">61.5%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">100</td>
<td align="right">26.3%</td>
<td align="right">100</td>
<td align="right">38.5%</td>
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
<td align="right">60</td>
<td align="right">37.5%</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">21.4%</td>
<td align="right">60</td>
<td align="right">37.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">40</td>
<td align="right">14.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">40</td>
<td align="right">14.3%</td>
<td align="right">40</td>
<td align="right">25.0%</td>
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
<td align="right">478,020</td>
<td align="right">0.7%</td>
<td align="right">470,200</td>
<td align="right">0.7%</td>
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
<td align="right">65,069,440</td>
<td align="right">99.3%</td>
<td align="right">65,080,660</td>
<td align="right">99.3%</td>
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
<td align="right">9,220</td>
<td align="right">100.0%</td>
<td align="right">9,100</td>
<td align="right">100.0%</td>
<td align="right">-1.3%</td>
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
<td align="right">754,120</td>
<td align="right">48.3%</td>
<td align="right">111,840</td>
<td align="right">15.5%</td>
<td align="right">-85.2%</td>
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
<td align="right">51.6%</td>
<td align="right">611,040</td>
<td align="right">84.5%</td>
<td align="right">-24.2%</td>
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
<td align="right">1,200</td>
<td align="right">100.0%</td>
<td align="right">260</td>
<td align="right">100.0%</td>
<td align="right">-78.3%</td>
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
<td align="left">baseobject</td>
<td align="right">560</td>
<td align="right">46.7%</td>
<td align="right">60</td>
<td align="right">23.1%</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">420</td>
<td align="right">35.0%</td>
<td align="right">80</td>
<td align="right">30.8%</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">5.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right">40</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right">40</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">40</td>
<td align="right">3.3%</td>
<td align="right">40</td>
<td align="right">15.4%</td>
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
<td align="right">150,020</td>
<td align="right">25.8%</td>
<td align="right">19,680</td>
<td align="right">4.4%</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">404,880</td>
<td align="right">69.7%</td>
<td align="right">429,600</td>
<td align="right">95.6%</td>
<td align="right">6.1%</td>
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
<td align="right">4.4%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">480</td>
<td align="right">55.8%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">380</td>
<td align="right">44.2%</td>
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">-63.2%</td>
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
<td align="right">160</td>
<td align="right">42.1%</td>
<td align="right">40</td>
<td align="right">28.6%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">220</td>
<td align="right">57.9%</td>
<td align="right">100</td>
<td align="right">71.4%</td>
<td align="right">-54.5%</td>
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
<td align="right">4,753,880</td>
<td align="right">51.3%</td>
<td align="right">8,135,040</td>
<td align="right">63.0%</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,507,960</td>
<td align="right">48.7%</td>
<td align="right">4,781,400</td>
<td align="right">37.0%</td>
<td align="right">6.1%</td>
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
<td align="right">2,140</td>
<td align="right">100.0%</td>
<td align="right">2,600</td>
<td align="right">100.0%</td>
<td align="right">21.5%</td>
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
<td align="left">dict keys</td>
<td align="right">160</td>
<td align="right">7.5%</td>
<td align="right">40</td>
<td align="right">1.5%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">120</td>
<td align="right">5.6%</td>
<td align="right">40</td>
<td align="right">1.5%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,280</td>
<td align="right">59.8%</td>
<td align="right">2,000</td>
<td align="right">76.9%</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">60</td>
<td align="right">2.8%</td>
<td align="right">80</td>
<td align="right">3.1%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">160</td>
<td align="right">7.5%</td>
<td align="right">120</td>
<td align="right">4.6%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">200</td>
<td align="right">9.3%</td>
<td align="right">200</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">80</td>
<td align="right">3.7%</td>
<td align="right">80</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">1.9%</td>
<td align="right">40</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">40</td>
<td align="right">1.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">458,800</td>
<td align="right">1.0%</td>
<td align="right">35,280</td>
<td align="right">0.1%</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,872,940</td>
<td align="right">13.2%</td>
<td align="right">6,067,860</td>
<td align="right">13.6%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">38,187,820</td>
<td align="right">85.8%</td>
<td align="right">38,459,220</td>
<td align="right">86.3%</td>
<td align="right">0.7%</td>
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
<td align="right">0.7%</td>
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
<td align="left">Failure</td>
<td align="right">4,140</td>
<td align="right">3.6%</td>
<td align="right">1,480</td>
<td align="right">1.3%</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">110,880</td>
<td align="right">96.4%</td>
<td align="right">114,540</td>
<td align="right">98.7%</td>
<td align="right">3.3%</td>
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
<td align="right">3,440</td>
<td align="right">83.1%</td>
<td align="right">1,020</td>
<td align="right">68.9%</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">660</td>
<td align="right">15.9%</td>
<td align="right">420</td>
<td align="right">28.4%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">40</td>
<td align="right">1.0%</td>
<td align="right">40</td>
<td align="right">2.7%</td>
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
<td align="right">52,876,980</td>
<td align="right">100.0%</td>
<td align="right">78,649,440</td>
<td align="right">100.0%</td>
<td align="right">48.7%</td>
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

### LOAD_METHOD

<details>
<summary> specialization stats for LOAD_METHOD family </summary>

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
<td align="right">19,740</td>
<td align="right">2.2%</td>
<td align="right">10,100</td>
<td align="right">1.3%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">872,540</td>
<td align="right">97.8%</td>
<td align="right">793,240</td>
<td align="right">98.7%</td>
<td align="right">-9.1%</td>
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
<td align="right">160</td>
<td align="right">1.0%</td>
<td align="right">60</td>
<td align="right">0.4%</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,440</td>
<td align="right">99.0%</td>
<td align="right">14,920</td>
<td align="right">99.6%</td>
<td align="right">-9.2%</td>
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
<td align="right">140</td>
<td align="right">87.5%</td>
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">-71.4%</td>
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
<td align="right">1,456,680</td>
<td align="right">44.5%</td>
<td align="right">1,332,940</td>
<td align="right">40.8%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,815,100</td>
<td align="right">55.5%</td>
<td align="right">1,934,920</td>
<td align="right">59.2%</td>
<td align="right">6.6%</td>
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
<td align="right">27,700</td>
<td align="right">100.0%</td>
<td align="right">25,340</td>
<td align="right">100.0%</td>
<td align="right">-8.5%</td>
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
<td align="right">263,880</td>
<td align="right">0.7%</td>
<td align="right">148,380</td>
<td align="right">0.4%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,200,940</td>
<td align="right">5.7%</td>
<td align="right">1,993,560</td>
<td align="right">5.2%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">35,994,500</td>
<td align="right">93.6%</td>
<td align="right">36,073,900</td>
<td align="right">94.4%</td>
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
<td align="right">460</td>
<td align="right">1.1%</td>
<td align="right">220</td>
<td align="right">0.6%</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,420</td>
<td align="right">98.9%</td>
<td align="right">37,580</td>
<td align="right">99.4%</td>
<td align="right">-9.3%</td>
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
<td align="right">8.7%</td>
<td align="right">100</td>
<td align="right">45.5%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">320</td>
<td align="right">69.6%</td>
<td align="right">100</td>
<td align="right">45.5%</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">13.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">20</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">3,240</td>
<td align="right">0.0%</td>
<td align="right">-71.0%</td>
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
<td align="right">11,437,500</td>
<td align="right">100.0%</td>
<td align="right">-2.5%</td>
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
<td align="left">other</td>
<td align="right">40</td>
<td align="right">100.0%</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">-50.0%</td>
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
<td align="right">211,394,360</td>
<td align="right">41.0%</td>
<td align="right">116,462,060</td>
<td align="right">39.4%</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">286,823,700</td>
<td align="right">55.6%</td>
<td align="right">160,151,880</td>
<td align="right">54.1%</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">6,534,040</td>
<td align="right">1.3%</td>
<td align="right">8,497,760</td>
<td align="right">2.9%</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">10,911,500</td>
<td align="right">2.1%</td>
<td align="right">10,662,660</td>
<td align="right">3.6%</td>
<td align="right">-2.3%</td>
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
<td align="right">45,480</td>
<td align="right">0.7%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">458,800</td>
<td align="right">7.0%</td>
<td align="right">35,280</td>
<td align="right">0.4%</td>
<td align="right">-92.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">150,020</td>
<td align="right">2.3%</td>
<td align="right">19,680</td>
<td align="right">0.2%</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">754,120</td>
<td align="right">11.6%</td>
<td align="right">111,840</td>
<td align="right">1.3%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">14,280</td>
<td align="right">0.2%</td>
<td align="right">2,520</td>
<td align="right">0.0%</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,753,880</td>
<td align="right">72.9%</td>
<td align="right">8,135,040</td>
<td align="right">95.8%</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">11,160</td>
<td align="right">0.2%</td>
<td align="right">3,240</td>
<td align="right">0.0%</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">53,040</td>
<td align="right">0.8%</td>
<td align="right">26,040</td>
<td align="right">0.3%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">19,740</td>
<td align="right">0.3%</td>
<td align="right">10,100</td>
<td align="right">0.1%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">263,880</td>
<td align="right">4.0%</td>
<td align="right">148,380</td>
<td align="right">1.7%</td>
<td align="right">-43.8%</td>
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
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">36,720</td>
<td align="right">0.3%</td>
<td align="right">21,360</td>
<td align="right">0.2%</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">487,300</td>
<td align="right">4.5%</td>
<td align="right">404,260</td>
<td align="right">3.8%</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">226,480</td>
<td align="right">2.1%</td>
<td align="right">190,700</td>
<td align="right">1.8%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">872,420</td>
<td align="right">8.0%</td>
<td align="right">793,120</td>
<td align="right">7.4%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,456,680</td>
<td align="right">13.3%</td>
<td align="right">1,332,940</td>
<td align="right">12.5%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">198,300</td>
<td align="right">1.8%</td>
<td align="right">187,460</td>
<td align="right">1.8%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,473,460</td>
<td align="right">13.5%</td>
<td align="right">1,395,480</td>
<td align="right">13.1%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,680,580</td>
<td align="right">42.9%</td>
<td align="right">4,898,360</td>
<td align="right">45.9%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">265,500</td>
<td align="right">2.4%</td>
<td align="right">276,020</td>
<td align="right">2.6%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,142,680</td>
<td align="right">10.5%</td>
<td align="right">1,135,420</td>
<td align="right">10.6%</td>
<td align="right">-0.6%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,401,020</td>
<td align="right">6.6%</td>
<td align="right">2,683,800</td>
<td align="right">7.4%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">3,366,840</td>
<td align="right">9.3%</td>
<td align="right">3,649,620</td>
<td align="right">10.1%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">3,366,840</td>
<td align="right">9.3%</td>
<td align="right">3,649,620</td>
<td align="right">10.1%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,801,080</td>
<td align="right">21.6%</td>
<td align="right">8,083,860</td>
<td align="right">22.4%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,801,080</td>
<td align="right">21.6%</td>
<td align="right">8,083,860</td>
<td align="right">22.4%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">28,315,620</td>
<td align="right">78.4%</td>
<td align="right">28,032,840</td>
<td align="right">77.6%</td>
<td align="right">-1.0%</td>
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
<td align="right">26,201,940</td>
<td align="right">72.5%</td>
<td align="right">26,201,940</td>
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
<td align="left">Allocations over 4 kbytes</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">1,300</td>
<td align="right">0.0%</td>
<td align="right">282.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">14,399</td>
<td align="right"></td>
<td align="right">21,355</td>
<td align="right"></td>
<td align="right">48.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">212,738,320</td>
<td align="right">32.9%</td>
<td align="right">129,975,400</td>
<td align="right">20.4%</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">254,964,175</td>
<td align="right">39.4%</td>
<td align="right">316,548,206</td>
<td align="right">49.8%</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">259,738,280</td>
<td align="right">36.1%</td>
<td align="right">203,769,840</td>
<td align="right">29.6%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">45,395,860</td>
<td align="right">6.3%</td>
<td align="right">38,249,960</td>
<td align="right">5.6%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">273,184,047</td>
<td align="right">38.0%</td>
<td align="right">308,272,129</td>
<td align="right">44.8%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">46,062,740</td>
<td align="right">7.1%</td>
<td align="right">40,263,080</td>
<td align="right">6.3%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">133,517,111</td>
<td align="right">20.6%</td>
<td align="right">148,870,812</td>
<td align="right">23.4%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">493,714</td>
<td align="right"></td>
<td align="right">545,594</td>
<td align="right"></td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">479,544</td>
<td align="right"></td>
<td align="right">524,524</td>
<td align="right"></td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">9,070,276</td>
<td align="right"></td>
<td align="right">9,707,436</td>
<td align="right"></td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">141,005,499</td>
<td align="right">19.6%</td>
<td align="right">138,268,589</td>
<td align="right">20.1%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">57,020</td>
<td align="right">0.1%</td>
<td align="right">57,800</td>
<td align="right">0.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">42,974,440</td>
<td align="right">59.8%</td>
<td align="right">43,275,980</td>
<td align="right">60.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">42,917,080</td>
<td align="right">59.8%</td>
<td align="right">43,216,880</td>
<td align="right">59.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">43,935,075</td>
<td align="right"></td>
<td align="right">44,234,919</td>
<td align="right"></td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">46,198,581</td>
<td align="right"></td>
<td align="right">46,099,105</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">28,835,420</td>
<td align="right">40.2%</td>
<td align="right">28,834,880</td>
<td align="right">40.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">28,834,980</td>
<td align="right"></td>
<td align="right">28,835,400</td>
<td align="right"></td>
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
<td align="right">140</td>
<td align="right">189,800</td>
<td align="right">1,701,580</td>
<td align="right">76,540</td>
<td align="right">247,200</td>
<td align="right">140</td>
<td align="right">190,380</td>
<td align="right">1,738,980</td>
<td align="right">67,440</td>
<td align="right">254,680</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">513,931,880</td>
<td align="right">1,712.3%</td>
<td align="right">1,182,173,180</td>
<td align="right">2,131.9%</td>
<td align="right">130.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">2,240</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">840</td>
<td align="right">37.5%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,580</td>
<td align="right">70.5%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,400</td>
<td align="right">62.5%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">20</td>
<td align="right">0.9%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">60</td>
<td align="right">2.7%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">30,013,640</td>
<td align="right"></td>
<td align="right">55,451,000</td>
<td align="right"></td>
<td align="right">84.8%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right">840</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">840</td>
<td align="right">100.0%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">60</td>
<td align="right">7.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">200</td>
<td align="right">23.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">220</td>
<td align="right">26.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">120</td>
<td align="right">14.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">80</td>
<td align="right">9.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">160</td>
<td align="right">19.0%</td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">40</td>
<td align="right">4.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">160</td>
<td align="right">19.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">100</td>
<td align="right">11.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">200</td>
<td align="right">23.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">100</td>
<td align="right">11.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">21.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">60</td>
<td align="right">7.1%</td>
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
<td align="left">_DEOPT</td>
<td align="right">60</td>
<td align="right">189,380</td>
<td align="right">315,533.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">1,160</td>
<td align="right">839,040</td>
<td align="right">72,231.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,500</td>
<td align="right">715,900</td>
<td align="right">47,626.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">4,500</td>
<td align="right">1,048,960</td>
<td align="right">23,210.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,500</td>
<td align="right">307,220</td>
<td align="right">20,381.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,500</td>
<td align="right">217,560</td>
<td align="right">14,404.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,000</td>
<td align="right">422,300</td>
<td align="right">13,976.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,000</td>
<td align="right">409,100</td>
<td align="right">13,536.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">3,000</td>
<td align="right">339,120</td>
<td align="right">11,204.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">15,240</td>
<td align="right">1,342,720</td>
<td align="right">8,710.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,500</td>
<td align="right">107,760</td>
<td align="right">7,084.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">490,920</td>
<td align="right">33,310,560</td>
<td align="right">6,685.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">490,920</td>
<td align="right">33,170,640</td>
<td align="right">6,656.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">490,920</td>
<td align="right">33,170,640</td>
<td align="right">6,656.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">6,000</td>
<td align="right">345,360</td>
<td align="right">5,656.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">168,180</td>
<td align="right">9,645,620</td>
<td align="right">5,635.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,634,980</td>
<td align="right">87,472,480</td>
<td align="right">3,219.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">762,840</td>
<td align="right">17,901,640</td>
<td align="right">2,246.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">762,840</td>
<td align="right">17,901,640</td>
<td align="right">2,246.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">414,720</td>
<td align="right">6,589,100</td>
<td align="right">1,488.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">414,720</td>
<td align="right">6,589,100</td>
<td align="right">1,488.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,183,000</td>
<td align="right">29,387,260</td>
<td align="right">1,246.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">950,240</td>
<td align="right">9,645,620</td>
<td align="right">915.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">139,240</td>
<td align="right">1,102,180</td>
<td align="right">691.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">816,580</td>
<td align="right">5,853,520</td>
<td align="right">616.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,540,140</td>
<td align="right">24,495,880</td>
<td align="right">591.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">3,842,580</td>
<td align="right">19,985,480</td>
<td align="right">420.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">4,942,700</td>
<td align="right">25,093,880</td>
<td align="right">407.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">112,880</td>
<td align="right">561,360</td>
<td align="right">397.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,291,900</td>
<td align="right">11,014,380</td>
<td align="right">380.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">518,220</td>
<td align="right">2,242,540</td>
<td align="right">332.7%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">138,520</td>
<td align="right">573,080</td>
<td align="right">313.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">47,500</td>
<td align="right">178,080</td>
<td align="right">274.9%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_NO_DICT</td>
<td align="right">1,955,000</td>
<td align="right">6,723,480</td>
<td align="right">243.9%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">138,520</td>
<td align="right">464,720</td>
<td align="right">235.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">16,188,080</td>
<td align="right">54,196,820</td>
<td align="right">234.8%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">935,460</td>
<td align="right">2,981,160</td>
<td align="right">218.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,339,400</td>
<td align="right">25,966,360</td>
<td align="right">211.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">728,640</td>
<td align="right">2,166,960</td>
<td align="right">197.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,240,100</td>
<td align="right">3,373,440</td>
<td align="right">172.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">42,700,320</td>
<td align="right">107,758,000</td>
<td align="right">152.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">268,080</td>
<td align="right">618,360</td>
<td align="right">130.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">5,110,880</td>
<td align="right">10,811,340</td>
<td align="right">111.5%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">1,475,760</td>
<td align="right">3,017,400</td>
<td align="right">104.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,578,620</td>
<td align="right">5,072,600</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">446,720</td>
<td align="right">871,080</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">111,380</td>
<td align="right">8,000</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">914,920</td>
<td align="right">66,240</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">187,560</td>
<td align="right">14,560</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">187,560</td>
<td align="right">14,560</td>
<td align="right">-92.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">4,163,400</td>
<td align="right">7,851,320</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">11,403,920</td>
<td align="right">21,169,480</td>
<td align="right">85.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">227,580</td>
<td align="right">33,080</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">443,820</td>
<td align="right">820,280</td>
<td align="right">84.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">15,814,480</td>
<td align="right">28,683,540</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">10,462,860</td>
<td align="right">18,502,960</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">960,320</td>
<td align="right">1,677,640</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">9,037,660</td>
<td align="right">15,700,700</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">524,780</td>
<td align="right">151,660</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">58,880,860</td>
<td align="right">89,562,040</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,462,080</td>
<td align="right">2,221,120</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">26,086,800</td>
<td align="right">12,897,120</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">729,740</td>
<td align="right">1,067,480</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">2,481,380</td>
<td align="right">3,604,320</td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,542,040</td>
<td align="right">2,212,440</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">9,713,380</td>
<td align="right">5,828,040</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,214,740</td>
<td align="right">3,077,780</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,081,440</td>
<td align="right">3,235,580</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">251,040</td>
<td align="right">340,480</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">251,040</td>
<td align="right">340,480</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">9,618,460</td>
<td align="right">6,305,460</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_WITH_VALUES</td>
<td align="right">251,040</td>
<td align="right">328,960</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,620,880</td>
<td align="right">3,145,640</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">1,445,400</td>
<td align="right">1,266,240</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">11,195,440</td>
<td align="right">12,441,120</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">17,427,100</td>
<td align="right">19,313,060</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">677,340</td>
<td align="right">614,080</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">3,926,780</td>
<td align="right">3,622,700</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">5,918,780</td>
<td align="right">5,750,180</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">5,918,780</td>
<td align="right">5,750,180</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">31,771,120</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">30,013,640</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">17,967,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">11,548,420</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">11,456,240</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">9,860,520</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">9,161,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,839,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">5,818,900</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,310,060</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,350,360</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">3,968,920</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">3,695,620</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">3,609,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">3,483,300</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,064,920</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">3,056,620</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,438,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">2,205,920</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,195,700</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,127,700</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,815,400</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,815,400</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,804,080</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1,757,480</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,653,280</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">914,920</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">439,380</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">215,680</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">82,860</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">47,500</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">1,500</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">227,867,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">16,497,500</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP</td>
<td align="right"></td>
<td align="right">14,233,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">9,645,620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right"></td>
<td align="right">4,782,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">4,214,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_NONE</td>
<td align="right"></td>
<td align="right">3,179,220</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right"></td>
<td align="right">2,411,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right"></td>
<td align="right">2,375,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">1,318,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">1,153,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">1,003,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">772,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">772,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right"></td>
<td align="right">714,700</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD</td>
<td align="right"></td>
<td align="right">612,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right"></td>
<td align="right">536,620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right"></td>
<td align="right">473,460</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">471,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right"></td>
<td align="right">451,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">451,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">417,840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">342,840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">330,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">305,520</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">241,460</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">231,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right"></td>
<td align="right">218,520</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_FOR</td>
<td align="right"></td>
<td align="right">209,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right"></td>
<td align="right">173,400</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right"></td>
<td align="right">171,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">153,840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right"></td>
<td align="right">133,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right">116,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">89,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right"></td>
<td align="right">89,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">89,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">81,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">80,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">80,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">56,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">56,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">55,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">53,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">52,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">51,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">51,520</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">47,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">47,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">45,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">32,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">32,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">28,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right"></td>
<td align="right">27,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">26,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">26,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">23,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">21,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">19,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">18,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">18,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">17,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right"></td>
<td align="right">16,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right"></td>
<td align="right">12,620</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right"></td>
<td align="right">11,520</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">9,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">4,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">1,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">1,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right"></td>
<td align="right">840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">720</td>
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
Stats gathered on: 2025-01-27
