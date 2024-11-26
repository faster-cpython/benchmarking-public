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
<td align="right">513,300</td>
<td align="right">540</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">75,960</td>
<td align="right">360</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">7,613,400</td>
<td align="right">168,640</td>
<td align="right">-97.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">609,760</td>
<td align="right">39,640</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">397,900</td>
<td align="right">26,400</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">6,583,240</td>
<td align="right">577,600</td>
<td align="right">-91.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">156,900</td>
<td align="right">15,700</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">32,948,000</td>
<td align="right">3,351,380</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,170,180</td>
<td align="right">448,380</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">3,300</td>
<td align="right">360</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">4,482,700</td>
<td align="right">490,480</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">318,480</td>
<td align="right">41,260</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">28,338,040</td>
<td align="right">4,480,640</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,795,080</td>
<td align="right">2,710,780</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,036,100</td>
<td align="right">740,100</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">20,454,940</td>
<td align="right">3,753,720</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">61,102,920</td>
<td align="right">11,646,700</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">16,367,600</td>
<td align="right">3,265,420</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">12,876,340</td>
<td align="right">2,835,680</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">237,587,100</td>
<td align="right">53,427,800</td>
<td align="right">-77.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">38,786,620</td>
<td align="right">8,931,300</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">7,119,760</td>
<td align="right">1,656,100</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">28,982,340</td>
<td align="right">6,824,960</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">28,982,400</td>
<td align="right">6,825,020</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,262,360</td>
<td align="right">781,520</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">902,760</td>
<td align="right">218,560</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">14,643,960</td>
<td align="right">3,583,940</td>
<td align="right">-75.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">18,090,460</td>
<td align="right">5,196,840</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,966,200</td>
<td align="right">570,160</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,133,640</td>
<td align="right">9,361,720</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">36,535,020</td>
<td align="right">10,805,500</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">21,765,300</td>
<td align="right">6,653,540</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,730,960</td>
<td align="right">890,640</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,727,900</td>
<td align="right">890,520</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">143,808,880</td>
<td align="right">240,032,120</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">62,668,500</td>
<td align="right">21,267,360</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">92,573,100</td>
<td align="right">33,213,460</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">228,720</td>
<td align="right">84,140</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">14,700</td>
<td align="right">5,880</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">11,142,760</td>
<td align="right">4,478,380</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,847,920</td>
<td align="right">2,756,320</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">171,192,180</td>
<td align="right">69,719,000</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,043,800</td>
<td align="right">429,640</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">110,649,840</td>
<td align="right">46,258,780</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,456,320</td>
<td align="right">4,831,840</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">44,367,520</td>
<td align="right">18,887,360</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">9,850,380</td>
<td align="right">4,241,560</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">323,000</td>
<td align="right">140,040</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">283,271,980</td>
<td align="right">127,105,980</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,139,100</td>
<td align="right">3,212,560</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,957,780</td>
<td align="right">2,231,880</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">34,453,280</td>
<td align="right">53,201,920</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">6,377,580</td>
<td align="right">2,998,160</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">6,127,760</td>
<td align="right">2,965,620</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,591,840</td>
<td align="right">795,900</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,880</td>
<td align="right">2,940</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">216,486,740</td>
<td align="right">108,723,840</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">44,944,480</td>
<td align="right">22,714,900</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">149,700</td>
<td align="right">75,920</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,315,620</td>
<td align="right">8,280,220</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">65,414,920</td>
<td align="right">33,260,360</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,509,320</td>
<td align="right">768,480</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,155,535,920</td>
<td align="right">611,369,860</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">158,653,360</td>
<td align="right">84,082,880</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">209,986,600</td>
<td align="right">112,163,800</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">227,476,360</td>
<td align="right">122,906,040</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">524,720</td>
<td align="right">764,100</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">38,323,880</td>
<td align="right">21,105,300</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">332,160</td>
<td align="right">187,400</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,387,980</td>
<td align="right">17,306,840</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,869,460</td>
<td align="right">6,190,500</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">13,066,200</td>
<td align="right">7,449,220</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,576,800</td>
<td align="right">2,627,820</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">23,810,440</td>
<td align="right">13,915,780</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">11,206,460</td>
<td align="right">6,694,220</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,739,780</td>
<td align="right">10,622,160</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,567,160</td>
<td align="right">11,809,200</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">142,467,800</td>
<td align="right">87,590,560</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">7,284,780</td>
<td align="right">4,573,360</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">61,141,600</td>
<td align="right">38,573,480</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">130,789,360</td>
<td align="right">82,947,640</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">68,279,540</td>
<td align="right">44,106,300</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">149,951,420</td>
<td align="right">97,425,840</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">54,920</td>
<td align="right">73,700</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,235,240</td>
<td align="right">1,493,280</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">319,340</td>
<td align="right">217,180</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,217,800</td>
<td align="right">62,266,080</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,436,800</td>
<td align="right">3,055,180</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">103,181,600</td>
<td align="right">71,894,320</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,400</td>
<td align="right">8,000</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">582,560</td>
<td align="right">421,480</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">61,467,280</td>
<td align="right">45,303,280</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">480</td>
<td align="right">360</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,539,400</td>
<td align="right">1,935,620</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">13,348,980</td>
<td align="right">10,267,220</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">106,869,580</td>
<td align="right">83,142,500</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">17,666,400</td>
<td align="right">14,352,900</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">17,789,000</td>
<td align="right">14,578,020</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,332,440</td>
<td align="right">9,399,100</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,709,900</td>
<td align="right">2,269,440</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,742,740</td>
<td align="right">2,300,940</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,449,640</td>
<td align="right">1,220,340</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">9,856,740</td>
<td align="right">8,299,560</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,015,820</td>
<td align="right">13,551,700</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">450,860</td>
<td align="right">383,320</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">38,371,060</td>
<td align="right">33,591,320</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">230,880</td>
<td align="right">204,420</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,129,960</td>
<td align="right">8,243,160</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,942,860</td>
<td align="right">2,662,920</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,401,960</td>
<td align="right">2,205,060</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">28,174,320</td>
<td align="right">26,256,040</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,218,980</td>
<td align="right">8,634,900</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,404,280</td>
<td align="right">4,147,300</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,656,580</td>
<td align="right">9,120,200</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">140,003,200</td>
<td align="right">132,285,420</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">840</td>
<td align="right">880</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,412,120</td>
<td align="right">8,048,060</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">42,960</td>
<td align="right">44,680</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,000</td>
<td align="right">2,040</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">159,814,580</td>
<td align="right">157,844,780</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">71,060</td>
<td align="right">71,920</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">6,660</td>
<td align="right">6,700</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">207,128,180</td>
<td align="right">206,158,660</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,254,620</td>
<td align="right">1,258,900</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">38,337,840</td>
<td align="right">38,467,440</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,110,600</td>
<td align="right">38,036,460</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,113,900</td>
<td align="right">37,070,500</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,581,860</td>
<td align="right">4,580,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">36,886,980</td>
<td align="right">36,886,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">11,627,760</td>
<td align="right">11,627,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">6,134,820</td>
<td align="right">6,134,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">6,134,820</td>
<td align="right">6,134,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">5,778,720</td>
<td align="right">5,778,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,951,860</td>
<td align="right">4,951,860</td>
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
<td align="left">UNARY_NEGATIVE</td>
<td align="right">176,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">145,320</td>
<td align="right">145,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">61,740</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">49,980</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">35,280</td>
<td align="right">35,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">27,480</td>
<td align="right">27,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">14,640</td>
<td align="right">14,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">6,180</td>
<td align="right">6,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">5,880</td>
<td align="right">5,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">5,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,020</td>
<td align="right">4,020</td>
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
<td align="right"></td>
<td align="right"></td>
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
<td align="left">END_SEND</td>
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
<td align="right">280</td>
<td align="right">280</td>
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
<td align="right">11,322,560</td>
<td align="right">19.0%</td>
<td align="right">9,390,180</td>
<td align="right">16.2%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">48,411,900</td>
<td align="right">81.0%</td>
<td align="right">48,411,900</td>
<td align="right">83.7%</td>
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
<td align="right">9,660</td>
<td align="right">97.8%</td>
<td align="right">8,700</td>
<td align="right">97.5%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">220</td>
<td align="right">2.2%</td>
<td align="right">220</td>
<td align="right">2.5%</td>
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
<td align="right">2,620</td>
<td align="right">27.1%</td>
<td align="right">2,020</td>
<td align="right">23.2%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,180</td>
<td align="right">32.9%</td>
<td align="right">2,940</td>
<td align="right">33.8%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">32.7%</td>
<td align="right">3,040</td>
<td align="right">34.9%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">320</td>
<td align="right">3.3%</td>
<td align="right">320</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">180</td>
<td align="right">1.9%</td>
<td align="right">180</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">160</td>
<td align="right">1.7%</td>
<td align="right">160</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">6,377,580</td>
<td align="right">100.0%</td>
<td align="right">2,998,160</td>
<td align="right">100.0%</td>
<td align="right">-53.0%</td>
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
<td align="right">9,643,600</td>
<td align="right">9.1%</td>
<td align="right">9,107,080</td>
<td align="right">8.7%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,146,940</td>
<td align="right">2.0%</td>
<td align="right">2,141,620</td>
<td align="right">2.0%</td>
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
<td align="right">93,974,660</td>
<td align="right">88.8%</td>
<td align="right">93,941,420</td>
<td align="right">89.3%</td>
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
<td align="right">12,360</td>
<td align="right">23.1%</td>
<td align="right">12,500</td>
<td align="right">23.4%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,100</td>
<td align="right">76.9%</td>
<td align="right">41,020</td>
<td align="right">76.6%</td>
<td align="right">-0.2%</td>
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
<td align="left">string slice</td>
<td align="right">720</td>
<td align="right">5.8%</td>
<td align="right">560</td>
<td align="right">4.5%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">9,120</td>
<td align="right">73.8%</td>
<td align="right">9,480</td>
<td align="right">75.8%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">680</td>
<td align="right">5.5%</td>
<td align="right">660</td>
<td align="right">5.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,660</td>
<td align="right">13.4%</td>
<td align="right">1,620</td>
<td align="right">13.0%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">1.5%</td>
<td align="right">180</td>
<td align="right">1.4%</td>
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
<td align="right">16,624,580</td>
<td align="right">2.9%</td>
<td align="right">15,286,780</td>
<td align="right">2.7%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">554,639,780</td>
<td align="right">97.1%</td>
<td align="right">556,015,640</td>
<td align="right">97.3%</td>
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
<td align="left">Success</td>
<td align="right">317,720</td>
<td align="right">100.0%</td>
<td align="right">292,520</td>
<td align="right">100.0%</td>
<td align="right">-7.9%</td>
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
<td align="right">220,160</td>
<td align="right">0.6%</td>
<td align="right">103,560</td>
<td align="right">0.3%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,497,600</td>
<td align="right">4.1%</td>
<td align="right">762,780</td>
<td align="right">2.1%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,760,180</td>
<td align="right">95.3%</td>
<td align="right">34,655,720</td>
<td align="right">97.5%</td>
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
<td align="left">Failure</td>
<td align="right">11,360</td>
<td align="right">71.6%</td>
<td align="right">5,340</td>
<td align="right">69.9%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,500</td>
<td align="right">28.4%</td>
<td align="right">2,300</td>
<td align="right">30.1%</td>
<td align="right">-48.9%</td>
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
<td align="right">10,900</td>
<td align="right">96.0%</td>
<td align="right">4,920</td>
<td align="right">92.1%</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">80</td>
<td align="right">0.7%</td>
<td align="right">40</td>
<td align="right">0.7%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">1.8%</td>
<td align="right">200</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">80</td>
<td align="right">0.7%</td>
<td align="right">80</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">40</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.4%</td>
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
<td align="right">4,953,820</td>
<td align="right">8.4%</td>
<td align="right">2,229,060</td>
<td align="right">3.9%</td>
<td align="right">-55.0%</td>
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
<td align="right">91.6%</td>
<td align="right">54,350,400</td>
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
<td align="left">Failure</td>
<td align="right">3,840</td>
<td align="right">97.0%</td>
<td align="right">2,700</td>
<td align="right">95.7%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">3.0%</td>
<td align="right">120</td>
<td align="right">4.3%</td>
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
<td align="right">880</td>
<td align="right">22.9%</td>
<td align="right">540</td>
<td align="right">20.0%</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">680</td>
<td align="right">17.7%</td>
<td align="right">420</td>
<td align="right">15.6%</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">20.8%</td>
<td align="right">500</td>
<td align="right">18.5%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,480</td>
<td align="right">38.5%</td>
<td align="right">1,240</td>
<td align="right">45.9%</td>
<td align="right">-16.2%</td>
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
<td align="right">15,790,280</td>
<td align="right">10.5%</td>
<td align="right">2,709,240</td>
<td align="right">2.5%</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">111,286,140</td>
<td align="right">74.4%</td>
<td align="right">86,219,060</td>
<td align="right">80.5%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,591,940</td>
<td align="right">15.1%</td>
<td align="right">18,230,920</td>
<td align="right">17.0%</td>
<td align="right">-19.3%</td>
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
<td align="right">4,800</td>
<td align="right">1.1%</td>
<td align="right">1,540</td>
<td align="right">0.4%</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">426,260</td>
<td align="right">98.9%</td>
<td align="right">343,960</td>
<td align="right">99.6%</td>
<td align="right">-19.3%</td>
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
<td align="right">2,480</td>
<td align="right">51.7%</td>
<td align="right">180</td>
<td align="right">11.7%</td>
<td align="right">-92.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">180</td>
<td align="right">3.8%</td>
<td align="right">60</td>
<td align="right">3.9%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">680</td>
<td align="right">14.2%</td>
<td align="right">260</td>
<td align="right">16.9%</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">800</td>
<td align="right">16.7%</td>
<td align="right">520</td>
<td align="right">33.8%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">360</td>
<td align="right">7.5%</td>
<td align="right">320</td>
<td align="right">20.8%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">100</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">60</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">60</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">2.6%</td>
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
<td align="right">91,947,120</td>
<td align="right">9.4%</td>
<td align="right">32,663,680</td>
<td align="right">3.8%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">232,383,740</td>
<td align="right">23.9%</td>
<td align="right">152,941,380</td>
<td align="right">17.9%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">648,713,580</td>
<td align="right">66.6%</td>
<td align="right">666,553,560</td>
<td align="right">78.2%</td>
<td align="right">2.8%</td>
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
<td align="right">18,160</td>
<td align="right">0.4%</td>
<td align="right">3,380</td>
<td align="right">0.1%</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,992,020</td>
<td align="right">99.6%</td>
<td align="right">3,432,020</td>
<td align="right">99.9%</td>
<td align="right">-31.2%</td>
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
<td align="right">2,840</td>
<td align="right">15.6%</td>
<td align="right">160</td>
<td align="right">4.7%</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">7,500</td>
<td align="right">41.3%</td>
<td align="right">740</td>
<td align="right">21.9%</td>
<td align="right">-90.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,600</td>
<td align="right">30.8%</td>
<td align="right">1,160</td>
<td align="right">34.3%</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">1.9%</td>
<td align="right">80</td>
<td align="right">2.4%</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">180</td>
<td align="right">1.0%</td>
<td align="right">60</td>
<td align="right">1.8%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">0.7%</td>
<td align="right">40</td>
<td align="right">1.2%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">620</td>
<td align="right">3.4%</td>
<td align="right">400</td>
<td align="right">11.8%</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">2.3%</td>
<td align="right">340</td>
<td align="right">10.1%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">240</td>
<td align="right">1.3%</td>
<td align="right">220</td>
<td align="right">6.5%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">233,858,540</td>
<td align="right">100.0%</td>
<td align="right">90,984,880</td>
<td align="right">100.0%</td>
<td align="right">-61.1%</td>
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
<td align="right">2,040</td>
<td align="right">100.0%</td>
<td align="right">2,080</td>
<td align="right">100.0%</td>
<td align="right">2.0%</td>
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
<td align="right">16,003,920</td>
<td align="right">13.7%</td>
<td align="right">13,543,240</td>
<td align="right">12.4%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,915,360</td>
<td align="right">46.1%</td>
<td align="right">47,071,160</td>
<td align="right">43.1%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,039,820</td>
<td align="right">40.2%</td>
<td align="right">48,502,380</td>
<td align="right">44.4%</td>
<td align="right">3.1%</td>
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
<td align="right">11,500</td>
<td align="right">1.1%</td>
<td align="right">8,020</td>
<td align="right">0.9%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,017,780</td>
<td align="right">98.9%</td>
<td align="right">888,860</td>
<td align="right">99.1%</td>
<td align="right">-12.7%</td>
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
<td align="left">not in keys</td>
<td align="right">360</td>
<td align="right">3.1%</td>
<td align="right">200</td>
<td align="right">2.5%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">8,860</td>
<td align="right">77.0%</td>
<td align="right">5,940</td>
<td align="right">74.1%</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">17.7%</td>
<td align="right">1,640</td>
<td align="right">20.4%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">200</td>
<td align="right">1.7%</td>
<td align="right">200</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
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
<td align="right">54,920</td>
<td align="right">100.0%</td>
<td align="right">73,700</td>
<td align="right">100.0%</td>
<td align="right">34.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">380</td>
<td align="right">0.0%</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,577,980</td>
<td align="right">9.7%</td>
<td align="right">4,576,560</td>
<td align="right">9.7%</td>
<td align="right">-0.0%</td>
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
<td align="right">42,557,800</td>
<td align="right">90.3%</td>
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
<td align="left">Success</td>
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">120</td>
<td align="right">3.1%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,760</td>
<td align="right">95.9%</td>
<td align="right">3,800</td>
<td align="right">96.9%</td>
<td align="right">1.1%</td>
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
<td align="right">220</td>
<td align="right">5.9%</td>
<td align="right">260</td>
<td align="right">6.8%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,440</td>
<td align="right">64.9%</td>
<td align="right">2,440</td>
<td align="right">64.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">1,060</td>
<td align="right">27.9%</td>
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
<td align="right">5,630,480</td>
<td align="right">2.0%</td>
<td align="right">3,449,780</td>
<td align="right">1.3%</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,431,760</td>
<td align="right">0.9%</td>
<td align="right">1,865,380</td>
<td align="right">0.7%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">266,669,380</td>
<td align="right">97.0%</td>
<td align="right">264,577,680</td>
<td align="right">98.0%</td>
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
<td align="right">107,060</td>
<td align="right">50.1%</td>
<td align="right">65,900</td>
<td align="right">48.7%</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">106,740</td>
<td align="right">49.9%</td>
<td align="right">69,400</td>
<td align="right">51.3%</td>
<td align="right">-35.0%</td>
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
<td align="right">61,640</td>
<td align="right">57.7%</td>
<td align="right">24,760</td>
<td align="right">35.7%</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,040</td>
<td align="right">1.0%</td>
<td align="right">860</td>
<td align="right">1.2%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">120</td>
<td align="right">0.2%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,360</td>
<td align="right">2.2%</td>
<td align="right">2,300</td>
<td align="right">3.3%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">41,540</td>
<td align="right">38.9%</td>
<td align="right">41,340</td>
<td align="right">59.6%</td>
<td align="right">-0.5%</td>
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
<td align="right">48,290,080</td>
<td align="right">100.0%</td>
<td align="right">48,290,080</td>
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
<td align="right">360</td>
<td align="right">100.0%</td>
<td align="right">360</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,856,608,440</td>
<td align="right">32.0%</td>
<td align="right">874,209,040</td>
<td align="right">25.1%</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">165,400,480</td>
<td align="right">2.8%</td>
<td align="right">80,590,180</td>
<td align="right">2.3%</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,454,751,680</td>
<td align="right">59.5%</td>
<td align="right">2,294,001,000</td>
<td align="right">65.8%</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">333,530,480</td>
<td align="right">5.7%</td>
<td align="right">239,241,000</td>
<td align="right">6.9%</td>
<td align="right">-28.3%</td>
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
<td align="right">15,790,280</td>
<td align="right">9.6%</td>
<td align="right">2,709,240</td>
<td align="right">3.4%</td>
<td align="right">-82.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">91,947,120</td>
<td align="right">55.9%</td>
<td align="right">32,663,680</td>
<td align="right">40.9%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,953,820</td>
<td align="right">3.0%</td>
<td align="right">2,229,060</td>
<td align="right">2.8%</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">6,377,580</td>
<td align="right">3.9%</td>
<td align="right">2,998,160</td>
<td align="right">3.8%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,497,600</td>
<td align="right">0.9%</td>
<td align="right">762,780</td>
<td align="right">1.0%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,431,760</td>
<td align="right">1.5%</td>
<td align="right">1,865,380</td>
<td align="right">2.3%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,322,560</td>
<td align="right">6.9%</td>
<td align="right">9,390,180</td>
<td align="right">11.7%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,003,920</td>
<td align="right">9.7%</td>
<td align="right">13,543,240</td>
<td align="right">16.9%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,643,600</td>
<td align="right">5.9%</td>
<td align="right">9,107,080</td>
<td align="right">11.4%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,577,980</td>
<td align="right">2.8%</td>
<td align="right">4,576,560</td>
<td align="right">5.7%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">70,888,240</td>
<td align="right">21.3%</td>
<td align="right">43,864,220</td>
<td align="right">18.3%</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">46,429,620</td>
<td align="right">13.9%</td>
<td align="right">29,543,780</td>
<td align="right">12.3%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">11,295,860</td>
<td align="right">3.4%</td>
<td align="right">9,114,380</td>
<td align="right">3.8%</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">11,296,080</td>
<td align="right">3.4%</td>
<td align="right">9,116,540</td>
<td align="right">3.8%</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,131,440</td>
<td align="right">2.7%</td>
<td align="right">7,875,540</td>
<td align="right">3.3%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,912,180</td>
<td align="right">16.2%</td>
<td align="right">47,071,160</td>
<td align="right">19.7%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80,484,360</td>
<td align="right">24.1%</td>
<td align="right">70,403,960</td>
<td align="right">29.4%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,144,720</td>
<td align="right">2.1%</td>
<td align="right">6,413,080</td>
<td align="right">2.7%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,001,400</td>
<td align="right">1.2%</td>
<td align="right">3,945,540</td>
<td align="right">1.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">25,599,040</td>
<td align="right">7.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2,128,240</td>
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
<td align="right">8,013,720</td>
<td align="right">2.3%</td>
<td align="right">7,943,860</td>
<td align="right">2.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">38,841,220</td>
<td align="right">11.0%</td>
<td align="right">38,767,080</td>
<td align="right">10.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">38,844,700</td>
<td align="right">11.0%</td>
<td align="right">38,770,560</td>
<td align="right">10.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,152,560</td>
<td align="right">11.0%</td>
<td align="right">39,078,420</td>
<td align="right">11.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,152,560</td>
<td align="right">11.0%</td>
<td align="right">39,078,420</td>
<td align="right">11.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">315,243,260</td>
<td align="right">89.0%</td>
<td align="right">315,317,400</td>
<td align="right">89.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,635,500</td>
<td align="right">88.5%</td>
<td align="right">313,639,780</td>
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
<td align="right">13,629,300</td>
<td align="right">3.8%</td>
<td align="right">13,629,300</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">1,826,880</td>
<td align="right">0.5%</td>
<td align="right">1,826,880</td>
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
<td align="right">9,598,440</td>
<td align="right">2.7%</td>
<td align="right">9,598,440</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">686,580</td>
<td align="right">0.1%</td>
<td align="right">1,053,660</td>
<td align="right">0.1%</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">3,332,423,522</td>
<td align="right">38.4%</td>
<td align="right">4,790,946,301</td>
<td align="right">52.4%</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">3,059,440,518</td>
<td align="right">32.8%</td>
<td align="right">4,286,736,742</td>
<td align="right">42.9%</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">898,235,860</td>
<td align="right">10.3%</td>
<td align="right">539,852,980</td>
<td align="right">5.9%</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,539,342,820</td>
<td align="right">29.2%</td>
<td align="right">1,658,400,460</td>
<td align="right">18.1%</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">938,481,700</td>
<td align="right">10.1%</td>
<td align="right">634,043,800</td>
<td align="right">6.3%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,923,973,036</td>
<td align="right">20.6%</td>
<td align="right">2,327,124,766</td>
<td align="right">23.3%</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,402,072,040</td>
<td align="right">36.5%</td>
<td align="right">2,753,957,960</td>
<td align="right">27.5%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,919,020,269</td>
<td align="right">22.1%</td>
<td align="right">2,157,637,922</td>
<td align="right">23.6%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,292,579</td>
<td align="right"></td>
<td align="right">2,035,273</td>
<td align="right"></td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">40,051,836</td>
<td align="right"></td>
<td align="right">36,668,457</td>
<td align="right"></td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">38,519,645</td>
<td align="right"></td>
<td align="right">35,393,726</td>
<td align="right"></td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">196,794,721</td>
<td align="right"></td>
<td align="right">188,948,247</td>
<td align="right"></td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">457,224,915</td>
<td align="right"></td>
<td align="right">442,222,554</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">345,860</td>
<td align="right">0.0%</td>
<td align="right">348,420</td>
<td align="right">0.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">607,736,798</td>
<td align="right"></td>
<td align="right">608,979,232</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">571,880,360</td>
<td align="right">70.7%</td>
<td align="right">572,453,560</td>
<td align="right">70.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">236,866,720</td>
<td align="right">29.3%</td>
<td align="right">236,775,500</td>
<td align="right">29.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">570,847,920</td>
<td align="right">70.6%</td>
<td align="right">571,051,480</td>
<td align="right">70.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">236,838,460</td>
<td align="right"></td>
<td align="right">236,776,780</td>
<td align="right"></td>
<td align="right">-0.0%</td>
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
<td align="right">25,880</td>
<td align="right">72,717,480</td>
<td align="right">1,459,555,520</td>
<td align="right">25,960</td>
<td align="right">73,098,660</td>
<td align="right">1,471,938,020</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">6,820</td>
<td align="right">1.8%</td>
<td align="right">38,780</td>
<td align="right">3.9%</td>
<td align="right">468.6%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,740</td>
<td align="right">0.5%</td>
<td align="right">6,700</td>
<td align="right">0.7%</td>
<td align="right">285.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">127,680</td>
<td align="right">33.9%</td>
<td align="right">421,280</td>
<td align="right">42.5%</td>
<td align="right">229.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">273,720</td>
<td align="right">72.8%</td>
<td align="right">755,480</td>
<td align="right">76.2%</td>
<td align="right">176.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">376,180</td>
<td align="right"></td>
<td align="right">991,440</td>
<td align="right"></td>
<td align="right">163.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">101,080</td>
<td align="right">26.9%</td>
<td align="right">235,780</td>
<td align="right">23.8%</td>
<td align="right">133.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">537,871,880</td>
<td align="right"></td>
<td align="right">1,035,038,320</td>
<td align="right"></td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">6,766,414,860</td>
<td align="right">1,258.0%</td>
<td align="right">12,960,541,800</td>
<td align="right">1,252.2%</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,380</td>
<td align="right">0.4%</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">7,040</td>
<td align="right">1.9%</td>
<td align="right">6,520</td>
<td align="right">0.7%</td>
<td align="right">-7.4%</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">233.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">256,000</td>
<td align="right">93.5%</td>
<td align="right">742,540</td>
<td align="right">98.3%</td>
<td align="right">190.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">273,720</td>
<td align="right"></td>
<td align="right">755,480</td>
<td align="right"></td>
<td align="right">176.0%</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60 / 0 !!</td>
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
<td align="right">6,100</td>
<td align="right">0.8%</td>
<td align="right">6,100 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">12,100</td>
<td align="right">4.4%</td>
<td align="right">28,840</td>
<td align="right">3.8%</td>
<td align="right">138.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">38,560</td>
<td align="right">14.1%</td>
<td align="right">86,120</td>
<td align="right">11.4%</td>
<td align="right">123.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">89,040</td>
<td align="right">32.5%</td>
<td align="right">280,160</td>
<td align="right">37.1%</td>
<td align="right">214.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">81,600</td>
<td align="right">29.8%</td>
<td align="right">227,260</td>
<td align="right">30.1%</td>
<td align="right">178.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">42,100</td>
<td align="right">15.4%</td>
<td align="right">95,820</td>
<td align="right">12.7%</td>
<td align="right">127.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">8,360</td>
<td align="right">3.1%</td>
<td align="right">26,240</td>
<td align="right">3.5%</td>
<td align="right">213.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,860</td>
<td align="right">0.7%</td>
<td align="right">4,940</td>
<td align="right">0.7%</td>
<td align="right">165.6%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">100</td>
<td align="right">0.0%</td>
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
<td align="right">7,460</td>
<td align="right">2.7%</td>
<td align="right">26,640</td>
<td align="right">3.5%</td>
<td align="right">257.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">25,620</td>
<td align="right">9.4%</td>
<td align="right">37,060</td>
<td align="right">4.9%</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">51,060</td>
<td align="right">18.7%</td>
<td align="right">181,080</td>
<td align="right">24.0%</td>
<td align="right">254.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">104,200</td>
<td align="right">38.1%</td>
<td align="right">296,300</td>
<td align="right">39.2%</td>
<td align="right">184.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">49,240</td>
<td align="right">18.0%</td>
<td align="right">151,460</td>
<td align="right">20.0%</td>
<td align="right">207.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">14,960</td>
<td align="right">5.5%</td>
<td align="right">40,480</td>
<td align="right">5.4%</td>
<td align="right">170.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,900</td>
<td align="right">1.1%</td>
<td align="right">9,300</td>
<td align="right">1.2%</td>
<td align="right">220.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">560</td>
<td align="right">0.2%</td>
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">-60.7%</td>
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
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">80</td>
<td align="right">2,443,600</td>
<td align="right">3,054,400.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">540</td>
<td align="right">1,840,860</td>
<td align="right">340,800.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">540</td>
<td align="right">1,837,920</td>
<td align="right">340,255.6%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">7,440</td>
<td align="right">3,933,980</td>
<td align="right">52,776.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">23,580</td>
<td align="right">3,745,380</td>
<td align="right">15,783.7%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">600</td>
<td align="right">44,000</td>
<td align="right">7,233.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">273,600</td>
<td align="right">8,309,000</td>
<td align="right">2,936.9%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">455,040</td>
<td align="right">11,515,060</td>
<td align="right">2,430.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">32,420</td>
<td align="right">730,900</td>
<td align="right">2,154.5%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,225,560</td>
<td align="right">23,382,940</td>
<td align="right">1,807.9%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,225,560</td>
<td align="right">23,382,940</td>
<td align="right">1,807.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">699,460</td>
<td align="right">13,080,340</td>
<td align="right">1,770.1%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">51,360</td>
<td align="right">873,160</td>
<td align="right">1,600.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">199,520</td>
<td align="right">2,680,360</td>
<td align="right">1,243.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">2,117,800</td>
<td align="right">25,691,120</td>
<td align="right">1,113.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,117,800</td>
<td align="right">25,691,120</td>
<td align="right">1,113.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">22,878,680</td>
<td align="right">261,008,320</td>
<td align="right">1,040.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,284,680</td>
<td align="right">14,178,300</td>
<td align="right">1,003.6%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">42,440</td>
<td align="right">413,940</td>
<td align="right">875.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">6,645,720</td>
<td align="right">56,101,940</td>
<td align="right">744.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,829,240</td>
<td align="right">14,672,720</td>
<td align="right">702.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">6,272,400</td>
<td align="right">43,217,760</td>
<td align="right">589.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">3,367,220</td>
<td align="right">19,358,100</td>
<td align="right">474.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">5,322,020</td>
<td align="right">28,093,940</td>
<td align="right">427.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,434,120</td>
<td align="right">12,825,980</td>
<td align="right">426.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,487,100</td>
<td align="right">22,963,860</td>
<td align="right">411.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">238,580</td>
<td align="right">1,192,260</td>
<td align="right">399.7%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">119,420</td>
<td align="right">559,800</td>
<td align="right">368.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">600,380</td>
<td align="right">2,606,760</td>
<td align="right">334.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">3,910,640</td>
<td align="right">15,303,760</td>
<td align="right">291.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">514,740</td>
<td align="right">1,910,780</td>
<td align="right">271.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">6,983,080</td>
<td align="right">24,543,640</td>
<td align="right">251.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">12,562,420</td>
<td align="right">42,407,000</td>
<td align="right">237.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,298,180</td>
<td align="right">14,162,040</td>
<td align="right">229.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">864,060</td>
<td align="right">2,813,040</td>
<td align="right">225.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">45,258,740</td>
<td align="right">141,949,480</td>
<td align="right">213.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">1,440</td>
<td align="right">4,380</td>
<td align="right">204.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,429,640</td>
<td align="right">19,531,820</td>
<td align="right">203.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,748,620</td>
<td align="right">5,046,000</td>
<td align="right">188.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">39,214,360</td>
<td align="right">111,114,380</td>
<td align="right">183.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">9,191,480</td>
<td align="right">25,892,700</td>
<td align="right">181.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">11,263,820</td>
<td align="right">31,355,600</td>
<td align="right">178.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,251,620</td>
<td align="right">6,228,640</td>
<td align="right">176.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">324,920</td>
<td align="right">895,040</td>
<td align="right">175.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">38,583,880</td>
<td align="right">104,345,300</td>
<td align="right">170.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">309,120</td>
<td align="right">821,880</td>
<td align="right">165.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">186,893,140</td>
<td align="right">485,976,380</td>
<td align="right">160.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">60,151,920</td>
<td align="right">156,105,400</td>
<td align="right">159.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">14,174,540</td>
<td align="right">36,404,120</td>
<td align="right">156.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,306,120</td>
<td align="right">3,339,020</td>
<td align="right">155.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,092,460</td>
<td align="right">7,872,200</td>
<td align="right">154.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">36,620,820</td>
<td align="right">92,980,320</td>
<td align="right">153.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">36,148,180</td>
<td align="right">91,518,380</td>
<td align="right">153.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">3,957,520</td>
<td align="right">9,996,260</td>
<td align="right">152.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">242,940</td>
<td align="right">607,000</td>
<td align="right">149.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">33,950,040</td>
<td align="right">83,704,800</td>
<td align="right">146.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">15,743,220</td>
<td align="right">38,749,320</td>
<td align="right">146.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">15,806,480</td>
<td align="right">38,876,000</td>
<td align="right">145.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">60,487,020</td>
<td align="right">146,826,460</td>
<td align="right">142.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">2,237,540</td>
<td align="right">5,403,540</td>
<td align="right">141.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">2,236,460</td>
<td align="right">5,398,600</td>
<td align="right">141.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">126,365,780</td>
<td align="right">302,518,740</td>
<td align="right">139.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">4,094,640</td>
<td align="right">9,711,620</td>
<td align="right">137.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">34,420,960</td>
<td align="right">79,952,080</td>
<td align="right">132.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">5,880</td>
<td align="right">13,520</td>
<td align="right">129.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">5,958,360</td>
<td align="right">13,669,100</td>
<td align="right">129.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">18,447,620</td>
<td align="right">42,174,700</td>
<td align="right">128.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">66,920,120</td>
<td align="right">152,716,120</td>
<td align="right">128.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,088,140</td>
<td align="right">13,801,500</td>
<td align="right">126.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">10,514,200</td>
<td align="right">23,615,960</td>
<td align="right">124.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">72,638,580</td>
<td align="right">161,907,460</td>
<td align="right">122.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">71,310,660</td>
<td align="right">157,694,500</td>
<td align="right">121.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">21,850,820</td>
<td align="right">47,338,400</td>
<td align="right">116.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">420,776,220</td>
<td align="right">891,562,040</td>
<td align="right">111.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">16,378,020</td>
<td align="right">34,702,520</td>
<td align="right">111.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">4,139,320</td>
<td align="right">8,651,560</td>
<td align="right">109.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">22,031,120</td>
<td align="right">45,876,000</td>
<td align="right">108.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,454,400</td>
<td align="right">11,350,700</td>
<td align="right">108.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">106,957,940</td>
<td align="right">221,674,820</td>
<td align="right">107.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">9,412,180</td>
<td align="right">19,452,840</td>
<td align="right">106.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">35,225,560</td>
<td align="right">72,553,100</td>
<td align="right">106.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">108,236,320</td>
<td align="right">220,856,120</td>
<td align="right">104.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">26,838,140</td>
<td align="right">54,734,880</td>
<td align="right">103.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">53,618,260</td>
<td align="right">109,115,900</td>
<td align="right">103.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,510,360</td>
<td align="right">3,070,400</td>
<td align="right">103.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,171,900</td>
<td align="right">20,665,540</td>
<td align="right">103.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">44,059,840</td>
<td align="right">89,431,260</td>
<td align="right">103.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">277,580</td>
<td align="right">557,520</td>
<td align="right">100.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">277,580</td>
<td align="right">557,520</td>
<td align="right">100.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">29,823,900</td>
<td align="right">58,215,160</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">56,813,340</td>
<td align="right">2,846,060</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">10,204,940</td>
<td align="right">19,896,800</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">8,004,840</td>
<td align="right">15,603,960</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">5,572,060</td>
<td align="right">10,814,660</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">537,871,880</td>
<td align="right">1,035,038,320</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">26,261,440</td>
<td align="right">50,434,680</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,476,360</td>
<td align="right">16,234,520</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">505,024,020</td>
<td align="right">965,761,180</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">107,832,200</td>
<td align="right">205,856,620</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">263,380</td>
<td align="right">24,000</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">110,169,680</td>
<td align="right">210,250,820</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">110,136,300</td>
<td align="right">210,089,760</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">81,221,400</td>
<td align="right">153,504,760</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">7,681,340</td>
<td align="right">14,305,820</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">49,350,160</td>
<td align="right">91,299,220</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">694,360</td>
<td align="right">1,278,400</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">586,354,400</td>
<td align="right">1,079,231,280</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">22,293,220</td>
<td align="right">39,511,800</td>
<td align="right">77.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">535,847,040</td>
<td align="right">938,601,440</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">842,120</td>
<td align="right">1,456,280</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">44,331,800</td>
<td align="right">75,603,100</td>
<td align="right">70.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">432,374,380</td>
<td align="right">734,549,880</td>
<td align="right">69.9%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">1,798,360</td>
<td align="right">3,041,980</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">875,000</td>
<td align="right">1,450,000</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">525,620</td>
<td align="right">867,940</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">44,520,260</td>
<td align="right">72,688,680</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">157,680</td>
<td align="right">255,120</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">258,040</td>
<td align="right">413,600</td>
<td align="right">60.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">5,721,240</td>
<td align="right">9,100,660</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,412,340</td>
<td align="right">19,528,940</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">28,503,000</td>
<td align="right">44,462,160</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">10,148,000</td>
<td align="right">15,644,780</td>
<td align="right">54.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">6,312,040</td>
<td align="right">9,523,020</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">24,615,580</td>
<td align="right">36,156,940</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">482,540</td>
<td align="right">707,980</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,376,080</td>
<td align="right">1,988,520</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">16,281,420</td>
<td align="right">23,399,220</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">16,281,420</td>
<td align="right">23,399,040</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">31,353,660</td>
<td align="right">44,434,680</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">472,280</td>
<td align="right">669,180</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">243,124,320</td>
<td align="right">339,242,220</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">21,800</td>
<td align="right">30,400</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">21,800</td>
<td align="right">30,400</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">7,239,440</td>
<td align="right">9,964,200</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">211,560</td>
<td align="right">285,340</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">38,094,800</td>
<td align="right">51,132,860</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">1,645,780</td>
<td align="right">2,206,000</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">2,560</td>
<td align="right">1,700</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">352,900</td>
<td align="right">455,060</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">3,880,980</td>
<td align="right">4,980,340</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">15,523,540</td>
<td align="right">19,653,740</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">97,046,380</td>
<td align="right">122,542,440</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">55,798,680</td>
<td align="right">69,817,380</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">35,995,560</td>
<td align="right">44,490,480</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">34,323,640</td>
<td align="right">42,044,600</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">43,472,480</td>
<td align="right">52,914,460</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">72,314,240</td>
<td align="right">87,707,340</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">16,571,360</td>
<td align="right">20,073,120</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">9,730,300</td>
<td align="right">11,662,680</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">37,480,860</td>
<td align="right">44,610,300</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">16,811,340</td>
<td align="right">19,893,100</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">103,140,340</td>
<td align="right">119,265,140</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">95,905,660</td>
<td align="right">110,251,180</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">13,549,500</td>
<td align="right">15,467,780</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">119,976,380</td>
<td align="right">132,878,040</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">964,980</td>
<td align="right">1,065,240</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">212,200</td>
<td align="right">193,420</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">48,482,520</td>
<td align="right">44,192,960</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">47,440,740</td>
<td align="right">51,532,340</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">18,353,860</td>
<td align="right">19,773,580</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,221,980</td>
<td align="right">2,390,580</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">995,260</td>
<td align="right">1,062,800</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">995,260</td>
<td align="right">1,062,800</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">600</td>
<td align="right">560</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">600</td>
<td align="right">560</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,063,420</td>
<td align="right">4,322,020</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">3,138,940</td>
<td align="right">3,321,900</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">3,138,940</td>
<td align="right">3,321,900</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,800,900</td>
<td align="right">2,960,860</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">18,621,260</td>
<td align="right">19,417,200</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">3,361,980</td>
<td align="right">3,232,380</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">14,236,020</td>
<td align="right">14,698,360</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">63,400</td>
<td align="right">61,920</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">13,661,240</td>
<td align="right">13,926,300</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">17,163,480</td>
<td align="right">17,440,700</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">26,460</td>
<td align="right">26,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">2,940</td>
<td align="right">2,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">7,441,520</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right"></td>
<td align="right">176,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right"></td>
<td align="right">144,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">144,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right"></td>
<td align="right">141,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right"></td>
<td align="right">86,100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">75,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">57,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right"></td>
<td align="right">49,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">30,220</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">26,460</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right"></td>
<td align="right">8,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">5,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">5,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">3,400</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right"></td>
<td align="right">3,360</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right"></td>
<td align="right">2,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right"></td>
<td align="right">120</td>
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
<td align="right">8,260</td>
<td align="right">37,320</td>
<td align="right">351.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,540</td>
<td align="right">5,900</td>
<td align="right">283.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,760</td>
<td align="right">4,820</td>
<td align="right">28.2%</td>
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
Stats gathered on: 2024-10-25
