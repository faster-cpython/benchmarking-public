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
<td align="right">96,145,000</td>
<td align="right">179.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">513,300</td>
<td align="right">560</td>
<td align="right">-99.9%</td>
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
<td align="right">182,420</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">609,760</td>
<td align="right">43,920</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">4,482,700</td>
<td align="right">366,800</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">397,900</td>
<td align="right">37,300</td>
<td align="right">-90.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">156,900</td>
<td align="right">15,700</td>
<td align="right">-90.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">3,300</td>
<td align="right">360</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">6,583,240</td>
<td align="right">754,860</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">318,480</td>
<td align="right">46,920</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">4,036,100</td>
<td align="right">761,340</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">20,454,940</td>
<td align="right">4,127,480</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,170,180</td>
<td align="right">862,000</td>
<td align="right">-79.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">16,367,600</td>
<td align="right">3,555,980</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">12,876,340</td>
<td align="right">2,998,180</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">28,338,040</td>
<td align="right">7,058,100</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">237,587,100</td>
<td align="right">62,069,460</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">61,102,920</td>
<td align="right">16,520,720</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">902,760</td>
<td align="right">246,480</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">28,982,340</td>
<td align="right">8,384,080</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">28,982,400</td>
<td align="right">8,384,140</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,262,360</td>
<td align="right">950,780</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">14,643,960</td>
<td align="right">4,272,580</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">21,765,300</td>
<td align="right">6,722,380</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">32,948,000</td>
<td align="right">10,378,540</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,966,200</td>
<td align="right">629,060</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,730,960</td>
<td align="right">897,120</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,727,900</td>
<td align="right">897,000</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">18,090,460</td>
<td align="right">6,085,340</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">32,133,640</td>
<td align="right">11,075,880</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">62,668,500</td>
<td align="right">22,153,720</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">228,720</td>
<td align="right">84,160</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">54,920</td>
<td align="right">88,980</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,795,080</td>
<td align="right">6,205,240</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">14,700</td>
<td align="right">5,880</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">38,786,620</td>
<td align="right">15,601,620</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">11,142,760</td>
<td align="right">4,711,740</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">7,119,760</td>
<td align="right">3,151,200</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">92,573,100</td>
<td align="right">41,355,040</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,139,100</td>
<td align="right">3,253,340</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">171,192,180</td>
<td align="right">78,221,520</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">110,649,840</td>
<td align="right">51,287,960</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">9,850,380</td>
<td align="right">4,653,000</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">44,367,520</td>
<td align="right">21,064,180</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,456,320</td>
<td align="right">5,578,260</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">323,000</td>
<td align="right">158,420</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">143,808,880</td>
<td align="right">216,857,860</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,880</td>
<td align="right">2,940</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">36,535,020</td>
<td align="right">18,500,520</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">6,127,760</td>
<td align="right">3,143,200</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,591,840</td>
<td align="right">824,220</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">6,377,580</td>
<td align="right">3,417,200</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">524,720</td>
<td align="right">764,200</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,509,320</td>
<td align="right">823,900</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">332,160</td>
<td align="right">187,420</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">38,323,880</td>
<td align="right">21,709,020</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">283,271,980</td>
<td align="right">162,274,940</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,576,800</td>
<td align="right">2,637,580</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,315,620</td>
<td align="right">9,550,480</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">44,944,480</td>
<td align="right">26,379,300</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">13,066,200</td>
<td align="right">7,687,620</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">227,476,360</td>
<td align="right">134,141,320</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,155,535,920</td>
<td align="right">684,712,160</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">65,414,920</td>
<td align="right">38,995,080</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">209,986,600</td>
<td align="right">125,211,260</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">216,486,740</td>
<td align="right">131,131,360</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,869,460</td>
<td align="right">6,747,640</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">7,284,780</td>
<td align="right">4,631,760</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">23,810,440</td>
<td align="right">15,376,340</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,739,780</td>
<td align="right">11,571,920</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">158,653,360</td>
<td align="right">106,658,920</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">130,789,360</td>
<td align="right">88,539,280</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,567,160</td>
<td align="right">13,319,140</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">68,279,540</td>
<td align="right">46,610,040</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,217,800</td>
<td align="right">62,287,980</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">149,700</td>
<td align="right">102,460</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,400</td>
<td align="right">8,000</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">149,951,420</td>
<td align="right">106,920,600</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">61,141,600</td>
<td align="right">43,807,920</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,436,800</td>
<td align="right">3,192,320</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,332,440</td>
<td align="right">14,471,580</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">30,387,980</td>
<td align="right">22,234,660</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">142,467,800</td>
<td align="right">104,387,300</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,847,920</td>
<td align="right">5,121,360</td>
<td align="right">-25.2%</td>
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
<td align="right">78,399,440</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">582,560</td>
<td align="right">464,080</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">11,206,460</td>
<td align="right">8,991,720</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,235,240</td>
<td align="right">1,802,920</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">13,348,980</td>
<td align="right">11,092,900</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,709,900</td>
<td align="right">2,278,140</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,043,800</td>
<td align="right">879,060</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">106,869,580</td>
<td align="right">92,009,100</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,957,780</td>
<td align="right">4,270,240</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">17,789,000</td>
<td align="right">15,399,260</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,015,820</td>
<td align="right">13,994,320</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">61,467,280</td>
<td align="right">69,215,320</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">230,880</td>
<td align="right">204,140</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">38,371,060</td>
<td align="right">34,182,440</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,404,280</td>
<td align="right">4,874,800</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">17,666,400</td>
<td align="right">15,920,460</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">9,856,740</td>
<td align="right">8,934,240</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">319,340</td>
<td align="right">289,560</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,942,860</td>
<td align="right">2,720,960</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">450,860</td>
<td align="right">419,120</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,742,740</td>
<td align="right">2,572,140</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,401,960</td>
<td align="right">2,257,520</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">140,003,200</td>
<td align="right">132,121,540</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,218,980</td>
<td align="right">8,705,500</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">840</td>
<td align="right">880</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">38,337,840</td>
<td align="right">39,898,920</td>
<td align="right">4.1%</td>
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
<td align="right">2,080</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,412,120</td>
<td align="right">8,087,940</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,656,580</td>
<td align="right">9,353,840</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,539,400</td>
<td align="right">2,466,240</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">71,060</td>
<td align="right">73,040</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">28,174,320</td>
<td align="right">27,596,600</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">207,128,180</td>
<td align="right">210,444,000</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">159,814,580</td>
<td align="right">157,971,760</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">35,280</td>
<td align="right">35,000</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">6,660</td>
<td align="right">6,700</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,129,960</td>
<td align="right">9,156,780</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,254,620</td>
<td align="right">1,257,880</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,110,600</td>
<td align="right">38,173,280</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,449,640</td>
<td align="right">1,447,640</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,113,900</td>
<td align="right">37,070,520</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,581,860</td>
<td align="right">4,580,840</td>
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
<td align="right">14,461,420</td>
<td align="right">23.0%</td>
<td align="right">27.7%</td>
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
<td align="right">77.0%</td>
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
<td align="right">9,940</td>
<td align="right">97.8%</td>
<td align="right">2.9%</td>
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
<td align="right">3,260</td>
<td align="right">32.8%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,180</td>
<td align="right">32.9%</td>
<td align="right">2,920</td>
<td align="right">29.4%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">32.7%</td>
<td align="right">3,060</td>
<td align="right">30.8%</td>
<td align="right">-3.2%</td>
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
<td align="right">3,417,200</td>
<td align="right">100.0%</td>
<td align="right">-46.4%</td>
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
<td align="right">9,340,700</td>
<td align="right">8.9%</td>
<td align="right">-3.1%</td>
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
<td align="right">2,143,580</td>
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
<td align="right">93,957,080</td>
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
<td align="right">12,520</td>
<td align="right">23.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,100</td>
<td align="right">76.9%</td>
<td align="right">41,060</td>
<td align="right">76.6%</td>
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
<td align="right">75.7%</td>
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
<td align="right">1,640</td>
<td align="right">13.1%</td>
<td align="right">-1.2%</td>
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
<td align="right">15,640,760</td>
<td align="right">2.7%</td>
<td align="right">-5.9%</td>
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
<td align="right">555,589,620</td>
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
<td align="right">299,160</td>
<td align="right">100.0%</td>
<td align="right">-5.8%</td>
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
<td align="right">818,180</td>
<td align="right">2.3%</td>
<td align="right">-45.4%</td>
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
<td align="right">97.4%</td>
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
<td align="right">5,360</td>
<td align="right">70.0%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,500</td>
<td align="right">28.4%</td>
<td align="right">2,300</td>
<td align="right">30.0%</td>
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
<td align="right">4,940</td>
<td align="right">92.2%</td>
<td align="right">-54.7%</td>
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
<td align="right">4,266,820</td>
<td align="right">7.3%</td>
<td align="right">-13.9%</td>
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
<td align="right">92.7%</td>
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
<td align="right">3,300</td>
<td align="right">96.5%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">3.0%</td>
<td align="right">120</td>
<td align="right">3.5%</td>
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
<td align="right">440</td>
<td align="right">13.3%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">20.8%</td>
<td align="right">520</td>
<td align="right">15.8%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">880</td>
<td align="right">22.9%</td>
<td align="right">600</td>
<td align="right">18.2%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,480</td>
<td align="right">38.5%</td>
<td align="right">1,740</td>
<td align="right">52.7%</td>
<td align="right">17.6%</td>
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
<td align="right">6,202,860</td>
<td align="right">4.4%</td>
<td align="right">-60.7%</td>
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
<td align="right">25,367,160</td>
<td align="right">18.2%</td>
<td align="right">12.3%</td>
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
<td align="right">107,941,060</td>
<td align="right">77.4%</td>
<td align="right">-3.0%</td>
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
<td align="right">2,380</td>
<td align="right">0.5%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">426,260</td>
<td align="right">98.9%</td>
<td align="right">478,580</td>
<td align="right">99.5%</td>
<td align="right">12.3%</td>
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
<td align="right">480</td>
<td align="right">20.2%</td>
<td align="right">700.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,480</td>
<td align="right">51.7%</td>
<td align="right">160</td>
<td align="right">6.7%</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">180</td>
<td align="right">3.8%</td>
<td align="right">60</td>
<td align="right">2.5%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">680</td>
<td align="right">14.2%</td>
<td align="right">240</td>
<td align="right">10.1%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">360</td>
<td align="right">7.5%</td>
<td align="right">420</td>
<td align="right">17.6%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">800</td>
<td align="right">16.7%</td>
<td align="right">880</td>
<td align="right">37.0%</td>
<td align="right">10.0%</td>
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
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.8%</td>
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
<td align="right">91,947,120</td>
<td align="right">9.4%</td>
<td align="right">40,802,780</td>
<td align="right">4.6%</td>
<td align="right">-55.6%</td>
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
<td align="right">182,036,400</td>
<td align="right">20.4%</td>
<td align="right">-21.7%</td>
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
<td align="right">667,816,480</td>
<td align="right">74.9%</td>
<td align="right">2.9%</td>
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
<td align="right">5,380</td>
<td align="right">0.1%</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">4,992,020</td>
<td align="right">99.6%</td>
<td align="right">3,981,380</td>
<td align="right">99.9%</td>
<td align="right">-20.2%</td>
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
<td align="right">4.8%</td>
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
<td align="right">26.0%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">7,500</td>
<td align="right">41.3%</td>
<td align="right">2,420</td>
<td align="right">45.0%</td>
<td align="right">-67.7%</td>
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
<td align="right">0.7%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">620</td>
<td align="right">3.4%</td>
<td align="right">380</td>
<td align="right">7.1%</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">2.3%</td>
<td align="right">340</td>
<td align="right">6.3%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">240</td>
<td align="right">1.3%</td>
<td align="right">220</td>
<td align="right">4.1%</td>
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
<td align="right">100,373,760</td>
<td align="right">100.0%</td>
<td align="right">-57.1%</td>
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
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">2,100</td>
<td align="right">100.0%</td>
<td align="right">2.9%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,915,360</td>
<td align="right">46.1%</td>
<td align="right">46,878,120</td>
<td align="right">42.9%</td>
<td align="right">-13.1%</td>
</tr>
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
<td align="right">13,985,720</td>
<td align="right">12.8%</td>
<td align="right">-12.6%</td>
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
<td align="right">48,313,080</td>
<td align="right">44.2%</td>
<td align="right">2.7%</td>
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
<td align="right">8,160</td>
<td align="right">0.9%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,017,780</td>
<td align="right">98.9%</td>
<td align="right">885,180</td>
<td align="right">99.1%</td>
<td align="right">-13.0%</td>
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
<td align="right">6,080</td>
<td align="right">74.5%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">17.7%</td>
<td align="right">1,640</td>
<td align="right">20.1%</td>
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
<td align="right">88,980</td>
<td align="right">100.0%</td>
<td align="right">62.0%</td>
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
<td align="right">4,576,940</td>
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
<td align="right">3,822,740</td>
<td align="right">1.4%</td>
<td align="right">-32.1%</td>
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
<td align="right">2,391,200</td>
<td align="right">0.9%</td>
<td align="right">-1.7%</td>
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
<td align="right">263,897,280</td>
<td align="right">97.7%</td>
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
<td align="left">Success</td>
<td align="right">107,060</td>
<td align="right">50.1%</td>
<td align="right">72,940</td>
<td align="right">49.6%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">106,740</td>
<td align="right">49.9%</td>
<td align="right">74,240</td>
<td align="right">50.4%</td>
<td align="right">-30.4%</td>
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
<td align="right">29,480</td>
<td align="right">39.7%</td>
<td align="right">-52.2%</td>
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
<td align="left">dict</td>
<td align="right">1,040</td>
<td align="right">1.0%</td>
<td align="right">1,000</td>
<td align="right">1.3%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,360</td>
<td align="right">2.2%</td>
<td align="right">2,300</td>
<td align="right">3.1%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">41,540</td>
<td align="right">38.9%</td>
<td align="right">41,320</td>
<td align="right">55.7%</td>
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
<td align="right">1,005,493,380</td>
<td align="right">25.8%</td>
<td align="right">-45.8%</td>
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
<td align="right">101,034,100</td>
<td align="right">2.6%</td>
<td align="right">-38.9%</td>
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
<td align="right">2,508,437,960</td>
<td align="right">64.5%</td>
<td align="right">-27.4%</td>
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
<td align="right">276,009,820</td>
<td align="right">7.1%</td>
<td align="right">-17.2%</td>
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
<td align="right">6,202,860</td>
<td align="right">6.2%</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">91,947,120</td>
<td align="right">55.9%</td>
<td align="right">40,802,780</td>
<td align="right">40.7%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">6,377,580</td>
<td align="right">3.9%</td>
<td align="right">3,417,200</td>
<td align="right">3.4%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,497,600</td>
<td align="right">0.9%</td>
<td align="right">818,180</td>
<td align="right">0.8%</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,322,560</td>
<td align="right">6.9%</td>
<td align="right">14,461,420</td>
<td align="right">14.4%</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,953,820</td>
<td align="right">3.0%</td>
<td align="right">4,266,820</td>
<td align="right">4.3%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,003,920</td>
<td align="right">9.7%</td>
<td align="right">13,985,720</td>
<td align="right">13.9%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,643,600</td>
<td align="right">5.9%</td>
<td align="right">9,340,700</td>
<td align="right">9.3%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,431,760</td>
<td align="right">1.5%</td>
<td align="right">2,391,200</td>
<td align="right">2.4%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,577,980</td>
<td align="right">2.8%</td>
<td align="right">4,576,940</td>
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
<td align="right">7,397,900</td>
<td align="right">2.7%</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">46,429,620</td>
<td align="right">13.9%</td>
<td align="right">32,792,500</td>
<td align="right">11.9%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">70,888,240</td>
<td align="right">21.3%</td>
<td align="right">57,276,840</td>
<td align="right">20.8%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,912,180</td>
<td align="right">16.2%</td>
<td align="right">46,878,120</td>
<td align="right">17.0%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">11,296,080</td>
<td align="right">3.4%</td>
<td align="right">12,684,280</td>
<td align="right">4.6%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">11,295,860</td>
<td align="right">3.4%</td>
<td align="right">12,682,880</td>
<td align="right">4.6%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,131,440</td>
<td align="right">2.7%</td>
<td align="right">8,128,300</td>
<td align="right">2.9%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">80,484,360</td>
<td align="right">24.1%</td>
<td align="right">76,585,940</td>
<td align="right">27.7%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,144,720</td>
<td align="right">2.1%</td>
<td align="right">7,211,940</td>
<td align="right">2.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,001,400</td>
<td align="right">1.2%</td>
<td align="right">4,036,700</td>
<td align="right">1.5%</td>
<td align="right">0.9%</td>
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
<td align="right">8,079,660</td>
<td align="right">2.3%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">38,841,220</td>
<td align="right">11.0%</td>
<td align="right">38,903,900</td>
<td align="right">11.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">38,844,700</td>
<td align="right">11.0%</td>
<td align="right">38,907,380</td>
<td align="right">11.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,152,560</td>
<td align="right">11.0%</td>
<td align="right">39,215,240</td>
<td align="right">11.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,152,560</td>
<td align="right">11.0%</td>
<td align="right">39,215,240</td>
<td align="right">11.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">315,243,260</td>
<td align="right">89.0%</td>
<td align="right">315,180,580</td>
<td align="right">88.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,635,500</td>
<td align="right">88.5%</td>
<td align="right">313,638,760</td>
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
<td align="right">1,291,400</td>
<td align="right">0.2%</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">3,328,732,966</td>
<td align="right">38.3%</td>
<td align="right">4,501,710,728</td>
<td align="right">50.0%</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">898,235,860</td>
<td align="right">10.3%</td>
<td align="right">591,135,200</td>
<td align="right">6.6%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,549,762</td>
<td align="right"></td>
<td align="right">1,686,347</td>
<td align="right"></td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">3,055,750,091</td>
<td align="right">32.8%</td>
<td align="right">4,017,214,688</td>
<td align="right">40.9%</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,539,342,820</td>
<td align="right">29.2%</td>
<td align="right">1,785,109,460</td>
<td align="right">19.8%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">938,481,700</td>
<td align="right">10.1%</td>
<td align="right">685,957,020</td>
<td align="right">7.0%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,920,425,891</td>
<td align="right">20.6%</td>
<td align="right">2,249,186,210</td>
<td align="right">22.9%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,402,072,040</td>
<td align="right">36.5%</td>
<td align="right">2,859,835,460</td>
<td align="right">29.1%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,915,473,252</td>
<td align="right">22.1%</td>
<td align="right">2,124,732,805</td>
<td align="right">23.6%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">461,100,885</td>
<td align="right"></td>
<td align="right">440,620,883</td>
<td align="right"></td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">34,643,675</td>
<td align="right"></td>
<td align="right">35,929,937</td>
<td align="right"></td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">345,860</td>
<td align="right">0.0%</td>
<td align="right">356,340</td>
<td align="right">0.0%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">196,537,538</td>
<td align="right"></td>
<td align="right">190,612,273</td>
<td align="right"></td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">36,432,900</td>
<td align="right"></td>
<td align="right">36,856,087</td>
<td align="right"></td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">571,880,360</td>
<td align="right">70.7%</td>
<td align="right">572,819,760</td>
<td align="right">70.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">607,736,916</td>
<td align="right"></td>
<td align="right">608,537,920</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">236,866,720</td>
<td align="right">29.3%</td>
<td align="right">236,720,580</td>
<td align="right">29.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">570,847,920</td>
<td align="right">70.6%</td>
<td align="right">571,172,020</td>
<td align="right">70.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">236,838,460</td>
<td align="right"></td>
<td align="right">236,708,700</td>
<td align="right"></td>
<td align="right">-0.1%</td>
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
<td align="right">25,980</td>
<td align="right">72,608,220</td>
<td align="right">1,456,689,240</td>
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
<td align="right">64,400</td>
<td align="right">4.8%</td>
<td align="right">844.3%</td>
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
<td align="right">10,080</td>
<td align="right">0.8%</td>
<td align="right">479.3%</td>
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
<td align="right">549,760</td>
<td align="right">41.4%</td>
<td align="right">330.6%</td>
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
<td align="right">1,065,560</td>
<td align="right">80.2%</td>
<td align="right">289.3%</td>
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
<td align="right">1,327,840</td>
<td align="right"></td>
<td align="right">253.0%</td>
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
<td align="right">261,900</td>
<td align="right">19.7%</td>
<td align="right">159.1%</td>
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
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">125.0%</td>
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
<td align="right">380</td>
<td align="right">0.0%</td>
<td align="right">-72.5%</td>
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
<td align="right">11,599,687,040</td>
<td align="right">1,300.0%</td>
<td align="right">71.4%</td>
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
<td align="right">892,279,960</td>
<td align="right"></td>
<td align="right">65.9%</td>
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
<td align="right">6,040</td>
<td align="right">0.5%</td>
<td align="right">-14.2%</td>
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
<td align="right">1,048,800</td>
<td align="right">98.4%</td>
<td align="right">309.7%</td>
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
<td align="right">1,065,560</td>
<td align="right"></td>
<td align="right">289.3%</td>
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
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">233.3%</td>
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
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">120 / 0 !!</td>
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
<td align="right">8,480</td>
<td align="right">0.8%</td>
<td align="right">8,480 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">12,100</td>
<td align="right">4.4%</td>
<td align="right">38,060</td>
<td align="right">3.6%</td>
<td align="right">214.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">38,560</td>
<td align="right">14.1%</td>
<td align="right">111,840</td>
<td align="right">10.5%</td>
<td align="right">190.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">89,040</td>
<td align="right">32.5%</td>
<td align="right">401,120</td>
<td align="right">37.6%</td>
<td align="right">350.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">81,600</td>
<td align="right">29.8%</td>
<td align="right">316,100</td>
<td align="right">29.7%</td>
<td align="right">287.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">42,100</td>
<td align="right">15.4%</td>
<td align="right">142,540</td>
<td align="right">13.4%</td>
<td align="right">238.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">8,360</td>
<td align="right">3.1%</td>
<td align="right">34,420</td>
<td align="right">3.2%</td>
<td align="right">311.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,860</td>
<td align="right">0.7%</td>
<td align="right">13,000</td>
<td align="right">1.2%</td>
<td align="right">598.9%</td>
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
<td align="right">36,460</td>
<td align="right">3.4%</td>
<td align="right">388.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">25,620</td>
<td align="right">9.4%</td>
<td align="right">44,320</td>
<td align="right">4.2%</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">51,060</td>
<td align="right">18.7%</td>
<td align="right">253,120</td>
<td align="right">23.8%</td>
<td align="right">395.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">104,200</td>
<td align="right">38.1%</td>
<td align="right">416,400</td>
<td align="right">39.1%</td>
<td align="right">299.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">49,240</td>
<td align="right">18.0%</td>
<td align="right">220,580</td>
<td align="right">20.7%</td>
<td align="right">348.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">14,960</td>
<td align="right">5.5%</td>
<td align="right">61,620</td>
<td align="right">5.8%</td>
<td align="right">311.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,900</td>
<td align="right">1.1%</td>
<td align="right">15,780</td>
<td align="right">1.5%</td>
<td align="right">444.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">560</td>
<td align="right">0.2%</td>
<td align="right">520</td>
<td align="right">0.0%</td>
<td align="right">-7.1%</td>
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
<td align="right">2,442,920</td>
<td align="right">3,053,550.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">540</td>
<td align="right">1,834,380</td>
<td align="right">339,600.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">540</td>
<td align="right">1,831,440</td>
<td align="right">339,055.6%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">7,440</td>
<td align="right">3,893,200</td>
<td align="right">52,228.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">23,580</td>
<td align="right">3,331,760</td>
<td align="right">14,029.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">600</td>
<td align="right">43,980</td>
<td align="right">7,230.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">273,600</td>
<td align="right">7,038,740</td>
<td align="right">2,472.6%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">455,040</td>
<td align="right">10,826,420</td>
<td align="right">2,279.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">32,420</td>
<td align="right">714,340</td>
<td align="right">2,103.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">699,460</td>
<td align="right">13,011,460</td>
<td align="right">1,760.2%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,225,560</td>
<td align="right">21,823,820</td>
<td align="right">1,680.7%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,225,560</td>
<td align="right">21,823,820</td>
<td align="right">1,680.7%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">199,520</td>
<td align="right">2,511,100</td>
<td align="right">1,158.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">2,117,800</td>
<td align="right">25,286,880</td>
<td align="right">1,094.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,117,800</td>
<td align="right">25,286,880</td>
<td align="right">1,094.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">22,878,680</td>
<td align="right">253,833,920</td>
<td align="right">1,009.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,284,680</td>
<td align="right">13,289,800</td>
<td align="right">934.5%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">42,440</td>
<td align="right">403,040</td>
<td align="right">849.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,829,240</td>
<td align="right">14,182,420</td>
<td align="right">675.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">6,645,720</td>
<td align="right">51,227,920</td>
<td align="right">670.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">21,800</td>
<td align="right">145,100</td>
<td align="right">565.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">21,800</td>
<td align="right">145,100</td>
<td align="right">565.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">6,272,400</td>
<td align="right">41,603,020</td>
<td align="right">563.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">3,367,220</td>
<td align="right">19,282,680</td>
<td align="right">472.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">51,360</td>
<td align="right">266,700</td>
<td align="right">419.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,487,100</td>
<td align="right">22,692,560</td>
<td align="right">405.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">5,322,020</td>
<td align="right">26,379,780</td>
<td align="right">395.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">238,580</td>
<td align="right">1,136,860</td>
<td align="right">376.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,434,120</td>
<td align="right">11,344,920</td>
<td align="right">366.1%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">119,420</td>
<td align="right">551,100</td>
<td align="right">361.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">3,910,640</td>
<td align="right">16,303,240</td>
<td align="right">316.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">600,380</td>
<td align="right">2,411,940</td>
<td align="right">301.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">514,740</td>
<td align="right">1,851,880</td>
<td align="right">259.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">864,060</td>
<td align="right">2,803,280</td>
<td align="right">224.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,298,180</td>
<td align="right">13,744,980</td>
<td align="right">219.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">6,983,080</td>
<td align="right">22,270,360</td>
<td align="right">218.9%</td>
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
<td align="right">19,241,260</td>
<td align="right">199.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">45,258,740</td>
<td align="right">134,067,280</td>
<td align="right">196.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,748,620</td>
<td align="right">5,024,000</td>
<td align="right">187.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">12,562,420</td>
<td align="right">35,738,420</td>
<td align="right">184.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,251,620</td>
<td align="right">6,353,340</td>
<td align="right">182.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">9,191,480</td>
<td align="right">25,518,940</td>
<td align="right">177.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">324,920</td>
<td align="right">890,760</td>
<td align="right">174.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">309,120</td>
<td align="right">821,860</td>
<td align="right">165.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">39,214,360</td>
<td align="right">100,724,980</td>
<td align="right">156.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,306,120</td>
<td align="right">3,288,420</td>
<td align="right">151.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">186,893,140</td>
<td align="right">467,789,700</td>
<td align="right">150.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">11,263,820</td>
<td align="right">27,998,000</td>
<td align="right">148.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">60,151,920</td>
<td align="right">149,348,720</td>
<td align="right">148.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">38,583,880</td>
<td align="right">94,294,520</td>
<td align="right">144.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,092,460</td>
<td align="right">7,281,080</td>
<td align="right">135.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">36,620,820</td>
<td align="right">86,207,420</td>
<td align="right">135.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">2,237,540</td>
<td align="right">5,225,960</td>
<td align="right">133.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">2,236,460</td>
<td align="right">5,221,020</td>
<td align="right">133.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">242,940</td>
<td align="right">567,120</td>
<td align="right">133.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">4,094,640</td>
<td align="right">9,473,220</td>
<td align="right">131.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">5,958,360</td>
<td align="right">13,777,800</td>
<td align="right">131.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">14,174,540</td>
<td align="right">32,739,720</td>
<td align="right">131.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">36,148,180</td>
<td align="right">82,949,420</td>
<td align="right">129.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">33,950,040</td>
<td align="right">77,719,600</td>
<td align="right">128.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,088,140</td>
<td align="right">13,737,680</td>
<td align="right">125.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">5,880</td>
<td align="right">13,140</td>
<td align="right">123.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">3,957,520</td>
<td align="right">8,813,800</td>
<td align="right">122.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">157,680</td>
<td align="right">347,040</td>
<td align="right">120.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">126,365,780</td>
<td align="right">275,140,420</td>
<td align="right">117.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">34,420,960</td>
<td align="right">74,419,600</td>
<td align="right">116.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">60,487,020</td>
<td align="right">130,166,700</td>
<td align="right">115.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">16,378,020</td>
<td align="right">34,521,560</td>
<td align="right">110.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">15,806,480</td>
<td align="right">32,448,720</td>
<td align="right">105.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">15,743,220</td>
<td align="right">32,311,080</td>
<td align="right">105.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">9,412,180</td>
<td align="right">19,290,340</td>
<td align="right">105.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,171,900</td>
<td align="right">20,639,560</td>
<td align="right">102.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">21,850,820</td>
<td align="right">44,260,740</td>
<td align="right">102.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,454,400</td>
<td align="right">10,980,380</td>
<td align="right">101.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">10,514,200</td>
<td align="right">20,831,400</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">56,813,340</td>
<td align="right">1,380,300</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">22,031,120</td>
<td align="right">43,311,060</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">10,204,940</td>
<td align="right">19,932,680</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">8,004,840</td>
<td align="right">15,581,160</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">66,920,120</td>
<td align="right">128,877,300</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">263,380</td>
<td align="right">23,900</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">420,776,220</td>
<td align="right">803,313,300</td>
<td align="right">90.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">44,059,840</td>
<td align="right">83,249,900</td>
<td align="right">88.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">71,310,660</td>
<td align="right">134,653,980</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">72,638,580</td>
<td align="right">136,450,880</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">35,225,560</td>
<td align="right">65,747,740</td>
<td align="right">86.6%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">110,169,680</td>
<td align="right">205,238,820</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">110,136,300</td>
<td align="right">205,086,860</td>
<td align="right">86.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">26,261,440</td>
<td align="right">47,930,940</td>
<td align="right">82.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">29,823,900</td>
<td align="right">54,311,240</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">694,360</td>
<td align="right">1,257,360</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">108,236,320</td>
<td align="right">195,441,100</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">18,447,620</td>
<td align="right">33,308,100</td>
<td align="right">80.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">277,580</td>
<td align="right">499,480</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">277,580</td>
<td align="right">499,480</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">81,221,400</td>
<td align="right">146,095,840</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">2,560</td>
<td align="right">580</td>
<td align="right">-77.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">7,681,340</td>
<td align="right">13,559,400</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">22,293,220</td>
<td align="right">38,908,080</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,476,360</td>
<td align="right">14,724,580</td>
<td align="right">73.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">106,957,940</td>
<td align="right">184,398,500</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">53,618,260</td>
<td align="right">92,257,120</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">5,572,060</td>
<td align="right">9,319,560</td>
<td align="right">67.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">537,871,880</td>
<td align="right">892,279,960</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">505,024,020</td>
<td align="right">834,001,780</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">26,838,140</td>
<td align="right">44,233,680</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,510,360</td>
<td align="right">2,435,120</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">107,832,200</td>
<td align="right">173,468,540</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">586,354,400</td>
<td align="right">936,738,680</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">535,847,040</td>
<td align="right">838,065,780</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">44,331,800</td>
<td align="right">69,112,800</td>
<td align="right">55.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,412,340</td>
<td align="right">19,288,980</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">4,139,320</td>
<td align="right">6,354,060</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">1,798,360</td>
<td align="right">2,754,900</td>
<td align="right">53.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">432,374,380</td>
<td align="right">661,931,900</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">5,721,240</td>
<td align="right">8,681,620</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">49,350,160</td>
<td align="right">74,395,560</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">3,361,980</td>
<td align="right">1,800,900</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">525,620</td>
<td align="right">760,440</td>
<td align="right">44.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">28,503,000</td>
<td align="right">41,074,720</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">258,040</td>
<td align="right">371,000</td>
<td align="right">43.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">24,615,580</td>
<td align="right">34,915,060</td>
<td align="right">41.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">16,281,420</td>
<td align="right">22,449,460</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">16,281,420</td>
<td align="right">22,449,280</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">6,312,040</td>
<td align="right">8,701,780</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">875,000</td>
<td align="right">1,198,800</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">1,645,780</td>
<td align="right">2,191,020</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,376,080</td>
<td align="right">1,830,620</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">9,730,300</td>
<td align="right">6,591,440</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">10,148,000</td>
<td align="right">13,413,640</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">472,280</td>
<td align="right">616,720</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">44,520,260</td>
<td align="right">57,492,840</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">3,880,980</td>
<td align="right">4,932,620</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">31,353,660</td>
<td align="right">39,771,700</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">243,124,320</td>
<td align="right">304,680,440</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">37,480,860</td>
<td align="right">28,662,440</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">38,094,800</td>
<td align="right">46,794,880</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">211,560</td>
<td align="right">258,800</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">842,120</td>
<td align="right">1,006,860</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">97,046,380</td>
<td align="right">115,200,540</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">43,472,480</td>
<td align="right">51,197,800</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">15,523,540</td>
<td align="right">18,101,560</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">212,200</td>
<td align="right">178,140</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">16,811,340</td>
<td align="right">19,067,420</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">16,571,360</td>
<td align="right">18,670,920</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">7,239,440</td>
<td align="right">7,926,440</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,221,980</td>
<td align="right">2,020,900</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">964,980</td>
<td align="right">1,051,500</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">352,900</td>
<td align="right">382,680</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">48,482,520</td>
<td align="right">44,458,720</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">119,976,380</td>
<td align="right">110,284,720</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">35,995,560</td>
<td align="right">38,849,980</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">103,140,340</td>
<td align="right">96,067,240</td>
<td align="right">-6.9%</td>
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
<td align="right">4,315,980</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">95,905,660</td>
<td align="right">90,145,260</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">3,138,940</td>
<td align="right">3,303,520</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">3,138,940</td>
<td align="right">3,303,520</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,800,900</td>
<td align="right">2,946,920</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">482,540</td>
<td align="right">457,620</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">13,549,500</td>
<td align="right">14,127,220</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">18,621,260</td>
<td align="right">19,388,880</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">47,440,740</td>
<td align="right">49,167,300</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">13,661,240</td>
<td align="right">13,198,800</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">995,260</td>
<td align="right">1,027,000</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">995,260</td>
<td align="right">1,027,000</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">55,798,680</td>
<td align="right">57,202,560</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">34,323,640</td>
<td align="right">35,157,920</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">63,400</td>
<td align="right">61,920</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">72,314,240</td>
<td align="right">73,766,540</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">17,163,480</td>
<td align="right">17,435,040</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">14,236,020</td>
<td align="right">14,433,600</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">26,460</td>
<td align="right">26,740</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">18,353,860</td>
<td align="right">18,520,440</td>
<td align="right">0.9%</td>
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
<td align="right">7,427,740</td>
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
<td align="right">144,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">144,560</td>
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
<td align="right">75,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">57,020</td>
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
<td align="right">26,740</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">19,480</td>
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
<td align="right">50,320</td>
<td align="right">509.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,540</td>
<td align="right">6,480</td>
<td align="right">320.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,760</td>
<td align="right">5,500</td>
<td align="right">46.3%</td>
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
Stats gathered on: 2024-10-23
