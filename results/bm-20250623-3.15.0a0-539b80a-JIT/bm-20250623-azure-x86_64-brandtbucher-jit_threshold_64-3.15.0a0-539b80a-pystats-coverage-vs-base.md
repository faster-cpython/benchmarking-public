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
<td align="left">CONTAINS_OP</td>
<td align="right">249,460</td>
<td align="right">7,700</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">249,660</td>
<td align="right">7,920</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">250,080</td>
<td align="right">8,340</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">252,740</td>
<td align="right">10,620</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">253,440</td>
<td align="right">11,700</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">561,600</td>
<td align="right">65,840</td>
<td align="right">-88.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">302,829</td>
<td align="right">42,614</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">18,720</td>
<td align="right">5,760</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">19,460</td>
<td align="right">6,680</td>
<td align="right">-65.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">25,260</td>
<td align="right">12,300</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">15,960</td>
<td align="right">9,300</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">14,820</td>
<td align="right">8,680</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">8,580</td>
<td align="right">5,220</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">8,220</td>
<td align="right">5,220</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">41,769</td>
<td align="right">26,814</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">25,260</td>
<td align="right">16,260</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,580</td>
<td align="right">3,942</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">56,409</td>
<td align="right">40,434</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">154,809</td>
<td align="right">113,454</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">11,640</td>
<td align="right">8,640</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">12,360</td>
<td align="right">9,360</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">19,620</td>
<td align="right">14,982</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">6,960</td>
<td align="right">5,322</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">12,780</td>
<td align="right">9,780</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">41,940</td>
<td align="right">34,162</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">19,920</td>
<td align="right">16,920</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">22,140</td>
<td align="right">19,380</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">29,829</td>
<td align="right">26,814</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">32,409</td>
<td align="right">29,394</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">6,420</td>
<td align="right">5,850</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">73,429</td>
<td align="right">67,414</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">3,780</td>
<td align="right">4,020</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">3,780</td>
<td align="right">4,020</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">3,780</td>
<td align="right">4,020</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">2,640</td>
<td align="right">2,500</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">73,080</td>
<td align="right">69,940</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">6,660</td>
<td align="right">6,900</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">8,280</td>
<td align="right">8,000</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">73,440</td>
<td align="right">71,762</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">87,260</td>
<td align="right">85,622</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">29,515,620</td>
<td align="right">29,242,980</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">73,500</td>
<td align="right">72,930</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">26,220</td>
<td align="right">26,080</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">73,475,358</td>
<td align="right">73,160,652</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">29,040</td>
<td align="right">29,140</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">81,480</td>
<td align="right">81,200</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,687,280</td>
<td align="right">14,684,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">29,147,340</td>
<td align="right">29,144,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">29,196,900</td>
<td align="right">29,195,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">58,294,440</td>
<td align="right">58,291,440</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">29,140,140</td>
<td align="right">29,140,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right">29,134,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">29,134,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,570,000</td>
<td align="right">14,570,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">14,569,380</td>
<td align="right">14,569,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">29,520</td>
<td align="right">29,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">18,180</td>
<td align="right">18,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,120</td>
<td align="right">15,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">12,900</td>
<td align="right">12,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">12,420</td>
<td align="right">12,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">12,240</td>
<td align="right">12,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">11,100</td>
<td align="right">11,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">10,800</td>
<td align="right">10,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">9,000</td>
<td align="right">9,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">8,940</td>
<td align="right">8,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">8,820</td>
<td align="right">8,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">7,700</td>
<td align="right">7,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,260</td>
<td align="right">7,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">6,480</td>
<td align="right">6,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,120</td>
<td align="right">6,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,000</td>
<td align="right">6,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">5,520</td>
<td align="right">5,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">5,280</td>
<td align="right">5,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">5,260</td>
<td align="right">5,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">5,160</td>
<td align="right">5,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">4,560</td>
<td align="right">4,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,260</td>
<td align="right">4,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">4,200</td>
<td align="right">4,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">3,900</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">3,700</td>
<td align="right">3,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">3,600</td>
<td align="right">3,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">3,600</td>
<td align="right">3,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,480</td>
<td align="right">3,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,420</td>
<td align="right">3,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">3,360</td>
<td align="right">3,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,240</td>
<td align="right">3,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">3,000</td>
<td align="right">3,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,760</td>
<td align="right">2,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,460</td>
<td align="right">2,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">2,280</td>
<td align="right">2,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">2,220</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">2,160</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,100</td>
<td align="right">2,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">1,980</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,980</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,980</td>
<td align="right">1,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,860</td>
<td align="right">1,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">1,860</td>
<td align="right">1,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,860</td>
<td align="right">1,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,380</td>
<td align="right">1,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,380</td>
<td align="right">1,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,280</td>
<td align="right">1,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">1,140</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,140</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,020</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,020</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,020</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,020</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">780</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">780</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">780</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">340</td>
<td align="right">340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
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
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">1,970</td>
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
<td align="right">7,140</td>
<td align="right">0.0%</td>
<td align="right">7,140</td>
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
<td align="right">43,743,060</td>
<td align="right">100.0%</td>
<td align="right">43,743,060</td>
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
<td align="right">100</td>
<td align="right">17.9%</td>
<td align="right">100</td>
<td align="right">17.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">460</td>
<td align="right">82.1%</td>
<td align="right">460</td>
<td align="right">82.1%</td>
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
<td align="right">80</td>
<td align="right">17.4%</td>
<td align="right">80</td>
<td align="right">17.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">80</td>
<td align="right">17.4%</td>
<td align="right">80</td>
<td align="right">17.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">60</td>
<td align="right">13.0%</td>
<td align="right">60</td>
<td align="right">13.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">60</td>
<td align="right">13.0%</td>
<td align="right">60</td>
<td align="right">13.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">40</td>
<td align="right">8.7%</td>
<td align="right">40</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">40</td>
<td align="right">8.7%</td>
<td align="right">40</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">40</td>
<td align="right">8.7%</td>
<td align="right">40</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right">20</td>
<td align="right">4.3%</td>
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
<td align="right">2,940</td>
<td align="right">100.0%</td>
<td align="right">2,940</td>
<td align="right">100.0%</td>
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
<td align="right">29,314,209</td>
<td align="right">100.0%</td>
<td align="right">29,315,154</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
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
<td align="right">3,240</td>
<td align="right">100.0%</td>
<td align="right">3,240</td>
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
<td align="right">29,166,300</td>
<td align="right">100.0%</td>
<td align="right">29,166,300</td>
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
<td align="right">40.0%</td>
<td align="right">40</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">60</td>
<td align="right">60.0%</td>
<td align="right">60</td>
<td align="right">60.0%</td>
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
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">40</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">20</td>
<td align="right">33.3%</td>
<td align="right">20</td>
<td align="right">33.3%</td>
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
<td align="right">249,180</td>
<td align="right">98.5%</td>
<td align="right">7,440</td>
<td align="right">65.8%</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,600</td>
<td align="right">1.4%</td>
<td align="right">3,600</td>
<td align="right">31.9%</td>
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
<td align="right">200</td>
<td align="right">71.4%</td>
<td align="right">180</td>
<td align="right">69.2%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">80</td>
<td align="right">28.6%</td>
<td align="right">80</td>
<td align="right">30.8%</td>
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
<td align="right">60</td>
<td align="right">30.0%</td>
<td align="right">40</td>
<td align="right">22.2%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">80</td>
<td align="right">40.0%</td>
<td align="right">80</td>
<td align="right">44.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">60</td>
<td align="right">30.0%</td>
<td align="right">60</td>
<td align="right">33.3%</td>
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
<td align="right">252,240</td>
<td align="right">82.1%</td>
<td align="right">10,140</td>
<td align="right">20.2%</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">54,549</td>
<td align="right">17.8%</td>
<td align="right">39,594</td>
<td align="right">78.9%</td>
<td align="right">-27.4%</td>
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
<td align="right">360</td>
<td align="right">72.0%</td>
<td align="right">340</td>
<td align="right">70.8%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">140</td>
<td align="right">28.0%</td>
<td align="right">140</td>
<td align="right">29.2%</td>
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
<td align="right">160</td>
<td align="right">44.4%</td>
<td align="right">140</td>
<td align="right">41.2%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">80</td>
<td align="right">22.2%</td>
<td align="right">80</td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">80</td>
<td align="right">22.2%</td>
<td align="right">80</td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">40</td>
<td align="right">11.1%</td>
<td align="right">40</td>
<td align="right">11.8%</td>
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
<td align="right">7,020</td>
<td align="right">7,020 / 0 !!</td>
<td align="right">7,020</td>
<td align="right">7,020 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">900</td>
<td align="right">900 / 0 !!</td>
<td align="right">900</td>
<td align="right">900 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">720</td>
<td align="right">720 / 0 !!</td>
<td align="right">720</td>
<td align="right">720 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">360</td>
<td align="right">360 / 0 !!</td>
<td align="right">360</td>
<td align="right">360 / 0 !!</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">180,049</td>
<td align="right">86.8%</td>
<td align="right">150,974</td>
<td align="right">84.7%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,120</td>
<td align="right">9.7%</td>
<td align="right">19,980</td>
<td align="right">11.2%</td>
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
<td align="right">1,140</td>
<td align="right">0.5%</td>
<td align="right">1,140</td>
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
<td align="right">4,900</td>
<td align="right">83.6%</td>
<td align="right">4,900</td>
<td align="right">83.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">960</td>
<td align="right">16.4%</td>
<td align="right">960</td>
<td align="right">16.4%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">380</td>
<td align="right">39.6%</td>
<td align="right">380</td>
<td align="right">39.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">300</td>
<td align="right">31.2%</td>
<td align="right">300</td>
<td align="right">31.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">100</td>
<td align="right">10.4%</td>
<td align="right">100</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">60</td>
<td align="right">6.2%</td>
<td align="right">60</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">60</td>
<td align="right">6.2%</td>
<td align="right">60</td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">40</td>
<td align="right">4.2%</td>
<td align="right">40</td>
<td align="right">4.2%</td>
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
<td align="right">14,760,540</td>
<td align="right">50.3%</td>
<td align="right">14,755,722</td>
<td align="right">50.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,567,820</td>
<td align="right">49.7%</td>
<td align="right">14,567,820</td>
<td align="right">49.7%</td>
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
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">180</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,160</td>
<td align="right">100.0%</td>
<td align="right">2,160</td>
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
<td align="right">8,880</td>
<td align="right">30.6%</td>
<td align="right">8,880</td>
<td align="right">30.6%</td>
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
<td align="right">16,140</td>
<td align="right">55.6%</td>
<td align="right">16,140</td>
<td align="right">55.6%</td>
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
<td align="right">2,640</td>
<td align="right">65.7%</td>
<td align="right">2,640</td>
<td align="right">65.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,380</td>
<td align="right">34.3%</td>
<td align="right">1,380</td>
<td align="right">34.3%</td>
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
<td align="left">not in dict</td>
<td align="right">1,220</td>
<td align="right">88.4%</td>
<td align="right">1,220</td>
<td align="right">88.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">80</td>
<td align="right">5.8%</td>
<td align="right">80</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">40</td>
<td align="right">2.9%</td>
<td align="right">40</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">20</td>
<td align="right">1.4%</td>
<td align="right">20</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">20</td>
<td align="right">1.4%</td>
<td align="right">20</td>
<td align="right">1.4%</td>
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
<td align="right">270,780</td>
<td align="right">100.0%</td>
<td align="right">270,780</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">114,809</td>
<td align="right">93.8%</td>
<td align="right">114,794</td>
<td align="right">93.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,440</td>
<td align="right">2.8%</td>
<td align="right">3,440</td>
<td align="right">2.8%</td>
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
<td align="right">2,300</td>
<td align="right">1.9%</td>
<td align="right">2,300</td>
<td align="right">1.9%</td>
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
<td align="right">1,520</td>
<td align="right">81.7%</td>
<td align="right">1,520</td>
<td align="right">81.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">340</td>
<td align="right">18.3%</td>
<td align="right">340</td>
<td align="right">18.3%</td>
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
<td align="right">120</td>
<td align="right">35.3%</td>
<td align="right">120</td>
<td align="right">35.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">100</td>
<td align="right">29.4%</td>
<td align="right">100</td>
<td align="right">29.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">60</td>
<td align="right">17.6%</td>
<td align="right">60</td>
<td align="right">17.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">40</td>
<td align="right">11.8%</td>
<td align="right">40</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">5.9%</td>
<td align="right">20</td>
<td align="right">5.9%</td>
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
<td align="right">272,340</td>
<td align="right">100.0%</td>
<td align="right">272,340</td>
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
<td align="right">15,139,960</td>
<td align="right">3.7%</td>
<td align="right">14,655,940</td>
<td align="right">3.6%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">118,265,845</td>
<td align="right">28.7%</td>
<td align="right">117,396,698</td>
<td align="right">28.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">279,301,956</td>
<td align="right">67.7%</td>
<td align="right">277,904,876</td>
<td align="right">67.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">15,160</td>
<td align="right">0.0%</td>
<td align="right">15,160</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">249,180</td>
<td align="right">1.6%</td>
<td align="right">7,440</td>
<td align="right">0.1%</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">252,240</td>
<td align="right">1.7%</td>
<td align="right">10,140</td>
<td align="right">0.1%</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">20,120</td>
<td align="right">0.1%</td>
<td align="right">19,980</td>
<td align="right">0.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,567,820</td>
<td align="right">96.4%</td>
<td align="right">14,567,820</td>
<td align="right">99.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,880</td>
<td align="right">0.1%</td>
<td align="right">8,880</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">7,140</td>
<td align="right">0.0%</td>
<td align="right">7,140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,440</td>
<td align="right">0.0%</td>
<td align="right">3,440</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">11,480</td>
<td align="right">43.1%</td>
<td align="right">11,480</td>
<td align="right">43.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">11,480</td>
<td align="right">43.1%</td>
<td align="right">11,480</td>
<td align="right">43.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,240</td>
<td align="right">4.7%</td>
<td align="right">1,240</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,060</td>
<td align="right">4.0%</td>
<td align="right">1,060</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">600</td>
<td align="right">2.3%</td>
<td align="right">600</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">540</td>
<td align="right">2.0%</td>
<td align="right">540</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">180</td>
<td align="right">0.7%</td>
<td align="right">180</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.2%</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
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
<td align="left">Frames pushed</td>
<td align="right">29,208,120</td>
<td align="right">100.0%</td>
<td align="right">29,208,600</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">29,213,100</td>
<td align="right">100.0%</td>
<td align="right">29,213,580</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">29,138,780</td>
<td align="right">99.7%</td>
<td align="right">29,139,020</td>
<td align="right">99.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,320</td>
<td align="right">0.0%</td>
<td align="right">7,320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,320</td>
<td align="right">0.0%</td>
<td align="right">7,320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">5,040</td>
<td align="right">0.0%</td>
<td align="right">5,040</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">2,280</td>
<td align="right">0.0%</td>
<td align="right">2,280</td>
<td align="right">0.0%</td>
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
<td align="right">5,040</td>
<td align="right">0.0%</td>
<td align="right">5,040</td>
<td align="right">0.0%</td>
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
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">960</td>
<td align="right">0.0%</td>
<td align="right">960</td>
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
<td align="left">Interpreter immortal increfs</td>
<td align="right">487,500</td>
<td align="right">0.1%</td>
<td align="right">50,370</td>
<td align="right">0.0%</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">2,460</td>
<td align="right">0.0%</td>
<td align="right">2,600</td>
<td align="right">0.0%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">2,933</td>
<td align="right"></td>
<td align="right">3,046</td>
<td align="right"></td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">2,727</td>
<td align="right"></td>
<td align="right">2,798</td>
<td align="right"></td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">2,820</td>
<td align="right">0.0%</td>
<td align="right">2,880</td>
<td align="right">0.0%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">533</td>
<td align="right"></td>
<td align="right">542</td>
<td align="right"></td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">88,391,638</td>
<td align="right">12.0%</td>
<td align="right">88,051,379</td>
<td align="right">12.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">44,305,918</td>
<td align="right">6.8%</td>
<td align="right">44,168,550</td>
<td align="right">6.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">238,185,631</td>
<td align="right">36.7%</td>
<td align="right">238,628,256</td>
<td align="right">36.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">497,820</td>
<td align="right"></td>
<td align="right">498,540</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">500,320</td>
<td align="right">0.8%</td>
<td align="right">501,040</td>
<td align="right">0.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">292,890,584</td>
<td align="right">39.8%</td>
<td align="right">293,234,495</td>
<td align="right">39.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">365,441,152</td>
<td align="right">56.4%</td>
<td align="right">365,579,894</td>
<td align="right">56.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">42,367</td>
<td align="right"></td>
<td align="right">42,358</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">58,532,738</td>
<td align="right"></td>
<td align="right">58,534,711</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">58,518,100</td>
<td align="right">99.2%</td>
<td align="right">58,519,740</td>
<td align="right">99.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">58,512,820</td>
<td align="right">99.1%</td>
<td align="right">58,514,260</td>
<td align="right">99.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">355,324,992</td>
<td align="right">48.2%</td>
<td align="right">355,330,064</td>
<td align="right">48.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">29,181,113</td>
<td align="right"></td>
<td align="right">29,181,202</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,980</td>
<td align="right"></td>
<td align="right">1,980</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">12,240</td>
<td align="right">0.0%</td>
<td align="right">12,240</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">180</td>
<td align="right">9.1%</td>
<td align="right">180</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">180</td>
<td align="right">9.1%</td>
<td align="right">180</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">120</td>
<td align="right">6.1%</td>
<td align="right">120</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
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
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">60</td>
<td align="right"></td>
<td align="right">2,230</td>
<td align="right"></td>
<td align="right">3,616.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">591,840</td>
<td align="right">986,400.0%</td>
<td align="right">8,166,264</td>
<td align="right">366,200.2%</td>
<td align="right">1,279.8%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">120</td>
<td align="right">200.0%</td>
<td align="right">620</td>
<td align="right">221.4%</td>
<td align="right">416.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">60</td>
<td align="right"></td>
<td align="right">300</td>
<td align="right"></td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">280</td>
<td align="right">93.3%</td>
<td align="right">366.7%</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
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
<td align="right">20</td>
<td align="right">6.7%</td>
<td align="right">20 / 0 !!</td>
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
<td align="right">60</td>
<td align="right"></td>
<td align="right">280</td>
<td align="right"></td>
<td align="right">366.7%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">260</td>
<td align="right">92.9%</td>
<td align="right">333.3%</td>
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
<td align="right">340,020</td>
<td align="right">69.2%</td>
<td align="right">2,779,740</td>
<td align="right">87.0%</td>
<td align="right">717.5%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">11,040</td>
<td align="right">2.2%</td>
<td align="right">75,360</td>
<td align="right">2.4%</td>
<td align="right">582.6%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">491,520</td>
<td align="right"></td>
<td align="right">3,194,880</td>
<td align="right"></td>
<td align="right">550.0%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">140,460</td>
<td align="right">28.6%</td>
<td align="right">339,780</td>
<td align="right">10.6%</td>
<td align="right">141.9%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="left"><= 8,192</td>
<td align="left">60</td>
<td align="right">100.0%</td>
<td align="left">180</td>
<td align="right">69.2%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">20</td>
<td align="right">7.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">60</td>
<td align="right">23.1%</td>
<td align="right"></td>
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
<td align="left"><= 64</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">180</td>
<td align="right">64.3%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">40</td>
<td align="right">14.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">60</td>
<td align="right">21.4%</td>
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
<td align="left"><= 32</td>
<td align="right">60</td>
<td align="right">100.0%</td>
<td align="right">60</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">140</td>
<td align="right">50.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">60</td>
<td align="right">21.4%</td>
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
<td align="left">_START_EXECUTOR</td>
<td align="right">60</td>
<td align="right">2,230</td>
<td align="right">3,616.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">60</td>
<td align="right">1,162</td>
<td align="right">1,836.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">21,180</td>
<td align="right">305,490</td>
<td align="right">1,342.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">105,660</td>
<td align="right">1,442,116</td>
<td align="right">1,264.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">126,840</td>
<td align="right">1,724,704</td>
<td align="right">1,259.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">21,120</td>
<td align="right">283,938</td>
<td align="right">1,244.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">21,180</td>
<td align="right">282,060</td>
<td align="right">1,231.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">21,120</td>
<td align="right">279,830</td>
<td align="right">1,225.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">21,120</td>
<td align="right">278,218</td>
<td align="right">1,217.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">21,120</td>
<td align="right">277,860</td>
<td align="right">1,215.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">21,120</td>
<td align="right">275,960</td>
<td align="right">1,206.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">42,240</td>
<td align="right">541,820</td>
<td align="right">1,182.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">21,120</td>
<td align="right">266,140</td>
<td align="right">1,160.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">21,120</td>
<td align="right">263,000</td>
<td align="right">1,145.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">21,120</td>
<td align="right">262,860</td>
<td align="right">1,144.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">21,120</td>
<td align="right">262,860</td>
<td align="right">1,144.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">21,120</td>
<td align="right">262,860</td>
<td align="right">1,144.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">21,120</td>
<td align="right">262,860</td>
<td align="right">1,144.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">21,120</td>
<td align="right">262,860</td>
<td align="right">1,144.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">21,180</td>
<td align="right">263,280</td>
<td align="right">1,143.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right"></td>
<td align="right">36,360</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right"></td>
<td align="right">18,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right"></td>
<td align="right">15,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right"></td>
<td align="right">15,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right"></td>
<td align="right">15,078</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right"></td>
<td align="right">15,078</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right"></td>
<td align="right">15,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">12,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">12,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">12,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right"></td>
<td align="right">12,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right"></td>
<td align="right">12,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right"></td>
<td align="right">12,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right"></td>
<td align="right">12,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right"></td>
<td align="right">12,920</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right"></td>
<td align="right">12,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right"></td>
<td align="right">10,656</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right">9,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right"></td>
<td align="right">6,360</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">6,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right"></td>
<td align="right">6,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right"></td>
<td align="right">5,398</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right"></td>
<td align="right">5,258</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right"></td>
<td align="right">3,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right"></td>
<td align="right">3,360</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right"></td>
<td align="right">3,140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">3,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right"></td>
<td align="right">2,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">2,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">2,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right"></td>
<td align="right">2,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right"></td>
<td align="right">2,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right"></td>
<td align="right">2,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right"></td>
<td align="right">2,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right"></td>
<td align="right">2,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right"></td>
<td align="right">2,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right"></td>
<td align="right">2,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">1,068</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">1,050</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right"></td>
<td align="right">1,050</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right"></td>
<td align="right">140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right"></td>
<td align="right">140</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right"></td>
<td align="right">140</td>
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
Stats gathered on: 2025-06-24
