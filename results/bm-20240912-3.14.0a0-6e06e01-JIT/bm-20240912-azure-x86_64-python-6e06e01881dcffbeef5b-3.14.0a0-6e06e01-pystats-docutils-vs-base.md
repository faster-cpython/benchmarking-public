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
<td align="right">278,008,160</td>
<td align="right">425,880</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">23,642,020</td>
<td align="right">592,780</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">5,304,620</td>
<td align="right">192,560</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">140,640</td>
<td align="right">8,160</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,173,360</td>
<td align="right">1,124,360</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">27,078,180</td>
<td align="right">1,796,380</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">5,032,600</td>
<td align="right">417,880</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">60,519,720</td>
<td align="right">5,604,780</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">72,554,740</td>
<td align="right">7,367,480</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">67,281,560</td>
<td align="right">8,682,460</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">22,751,740</td>
<td align="right">3,003,200</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">92,655,140</td>
<td align="right">12,313,280</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">221,322,420</td>
<td align="right">32,827,680</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">495,320</td>
<td align="right">83,100</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">24,048,900</td>
<td align="right">4,592,940</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,929,640</td>
<td align="right">458,480</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">50,216,120</td>
<td align="right">12,226,380</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">70,726,040</td>
<td align="right">17,831,620</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">181,074,600</td>
<td align="right">49,612,380</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">86,647,920</td>
<td align="right">24,471,640</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">64,590,900</td>
<td align="right">20,234,260</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">90,439,000</td>
<td align="right">28,581,500</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">6,862,040</td>
<td align="right">2,234,720</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">16,543,740</td>
<td align="right">5,473,540</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">38,500,180</td>
<td align="right">12,908,980</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,292,860</td>
<td align="right">435,820</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,636,540</td>
<td align="right">591,340</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">271,880</td>
<td align="right">98,240</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">45,427,820</td>
<td align="right">17,131,680</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">590,800,840</td>
<td align="right">229,101,360</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">40,454,260</td>
<td align="right">15,920,840</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">68,528,100</td>
<td align="right">28,049,080</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">9,000</td>
<td align="right">3,720</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">95,021,600</td>
<td align="right">39,712,620</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">25,665,840</td>
<td align="right">10,800,820</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">28,311,540</td>
<td align="right">12,153,820</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">18,749,240</td>
<td align="right">8,098,320</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">29,480,520</td>
<td align="right">13,065,360</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">29,849,340</td>
<td align="right">13,891,600</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">77,736,140</td>
<td align="right">36,782,700</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">396,269,600</td>
<td align="right">188,422,000</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">298,766,940</td>
<td align="right">144,755,380</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,146,860</td>
<td align="right">557,260</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">510,098,780</td>
<td align="right">248,416,620</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">338,134,500</td>
<td align="right">165,069,720</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">301,969,140</td>
<td align="right">148,688,380</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">17,837,460</td>
<td align="right">8,980,380</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">37,524,080</td>
<td align="right">19,116,860</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">5,455,000</td>
<td align="right">2,806,200</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">225,738,680</td>
<td align="right">118,826,420</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">7,860,060</td>
<td align="right">4,205,440</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">2,516,680</td>
<td align="right">1,361,900</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">175,276,580</td>
<td align="right">95,714,860</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">126,196,240</td>
<td align="right">69,524,080</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,143,660,120</td>
<td align="right">1,185,383,560</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">81,766,920</td>
<td align="right">45,233,880</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">261,072,620</td>
<td align="right">148,948,440</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">20,275,440</td>
<td align="right">11,569,620</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">196,992,820</td>
<td align="right">115,526,780</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">69,934,320</td>
<td align="right">41,304,460</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">384,832,000</td>
<td align="right">231,867,460</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,335,300</td>
<td align="right">1,409,420</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">125,667,140</td>
<td align="right">76,257,480</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,111,480</td>
<td align="right">675,100</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">3,241,740</td>
<td align="right">1,971,700</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">28,824,020</td>
<td align="right">17,630,020</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">424,278,160</td>
<td align="right">261,943,700</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">39,732,080</td>
<td align="right">24,803,600</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">9,455,580</td>
<td align="right">5,995,360</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,274,980</td>
<td align="right">809,560</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">32,161,120</td>
<td align="right">20,426,760</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">146,337,760</td>
<td align="right">93,069,060</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">164,141,480</td>
<td align="right">104,640,220</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">78,932,400</td>
<td align="right">51,160,200</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">30,869,080</td>
<td align="right">20,054,080</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">3,321,840</td>
<td align="right">2,168,900</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">22,974,660</td>
<td align="right">15,158,240</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">1,063,800</td>
<td align="right">705,560</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">2,060</td>
<td align="right">1,380</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,465,680</td>
<td align="right">13,729,520</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">1,960</td>
<td align="right">1,380</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">55,715,040</td>
<td align="right">39,263,780</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">29,549,980</td>
<td align="right">20,885,660</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">11,176,080</td>
<td align="right">8,019,140</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">7,260,660</td>
<td align="right">5,236,860</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">106,740</td>
<td align="right">77,900</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,906,720</td>
<td align="right">8,153,940</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">15,900</td>
<td align="right">11,980</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">10,340</td>
<td align="right">7,820</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">7,409,000</td>
<td align="right">5,678,260</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">15,284,680</td>
<td align="right">11,753,920</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">46,800</td>
<td align="right">36,440</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,490,500</td>
<td align="right">1,175,920</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,420</td>
<td align="right">20,200</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,885,440</td>
<td align="right">3,091,880</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">4,302,340</td>
<td align="right">3,491,660</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">44,920</td>
<td align="right">36,600</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">603,420</td>
<td align="right">510,320</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">13,634,680</td>
<td align="right">11,555,000</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">4,621,240</td>
<td align="right">4,056,960</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,525,580</td>
<td align="right">1,701,140</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">25,863,780</td>
<td align="right">22,891,640</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">55,599,980</td>
<td align="right">49,232,620</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">30,832,260</td>
<td align="right">27,469,280</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">5,603,840</td>
<td align="right">5,014,080</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">310,860</td>
<td align="right">278,680</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">55,377,460</td>
<td align="right">49,705,600</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">284,496,280</td>
<td align="right">255,975,920</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">17,260</td>
<td align="right">15,660</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">40,284,500</td>
<td align="right">37,289,460</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">40,282,060</td>
<td align="right">37,287,740</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">197,062,220</td>
<td align="right">182,707,320</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">9,620</td>
<td align="right">9,040</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">125,189,700</td>
<td align="right">117,762,680</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">20,138,080</td>
<td align="right">18,995,060</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">3,802,660</td>
<td align="right">3,615,380</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">22,153,480</td>
<td align="right">21,386,820</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">11,798,560</td>
<td align="right">11,410,140</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">217,404,620</td>
<td align="right">210,984,120</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">99,460</td>
<td align="right">96,860</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">93,880</td>
<td align="right">91,680</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,838,900</td>
<td align="right">12,559,780</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20,340</td>
<td align="right">20,020</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">485,040</td>
<td align="right">479,560</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">51,676,200</td>
<td align="right">51,215,940</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">3,643,620</td>
<td align="right">3,626,820</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">3,648,360</td>
<td align="right">3,631,560</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">9,532,040</td>
<td align="right">9,509,520</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">316,960</td>
<td align="right">316,640</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">49,489,200</td>
<td align="right">49,483,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">49,182,620</td>
<td align="right">49,182,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">15,519,420</td>
<td align="right">15,519,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">10,150,520</td>
<td align="right">10,150,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">8,191,960</td>
<td align="right">8,191,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">8,191,960</td>
<td align="right">8,191,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">7,717,040</td>
<td align="right">7,717,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,607,040</td>
<td align="right">6,607,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,885,520</td>
<td align="right">1,885,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,567,560</td>
<td align="right">1,567,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">237,500</td>
<td align="right">237,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">217,520</td>
<td align="right">217,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">201,000</td>
<td align="right">201,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">130,660</td>
<td align="right">130,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">109,540</td>
<td align="right">109,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">94,860</td>
<td align="right">94,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">62,360</td>
<td align="right">62,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">36,640</td>
<td align="right">36,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">32,180</td>
<td align="right">32,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">13,800</td>
<td align="right">13,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">7,340</td>
<td align="right">7,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">6,900</td>
<td align="right">6,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">6,100</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">4,480</td>
<td align="right">4,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">4,300</td>
<td align="right">4,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">3,900</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">3,900</td>
<td align="right">3,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,960</td>
<td align="right">1,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,400</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,040</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">1,020</td>
<td align="right">1,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">287,936,640</td>
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
<td align="right">28,268,800</td>
<td align="right">30.2%</td>
<td align="right">12,115,900</td>
<td align="right">15.7%</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">65,230,660</td>
<td align="right">69.7%</td>
<td align="right">65,230,660</td>
<td align="right">84.3%</td>
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
<td align="left">Failure</td>
<td align="right">35,760</td>
<td align="right">83.7%</td>
<td align="right">30,940</td>
<td align="right">81.6%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,980</td>
<td align="right">16.3%</td>
<td align="right">6,980</td>
<td align="right">18.4%</td>
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
<td align="left">floor divide</td>
<td align="right">360</td>
<td align="right">1.0%</td>
<td align="right">200</td>
<td align="right">0.6%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">11,560</td>
<td align="right">32.3%</td>
<td align="right">7,360</td>
<td align="right">23.8%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,260</td>
<td align="right">3.5%</td>
<td align="right">1,180</td>
<td align="right">3.8%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,600</td>
<td align="right">4.5%</td>
<td align="right">1,500</td>
<td align="right">4.8%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">10,880</td>
<td align="right">30.4%</td>
<td align="right">10,700</td>
<td align="right">34.6%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,300</td>
<td align="right">26.0%</td>
<td align="right">9,200</td>
<td align="right">29.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">660</td>
<td align="right">1.8%</td>
<td align="right">660</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">28,824,020</td>
<td align="right">100.0%</td>
<td align="right">17,630,020</td>
<td align="right">100.0%</td>
<td align="right">-38.8%</td>
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
<td align="right">1,612,280</td>
<td align="right">1.2%</td>
<td align="right">564,620</td>
<td align="right">0.4%</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,074,080</td>
<td align="right">2.3%</td>
<td align="right">3,046,560</td>
<td align="right">2.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">126,118,220</td>
<td align="right">96.4%</td>
<td align="right">126,122,040</td>
<td align="right">97.2%</td>
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
<td align="right">12,960</td>
<td align="right">15.8%</td>
<td align="right">15,420</td>
<td align="right">18.4%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">69,020</td>
<td align="right">84.2%</td>
<td align="right">68,500</td>
<td align="right">81.6%</td>
<td align="right">-0.8%</td>
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
<td align="right">60</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">11,580</td>
<td align="right">89.4%</td>
<td align="right">14,180</td>
<td align="right">92.0%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,280</td>
<td align="right">9.9%</td>
<td align="right">1,160</td>
<td align="right">7.5%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">23,796,020</td>
<td align="right">3.1%</td>
<td align="right">19,190,920</td>
<td align="right">2.5%</td>
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
<td align="right">740,002,600</td>
<td align="right">96.9%</td>
<td align="right">745,587,600</td>
<td align="right">97.5%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">71,480</td>
<td align="right">0.0%</td>
<td align="right">71,480</td>
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
<td align="right">510,440</td>
<td align="right">100.0%</td>
<td align="right">423,560</td>
<td align="right">100.0%</td>
<td align="right">-17.0%</td>
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
<td align="left">init not simple</td>
<td align="right">1,380</td>
<td align="right">1,380 / 0 !!</td>
<td align="right">1,380</td>
<td align="right">1,380 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">500</td>
<td align="right">500 / 0 !!</td>
<td align="right">500</td>
<td align="right">500 / 0 !!</td>
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
<td align="right">3,600</td>
<td align="right">52.2%</td>
<td align="right">3,600</td>
<td align="right">52.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">342,040</td>
<td align="right">0.7%</td>
<td align="right">140,640</td>
<td align="right">0.3%</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,309,540</td>
<td align="right">4.6%</td>
<td align="right">1,393,460</td>
<td align="right">2.8%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,346,820</td>
<td align="right">94.6%</td>
<td align="right">47,360,220</td>
<td align="right">96.8%</td>
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
<td align="right">20,140</td>
<td align="right">62.6%</td>
<td align="right">10,400</td>
<td align="right">55.9%</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,040</td>
<td align="right">37.4%</td>
<td align="right">8,200</td>
<td align="right">44.1%</td>
<td align="right">-31.9%</td>
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
<td align="right">17,780</td>
<td align="right">88.3%</td>
<td align="right">8,060</td>
<td align="right">77.5%</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">340</td>
<td align="right">1.7%</td>
<td align="right">320</td>
<td align="right">3.1%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">720</td>
<td align="right">3.6%</td>
<td align="right">720</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">660</td>
<td align="right">3.3%</td>
<td align="right">660</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">380</td>
<td align="right">1.9%</td>
<td align="right">380</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">200</td>
<td align="right">1.0%</td>
<td align="right">200</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">16,524,240</td>
<td align="right">18.5%</td>
<td align="right">5,457,620</td>
<td align="right">7.0%</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">72,826,620</td>
<td align="right">81.5%</td>
<td align="right">72,826,620</td>
<td align="right">93.0%</td>
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
<td align="right">17,760</td>
<td align="right">91.1%</td>
<td align="right">14,180</td>
<td align="right">89.1%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,740</td>
<td align="right">8.9%</td>
<td align="right">1,740</td>
<td align="right">10.9%</td>
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
<td align="right">4,560</td>
<td align="right">25.7%</td>
<td align="right">3,160</td>
<td align="right">22.3%</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">3,540</td>
<td align="right">19.9%</td>
<td align="right">2,520</td>
<td align="right">17.8%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">6,740</td>
<td align="right">38.0%</td>
<td align="right">5,580</td>
<td align="right">39.4%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,920</td>
<td align="right">16.4%</td>
<td align="right">2,920</td>
<td align="right">20.6%</td>
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
<td align="right">60,491,780</td>
<td align="right">13.9%</td>
<td align="right">5,591,960</td>
<td align="right">5.2%</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">50,379,700</td>
<td align="right">11.6%</td>
<td align="right">6,351,160</td>
<td align="right">5.9%</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">324,230,440</td>
<td align="right">74.5%</td>
<td align="right">94,807,660</td>
<td align="right">88.8%</td>
<td align="right">-70.8%</td>
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
<td align="right">955,040</td>
<td align="right">97.6%</td>
<td align="right">124,360</td>
<td align="right">93.8%</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">23,380</td>
<td align="right">2.4%</td>
<td align="right">8,240</td>
<td align="right">6.2%</td>
<td align="right">-64.8%</td>
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
<td align="left">dict values</td>
<td align="right">3,780</td>
<td align="right">16.2%</td>
<td align="right">640</td>
<td align="right">7.8%</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,700</td>
<td align="right">11.5%</td>
<td align="right">520</td>
<td align="right">6.3%</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,220</td>
<td align="right">5.2%</td>
<td align="right">260</td>
<td align="right">3.2%</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">7,020</td>
<td align="right">30.0%</td>
<td align="right">1,520</td>
<td align="right">18.4%</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">3,760</td>
<td align="right">16.1%</td>
<td align="right">1,800</td>
<td align="right">21.8%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">320</td>
<td align="right">1.4%</td>
<td align="right">180</td>
<td align="right">2.2%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">220</td>
<td align="right">0.9%</td>
<td align="right">140</td>
<td align="right">1.7%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">2,800</td>
<td align="right">12.0%</td>
<td align="right">1,860</td>
<td align="right">22.6%</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">180</td>
<td align="right">0.8%</td>
<td align="right">120</td>
<td align="right">1.5%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,040</td>
<td align="right">4.4%</td>
<td align="right">860</td>
<td align="right">10.4%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">200</td>
<td align="right">0.9%</td>
<td align="right">200</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">0.5%</td>
<td align="right">120</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">442,736,720</td>
<td align="right">30.1%</td>
<td align="right">177,880,000</td>
<td align="right">15.8%</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">145,343,600</td>
<td align="right">9.9%</td>
<td align="right">92,148,560</td>
<td align="right">8.2%</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">881,080,000</td>
<td align="right">59.9%</td>
<td align="right">853,981,320</td>
<td align="right">75.9%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
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
<td align="right">9,300,460</td>
<td align="right">99.6%</td>
<td align="right">4,242,680</td>
<td align="right">99.4%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40,580</td>
<td align="right">0.4%</td>
<td align="right">27,400</td>
<td align="right">0.6%</td>
<td align="right">-32.5%</td>
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
<td align="left">metaclass attribute</td>
<td align="right">16,820</td>
<td align="right">41.4%</td>
<td align="right">6,160</td>
<td align="right">22.5%</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2,520</td>
<td align="right">6.2%</td>
<td align="right">2,160</td>
<td align="right">7.9%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">11,920</td>
<td align="right">29.4%</td>
<td align="right">10,400</td>
<td align="right">38.0%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">560</td>
<td align="right">1.4%</td>
<td align="right">500</td>
<td align="right">1.8%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,020</td>
<td align="right">2.5%</td>
<td align="right">940</td>
<td align="right">3.4%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,360</td>
<td align="right">3.4%</td>
<td align="right">1,300</td>
<td align="right">4.7%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">560</td>
<td align="right">1.4%</td>
<td align="right">540</td>
<td align="right">2.0%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,160</td>
<td align="right">10.3%</td>
<td align="right">4,160</td>
<td align="right">15.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">1.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">260</td>
<td align="right">0.6%</td>
<td align="right">260</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">120</td>
<td align="right">0.3%</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
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
<td align="right">427,607,580</td>
<td align="right">100.0%</td>
<td align="right">224,917,160</td>
<td align="right">100.0%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">31,560</td>
<td align="right">0.0%</td>
<td align="right">31,560</td>
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
<td align="right">1,100</td>
<td align="right">0.0%</td>
<td align="right">1,100</td>
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
<td align="right">28,700</td>
<td align="right">0.0%</td>
<td align="right">28,700</td>
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
<td align="right">31,380</td>
<td align="right">100.0%</td>
<td align="right">31,380</td>
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
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
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
<td align="right">109,980</td>
<td align="right">99.8%</td>
<td align="right">109,980</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">180</td>
<td align="right">1.8%</td>
<td align="right">180</td>
<td align="right">1.8%</td>
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
<td align="right">9,620</td>
<td align="right">97.4%</td>
<td align="right">9,620</td>
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
<td align="left">Success</td>
<td align="right">60</td>
<td align="right">75.0%</td>
<td align="right">60</td>
<td align="right">75.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">20</td>
<td align="right">25.0%</td>
<td align="right">20</td>
<td align="right">25.0%</td>
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
<td align="right">20</td>
<td align="right">100.0%</td>
<td align="right">20</td>
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
<td align="right">29,505,260</td>
<td align="right">17.9%</td>
<td align="right">20,843,280</td>
<td align="right">13.5%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">71,863,580</td>
<td align="right">43.6%</td>
<td align="right">69,256,760</td>
<td align="right">44.7%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">63,486,980</td>
<td align="right">38.5%</td>
<td align="right">64,811,360</td>
<td align="right">41.8%</td>
<td align="right">2.1%</td>
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
<td align="right">34,780</td>
<td align="right">2.5%</td>
<td align="right">32,440</td>
<td align="right">2.4%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,365,200</td>
<td align="right">97.5%</td>
<td align="right">1,316,000</td>
<td align="right">97.6%</td>
<td align="right">-3.6%</td>
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
<td align="left">class attr simple</td>
<td align="right">24,500</td>
<td align="right">70.4%</td>
<td align="right">22,180</td>
<td align="right">68.4%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">2,500</td>
<td align="right">7.2%</td>
<td align="right">2,480</td>
<td align="right">7.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,420</td>
<td align="right">18.5%</td>
<td align="right">6,420</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">460</td>
<td align="right">1.3%</td>
<td align="right">460</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">380</td>
<td align="right">1.1%</td>
<td align="right">380</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">360</td>
<td align="right">1.0%</td>
<td align="right">360</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">160</td>
<td align="right">0.5%</td>
<td align="right">160</td>
<td align="right">0.5%</td>
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
<td align="right">5,304,620</td>
<td align="right">100.0%</td>
<td align="right">192,560</td>
<td align="right">100.0%</td>
<td align="right">-96.4%</td>
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
<td align="right">1,479,140</td>
<td align="right">2.5%</td>
<td align="right">1,164,960</td>
<td align="right">2.0%</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">56,859,000</td>
<td align="right">97.4%</td>
<td align="right">56,859,000</td>
<td align="right">98.0%</td>
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
<td align="right">2,900</td>
<td align="right">0.0%</td>
<td align="right">2,900</td>
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
<td align="right">9,140</td>
<td align="right">80.2%</td>
<td align="right">8,740</td>
<td align="right">79.5%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,260</td>
<td align="right">19.8%</td>
<td align="right">2,260</td>
<td align="right">20.5%</td>
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
<td align="left">bytearray int</td>
<td align="right">760</td>
<td align="right">8.3%</td>
<td align="right">420</td>
<td align="right">4.8%</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">780</td>
<td align="right">8.5%</td>
<td align="right">720</td>
<td align="right">8.2%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">7,380</td>
<td align="right">80.7%</td>
<td align="right">7,380</td>
<td align="right">84.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">2.4%</td>
<td align="right">220</td>
<td align="right">2.5%</td>
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
<td align="right">15,133,780</td>
<td align="right">4.0%</td>
<td align="right">5,085,560</td>
<td align="right">1.4%</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,212,460</td>
<td align="right">1.4%</td>
<td align="right">2,693,540</td>
<td align="right">0.8%</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">359,864,420</td>
<td align="right">94.6%</td>
<td align="right">349,920,760</td>
<td align="right">97.8%</td>
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
<td align="left">Success</td>
<td align="right">300,960</td>
<td align="right">57.1%</td>
<td align="right">111,420</td>
<td align="right">53.6%</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">226,180</td>
<td align="right">42.9%</td>
<td align="right">96,400</td>
<td align="right">46.4%</td>
<td align="right">-57.4%</td>
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
<td align="left">number</td>
<td align="right">160,140</td>
<td align="right">70.8%</td>
<td align="right">32,540</td>
<td align="right">33.8%</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,600</td>
<td align="right">1.1%</td>
<td align="right">2,020</td>
<td align="right">2.1%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">6,660</td>
<td align="right">2.9%</td>
<td align="right">6,420</td>
<td align="right">6.7%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">640</td>
<td align="right">0.3%</td>
<td align="right">620</td>
<td align="right">0.6%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">56,120</td>
<td align="right">24.8%</td>
<td align="right">54,780</td>
<td align="right">56.8%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,240</td>
<td align="right">0.0%</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,639,560</td>
<td align="right">100.0%</td>
<td align="right">64,640,680</td>
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
<td align="right">3,680</td>
<td align="right">0.0%</td>
<td align="right">3,680</td>
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
<td align="right">3,740</td>
<td align="right">100.0%</td>
<td align="right">3,700</td>
<td align="right">100.0%</td>
<td align="right">-1.1%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">607,370,420</td>
<td align="right">5.6%</td>
<td align="right">280,994,740</td>
<td align="right">4.6%</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">326,516,420</td>
<td align="right">3.0%</td>
<td align="right">161,200,020</td>
<td align="right">2.6%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">3,762,659,400</td>
<td align="right">34.6%</td>
<td align="right">1,918,343,460</td>
<td align="right">31.5%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">6,169,626,640</td>
<td align="right">56.8%</td>
<td align="right">3,733,215,440</td>
<td align="right">61.3%</td>
<td align="right">-39.5%</td>
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
<td align="right">60,491,780</td>
<td align="right">18.6%</td>
<td align="right">5,591,960</td>
<td align="right">3.5%</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">16,524,240</td>
<td align="right">5.1%</td>
<td align="right">5,457,620</td>
<td align="right">3.4%</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,612,280</td>
<td align="right">0.5%</td>
<td align="right">564,620</td>
<td align="right">0.4%</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">28,268,800</td>
<td align="right">8.7%</td>
<td align="right">12,115,900</td>
<td align="right">7.6%</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">5,212,460</td>
<td align="right">1.6%</td>
<td align="right">2,693,540</td>
<td align="right">1.7%</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,309,540</td>
<td align="right">0.7%</td>
<td align="right">1,393,460</td>
<td align="right">0.9%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">28,824,020</td>
<td align="right">8.9%</td>
<td align="right">17,630,020</td>
<td align="right">11.0%</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">145,343,600</td>
<td align="right">44.7%</td>
<td align="right">92,148,560</td>
<td align="right">57.6%</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">29,505,260</td>
<td align="right">9.1%</td>
<td align="right">20,843,280</td>
<td align="right">13.0%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">5,304,620</td>
<td align="right">1.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1,164,960</td>
<td align="right">0.7%</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">25,187,040</td>
<td align="right">4.1%</td>
<td align="right">3,174,860</td>
<td align="right">1.1%</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">25,192,660</td>
<td align="right">4.1%</td>
<td align="right">3,176,300</td>
<td align="right">1.1%</td>
<td align="right">-87.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">47,092,860</td>
<td align="right">7.8%</td>
<td align="right">11,869,840</td>
<td align="right">4.2%</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">134,209,720</td>
<td align="right">22.1%</td>
<td align="right">50,472,640</td>
<td align="right">18.0%</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">177,294,400</td>
<td align="right">29.2%</td>
<td align="right">73,896,880</td>
<td align="right">26.3%</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">69,060,240</td>
<td align="right">11.4%</td>
<td align="right">30,005,740</td>
<td align="right">10.7%</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,933,600</td>
<td align="right">2.1%</td>
<td align="right">9,706,420</td>
<td align="right">3.5%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">71,859,340</td>
<td align="right">11.8%</td>
<td align="right">69,252,520</td>
<td align="right">24.6%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">10,094,740</td>
<td align="right">1.7%</td>
<td align="right">9,804,580</td>
<td align="right">3.5%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">8,150,220</td>
<td align="right">1.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">4,856,240</td>
<td align="right">1.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">11,253,680</td>
<td align="right">2.4%</td>
<td align="right">10,968,980</td>
<td align="right">2.3%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">52,649,220</td>
<td align="right">11.1%</td>
<td align="right">52,188,960</td>
<td align="right">11.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">52,661,120</td>
<td align="right">11.1%</td>
<td align="right">52,200,860</td>
<td align="right">11.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">53,079,040</td>
<td align="right">11.2%</td>
<td align="right">52,618,780</td>
<td align="right">11.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">53,079,040</td>
<td align="right">11.2%</td>
<td align="right">52,618,780</td>
<td align="right">11.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">420,720,500</td>
<td align="right">88.8%</td>
<td align="right">421,180,760</td>
<td align="right">88.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">419,297,540</td>
<td align="right">88.5%</td>
<td align="right">419,473,100</td>
<td align="right">88.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">417,920</td>
<td align="right">0.1%</td>
<td align="right">417,920</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">5,800</td>
<td align="right">0.0%</td>
<td align="right">5,800</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
<td align="right">6,100</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">18,275,060</td>
<td align="right">3.9%</td>
<td align="right">18,275,060</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">2,438,740</td>
<td align="right">0.5%</td>
<td align="right">2,438,740</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">12,832,760</td>
<td align="right">2.7%</td>
<td align="right">12,832,760</td>
<td align="right">2.7%</td>
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
<td align="right">2,324,306,569</td>
<td align="right">30.0%</td>
<td align="right">5,051,671,210</td>
<td align="right">55.2%</td>
<td align="right">117.3%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">2,661,291,964</td>
<td align="right">38.3%</td>
<td align="right">5,491,666,478</td>
<td align="right">65.8%</td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">4,498,425</td>
<td align="right"></td>
<td align="right">2,641,830</td>
<td align="right"></td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">4,281,256,760</td>
<td align="right">61.7%</td>
<td align="right">2,860,459,180</td>
<td align="right">34.2%</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">5,414,276,920</td>
<td align="right">70.0%</td>
<td align="right">4,096,254,040</td>
<td align="right">44.8%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">44,646,869</td>
<td align="right"></td>
<td align="right">48,909,273</td>
<td align="right"></td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">48,334,531</td>
<td align="right"></td>
<td align="right">50,741,159</td>
<td align="right"></td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">263,596,555</td>
<td align="right"></td>
<td align="right">254,828,390</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">689,900</td>
<td align="right">0.1%</td>
<td align="right">704,640</td>
<td align="right">0.1%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">627,886,151</td>
<td align="right"></td>
<td align="right">628,671,867</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">334,052,200</td>
<td align="right">30.4%</td>
<td align="right">333,755,660</td>
<td align="right">30.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">464,080</td>
<td align="right">0.0%</td>
<td align="right">464,480</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">334,068,300</td>
<td align="right"></td>
<td align="right">333,782,620</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">765,439,560</td>
<td align="right">69.6%</td>
<td align="right">765,582,520</td>
<td align="right">69.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">764,285,580</td>
<td align="right">69.5%</td>
<td align="right">764,413,400</td>
<td align="right">69.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">806,535,676</td>
<td align="right"></td>
<td align="right">806,629,560</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">14,081,720</td>
<td align="right"></td>
<td align="right">14,081,720</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">35,400</td>
<td align="right">0.3%</td>
<td align="right">35,400</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">158,720</td>
<td align="right">1.1%</td>
<td align="right">158,720</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">3,920</td>
<td align="right">0.0%</td>
<td align="right">3,920</td>
<td align="right">0.0%</td>
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
<td align="right">34,760</td>
<td align="right">93,584,920</td>
<td align="right">1,883,390,620</td>
<td align="right">34,840</td>
<td align="right">93,574,180</td>
<td align="right">1,880,285,240</td>
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
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
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
<td align="right">20</td>
<td align="right">20 / 0 !!</td>
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
