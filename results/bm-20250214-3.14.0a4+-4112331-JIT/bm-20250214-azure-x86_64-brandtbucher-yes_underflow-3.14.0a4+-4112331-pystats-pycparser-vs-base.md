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
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">720</td>
<td align="right">319,400</td>
<td align="right">44,261.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">205,400</td>
<td align="right">1,157,120</td>
<td align="right">463.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">777,980</td>
<td align="right">2,682,260</td>
<td align="right">244.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">614,000</td>
<td align="right">2,067,780</td>
<td align="right">236.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">84,420</td>
<td align="right">248,220</td>
<td align="right">194.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,553,380</td>
<td align="right">3,715,020</td>
<td align="right">139.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">986,860</td>
<td align="right">2,296,640</td>
<td align="right">132.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">316,080</td>
<td align="right">734,880</td>
<td align="right">132.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">32,012,800</td>
<td align="right">808,480</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">32,012,800</td>
<td align="right">808,480</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,032,220</td>
<td align="right">249,420</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">27,902,960</td>
<td align="right">1,148,260</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">60,196,300</td>
<td align="right">2,813,540</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">44,069,520</td>
<td align="right">2,483,400</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">17,043,320</td>
<td align="right">1,192,800</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,142,120</td>
<td align="right">2,166,320</td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">67,701,240</td>
<td align="right">7,386,820</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">36,642,320</td>
<td align="right">4,482,840</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">13,729,300</td>
<td align="right">1,774,720</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,228,100</td>
<td align="right">1,210,160</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">5,838,280</td>
<td align="right">808,480</td>
<td align="right">-86.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">8,928,700</td>
<td align="right">1,238,360</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">5,854,300</td>
<td align="right">824,500</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">16,598,740</td>
<td align="right">3,340,480</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">80,946,360</td>
<td align="right">17,031,980</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,025,220</td>
<td align="right">1,599,200</td>
<td align="right">-77.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">124,464,280</td>
<td align="right">33,912,380</td>
<td align="right">-72.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,170,680</td>
<td align="right">3,647,980</td>
<td align="right">68.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">26,330,020</td>
<td align="right">8,763,980</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">763,253,320</td>
<td align="right">286,912,680</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">9,780,400</td>
<td align="right">3,698,640</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">9,557,300</td>
<td align="right">3,700,520</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">669,540</td>
<td align="right">261,380</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,200,140</td>
<td align="right">2,400,680</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,713,920</td>
<td align="right">13,067,220</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">175,569,280</td>
<td align="right">90,626,920</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">36,714,780</td>
<td align="right">20,608,280</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">161,694,440</td>
<td align="right">93,063,700</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">4,070,660</td>
<td align="right">2,373,560</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">62,243,880</td>
<td align="right">36,710,060</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,199,760</td>
<td align="right">3,715,280</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">798,540</td>
<td align="right">1,094,660</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">20,063,580</td>
<td align="right">12,881,840</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">133,157,580</td>
<td align="right">86,730,280</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,535,100</td>
<td align="right">12,308,900</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">406,300</td>
<td align="right">269,820</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">1,274,660</td>
<td align="right">1,688,060</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">66,048,420</td>
<td align="right">44,704,980</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">770,160</td>
<td align="right">524,480</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">117,125,040</td>
<td align="right">82,649,320</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,842,560</td>
<td align="right">1,325,920</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,609,400</td>
<td align="right">1,914,960</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">4,013,520</td>
<td align="right">2,959,840</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,358,920</td>
<td align="right">9,149,440</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">20,936,460</td>
<td align="right">15,569,580</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">22,199,840</td>
<td align="right">16,547,280</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">7,301,440</td>
<td align="right">5,608,580</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">9,839,740</td>
<td align="right">7,733,300</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">28,390,680</td>
<td align="right">23,031,440</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">57,925,500</td>
<td align="right">47,295,020</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">787,560</td>
<td align="right">929,680</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">379,680</td>
<td align="right">313,400</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,489,460</td>
<td align="right">1,257,020</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">585,260</td>
<td align="right">665,320</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">12,302,260</td>
<td align="right">10,776,960</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">61,769,260</td>
<td align="right">54,337,060</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">52,179,300</td>
<td align="right">46,382,300</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,041,260</td>
<td align="right">1,828,900</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,330,700</td>
<td align="right">11,374,520</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,760,020</td>
<td align="right">6,324,740</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">972,260</td>
<td align="right">1,062,900</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">8,068,620</td>
<td align="right">7,341,780</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,091,700</td>
<td align="right">1,017,240</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,091,760</td>
<td align="right">1,017,320</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,102,420</td>
<td align="right">1,162,540</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">74,629,400</td>
<td align="right">71,330,500</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">109,161,480</td>
<td align="right">105,926,920</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">855,060</td>
<td align="right">829,940</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">33,650,940</td>
<td align="right">32,698,280</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,553,560</td>
<td align="right">1,588,740</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">34,325,400</td>
<td align="right">33,727,680</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,631,180</td>
<td align="right">1,604,680</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">9,035,660</td>
<td align="right">9,168,060</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">16,311,960</td>
<td align="right">16,073,600</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">45,092,120</td>
<td align="right">45,457,940</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">411,180</td>
<td align="right">411,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">41,912,040</td>
<td align="right">41,912,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">4,013,340</td>
<td align="right">4,013,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">216,960</td>
<td align="right">216,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">180,960</td>
<td align="right">180,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">94,920</td>
<td align="right">94,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">90,980</td>
<td align="right">90,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">88,680</td>
<td align="right">88,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">65,880</td>
<td align="right">65,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">65,880</td>
<td align="right">65,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">56,100</td>
<td align="right">56,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">32,940</td>
<td align="right">32,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,600</td>
<td align="right">30,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">30,420</td>
<td align="right">30,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">30,420</td>
<td align="right">30,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">13,860</td>
<td align="right">13,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">13,860</td>
<td align="right">13,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">3,840</td>
<td align="right">3,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,980</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
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
<td align="left">IS_OP</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
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
<td align="right">798,060</td>
<td align="right">1.9%</td>
<td align="right">1,094,120</td>
<td align="right">2.6%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">40,525,620</td>
<td align="right">98.1%</td>
<td align="right">40,525,620</td>
<td align="right">97.4%</td>
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
<td align="right">95.8%</td>
<td align="right">520</td>
<td align="right">96.3%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">20</td>
<td align="right">4.2%</td>
<td align="right">20</td>
<td align="right">3.7%</td>
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
<td align="left">multiply different types</td>
<td align="right">80</td>
<td align="right">17.4%</td>
<td align="right">160</td>
<td align="right">30.8%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">200</td>
<td align="right">43.5%</td>
<td align="right">180</td>
<td align="right">34.6%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">120</td>
<td align="right">26.1%</td>
<td align="right">120</td>
<td align="right">23.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">40</td>
<td align="right">8.7%</td>
<td align="right">40</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">20</td>
<td align="right">3.8%</td>
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
<td align="right">5,854,300</td>
<td align="right">100.0%</td>
<td align="right">824,500</td>
<td align="right">100.0%</td>
<td align="right">-85.9%</td>
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
<td align="right">27,895,580</td>
<td align="right">9.6%</td>
<td align="right">1,147,360</td>
<td align="right">0.4%</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">261,746,940</td>
<td align="right">90.4%</td>
<td align="right">261,746,940</td>
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
<td align="left">Failure</td>
<td align="right">7,340</td>
<td align="right">99.5%</td>
<td align="right">860</td>
<td align="right">95.6%</td>
<td align="right">-88.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">4.4%</td>
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
<td align="right">7,040</td>
<td align="right">95.9%</td>
<td align="right">580</td>
<td align="right">67.4%</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">260</td>
<td align="right">3.5%</td>
<td align="right">240</td>
<td align="right">27.9%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">4.7%</td>
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
<td align="right">25,024,820</td>
<td align="right">7.8%</td>
<td align="right">26,349,920</td>
<td align="right">8.2%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,506,060</td>
<td align="right">8.0%</td>
<td align="right">26,856,640</td>
<td align="right">8.3%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">294,023,240</td>
<td align="right">92.0%</td>
<td align="right">295,311,480</td>
<td align="right">91.7%</td>
<td align="right">0.4%</td>
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
<td align="right">481,720</td>
<td align="right">100.0%</td>
<td align="right">507,200</td>
<td align="right">100.0%</td>
<td align="right">5.3%</td>
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
<td align="right">406,200</td>
<td align="right">0.3%</td>
<td align="right">269,760</td>
<td align="right">0.2%</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">130,939,800</td>
<td align="right">99.7%</td>
<td align="right">130,939,800</td>
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
<td align="right">100</td>
<td align="right">100.0%</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">-40.0%</td>
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
<td align="left">list</td>
<td align="right">100</td>
<td align="right">100.0%</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">-40.0%</td>
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
<td align="right">1,841,820</td>
<td align="right">5.0%</td>
<td align="right">1,325,300</td>
<td align="right">3.7%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,664,280</td>
<td align="right">95.0%</td>
<td align="right">34,664,280</td>
<td align="right">96.3%</td>
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
<td align="right">740</td>
<td align="right">100.0%</td>
<td align="right">620</td>
<td align="right">100.0%</td>
<td align="right">-16.2%</td>
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
<td align="left">tuple</td>
<td align="right">360</td>
<td align="right">48.6%</td>
<td align="right">240</td>
<td align="right">38.7%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">27.0%</td>
<td align="right">200</td>
<td align="right">32.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">180</td>
<td align="right">24.3%</td>
<td align="right">180</td>
<td align="right">29.0%</td>
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
<td align="right">986,360</td>
<td align="right">45.7%</td>
<td align="right">2,295,820</td>
<td align="right">51.1%</td>
<td align="right">132.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,172,840</td>
<td align="right">54.3%</td>
<td align="right">2,197,040</td>
<td align="right">48.9%</td>
<td align="right">87.3%</td>
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
<td align="right">500</td>
<td align="right">100.0%</td>
<td align="right">820</td>
<td align="right">100.0%</td>
<td align="right">64.0%</td>
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
<td align="left">reversed list</td>
<td align="right">80</td>
<td align="right">16.0%</td>
<td align="right">460</td>
<td align="right">56.1%</td>
<td align="right">475.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">120</td>
<td align="right">24.0%</td>
<td align="right">60</td>
<td align="right">7.3%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">160</td>
<td align="right">32.0%</td>
<td align="right">160</td>
<td align="right">19.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">60</td>
<td align="right">12.0%</td>
<td align="right">60</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">40</td>
<td align="right">8.0%</td>
<td align="right">40</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">40</td>
<td align="right">8.0%</td>
<td align="right">40</td>
<td align="right">4.9%</td>
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
<td align="right">28,381,380</td>
<td align="right">5.1%</td>
<td align="right">23,023,480</td>
<td align="right">4.2%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,896,260</td>
<td align="right">0.7%</td>
<td align="right">3,599,400</td>
<td align="right">0.7%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">524,897,380</td>
<td align="right">94.2%</td>
<td align="right">525,944,220</td>
<td align="right">95.2%</td>
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
<td align="right">8,940</td>
<td align="right">10.8%</td>
<td align="right">7,600</td>
<td align="right">10.0%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">73,800</td>
<td align="right">89.2%</td>
<td align="right">68,240</td>
<td align="right">90.0%</td>
<td align="right">-7.5%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">400</td>
<td align="right">4.5%</td>
<td align="right">320</td>
<td align="right">4.2%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">140</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">120</td>
<td align="right">1.3%</td>
<td align="right">120</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">100</td>
<td align="right">1.1%</td>
<td align="right">100</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">60</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.5%</td>
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
<td align="right">93,691,380</td>
<td align="right">100.0%</td>
<td align="right">86,180,180</td>
<td align="right">100.0%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,060</td>
<td align="right">0.0%</td>
<td align="right">4,060</td>
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
<td align="right">8,029,800</td>
<td align="right">3.3%</td>
<td align="right">248,900</td>
<td align="right">0.1%</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">183,540</td>
<td align="right">0.1%</td>
<td align="right">220,640</td>
<td align="right">0.1%</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">231,825,100</td>
<td align="right">96.6%</td>
<td align="right">231,788,700</td>
<td align="right">99.8%</td>
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
<td align="right">2,420</td>
<td align="right">41.2%</td>
<td align="right">520</td>
<td align="right">11.1%</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,460</td>
<td align="right">58.8%</td>
<td align="right">4,160</td>
<td align="right">88.9%</td>
<td align="right">20.2%</td>
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
<td align="left">split dict</td>
<td align="right">2,380</td>
<td align="right">98.3%</td>
<td align="right">480</td>
<td align="right">92.3%</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">8,060</td>
<td align="right">333.1%</td>
<td align="right">6,800</td>
<td align="right">1,307.7%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">40</td>
<td align="right">1.7%</td>
<td align="right">40</td>
<td align="right">7.7%</td>
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
<td align="right">26,704,940</td>
<td align="right">50.1%</td>
<td align="right">13,061,540</td>
<td align="right">33.0%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">26,554,200</td>
<td align="right">49.9%</td>
<td align="right">26,554,200</td>
<td align="right">67.0%</td>
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
<td align="right">8,980</td>
<td align="right">100.0%</td>
<td align="right">5,680</td>
<td align="right">100.0%</td>
<td align="right">-36.7%</td>
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
<td align="left">py simple</td>
<td align="right">8,980</td>
<td align="right">100.0%</td>
<td align="right">5,680</td>
<td align="right">100.0%</td>
<td align="right">-36.7%</td>
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
<td align="right">2,944,060</td>
<td align="right">2.3%</td>
<td align="right">1,144,820</td>
<td align="right">0.9%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,479,440</td>
<td align="right">1.1%</td>
<td align="right">1,241,140</td>
<td align="right">1.0%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">125,191,420</td>
<td align="right">96.6%</td>
<td align="right">124,902,780</td>
<td align="right">98.1%</td>
<td align="right">-0.2%</td>
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
<td align="right">55,540</td>
<td align="right">84.7%</td>
<td align="right">21,620</td>
<td align="right">57.7%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">10,000</td>
<td align="right">15.3%</td>
<td align="right">15,860</td>
<td align="right">42.3%</td>
<td align="right">58.6%</td>
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
<td align="right">6,300</td>
<td align="right">63.0%</td>
<td align="right">11,680</td>
<td align="right">73.6%</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,680</td>
<td align="right">26.8%</td>
<td align="right">3,160</td>
<td align="right">19.9%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,000</td>
<td align="right">10.0%</td>
<td align="right">1,000</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">36,819,480</td>
<td align="right">100.0%</td>
<td align="right">36,819,480</td>
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
<td align="right">102,418,600</td>
<td align="right">3.5%</td>
<td align="right">44,565,700</td>
<td align="right">2.9%</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,681,894,160</td>
<td align="right">57.0%</td>
<td align="right">766,749,900</td>
<td align="right">49.4%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,136,384,260</td>
<td align="right">38.5%</td>
<td align="right">710,456,940</td>
<td align="right">45.7%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">32,537,140</td>
<td align="right">1.1%</td>
<td align="right">31,828,720</td>
<td align="right">2.0%</td>
<td align="right">-2.2%</td>
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
<td align="right">986,360</td>
<td align="right">0.8%</td>
<td align="right">2,295,820</td>
<td align="right">3.2%</td>
<td align="right">132.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">27,895,580</td>
<td align="right">21.9%</td>
<td align="right">1,147,360</td>
<td align="right">1.6%</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">5,854,300</td>
<td align="right">4.6%</td>
<td align="right">824,500</td>
<td align="right">1.2%</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,704,940</td>
<td align="right">21.0%</td>
<td align="right">13,061,540</td>
<td align="right">18.4%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">798,060</td>
<td align="right">0.6%</td>
<td align="right">1,094,120</td>
<td align="right">1.5%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,841,820</td>
<td align="right">1.4%</td>
<td align="right">1,325,300</td>
<td align="right">1.9%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">28,381,380</td>
<td align="right">22.3%</td>
<td align="right">23,023,480</td>
<td align="right">32.5%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">1,479,440</td>
<td align="right">1.2%</td>
<td align="right">1,241,140</td>
<td align="right">1.8%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">25,024,820</td>
<td align="right">19.6%</td>
<td align="right">26,349,920</td>
<td align="right">37.2%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,029,800</td>
<td align="right">6.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">269,760</td>
<td align="right">0.4%</td>
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
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,339,980</td>
<td align="right">4.1%</td>
<td align="right">386,460</td>
<td align="right">1.2%</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,600,720</td>
<td align="right">4.9%</td>
<td align="right">756,060</td>
<td align="right">2.4%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">5,579,840</td>
<td align="right">17.1%</td>
<td align="right">2,780,900</td>
<td align="right">8.7%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">19,925,860</td>
<td align="right">61.2%</td>
<td align="right">24,075,380</td>
<td align="right">75.6%</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">183,180</td>
<td align="right">0.6%</td>
<td align="right">220,280</td>
<td align="right">0.7%</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,068,420</td>
<td align="right">6.4%</td>
<td align="right">1,674,620</td>
<td align="right">5.3%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,602,480</td>
<td align="right">4.9%</td>
<td align="right">1,699,420</td>
<td align="right">5.3%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">225,360</td>
<td align="right">0.7%</td>
<td align="right">225,360</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,160</td>
<td align="right">0.0%</td>
<td align="right">3,160</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,160</td>
<td align="right">0.0%</td>
<td align="right">3,160</td>
<td align="right">0.0%</td>
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
<td align="right">41,912,100</td>
<td align="right">26.4%</td>
<td align="right">41,912,100</td>
<td align="right">26.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">116,652,300</td>
<td align="right">73.6%</td>
<td align="right">116,652,300</td>
<td align="right">73.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">41,912,100</td>
<td align="right">26.4%</td>
<td align="right">41,912,100</td>
<td align="right">26.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">41,911,860</td>
<td align="right">26.4%</td>
<td align="right">41,911,860</td>
<td align="right">26.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">41,911,500</td>
<td align="right">26.4%</td>
<td align="right">41,911,500</td>
<td align="right">26.4%</td>
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
<td align="right">34,854,900</td>
<td align="right">22.0%</td>
<td align="right">34,854,900</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">73,800</td>
<td align="right">0.0%</td>
<td align="right">73,800</td>
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
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">162,577,500</td>
<td align="right">102.5%</td>
<td align="right">162,577,500</td>
<td align="right">102.5%</td>
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
<td align="right">497,218</td>
<td align="right"></td>
<td align="right">983,398</td>
<td align="right"></td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">514,461</td>
<td align="right"></td>
<td align="right">999,051</td>
<td align="right"></td>
<td align="right">94.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">323,521,160</td>
<td align="right">6.5%</td>
<td align="right">162,908,360</td>
<td align="right">3.2%</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">684,364,700</td>
<td align="right">11.4%</td>
<td align="right">350,735,700</td>
<td align="right">5.8%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,395,958,660</td>
<td align="right">27.9%</td>
<td align="right">932,213,380</td>
<td align="right">18.4%</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,726,485,820</td>
<td align="right">28.7%</td>
<td align="right">1,193,150,680</td>
<td align="right">19.6%</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,147,678,274</td>
<td align="right">35.7%</td>
<td align="right">2,760,599,504</td>
<td align="right">45.3%</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,242,034,251</td>
<td align="right">44.9%</td>
<td align="right">2,785,360,597</td>
<td align="right">54.9%</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,464,267,040</td>
<td align="right">24.3%</td>
<td align="right">1,792,524,618</td>
<td align="right">29.4%</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">3,100</td>
<td align="right">0.0%</td>
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,033,253,204</td>
<td align="right">20.7%</td>
<td align="right">1,195,076,894</td>
<td align="right">23.5%</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">25,420</td>
<td align="right"></td>
<td align="right">23,682</td>
<td align="right"></td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">75,638,462</td>
<td align="right"></td>
<td align="right">75,217,722</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">27,487,820</td>
<td align="right">8.8%</td>
<td align="right">27,491,120</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">136,138,660</td>
<td align="right">43.4%</td>
<td align="right">136,143,060</td>
<td align="right">43.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">163,729,170</td>
<td align="right"></td>
<td align="right">163,733,715</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">84,884,160</td>
<td align="right"></td>
<td align="right">84,882,598</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">177,215,240</td>
<td align="right"></td>
<td align="right">177,216,320</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">177,215,980</td>
<td align="right">56.6%</td>
<td align="right">177,217,060</td>
<td align="right">56.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">108,647,740</td>
<td align="right">34.7%</td>
<td align="right">108,648,240</td>
<td align="right">34.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">36,013,800</td>
<td align="right"></td>
<td align="right">36,013,800</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">6,660</td>
<td align="right">8,249,180</td>
<td align="right">220,941,887</td>
<td align="right">6,660</td>
<td align="right">8,249,180</td>
<td align="right">222,251,386</td>
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
<td align="right">1,660</td>
<td align="right">11.6%</td>
<td align="right">6,080</td>
<td align="right">50.4%</td>
<td align="right">266.3%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">440</td>
<td align="right">26.5%</td>
<td align="right">900</td>
<td align="right">14.8%</td>
<td align="right">104.5%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">120</td>
<td align="right">0.8%</td>
<td align="right">220</td>
<td align="right">1.8%</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">8,740</td>
<td align="right">61.3%</td>
<td align="right">2,280</td>
<td align="right">18.9%</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">12,600</td>
<td align="right">88.4%</td>
<td align="right">5,980</td>
<td align="right">49.6%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">215,662,720</td>
<td align="right"></td>
<td align="right">300,609,000</td>
<td align="right"></td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">7,949,150,160</td>
<td align="right">3,685.9%</td>
<td align="right">10,619,136,320</td>
<td align="right">3,532.5%</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">14,260</td>
<td align="right"></td>
<td align="right">12,060</td>
<td align="right"></td>
<td align="right">-15.4%</td>
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
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40 / 0 !!</td>
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
<td align="right">1,540</td>
<td align="right">92.8%</td>
<td align="right">6,080</td>
<td align="right">100.0%</td>
<td align="right">294.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,660</td>
<td align="right"></td>
<td align="right">6,080</td>
<td align="right"></td>
<td align="right">266.3%</td>
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
<td align="right">120</td>
<td align="right">7.2%</td>
<td align="right">60</td>
<td align="right">1.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">240</td>
<td align="right">14.5%</td>
<td align="right">2,980</td>
<td align="right">49.0%</td>
<td align="right">1,141.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">220</td>
<td align="right">13.3%</td>
<td align="right">880</td>
<td align="right">14.5%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">280</td>
<td align="right">16.9%</td>
<td align="right">680</td>
<td align="right">11.2%</td>
<td align="right">142.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">180</td>
<td align="right">10.8%</td>
<td align="right">320</td>
<td align="right">5.3%</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">500</td>
<td align="right">30.1%</td>
<td align="right">920</td>
<td align="right">15.1%</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">120</td>
<td align="right">7.2%</td>
<td align="right">240</td>
<td align="right">3.9%</td>
<td align="right">100.0%</td>
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
<td align="right">4.8%</td>
<td align="right">60</td>
<td align="right">1.0%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">260</td>
<td align="right">15.7%</td>
<td align="right">400</td>
<td align="right">6.6%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">100</td>
<td align="right">6.0%</td>
<td align="right">2,960</td>
<td align="right">48.7%</td>
<td align="right">2,860.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">380</td>
<td align="right">22.9%</td>
<td align="right">1,020</td>
<td align="right">16.8%</td>
<td align="right">168.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">160</td>
<td align="right">9.6%</td>
<td align="right">440</td>
<td align="right">7.2%</td>
<td align="right">175.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">160</td>
<td align="right">9.6%</td>
<td align="right">320</td>
<td align="right">5.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">360</td>
<td align="right">21.7%</td>
<td align="right">880</td>
<td align="right">14.5%</td>
<td align="right">144.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
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
<td align="left">_BINARY_SUBSCR</td>
<td align="right">67,060</td>
<td align="right">26,815,280</td>
<td align="right">39,887.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">67,060</td>
<td align="right">13,710,460</td>
<td align="right">20,345.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">883,060</td>
<td align="right">69,513,800</td>
<td align="right">7,771.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">61,820</td>
<td align="right">2,256,660</td>
<td align="right">3,550.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,863,660</td>
<td align="right">67,186,960</td>
<td align="right">3,505.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">10,296,680</td>
<td align="right">67,679,440</td>
<td align="right">557.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">693,340</td>
<td align="right">3,177,820</td>
<td align="right">358.3%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">688,100</td>
<td align="right">2,380,960</td>
<td align="right">246.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">688,100</td>
<td align="right">2,380,960</td>
<td align="right">246.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">27,403,260</td>
<td align="right">87,717,680</td>
<td align="right">220.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">20,336,240</td>
<td align="right">51,540,560</td>
<td align="right">153.4%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">20,336,240</td>
<td align="right">51,540,560</td>
<td align="right">153.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">81,108,100</td>
<td align="right">165,427,540</td>
<td align="right">104.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">61,820</td>
<td align="right">1,700</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">519,120</td>
<td align="right">100,320</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">300,600</td>
<td align="right">538,960</td>
<td align="right">79.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">2,721,460</td>
<td align="right">607,780</td>
<td align="right">-77.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,461,900</td>
<td align="right">557,620</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,917,940</td>
<td align="right">464,160</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">85,983,180</td>
<td align="right">149,873,580</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">7,369,740</td>
<td align="right">12,736,620</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">7,369,740</td>
<td align="right">12,736,620</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">7,369,740</td>
<td align="right">12,736,620</td>
<td align="right">72.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">550,700</td>
<td align="right">928,240</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">61,222,620</td>
<td align="right">102,808,740</td>
<td align="right">67.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">68,437,620</td>
<td align="right">113,835,480</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">706,457,800</td>
<td align="right">1,110,491,060</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">519,120</td>
<td align="right">223,060</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">1,863,660</td>
<td align="right">2,816,320</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">1,863,660</td>
<td align="right">2,816,320</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">316,281,840</td>
<td align="right">459,142,140</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">183,095,920</td>
<td align="right">260,360,640</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">94,041,300</td>
<td align="right">133,574,540</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">7,004,520</td>
<td align="right">9,803,980</td>
<td align="right">40.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">215,662,720</td>
<td align="right">300,609,000</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">254,302,260</td>
<td align="right">351,989,240</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">1,005,061,000</td>
<td align="right">1,381,407,640</td>
<td align="right">37.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">228,949,300</td>
<td align="right">313,625,540</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,757,080</td>
<td align="right">2,355,500</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">25,620,800</td>
<td align="right">33,311,140</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">880,840,300</td>
<td align="right">1,144,302,420</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">20,336,240</td>
<td align="right">26,418,000</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">480</td>
<td align="right">620</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">33,640,480</td>
<td align="right">43,147,120</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">80,453,200</td>
<td align="right">102,433,900</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">3,203,380</td>
<td align="right">2,336,060</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">123,098,580</td>
<td align="right">154,996,240</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,252,560</td>
<td align="right">933,880</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">645,540</td>
<td align="right">481,740</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">73,268,500</td>
<td align="right">91,555,100</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">20,336,240</td>
<td align="right">25,366,040</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">20,336,240</td>
<td align="right">25,366,040</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">23,360,580</td>
<td align="right">29,046,920</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">28,027,580</td>
<td align="right">34,681,420</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">8,041,600</td>
<td align="right">6,275,880</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">6,012,880</td>
<td align="right">4,703,420</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">20,678,520</td>
<td align="right">25,074,660</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">129,942,940</td>
<td align="right">156,529,700</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">19,316,300</td>
<td align="right">23,254,660</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">19,316,300</td>
<td align="right">23,254,660</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">6,719,100</td>
<td align="right">8,075,460</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">30,411,280</td>
<td align="right">36,360,060</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">55,420,680</td>
<td align="right">66,051,160</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">29,195,040</td>
<td align="right">34,668,860</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">41,967,520</td>
<td align="right">49,511,180</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">25,275,040</td>
<td align="right">29,814,500</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">90,985,140</td>
<td align="right">107,091,640</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">197,108,160</td>
<td align="right">231,576,460</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">197,108,160</td>
<td align="right">231,576,460</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">91,555,460</td>
<td align="right">107,125,640</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">129,877,740</td>
<td align="right">151,221,180</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">129,877,740</td>
<td align="right">151,221,180</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">129,877,740</td>
<td align="right">151,221,180</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">96,221,800</td>
<td align="right">111,577,500</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">13,951,400</td>
<td align="right">11,789,760</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">40,908,280</td>
<td align="right">47,134,480</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">40,858,020</td>
<td align="right">46,925,380</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">8,150,300</td>
<td align="right">9,294,940</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">44,330,120</td>
<td align="right">49,914,440</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">44,330,120</td>
<td align="right">49,914,440</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">182,107,300</td>
<td align="right">203,159,200</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">24,753,260</td>
<td align="right">27,579,380</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">63,050,740</td>
<td align="right">68,907,520</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">63,050,740</td>
<td align="right">68,907,520</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">11,697,220</td>
<td align="right">10,623,540</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">213,798,580</td>
<td align="right">233,421,420</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">26,513,380</td>
<td align="right">28,928,300</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">18,824,900</td>
<td align="right">20,462,520</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">176,426,600</td>
<td align="right">191,608,320</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">12,398,040</td>
<td align="right">13,389,640</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,446,420</td>
<td align="right">33,493,280</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">28,590,260</td>
<td align="right">30,115,560</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,907,600</td>
<td align="right">2,794,400</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">45,378,760</td>
<td align="right">47,085,980</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">22,889,600</td>
<td align="right">23,709,380</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">22,889,600</td>
<td align="right">23,709,380</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">31,472,680</td>
<td align="right">30,448,480</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">31,472,680</td>
<td align="right">30,448,480</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">32,506,140</td>
<td align="right">33,493,280</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">17,545,140</td>
<td align="right">18,061,660</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">89,103,720</td>
<td align="right">91,426,720</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">29,124,700</td>
<td align="right">28,413,740</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">13,286,580</td>
<td align="right">13,016,540</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">7,996,080</td>
<td align="right">7,853,120</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">60,926,080</td>
<td align="right">62,009,400</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">28,120,340</td>
<td align="right">28,595,620</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">22,889,600</td>
<td align="right">23,276,100</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">12,334,900</td>
<td align="right">12,433,660</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">28,569,820</td>
<td align="right">28,362,500</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">33,894,120</td>
<td align="right">34,139,800</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">26,778,820</td>
<td align="right">26,607,380</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">34,778,220</td>
<td align="right">34,990,580</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">7,942,360</td>
<td align="right">7,968,860</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">27,038,440</td>
<td align="right">26,958,380</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">14,786,180</td>
<td align="right">14,743,560</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">17,153,700</td>
<td align="right">17,193,600</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">17,153,520</td>
<td align="right">17,153,400</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">4,047,480</td>
<td align="right">4,047,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">8,700</td>
<td align="right">8,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">7,780,900</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">3,209,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">1,053,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">1,053,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right"></td>
<td align="right">694,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right"></td>
<td align="right">531,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right"></td>
<td align="right">408,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">241,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">136,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">74,460</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right"></td>
<td align="right">74,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right"></td>
<td align="right">73,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">66,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">40,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">40,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right"></td>
<td align="right">36,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">25,120</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">25,120</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right"></td>
<td align="right">18,360</td>
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
<td align="right">4,320</td>
<td align="right">5,980</td>
<td align="right">38.4%</td>
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
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
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
Stats gathered on: 2025-05-05
