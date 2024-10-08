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
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">36,808,940</td>
<td align="right">15,352,260</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5,632,000</td>
<td align="right">2,593,840</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">36,640</td>
<td align="right">18,320</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">50,202,200</td>
<td align="right">25,286,400</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">23,101,180</td>
<td align="right">12,571,480</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">185,079,340</td>
<td align="right">103,094,980</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">49,182,620</td>
<td align="right">28,216,480</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">203,240,760</td>
<td align="right">116,693,500</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">39,749,560</td>
<td align="right">56,549,660</td>
<td align="right">42.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">17,613,700</td>
<td align="right">10,306,400</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">12,419,740</td>
<td align="right">7,595,000</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,186,560</td>
<td align="right">8,313,000</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">14,197,480</td>
<td align="right">9,351,940</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">15,348,040</td>
<td align="right">10,196,640</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">806,320</td>
<td align="right">551,000</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">136,603,300</td>
<td align="right">93,928,220</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">9,797,100</td>
<td align="right">6,759,680</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">47,079,280</td>
<td align="right">33,630,300</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">14,992,520</td>
<td align="right">10,971,680</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">212,614,500</td>
<td align="right">156,149,420</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,192,180</td>
<td align="right">883,200</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">23,911,060</td>
<td align="right">18,047,880</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">3,235,280</td>
<td align="right">2,444,500</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">38,390,320</td>
<td align="right">29,244,640</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,392,040</td>
<td align="right">29,246,360</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">19,431,980</td>
<td align="right">14,939,060</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">23,539,980</td>
<td align="right">18,213,040</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">14,549,560</td>
<td align="right">11,269,380</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">8,198,940</td>
<td align="right">6,371,300</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">210,675,760</td>
<td align="right">164,132,020</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">614,000</td>
<td align="right">478,720</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">451,340</td>
<td align="right">352,080</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">274,551,920</td>
<td align="right">216,251,600</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">100,805,040</td>
<td align="right">80,543,200</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">3,640,960</td>
<td align="right">2,923,140</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">3,645,700</td>
<td align="right">2,927,880</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">16,725,660</td>
<td align="right">13,604,640</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,366,645,420</td>
<td align="right">1,132,615,320</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">31,334,260</td>
<td align="right">25,971,140</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">21,749,180</td>
<td align="right">18,028,680</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">295,149,380</td>
<td align="right">245,679,940</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">15,640</td>
<td align="right">13,020</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">59,261,260</td>
<td align="right">49,509,320</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,399,600</td>
<td align="right">1,172,660</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">6,354,860</td>
<td align="right">5,329,280</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,135,160</td>
<td align="right">4,335,580</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">20,509,520</td>
<td align="right">17,500,680</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">23,205,240</td>
<td align="right">19,815,440</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">701,320</td>
<td align="right">801,880</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">26,141,380</td>
<td align="right">22,497,600</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">13,051,060</td>
<td align="right">11,258,300</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">85,720,560</td>
<td align="right">74,035,900</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">285,573,660</td>
<td align="right">248,168,140</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">17,298,040</td>
<td align="right">15,189,120</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">9,822,800</td>
<td align="right">8,639,600</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">841,320</td>
<td align="right">941,520</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">26,798,580</td>
<td align="right">23,625,580</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">13,365,720</td>
<td align="right">14,898,320</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">6,136,660</td>
<td align="right">5,455,220</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">15,117,180</td>
<td align="right">13,478,420</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">101,114,100</td>
<td align="right">90,345,640</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">137,312,360</td>
<td align="right">122,849,220</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,995,900</td>
<td align="right">3,590,580</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">121,595,320</td>
<td align="right">109,267,020</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">959,480</td>
<td align="right">862,880</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">9,190,600</td>
<td align="right">8,270,000</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">166,334,940</td>
<td align="right">149,735,260</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">192,836,160</td>
<td align="right">173,863,820</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">305,537,400</td>
<td align="right">276,502,100</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">123,620</td>
<td align="right">111,920</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,782,800</td>
<td align="right">3,431,380</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">59,554,200</td>
<td align="right">54,220,080</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,236,020</td>
<td align="right">1,127,080</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">141,535,620</td>
<td align="right">129,122,600</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">38,382,460</td>
<td align="right">35,136,460</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">190,790,660</td>
<td align="right">174,836,900</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,928,420</td>
<td align="right">2,691,280</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">21,696,240</td>
<td align="right">19,979,680</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">186,792,940</td>
<td align="right">173,301,220</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">4,319,260</td>
<td align="right">4,007,560</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">299,614,860</td>
<td align="right">278,323,480</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,669,760</td>
<td align="right">2,486,660</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">79,270,820</td>
<td align="right">73,930,640</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,156,480</td>
<td align="right">2,017,680</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">20,253,600</td>
<td align="right">21,552,260</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">547,920</td>
<td align="right">513,500</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,814,800</td>
<td align="right">3,577,400</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">215,420</td>
<td align="right">202,320</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,989,040</td>
<td align="right">5,627,780</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">32,875,560</td>
<td align="right">34,834,280</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">2,159,500</td>
<td align="right">2,036,820</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">52,250,840</td>
<td align="right">49,353,560</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">6,329,820</td>
<td align="right">6,672,200</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">29,259,060</td>
<td align="right">27,719,420</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">76,876,660</td>
<td align="right">80,837,240</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">5,318,900</td>
<td align="right">5,056,720</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">709,380</td>
<td align="right">676,700</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">33,867,840</td>
<td align="right">32,314,980</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">693,700</td>
<td align="right">667,700</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">3,647,200</td>
<td align="right">3,518,820</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,102,320</td>
<td align="right">2,043,000</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">6,607,040</td>
<td align="right">6,429,620</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">17,995,440</td>
<td align="right">18,478,620</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">28,739,640</td>
<td align="right">28,114,020</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">55,717,120</td>
<td align="right">54,582,420</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">50,958,520</td>
<td align="right">51,884,560</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">9,522,720</td>
<td align="right">9,359,520</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">10,150,520</td>
<td align="right">10,026,400</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">104,480</td>
<td align="right">103,380</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">21,506,840</td>
<td align="right">21,288,320</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,054,440</td>
<td align="right">12,159,580</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,683,580</td>
<td align="right">1,695,740</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">8,574,560</td>
<td align="right">8,527,580</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">25,757,760</td>
<td align="right">25,671,180</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">11,432,900</td>
<td align="right">11,402,820</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">721,860</td>
<td align="right">722,800</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">49,488,280</td>
<td align="right">49,465,440</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">51,025,320</td>
<td align="right">51,039,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">4,806,940</td>
<td align="right">4,805,980</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">15,519,420</td>
<td align="right">15,519,420</td>
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
<td align="left">MAKE_FUNCTION</td>
<td align="right">484,720</td>
<td align="right">484,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">316,640</td>
<td align="right">316,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">310,860</td>
<td align="right">310,860</td>
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
<td align="right">130,620</td>
<td align="right">130,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">109,540</td>
<td align="right">109,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">96,800</td>
<td align="right">96,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">94,860</td>
<td align="right">94,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">91,660</td>
<td align="right">91,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">62,320</td>
<td align="right">62,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">46,320</td>
<td align="right">46,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">36,600</td>
<td align="right">36,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">36,220</td>
<td align="right">36,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">32,180</td>
<td align="right">32,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">25,420</td>
<td align="right">25,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20,020</td>
<td align="right">20,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">13,800</td>
<td align="right">13,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,980</td>
<td align="right">11,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">10,340</td>
<td align="right">10,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">9,020</td>
<td align="right">9,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">9,000</td>
<td align="right">9,000</td>
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
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1,400</td>
<td align="right">1,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">1,360</td>
<td align="right">1,360</td>
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
<td align="right">17,955,660</td>
<td align="right">21.6%</td>
<td align="right">18,438,760</td>
<td align="right">22.1%</td>
<td align="right">2.7%</td>
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
<td align="right">78.4%</td>
<td align="right">65,036,300</td>
<td align="right">77.9%</td>
<td align="right">-0.3%</td>
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
<td align="right">32,800</td>
<td align="right">82.5%</td>
<td align="right">32,880</td>
<td align="right">82.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,980</td>
<td align="right">17.5%</td>
<td align="right">6,980</td>
<td align="right">17.5%</td>
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
<td align="right">9,020</td>
<td align="right">27.5%</td>
<td align="right">10,080</td>
<td align="right">30.7%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,260</td>
<td align="right">28.2%</td>
<td align="right">8,320</td>
<td align="right">25.3%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">10,740</td>
<td align="right">32.7%</td>
<td align="right">10,700</td>
<td align="right">32.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,520</td>
<td align="right">4.6%</td>
<td align="right">1,520</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,260</td>
<td align="right">3.8%</td>
<td align="right">1,260</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">660</td>
<td align="right">2.0%</td>
<td align="right">660</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">200</td>
<td align="right">0.6%</td>
<td align="right">200</td>
<td align="right">0.6%</td>
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
<td align="right">20,509,520</td>
<td align="right">100.0%</td>
<td align="right">17,500,680</td>
<td align="right">100.0%</td>
<td align="right">-14.7%</td>
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
<td align="right">934,000</td>
<td align="right">0.7%</td>
<td align="right">836,980</td>
<td align="right">0.6%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,057,900</td>
<td align="right">2.3%</td>
<td align="right">3,052,160</td>
<td align="right">2.3%</td>
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
<td align="right">126,121,360</td>
<td align="right">96.9%</td>
<td align="right">126,065,900</td>
<td align="right">97.0%</td>
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
<td align="right">14,180</td>
<td align="right">17.1%</td>
<td align="right">14,600</td>
<td align="right">17.5%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">68,720</td>
<td align="right">82.9%</td>
<td align="right">68,620</td>
<td align="right">82.5%</td>
<td align="right">-0.1%</td>
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
<td align="right">12,940</td>
<td align="right">91.3%</td>
<td align="right">13,360</td>
<td align="right">91.5%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,160</td>
<td align="right">8.2%</td>
<td align="right">1,160</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
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
<td align="right">21,231,680</td>
<td align="right">2.8%</td>
<td align="right">18,268,120</td>
<td align="right">2.4%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">743,196,620</td>
<td align="right">97.2%</td>
<td align="right">748,417,580</td>
<td align="right">97.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">71,460</td>
<td align="right">0.0%</td>
<td align="right">71,460</td>
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
<td align="right">461,940</td>
<td align="right">100.0%</td>
<td align="right">406,080</td>
<td align="right">100.0%</td>
<td align="right">-12.1%</td>
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
<td align="right">142,500</td>
<td align="right">0.3%</td>
<td align="right">161,580</td>
<td align="right">0.3%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,085,960</td>
<td align="right">4.2%</td>
<td align="right">2,025,080</td>
<td align="right">4.1%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,220,420</td>
<td align="right">95.5%</td>
<td align="right">47,220,960</td>
<td align="right">95.5%</td>
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
<td align="right">10,780</td>
<td align="right">56.7%</td>
<td align="right">12,340</td>
<td align="right">58.9%</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,240</td>
<td align="right">43.3%</td>
<td align="right">8,600</td>
<td align="right">41.1%</td>
<td align="right">4.4%</td>
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
<td align="right">8,420</td>
<td align="right">78.1%</td>
<td align="right">9,980</td>
<td align="right">80.9%</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">720</td>
<td align="right">6.7%</td>
<td align="right">720</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">660</td>
<td align="right">6.1%</td>
<td align="right">660</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">380</td>
<td align="right">3.5%</td>
<td align="right">380</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">340</td>
<td align="right">3.2%</td>
<td align="right">340</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">200</td>
<td align="right">1.9%</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">6,313,040</td>
<td align="right">8.0%</td>
<td align="right">6,655,480</td>
<td align="right">8.4%</td>
<td align="right">5.4%</td>
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
<td align="right">92.0%</td>
<td align="right">72,826,620</td>
<td align="right">91.6%</td>
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
<td align="right">15,040</td>
<td align="right">89.6%</td>
<td align="right">14,980</td>
<td align="right">89.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,740</td>
<td align="right">10.4%</td>
<td align="right">1,740</td>
<td align="right">10.4%</td>
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
<td align="right">2,920</td>
<td align="right">19.4%</td>
<td align="right">2,900</td>
<td align="right">19.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,860</td>
<td align="right">25.7%</td>
<td align="right">3,840</td>
<td align="right">25.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,640</td>
<td align="right">37.5%</td>
<td align="right">5,620</td>
<td align="right">37.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">2,620</td>
<td align="right">17.4%</td>
<td align="right">2,620</td>
<td align="right">17.5%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,597,300</td>
<td align="right">14.0%</td>
<td align="right">31,586,620</td>
<td align="right">17.0%</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,236,820</td>
<td align="right">11.1%</td>
<td align="right">21,535,180</td>
<td align="right">11.6%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">136,589,740</td>
<td align="right">74.9%</td>
<td align="right">132,922,100</td>
<td align="right">71.4%</td>
<td align="right">-2.7%</td>
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
<td align="right">487,460</td>
<td align="right">97.6%</td>
<td align="right">600,460</td>
<td align="right">98.0%</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">12,200</td>
<td align="right">2.4%</td>
<td align="right">12,500</td>
<td align="right">2.0%</td>
<td align="right">2.5%</td>
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
<td align="right">260</td>
<td align="right">2.1%</td>
<td align="right">560</td>
<td align="right">4.5%</td>
<td align="right">115.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,920</td>
<td align="right">15.7%</td>
<td align="right">1,860</td>
<td align="right">14.9%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">2,180</td>
<td align="right">17.9%</td>
<td align="right">2,220</td>
<td align="right">17.8%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">2,000</td>
<td align="right">16.4%</td>
<td align="right">2,020</td>
<td align="right">16.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,640</td>
<td align="right">29.8%</td>
<td align="right">3,640</td>
<td align="right">29.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">860</td>
<td align="right">7.0%</td>
<td align="right">860</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">540</td>
<td align="right">4.4%</td>
<td align="right">540</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">180</td>
<td align="right">1.5%</td>
<td align="right">180</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">160</td>
<td align="right">1.3%</td>
<td align="right">160</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">140</td>
<td align="right">1.1%</td>
<td align="right">140</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120</td>
<td align="right">1.0%</td>
<td align="right">120</td>
<td align="right">1.0%</td>
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
<td align="right">100,188,560</td>
<td align="right">8.1%</td>
<td align="right">89,455,200</td>
<td align="right">7.3%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">249,550,540</td>
<td align="right">20.3%</td>
<td align="right">257,729,940</td>
<td align="right">20.9%</td>
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
<td align="right">881,115,500</td>
<td align="right">71.5%</td>
<td align="right">883,761,640</td>
<td align="right">71.7%</td>
<td align="right">0.3%</td>
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
<td align="left">Failure</td>
<td align="right">30,160</td>
<td align="right">0.5%</td>
<td align="right">28,000</td>
<td align="right">0.5%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,597,160</td>
<td align="right">99.5%</td>
<td align="right">5,718,700</td>
<td align="right">99.5%</td>
<td align="right">2.2%</td>
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
<td align="right">4,160</td>
<td align="right">13.8%</td>
<td align="right">3,100</td>
<td align="right">11.1%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">10,660</td>
<td align="right">35.3%</td>
<td align="right">9,400</td>
<td align="right">33.6%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">540</td>
<td align="right">1.8%</td>
<td align="right">560</td>
<td align="right">2.0%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">580</td>
<td align="right">1.9%</td>
<td align="right">560</td>
<td align="right">2.0%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">7,820</td>
<td align="right">25.9%</td>
<td align="right">7,980</td>
<td align="right">28.5%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,360</td>
<td align="right">4.5%</td>
<td align="right">1,380</td>
<td align="right">4.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2,480</td>
<td align="right">8.2%</td>
<td align="right">2,460</td>
<td align="right">8.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">940</td>
<td align="right">3.1%</td>
<td align="right">940</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">1.1%</td>
<td align="right">340</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">260</td>
<td align="right">0.9%</td>
<td align="right">260</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">120</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">80</td>
<td align="right">0.3%</td>
<td align="right">80</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
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
<td align="right">252,026,800</td>
<td align="right">100.0%</td>
<td align="right">223,742,460</td>
<td align="right">100.0%</td>
<td align="right">-11.2%</td>
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
<td align="right">31,340</td>
<td align="right">100.0%</td>
<td align="right">31,340</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">71,693,200</td>
<td align="right">45.7%</td>
<td align="right">68,791,500</td>
<td align="right">44.6%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,464,120</td>
<td align="right">13.7%</td>
<td align="right">21,247,420</td>
<td align="right">13.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">63,612,760</td>
<td align="right">40.6%</td>
<td align="right">64,036,960</td>
<td align="right">41.6%</td>
<td align="right">0.7%</td>
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
<td align="right">32,780</td>
<td align="right">2.4%</td>
<td align="right">30,960</td>
<td align="right">2.3%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,362,000</td>
<td align="right">97.6%</td>
<td align="right">1,307,260</td>
<td align="right">97.7%</td>
<td align="right">-4.0%</td>
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
<td align="left">property</td>
<td align="right">460</td>
<td align="right">1.4%</td>
<td align="right">380</td>
<td align="right">1.2%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">22,480</td>
<td align="right">68.6%</td>
<td align="right">20,900</td>
<td align="right">67.5%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,420</td>
<td align="right">19.6%</td>
<td align="right">6,260</td>
<td align="right">20.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">2,500</td>
<td align="right">7.6%</td>
<td align="right">2,500</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">380</td>
<td align="right">1.2%</td>
<td align="right">380</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">360</td>
<td align="right">1.1%</td>
<td align="right">360</td>
<td align="right">1.2%</td>
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
<tr>
<td align="left">overriding descriptor</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">4,806,940</td>
<td align="right">100.0%</td>
<td align="right">4,805,980</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">1,181,160</td>
<td align="right">2.0%</td>
<td align="right">872,260</td>
<td align="right">1.5%</td>
<td align="right">-26.2%</td>
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
<td align="right">97.9%</td>
<td align="right">56,859,000</td>
<td align="right">98.5%</td>
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
<td align="right">8,800</td>
<td align="right">79.6%</td>
<td align="right">8,720</td>
<td align="right">79.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,260</td>
<td align="right">20.4%</td>
<td align="right">2,260</td>
<td align="right">20.6%</td>
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
<td align="right">7,380</td>
<td align="right">83.9%</td>
<td align="right">7,300</td>
<td align="right">83.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">780</td>
<td align="right">8.9%</td>
<td align="right">780</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">420</td>
<td align="right">4.8%</td>
<td align="right">420</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">220</td>
<td align="right">2.5%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,692,540</td>
<td align="right">1.0%</td>
<td align="right">3,389,440</td>
<td align="right">1.0%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,647,920</td>
<td align="right">1.8%</td>
<td align="right">6,504,480</td>
<td align="right">1.8%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">352,366,320</td>
<td align="right">97.1%</td>
<td align="right">344,957,680</td>
<td align="right">97.2%</td>
<td align="right">-2.1%</td>
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
<td align="right">105,920</td>
<td align="right">42.9%</td>
<td align="right">171,620</td>
<td align="right">55.4%</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">140,860</td>
<td align="right">57.1%</td>
<td align="right">138,220</td>
<td align="right">44.6%</td>
<td align="right">-1.9%</td>
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
<td align="right">40,160</td>
<td align="right">37.9%</td>
<td align="right">105,720</td>
<td align="right">61.6%</td>
<td align="right">163.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">620</td>
<td align="right">0.6%</td>
<td align="right">820</td>
<td align="right">0.5%</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">6,620</td>
<td align="right">6.2%</td>
<td align="right">6,500</td>
<td align="right">3.8%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,360</td>
<td align="right">2.2%</td>
<td align="right">2,380</td>
<td align="right">1.4%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">56,140</td>
<td align="right">53.0%</td>
<td align="right">56,180</td>
<td align="right">32.7%</td>
<td align="right">0.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">64,639,560</td>
<td align="right">100.0%</td>
<td align="right">55,726,000</td>
<td align="right">100.0%</td>
<td align="right">-13.8%</td>
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
<td align="right">4,240</td>
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
<td align="right">3,740</td>
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
<td align="right">4,141,254,620</td>
<td align="right">59.5%</td>
<td align="right">3,358,299,060</td>
<td align="right">57.3%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">2,244,170,940</td>
<td align="right">32.2%</td>
<td align="right">1,925,003,820</td>
<td align="right">32.9%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">200,792,660</td>
<td align="right">2.9%</td>
<td align="right">188,217,800</td>
<td align="right">3.2%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">377,968,720</td>
<td align="right">5.4%</td>
<td align="right">386,141,840</td>
<td align="right">6.6%</td>
<td align="right">2.2%</td>
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
<td align="right">1,181,160</td>
<td align="right">0.6%</td>
<td align="right">872,260</td>
<td align="right">0.5%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">20,509,520</td>
<td align="right">10.3%</td>
<td align="right">17,500,680</td>
<td align="right">9.4%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">100,188,560</td>
<td align="right">50.2%</td>
<td align="right">89,455,200</td>
<td align="right">47.9%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,692,540</td>
<td align="right">1.9%</td>
<td align="right">3,389,440</td>
<td align="right">1.8%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">20,236,820</td>
<td align="right">10.1%</td>
<td align="right">21,535,180</td>
<td align="right">11.5%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">6,313,040</td>
<td align="right">3.2%</td>
<td align="right">6,655,480</td>
<td align="right">3.6%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">2,085,960</td>
<td align="right">1.0%</td>
<td align="right">2,025,080</td>
<td align="right">1.1%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">17,955,660</td>
<td align="right">9.0%</td>
<td align="right">18,438,760</td>
<td align="right">9.9%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">21,464,120</td>
<td align="right">10.8%</td>
<td align="right">21,247,420</td>
<td align="right">11.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">4,806,940</td>
<td align="right">2.4%</td>
<td align="right">4,805,980</td>
<td align="right">2.6%</td>
<td align="right">-0.0%</td>
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
<td align="right">12,798,040</td>
<td align="right">3.4%</td>
<td align="right">15,792,900</td>
<td align="right">4.1%</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">12,799,260</td>
<td align="right">3.4%</td>
<td align="right">15,793,720</td>
<td align="right">4.1%</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">75,089,660</td>
<td align="right">19.9%</td>
<td align="right">80,099,680</td>
<td align="right">20.7%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">11,241,420</td>
<td align="right">3.0%</td>
<td align="right">10,631,800</td>
<td align="right">2.8%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">71,688,960</td>
<td align="right">19.0%</td>
<td align="right">68,790,440</td>
<td align="right">17.8%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">107,024,700</td>
<td align="right">28.3%</td>
<td align="right">110,548,780</td>
<td align="right">28.6%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,351,100</td>
<td align="right">2.5%</td>
<td align="right">9,619,240</td>
<td align="right">2.5%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">16,715,600</td>
<td align="right">4.4%</td>
<td align="right">17,063,720</td>
<td align="right">4.4%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">38,933,060</td>
<td align="right">10.3%</td>
<td align="right">38,293,900</td>
<td align="right">9.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">5,306,840</td>
<td align="right">1.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">3,520,140</td>
<td align="right">0.9%</td>
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
<td align="right">10,760,800</td>
<td align="right">2.3%</td>
<td align="right">10,787,140</td>
<td align="right">2.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">51,998,340</td>
<td align="right">11.0%</td>
<td align="right">52,012,520</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">52,010,240</td>
<td align="right">11.0%</td>
<td align="right">52,024,420</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">52,428,160</td>
<td align="right">11.1%</td>
<td align="right">52,442,340</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">52,428,160</td>
<td align="right">11.1%</td>
<td align="right">52,442,340</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">421,371,380</td>
<td align="right">88.9%</td>
<td align="right">421,357,200</td>
<td align="right">88.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">419,455,540</td>
<td align="right">88.5%</td>
<td align="right">419,467,700</td>
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
<td align="left">Interpreter immortal increfs</td>
<td align="right">1,067,617,320</td>
<td align="right">9.1%</td>
<td align="right">867,317,280</td>
<td align="right">7.4%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">3,139,050,000</td>
<td align="right">26.7%</td>
<td align="right">2,625,557,540</td>
<td align="right">22.4%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,134,331,660</td>
<td align="right">9.0%</td>
<td align="right">1,002,593,000</td>
<td align="right">8.0%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">4,841,850,526</td>
<td align="right">41.2%</td>
<td align="right">5,378,483,692</td>
<td align="right">46.0%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">4,435,709,156</td>
<td align="right">35.1%</td>
<td align="right">4,850,905,173</td>
<td align="right">38.5%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">4,341,384,200</td>
<td align="right">34.3%</td>
<td align="right">3,958,042,980</td>
<td align="right">31.4%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,001,320</td>
<td align="right">0.1%</td>
<td align="right">1,069,560</td>
<td align="right">0.1%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">40,317,901</td>
<td align="right"></td>
<td align="right">38,612,031</td>
<td align="right"></td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">2,712,121,506</td>
<td align="right">23.1%</td>
<td align="right">2,824,824,644</td>
<td align="right">24.2%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">42,343,963</td>
<td align="right"></td>
<td align="right">40,620,875</td>
<td align="right"></td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">2,731,348,558</td>
<td align="right">21.6%</td>
<td align="right">2,774,157,027</td>
<td align="right">22.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">765,951,740</td>
<td align="right">69.6%</td>
<td align="right">775,001,900</td>
<td align="right">69.9%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">764,484,580</td>
<td align="right">69.5%</td>
<td align="right">773,465,400</td>
<td align="right">69.8%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">807,036,061</td>
<td align="right"></td>
<td align="right">815,963,614</td>
<td align="right"></td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,835,884</td>
<td align="right"></td>
<td align="right">2,818,155</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">256,985,416</td>
<td align="right"></td>
<td align="right">255,579,105</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">612,073,939</td>
<td align="right"></td>
<td align="right">609,227,949</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">465,840</td>
<td align="right">0.0%</td>
<td align="right">466,940</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">333,827,720</td>
<td align="right"></td>
<td align="right">333,777,220</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">333,805,520</td>
<td align="right">30.4%</td>
<td align="right">333,758,080</td>
<td align="right">30.1%</td>
<td align="right">-0.0%</td>
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
<td align="right">34,840</td>
<td align="right">93,560,880</td>
<td align="right">1,876,076,280</td>
<td align="right">34,840</td>
<td align="right">93,445,360</td>
<td align="right">1,878,293,400</td>
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
<td align="right">205,300</td>
<td align="right">35.5%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,720</td>
<td align="right">0.3%</td>
<td align="right">2,860</td>
<td align="right">0.5%</td>
<td align="right">66.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">166,120</td>
<td align="right">28.7%</td>
<td align="right">73,380</td>
<td align="right">12.5%</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,120</td>
<td align="right">1.1%</td>
<td align="right">8,320</td>
<td align="right">1.4%</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">410,080</td>
<td align="right">71.0%</td>
<td align="right">511,500</td>
<td align="right">87.0%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">10,460</td>
<td align="right">1.8%</td>
<td align="right">12,600</td>
<td align="right">2.1%</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">11,142,887,360</td>
<td align="right">1,277.4%</td>
<td align="right">13,192,391,740</td>
<td align="right">1,347.7%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">872,282,800</td>
<td align="right"></td>
<td align="right">978,855,060</td>
<td align="right"></td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,320</td>
<td align="right">0.2%</td>
<td align="right">1,380</td>
<td align="right">0.2%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">577,920</td>
<td align="right"></td>
<td align="right">587,740</td>
<td align="right"></td>
<td align="right">1.7%</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
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
<td align="right">396,900</td>
<td align="right">96.8%</td>
<td align="right">497,200</td>
<td align="right">97.2%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">410,080</td>
<td align="right"></td>
<td align="right">511,500</td>
<td align="right"></td>
<td align="right">24.7%</td>
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
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.0%</td>
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
<td align="right">18,200</td>
<td align="right">4.4%</td>
<td align="right">26,940</td>
<td align="right">5.3%</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">59,840</td>
<td align="right">14.6%</td>
<td align="right">67,740</td>
<td align="right">13.2%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">138,560</td>
<td align="right">33.8%</td>
<td align="right">168,860</td>
<td align="right">33.0%</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">128,400</td>
<td align="right">31.3%</td>
<td align="right">155,560</td>
<td align="right">30.4%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">50,300</td>
<td align="right">12.3%</td>
<td align="right">71,780</td>
<td align="right">14.0%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">12,840</td>
<td align="right">3.1%</td>
<td align="right">18,060</td>
<td align="right">3.5%</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,940</td>
<td align="right">0.5%</td>
<td align="right">2,560</td>
<td align="right">0.5%</td>
<td align="right">32.0%</td>
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
<td align="right">11,380</td>
<td align="right">2.8%</td>
<td align="right">4,040</td>
<td align="right">0.8%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">38,700</td>
<td align="right">9.4%</td>
<td align="right">56,480</td>
<td align="right">11.0%</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">77,040</td>
<td align="right">18.8%</td>
<td align="right">92,720</td>
<td align="right">18.1%</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">162,440</td>
<td align="right">39.6%</td>
<td align="right">196,620</td>
<td align="right">38.4%</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">77,900</td>
<td align="right">19.0%</td>
<td align="right">107,440</td>
<td align="right">21.0%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">24,880</td>
<td align="right">6.1%</td>
<td align="right">32,640</td>
<td align="right">6.4%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,320</td>
<td align="right">1.1%</td>
<td align="right">6,880</td>
<td align="right">1.3%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">240</td>
<td align="right">0.1%</td>
<td align="right">380</td>
<td align="right">0.1%</td>
<td align="right">58.3%</td>
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
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">2,660</td>
<td align="right">720,480</td>
<td align="right">26,985.7%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">2,660</td>
<td align="right">720,480</td>
<td align="right">26,985.7%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">920</td>
<td align="right">23,760</td>
<td align="right">2,482.6%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">9,320</td>
<td align="right">172,520</td>
<td align="right">1,751.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">39,660</td>
<td align="right">513,040</td>
<td align="right">1,193.6%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">404,300</td>
<td align="right">4,124,800</td>
<td align="right">920.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">16,931,000</td>
<td align="right">155,392,600</td>
<td align="right">817.8%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">706,100</td>
<td align="right">5,199,020</td>
<td align="right">636.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,500</td>
<td align="right">17,380</td>
<td align="right">595.2%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,891,740</td>
<td align="right">11,037,420</td>
<td align="right">483.5%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,892,460</td>
<td align="right">11,038,140</td>
<td align="right">483.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">5,175,260</td>
<td align="right">30,080,400</td>
<td align="right">481.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,106,920</td>
<td align="right">9,268,260</td>
<td align="right">339.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,379,380</td>
<td align="right">9,487,880</td>
<td align="right">298.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,952,720</td>
<td align="right">7,621,540</td>
<td align="right">290.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">3,549,780</td>
<td align="right">13,403,820</td>
<td align="right">277.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,549,780</td>
<td align="right">13,403,820</td>
<td align="right">277.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,356,500</td>
<td align="right">4,955,700</td>
<td align="right">265.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">150,680</td>
<td align="right">485,460</td>
<td align="right">222.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">150,680</td>
<td align="right">485,460</td>
<td align="right">222.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">10,237,780</td>
<td align="right">29,853,240</td>
<td align="right">191.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">66,214,120</td>
<td align="right">189,643,940</td>
<td align="right">186.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">1,620</td>
<td align="right">4,240</td>
<td align="right">161.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">306,440</td>
<td align="right">711,760</td>
<td align="right">132.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">306,440</td>
<td align="right">711,760</td>
<td align="right">132.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">650,160</td>
<td align="right">1,440,940</td>
<td align="right">121.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">18,906,100</td>
<td align="right">40,362,780</td>
<td align="right">113.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">297,980</td>
<td align="right">606,880</td>
<td align="right">103.7%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">301,980</td>
<td align="right">613,680</td>
<td align="right">103.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">6,531,160</td>
<td align="right">12,861,280</td>
<td align="right">96.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">8,678,640</td>
<td align="right">16,920,960</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">9,510,580</td>
<td align="right">18,276,640</td>
<td align="right">92.2%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">284,940</td>
<td align="right">547,120</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">103,509,660</td>
<td align="right">192,001,580</td>
<td align="right">85.5%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">152,440</td>
<td align="right">280,580</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">51,940</td>
<td align="right">93,420</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">7,055,280</td>
<td align="right">12,471,680</td>
<td align="right">76.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">340,540</td>
<td align="right">595,860</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">2,986,860</td>
<td align="right">5,185,520</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">7,183,460</td>
<td align="right">12,279,220</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">9,810,260</td>
<td align="right">16,724,600</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">2,235,140</td>
<td align="right">3,795,620</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">60,348,140</td>
<td align="right">102,060,160</td>
<td align="right">69.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">55,500</td>
<td align="right">89,920</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">8,621,140</td>
<td align="right">13,958,740</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">2,979,460</td>
<td align="right">4,808,800</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">2,977,140</td>
<td align="right">4,804,780</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">22,605,860</td>
<td align="right">35,018,880</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">982,380</td>
<td align="right">449,660</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">51,859,760</td>
<td align="right">79,781,460</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,272,340</td>
<td align="right">1,953,780</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">13,937,300</td>
<td align="right">21,226,140</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">127,512,580</td>
<td align="right">192,476,680</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">48,707,900</td>
<td align="right">73,053,180</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">19,671,140</td>
<td align="right">29,423,080</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">88,853,060</td>
<td align="right">132,436,760</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">2,260</td>
<td align="right">3,360</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">1,167,320</td>
<td align="right">1,712,320</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">22,951,580</td>
<td align="right">33,656,860</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">64,943,480</td>
<td align="right">95,106,160</td>
<td align="right">46.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">53,924,220</td>
<td align="right">77,550,640</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">6,299,120</td>
<td align="right">8,997,060</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">260,640</td>
<td align="right">154,680</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">64,091,040</td>
<td align="right">89,903,280</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">34,687,640</td>
<td align="right">48,136,620</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">49,924,460</td>
<td align="right">68,817,260</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">68,393,620</td>
<td align="right">94,046,260</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">5,676,620</td>
<td align="right">7,785,540</td>
<td align="right">37.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">8,314,500</td>
<td align="right">11,323,340</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">162,399,160</td>
<td align="right">217,140,740</td>
<td align="right">33.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">119,574,960</td>
<td align="right">158,798,420</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">8,082,540</td>
<td align="right">10,722,000</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">16,099,200</td>
<td align="right">21,315,620</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">3,169,560</td>
<td align="right">4,195,180</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">11,382,700</td>
<td align="right">15,026,480</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">1,598,800</td>
<td align="right">2,097,480</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">5,348,500</td>
<td align="right">6,987,260</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">2,725,980</td>
<td align="right">3,525,560</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">25,138,600</td>
<td align="right">32,253,940</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">48,042,900</td>
<td align="right">61,548,540</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">652,080</td>
<td align="right">835,180</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">338,549,900</td>
<td align="right">430,561,600</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">9,316,180</td>
<td align="right">11,780,660</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">534,200</td>
<td align="right">670,900</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">12,933,500</td>
<td align="right">16,106,500</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">410,160</td>
<td align="right">309,600</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">75,537,920</td>
<td align="right">93,803,100</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">9,620,920</td>
<td align="right">11,918,520</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">13,123,680</td>
<td align="right">16,244,700</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">213,120,100</td>
<td align="right">262,896,660</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">433,660</td>
<td align="right">333,460</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">691,020</td>
<td align="right">849,140</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">22,368,120</td>
<td align="right">27,341,900</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">147,569,800</td>
<td align="right">179,591,780</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">147,558,280</td>
<td align="right">179,571,180</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">1,117,080</td>
<td align="right">1,344,020</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,641,460</td>
<td align="right">3,715,420</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">82,952,080</td>
<td align="right">99,107,180</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">9,172,840</td>
<td align="right">10,889,400</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">110,949,600</td>
<td align="right">131,323,600</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">118,721,240</td>
<td align="right">140,124,980</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">50,149,260</td>
<td align="right">41,468,980</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,906,200</td>
<td align="right">2,226,020</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">13,973,540</td>
<td align="right">16,281,280</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">908,008,120</td>
<td align="right">1,055,901,160</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">2,671,080</td>
<td align="right">3,096,600</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">118,511,380</td>
<td align="right">137,236,200</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">20,941,920</td>
<td align="right">24,240,100</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">7,688,720</td>
<td align="right">8,891,540</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">22,222,580</td>
<td align="right">25,612,380</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">22,222,580</td>
<td align="right">25,612,380</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">84,967,880</td>
<td align="right">97,549,560</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">726,718,440</td>
<td align="right">829,289,860</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">123,491,020</td>
<td align="right">140,697,740</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">54,371,700</td>
<td align="right">61,910,920</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">5,269,500</td>
<td align="right">5,988,780</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">766,403,140</td>
<td align="right">870,393,680</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">12,298,400</td>
<td align="right">10,765,800</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">872,282,800</td>
<td align="right">978,855,060</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">132,601,260</td>
<td align="right">148,202,300</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">17,429,880</td>
<td align="right">19,475,420</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">17,527,600</td>
<td align="right">19,572,220</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">35,223,600</td>
<td align="right">39,244,440</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">46,925,420</td>
<td align="right">52,265,600</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">40,749,660</td>
<td align="right">45,308,700</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">25,377,120</td>
<td align="right">28,213,980</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">937,747,300</td>
<td align="right">1,041,205,160</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">207,034,840</td>
<td align="right">229,744,180</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">1,315,640</td>
<td align="right">1,450,920</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">1,315,640</td>
<td align="right">1,450,920</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">82,701,220</td>
<td align="right">90,772,740</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">354,420</td>
<td align="right">387,100</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">72,805,620</td>
<td align="right">66,175,280</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">59,106,520</td>
<td align="right">64,469,640</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">53,084,080</td>
<td align="right">57,882,720</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">20,188,860</td>
<td align="right">21,971,760</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">365,660</td>
<td align="right">395,740</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">52,646,600</td>
<td align="right">56,801,820</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">148,260</td>
<td align="right">159,960</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">545,760</td>
<td align="right">587,380</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">85,013,500</td>
<td align="right">89,716,420</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">2,194,780</td>
<td align="right">2,313,620</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">167,149,740</td>
<td align="right">158,402,960</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">65,464,500</td>
<td align="right">62,350,100</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">279,900</td>
<td align="right">293,000</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">34,643,620</td>
<td align="right">36,225,620</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">51,096,420</td>
<td align="right">48,862,920</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">22,840,560</td>
<td align="right">23,833,860</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">599,160</td>
<td align="right">625,160</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">87,810,000</td>
<td align="right">84,286,880</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">60,480,740</td>
<td align="right">62,896,780</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">5,398,280</td>
<td align="right">5,613,560</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">45,446,900</td>
<td align="right">43,688,620</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">146,968,220</td>
<td align="right">141,435,680</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">100,385,520</td>
<td align="right">103,852,500</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">10,211,200</td>
<td align="right">9,868,760</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">10,313,140</td>
<td align="right">10,024,400</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">16,308,440</td>
<td align="right">16,763,020</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">59,980,960</td>
<td align="right">61,609,920</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">4,086,840</td>
<td align="right">4,187,220</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">142,201,340</td>
<td align="right">138,724,360</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">796,491,860</td>
<td align="right">777,275,780</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">18,453,940</td>
<td align="right">18,892,540</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">4,581,260</td>
<td align="right">4,680,520</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">4,581,260</td>
<td align="right">4,680,520</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">19,049,000</td>
<td align="right">19,427,480</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">382,577,740</td>
<td align="right">390,015,700</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">63,364,140</td>
<td align="right">64,284,740</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">210,860,680</td>
<td align="right">207,977,580</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">2,644,500</td>
<td align="right">2,666,180</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">24,921,700</td>
<td align="right">25,060,500</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,283,160</td>
<td align="right">1,286,560</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">497,680</td>
<td align="right">498,640</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">22,920,760</td>
<td align="right">22,919,820</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">96,140</td>
<td align="right">96,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">10,580</td>
<td align="right">10,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">8,320</td>
<td align="right">8,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">3,920</td>
<td align="right">3,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">2,660</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">2,220</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">620</td>
<td align="right">620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">620</td>
<td align="right">620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">600</td>
<td align="right">600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">600</td>
<td align="right">600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">8,913,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">253,320</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">177,420</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">120,880</td>
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
<td align="right">7,720</td>
<td align="right">21,060</td>
<td align="right">172.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">2,000</td>
<td align="right">3,620</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">16,600</td>
<td align="right">28,480</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right"></td>
<td align="right">2,180</td>
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
<td align="right">60</td>
<td align="right">60</td>
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
<td align="right">60</td>
<td align="right">60</td>
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
