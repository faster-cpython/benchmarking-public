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
<td align="left">DELETE_SUBSCR</td>
<td align="right">41,768,220</td>
<td align="right">180,640</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">41,773,240</td>
<td align="right">185,660</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">55,993,900</td>
<td align="right">316,520</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">6,882,560</td>
<td align="right">77,560</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">10,469,700</td>
<td align="right">131,780</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">7,450,000</td>
<td align="right">110,920</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">11,901,500</td>
<td align="right">205,380</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">21,930,560</td>
<td align="right">379,120</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,429,100</td>
<td align="right">148,100</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">78,695,660</td>
<td align="right">1,585,260</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">10,788,160</td>
<td align="right">273,500</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">11,265,220</td>
<td align="right">313,400</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">88,254,760</td>
<td align="right">2,626,040</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,399,220</td>
<td align="right">1,125,620</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">35,436,020</td>
<td align="right">2,122,720</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">554,260</td>
<td align="right">37,740</td>
<td align="right">-93.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">12,809,300</td>
<td align="right">879,700</td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">43,853,160</td>
<td align="right">3,298,300</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">12,164,180</td>
<td align="right">1,023,760</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">149,027,340</td>
<td align="right">13,906,400</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,090,340</td>
<td align="right">862,300</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">105,765,900</td>
<td align="right">12,011,280</td>
<td align="right">-88.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">871,640</td>
<td align="right">103,880</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,886,680</td>
<td align="right">225,860</td>
<td align="right">-88.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,398,980</td>
<td align="right">291,540</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">19,385,480</td>
<td align="right">2,724,700</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">118,913,540</td>
<td align="right">19,135,060</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">730,420</td>
<td align="right">120,500</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">9,456,000</td>
<td align="right">1,632,160</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">27,300,580</td>
<td align="right">4,775,360</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">16,339,540</td>
<td align="right">2,894,380</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">14,851,100</td>
<td align="right">2,638,080</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,139,960</td>
<td align="right">210,420</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">943,757,220</td>
<td align="right">181,024,980</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">7,792,260</td>
<td align="right">1,724,080</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">517,780</td>
<td align="right">117,220</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">322,462,280</td>
<td align="right">81,139,900</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">65,363,420</td>
<td align="right">16,964,520</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">38,112,500</td>
<td align="right">11,435,520</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">25,804,320</td>
<td align="right">9,906,800</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,073,680</td>
<td align="right">2,402,140</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">26,817,000</td>
<td align="right">10,680,300</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,078,380</td>
<td align="right">430,700</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">128,260</td>
<td align="right">59,840</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,122,800</td>
<td align="right">1,586,860</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">177,666,500</td>
<td align="right">90,932,480</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">83,379,260</td>
<td align="right">43,151,000</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">90,801,700</td>
<td align="right">47,993,920</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">55,371,120</td>
<td align="right">30,602,060</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">371,840</td>
<td align="right">211,680</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">66,182,700</td>
<td align="right">39,348,160</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">91,910,900</td>
<td align="right">55,549,940</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,201,100</td>
<td align="right">1,972,780</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">81,380</td>
<td align="right">111,860</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">7,960</td>
<td align="right">4,980</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">12,726,040</td>
<td align="right">8,474,540</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">62,359,560</td>
<td align="right">41,632,720</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">7,620</td>
<td align="right">10,100</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">5,216,720</td>
<td align="right">3,616,920</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">68,540</td>
<td align="right">89,260</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,431,560</td>
<td align="right">1,142,640</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,431,880</td>
<td align="right">1,142,980</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">140,939,480</td>
<td align="right">113,318,620</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">45,560,100</td>
<td align="right">37,340,140</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">48,860</td>
<td align="right">40,080</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,884,020</td>
<td align="right">3,189,920</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">81,900</td>
<td align="right">67,520</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">55,400</td>
<td align="right">45,880</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">9,269,080</td>
<td align="right">7,855,800</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,517,160</td>
<td align="right">2,982,980</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,126,820</td>
<td align="right">10,479,400</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">10,200</td>
<td align="right">8,820</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">133,440</td>
<td align="right">119,740</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">35,200</td>
<td align="right">31,960</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">14,680</td>
<td align="right">15,920</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">88,760</td>
<td align="right">82,540</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">14,720</td>
<td align="right">13,800</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">22,095,320</td>
<td align="right">20,947,580</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">62,860</td>
<td align="right">65,900</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">78,740</td>
<td align="right">75,100</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">87,493,580</td>
<td align="right">84,266,220</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">239,960</td>
<td align="right">231,460</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">45,575,180</td>
<td align="right">45,127,520</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">238,000</td>
<td align="right">239,220</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">7,260</td>
<td align="right">7,240</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">3,229,480</td>
<td align="right">3,221,160</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,328,940</td>
<td align="right">1,328,080</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">51,100</td>
<td align="right">51,080</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">61,270,460</td>
<td align="right">61,270,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">4,370,180</td>
<td align="right">4,370,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">509,300</td>
<td align="right">509,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">236,980</td>
<td align="right">236,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">87,840</td>
<td align="right">87,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">87,840</td>
<td align="right">87,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">74,920</td>
<td align="right">74,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">49,340</td>
<td align="right">49,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">43,920</td>
<td align="right">43,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">40,660</td>
<td align="right">40,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">32,880</td>
<td align="right">32,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">26,020</td>
<td align="right">26,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">21,480</td>
<td align="right">21,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">15,640</td>
<td align="right">15,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">15,120</td>
<td align="right">15,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">13,020</td>
<td align="right">13,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">11,680</td>
<td align="right">11,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">10,680</td>
<td align="right">10,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">10,100</td>
<td align="right">10,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">8,900</td>
<td align="right">8,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">7,220</td>
<td align="right">7,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">6,980</td>
<td align="right">6,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">5,580</td>
<td align="right">5,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,700</td>
<td align="right">4,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,600</td>
<td align="right">4,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">4,540</td>
<td align="right">4,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,000</td>
<td align="right">4,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,560</td>
<td align="right">3,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">3,400</td>
<td align="right">3,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">2,820</td>
<td align="right">2,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,280</td>
<td align="right">2,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,000</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">1,200</td>
<td align="right">1,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">640</td>
<td align="right">640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
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
<td align="right">728,220</td>
<td align="right">1.3%</td>
<td align="right">118,480</td>
<td align="right">0.2%</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">54,214,480</td>
<td align="right">98.7%</td>
<td align="right">54,205,580</td>
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
<td align="right">1,940</td>
<td align="right">88.2%</td>
<td align="right">1,760</td>
<td align="right">87.1%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">260</td>
<td align="right">11.8%</td>
<td align="right">260</td>
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
<td align="left">add other</td>
<td align="right">900</td>
<td align="right">46.4%</td>
<td align="right">700</td>
<td align="right">39.8%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">380</td>
<td align="right">19.6%</td>
<td align="right">400</td>
<td align="right">22.7%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">280</td>
<td align="right">14.4%</td>
<td align="right">280</td>
<td align="right">15.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">240</td>
<td align="right">12.4%</td>
<td align="right">240</td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">120</td>
<td align="right">6.2%</td>
<td align="right">120</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20</td>
<td align="right">1.0%</td>
<td align="right">20</td>
<td align="right">1.1%</td>
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
<td align="right">7,450,000</td>
<td align="right">100.0%</td>
<td align="right">110,920</td>
<td align="right">100.0%</td>
<td align="right">-98.5%</td>
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
<td align="right">36,381,760</td>
<td align="right">9.4%</td>
<td align="right">1,116,820</td>
<td align="right">0.3%</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">349,446,800</td>
<td align="right">90.6%</td>
<td align="right">349,446,800</td>
<td align="right">99.7%</td>
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
<td align="right">10,060</td>
<td align="right">0.0%</td>
<td align="right">10,060</td>
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
<td align="right">10,760</td>
<td align="right">60.9%</td>
<td align="right">2,100</td>
<td align="right">23.3%</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,900</td>
<td align="right">39.1%</td>
<td align="right">6,900</td>
<td align="right">76.7%</td>
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
<td align="right">10,700</td>
<td align="right">99.4%</td>
<td align="right">2,040</td>
<td align="right">97.1%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">1.0%</td>
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
<td align="right">34,225,680</td>
<td align="right">8.1%</td>
<td align="right">34,975,780</td>
<td align="right">8.3%</td>
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
<td align="right">386,929,820</td>
<td align="right">91.9%</td>
<td align="right">387,329,060</td>
<td align="right">91.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,560</td>
<td align="right">0.0%</td>
<td align="right">7,560</td>
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
<td align="right">654,300</td>
<td align="right">100.0%</td>
<td align="right">668,440</td>
<td align="right">100.0%</td>
<td align="right">2.2%</td>
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
<td align="right">960</td>
<td align="right">960 / 0 !!</td>
<td align="right">960</td>
<td align="right">960 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">80</td>
<td align="right">80 / 0 !!</td>
<td align="right">80</td>
<td align="right">80 / 0 !!</td>
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
<td align="right">1,000</td>
<td align="right">50.0%</td>
<td align="right">1,000</td>
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
<td align="right">552,480</td>
<td align="right">0.3%</td>
<td align="right">36,140</td>
<td align="right">0.0%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">174,812,740</td>
<td align="right">99.7%</td>
<td align="right">174,812,740</td>
<td align="right">100.0%</td>
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
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">160</td>
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
<td align="right">460</td>
<td align="right">25.8%</td>
<td align="right">280</td>
<td align="right">17.5%</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,320</td>
<td align="right">74.2%</td>
<td align="right">1,320</td>
<td align="right">82.5%</td>
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
<td align="left">list</td>
<td align="right">340</td>
<td align="right">73.9%</td>
<td align="right">200</td>
<td align="right">71.4%</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">80</td>
<td align="right">17.4%</td>
<td align="right">80</td>
<td align="right">28.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">20</td>
<td align="right">4.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">1,884,400</td>
<td align="right">3.9%</td>
<td align="right">224,100</td>
<td align="right">0.5%</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">46,538,060</td>
<td align="right">96.1%</td>
<td align="right">46,538,060</td>
<td align="right">99.5%</td>
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
<td align="right">2,060</td>
<td align="right">90.4%</td>
<td align="right">1,540</td>
<td align="right">87.5%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">220</td>
<td align="right">9.6%</td>
<td align="right">220</td>
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
<td align="left">tuple</td>
<td align="right">960</td>
<td align="right">46.6%</td>
<td align="right">600</td>
<td align="right">39.0%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">740</td>
<td align="right">35.9%</td>
<td align="right">580</td>
<td align="right">37.7%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">360</td>
<td align="right">17.5%</td>
<td align="right">360</td>
<td align="right">23.4%</td>
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
<td align="right">400,300</td>
<td align="right">10.2%</td>
<td align="right">240,140</td>
<td align="right">7.5%</td>
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
<td align="right">3,514,220</td>
<td align="right">89.7%</td>
<td align="right">2,980,220</td>
<td align="right">92.5%</td>
<td align="right">-15.2%</td>
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
<td align="right">2,440</td>
<td align="right">83.0%</td>
<td align="right">2,260</td>
<td align="right">81.9%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">500</td>
<td align="right">17.0%</td>
<td align="right">500</td>
<td align="right">18.1%</td>
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
<td align="left">ascii string</td>
<td align="right">320</td>
<td align="right">13.1%</td>
<td align="right">140</td>
<td align="right">6.2%</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">900</td>
<td align="right">36.9%</td>
<td align="right">900</td>
<td align="right">39.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">560</td>
<td align="right">23.0%</td>
<td align="right">560</td>
<td align="right">24.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">160</td>
<td align="right">6.6%</td>
<td align="right">160</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">160</td>
<td align="right">6.6%</td>
<td align="right">160</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">160</td>
<td align="right">6.6%</td>
<td align="right">160</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">120</td>
<td align="right">4.9%</td>
<td align="right">120</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">60</td>
<td align="right">2.5%</td>
<td align="right">60</td>
<td align="right">2.7%</td>
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
<td align="right">14,030,220</td>
<td align="right">1.8%</td>
<td align="right">12,137,920</td>
<td align="right">1.6%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">224,660</td>
<td align="right">0.0%</td>
<td align="right">225,880</td>
<td align="right">0.0%</td>
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
<td align="right">745,914,460</td>
<td align="right">98.1%</td>
<td align="right">742,511,400</td>
<td align="right">98.4%</td>
<td align="right">-0.5%</td>
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
<td align="right">274,740</td>
<td align="right">99.1%</td>
<td align="right">239,060</td>
<td align="right">99.0%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,420</td>
<td align="right">0.9%</td>
<td align="right">2,420</td>
<td align="right">1.0%</td>
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
<td align="left">overridden</td>
<td align="right">620</td>
<td align="right">25.6%</td>
<td align="right">620</td>
<td align="right">25.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">600</td>
<td align="right">24.8%</td>
<td align="right">600</td>
<td align="right">24.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">460</td>
<td align="right">19.0%</td>
<td align="right">460</td>
<td align="right">19.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">320</td>
<td align="right">13.2%</td>
<td align="right">320</td>
<td align="right">13.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">300</td>
<td align="right">12.4%</td>
<td align="right">300</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">60</td>
<td align="right">2.5%</td>
<td align="right">60</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">20</td>
<td align="right">0.8%</td>
<td align="right">20</td>
<td align="right">0.8%</td>
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
<td align="right">159,964,940</td>
<td align="right">100.0%</td>
<td align="right">131,324,720</td>
<td align="right">100.0%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,280</td>
<td align="right">0.0%</td>
<td align="right">5,280</td>
<td align="right">0.0%</td>
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
<td align="right">26,560</td>
<td align="right">0.0%</td>
<td align="right">26,560</td>
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
<td align="right">5,800</td>
<td align="right">100.0%</td>
<td align="right">5,800</td>
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
<td align="right">80</td>
<td align="right">100.0%</td>
<td align="right">80</td>
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
<td align="right">11,064,320</td>
<td align="right">3.5%</td>
<td align="right">345,780</td>
<td align="right">0.1%</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">309,243,220</td>
<td align="right">96.5%</td>
<td align="right">309,430,940</td>
<td align="right">99.9%</td>
<td align="right">0.1%</td>
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
<td align="right">214,620</td>
<td align="right">99.9%</td>
<td align="right">12,420</td>
<td align="right">99.0%</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">120</td>
<td align="right">1.0%</td>
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
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">120</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">35,406,240</td>
<td align="right">49.8%</td>
<td align="right">2,103,320</td>
<td align="right">5.6%</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">35,700,820</td>
<td align="right">50.2%</td>
<td align="right">35,700,820</td>
<td align="right">94.4%</td>
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
<td align="right">29,380</td>
<td align="right">98.7%</td>
<td align="right">19,000</td>
<td align="right">97.9%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">400</td>
<td align="right">1.3%</td>
<td align="right">400</td>
<td align="right">2.1%</td>
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
<td align="left">py simple</td>
<td align="right">29,300</td>
<td align="right">99.7%</td>
<td align="right">18,920</td>
<td align="right">99.6%</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">737,400</td>
<td align="right">0.4%</td>
<td align="right">118,800</td>
<td align="right">0.1%</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">61,860</td>
<td align="right">0.0%</td>
<td align="right">84,520</td>
<td align="right">0.1%</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">166,704,660</td>
<td align="right">99.5%</td>
<td align="right">165,389,000</td>
<td align="right">99.9%</td>
<td align="right">-0.8%</td>
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
<td align="right">15,620</td>
<td align="right">76.2%</td>
<td align="right">3,980</td>
<td align="right">57.3%</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,880</td>
<td align="right">23.8%</td>
<td align="right">2,960</td>
<td align="right">42.7%</td>
<td align="right">-39.3%</td>
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
<td align="right">3,660</td>
<td align="right">75.0%</td>
<td align="right">1,740</td>
<td align="right">58.8%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">820</td>
<td align="right">16.8%</td>
<td align="right">820</td>
<td align="right">27.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">320</td>
<td align="right">6.6%</td>
<td align="right">320</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">80</td>
<td align="right">1.6%</td>
<td align="right">80</td>
<td align="right">2.7%</td>
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
<td align="right">49,441,460</td>
<td align="right">100.0%</td>
<td align="right">49,426,560</td>
<td align="right">100.0%</td>
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
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
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
<td align="right">320</td>
<td align="right">100.0%</td>
<td align="right">320</td>
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
<td align="right">86,324,380</td>
<td align="right">2.4%</td>
<td align="right">7,098,900</td>
<td align="right">0.6%</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,222,732,380</td>
<td align="right">62.6%</td>
<td align="right">591,602,060</td>
<td align="right">51.1%</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,179,244,540</td>
<td align="right">33.2%</td>
<td align="right">511,844,420</td>
<td align="right">44.2%</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">60,096,980</td>
<td align="right">1.7%</td>
<td align="right">47,618,360</td>
<td align="right">4.1%</td>
<td align="right">-20.8%</td>
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
<td align="right">7,450,000</td>
<td align="right">8.6%</td>
<td align="right">110,920</td>
<td align="right">1.6%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">36,381,760</td>
<td align="right">42.2%</td>
<td align="right">1,116,820</td>
<td align="right">15.9%</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">35,406,240</td>
<td align="right">41.1%</td>
<td align="right">2,103,320</td>
<td align="right">29.9%</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">552,480</td>
<td align="right">0.6%</td>
<td align="right">36,140</td>
<td align="right">0.5%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,884,400</td>
<td align="right">2.2%</td>
<td align="right">224,100</td>
<td align="right">3.2%</td>
<td align="right">-88.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">728,220</td>
<td align="right">0.8%</td>
<td align="right">118,480</td>
<td align="right">1.7%</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">61,860</td>
<td align="right">0.1%</td>
<td align="right">84,520</td>
<td align="right">1.2%</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,514,220</td>
<td align="right">4.1%</td>
<td align="right">2,980,220</td>
<td align="right">42.4%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">224,660</td>
<td align="right">0.3%</td>
<td align="right">225,880</td>
<td align="right">3.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">9,540</td>
<td align="right">0.0%</td>
<td align="right">9,540</td>
<td align="right">0.1%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">10,815,200</td>
<td align="right">18.0%</td>
<td align="right">289,180</td>
<td align="right">0.6%</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">270,660</td>
<td align="right">0.5%</td>
<td align="right">30,220</td>
<td align="right">0.1%</td>
<td align="right">-88.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">458,080</td>
<td align="right">0.8%</td>
<td align="right">79,920</td>
<td align="right">0.2%</td>
<td align="right">-82.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">249,120</td>
<td align="right">0.4%</td>
<td align="right">56,600</td>
<td align="right">0.1%</td>
<td align="right">-77.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,528,260</td>
<td align="right">2.5%</td>
<td align="right">356,760</td>
<td align="right">0.7%</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">7,573,700</td>
<td align="right">12.6%</td>
<td align="right">6,405,300</td>
<td align="right">13.5%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">26,648,580</td>
<td align="right">44.3%</td>
<td align="right">28,567,080</td>
<td align="right">60.0%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">12,224,880</td>
<td align="right">20.3%</td>
<td align="right">11,505,160</td>
<td align="right">24.2%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">276,640</td>
<td align="right">0.5%</td>
<td align="right">275,560</td>
<td align="right">0.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">15,640</td>
<td align="right">0.0%</td>
<td align="right">15,640</td>
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
<td align="right">61,280,160</td>
<td align="right">28.9%</td>
<td align="right">61,280,160</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">150,432,040</td>
<td align="right">71.1%</td>
<td align="right">150,432,040</td>
<td align="right">71.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">61,280,160</td>
<td align="right">28.9%</td>
<td align="right">61,280,160</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">61,279,680</td>
<td align="right">28.9%</td>
<td align="right">61,279,680</td>
<td align="right">28.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">520</td>
<td align="right">0.0%</td>
<td align="right">520</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">61,279,160</td>
<td align="right">28.9%</td>
<td align="right">61,279,160</td>
<td align="right">28.9%</td>
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
<td align="right">46,520,240</td>
<td align="right">22.0%</td>
<td align="right">46,520,240</td>
<td align="right">22.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">98,540</td>
<td align="right">0.0%</td>
<td align="right">98,540</td>
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
<td align="right">20,280</td>
<td align="right">0.0%</td>
<td align="right">20,280</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">211,723,400</td>
<td align="right">100.0%</td>
<td align="right">211,723,400</td>
<td align="right">100.0%</td>
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
<td align="right">3,940</td>
<td align="right">0.0%</td>
<td align="right">9,940</td>
<td align="right">0.0%</td>
<td align="right">152.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">39,001</td>
<td align="right"></td>
<td align="right">81,111</td>
<td align="right"></td>
<td align="right">108.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">785,164,080</td>
<td align="right">11.0%</td>
<td align="right">266,098,680</td>
<td align="right">3.8%</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">852,195,340</td>
<td align="right">10.5%</td>
<td align="right">309,263,480</td>
<td align="right">3.8%</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">164,444</td>
<td align="right"></td>
<td align="right">257,600</td>
<td align="right"></td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,807,498,680</td>
<td align="right">25.2%</td>
<td align="right">918,704,220</td>
<td align="right">13.1%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,215,064,580</td>
<td align="right">27.4%</td>
<td align="right">1,283,647,480</td>
<td align="right">15.7%</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">141,752</td>
<td align="right"></td>
<td align="right">192,131</td>
<td align="right"></td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">3,037,375,249</td>
<td align="right">37.6%</td>
<td align="right">4,104,825,349</td>
<td align="right">50.1%</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">3,131,364,381</td>
<td align="right">43.7%</td>
<td align="right">4,156,136,230</td>
<td align="right">59.1%</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,983,019,861</td>
<td align="right">24.5%</td>
<td align="right">2,487,963,083</td>
<td align="right">30.4%</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,439,267,247</td>
<td align="right">20.1%</td>
<td align="right">1,694,550,038</td>
<td align="right">24.1%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">55,290,848</td>
<td align="right"></td>
<td align="right">56,221,029</td>
<td align="right"></td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">118,640,259</td>
<td align="right"></td>
<td align="right">118,587,769</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">36,677,160</td>
<td align="right">8.7%</td>
<td align="right">36,690,680</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">240,167,200</td>
<td align="right">56.6%</td>
<td align="right">240,224,600</td>
<td align="right">56.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">273,141,981</td>
<td align="right"></td>
<td align="right">273,198,424</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">203,486,100</td>
<td align="right">48.0%</td>
<td align="right">203,523,980</td>
<td align="right">48.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">183,808,240</td>
<td align="right">43.4%</td>
<td align="right">183,810,140</td>
<td align="right">43.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">183,831,420</td>
<td align="right"></td>
<td align="right">183,833,320</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">48,028,940</td>
<td align="right"></td>
<td align="right">48,028,940</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">480</td>
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
<td align="right">8,920</td>
<td align="right">13,125,960</td>
<td align="right">310,746,560</td>
<td align="right">8,920</td>
<td align="right">13,131,880</td>
<td align="right">309,668,880</td>
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
<td align="right">17,880</td>
<td align="right">38.5%</td>
<td align="right">60,420</td>
<td align="right">74.8%</td>
<td align="right">237.9%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">3,280</td>
<td align="right">18.3%</td>
<td align="right">8,620</td>
<td align="right">14.3%</td>
<td align="right">162.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">20,280</td>
<td align="right">43.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">120</td>
<td align="right">0.3%</td>
<td align="right">220</td>
<td align="right">0.3%</td>
<td align="right">83.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">46,500</td>
<td align="right"></td>
<td align="right">80,820</td>
<td align="right"></td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">334,129,740</td>
<td align="right"></td>
<td align="right">513,508,560</td>
<td align="right"></td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">740</td>
<td align="right">1.6%</td>
<td align="right">1,100</td>
<td align="right">1.4%</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">9,471,700,340</td>
<td align="right">2,834.7%</td>
<td align="right">13,804,831,540</td>
<td align="right">2,688.3%</td>
<td align="right">45.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">28,620</td>
<td align="right">61.5%</td>
<td align="right">20,400</td>
<td align="right">25.2%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">700</td>
<td align="right">1.5%</td>
<td align="right">780</td>
<td align="right">1.0%</td>
<td align="right">11.4%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">17,300</td>
<td align="right">96.8%</td>
<td align="right">59,900</td>
<td align="right">99.1%</td>
<td align="right">246.2%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">17,880</td>
<td align="right"></td>
<td align="right">60,420</td>
<td align="right"></td>
<td align="right">237.9%</td>
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
<td align="right">320</td>
<td align="right">1.8%</td>
<td align="right">320</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
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
<td align="right">1,400</td>
<td align="right">7.8%</td>
<td align="right">2,380</td>
<td align="right">3.9%</td>
<td align="right">70.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,060</td>
<td align="right">5.9%</td>
<td align="right">20,480</td>
<td align="right">33.9%</td>
<td align="right">1,832.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">5,620</td>
<td align="right">31.4%</td>
<td align="right">13,740</td>
<td align="right">22.7%</td>
<td align="right">144.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">3,920</td>
<td align="right">21.9%</td>
<td align="right">7,040</td>
<td align="right">11.7%</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,360</td>
<td align="right">18.8%</td>
<td align="right">5,780</td>
<td align="right">9.6%</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,440</td>
<td align="right">13.6%</td>
<td align="right">9,340</td>
<td align="right">15.5%</td>
<td align="right">282.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">80</td>
<td align="right">0.4%</td>
<td align="right">1,640</td>
<td align="right">2.7%</td>
<td align="right">1,950.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">220</td>
<td align="right">1.2%</td>
<td align="right">180</td>
<td align="right">0.3%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,800</td>
<td align="right">10.1%</td>
<td align="right">3,660</td>
<td align="right">6.1%</td>
<td align="right">103.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,100</td>
<td align="right">6.2%</td>
<td align="right">23,460</td>
<td align="right">38.8%</td>
<td align="right">2,032.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,100</td>
<td align="right">39.7%</td>
<td align="right">13,420</td>
<td align="right">22.2%</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">2,640</td>
<td align="right">14.8%</td>
<td align="right">5,640</td>
<td align="right">9.3%</td>
<td align="right">113.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,740</td>
<td align="right">20.9%</td>
<td align="right">6,840</td>
<td align="right">11.3%</td>
<td align="right">82.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">700</td>
<td align="right">3.9%</td>
<td align="right">6,680</td>
<td align="right">11.1%</td>
<td align="right">854.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="left">_LOAD_GLOBAL</td>
<td align="right">2,760</td>
<td align="right">1,471,740</td>
<td align="right">53,223.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">25,920</td>
<td align="right">8,210,940</td>
<td align="right">31,578.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">45,820</td>
<td align="right">9,396,400</td>
<td align="right">20,407.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">889,260</td>
<td align="right">137,028,700</td>
<td align="right">15,309.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">311,060</td>
<td align="right">35,576,000</td>
<td align="right">11,337.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">91,960</td>
<td align="right">10,420,580</td>
<td align="right">11,231.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">324,840</td>
<td align="right">33,627,760</td>
<td align="right">10,252.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">143,340</td>
<td align="right">13,588,500</td>
<td align="right">9,379.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,812,280</td>
<td align="right">122,576,940</td>
<td align="right">6,663.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">38,400</td>
<td align="right">2,293,000</td>
<td align="right">5,871.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">38,400</td>
<td align="right">2,293,000</td>
<td align="right">5,871.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">26,640</td>
<td align="right">794,400</td>
<td align="right">2,882.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">24,280</td>
<td align="right">313,200</td>
<td align="right">1,190.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">24,280</td>
<td align="right">313,180</td>
<td align="right">1,189.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">88,440</td>
<td align="right">854,520</td>
<td align="right">866.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">145,940</td>
<td align="right">1,293,680</td>
<td align="right">786.4%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">1,196,120</td>
<td align="right">9,019,960</td>
<td align="right">654.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">1,196,120</td>
<td align="right">9,019,960</td>
<td align="right">654.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,136,480</td>
<td align="right">8,364,520</td>
<td align="right">636.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">13,020</td>
<td align="right">81,440</td>
<td align="right">525.5%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">15,320,720</td>
<td align="right">92,431,120</td>
<td align="right">503.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">600</td>
<td align="right">3,580</td>
<td align="right">496.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">1,809,300</td>
<td align="right">10,029,260</td>
<td align="right">454.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">1,809,300</td>
<td align="right">10,029,260</td>
<td align="right">454.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">9,050,580</td>
<td align="right">48,811,980</td>
<td align="right">439.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">391,400</td>
<td align="right">1,927,340</td>
<td align="right">392.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">600</td>
<td align="right">1,980</td>
<td align="right">230.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">38,814,880</td>
<td align="right">124,443,600</td>
<td align="right">220.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">10,537,880</td>
<td align="right">32,880,220</td>
<td align="right">212.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">10,537,880</td>
<td align="right">32,880,220</td>
<td align="right">212.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,537,880</td>
<td align="right">32,880,220</td>
<td align="right">212.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">6,256,080</td>
<td align="right">19,297,340</td>
<td align="right">208.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">8,538,420</td>
<td align="right">21,671,040</td>
<td align="right">153.8%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">28,030,540</td>
<td align="right">69,618,120</td>
<td align="right">148.4%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">28,033,540</td>
<td align="right">69,621,120</td>
<td align="right">148.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">535,560</td>
<td align="right">1,183,240</td>
<td align="right">120.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">28,958,400</td>
<td align="right">61,264,060</td>
<td align="right">111.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">293,633,800</td>
<td align="right">557,609,140</td>
<td align="right">89.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">27,141,900</td>
<td align="right">51,226,900</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">27,146,120</td>
<td align="right">51,231,820</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">32,255,540</td>
<td align="right">58,904,460</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">27,119,480</td>
<td align="right">49,507,880</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">52,733,040</td>
<td align="right">95,878,360</td>
<td align="right">81.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">116,854,720</td>
<td align="right">210,421,480</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">84,396,440</td>
<td align="right">140,073,820</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">9,960</td>
<td align="right">16,180</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,069,140</td>
<td align="right">1,687,780</td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">50,628,300</td>
<td align="right">79,473,360</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">995,918,080</td>
<td align="right">1,532,464,580</td>
<td align="right">53.9%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">334,129,740</td>
<td align="right">513,508,560</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">337,320,780</td>
<td align="right">516,690,240</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">36,522,560</td>
<td align="right">55,318,080</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">11,619,620</td>
<td align="right">17,444,660</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">742,155,340</td>
<td align="right">1,106,663,500</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">621,471,260</td>
<td align="right">926,492,220</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">515,967,320</td>
<td align="right">764,201,900</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">65,651,200</td>
<td align="right">93,313,760</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">258,168,440</td>
<td align="right">361,762,840</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">36,140</td>
<td align="right">50,520</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">28,042,320</td>
<td align="right">39,182,740</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">255,527,480</td>
<td align="right">355,508,660</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">189,075,460</td>
<td align="right">260,102,400</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">17,356,880</td>
<td align="right">23,402,080</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">187,152,460</td>
<td align="right">248,595,200</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">36,429,740</td>
<td align="right">48,389,520</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">47,420,660</td>
<td align="right">62,834,800</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">34,401,240</td>
<td align="right">45,310,360</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">85,003,940</td>
<td align="right">111,838,480</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">52,459,820</td>
<td align="right">68,596,520</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">14,275,900</td>
<td align="right">18,556,620</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">28,782,100</td>
<td align="right">37,261,900</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">302,672,660</td>
<td align="right">390,616,160</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">46,148,360</td>
<td align="right">59,547,060</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">273,890,560</td>
<td align="right">353,354,260</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">35,647,640</td>
<td align="right">45,985,560</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">16,617,620</td>
<td align="right">21,308,380</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,398,900</td>
<td align="right">5,602,540</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">28,091,820</td>
<td align="right">35,430,900</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">119,045,520</td>
<td align="right">149,575,380</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">28,034,740</td>
<td align="right">34,839,740</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">13,628,880</td>
<td align="right">16,890,440</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">102,024,800</td>
<td align="right">125,777,120</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">107,626,420</td>
<td align="right">131,060,700</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">15,060</td>
<td align="right">18,300</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">238,693,140</td>
<td align="right">288,054,880</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">132,196,360</td>
<td align="right">158,873,340</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">132,051,600</td>
<td align="right">157,792,040</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">3,520</td>
<td align="right">4,180</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">50,946,980</td>
<td align="right">60,223,560</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">23,654,360</td>
<td align="right">27,876,720</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">327,918,560</td>
<td align="right">385,329,080</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">2,532,000</td>
<td align="right">2,974,860</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">3,629,260</td>
<td align="right">4,221,100</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">4,645,220</td>
<td align="right">5,383,240</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">188,821,100</td>
<td align="right">218,523,340</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">238,310,300</td>
<td align="right">275,039,140</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">78,816,060</td>
<td align="right">90,842,420</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">55,161,700</td>
<td align="right">62,965,700</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">89,358,000</td>
<td align="right">101,287,600</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">89,358,000</td>
<td align="right">101,287,600</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">46,778,680</td>
<td align="right">52,846,860</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">16,867,280</td>
<td align="right">14,808,840</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">61,939,160</td>
<td align="right">69,467,500</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">13,075,960</td>
<td align="right">14,304,280</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">6,113,880</td>
<td align="right">6,647,880</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">98,800</td>
<td align="right">107,300</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">43,625,920</td>
<td align="right">47,161,740</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">18,990,240</td>
<td align="right">20,403,520</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">24,007,980</td>
<td align="right">25,668,280</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">14,400</td>
<td align="right">15,320</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">38,138,780</td>
<td align="right">40,517,980</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">165,320</td>
<td align="right">173,640</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">71,910,940</td>
<td align="right">75,410,760</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">15,139,240</td>
<td align="right">15,833,340</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">38,883,860</td>
<td align="right">40,565,360</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">11,209,340</td>
<td align="right">11,629,260</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">33,960</td>
<td align="right">34,500</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">30,131,840</td>
<td align="right">30,430,980</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">41,388,400</td>
<td align="right">41,632,960</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">39,992,600</td>
<td align="right">40,152,760</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">43,180,540</td>
<td align="right">43,340,700</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">43,189,040</td>
<td align="right">43,349,200</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">3,191,040</td>
<td align="right">3,181,680</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,664,480</td>
<td align="right">1,662,000</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">965,720</td>
<td align="right">964,480</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">46,406,420</td>
<td align="right">46,375,940</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">678,780</td>
<td align="right">679,120</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">20,812,440</td>
<td align="right">20,808,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">123,900</td>
<td align="right">123,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,065,040</td>
<td align="right">1,064,920</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">23,766,140</td>
<td align="right">23,768,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">11,537,480</td>
<td align="right">11,538,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">90,412,880</td>
<td align="right">90,408,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">49,299,460</td>
<td align="right">49,298,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">36,618,160</td>
<td align="right">36,618,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">23,451,040</td>
<td align="right">23,451,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,503,980</td>
<td align="right">5,503,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,585,200</td>
<td align="right">1,585,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">528,040</td>
<td align="right">528,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">274,220</td>
<td align="right">274,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">133,820</td>
<td align="right">133,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">45,000</td>
<td align="right">45,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">45,000</td>
<td align="right">45,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">35,160</td>
<td align="right">35,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">26,520</td>
<td align="right">26,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">20,480</td>
<td align="right">20,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">20,480</td>
<td align="right">20,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">14,580</td>
<td align="right">14,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">12,800</td>
<td align="right">12,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">5,740</td>
<td align="right">5,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">5,700</td>
<td align="right">5,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">5,520</td>
<td align="right">5,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">2,980</td>
<td align="right">2,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">2,980</td>
<td align="right">2,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">2,720</td>
<td align="right">2,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">2,480</td>
<td align="right">2,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">1,620</td>
<td align="right">1,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">600</td>
<td align="right">600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">40</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">929,540</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">929,540</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">516,340</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">14,900</td>
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
<td align="right">10,540</td>
<td align="right">19,980</td>
<td align="right">89.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">760</td>
<td align="right">760</td>
<td align="right">0.0%</td>
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
<td align="right">240</td>
<td align="right">240</td>
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
<td align="right">240</td>
<td align="right">240</td>
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
Stats gathered on: 2024-10-05
