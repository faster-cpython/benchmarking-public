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
<td align="left">CALL_STR_1</td>
<td align="right">13,441,560</td>
<td align="right">9,420</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">14,257,620</td>
<td align="right">26,880</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">18,809,140</td>
<td align="right">38,420</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">4,006,220</td>
<td align="right">9,800</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">18,821,040</td>
<td align="right">49,900</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">8,415,400</td>
<td align="right">24,520</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">9,780,880</td>
<td align="right">31,760</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">7,524,340</td>
<td align="right">24,660</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">9,937,940</td>
<td align="right">37,020</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">8,023,800</td>
<td align="right">31,040</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">21,477,880</td>
<td align="right">84,760</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">3,529,040</td>
<td align="right">21,220</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,073,180</td>
<td align="right">80,500</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">884,500</td>
<td align="right">8,200</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">21,218,840</td>
<td align="right">207,700</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">403,000</td>
<td align="right">4,720</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">968,540</td>
<td align="right">11,460</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">109,186,560</td>
<td align="right">1,374,280</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">85,250,300</td>
<td align="right">1,075,900</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">76,092,640</td>
<td align="right">981,460</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">889,660</td>
<td align="right">13,440</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">403,860</td>
<td align="right">6,380</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">890,560</td>
<td align="right">14,800</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">404,460</td>
<td align="right">6,980</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">402,920</td>
<td align="right">7,120</td>
<td align="right">-98.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">41,448,600</td>
<td align="right">934,560</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">14,883,120</td>
<td align="right">426,860</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">411,480</td>
<td align="right">12,580</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">124,991,200</td>
<td align="right">3,844,220</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,586,860</td>
<td align="right">197,400</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">297,122,860</td>
<td align="right">13,346,720</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">421,140</td>
<td align="right">23,700</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">4,104,100</td>
<td align="right">274,920</td>
<td align="right">-93.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">112,184,500</td>
<td align="right">8,489,800</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">84,194,160</td>
<td align="right">7,115,220</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">5,145,620</td>
<td align="right">528,600</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">26,923,720</td>
<td align="right">3,015,720</td>
<td align="right">-88.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">18,186,680</td>
<td align="right">2,704,620</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">30,564,860</td>
<td align="right">5,449,360</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">29,098,440</td>
<td align="right">5,679,800</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">13,244,860</td>
<td align="right">2,711,960</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">551,080</td>
<td align="right">158,240</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">576,320</td>
<td align="right">176,000</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,211,880</td>
<td align="right">2,913,160</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">42,750,020</td>
<td align="right">19,035,500</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">5,233,380</td>
<td align="right">2,692,740</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,003,200</td>
<td align="right">5,335,780</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">440</td>
<td align="right">240</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">4,402,080</td>
<td align="right">2,419,320</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">4,417,880</td>
<td align="right">2,435,480</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">4,805,840</td>
<td align="right">2,663,280</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,821,580</td>
<td align="right">2,678,860</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,824,760</td>
<td align="right">2,681,680</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,872,880</td>
<td align="right">2,729,360</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">404,120</td>
<td align="right">243,000</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">404,880</td>
<td align="right">244,080</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">8,969,080</td>
<td align="right">5,448,280</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">8,983,920</td>
<td align="right">5,463,600</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">417,380</td>
<td align="right">257,060</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">21,403,060</td>
<td align="right">13,342,580</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">20,644,660</td>
<td align="right">13,602,420</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">25,906,660</td>
<td align="right">18,054,680</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,200</td>
<td align="right">1,720</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,000</td>
<td align="right">800</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">800</td>
<td align="right">640</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">2,720</td>
<td align="right">2,240</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,840</td>
<td align="right">2,360</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,040</td>
<td align="right">1,720</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">1,040</td>
<td align="right">880</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">8,360</td>
<td align="right">7,080</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">3,240</td>
<td align="right">2,760</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">1,580</td>
<td align="right">1,380</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">2,940</td>
<td align="right">2,600</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,200</td>
<td align="right">3,720</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,400</td>
<td align="right">3,920</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">13,700</td>
<td align="right">12,260</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">3,380</td>
<td align="right">3,040</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,580</td>
<td align="right">1,440</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,160</td>
<td align="right">5,840</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,100</td>
<td align="right">2,940</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,020</td>
<td align="right">7,660</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">18,740</td>
<td align="right">18,100</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">26,620</td>
<td align="right">25,780</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">5,260</td>
<td align="right">5,100</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,680</td>
<td align="right">5,520</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">7,500</td>
<td align="right">7,300</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">24,700</td>
<td align="right">24,060</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">25,920</td>
<td align="right">25,440</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">9,080</td>
<td align="right">8,920</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">20,880</td>
<td align="right">20,560</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">11,220</td>
<td align="right">11,060</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">27,220</td>
<td align="right">26,900</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">14,660</td>
<td align="right">14,500</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">17,220</td>
<td align="right">17,060</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,080</td>
<td align="right">24,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,040</td>
<td align="right">20,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">16,920</td>
<td align="right">16,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">12,580</td>
<td align="right">12,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">11,100</td>
<td align="right">11,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">8,680</td>
<td align="right">8,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">8,660</td>
<td align="right">8,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">6,940</td>
<td align="right">6,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">6,000</td>
<td align="right">6,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">5,760</td>
<td align="right">5,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,440</td>
<td align="right">5,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">5,320</td>
<td align="right">5,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5,220</td>
<td align="right">5,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">5,160</td>
<td align="right">5,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">4,480</td>
<td align="right">4,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">4,480</td>
<td align="right">4,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">4,480</td>
<td align="right">4,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,240</td>
<td align="right">4,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">2,860</td>
<td align="right">2,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">2,480</td>
<td align="right">2,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,320</td>
<td align="right">2,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2,220</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">2,120</td>
<td align="right">2,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,900</td>
<td align="right">1,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">1,780</td>
<td align="right">1,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,600</td>
<td align="right">1,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,480</td>
<td align="right">1,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,120</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,100</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">1,040</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">940</td>
<td align="right">940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">880</td>
<td align="right">880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">680</td>
<td align="right">680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">600</td>
<td align="right">600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">580</td>
<td align="right">580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
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
<td align="right">14,960</td>
<td align="right">38.0%</td>
<td align="right">14,960</td>
<td align="right">38.0%</td>
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
<td align="right">22,480</td>
<td align="right">57.1%</td>
<td align="right">22,480</td>
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
<td align="left">Success</td>
<td align="right">660</td>
<td align="right">33.7%</td>
<td align="right">660</td>
<td align="right">33.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,300</td>
<td align="right">66.3%</td>
<td align="right">1,300</td>
<td align="right">66.3%</td>
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
<td align="left">remainder</td>
<td align="right">780</td>
<td align="right">60.0%</td>
<td align="right">780</td>
<td align="right">60.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">220</td>
<td align="right">16.9%</td>
<td align="right">220</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">200</td>
<td align="right">15.4%</td>
<td align="right">200</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">60</td>
<td align="right">4.6%</td>
<td align="right">60</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">40</td>
<td align="right">3.1%</td>
<td align="right">40</td>
<td align="right">3.1%</td>
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
<td align="right">403,860</td>
<td align="right">100.0%</td>
<td align="right">6,380</td>
<td align="right">100.0%</td>
<td align="right">-98.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">46,263,540</td>
<td align="right">100.0%</td>
<td align="right">28,661,780</td>
<td align="right">100.0%</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,540</td>
<td align="right">0.0%</td>
<td align="right">9,540</td>
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
<td align="right">660</td>
<td align="right">0.0%</td>
<td align="right">660</td>
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
<td align="right">960</td>
<td align="right">61.5%</td>
<td align="right">960</td>
<td align="right">61.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">600</td>
<td align="right">38.5%</td>
<td align="right">600</td>
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
<td align="left">out of range</td>
<td align="right">580</td>
<td align="right">96.7%</td>
<td align="right">580</td>
<td align="right">96.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">20</td>
<td align="right">3.3%</td>
<td align="right">20</td>
<td align="right">3.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">85,294,700</td>
<td align="right">100.0%</td>
<td align="right">53,928,940</td>
<td align="right">99.9%</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,660</td>
<td align="right">0.0%</td>
<td align="right">12,660</td>
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
<td align="right">5,060</td>
<td align="right">0.0%</td>
<td align="right">5,060</td>
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
<td align="right">12,020</td>
<td align="right">100.0%</td>
<td align="right">12,020</td>
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
<td align="right">60</td>
<td align="right">60 / 0 !!</td>
<td align="right">60</td>
<td align="right">60 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
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
<td align="right">560</td>
<td align="right">50.0%</td>
<td align="right">560</td>
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
<td align="right">888,080</td>
<td align="right">47.2%</td>
<td align="right">12,140</td>
<td align="right">1.2%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">991,080</td>
<td align="right">52.7%</td>
<td align="right">990,920</td>
<td align="right">98.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
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
<td align="right">860</td>
<td align="right">54.4%</td>
<td align="right">580</td>
<td align="right">44.6%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">720</td>
<td align="right">45.6%</td>
<td align="right">720</td>
<td align="right">55.4%</td>
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
<td align="right">60.5%</td>
<td align="right">240</td>
<td align="right">41.4%</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">260</td>
<td align="right">30.2%</td>
<td align="right">260</td>
<td align="right">44.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">7.0%</td>
<td align="right">60</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">20</td>
<td align="right">2.3%</td>
<td align="right">20</td>
<td align="right">3.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,973,060</td>
<td align="right">99.9%</td>
<td align="right">4,892,740</td>
<td align="right">99.9%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,240</td>
<td align="right">0.1%</td>
<td align="right">5,240</td>
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
<td align="right">160</td>
<td align="right">21.1%</td>
<td align="right">160</td>
<td align="right">21.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">600</td>
<td align="right">78.9%</td>
<td align="right">600</td>
<td align="right">78.9%</td>
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
<td align="left">str</td>
<td align="right">360</td>
<td align="right">60.0%</td>
<td align="right">360</td>
<td align="right">60.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">180</td>
<td align="right">30.0%</td>
<td align="right">180</td>
<td align="right">30.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">60</td>
<td align="right">10.0%</td>
<td align="right">60</td>
<td align="right">10.0%</td>
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
<td align="right">4,820,820</td>
<td align="right">7.3%</td>
<td align="right">2,678,260</td>
<td align="right">6.3%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">61,231,780</td>
<td align="right">92.7%</td>
<td align="right">40,032,760</td>
<td align="right">93.7%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,440</td>
<td align="right">0.0%</td>
<td align="right">6,120</td>
<td align="right">0.0%</td>
<td align="right">-5.0%</td>
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
<td align="right">2,840</td>
<td align="right">70.6%</td>
<td align="right">2,320</td>
<td align="right">66.3%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,180</td>
<td align="right">29.4%</td>
<td align="right">1,180</td>
<td align="right">33.7%</td>
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
<td align="right">1,540</td>
<td align="right">54.2%</td>
<td align="right">1,020</td>
<td align="right">44.0%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">320</td>
<td align="right">11.3%</td>
<td align="right">320</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">260</td>
<td align="right">9.2%</td>
<td align="right">260</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">220</td>
<td align="right">7.7%</td>
<td align="right">220</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">200</td>
<td align="right">7.0%</td>
<td align="right">200</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">200</td>
<td align="right">7.0%</td>
<td align="right">200</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">60</td>
<td align="right">2.1%</td>
<td align="right">60</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">40</td>
<td align="right">1.4%</td>
<td align="right">40</td>
<td align="right">1.7%</td>
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
<td align="right">12,057,560</td>
<td align="right">19.8%</td>
<td align="right">68,340</td>
<td align="right">0.3%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">48,709,160</td>
<td align="right">80.1%</td>
<td align="right">21,354,260</td>
<td align="right">99.6%</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,440</td>
<td align="right">0.0%</td>
<td align="right">5,440</td>
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
<td align="right">6,200</td>
<td align="right">39.6%</td>
<td align="right">2,740</td>
<td align="right">22.5%</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,460</td>
<td align="right">60.4%</td>
<td align="right">9,460</td>
<td align="right">77.5%</td>
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
<td align="left">class method obj</td>
<td align="right">4,320</td>
<td align="right">69.7%</td>
<td align="right">960</td>
<td align="right">35.0%</td>
<td align="right">-77.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">960</td>
<td align="right">15.5%</td>
<td align="right">860</td>
<td align="right">31.4%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">360</td>
<td align="right">5.8%</td>
<td align="right">360</td>
<td align="right">13.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">320</td>
<td align="right">5.2%</td>
<td align="right">320</td>
<td align="right">11.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">160</td>
<td align="right">2.6%</td>
<td align="right">160</td>
<td align="right">5.8%</td>
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
<td align="right">139,869,160</td>
<td align="right">100.0%</td>
<td align="right">4,265,920</td>
<td align="right">99.4%</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">10,000</td>
<td align="right">0.0%</td>
<td align="right">10,000</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,160</td>
<td align="right">0.0%</td>
<td align="right">5,160</td>
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
<td align="right">10,040</td>
<td align="right">100.0%</td>
<td align="right">10,040</td>
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
<td align="right">9.1%</td>
<td align="right">40</td>
<td align="right">9.1%</td>
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
<td align="right">360</td>
<td align="right">81.8%</td>
<td align="right">360</td>
<td align="right">81.8%</td>
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
<td align="right">4,900</td>
<td align="right">11.6%</td>
<td align="right">4,580</td>
<td align="right">11.1%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,380</td>
<td align="right">81.1%</td>
<td align="right">33,420</td>
<td align="right">81.4%</td>
<td align="right">-2.8%</td>
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
<td align="right">480</td>
<td align="right">15.4%</td>
<td align="right">440</td>
<td align="right">14.3%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,640</td>
<td align="right">84.6%</td>
<td align="right">2,640</td>
<td align="right">85.7%</td>
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
<td align="right">160</td>
<td align="right">33.3%</td>
<td align="right">120</td>
<td align="right">27.3%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">300</td>
<td align="right">62.5%</td>
<td align="right">300</td>
<td align="right">68.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">20</td>
<td align="right">4.2%</td>
<td align="right">20</td>
<td align="right">4.5%</td>
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
<td align="right">320</td>
<td align="right">100.0%</td>
<td align="right">320</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,404,680</td>
<td align="right">100.0%</td>
<td align="right">2,644,680</td>
<td align="right">100.0%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">680</td>
<td align="right">0.0%</td>
<td align="right">680</td>
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
<td align="right">240</td>
<td align="right">92.3%</td>
<td align="right">240</td>
<td align="right">92.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">7.7%</td>
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
<td align="left">out of range</td>
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
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
<td align="right">9,774,440</td>
<td align="right">21.8%</td>
<td align="right">28,140</td>
<td align="right">0.1%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">35,080,740</td>
<td align="right">78.2%</td>
<td align="right">24,679,260</td>
<td align="right">99.9%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,820</td>
<td align="right">0.0%</td>
<td align="right">1,820</td>
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
<td align="right">3,840</td>
<td align="right">59.4%</td>
<td align="right">1,020</td>
<td align="right">28.0%</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,620</td>
<td align="right">40.6%</td>
<td align="right">2,620</td>
<td align="right">72.0%</td>
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
<td align="right">2,760</td>
<td align="right">71.9%</td>
<td align="right">520</td>
<td align="right">51.0%</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">960</td>
<td align="right">25.0%</td>
<td align="right">400</td>
<td align="right">39.2%</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">120</td>
<td align="right">3.1%</td>
<td align="right">100</td>
<td align="right">9.8%</td>
<td align="right">-16.7%</td>
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
<td align="right">22,428,060</td>
<td align="right">100.0%</td>
<td align="right">3,655,860</td>
<td align="right">99.9%</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,520</td>
<td align="right">0.0%</td>
<td align="right">1,520</td>
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
<td align="right">840</td>
<td align="right">87.5%</td>
<td align="right">840</td>
<td align="right">87.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">120</td>
<td align="right">12.5%</td>
<td align="right">120</td>
<td align="right">12.5%</td>
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
<td align="left">iterator</td>
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">120</td>
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
<td align="right">28,063,440</td>
<td align="right">2.0%</td>
<td align="right">2,904,500</td>
<td align="right">1.8%</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,025,299,740</td>
<td align="right">71.3%</td>
<td align="right">111,449,720</td>
<td align="right">68.8%</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">385,304,680</td>
<td align="right">26.8%</td>
<td align="right">47,603,940</td>
<td align="right">29.4%</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">25,500</td>
<td align="right">0.0%</td>
<td align="right">25,040</td>
<td align="right">0.0%</td>
<td align="right">-1.8%</td>
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
<td align="right">9,774,440</td>
<td align="right">34.9%</td>
<td align="right">28,140</td>
<td align="right">1.0%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">12,057,560</td>
<td align="right">43.1%</td>
<td align="right">68,340</td>
<td align="right">2.4%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">888,080</td>
<td align="right">3.2%</td>
<td align="right">12,140</td>
<td align="right">0.4%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">403,860</td>
<td align="right">1.4%</td>
<td align="right">6,380</td>
<td align="right">0.2%</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,820,820</td>
<td align="right">17.2%</td>
<td align="right">2,678,260</td>
<td align="right">93.9%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">14,960</td>
<td align="right">0.1%</td>
<td align="right">14,960</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">12,660</td>
<td align="right">0.0%</td>
<td align="right">12,660</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">10,000</td>
<td align="right">0.0%</td>
<td align="right">10,000</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,540</td>
<td align="right">0.0%</td>
<td align="right">9,540</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">5,240</td>
<td align="right">0.0%</td>
<td align="right">5,240</td>
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
<td align="left">RESUME</td>
<td align="right">720</td>
<td align="right">2.7%</td>
<td align="right">580</td>
<td align="right">2.3%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">720</td>
<td align="right">2.7%</td>
<td align="right">580</td>
<td align="right">2.3%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">5,680</td>
<td align="right">21.7%</td>
<td align="right">5,680</td>
<td align="right">22.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,760</td>
<td align="right">18.2%</td>
<td align="right">4,760</td>
<td align="right">18.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,340</td>
<td align="right">12.7%</td>
<td align="right">3,340</td>
<td align="right">13.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,080</td>
<td align="right">11.7%</td>
<td align="right">3,080</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,080</td>
<td align="right">7.9%</td>
<td align="right">2,080</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,480</td>
<td align="right">5.6%</td>
<td align="right">1,480</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,060</td>
<td align="right">4.0%</td>
<td align="right">1,060</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">760</td>
<td align="right">2.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">540</td>
<td align="right">2.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,400,440</td>
<td align="right">3.8%</td>
<td align="right">2,640,280</td>
<td align="right">3.5%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,955,560</td>
<td align="right">4.3%</td>
<td align="right">3,033,960</td>
<td align="right">4.0%</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">39,263,820</td>
<td align="right">33.9%</td>
<td align="right">24,379,820</td>
<td align="right">32.5%</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">95,113,940</td>
<td align="right">82.2%</td>
<td align="right">61,350,100</td>
<td align="right">81.9%</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">20,645,200</td>
<td align="right">17.8%</td>
<td align="right">13,602,960</td>
<td align="right">18.1%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">20,645,200</td>
<td align="right">17.8%</td>
<td align="right">13,602,960</td>
<td align="right">18.1%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">15,689,640</td>
<td align="right">13.6%</td>
<td align="right">10,569,000</td>
<td align="right">14.1%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">554,760</td>
<td align="right">0.5%</td>
<td align="right">393,320</td>
<td align="right">0.5%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">760</td>
<td align="right">0.0%</td>
<td align="right">600</td>
<td align="right">0.0%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,520</td>
<td align="right">0.0%</td>
<td align="right">1,360</td>
<td align="right">0.0%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">3,740</td>
<td align="right">0.0%</td>
<td align="right">3,740</td>
<td align="right">0.0%</td>
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
<td align="right">10,200</td>
<td align="right">0.0%</td>
<td align="right">10,200</td>
<td align="right">0.0%</td>
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
<td align="left">Interpreter mortal increfs</td>
<td align="right">653,641,700</td>
<td align="right">44.8%</td>
<td align="right">70,736,780</td>
<td align="right">7.2%</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">175,662,040</td>
<td align="right">12.0%</td>
<td align="right">30,459,700</td>
<td align="right">3.1%</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">736,529,820</td>
<td align="right">46.1%</td>
<td align="right">170,522,480</td>
<td align="right">15.1%</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">161,110,080</td>
<td align="right">10.1%</td>
<td align="right">42,104,020</td>
<td align="right">3.7%</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">495,002,006</td>
<td align="right">33.9%</td>
<td align="right">751,533,756</td>
<td align="right">76.6%</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">491,168,637</td>
<td align="right">30.8%</td>
<td align="right">719,644,338</td>
<td align="right">63.7%</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">26,946,147</td>
<td align="right"></td>
<td align="right">16,215,652</td>
<td align="right"></td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">9,051,154</td>
<td align="right"></td>
<td align="right">5,528,882</td>
<td align="right"></td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">46,642,480</td>
<td align="right">47.8%</td>
<td align="right">33,355,340</td>
<td align="right">41.3%</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">46,643,220</td>
<td align="right"></td>
<td align="right">33,356,020</td>
<td align="right"></td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">4,060</td>
<td align="right"></td>
<td align="right">3,740</td>
<td align="right"></td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">50,833,280</td>
<td align="right">52.1%</td>
<td align="right">47,358,220</td>
<td align="right">58.7%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">50,843,620</td>
<td align="right">52.2%</td>
<td align="right">47,368,400</td>
<td align="right">58.7%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">54,583,861</td>
<td align="right"></td>
<td align="right">51,109,219</td>
<td align="right"></td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">136,295,471</td>
<td align="right">9.3%</td>
<td align="right">128,536,591</td>
<td align="right">13.1%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">14,167</td>
<td align="right"></td>
<td align="right">14,870</td>
<td align="right"></td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">3,440</td>
<td align="right">0.0%</td>
<td align="right">3,280</td>
<td align="right">0.0%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">207,162,759</td>
<td align="right">13.0%</td>
<td align="right">198,289,924</td>
<td align="right">17.5%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">16,913</td>
<td align="right"></td>
<td align="right">17,508</td>
<td align="right"></td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,566</td>
<td align="right"></td>
<td align="right">2,598</td>
<td align="right"></td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">6,900</td>
<td align="right">0.0%</td>
<td align="right">6,900</td>
<td align="right">0.0%</td>
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
<td align="right">520</td>
<td align="right">10,880</td>
<td align="right">7,010,340</td>
<td align="right">520</td>
<td align="right">9,440</td>
<td align="right">7,022,060</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,080</td>
<td align="right">56.7%</td>
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
<td align="right">7,740</td>
<td align="right">72.2%</td>
<td align="right">2,540</td>
<td align="right">42.5%</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">1,549,480,980</td>
<td align="right">1,010.6%</td>
<td align="right">2,280,978,340</td>
<td align="right">1,484.1%</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">10,720</td>
<td align="right"></td>
<td align="right">5,980</td>
<td align="right"></td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,980</td>
<td align="right">27.8%</td>
<td align="right">3,440</td>
<td align="right">57.5%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">440</td>
<td align="right">4.1%</td>
<td align="right">400</td>
<td align="right">6.7%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">153,323,520</td>
<td align="right"></td>
<td align="right">153,694,180</td>
<td align="right"></td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">2,940</td>
<td align="right">98.7%</td>
<td align="right">3,400</td>
<td align="right">98.8%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,980</td>
<td align="right"></td>
<td align="right">3,440</td>
<td align="right"></td>
<td align="right">15.4%</td>
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
<td align="right">440</td>
<td align="right">14.8%</td>
<td align="right">340</td>
<td align="right">9.9%</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">620</td>
<td align="right">20.8%</td>
<td align="right">760</td>
<td align="right">22.1%</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">140</td>
<td align="right">4.7%</td>
<td align="right">360</td>
<td align="right">10.5%</td>
<td align="right">157.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">1,360</td>
<td align="right">45.6%</td>
<td align="right">1,320</td>
<td align="right">38.4%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">140</td>
<td align="right">4.7%</td>
<td align="right">340</td>
<td align="right">9.9%</td>
<td align="right">142.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">200</td>
<td align="right">6.7%</td>
<td align="right">240</td>
<td align="right">7.0%</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">80</td>
<td align="right">2.7%</td>
<td align="right">80</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
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
<td align="right">80</td>
<td align="right">2.7%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">800</td>
<td align="right">26.8%</td>
<td align="right">900</td>
<td align="right">26.2%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">260</td>
<td align="right">8.7%</td>
<td align="right">440</td>
<td align="right">12.8%</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">1,280</td>
<td align="right">43.0%</td>
<td align="right">1,260</td>
<td align="right">36.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">220</td>
<td align="right">7.4%</td>
<td align="right">300</td>
<td align="right">8.7%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">160</td>
<td align="right">5.4%</td>
<td align="right">360</td>
<td align="right">10.5%</td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">140</td>
<td align="right">4.7%</td>
<td align="right">140</td>
<td align="right">4.1%</td>
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
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">80</td>
<td align="right">24,832,840</td>
<td align="right">31,040,950.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">160</td>
<td align="right">237,320</td>
<td align="right">148,225.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">4,740</td>
<td align="right">6,705,500</td>
<td align="right">141,366.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">720</td>
<td align="right">233,080</td>
<td align="right">32,272.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">800</td>
<td align="right">223,040</td>
<td align="right">27,780.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">880</td>
<td align="right">223,120</td>
<td align="right">25,254.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">880</td>
<td align="right">223,120</td>
<td align="right">25,254.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">880</td>
<td align="right">223,120</td>
<td align="right">25,254.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,340</td>
<td align="right">240,660</td>
<td align="right">7,105.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">165,440</td>
<td align="right">8,327,840</td>
<td align="right">4,933.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">7,680</td>
<td align="right">229,920</td>
<td align="right">2,893.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">800,060</td>
<td align="right">19,084,040</td>
<td align="right">2,285.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">401,720</td>
<td align="right">8,071,820</td>
<td align="right">1,909.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">879,380</td>
<td align="right">16,991,220</td>
<td align="right">1,832.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">399,220</td>
<td align="right">6,138,580</td>
<td align="right">1,437.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">558,480</td>
<td align="right">8,461,740</td>
<td align="right">1,415.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,198,580</td>
<td align="right">13,779,900</td>
<td align="right">1,049.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,282,100</td>
<td align="right">13,972,400</td>
<td align="right">989.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">7,356,160</td>
<td align="right">74,193,480</td>
<td align="right">908.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">399,620</td>
<td align="right">3,511,800</td>
<td align="right">778.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">398,240</td>
<td align="right">3,093,860</td>
<td align="right">676.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">398,020</td>
<td align="right">2,856,260</td>
<td align="right">617.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">398,020</td>
<td align="right">2,856,260</td>
<td align="right">617.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">397,280</td>
<td align="right">2,633,260</td>
<td align="right">562.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">397,380</td>
<td align="right">2,633,620</td>
<td align="right">562.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">794,800</td>
<td align="right">5,266,760</td>
<td align="right">562.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,192,360</td>
<td align="right">7,900,300</td>
<td align="right">562.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">398,200</td>
<td align="right">2,634,460</td>
<td align="right">561.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">10,714,840</td>
<td align="right">63,046,200</td>
<td align="right">488.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">12,214,500</td>
<td align="right">60,238,440</td>
<td align="right">393.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">180</td>
<td align="right">880</td>
<td align="right">388.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">1,192,000</td>
<td align="right">5,740,960</td>
<td align="right">381.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">16,956,280</td>
<td align="right">80,136,360</td>
<td align="right">372.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,124,820</td>
<td align="right">5,100,400</td>
<td align="right">353.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">100</td>
<td align="right">440</td>
<td align="right">340.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,804,240</td>
<td align="right">17,446,480</td>
<td align="right">263.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">37,174,460</td>
<td align="right">131,164,980</td>
<td align="right">252.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,470,620</td>
<td align="right">8,696,640</td>
<td align="right">252.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">16,232,480</td>
<td align="right">57,092,880</td>
<td align="right">251.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,475,400</td>
<td align="right">19,020,840</td>
<td align="right">193.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">180</td>
<td align="right">520</td>
<td align="right">188.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,191,980</td>
<td align="right">3,107,800</td>
<td align="right">160.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">28,154,660</td>
<td align="right">72,513,140</td>
<td align="right">157.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">7,825,840</td>
<td align="right">20,094,820</td>
<td align="right">156.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">7,281,880</td>
<td align="right">18,126,640</td>
<td align="right">148.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,753,600</td>
<td align="right">4,221,940</td>
<td align="right">140.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">120</td>
<td align="right">280</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">15,670,200</td>
<td align="right">32,628,600</td>
<td align="right">108.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">5,590,060</td>
<td align="right">11,220,080</td>
<td align="right">100.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">879,520</td>
<td align="right">1,755,820</td>
<td align="right">99.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">9,588,440</td>
<td align="right">18,523,400</td>
<td align="right">93.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">13,974,800</td>
<td align="right">24,016,180</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">51,840,260</td>
<td align="right">89,036,740</td>
<td align="right">71.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">15,426,260</td>
<td align="right">26,484,400</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">4,397,540</td>
<td align="right">7,341,260</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">19,582,000</td>
<td align="right">32,050,060</td>
<td align="right">63.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,756,620</td>
<td align="right">2,713,700</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">126,450,380</td>
<td align="right">195,015,620</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">67,415,040</td>
<td align="right">98,601,600</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">4,556,140</td>
<td align="right">6,464,840</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,556,140</td>
<td align="right">6,464,840</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">397,360</td>
<td align="right">237,200</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">397,400</td>
<td align="right">237,380</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">398,100</td>
<td align="right">238,120</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">4,396,320</td>
<td align="right">2,636,320</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">4,396,320</td>
<td align="right">2,636,320</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">4,396,320</td>
<td align="right">2,636,320</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">4,396,320</td>
<td align="right">2,636,480</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">8,793,640</td>
<td align="right">5,273,640</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">4,396,560</td>
<td align="right">2,636,760</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">26,328,600</td>
<td align="right">16,165,240</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">17,365,600</td>
<td align="right">10,722,240</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">12,962,640</td>
<td align="right">8,079,600</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">8,801,320</td>
<td align="right">5,503,560</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">101,481,560</td>
<td align="right">64,656,120</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">560</td>
<td align="right">760</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">560</td>
<td align="right">760</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">10,864,960</td>
<td align="right">14,734,980</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">4,396,320</td>
<td align="right">2,873,640</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">60,377,680</td>
<td align="right">39,736,880</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">9,671,900</td>
<td align="right">6,387,360</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">80,995,040</td>
<td align="right">53,765,860</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,274,900</td>
<td align="right">3,514,900</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">51,839,880</td>
<td align="right">34,558,760</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">5,354,960</td>
<td align="right">3,594,960</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">11,824,820</td>
<td align="right">15,695,000</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">5,911,600</td>
<td align="right">3,991,440</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">12,222,060</td>
<td align="right">15,931,880</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">5,355,580</td>
<td align="right">3,834,320</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">6,074,940</td>
<td align="right">4,453,980</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">8,325,200</td>
<td align="right">6,307,120</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">6,156,440</td>
<td align="right">7,583,780</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">1,700</td>
<td align="right">1,320</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">63,665,080</td>
<td align="right">50,254,500</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">980</td>
<td align="right">1,180</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">60,563,640</td>
<td align="right">49,571,220</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">94,730,360</td>
<td align="right">79,951,720</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">403,200</td>
<td align="right">465,440</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">10,951,700</td>
<td align="right">12,358,420</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,520</td>
<td align="right">1,680</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">153,323,520</td>
<td align="right">153,694,180</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">153,488,020</td>
<td align="right">153,858,680</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">960,220</td>
<td align="right">960,900</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">961,160</td>
<td align="right">961,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">959,860</td>
<td align="right">960,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">960,300</td>
<td align="right">960,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">160,400</td>
<td align="right">160,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">160,400</td>
<td align="right">160,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,721,700</td>
<td align="right">2,721,660</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">960,300</td>
<td align="right">960,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">959,860</td>
<td align="right">959,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">959,860</td>
<td align="right">959,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">883,240</td>
<td align="right">883,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">882,000</td>
<td align="right">882,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">882,000</td>
<td align="right">882,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">476,460</td>
<td align="right">476,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">164,500</td>
<td align="right">164,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">159,800</td>
<td align="right">159,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">159,680</td>
<td align="right">159,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">159,240</td>
<td align="right">159,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">159,240</td>
<td align="right">159,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">3,520</td>
<td align="right">3,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,520</td>
<td align="right">3,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">2,160</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,540</td>
<td align="right">1,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,400</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">1,300</td>
<td align="right">1,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,180</td>
<td align="right">1,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">860</td>
<td align="right">860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">220</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">220</td>
<td align="right">220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">49,349,900</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">13,491,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">6,711,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">875,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">666,780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right"></td>
<td align="right">444,500</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">237,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">222,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">160</td>
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
<td align="right">240</td>
<td align="right">280</td>
<td align="right">16.7%</td>
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
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
