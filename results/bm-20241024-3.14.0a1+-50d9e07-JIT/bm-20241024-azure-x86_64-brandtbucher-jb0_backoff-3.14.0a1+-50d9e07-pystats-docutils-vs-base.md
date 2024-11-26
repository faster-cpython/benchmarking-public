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
<td align="right">34,453,280</td>
<td align="right">98,858,280</td>
<td align="right">186.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">513,300</td>
<td align="right">1,440</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">75,960</td>
<td align="right">380</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">7,613,400</td>
<td align="right">175,340</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">609,760</td>
<td align="right">44,120</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">156,900</td>
<td align="right">16,140</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">397,900</td>
<td align="right">41,260</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">6,583,240</td>
<td align="right">690,880</td>
<td align="right">-89.5%</td>
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
<td align="right">567,480</td>
<td align="right">-87.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">318,480</td>
<td align="right">41,220</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,170,180</td>
<td align="right">769,120</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">20,454,940</td>
<td align="right">3,971,460</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,036,100</td>
<td align="right">790,140</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">16,367,600</td>
<td align="right">3,367,300</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">12,876,340</td>
<td align="right">2,955,360</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">28,338,040</td>
<td align="right">6,567,820</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">237,587,100</td>
<td align="right">61,333,280</td>
<td align="right">-74.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">902,760</td>
<td align="right">235,160</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">61,102,920</td>
<td align="right">16,211,240</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,262,360</td>
<td align="right">932,140</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">28,982,340</td>
<td align="right">8,463,280</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">28,982,400</td>
<td align="right">8,463,340</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">14,643,960</td>
<td align="right">4,313,520</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">21,765,300</td>
<td align="right">6,578,080</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">32,948,000</td>
<td align="right">10,220,420</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,966,200</td>
<td align="right">615,260</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,730,960</td>
<td align="right">899,940</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,727,900</td>
<td align="right">899,820</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,133,640</td>
<td align="right">10,720,100</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">18,090,460</td>
<td align="right">6,104,100</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">62,668,500</td>
<td align="right">21,898,640</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,795,080</td>
<td align="right">5,774,860</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">228,720</td>
<td align="right">84,780</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">38,786,620</td>
<td align="right">15,287,620</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">14,700</td>
<td align="right">5,880</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">54,920</td>
<td align="right">86,760</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">11,142,760</td>
<td align="right">4,703,140</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">92,573,100</td>
<td align="right">40,943,220</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">171,192,180</td>
<td align="right">76,972,420</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,139,100</td>
<td align="right">3,239,760</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">44,367,520</td>
<td align="right">20,391,780</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">7,119,760</td>
<td align="right">3,289,540</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">110,649,840</td>
<td align="right">51,163,020</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">9,850,380</td>
<td align="right">4,646,760</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,456,320</td>
<td align="right">5,427,780</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">6,377,580</td>
<td align="right">3,132,280</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,880</td>
<td align="right">2,940</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">6,127,760</td>
<td align="right">3,128,620</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">36,535,020</td>
<td align="right">18,741,700</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,591,840</td>
<td align="right">818,780</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">323,000</td>
<td align="right">169,060</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">143,808,880</td>
<td align="right">212,282,900</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">524,720</td>
<td align="right">764,220</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">38,323,880</td>
<td align="right">21,644,780</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">332,160</td>
<td align="right">188,220</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">283,271,980</td>
<td align="right">160,771,120</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,509,320</td>
<td align="right">864,800</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,315,620</td>
<td align="right">9,428,120</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">65,414,920</td>
<td align="right">38,158,560</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">13,066,200</td>
<td align="right">7,632,380</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">44,944,480</td>
<td align="right">26,304,800</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">209,986,600</td>
<td align="right">123,182,180</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">227,476,360</td>
<td align="right">133,897,820</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,155,535,920</td>
<td align="right">681,903,660</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,576,800</td>
<td align="right">2,723,500</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">216,486,740</td>
<td align="right">130,234,260</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,739,780</td>
<td align="right">11,203,240</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,869,460</td>
<td align="right">6,878,900</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">7,284,780</td>
<td align="right">4,630,740</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">23,810,440</td>
<td align="right">15,168,300</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">149,700</td>
<td align="right">96,160</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,567,160</td>
<td align="right">13,085,080</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">130,789,360</td>
<td align="right">87,559,560</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">68,279,540</td>
<td align="right">45,961,080</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">158,653,360</td>
<td align="right">108,345,140</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,217,800</td>
<td align="right">62,528,240</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,043,800</td>
<td align="right">726,220</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,235,240</td>
<td align="right">1,565,860</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">149,951,420</td>
<td align="right">105,565,320</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,436,800</td>
<td align="right">3,166,340</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,332,440</td>
<td align="right">14,550,940</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">61,141,600</td>
<td align="right">43,962,260</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,400</td>
<td align="right">8,220</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,847,920</td>
<td align="right">4,973,020</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">142,467,800</td>
<td align="right">106,054,120</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,387,980</td>
<td align="right">22,629,200</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">480</td>
<td align="right">360</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">103,181,600</td>
<td align="right">77,612,080</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">582,560</td>
<td align="right">459,340</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">11,206,460</td>
<td align="right">8,911,680</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,957,780</td>
<td align="right">3,966,920</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">13,348,980</td>
<td align="right">11,031,500</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,709,900</td>
<td align="right">2,263,200</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">61,467,280</td>
<td align="right">71,566,240</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,539,400</td>
<td align="right">2,188,660</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">17,789,000</td>
<td align="right">15,423,500</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,015,820</td>
<td align="right">13,944,500</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">106,869,580</td>
<td align="right">93,373,080</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,742,740</td>
<td align="right">2,426,780</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">230,880</td>
<td align="right">204,420</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">38,371,060</td>
<td align="right">33,978,680</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">319,340</td>
<td align="right">283,100</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">17,666,400</td>
<td align="right">15,790,660</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,942,860</td>
<td align="right">2,631,840</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">9,856,740</td>
<td align="right">8,923,980</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,404,280</td>
<td align="right">4,806,680</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">450,860</td>
<td align="right">411,040</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,218,980</td>
<td align="right">8,529,040</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,449,640</td>
<td align="right">1,349,600</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,129,960</td>
<td align="right">8,550,460</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,401,960</td>
<td align="right">2,251,300</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">140,003,200</td>
<td align="right">132,084,620</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">38,337,840</td>
<td align="right">40,143,300</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,412,120</td>
<td align="right">8,074,960</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">42,960</td>
<td align="right">44,680</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,656,580</td>
<td align="right">9,296,560</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">28,174,320</td>
<td align="right">27,240,260</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">71,060</td>
<td align="right">72,940</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">2,000</td>
<td align="right">2,040</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">207,128,180</td>
<td align="right">210,763,480</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">159,814,580</td>
<td align="right">157,829,340</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,254,620</td>
<td align="right">1,257,480</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,113,900</td>
<td align="right">37,070,460</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,110,600</td>
<td align="right">38,076,220</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,581,860</td>
<td align="right">4,581,100</td>
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
<td align="left">SEND_GEN</td>
<td align="right">6,660</td>
<td align="right">6,660</td>
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
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">840</td>
<td align="right">840</td>
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
<td align="right">14,540,720</td>
<td align="right">23.1%</td>
<td align="right">28.4%</td>
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
<td align="right">76.9%</td>
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
<td align="right">10,000</td>
<td align="right">97.8%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">220</td>
<td align="right">2.2%</td>
<td align="right">220</td>
<td align="right">2.2%</td>
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
<td align="right">3,280</td>
<td align="right">32.8%</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,180</td>
<td align="right">32.9%</td>
<td align="right">2,940</td>
<td align="right">29.4%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">32.7%</td>
<td align="right">3,080</td>
<td align="right">30.8%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">320</td>
<td align="right">3.3%</td>
<td align="right">320</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">180</td>
<td align="right">1.9%</td>
<td align="right">180</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">160</td>
<td align="right">1.7%</td>
<td align="right">160</td>
<td align="right">1.6%</td>
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
<td align="right">3,132,280</td>
<td align="right">100.0%</td>
<td align="right">-50.9%</td>
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
<td align="right">9,283,480</td>
<td align="right">8.8%</td>
<td align="right">-3.7%</td>
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
<td align="right">2,145,160</td>
<td align="right">2.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">93,973,360</td>
<td align="right">89.1%</td>
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
<td align="right">12,460</td>
<td align="right">23.3%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,100</td>
<td align="right">76.9%</td>
<td align="right">41,080</td>
<td align="right">76.7%</td>
<td align="right">-0.0%</td>
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
<td align="right">580</td>
<td align="right">4.7%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">9,120</td>
<td align="right">73.8%</td>
<td align="right">9,380</td>
<td align="right">75.3%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,660</td>
<td align="right">13.4%</td>
<td align="right">1,640</td>
<td align="right">13.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">680</td>
<td align="right">5.5%</td>
<td align="right">680</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
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
<td align="right">15,386,200</td>
<td align="right">2.7%</td>
<td align="right">-7.4%</td>
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
<td align="right">555,885,000</td>
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
<td align="right">294,360</td>
<td align="right">100.0%</td>
<td align="right">-7.4%</td>
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
<td align="right">859,060</td>
<td align="right">2.4%</td>
<td align="right">-42.6%</td>
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
<td align="right">34,673,180</td>
<td align="right">97.3%</td>
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
<td align="right">5,380</td>
<td align="right">70.1%</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,500</td>
<td align="right">28.4%</td>
<td align="right">2,300</td>
<td align="right">29.9%</td>
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
<td align="right">4,960</td>
<td align="right">92.2%</td>
<td align="right">-54.5%</td>
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
<td align="right">3,963,640</td>
<td align="right">6.8%</td>
<td align="right">-20.0%</td>
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
<td align="right">93.2%</td>
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
<td align="right">3,160</td>
<td align="right">96.3%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">3.0%</td>
<td align="right">120</td>
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
<td align="left">str</td>
<td align="right">680</td>
<td align="right">17.7%</td>
<td align="right">420</td>
<td align="right">13.3%</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">20.8%</td>
<td align="right">520</td>
<td align="right">16.5%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">880</td>
<td align="right">22.9%</td>
<td align="right">580</td>
<td align="right">18.4%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,480</td>
<td align="right">38.5%</td>
<td align="right">1,640</td>
<td align="right">51.9%</td>
<td align="right">10.8%</td>
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
<td align="right">5,772,660</td>
<td align="right">4.1%</td>
<td align="right">-63.4%</td>
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
<td align="right">26,234,280</td>
<td align="right">18.5%</td>
<td align="right">16.1%</td>
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
<td align="right">109,830,040</td>
<td align="right">77.4%</td>
<td align="right">-1.3%</td>
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
<td align="right">2,200</td>
<td align="right">0.4%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">426,260</td>
<td align="right">98.9%</td>
<td align="right">494,940</td>
<td align="right">99.6%</td>
<td align="right">16.1%</td>
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
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">420</td>
<td align="right">19.1%</td>
<td align="right">600.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,480</td>
<td align="right">51.7%</td>
<td align="right">140</td>
<td align="right">6.4%</td>
<td align="right">-94.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">180</td>
<td align="right">3.8%</td>
<td align="right">60</td>
<td align="right">2.7%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">680</td>
<td align="right">14.2%</td>
<td align="right">240</td>
<td align="right">10.9%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">800</td>
<td align="right">16.7%</td>
<td align="right">840</td>
<td align="right">38.2%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">360</td>
<td align="right">7.5%</td>
<td align="right">360</td>
<td align="right">16.4%</td>
<td align="right">0.0%</td>
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
<td align="left">zip</td>
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">60</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">1.8%</td>
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
<td align="right">40,391,560</td>
<td align="right">4.5%</td>
<td align="right">-56.1%</td>
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
<td align="right">183,249,680</td>
<td align="right">20.5%</td>
<td align="right">-21.1%</td>
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
<td align="right">668,414,120</td>
<td align="right">74.9%</td>
<td align="right">3.0%</td>
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
<td align="right">5,240</td>
<td align="right">0.1%</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,992,020</td>
<td align="right">99.6%</td>
<td align="right">4,003,980</td>
<td align="right">99.9%</td>
<td align="right">-19.8%</td>
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
<td align="right">260</td>
<td align="right">5.0%</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">1.9%</td>
<td align="right">80</td>
<td align="right">1.5%</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,600</td>
<td align="right">30.8%</td>
<td align="right">1,400</td>
<td align="right">26.7%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">7,500</td>
<td align="right">41.3%</td>
<td align="right">2,360</td>
<td align="right">45.0%</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">180</td>
<td align="right">1.0%</td>
<td align="right">60</td>
<td align="right">1.1%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">0.7%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">620</td>
<td align="right">3.4%</td>
<td align="right">360</td>
<td align="right">6.9%</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">240</td>
<td align="right">1.3%</td>
<td align="right">160</td>
<td align="right">3.1%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">2.3%</td>
<td align="right">340</td>
<td align="right">6.5%</td>
<td align="right">-19.0%</td>
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
<td align="right">98,869,260</td>
<td align="right">100.0%</td>
<td align="right">-57.7%</td>
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
<td align="right">13,935,900</td>
<td align="right">12.6%</td>
<td align="right">-12.9%</td>
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
<td align="right">47,156,240</td>
<td align="right">42.7%</td>
<td align="right">-12.5%</td>
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
<td align="right">49,218,600</td>
<td align="right">44.6%</td>
<td align="right">4.6%</td>
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
<td align="right">8,200</td>
<td align="right">0.9%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,017,780</td>
<td align="right">98.9%</td>
<td align="right">890,380</td>
<td align="right">99.1%</td>
<td align="right">-12.5%</td>
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
<td align="right">220</td>
<td align="right">2.7%</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">8,860</td>
<td align="right">77.0%</td>
<td align="right">6,100</td>
<td align="right">74.4%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">17.7%</td>
<td align="right">1,640</td>
<td align="right">20.0%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">200</td>
<td align="right">1.7%</td>
<td align="right">200</td>
<td align="right">2.4%</td>
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
<td align="right">86,760</td>
<td align="right">100.0%</td>
<td align="right">58.0%</td>
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
<td align="right">4,577,200</td>
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
<td align="right">42,557,680</td>
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
<td align="right">3,845,080</td>
<td align="right">1.4%</td>
<td align="right">-31.7%</td>
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
<td align="right">2,110,500</td>
<td align="right">0.8%</td>
<td align="right">-13.2%</td>
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
<td align="right">263,731,800</td>
<td align="right">97.8%</td>
<td align="right">-1.1%</td>
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
<td align="right">73,400</td>
<td align="right">48.7%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">106,740</td>
<td align="right">49.9%</td>
<td align="right">77,340</td>
<td align="right">51.3%</td>
<td align="right">-27.5%</td>
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
<td align="right">32,720</td>
<td align="right">42.3%</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,040</td>
<td align="right">1.0%</td>
<td align="right">840</td>
<td align="right">1.1%</td>
<td align="right">-19.2%</td>
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
<td align="right">2,320</td>
<td align="right">3.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">41,540</td>
<td align="right">38.9%</td>
<td align="right">41,320</td>
<td align="right">53.4%</td>
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
<td align="right">1,001,090,240</td>
<td align="right">25.8%</td>
<td align="right">-46.1%</td>
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
<td align="right">99,337,240</td>
<td align="right">2.6%</td>
<td align="right">-39.9%</td>
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
<td align="right">2,496,612,000</td>
<td align="right">64.4%</td>
<td align="right">-27.7%</td>
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
<td align="right">278,137,200</td>
<td align="right">7.2%</td>
<td align="right">-16.6%</td>
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
<td align="right">5,772,660</td>
<td align="right">5.9%</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">91,947,120</td>
<td align="right">55.9%</td>
<td align="right">40,391,560</td>
<td align="right">40.9%</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">6,377,580</td>
<td align="right">3.9%</td>
<td align="right">3,132,280</td>
<td align="right">3.2%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,497,600</td>
<td align="right">0.9%</td>
<td align="right">859,060</td>
<td align="right">0.9%</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,322,560</td>
<td align="right">6.9%</td>
<td align="right">14,540,720</td>
<td align="right">14.7%</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,953,820</td>
<td align="right">3.0%</td>
<td align="right">3,963,640</td>
<td align="right">4.0%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,431,760</td>
<td align="right">1.5%</td>
<td align="right">2,110,500</td>
<td align="right">2.1%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,003,920</td>
<td align="right">9.7%</td>
<td align="right">13,935,900</td>
<td align="right">14.1%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,643,600</td>
<td align="right">5.9%</td>
<td align="right">9,283,480</td>
<td align="right">9.4%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,577,980</td>
<td align="right">2.8%</td>
<td align="right">4,577,200</td>
<td align="right">4.6%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">25,599,040</td>
<td align="right">7.7%</td>
<td align="right">7,350,680</td>
<td align="right">2.6%</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">46,429,620</td>
<td align="right">13.9%</td>
<td align="right">32,823,380</td>
<td align="right">11.8%</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">70,888,240</td>
<td align="right">21.3%</td>
<td align="right">58,688,600</td>
<td align="right">21.1%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">11,296,080</td>
<td align="right">3.4%</td>
<td align="right">13,117,820</td>
<td align="right">4.7%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">11,295,860</td>
<td align="right">3.4%</td>
<td align="right">13,116,460</td>
<td align="right">4.7%</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,131,440</td>
<td align="right">2.7%</td>
<td align="right">7,930,560</td>
<td align="right">2.9%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,912,180</td>
<td align="right">16.2%</td>
<td align="right">47,156,240</td>
<td align="right">17.0%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,144,720</td>
<td align="right">2.1%</td>
<td align="right">6,677,000</td>
<td align="right">2.4%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80,484,360</td>
<td align="right">24.1%</td>
<td align="right">77,032,880</td>
<td align="right">27.7%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,001,400</td>
<td align="right">1.2%</td>
<td align="right">3,980,520</td>
<td align="right">1.4%</td>
<td align="right">-0.5%</td>
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
<td align="right">7,982,200</td>
<td align="right">2.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">38,841,220</td>
<td align="right">11.0%</td>
<td align="right">38,806,840</td>
<td align="right">11.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">38,844,700</td>
<td align="right">11.0%</td>
<td align="right">38,810,320</td>
<td align="right">11.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,152,560</td>
<td align="right">11.0%</td>
<td align="right">39,118,180</td>
<td align="right">11.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,152,560</td>
<td align="right">11.0%</td>
<td align="right">39,118,180</td>
<td align="right">11.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">315,243,260</td>
<td align="right">89.0%</td>
<td align="right">315,277,640</td>
<td align="right">89.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,635,500</td>
<td align="right">88.5%</td>
<td align="right">313,638,360</td>
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
<td align="right">1,285,760</td>
<td align="right">0.2%</td>
<td align="right">87.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">3,332,423,522</td>
<td align="right">38.4%</td>
<td align="right">4,503,665,895</td>
<td align="right">50.1%</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">898,235,860</td>
<td align="right">10.3%</td>
<td align="right">585,325,420</td>
<td align="right">6.5%</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">3,059,440,518</td>
<td align="right">32.8%</td>
<td align="right">4,018,242,896</td>
<td align="right">41.0%</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,539,342,820</td>
<td align="right">29.2%</td>
<td align="right">1,776,876,600</td>
<td align="right">19.7%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">938,481,700</td>
<td align="right">10.1%</td>
<td align="right">682,387,160</td>
<td align="right">7.0%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,923,973,036</td>
<td align="right">20.6%</td>
<td align="right">2,251,623,962</td>
<td align="right">23.0%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,402,072,040</td>
<td align="right">36.5%</td>
<td align="right">2,852,437,460</td>
<td align="right">29.1%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,919,020,269</td>
<td align="right">22.1%</td>
<td align="right">2,131,196,422</td>
<td align="right">23.7%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,292,579</td>
<td align="right"></td>
<td align="right">2,111,817</td>
<td align="right"></td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">457,224,915</td>
<td align="right"></td>
<td align="right">436,657,119</td>
<td align="right"></td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">196,794,721</td>
<td align="right"></td>
<td align="right">189,461,403</td>
<td align="right"></td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">345,860</td>
<td align="right">0.0%</td>
<td align="right">352,280</td>
<td align="right">0.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">38,519,645</td>
<td align="right"></td>
<td align="right">39,015,441</td>
<td align="right"></td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">40,051,836</td>
<td align="right"></td>
<td align="right">40,366,870</td>
<td align="right"></td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">571,880,360</td>
<td align="right">70.7%</td>
<td align="right">572,676,480</td>
<td align="right">70.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">607,736,798</td>
<td align="right"></td>
<td align="right">608,328,162</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">570,847,920</td>
<td align="right">70.6%</td>
<td align="right">571,038,440</td>
<td align="right">70.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">236,866,720</td>
<td align="right">29.3%</td>
<td align="right">236,842,380</td>
<td align="right">29.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">236,838,460</td>
<td align="right"></td>
<td align="right">236,819,460</td>
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
<td align="right">25,940</td>
<td align="right">72,578,380</td>
<td align="right">1,454,111,180</td>
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
<td align="right">63,760</td>
<td align="right">4.9%</td>
<td align="right">834.9%</td>
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
<td align="right">528,040</td>
<td align="right">40.9%</td>
<td align="right">313.6%</td>
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
<td align="right">6,980</td>
<td align="right">0.5%</td>
<td align="right">301.1%</td>
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
<td align="right">1,041,120</td>
<td align="right">80.7%</td>
<td align="right">280.4%</td>
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
<td align="right">1,290,320</td>
<td align="right"></td>
<td align="right">243.0%</td>
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
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">175.0%</td>
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
<td align="right">248,800</td>
<td align="right">19.3%</td>
<td align="right">146.1%</td>
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
<td align="right">11,592,261,900</td>
<td align="right">1,303.5%</td>
<td align="right">71.3%</td>
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
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">-71.0%</td>
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
<td align="right">889,303,020</td>
<td align="right"></td>
<td align="right">65.3%</td>
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
<td align="right">5,900</td>
<td align="right">0.5%</td>
<td align="right">-16.2%</td>
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
<td align="right">256,000</td>
<td align="right">93.5%</td>
<td align="right">1,027,040</td>
<td align="right">98.6%</td>
<td align="right">301.2%</td>
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
<td align="right">1,041,120</td>
<td align="right"></td>
<td align="right">280.4%</td>
</tr>
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
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">133.3%</td>
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
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">80 / 0 !!</td>
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
<td align="right">8,060</td>
<td align="right">0.8%</td>
<td align="right">8,060 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">12,100</td>
<td align="right">4.4%</td>
<td align="right">36,060</td>
<td align="right">3.5%</td>
<td align="right">198.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">38,560</td>
<td align="right">14.1%</td>
<td align="right">106,940</td>
<td align="right">10.3%</td>
<td align="right">177.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">89,040</td>
<td align="right">32.5%</td>
<td align="right">398,180</td>
<td align="right">38.2%</td>
<td align="right">347.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">81,600</td>
<td align="right">29.8%</td>
<td align="right">309,120</td>
<td align="right">29.7%</td>
<td align="right">278.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">42,100</td>
<td align="right">15.4%</td>
<td align="right">138,180</td>
<td align="right">13.3%</td>
<td align="right">228.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">8,360</td>
<td align="right">3.1%</td>
<td align="right">36,560</td>
<td align="right">3.5%</td>
<td align="right">337.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,860</td>
<td align="right">0.7%</td>
<td align="right">8,020</td>
<td align="right">0.8%</td>
<td align="right">331.2%</td>
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
<td align="right">34,560</td>
<td align="right">3.3%</td>
<td align="right">363.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">25,620</td>
<td align="right">9.4%</td>
<td align="right">41,020</td>
<td align="right">3.9%</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">51,060</td>
<td align="right">18.7%</td>
<td align="right">246,240</td>
<td align="right">23.7%</td>
<td align="right">382.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">104,200</td>
<td align="right">38.1%</td>
<td align="right">411,260</td>
<td align="right">39.5%</td>
<td align="right">294.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">49,240</td>
<td align="right">18.0%</td>
<td align="right">218,720</td>
<td align="right">21.0%</td>
<td align="right">344.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">14,960</td>
<td align="right">5.5%</td>
<td align="right">58,700</td>
<td align="right">5.6%</td>
<td align="right">292.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,900</td>
<td align="right">1.1%</td>
<td align="right">15,940</td>
<td align="right">1.5%</td>
<td align="right">449.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">560</td>
<td align="right">0.2%</td>
<td align="right">600</td>
<td align="right">0.1%</td>
<td align="right">7.1%</td>
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
<td align="right">2,603,540</td>
<td align="right">3,254,325.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">540</td>
<td align="right">1,831,560</td>
<td align="right">339,077.8%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">540</td>
<td align="right">1,828,620</td>
<td align="right">338,533.3%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">7,440</td>
<td align="right">3,906,780</td>
<td align="right">52,410.5%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">23,580</td>
<td align="right">3,424,640</td>
<td align="right">14,423.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">600</td>
<td align="right">44,040</td>
<td align="right">7,240.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">273,600</td>
<td align="right">7,161,100</td>
<td align="right">2,517.4%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">455,040</td>
<td align="right">10,785,480</td>
<td align="right">2,270.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">32,420</td>
<td align="right">706,060</td>
<td align="right">2,077.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">699,460</td>
<td align="right">13,036,680</td>
<td align="right">1,763.8%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,225,560</td>
<td align="right">21,744,620</td>
<td align="right">1,674.3%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,225,560</td>
<td align="right">21,744,620</td>
<td align="right">1,674.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">51,360</td>
<td align="right">668,980</td>
<td align="right">1,202.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">199,520</td>
<td align="right">2,529,740</td>
<td align="right">1,167.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">2,117,800</td>
<td align="right">26,230,260</td>
<td align="right">1,138.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,117,800</td>
<td align="right">26,230,260</td>
<td align="right">1,138.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">22,878,680</td>
<td align="right">254,825,520</td>
<td align="right">1,013.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,284,680</td>
<td align="right">13,271,040</td>
<td align="right">933.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">42,440</td>
<td align="right">399,080</td>
<td align="right">840.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,829,240</td>
<td align="right">14,277,160</td>
<td align="right">680.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">6,645,720</td>
<td align="right">51,537,400</td>
<td align="right">675.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">6,272,400</td>
<td align="right">42,328,480</td>
<td align="right">574.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">3,367,220</td>
<td align="right">20,121,980</td>
<td align="right">497.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,487,100</td>
<td align="right">22,690,720</td>
<td align="right">405.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">5,322,020</td>
<td align="right">26,735,560</td>
<td align="right">402.4%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">119,420</td>
<td align="right">566,060</td>
<td align="right">374.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,434,120</td>
<td align="right">11,208,840</td>
<td align="right">360.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">238,580</td>
<td align="right">1,078,520</td>
<td align="right">352.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">600,380</td>
<td align="right">2,704,560</td>
<td align="right">350.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">3,910,640</td>
<td align="right">15,439,480</td>
<td align="right">294.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">514,740</td>
<td align="right">1,865,680</td>
<td align="right">262.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,298,180</td>
<td align="right">13,821,300</td>
<td align="right">221.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">6,983,080</td>
<td align="right">22,106,300</td>
<td align="right">216.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">864,060</td>
<td align="right">2,717,360</td>
<td align="right">214.5%</td>
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
<td align="right">19,429,940</td>
<td align="right">202.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">45,258,740</td>
<td align="right">135,401,240</td>
<td align="right">199.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">12,562,420</td>
<td align="right">36,057,680</td>
<td align="right">187.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,748,620</td>
<td align="right">4,994,740</td>
<td align="right">185.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">9,191,480</td>
<td align="right">25,674,960</td>
<td align="right">179.3%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">324,920</td>
<td align="right">890,560</td>
<td align="right">174.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,251,620</td>
<td align="right">6,170,080</td>
<td align="right">174.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">309,120</td>
<td align="right">820,980</td>
<td align="right">165.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">11,263,820</td>
<td align="right">29,598,500</td>
<td align="right">162.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">39,214,360</td>
<td align="right">100,560,400</td>
<td align="right">156.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,306,120</td>
<td align="right">3,285,160</td>
<td align="right">151.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">186,893,140</td>
<td align="right">469,933,600</td>
<td align="right">151.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">60,151,920</td>
<td align="right">151,221,580</td>
<td align="right">151.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">38,583,880</td>
<td align="right">94,123,900</td>
<td align="right">143.9%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,092,460</td>
<td align="right">7,484,840</td>
<td align="right">142.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">242,940</td>
<td align="right">580,100</td>
<td align="right">138.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">36,620,820</td>
<td align="right">86,351,220</td>
<td align="right">135.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">2,237,540</td>
<td align="right">5,240,480</td>
<td align="right">134.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">2,236,460</td>
<td align="right">5,235,600</td>
<td align="right">134.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">4,094,640</td>
<td align="right">9,528,460</td>
<td align="right">132.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">5,958,360</td>
<td align="right">13,796,300</td>
<td align="right">131.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">14,174,540</td>
<td align="right">32,814,220</td>
<td align="right">131.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">36,148,180</td>
<td align="right">82,914,580</td>
<td align="right">129.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">33,950,040</td>
<td align="right">77,338,580</td>
<td align="right">127.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">5,880</td>
<td align="right">13,000</td>
<td align="right">121.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">3,957,520</td>
<td align="right">8,714,180</td>
<td align="right">120.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">34,420,960</td>
<td align="right">75,253,800</td>
<td align="right">118.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">126,365,780</td>
<td align="right">274,561,400</td>
<td align="right">117.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">60,487,020</td>
<td align="right">131,097,000</td>
<td align="right">116.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">277,580</td>
<td align="right">588,600</td>
<td align="right">112.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">277,580</td>
<td align="right">588,600</td>
<td align="right">112.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">16,378,020</td>
<td align="right">34,546,620</td>
<td align="right">110.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,088,140</td>
<td align="right">12,609,100</td>
<td align="right">107.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">9,412,180</td>
<td align="right">19,333,160</td>
<td align="right">105.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">21,850,820</td>
<td align="right">44,811,760</td>
<td align="right">105.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,171,900</td>
<td align="right">20,599,780</td>
<td align="right">102.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">10,514,200</td>
<td align="right">21,272,900</td>
<td align="right">102.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">15,743,220</td>
<td align="right">31,611,460</td>
<td align="right">100.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">15,806,480</td>
<td align="right">31,721,940</td>
<td align="right">100.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,454,400</td>
<td align="right">10,946,260</td>
<td align="right">100.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">22,031,120</td>
<td align="right">43,801,340</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">56,813,340</td>
<td align="right">1,124,720</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">10,204,940</td>
<td align="right">20,111,620</td>
<td align="right">97.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">35,225,560</td>
<td align="right">67,628,900</td>
<td align="right">92.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">420,776,220</td>
<td align="right">805,325,780</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">66,920,120</td>
<td align="right">127,954,120</td>
<td align="right">91.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">263,380</td>
<td align="right">23,880</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">44,059,840</td>
<td align="right">83,922,820</td>
<td align="right">90.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">8,004,840</td>
<td align="right">15,105,960</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">110,169,680</td>
<td align="right">206,200,460</td>
<td align="right">87.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">110,136,300</td>
<td align="right">206,042,260</td>
<td align="right">87.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">71,310,660</td>
<td align="right">133,005,460</td>
<td align="right">86.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">72,638,580</td>
<td align="right">135,312,900</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">29,823,900</td>
<td align="right">55,252,160</td>
<td align="right">85.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">26,261,440</td>
<td align="right">48,579,900</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">694,360</td>
<td align="right">1,281,000</td>
<td align="right">84.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">81,221,400</td>
<td align="right">147,314,300</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">108,236,320</td>
<td align="right">194,955,620</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">7,681,340</td>
<td align="right">13,709,880</td>
<td align="right">78.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,476,360</td>
<td align="right">14,958,440</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">22,293,220</td>
<td align="right">38,972,320</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">2,560</td>
<td align="right">680</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">18,447,620</td>
<td align="right">31,944,120</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">106,957,940</td>
<td align="right">183,030,600</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">53,618,260</td>
<td align="right">90,755,460</td>
<td align="right">69.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">537,871,880</td>
<td align="right">889,303,020</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">5,572,060</td>
<td align="right">9,198,680</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">505,024,020</td>
<td align="right">830,776,200</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">26,838,140</td>
<td align="right">44,061,540</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,510,360</td>
<td align="right">2,446,040</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">157,680</td>
<td align="right">252,660</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">107,832,200</td>
<td align="right">172,286,180</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">586,354,400</td>
<td align="right">931,973,380</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">44,331,800</td>
<td align="right">69,897,200</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">5,721,240</td>
<td align="right">8,966,540</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">525,620</td>
<td align="right">821,440</td>
<td align="right">56.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">535,847,040</td>
<td align="right">835,602,400</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,412,340</td>
<td align="right">19,297,080</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">4,139,320</td>
<td align="right">6,434,100</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">3,361,980</td>
<td align="right">1,556,520</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">432,374,380</td>
<td align="right">663,100,280</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,376,080</td>
<td align="right">2,037,960</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">49,350,160</td>
<td align="right">72,869,420</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">28,503,000</td>
<td align="right">41,953,140</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">258,040</td>
<td align="right">375,520</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">3,880,980</td>
<td align="right">5,590,440</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">24,615,580</td>
<td align="right">35,214,080</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">1,798,360</td>
<td align="right">2,563,020</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">875,000</td>
<td align="right">1,238,180</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">16,281,420</td>
<td align="right">22,818,140</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">16,281,420</td>
<td align="right">22,817,960</td>
<td align="right">40.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">842,120</td>
<td align="right">1,159,700</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">6,312,040</td>
<td align="right">8,677,540</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">10,148,000</td>
<td align="right">13,697,440</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">1,645,780</td>
<td align="right">2,204,660</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">9,730,300</td>
<td align="right">6,512,140</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">472,280</td>
<td align="right">622,940</td>
<td align="right">31.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">482,540</td>
<td align="right">626,960</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">37,480,860</td>
<td align="right">26,346,720</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">31,353,660</td>
<td align="right">39,535,620</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">44,520,260</td>
<td align="right">55,810,100</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">211,560</td>
<td align="right">265,100</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">243,124,320</td>
<td align="right">304,293,280</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">38,094,800</td>
<td align="right">46,689,280</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">97,046,380</td>
<td align="right">117,393,380</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">15,523,540</td>
<td align="right">18,423,520</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">43,472,480</td>
<td align="right">50,440,980</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">212,200</td>
<td align="right">180,360</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">16,811,340</td>
<td align="right">19,128,820</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">16,571,360</td>
<td align="right">18,841,000</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">7,239,440</td>
<td align="right">8,229,620</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">48,482,520</td>
<td align="right">42,670,360</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">352,900</td>
<td align="right">389,140</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">35,995,560</td>
<td align="right">39,528,320</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">964,980</td>
<td align="right">1,055,800</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">119,976,380</td>
<td align="right">109,461,980</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">103,140,340</td>
<td align="right">94,110,020</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">95,905,660</td>
<td align="right">88,499,980</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">13,549,500</td>
<td align="right">14,483,560</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,063,420</td>
<td align="right">4,319,060</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">34,323,640</td>
<td align="right">36,306,860</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">3,138,940</td>
<td align="right">3,292,880</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">3,138,940</td>
<td align="right">3,292,880</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,800,900</td>
<td align="right">2,937,520</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">18,621,260</td>
<td align="right">19,394,320</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">995,260</td>
<td align="right">1,035,080</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">995,260</td>
<td align="right">1,035,080</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">47,440,740</td>
<td align="right">49,315,640</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">21,800</td>
<td align="right">22,580</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">21,800</td>
<td align="right">22,580</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">13,661,240</td>
<td align="right">13,266,900</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">18,353,860</td>
<td align="right">18,845,780</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,221,980</td>
<td align="right">2,165,860</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">14,236,020</td>
<td align="right">14,569,940</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">63,400</td>
<td align="right">61,920</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">55,798,680</td>
<td align="right">54,714,960</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">17,163,480</td>
<td align="right">17,440,740</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">72,314,240</td>
<td align="right">72,887,400</td>
<td align="right">0.8%</td>
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
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">7,434,820</td>
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
<td align="right">143,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">143,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right"></td>
<td align="right">140,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right"></td>
<td align="right">85,780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">75,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">56,480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right"></td>
<td align="right">49,980</td>
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
<td align="left">_DELETE_ATTR</td>
<td align="right"></td>
<td align="right">3,360</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">3,180</td>
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
<td align="right">340</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">340</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right"></td>
<td align="right">120</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">40</td>
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
<td align="right">49,060</td>
<td align="right">493.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,540</td>
<td align="right">6,340</td>
<td align="right">311.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,760</td>
<td align="right">4,860</td>
<td align="right">29.3%</td>
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
