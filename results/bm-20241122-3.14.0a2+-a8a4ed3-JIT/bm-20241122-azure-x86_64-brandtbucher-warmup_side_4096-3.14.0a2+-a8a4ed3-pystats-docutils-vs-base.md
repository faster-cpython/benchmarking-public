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
<td align="left">STORE_SLICE</td>
<td align="right">139,260</td>
<td align="right">267,120</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">32,978,340</td>
<td align="right">53,838,480</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,150,120</td>
<td align="right">4,840,120</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">237,400</td>
<td align="right">361,260</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">936,900</td>
<td align="right">1,423,280</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">5,731,320</td>
<td align="right">8,268,420</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">12,616,700</td>
<td align="right">17,706,460</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">15,776,260</td>
<td align="right">21,048,940</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,021,200</td>
<td align="right">3,890,900</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">13,803,960</td>
<td align="right">17,484,600</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">4,399,400</td>
<td align="right">3,302,560</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,568,340</td>
<td align="right">50,196,540</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">32,355,280</td>
<td align="right">38,756,280</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">9,072,520</td>
<td align="right">10,783,380</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,592,400</td>
<td align="right">1,885,920</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">574,320</td>
<td align="right">672,060</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">166,235,680</td>
<td align="right">194,279,080</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">44,074,560</td>
<td align="right">51,450,800</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">80,816,120</td>
<td align="right">94,168,540</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">66,159,780</td>
<td align="right">55,648,760</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">272,078,900</td>
<td align="right">314,536,400</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">147,047,360</td>
<td align="right">169,337,040</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">20,963,160</td>
<td align="right">24,007,340</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">42,435,240</td>
<td align="right">48,365,980</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">125,534,240</td>
<td align="right">108,093,160</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">738,260</td>
<td align="right">840,600</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">184,398,920</td>
<td align="right">207,895,280</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">261,342,140</td>
<td align="right">293,715,220</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">34,567,860</td>
<td align="right">38,610,420</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">8,004,900</td>
<td align="right">8,901,840</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">269,397,400</td>
<td align="right">299,258,640</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">63,255,060</td>
<td align="right">70,075,380</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,594,520</td>
<td align="right">2,874,000</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">60,272,840</td>
<td align="right">66,647,880</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">111,582,860</td>
<td align="right">122,743,820</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,951,420</td>
<td align="right">5,440,660</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,850,540</td>
<td align="right">5,322,120</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,231,400</td>
<td align="right">2,448,340</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">24,171,460</td>
<td align="right">26,471,680</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,225,860</td>
<td align="right">5,719,020</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">24,059,740</td>
<td align="right">26,195,160</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,828,660</td>
<td align="right">1,677,240</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,273,279,760</td>
<td align="right">1,377,999,040</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,198,620</td>
<td align="right">9,904,520</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">309,300,160</td>
<td align="right">332,294,960</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,563,020</td>
<td align="right">7,001,660</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,777,920</td>
<td align="right">35,088,800</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">8,370,280</td>
<td align="right">7,785,080</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">209,250,180</td>
<td align="right">223,536,660</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">12,521,080</td>
<td align="right">13,362,100</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">76,060,600</td>
<td align="right">80,810,380</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">97,447,720</td>
<td align="right">103,517,980</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">71,270,320</td>
<td align="right">75,650,920</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">19,708,120</td>
<td align="right">20,817,680</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">115,988,740</td>
<td align="right">122,395,600</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,025,580</td>
<td align="right">17,949,340</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">14,934,980</td>
<td align="right">15,736,960</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">225,588,160</td>
<td align="right">237,378,420</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,060,560</td>
<td align="right">3,220,200</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">145,583,000</td>
<td align="right">153,093,300</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">117,222,800</td>
<td align="right">123,268,300</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">194,250,500</td>
<td align="right">203,509,820</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,015,120</td>
<td align="right">10,472,740</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">19,688,840</td>
<td align="right">20,563,820</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">7,419,740</td>
<td align="right">7,742,940</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">47,302,460</td>
<td align="right">49,359,500</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">7,347,360</td>
<td align="right">7,034,660</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">26,568,560</td>
<td align="right">27,566,120</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,814,780</td>
<td align="right">17,402,240</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">37,261,340</td>
<td align="right">38,533,780</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">45,030,320</td>
<td align="right">46,562,480</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">25,636,340</td>
<td align="right">24,777,580</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">18,775,240</td>
<td align="right">19,375,020</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,394,400</td>
<td align="right">5,228,080</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">16,431,100</td>
<td align="right">15,958,580</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">63,591,400</td>
<td align="right">65,338,780</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,693,620</td>
<td align="right">2,620,720</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,194,020</td>
<td align="right">10,465,460</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,069,700</td>
<td align="right">11,362,660</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">42,886,480</td>
<td align="right">44,003,940</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">9,778,340</td>
<td align="right">10,009,760</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,193,380</td>
<td align="right">1,220,320</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">18,287,560</td>
<td align="right">17,887,120</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,108,040</td>
<td align="right">4,193,640</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,446,920</td>
<td align="right">39,102,680</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">29,574,140</td>
<td align="right">30,070,800</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">29,575,520</td>
<td align="right">30,072,180</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">14,854,000</td>
<td align="right">15,100,320</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">18,999,200</td>
<td align="right">19,311,420</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">11,872,540</td>
<td align="right">12,020,480</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">435,380</td>
<td align="right">440,340</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">22,641,640</td>
<td align="right">22,888,280</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,770,580</td>
<td align="right">2,746,040</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">76,804,060</td>
<td align="right">77,466,160</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">5,770,880</td>
<td align="right">5,801,620</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">306,697,620</td>
<td align="right">308,104,280</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">28,977,840</td>
<td align="right">29,066,860</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,805,940</td>
<td align="right">39,718,500</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,922,320</td>
<td align="right">1,925,660</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">39,862,580</td>
<td align="right">39,909,080</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,572,760</td>
<td align="right">5,576,740</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">739,740</td>
<td align="right">740,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,426,380</td>
<td align="right">3,425,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">853,440</td>
<td align="right">853,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,540,300</td>
<td align="right">16,539,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,949,900</td>
<td align="right">91,944,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,607,460</td>
<td align="right">8,607,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,114,500</td>
<td align="right">37,114,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">36,886,980</td>
<td align="right">36,886,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">11,627,520</td>
<td align="right">11,627,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">7,613,400</td>
<td align="right">7,613,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,146,540</td>
<td align="right">7,146,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">6,134,760</td>
<td align="right">6,134,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">6,134,760</td>
<td align="right">6,134,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">5,778,660</td>
<td align="right">5,778,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,951,860</td>
<td align="right">4,951,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,587,740</td>
<td align="right">4,587,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,731,500</td>
<td align="right">2,731,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,728,440</td>
<td align="right">2,728,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,413,900</td>
<td align="right">1,413,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,175,460</td>
<td align="right">1,175,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">724,200</td>
<td align="right">724,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">332,160</td>
<td align="right">332,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">230,880</td>
<td align="right">230,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">228,720</td>
<td align="right">228,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">176,880</td>
<td align="right">176,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">156,900</td>
<td align="right">156,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">145,320</td>
<td align="right">145,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">91,560</td>
<td align="right">91,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">75,960</td>
<td align="right">75,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">73,620</td>
<td align="right">73,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">61,740</td>
<td align="right">61,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">61,560</td>
<td align="right">61,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">49,980</td>
<td align="right">49,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">27,480</td>
<td align="right">27,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">16,860</td>
<td align="right">16,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">14,640</td>
<td align="right">14,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,400</td>
<td align="right">11,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8,820</td>
<td align="right">8,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">7,260</td>
<td align="right">7,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">4,740</td>
<td align="right">4,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,000</td>
<td align="right">4,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,420</td>
<td align="right">3,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">3,360</td>
<td align="right">3,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">1,440</td>
<td align="right">1,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">780</td>
<td align="right">780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">60</td>
<td align="right">60</td>
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
<td align="right">15,765,340</td>
<td align="right">24.6%</td>
<td align="right">21,036,720</td>
<td align="right">30.3%</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">48,411,720</td>
<td align="right">75.4%</td>
<td align="right">48,411,720</td>
<td align="right">69.7%</td>
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
<td align="right">10,720</td>
<td align="right">100.0%</td>
<td align="right">12,020</td>
<td align="right">100.0%</td>
<td align="right">12.1%</td>
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
<td align="left">remainder</td>
<td align="right">3,680</td>
<td align="right">34.3%</td>
<td align="right">4,980</td>
<td align="right">41.4%</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,200</td>
<td align="right">29.9%</td>
<td align="right">3,200</td>
<td align="right">26.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">29.5%</td>
<td align="right">3,160</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">320</td>
<td align="right">3.0%</td>
<td align="right">320</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">180</td>
<td align="right">1.7%</td>
<td align="right">180</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">160</td>
<td align="right">1.5%</td>
<td align="right">160</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">9,072,520</td>
<td align="right">100.0%</td>
<td align="right">10,783,380</td>
<td align="right">100.0%</td>
<td align="right">18.9%</td>
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
<td align="right">10,182,180</td>
<td align="right">9.6%</td>
<td align="right">10,453,700</td>
<td align="right">9.8%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,159,340</td>
<td align="right">2.0%</td>
<td align="right">2,162,220</td>
<td align="right">2.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">93,973,720</td>
<td align="right">88.4%</td>
<td align="right">93,973,260</td>
<td align="right">88.2%</td>
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
<td align="right">11,220</td>
<td align="right">21.3%</td>
<td align="right">11,140</td>
<td align="right">21.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,340</td>
<td align="right">78.7%</td>
<td align="right">41,380</td>
<td align="right">78.8%</td>
<td align="right">0.1%</td>
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
<td align="right">1,680</td>
<td align="right">15.0%</td>
<td align="right">1,740</td>
<td align="right">15.6%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">7,960</td>
<td align="right">70.9%</td>
<td align="right">7,820</td>
<td align="right">70.2%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">720</td>
<td align="right">6.4%</td>
<td align="right">720</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">680</td>
<td align="right">6.1%</td>
<td align="right">680</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">1.6%</td>
<td align="right">180</td>
<td align="right">1.6%</td>
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
<td align="right">17,155,900</td>
<td align="right">3.0%</td>
<td align="right">17,565,640</td>
<td align="right">3.1%</td>
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
<td align="right">554,145,480</td>
<td align="right">97.0%</td>
<td align="right">553,273,660</td>
<td align="right">96.9%</td>
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
<td align="right">327,720</td>
<td align="right">100.0%</td>
<td align="right">335,460</td>
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
<td align="right">160</td>
<td align="right">160 / 0 !!</td>
<td align="right">160</td>
<td align="right">160 / 0 !!</td>
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
<td align="right">111,820</td>
<td align="right">0.3%</td>
<td align="right">259,420</td>
<td align="right">0.7%</td>
<td align="right">132.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,822,120</td>
<td align="right">5.0%</td>
<td align="right">1,663,960</td>
<td align="right">4.5%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,684,700</td>
<td align="right">94.7%</td>
<td align="right">34,778,780</td>
<td align="right">94.7%</td>
<td align="right">0.3%</td>
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
<td align="right">2,420</td>
<td align="right">28.0%</td>
<td align="right">5,220</td>
<td align="right">28.7%</td>
<td align="right">115.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,220</td>
<td align="right">72.0%</td>
<td align="right">12,940</td>
<td align="right">71.3%</td>
<td align="right">108.0%</td>
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
<td align="right">5,760</td>
<td align="right">92.6%</td>
<td align="right">12,480</td>
<td align="right">96.4%</td>
<td align="right">116.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">3.2%</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">80</td>
<td align="right">1.3%</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">80</td>
<td align="right">1.3%</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">20</td>
<td align="right">0.3%</td>
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
<td align="right">8,000,240</td>
<td align="right">12.8%</td>
<td align="right">8,896,960</td>
<td align="right">14.1%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">54,350,400</td>
<td align="right">87.2%</td>
<td align="right">54,350,400</td>
<td align="right">85.9%</td>
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
<td align="right">4,540</td>
<td align="right">100.0%</td>
<td align="right">4,760</td>
<td align="right">100.0%</td>
<td align="right">4.8%</td>
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
<td align="right">960</td>
<td align="right">21.1%</td>
<td align="right">1,180</td>
<td align="right">24.8%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,880</td>
<td align="right">41.4%</td>
<td align="right">1,880</td>
<td align="right">39.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">900</td>
<td align="right">19.8%</td>
<td align="right">900</td>
<td align="right">18.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">17.6%</td>
<td align="right">800</td>
<td align="right">16.8%</td>
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
<td align="right">20,493,120</td>
<td align="right">11.8%</td>
<td align="right">26,954,040</td>
<td align="right">14.7%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">25,629,220</td>
<td align="right">14.8%</td>
<td align="right">24,770,720</td>
<td align="right">13.5%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">127,525,920</td>
<td align="right">73.4%</td>
<td align="right">131,773,700</td>
<td align="right">71.8%</td>
<td align="right">3.3%</td>
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
<td align="right">386,640</td>
<td align="right">98.2%</td>
<td align="right">508,560</td>
<td align="right">98.7%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,120</td>
<td align="right">1.8%</td>
<td align="right">6,860</td>
<td align="right">1.3%</td>
<td align="right">-3.7%</td>
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
<td align="right">720</td>
<td align="right">10.1%</td>
<td align="right">580</td>
<td align="right">8.5%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,620</td>
<td align="right">22.8%</td>
<td align="right">1,420</td>
<td align="right">20.7%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,420</td>
<td align="right">34.0%</td>
<td align="right">2,480</td>
<td align="right">36.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,020</td>
<td align="right">14.3%</td>
<td align="right">1,040</td>
<td align="right">15.2%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">560</td>
<td align="right">7.9%</td>
<td align="right">560</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">400</td>
<td align="right">5.6%</td>
<td align="right">400</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">220</td>
<td align="right">3.1%</td>
<td align="right">220</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">0.6%</td>
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
<td align="right">235,278,540</td>
<td align="right">23.8%</td>
<td align="right">277,432,260</td>
<td align="right">26.7%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">96,790,420</td>
<td align="right">9.8%</td>
<td align="right">102,860,700</td>
<td align="right">9.9%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">653,870,300</td>
<td align="right">66.3%</td>
<td align="right">657,402,320</td>
<td align="right">63.3%</td>
<td align="right">0.5%</td>
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
<td align="right">5,077,100</td>
<td align="right">99.6%</td>
<td align="right">5,870,940</td>
<td align="right">99.7%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">18,960</td>
<td align="right">0.4%</td>
<td align="right">20,500</td>
<td align="right">0.3%</td>
<td align="right">8.1%</td>
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
<td align="right">8,720</td>
<td align="right">46.0%</td>
<td align="right">10,120</td>
<td align="right">49.4%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,040</td>
<td align="right">26.6%</td>
<td align="right">5,180</td>
<td align="right">25.3%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2,840</td>
<td align="right">15.0%</td>
<td align="right">2,840</td>
<td align="right">13.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">640</td>
<td align="right">3.4%</td>
<td align="right">640</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">2.2%</td>
<td align="right">420</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">2.1%</td>
<td align="right">400</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">240</td>
<td align="right">1.3%</td>
<td align="right">240</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
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
<td align="right">271,052,420</td>
<td align="right">100.0%</td>
<td align="right">280,973,840</td>
<td align="right">100.0%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,140</td>
<td align="right">0.0%</td>
<td align="right">2,140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">75,960</td>
<td align="right">100.0%</td>
<td align="right">75,960</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">7,260</td>
<td align="right">100.0%</td>
<td align="right">7,260</td>
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
<td align="right">16,802,720</td>
<td align="right">14.3%</td>
<td align="right">17,390,020</td>
<td align="right">14.7%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,659,880</td>
<td align="right">45.6%</td>
<td align="right">53,915,360</td>
<td align="right">45.6%</td>
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
<td align="right">47,130,600</td>
<td align="right">40.1%</td>
<td align="right">47,039,540</td>
<td align="right">39.7%</td>
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
<td align="left">Failure</td>
<td align="right">11,660</td>
<td align="right">1.1%</td>
<td align="right">11,820</td>
<td align="right">1.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,012,980</td>
<td align="right">98.9%</td>
<td align="right">1,017,800</td>
<td align="right">98.9%</td>
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
<td align="left">class attr simple</td>
<td align="right">9,020</td>
<td align="right">77.4%</td>
<td align="right">9,180</td>
<td align="right">77.7%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">17.5%</td>
<td align="right">2,040</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">360</td>
<td align="right">3.1%</td>
<td align="right">360</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">200</td>
<td align="right">1.7%</td>
<td align="right">200</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">139,260</td>
<td align="right">100.0%</td>
<td align="right">267,120</td>
<td align="right">100.0%</td>
<td align="right">91.8%</td>
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
<td align="right">4,583,860</td>
<td align="right">9.7%</td>
<td align="right">4,583,860</td>
<td align="right">9.7%</td>
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
<td align="right">42,562,200</td>
<td align="right">90.3%</td>
<td align="right">42,562,200</td>
<td align="right">90.3%</td>
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
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">2,220</td>
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
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,760</td>
<td align="right">95.9%</td>
<td align="right">3,760</td>
<td align="right">95.9%</td>
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
<td align="right">2,440</td>
<td align="right">64.9%</td>
<td align="right">2,440</td>
<td align="right">64.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">220</td>
<td align="right">5.9%</td>
<td align="right">220</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right">40</td>
<td align="right">1.1%</td>
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
<td align="right">6,396,340</td>
<td align="right">2.3%</td>
<td align="right">9,602,720</td>
<td align="right">3.4%</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,931,020</td>
<td align="right">1.0%</td>
<td align="right">3,736,860</td>
<td align="right">1.3%</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">269,748,660</td>
<td align="right">96.6%</td>
<td align="right">267,030,020</td>
<td align="right">95.2%</td>
<td align="right">-1.0%</td>
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
<td align="right">89,320</td>
<td align="right">100.0%</td>
<td align="right">153,180</td>
<td align="right">100.0%</td>
<td align="right">71.5%</td>
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
<td align="left">number</td>
<td align="right">44,100</td>
<td align="right">49.4%</td>
<td align="right">107,920</td>
<td align="right">70.5%</td>
<td align="right">144.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,180</td>
<td align="right">1.3%</td>
<td align="right">1,200</td>
<td align="right">0.8%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,340</td>
<td align="right">2.6%</td>
<td align="right">2,360</td>
<td align="right">1.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">41,540</td>
<td align="right">46.5%</td>
<td align="right">41,540</td>
<td align="right">27.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">0.2%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
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
<td align="right">48,290,020</td>
<td align="right">100.0%</td>
<td align="right">48,290,020</td>
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
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">3,700</td>
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
<td align="right">380</td>
<td align="right">100.0%</td>
<td align="right">380</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">335,271,500</td>
<td align="right">5.1%</td>
<td align="right">387,906,760</td>
<td align="right">5.5%</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">2,409,248,640</td>
<td align="right">36.8%</td>
<td align="right">2,627,277,700</td>
<td align="right">37.3%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">192,529,920</td>
<td align="right">2.9%</td>
<td align="right">207,326,940</td>
<td align="right">2.9%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,611,882,780</td>
<td align="right">55.2%</td>
<td align="right">3,818,941,020</td>
<td align="right">54.2%</td>
<td align="right">5.7%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">15,765,340</td>
<td align="right">8.2%</td>
<td align="right">21,036,720</td>
<td align="right">10.2%</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,931,020</td>
<td align="right">1.5%</td>
<td align="right">3,736,860</td>
<td align="right">1.8%</td>
<td align="right">27.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">9,072,520</td>
<td align="right">4.7%</td>
<td align="right">10,783,380</td>
<td align="right">5.2%</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">8,000,240</td>
<td align="right">4.2%</td>
<td align="right">8,896,960</td>
<td align="right">4.3%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,822,120</td>
<td align="right">1.0%</td>
<td align="right">1,663,960</td>
<td align="right">0.8%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">96,790,420</td>
<td align="right">50.5%</td>
<td align="right">102,860,700</td>
<td align="right">49.8%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,802,720</td>
<td align="right">8.8%</td>
<td align="right">17,390,020</td>
<td align="right">8.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">25,629,220</td>
<td align="right">13.4%</td>
<td align="right">24,770,720</td>
<td align="right">12.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,182,180</td>
<td align="right">5.3%</td>
<td align="right">10,453,700</td>
<td align="right">5.1%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,583,860</td>
<td align="right">2.4%</td>
<td align="right">4,583,860</td>
<td align="right">2.2%</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">10,246,020</td>
<td align="right">3.1%</td>
<td align="right">13,476,540</td>
<td align="right">3.5%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">10,247,100</td>
<td align="right">3.1%</td>
<td align="right">13,477,500</td>
<td align="right">3.5%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">64,572,380</td>
<td align="right">19.3%</td>
<td align="right">82,061,320</td>
<td align="right">21.2%</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">86,805,440</td>
<td align="right">25.9%</td>
<td align="right">102,778,060</td>
<td align="right">26.5%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">28,766,480</td>
<td align="right">8.6%</td>
<td align="right">33,233,300</td>
<td align="right">8.6%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">46,850,600</td>
<td align="right">14.0%</td>
<td align="right">51,067,140</td>
<td align="right">13.2%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">5,940,100</td>
<td align="right">1.8%</td>
<td align="right">5,541,500</td>
<td align="right">1.4%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,588,700</td>
<td align="right">2.9%</td>
<td align="right">9,535,120</td>
<td align="right">2.5%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,656,700</td>
<td align="right">16.0%</td>
<td align="right">53,912,180</td>
<td align="right">13.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,003,520</td>
<td align="right">1.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">5,016,560</td>
<td align="right">1.3%</td>
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
<td align="right">8,289,100</td>
<td align="right">2.3%</td>
<td align="right">8,971,800</td>
<td align="right">2.5%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,177,540</td>
<td align="right">11.1%</td>
<td align="right">39,833,300</td>
<td align="right">11.2%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,181,020</td>
<td align="right">11.1%</td>
<td align="right">39,836,780</td>
<td align="right">11.2%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,488,880</td>
<td align="right">11.1%</td>
<td align="right">40,144,640</td>
<td align="right">11.3%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,488,880</td>
<td align="right">11.1%</td>
<td align="right">40,144,640</td>
<td align="right">11.3%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">314,907,480</td>
<td align="right">88.9%</td>
<td align="right">314,251,720</td>
<td align="right">88.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,574,800</td>
<td align="right">88.5%</td>
<td align="right">313,601,740</td>
<td align="right">88.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">307,860</td>
<td align="right">0.1%</td>
<td align="right">307,860</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,420</td>
<td align="right">0.0%</td>
<td align="right">3,420</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">13,629,240</td>
<td align="right">3.8%</td>
<td align="right">13,629,240</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,826,760</td>
<td align="right">0.5%</td>
<td align="right">1,826,760</td>
<td align="right">0.5%</td>
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
<td align="right">9,598,380</td>
<td align="right">2.7%</td>
<td align="right">9,598,380</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">1,811,606</td>
<td align="right"></td>
<td align="right">1,506,620</td>
<td align="right"></td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">3,053,247,884</td>
<td align="right">36.8%</td>
<td align="right">2,712,979,318</td>
<td align="right">33.4%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,788,765,690</td>
<td align="right">30.2%</td>
<td align="right">2,482,223,143</td>
<td align="right">27.6%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">36,059,668</td>
<td align="right"></td>
<td align="right">32,658,073</td>
<td align="right"></td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">35,008,695</td>
<td align="right"></td>
<td align="right">31,912,835</td>
<td align="right"></td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">673,828,940</td>
<td align="right">8.1%</td>
<td align="right">728,322,480</td>
<td align="right">9.0%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">534,760</td>
<td align="right">0.1%</td>
<td align="right">499,520</td>
<td align="right">0.1%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,744,628,940</td>
<td align="right">33.1%</td>
<td align="right">2,916,851,860</td>
<td align="right">35.9%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,778,870,056</td>
<td align="right">19.3%</td>
<td align="right">1,686,724,627</td>
<td align="right">18.7%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,050,897,520</td>
<td align="right">11.4%</td>
<td align="right">1,100,841,600</td>
<td align="right">12.2%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,600,596,360</td>
<td align="right">39.1%</td>
<td align="right">3,739,190,280</td>
<td align="right">41.5%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,825,658,900</td>
<td align="right">22.0%</td>
<td align="right">1,768,868,292</td>
<td align="right">21.8%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">197,538,874</td>
<td align="right"></td>
<td align="right">198,681,240</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">345,560</td>
<td align="right">0.1%</td>
<td align="right">344,480</td>
<td align="right">0.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">461,008,625</td>
<td align="right"></td>
<td align="right">460,232,825</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">236,957,900</td>
<td align="right">35.2%</td>
<td align="right">236,804,380</td>
<td align="right">35.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">236,942,280</td>
<td align="right"></td>
<td align="right">236,813,140</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">474,028,523</td>
<td align="right"></td>
<td align="right">474,270,927</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">436,244,640</td>
<td align="right">64.7%</td>
<td align="right">436,360,140</td>
<td align="right">64.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">437,124,960</td>
<td align="right">64.8%</td>
<td align="right">437,204,140</td>
<td align="right">64.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">10,534,200</td>
<td align="right"></td>
<td align="right">10,534,200</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">26,460</td>
<td align="right">0.3%</td>
<td align="right">26,460</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">119,040</td>
<td align="right">1.1%</td>
<td align="right">119,040</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
<td align="right">2,940</td>
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
<td align="right">25,860</td>
<td align="right">73,509,100</td>
<td align="right">1,491,920,122</td>
<td align="right">25,940</td>
<td align="right">73,539,740</td>
<td align="right">1,508,706,052</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">76,760</td>
<td align="right">49.9%</td>
<td align="right">11,100</td>
<td align="right">33.2%</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">85,840</td>
<td align="right">55.8%</td>
<td align="right">13,100</td>
<td align="right">39.2%</td>
<td align="right">-84.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,600</td>
<td align="right">1.0%</td>
<td align="right">280</td>
<td align="right">0.8%</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">620</td>
<td align="right">0.4%</td>
<td align="right">120</td>
<td align="right">0.4%</td>
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
<td align="right">153,700</td>
<td align="right"></td>
<td align="right">33,440</td>
<td align="right"></td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">76,420</td>
<td align="right">49.7%</td>
<td align="right">22,140</td>
<td align="right">66.2%</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">520</td>
<td align="right">0.3%</td>
<td align="right">200</td>
<td align="right">0.6%</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,980</td>
<td align="right">2.6%</td>
<td align="right">2,020</td>
<td align="right">6.0%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">480,422,140</td>
<td align="right"></td>
<td align="right">330,924,680</td>
<td align="right"></td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">5,451,816,480</td>
<td align="right">1,134.8%</td>
<td align="right">3,968,470,720</td>
<td align="right">1,199.2%</td>
<td align="right">-27.2%</td>
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
<td align="right">61,420</td>
<td align="right">80.4%</td>
<td align="right">15,320</td>
<td align="right">69.2%</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">76,420</td>
<td align="right"></td>
<td align="right">22,140</td>
<td align="right"></td>
<td align="right">-71.0%</td>
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
<td align="right">6,900</td>
<td align="right">9.0%</td>
<td align="right">1,120</td>
<td align="right">5.1%</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">13,320</td>
<td align="right">17.4%</td>
<td align="right">1,940</td>
<td align="right">8.8%</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">22,660</td>
<td align="right">29.7%</td>
<td align="right">7,240</td>
<td align="right">32.7%</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">17,040</td>
<td align="right">22.3%</td>
<td align="right">4,900</td>
<td align="right">22.1%</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">10,940</td>
<td align="right">14.3%</td>
<td align="right">4,120</td>
<td align="right">18.6%</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,520</td>
<td align="right">5.9%</td>
<td align="right">2,600</td>
<td align="right">11.7%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,020</td>
<td align="right">1.3%</td>
<td align="right">200</td>
<td align="right">0.9%</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right">320</td>
<td align="right">0.4%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">10,320</td>
<td align="right">13.5%</td>
<td align="right">2,120</td>
<td align="right">9.6%</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">23,300</td>
<td align="right">30.5%</td>
<td align="right">3,440</td>
<td align="right">15.5%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">16,460</td>
<td align="right">21.5%</td>
<td align="right">7,200</td>
<td align="right">32.5%</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">7,240</td>
<td align="right">9.5%</td>
<td align="right">1,780</td>
<td align="right">8.0%</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,760</td>
<td align="right">3.6%</td>
<td align="right">580</td>
<td align="right">2.6%</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">920</td>
<td align="right">1.2%</td>
<td align="right">180</td>
<td align="right">0.8%</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">-80.0%</td>
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
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">489,440</td>
<td align="right">200</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">159,880</td>
<td align="right">240</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">159,880</td>
<td align="right">240</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">188,920</td>
<td align="right">400</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">5,287,460</td>
<td align="right">16,080</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">71,940</td>
<td align="right">400</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">295,960</td>
<td align="right">3,000</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">418,360</td>
<td align="right">5,640</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">11,900</td>
<td align="right">200</td>
<td align="right">-98.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,577,400</td>
<td align="right">35,140</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,362,700</td>
<td align="right">35,140</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">6,660</td>
<td align="right">200</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">6,660</td>
<td align="right">200</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">509,220</td>
<td align="right">22,840</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">509,220</td>
<td align="right">22,840</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">527,900</td>
<td align="right">39,540</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">570,040</td>
<td align="right">49,080</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">942,400</td>
<td align="right">90,040</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">643,580</td>
<td align="right">64,820</td>
<td align="right">-89.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">13,960</td>
<td align="right">1,600</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">557,980</td>
<td align="right">64,820</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">8,228,240</td>
<td align="right">1,009,620</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">8,228,240</td>
<td align="right">1,009,620</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">249,540</td>
<td align="right">32,600</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">248,940</td>
<td align="right">34,020</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">326,580</td>
<td align="right">52,680</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">6,393,720</td>
<td align="right">1,058,600</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">97,040</td>
<td align="right">16,300</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">13,734,160</td>
<td align="right">2,573,200</td>
<td align="right">-81.3%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">1,599,540</td>
<td align="right">302,500</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">633,760</td>
<td align="right">137,100</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">633,760</td>
<td align="right">137,100</td>
<td align="right">-78.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">6,520,960</td>
<td align="right">1,431,200</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">34,779,380</td>
<td align="right">8,111,980</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">34,089,380</td>
<td align="right">9,453,620</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">1,256,060</td>
<td align="right">364,340</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">871,280</td>
<td align="right">255,620</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">15,141,920</td>
<td align="right">4,602,700</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">8,917,820</td>
<td align="right">2,984,860</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,871,940</td>
<td align="right">1,571,720</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,554,120</td>
<td align="right">648,840</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">3,026,300</td>
<td align="right">1,315,440</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">5,555,300</td>
<td align="right">2,609,460</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">40,248,180</td>
<td align="right">19,137,140</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">61,149,000</td>
<td align="right">29,586,480</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">99,667,540</td>
<td align="right">48,227,940</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">79,003,380</td>
<td align="right">38,339,000</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">58,691,360</td>
<td align="right">29,093,720</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">12,911,480</td>
<td align="right">6,524,300</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">4,677,620</td>
<td align="right">2,366,740</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">499,200</td>
<td align="right">262,940</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">61,662,000</td>
<td align="right">32,488,520</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">48,849,100</td>
<td align="right">26,037,480</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">74,120</td>
<td align="right">39,560</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">72,383,960</td>
<td align="right">38,805,780</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">46,044,000</td>
<td align="right">24,975,700</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">84,762,080</td>
<td align="right">46,667,760</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">3,264,400</td>
<td align="right">1,884,680</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">4,160,840</td>
<td align="right">2,413,460</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">59,900</td>
<td align="right">83,920</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,635,840</td>
<td align="right">988,160</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">71,955,560</td>
<td align="right">44,343,120</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">71,944,020</td>
<td align="right">44,343,120</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">23,596,420</td>
<td align="right">14,647,680</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">75,365,920</td>
<td align="right">47,027,060</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,156,480</td>
<td align="right">2,606,680</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">21,887,940</td>
<td align="right">13,953,880</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,225,740</td>
<td align="right">1,423,760</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">23,137,200</td>
<td align="right">14,880,980</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">23,444,560</td>
<td align="right">15,098,540</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">132,192,680</td>
<td align="right">89,033,760</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">2,654,260</td>
<td align="right">1,791,320</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">3,077,620</td>
<td align="right">2,080,060</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">22,274,540</td>
<td align="right">15,102,620</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">893,240</td>
<td align="right">1,175,720</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">353,952,260</td>
<td align="right">242,608,320</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">480,422,140</td>
<td align="right">330,924,680</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">1,016,860</td>
<td align="right">1,329,560</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">1,017,480</td>
<td align="right">1,329,980</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">21,217,960</td>
<td align="right">14,879,960</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">461,111,840</td>
<td align="right">323,715,100</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">27,627,400</td>
<td align="right">19,644,580</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">513,509,260</td>
<td align="right">366,340,820</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,108,400</td>
<td align="right">2,233,420</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,249,260</td>
<td align="right">927,100</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">18,479,900</td>
<td align="right">13,730,120</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">15,801,300</td>
<td align="right">11,758,740</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">4,392,860</td>
<td align="right">3,283,300</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">28,684,620</td>
<td align="right">21,557,360</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">14,099,640</td>
<td align="right">10,614,660</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">13,102,480</td>
<td align="right">9,907,980</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">3,086,600</td>
<td align="right">2,341,020</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">13,127,560</td>
<td align="right">9,989,840</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">13,054,320</td>
<td align="right">10,010,140</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">13,054,320</td>
<td align="right">10,010,140</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,619,980</td>
<td align="right">1,251,620</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">41,774,460</td>
<td align="right">32,452,880</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">438,803,300</td>
<td align="right">343,992,140</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">4,192,960</td>
<td align="right">3,296,240</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">35,334,960</td>
<td align="right">27,997,400</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">12,297,100</td>
<td align="right">9,760,000</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">13,293,680</td>
<td align="right">10,564,520</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">6,135,920</td>
<td align="right">4,907,820</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">30,299,360</td>
<td align="right">24,252,120</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">10,145,760</td>
<td align="right">8,323,140</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">11,816,440</td>
<td align="right">9,759,400</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">5,778,820</td>
<td align="right">4,787,280</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">92,559,180</td>
<td align="right">76,990,380</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">352,629,640</td>
<td align="right">294,682,980</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">37,912,520</td>
<td align="right">31,896,920</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">1,221,300</td>
<td align="right">1,391,160</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,221,300</td>
<td align="right">1,391,160</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">5,448,940</td>
<td align="right">4,702,040</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">23,521,420</td>
<td align="right">20,464,360</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">32,627,780</td>
<td align="right">28,871,140</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">78,427,760</td>
<td align="right">69,761,120</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">741,000</td>
<td align="right">814,600</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">25,746,080</td>
<td align="right">23,284,440</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,289,080</td>
<td align="right">2,976,860</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">768,320</td>
<td align="right">841,220</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">768,320</td>
<td align="right">841,220</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">40,484,700</td>
<td align="right">36,804,060</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">46,019,260</td>
<td align="right">41,918,140</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,493,120</td>
<td align="right">2,277,180</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">4,340,520</td>
<td align="right">3,970,880</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">65,543,540</td>
<td align="right">60,006,280</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">13,082,560</td>
<td align="right">14,179,400</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,752,280</td>
<td align="right">2,533,700</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">27,092,580</td>
<td align="right">25,071,520</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">33,087,120</td>
<td align="right">35,416,140</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">16,026,880</td>
<td align="right">14,964,160</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">17,728,700</td>
<td align="right">16,611,240</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">63,333,800</td>
<td align="right">59,370,320</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">33,171,640</td>
<td align="right">31,150,200</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,269,760</td>
<td align="right">4,038,340</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">3,454,920</td>
<td align="right">3,271,380</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">11,842,820</td>
<td align="right">12,428,020</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">1,893,880</td>
<td align="right">1,981,320</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,473,180</td>
<td align="right">3,325,240</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">12,365,460</td>
<td align="right">12,870,620</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">102,883,460</td>
<td align="right">98,855,200</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">92,565,620</td>
<td align="right">88,982,720</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">35,500</td>
<td align="right">36,740</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">11,872,760</td>
<td align="right">12,273,200</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">963,320</td>
<td align="right">932,520</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,600,820</td>
<td align="right">1,554,320</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">48,920</td>
<td align="right">50,160</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">3,529,400</td>
<td align="right">3,496,660</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">189,501,060</td>
<td align="right">191,058,960</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">12,745,980</td>
<td align="right">12,656,960</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">21,514,340</td>
<td align="right">21,608,980</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">117,180</td>
<td align="right">116,700</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">82,680</td>
<td align="right">82,380</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">82,680</td>
<td align="right">82,380</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">47,600</td>
<td align="right">47,760</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">11,395,220</td>
<td align="right">11,381,160</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">599,780</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">293,520</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">279,480</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">246,320</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">127,860</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">123,860</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">102,340</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">97,740</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">85,600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">63,840</td>
<td align="right">63,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">15,560</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">13,420</td>
<td align="right">13,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">4,960</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">4,040</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">3,260</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">180</td>
<td align="right">180</td>
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
<td align="right">3,900</td>
<td align="right">1,240</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">100</td>
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
