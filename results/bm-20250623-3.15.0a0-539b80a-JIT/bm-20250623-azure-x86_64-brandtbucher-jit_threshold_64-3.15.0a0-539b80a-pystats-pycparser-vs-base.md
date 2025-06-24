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
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,848,820</td>
<td align="right">3,875,360</td>
<td align="right">109.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,272,100</td>
<td align="right">17,220</td>
<td align="right">-99.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,517,080</td>
<td align="right">49,680</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">5,183,520</td>
<td align="right">67,480</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">764,000</td>
<td align="right">63,700</td>
<td align="right">-91.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,757,060</td>
<td align="right">3,210,000</td>
<td align="right">82.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">88,680</td>
<td align="right">20,900</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,320,880</td>
<td align="right">320,460</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">36,213,220</td>
<td align="right">11,201,040</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,686,820</td>
<td align="right">2,284,060</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">26,174,520</td>
<td align="right">10,736,880</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">26,601,120</td>
<td align="right">11,160,700</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">84,420</td>
<td align="right">36,240</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,195,920</td>
<td align="right">545,680</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">2,640,800</td>
<td align="right">4,059,480</td>
<td align="right">53.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">168,989,760</td>
<td align="right">80,715,200</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">30,116,640</td>
<td align="right">14,510,360</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">30,391,800</td>
<td align="right">14,903,340</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">33,536,440</td>
<td align="right">17,582,640</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">46,065,780</td>
<td align="right">24,879,520</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">105,292,140</td>
<td align="right">58,838,820</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">252,385,980</td>
<td align="right">157,343,760</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">49,579,380</td>
<td align="right">32,573,740</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">19,295,760</td>
<td align="right">12,679,820</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">10,354,760</td>
<td align="right">7,222,120</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">52,349,040</td>
<td align="right">36,911,400</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">52,349,040</td>
<td align="right">36,911,400</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">37,254,420</td>
<td align="right">26,490,740</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,102,420</td>
<td align="right">785,780</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">1,415,449,600</td>
<td align="right">1,044,258,760</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,609,400</td>
<td align="right">1,949,140</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">13,860</td>
<td align="right">10,660</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">13,860</td>
<td align="right">10,660</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">84,044,960</td>
<td align="right">65,212,400</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">247,075,300</td>
<td align="right">193,428,080</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">22,840,400</td>
<td align="right">18,026,720</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">229,929,080</td>
<td align="right">181,748,060</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">3,619,400</td>
<td align="right">2,864,060</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,328,180</td>
<td align="right">5,043,940</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">13,860</td>
<td align="right">11,080</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">108,578,620</td>
<td align="right">88,072,820</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">252,698,040</td>
<td align="right">205,296,560</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">177,055,540</td>
<td align="right">144,474,720</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">90,282,500</td>
<td align="right">74,003,040</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">216,960</td>
<td align="right">179,160</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,600</td>
<td align="right">25,940</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">39,706,940</td>
<td align="right">45,531,160</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">6,821,100</td>
<td align="right">5,959,180</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,774,600</td>
<td align="right">9,655,360</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">37,570,240</td>
<td align="right">33,696,580</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">7,302,700</td>
<td align="right">6,571,180</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">32,872,520</td>
<td align="right">29,768,560</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">100,407,320</td>
<td align="right">92,004,200</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">30,136,080</td>
<td align="right">28,076,060</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">379,680</td>
<td align="right">354,100</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">10,952,100</td>
<td align="right">10,301,860</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,880,240</td>
<td align="right">6,481,040</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">20,526,900</td>
<td align="right">19,626,740</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,793,400</td>
<td align="right">2,692,200</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">52,433,280</td>
<td align="right">50,536,260</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">12,358,920</td>
<td align="right">11,935,700</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,523,240</td>
<td align="right">2,449,600</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">669,540</td>
<td align="right">650,820</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">7,927,720</td>
<td align="right">7,718,340</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">15,331,040</td>
<td align="right">14,958,640</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">6,266,820</td>
<td align="right">6,133,980</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">73,938,300</td>
<td align="right">72,656,180</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">23,087,780</td>
<td align="right">22,715,260</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">180,960</td>
<td align="right">178,060</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,138,460</td>
<td align="right">4,075,280</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">46,971,020</td>
<td align="right">46,264,220</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">38,815,440</td>
<td align="right">38,242,540</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">107,406,800</td>
<td align="right">106,007,760</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">162,577,500</td>
<td align="right">161,007,000</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">16,603,860</td>
<td align="right">16,443,640</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,032,220</td>
<td align="right">7,973,960</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">28,863,200</td>
<td align="right">28,674,100</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">141,460,740</td>
<td align="right">140,665,560</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,781,000</td>
<td align="right">26,648,180</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">34,951,680</td>
<td align="right">34,785,960</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">62,177,580</td>
<td align="right">62,025,000</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,396,260</td>
<td align="right">1,393,480</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,411,000</td>
<td align="right">2,410,980</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">41,912,040</td>
<td align="right">41,912,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">35,514,600</td>
<td align="right">35,514,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">4,013,520</td>
<td align="right">4,013,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">4,013,340</td>
<td align="right">4,013,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,091,760</td>
<td align="right">1,091,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,091,700</td>
<td align="right">1,091,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">855,060</td>
<td align="right">855,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">835,200</td>
<td align="right">835,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">406,300</td>
<td align="right">406,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">378,060</td>
<td align="right">378,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">94,920</td>
<td align="right">94,920</td>
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
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,620</td>
<td align="right">1,620</td>
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
<td align="left">LOAD_FAST_AND_CLEAR</td>
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
<td align="left">LOAD_FAST_LOAD_FAST</td>
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
<td align="right">28,855,380</td>
<td align="right">6.5%</td>
<td align="right">28,666,380</td>
<td align="right">6.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">415,632,600</td>
<td align="right">93.5%</td>
<td align="right">415,632,600</td>
<td align="right">93.5%</td>
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
<td align="right">7,760</td>
<td align="right">99.2%</td>
<td align="right">7,660</td>
<td align="right">99.2%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">60</td>
<td align="right">0.8%</td>
<td align="right">60</td>
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
<td align="left">out of range</td>
<td align="right">7,060</td>
<td align="right">91.0%</td>
<td align="right">6,960</td>
<td align="right">90.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">200</td>
<td align="right">2.6%</td>
<td align="right">200</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">200</td>
<td align="right">2.6%</td>
<td align="right">200</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">120</td>
<td align="right">1.5%</td>
<td align="right">120</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">120</td>
<td align="right">1.5%</td>
<td align="right">120</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">40</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">20</td>
<td align="right">0.3%</td>
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
<td align="right">26,601,120</td>
<td align="right">100.0%</td>
<td align="right">11,160,700</td>
<td align="right">100.0%</td>
<td align="right">-58.0%</td>
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
<td align="right">28,452,900</td>
<td align="right">9.1%</td>
<td align="right">27,649,840</td>
<td align="right">8.7%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,916,060</td>
<td align="right">9.0%</td>
<td align="right">27,128,160</td>
<td align="right">8.6%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">282,985,280</td>
<td align="right">90.9%</td>
<td align="right">288,498,940</td>
<td align="right">91.3%</td>
<td align="right">1.9%</td>
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
<td align="right">537,320</td>
<td align="right">100.0%</td>
<td align="right">522,160</td>
<td align="right">100.0%</td>
<td align="right">-2.8%</td>
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
<td align="right">406,200</td>
<td align="right">0.3%</td>
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
<td align="right">130,939,800</td>
<td align="right">99.7%</td>
<td align="right">130,939,800</td>
<td align="right">99.7%</td>
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
<td align="right">100</td>
<td align="right">100.0%</td>
<td align="right">100</td>
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
<td align="left">list</td>
<td align="right">100</td>
<td align="right">100.0%</td>
<td align="right">100</td>
<td align="right">100.0%</td>
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
<td align="right">1,395,660</td>
<td align="right">3.9%</td>
<td align="right">1,392,880</td>
<td align="right">3.9%</td>
<td align="right">-0.2%</td>
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
<td align="right">96.1%</td>
<td align="right">34,664,280</td>
<td align="right">96.1%</td>
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
<td align="right">600</td>
<td align="right">100.0%</td>
<td align="right">600</td>
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
<td align="right">320</td>
<td align="right">53.3%</td>
<td align="right">320</td>
<td align="right">53.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">33.3%</td>
<td align="right">200</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">80</td>
<td align="right">13.3%</td>
<td align="right">80</td>
<td align="right">13.3%</td>
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
<td align="right">1,351,600</td>
<td align="right">32.6%</td>
<td align="right">346,520</td>
<td align="right">11.4%</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,792,460</td>
<td align="right">67.4%</td>
<td align="right">2,691,280</td>
<td align="right">88.6%</td>
<td align="right">-3.6%</td>
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
<td align="right">940</td>
<td align="right">100.0%</td>
<td align="right">920</td>
<td align="right">100.0%</td>
<td align="right">-2.1%</td>
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
<td align="left">enumerate</td>
<td align="right">40</td>
<td align="right">4.3%</td>
<td align="right">20</td>
<td align="right">2.2%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">540</td>
<td align="right">57.4%</td>
<td align="right">540</td>
<td align="right">58.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">160</td>
<td align="right">17.0%</td>
<td align="right">160</td>
<td align="right">17.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">100</td>
<td align="right">10.6%</td>
<td align="right">100</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">60</td>
<td align="right">6.4%</td>
<td align="right">60</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">40</td>
<td align="right">4.3%</td>
<td align="right">40</td>
<td align="right">4.3%</td>
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
<td align="right">11,586,960</td>
<td align="right">11,586,960 / 0 !!</td>
<td align="right">11,586,960</td>
<td align="right">11,586,960 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">2,209,860</td>
<td align="right">2,209,860 / 0 !!</td>
<td align="right">2,209,860</td>
<td align="right">2,209,860 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">405,480</td>
<td align="right">405,480 / 0 !!</td>
<td align="right">405,480</td>
<td align="right">405,480 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">14,400</td>
<td align="right">14,400 / 0 !!</td>
<td align="right">14,400</td>
<td align="right">14,400 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">13,860</td>
<td align="right">13,860 / 0 !!</td>
<td align="right">13,860</td>
<td align="right">13,860 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,320</td>
<td align="right">1,320 / 0 !!</td>
<td align="right">1,320</td>
<td align="right">1,320 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">37,558,840</td>
<td align="right">6.8%</td>
<td align="right">33,686,020</td>
<td align="right">6.3%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,230,120</td>
<td align="right">1.9%</td>
<td align="right">9,773,960</td>
<td align="right">1.8%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">504,032,920</td>
<td align="right">91.3%</td>
<td align="right">494,147,180</td>
<td align="right">91.9%</td>
<td align="right">-2.0%</td>
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
<td align="right">11,040</td>
<td align="right">5.4%</td>
<td align="right">10,200</td>
<td align="right">5.2%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">193,300</td>
<td align="right">94.6%</td>
<td align="right">184,740</td>
<td align="right">94.8%</td>
<td align="right">-4.4%</td>
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
<td align="right">1,120</td>
<td align="right">10.1%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">100</td>
<td align="right">0.9%</td>
<td align="right">160</td>
<td align="right">1.6%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">60</td>
<td align="right">0.5%</td>
<td align="right">80</td>
<td align="right">0.8%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">120</td>
<td align="right">1.1%</td>
<td align="right">120</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
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
<td align="right">156,596,440</td>
<td align="right">100.0%</td>
<td align="right">151,034,180</td>
<td align="right">100.0%</td>
<td align="right">-3.6%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">183,540</td>
<td align="right">0.1%</td>
<td align="right">181,620</td>
<td align="right">0.1%</td>
<td align="right">-1.0%</td>
</tr>
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
<td align="right">7,971,560</td>
<td align="right">3.3%</td>
<td align="right">-0.7%</td>
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
<td align="right">231,826,980</td>
<td align="right">96.6%</td>
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
<td align="right">3,460</td>
<td align="right">58.8%</td>
<td align="right">3,420</td>
<td align="right">58.8%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,420</td>
<td align="right">41.2%</td>
<td align="right">2,400</td>
<td align="right">41.2%</td>
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
<td align="left">other</td>
<td align="right">9,580</td>
<td align="right">395.9%</td>
<td align="right">9,740</td>
<td align="right">405.8%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">2,380</td>
<td align="right">98.3%</td>
<td align="right">2,360</td>
<td align="right">98.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">40</td>
<td align="right">1.7%</td>
<td align="right">40</td>
<td align="right">1.7%</td>
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
<td align="right">26,772,000</td>
<td align="right">50.2%</td>
<td align="right">26,639,220</td>
<td align="right">50.1%</td>
<td align="right">-0.5%</td>
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
<td align="right">49.8%</td>
<td align="right">26,554,200</td>
<td align="right">49.9%</td>
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
<td align="right">9,000</td>
<td align="right">100.0%</td>
<td align="right">8,960</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">9,000</td>
<td align="right">100.0%</td>
<td align="right">8,960</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">2,221,920</td>
<td align="right">1.7%</td>
<td align="right">13,500</td>
<td align="right">0.0%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,878,540</td>
<td align="right">3.0%</td>
<td align="right">1,221,460</td>
<td align="right">1.0%</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">123,331,340</td>
<td align="right">95.2%</td>
<td align="right">117,302,440</td>
<td align="right">99.0%</td>
<td align="right">-4.9%</td>
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
<td align="right">50,160</td>
<td align="right">40.7%</td>
<td align="right">3,700</td>
<td align="right">13.8%</td>
<td align="right">-92.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">73,140</td>
<td align="right">59.3%</td>
<td align="right">23,020</td>
<td align="right">86.2%</td>
<td align="right">-68.5%</td>
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
<td align="right">46,460</td>
<td align="right">92.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,680</td>
<td align="right">5.3%</td>
<td align="right">2,680</td>
<td align="right">72.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,000</td>
<td align="right">2.0%</td>
<td align="right">1,000</td>
<td align="right">27.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.5%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,124,308,220</td>
<td align="right">63.5%</td>
<td align="right">2,376,227,100</td>
<td align="right">61.8%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,615,748,580</td>
<td align="right">32.8%</td>
<td align="right">1,311,797,700</td>
<td align="right">34.1%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">138,336,040</td>
<td align="right">2.8%</td>
<td align="right">115,527,580</td>
<td align="right">3.0%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">42,751,220</td>
<td align="right">0.9%</td>
<td align="right">38,833,060</td>
<td align="right">1.0%</td>
<td align="right">-9.2%</td>
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
<td align="right">2,221,920</td>
<td align="right">1.4%</td>
<td align="right">13,500</td>
<td align="right">0.0%</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">26,601,120</td>
<td align="right">16.4%</td>
<td align="right">11,160,700</td>
<td align="right">8.0%</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">37,558,840</td>
<td align="right">23.1%</td>
<td align="right">33,686,020</td>
<td align="right">24.1%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">2,792,460</td>
<td align="right">1.7%</td>
<td align="right">2,691,280</td>
<td align="right">1.9%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">27,916,060</td>
<td align="right">17.2%</td>
<td align="right">27,128,160</td>
<td align="right">19.4%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,029,800</td>
<td align="right">4.9%</td>
<td align="right">7,971,560</td>
<td align="right">5.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">28,855,380</td>
<td align="right">17.8%</td>
<td align="right">28,666,380</td>
<td align="right">20.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">26,772,000</td>
<td align="right">16.5%</td>
<td align="right">26,639,220</td>
<td align="right">19.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,395,660</td>
<td align="right">0.9%</td>
<td align="right">1,392,880</td>
<td align="right">1.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">406,200</td>
<td align="right">0.2%</td>
<td align="right">406,200</td>
<td align="right">0.3%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,610,400</td>
<td align="right">6.1%</td>
<td align="right">679,080</td>
<td align="right">1.7%</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,264,780</td>
<td align="right">3.0%</td>
<td align="right">539,020</td>
<td align="right">1.4%</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">13,817,100</td>
<td align="right">32.3%</td>
<td align="right">9,034,380</td>
<td align="right">23.3%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,536,080</td>
<td align="right">3.6%</td>
<td align="right">1,079,920</td>
<td align="right">2.8%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">14,635,440</td>
<td align="right">34.2%</td>
<td align="right">18,615,100</td>
<td align="right">47.9%</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,060</td>
<td align="right">0.0%</td>
<td align="right">2,120</td>
<td align="right">0.0%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">183,180</td>
<td align="right">0.4%</td>
<td align="right">181,260</td>
<td align="right">0.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,468,680</td>
<td align="right">19.8%</td>
<td align="right">8,468,680</td>
<td align="right">21.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">225,360</td>
<td align="right">0.5%</td>
<td align="right">225,360</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,300</td>
<td align="right">0.0%</td>
<td align="right">2,300</td>
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
<td align="right">115,224</td>
<td align="right"></td>
<td align="right">335,320</td>
<td align="right"></td>
<td align="right">191.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">143,122</td>
<td align="right"></td>
<td align="right">355,969</td>
<td align="right"></td>
<td align="right">148.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">218,067,940</td>
<td align="right">7.8%</td>
<td align="right">136,266,100</td>
<td align="right">4.9%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">2,760</td>
<td align="right">0.0%</td>
<td align="right">3,540</td>
<td align="right">0.0%</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">736,819,296</td>
<td align="right">24.5%</td>
<td align="right">923,317,686</td>
<td align="right">30.7%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">35,196</td>
<td align="right"></td>
<td align="right">27,142</td>
<td align="right"></td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">52,619,600</td>
<td align="right">1.8%</td>
<td align="right">40,724,980</td>
<td align="right">1.4%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">843,433,612</td>
<td align="right">30.2%</td>
<td align="right">1,004,336,131</td>
<td align="right">36.0%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,108,051,240</td>
<td align="right">39.7%</td>
<td align="right">944,893,160</td>
<td align="right">33.8%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">624,010,265</td>
<td align="right">22.3%</td>
<td align="right">706,372,559</td>
<td align="right">25.3%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,439,642,680</td>
<td align="right">47.9%</td>
<td align="right">1,250,890,160</td>
<td align="right">41.6%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">776,850,466</td>
<td align="right">25.8%</td>
<td align="right">789,301,802</td>
<td align="right">26.3%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">82,265,296</td>
<td align="right"></td>
<td align="right">82,370,080</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">84,881,584</td>
<td align="right"></td>
<td align="right">84,889,498</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">27,487,220</td>
<td align="right">9.1%</td>
<td align="right">27,489,660</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">133,921,640</td>
<td align="right">44.3%</td>
<td align="right">133,925,240</td>
<td align="right">44.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">161,511,168</td>
<td align="right"></td>
<td align="right">161,512,737</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">106,431,660</td>
<td align="right">35.2%</td>
<td align="right">106,432,040</td>
<td align="right">35.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">168,239,480</td>
<td align="right"></td>
<td align="right">168,239,400</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">168,240,220</td>
<td align="right">55.7%</td>
<td align="right">168,240,140</td>
<td align="right">55.7%</td>
<td align="right">-0.0%</td>
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
<td align="right">6,660</td>
<td align="right">8,249,180</td>
<td align="right">219,593,675</td>
<td align="right">10,671,960</td>
<td align="right">21,228,580</td>
<td align="right">6,660</td>
<td align="right">8,249,180</td>
<td align="right">219,536,268</td>
<td align="right">10,653,120</td>
<td align="right">21,246,580</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">420</td>
<td align="right">4.8%</td>
<td align="right">3,540</td>
<td align="right">23.2%</td>
<td align="right">742.9%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">100</td>
<td align="right">23.8%</td>
<td align="right">580</td>
<td align="right">16.4%</td>
<td align="right">480.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">60</td>
<td align="right">0.7%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">8,780</td>
<td align="right"></td>
<td align="right">15,240</td>
<td align="right"></td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,024,893,280</td>
<td align="right">5,534.8%</td>
<td align="right">6,585,463,040</td>
<td align="right">6,778.4%</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">2,260</td>
<td align="right">25.7%</td>
<td align="right">3,100</td>
<td align="right">20.3%</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">72,719,120</td>
<td align="right"></td>
<td align="right">97,154,180</td>
<td align="right"></td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">6,100</td>
<td align="right">69.5%</td>
<td align="right">7,580</td>
<td align="right">49.7%</td>
<td align="right">24.3%</td>
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
<td align="right">120</td>
<td align="right">0.8%</td>
<td align="right">120 / 0 !!</td>
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
<td align="right">1,020</td>
<td align="right">6.7%</td>
<td align="right">1,020 / 0 !!</td>
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
<td align="right">200</td>
<td align="right">1.3%</td>
<td align="right">200 / 0 !!</td>
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
<td align="right">280</td>
<td align="right">66.7%</td>
<td align="right">3,480</td>
<td align="right">98.3%</td>
<td align="right">1,142.9%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">420</td>
<td align="right"></td>
<td align="right">3,540</td>
<td align="right"></td>
<td align="right">742.9%</td>
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
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">497,380</td>
<td align="right">8.1%</td>
<td align="right">8,248,980</td>
<td align="right">13.8%</td>
<td align="right">1,558.5%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">6,144,000</td>
<td align="right"></td>
<td align="right">59,965,440</td>
<td align="right"></td>
<td align="right">876.0%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">132,000</td>
<td align="right">2.1%</td>
<td align="right">1,232,320</td>
<td align="right">2.1%</td>
<td align="right">833.6%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">5,514,620</td>
<td align="right">89.8%</td>
<td align="right">50,484,140</td>
<td align="right">84.2%</td>
<td align="right">815.5%</td>
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
<td align="left"><= 4,096</td>
<td align="left">40</td>
<td align="right">14.3%</td>
<td align="left">60</td>
<td align="right">1.7%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">0</td>
<td align="right">0.0%</td>
<td align="left">1,500</td>
<td align="right">43.1%</td>
<td align="right">1,500 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">120</td>
<td align="right">42.9%</td>
<td align="left">1,020</td>
<td align="right">29.3%</td>
<td align="right">750.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">20</td>
<td align="right">7.1%</td>
<td align="left">460</td>
<td align="right">13.2%</td>
<td align="right">2,200.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">100</td>
<td align="right">35.7%</td>
<td align="left">280</td>
<td align="right">8.0%</td>
<td align="right">180.0%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">160</td>
<td align="right">4.6%</td>
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
<td align="left"><= 16</td>
<td align="right">40</td>
<td align="right">9.5%</td>
<td align="right">60</td>
<td align="right">1.7%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">100</td>
<td align="right">2.8%</td>
<td align="right">100 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">40</td>
<td align="right">9.5%</td>
<td align="right">1,700</td>
<td align="right">48.0%</td>
<td align="right">4,150.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">80</td>
<td align="right">19.0%</td>
<td align="right">640</td>
<td align="right">18.1%</td>
<td align="right">700.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">100</td>
<td align="right">23.8%</td>
<td align="right">520</td>
<td align="right">14.7%</td>
<td align="right">420.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">140</td>
<td align="right">33.3%</td>
<td align="right">400</td>
<td align="right">11.3%</td>
<td align="right">185.7%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">20</td>
<td align="right">4.8%</td>
<td align="right">120</td>
<td align="right">3.4%</td>
<td align="right">500.0%</td>
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
<td align="left"><= 8</td>
<td align="right">20</td>
<td align="right">4.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20</td>
<td align="right">4.8%</td>
<td align="right">80</td>
<td align="right">2.3%</td>
<td align="right">300.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">1,480</td>
<td align="right">41.8%</td>
<td align="right">1,480 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">80</td>
<td align="right">19.0%</td>
<td align="right">860</td>
<td align="right">24.3%</td>
<td align="right">975.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">60</td>
<td align="right">14.3%</td>
<td align="right">560</td>
<td align="right">15.8%</td>
<td align="right">833.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">100</td>
<td align="right">23.8%</td>
<td align="right">340</td>
<td align="right">9.6%</td>
<td align="right">240.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">160</td>
<td align="right">4.5%</td>
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
<td align="left">_CALL_LEN</td>
<td align="right">8,700</td>
<td align="right">168,920</td>
<td align="right">1,841.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">8,700</td>
<td align="right">82,340</td>
<td align="right">846.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">8,700</td>
<td align="right">76,480</td>
<td align="right">779.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">61,820</td>
<td align="right">462,300</td>
<td align="right">647.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">3,127,920</td>
<td align="right">19,652,980</td>
<td align="right">528.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">61,820</td>
<td align="right">378,460</td>
<td align="right">512.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">4,767,560</td>
<td align="right">25,273,360</td>
<td align="right">430.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">4,767,560</td>
<td align="right">22,816,200</td>
<td align="right">378.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">4,157,700</td>
<td align="right">19,646,160</td>
<td align="right">372.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">14,076,860</td>
<td align="right">64,240,880</td>
<td align="right">356.4%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">61,820</td>
<td align="right">271,200</td>
<td align="right">338.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">61,820</td>
<td align="right">271,200</td>
<td align="right">338.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">61,820</td>
<td align="right">267,120</td>
<td align="right">332.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">26,936,400</td>
<td align="right">115,210,960</td>
<td align="right">327.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">26,936,400</td>
<td align="right">115,210,960</td>
<td align="right">327.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">26,936,400</td>
<td align="right">115,210,960</td>
<td align="right">327.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">13,082,960</td>
<td align="right">49,182,180</td>
<td align="right">275.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">37,803,640</td>
<td align="right">133,438,200</td>
<td align="right">253.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">10,006,240</td>
<td align="right">34,287,260</td>
<td align="right">242.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">17,605,080</td>
<td align="right">57,773,700</td>
<td align="right">228.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">211,129,580</td>
<td align="right">557,147,000</td>
<td align="right">163.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">58,450,760</td>
<td align="right">151,473,700</td>
<td align="right">159.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,484,960</td>
<td align="right">22,439,620</td>
<td align="right">136.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,484,960</td>
<td align="right">22,439,620</td>
<td align="right">136.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,482,820</td>
<td align="right">29,880</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,558,860</td>
<td align="right">8,914,000</td>
<td align="right">95.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">22,330,820</td>
<td align="right">42,974,840</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">6,762,100</td>
<td align="right">12,272,300</td>
<td align="right">81.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">67,278,660</td>
<td align="right">120,925,880</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">67,278,660</td>
<td align="right">120,925,880</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">704,386,960</td>
<td align="right">1,192,464,040</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">36,394,820</td>
<td align="right">61,407,000</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">36,394,820</td>
<td align="right">61,407,000</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">680,102,000</td>
<td align="right">1,137,177,060</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">37,408,720</td>
<td align="right">61,477,360</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">210,520</td>
<td align="right">344,420</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">51,592,040</td>
<td align="right">82,555,580</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">15,094,000</td>
<td align="right">23,562,720</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,252,560</td>
<td align="right">1,902,800</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">8,925,260</td>
<td align="right">13,297,140</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,905,300</td>
<td align="right">2,695,440</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">37,417,420</td>
<td align="right">53,696,880</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">72,719,120</td>
<td align="right">97,154,180</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">72,719,120</td>
<td align="right">97,154,080</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">14,091,500</td>
<td align="right">18,747,140</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">48,429,680</td>
<td align="right">63,882,680</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">43,157,920</td>
<td align="right">30,690,400</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">18,354,000</td>
<td align="right">13,244,920</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">2,077,080</td>
<td align="right">2,649,980</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">126,869,540</td>
<td align="right">159,436,820</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">91,073,120</td>
<td align="right">110,399,100</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">626,280</td>
<td align="right">759,120</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">18,293,400</td>
<td align="right">22,076,820</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">2,633,960</td>
<td align="right">3,126,820</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">10,976,460</td>
<td align="right">12,908,340</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">116,315,020</td>
<td align="right">135,396,020</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">31,635,960</td>
<td align="right">36,752,000</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">31,635,960</td>
<td align="right">36,749,220</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">1,130,800</td>
<td align="right">1,296,480</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">50,218,160</td>
<td align="right">43,742,820</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,482,820</td>
<td align="right">1,674,020</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">26,570,860</td>
<td align="right">29,674,820</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">7,779,300</td>
<td align="right">8,679,460</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">7,779,300</td>
<td align="right">8,679,460</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,384,500</td>
<td align="right">1,533,060</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">7,779,300</td>
<td align="right">8,543,240</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">56,397,340</td>
<td align="right">61,473,160</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">86,307,400</td>
<td align="right">93,589,260</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">8,377,620</td>
<td align="right">9,027,860</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">19,045,900</td>
<td align="right">17,591,680</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">645,540</td>
<td align="right">693,720</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">10,612,840</td>
<td align="right">11,368,180</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,582,800</td>
<td align="right">9,185,460</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">21,166,200</td>
<td align="right">22,448,320</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">22,449,780</td>
<td align="right">23,665,520</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">17,103,240</td>
<td align="right">17,898,520</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">17,103,240</td>
<td align="right">17,898,520</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">17,103,240</td>
<td align="right">17,898,520</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">17,103,240</td>
<td align="right">17,898,520</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">20,324,960</td>
<td align="right">21,263,920</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">20,893,680</td>
<td align="right">21,639,460</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">28,945,960</td>
<td align="right">29,920,580</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">8,578,160</td>
<td align="right">8,854,760</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">31,293,920</td>
<td align="right">32,294,340</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">31,293,920</td>
<td align="right">32,294,340</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">20,248,800</td>
<td align="right">20,804,520</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">4,206,780</td>
<td align="right">4,307,960</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">26,859,700</td>
<td align="right">27,487,060</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">27,505,240</td>
<td align="right">28,132,600</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">26,859,700</td>
<td align="right">27,465,140</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">8,315,400</td>
<td align="right">8,467,980</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">8,315,400</td>
<td align="right">8,467,980</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">45,646,180</td>
<td align="right">46,423,160</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">31,662,940</td>
<td align="right">32,181,580</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">8,315,400</td>
<td align="right">8,449,620</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">27,784,040</td>
<td align="right">28,183,240</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">27,784,040</td>
<td align="right">28,183,240</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">59,207,520</td>
<td align="right">60,042,080</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">10,483,440</td>
<td align="right">10,627,380</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">15,558,600</td>
<td align="right">15,743,480</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">9,323,940</td>
<td align="right">9,228,380</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">88,734,340</td>
<td align="right">89,588,720</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">9,323,940</td>
<td align="right">9,342,800</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">645,540</td>
<td align="right">646,460</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">17,991,300</td>
<td align="right">17,994,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">1,271,800</td>
<td align="right">1,271,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">17,563,080</td>
<td align="right">17,563,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">8,405,580</td>
<td align="right">8,405,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">8,405,580</td>
<td align="right">8,405,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">1,252,560</td>
<td align="right">1,252,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">648,240</td>
<td align="right">648,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">645,540</td>
<td align="right">645,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right"></td>
<td align="right">46,453,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right"></td>
<td align="right">15,606,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">15,440,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">15,437,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right"></td>
<td align="right">15,437,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">15,437,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">1,570,500</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right"></td>
<td align="right">660,260</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">497,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right"></td>
<td align="right">497,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">423,220</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right"></td>
<td align="right">189,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">132,780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right"></td>
<td align="right">63,180</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right"></td>
<td align="right">63,180</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">58,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right"></td>
<td align="right">50,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">37,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">37,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">25,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">18,900</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right"></td>
<td align="right">18,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right"></td>
<td align="right">12,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right"></td>
<td align="right">4,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right"></td>
<td align="right">3,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right"></td>
<td align="right">3,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">3,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right"></td>
<td align="right">3,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">2,900</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">2,780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right"></td>
<td align="right">1,040</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">100</td>
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
<td align="right"></td>
<td align="right">660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right"></td>
<td align="right">540</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">100</td>
<td align="right">120</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">100</td>
<td align="right">120</td>
<td align="right">20.0%</td>
</tr>
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
