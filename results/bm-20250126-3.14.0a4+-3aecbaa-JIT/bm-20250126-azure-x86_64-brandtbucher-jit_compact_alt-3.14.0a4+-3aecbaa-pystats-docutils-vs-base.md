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
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">19,812,960</td>
<td align="right">41,263,580</td>
<td align="right">108.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">36,886,980</td>
<td align="right">740</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,114,500</td>
<td align="right">10,920</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">267,120</td>
<td align="right">120</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">440,340</td>
<td align="right">220</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,193,640</td>
<td align="right">22,340</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">4,951,860</td>
<td align="right">80,060</td>
<td align="right">-98.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,420,160</td>
<td align="right">83,680</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">740,040</td>
<td align="right">25,380</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">91,560</td>
<td align="right">3,220</td>
<td align="right">-96.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_METHOD_METHOD</td>
<td align="right">75,960</td>
<td align="right">3,300</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">11,400</td>
<td align="right">540</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,698,280</td>
<td align="right">3,221,780</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">5,799,620</td>
<td align="right">593,060</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">156,900</td>
<td align="right">16,740</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,898,840</td>
<td align="right">1,159,440</td>
<td align="right">-88.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">853,740</td>
<td align="right">102,040</td>
<td align="right">-88.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">724,200</td>
<td align="right">89,340</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">174,015,360</td>
<td align="right">23,718,500</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">840,600</td>
<td align="right">118,860</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">19,229,560</td>
<td align="right">3,394,040</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">16,860</td>
<td align="right">3,180</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">303,433,580</td>
<td align="right">57,514,220</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,922,140</td>
<td align="right">373,780</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">17,992,160</td>
<td align="right">3,943,840</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,885,920</td>
<td align="right">422,020</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">5,440,420</td>
<td align="right">1,225,200</td>
<td align="right">-77.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,874,000</td>
<td align="right">648,160</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,325,740</td>
<td align="right">3,081,680</td>
<td align="right">-76.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">332,160</td>
<td align="right">81,180</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,693,560</td>
<td align="right">420,580</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">10,787,480</td>
<td align="right">2,869,620</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">16,162,020</td>
<td align="right">4,319,480</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">78,356,060</td>
<td align="right">21,259,440</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">26,431,540</td>
<td align="right">7,177,920</td>
<td align="right">-72.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">230,880</td>
<td align="right">64,680</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">77,703,920</td>
<td align="right">22,743,340</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">2,480,940</td>
<td align="right">738,040</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,146,540</td>
<td align="right">2,146,340</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">39,411,840</td>
<td align="right">11,993,480</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">11,362,660</td>
<td align="right">3,458,500</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">16,145,600</td>
<td align="right">5,067,220</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">10,526,700</td>
<td align="right">3,346,480</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">8,710,720</td>
<td align="right">14,608,720</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">8,889,920</td>
<td align="right">2,933,360</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,539,060</td>
<td align="right">5,616,920</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">228,720</td>
<td align="right">77,740</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">7,806,820</td>
<td align="right">2,692,760</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">27,500,800</td>
<td align="right">9,628,160</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">209,298,040</td>
<td align="right">75,657,360</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">361,260</td>
<td align="right">133,500</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">150,154,040</td>
<td align="right">55,963,200</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">4,740</td>
<td align="right">1,800</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">20,588,820</td>
<td align="right">8,500,300</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">89,800,140</td>
<td align="right">37,504,340</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">20,540,740</td>
<td align="right">8,583,240</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">15,721,720</td>
<td align="right">6,640,880</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">14,640</td>
<td align="right">6,200</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">307,717,400</td>
<td align="right">131,264,140</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">23,621,320</td>
<td align="right">10,159,360</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">18,227,560</td>
<td align="right">7,870,820</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">38,538,740</td>
<td align="right">16,934,820</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">250,025,860</td>
<td align="right">110,520,760</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,322,120</td>
<td align="right">2,406,060</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">5,762,980</td>
<td align="right">2,663,260</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_NO_DICT</td>
<td align="right">122,893,960</td>
<td align="right">56,983,560</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">122,760,060</td>
<td align="right">58,593,100</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">19,358,660</td>
<td align="right">9,385,220</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">672,120</td>
<td align="right">329,160</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,944,720</td>
<td align="right">1,953,160</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">12,037,160</td>
<td align="right">6,009,200</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">294,107,800</td>
<td align="right">146,998,660</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">5,880</td>
<td align="right">2,940</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,880</td>
<td align="right">2,940</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">56,602,140</td>
<td align="right">28,399,200</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">73,620</td>
<td align="right">36,960</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">200,605,180</td>
<td align="right">103,342,580</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,145,480</td>
<td align="right">2,701,700</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,370,274,460</td>
<td align="right">746,649,400</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">49,314,980</td>
<td align="right">27,657,600</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">120,935,420</td>
<td align="right">68,014,460</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">61,560</td>
<td align="right">35,280</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">17,743,940</td>
<td align="right">10,219,120</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21,048,140</td>
<td align="right">12,483,380</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">237,283,160</td>
<td align="right">141,443,240</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">7,060,020</td>
<td align="right">4,231,240</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">44,100</td>
<td align="right">26,460</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">43,217,860</td>
<td align="right">26,319,460</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">3,219,960</td>
<td align="right">2,017,800</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">9,790,840</td>
<td align="right">6,314,840</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">7,260</td>
<td align="right">4,700</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">7,706,580</td>
<td align="right">5,046,820</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">1,440</td>
<td align="right">960</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">1,440</td>
<td align="right">960</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,969,220</td>
<td align="right">63,209,700</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,731,500</td>
<td align="right">1,896,200</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,728,440</td>
<td align="right">1,896,080</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">26,742,500</td>
<td align="right">18,595,080</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,762,440</td>
<td align="right">1,939,180</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">327,152,960</td>
<td align="right">230,477,120</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">28,754,760</td>
<td align="right">20,523,980</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">66,662,220</td>
<td align="right">48,011,600</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">54,947,720</td>
<td align="right">70,111,960</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">19,875,280</td>
<td align="right">14,786,920</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">5,767,920</td>
<td align="right">4,299,280</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,493,160</td>
<td align="right">7,834,340</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">51,322,440</td>
<td align="right">38,774,300</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">15,100,320</td>
<td align="right">11,445,600</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">172,104,900</td>
<td align="right">130,533,880</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,425,140</td>
<td align="right">2,614,080</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">30,064,100</td>
<td align="right">23,056,920</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">30,062,720</td>
<td align="right">23,056,920</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33,987,700</td>
<td align="right">26,209,100</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">1,430,000</td>
<td align="right">1,104,120</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">8,782,520</td>
<td align="right">6,898,960</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">315,929,260</td>
<td align="right">253,300,540</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">194,205,720</td>
<td align="right">157,049,540</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">101,100,140</td>
<td align="right">86,541,340</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,587,740</td>
<td align="right">3,967,900</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">95,017,300</td>
<td align="right">83,457,500</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">38,691,300</td>
<td align="right">43,216,580</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">64,461,540</td>
<td align="right">58,236,560</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">6,134,760</td>
<td align="right">5,616,180</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">300</td>
<td align="right">280</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">35,328,900</td>
<td align="right">37,653,620</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,909,960</td>
<td align="right">4,591,000</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,202,760</td>
<td align="right">1,128,580</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">75,760,000</td>
<td align="right">80,145,000</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,538,820</td>
<td align="right">2,394,880</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">47,443,580</td>
<td align="right">44,774,080</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">69,635,320</td>
<td align="right">65,926,400</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">45,537,700</td>
<td align="right">43,226,500</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">24,464,640</td>
<td align="right">25,650,640</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">7,613,400</td>
<td align="right">7,310,340</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,607,300</td>
<td align="right">8,300,240</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,940</td>
<td align="right">1,880</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,619,980</td>
<td align="right">9,444,960</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">145,320</td>
<td align="right">143,120</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,576,100</td>
<td align="right">38,487,520</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">106,046,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">11,627,520</td>
<td align="right">11,627,520</td>
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
<td align="left">NOT_TAKEN</td>
<td align="right">3,335,620</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">MAP_ADD</td>
<td align="right">49,980</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">27,480</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8,820</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_METHOD_LAZY_DICT</td>
<td align="right">5,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,960</td>
<td align="right">3,960</td>
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
<td align="right">21,035,920</td>
<td align="right">30.3%</td>
<td align="right">12,477,580</td>
<td align="right">20.5%</td>
<td align="right">-40.7%</td>
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
<td align="right">69.7%</td>
<td align="right">48,362,220</td>
<td align="right">79.5%</td>
<td align="right">-0.1%</td>
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
<td align="right">12,020</td>
<td align="right">98.4%</td>
<td align="right">5,640</td>
<td align="right">97.2%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">160</td>
<td align="right">2.8%</td>
<td align="right">-20.0%</td>
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
<td align="right">3,200</td>
<td align="right">26.6%</td>
<td align="right">660</td>
<td align="right">11.7%</td>
<td align="right">-79.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">26.3%</td>
<td align="right">1,060</td>
<td align="right">18.8%</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">4,980</td>
<td align="right">41.4%</td>
<td align="right">3,760</td>
<td align="right">66.7%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">180</td>
<td align="right">1.5%</td>
<td align="right">140</td>
<td align="right">2.5%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">320</td>
<td align="right">2.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">160</td>
<td align="right">1.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.4%</td>
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
<td align="right">10,787,480</td>
<td align="right">100.0%</td>
<td align="right">2,869,620</td>
<td align="right">100.0%</td>
<td align="right">-73.4%</td>
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
<td align="right">10,481,660</td>
<td align="right">9.8%</td>
<td align="right">7,823,560</td>
<td align="right">7.6%</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">93,971,280</td>
<td align="right">88.1%</td>
<td align="right">93,396,680</td>
<td align="right">90.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,165,080</td>
<td align="right">2.0%</td>
<td align="right">2,165,160</td>
<td align="right">2.1%</td>
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
<td align="right">10,880</td>
<td align="right">20.8%</td>
<td align="right">10,140</td>
<td align="right">19.7%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,420</td>
<td align="right">79.2%</td>
<td align="right">41,420</td>
<td align="right">80.3%</td>
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
<td align="left">string slice</td>
<td align="right">720</td>
<td align="right">6.6%</td>
<td align="right">320</td>
<td align="right">3.2%</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">680</td>
<td align="right">6.2%</td>
<td align="right">380</td>
<td align="right">3.7%</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,760</td>
<td align="right">16.2%</td>
<td align="right">1,440</td>
<td align="right">14.2%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">1.7%</td>
<td align="right">160</td>
<td align="right">1.6%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">7,540</td>
<td align="right">69.3%</td>
<td align="right">7,840</td>
<td align="right">77.3%</td>
<td align="right">4.0%</td>
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
<td align="right">17,609,700</td>
<td align="right">3.1%</td>
<td align="right">15,891,200</td>
<td align="right">2.8%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">553,234,680</td>
<td align="right">96.9%</td>
<td align="right">558,486,800</td>
<td align="right">97.2%</td>
<td align="right">0.9%</td>
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
<td align="right">336,040</td>
<td align="right">100.0%</td>
<td align="right">303,660</td>
<td align="right">100.0%</td>
<td align="right">-9.6%</td>
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
<td align="right">300</td>
<td align="right">100.0%</td>
<td align="right">300</td>
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
<td align="right">1,680,260</td>
<td align="right">4.6%</td>
<td align="right">408,300</td>
<td align="right">1.2%</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">259,420</td>
<td align="right">0.7%</td>
<td align="right">246,260</td>
<td align="right">0.7%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,778,780</td>
<td align="right">94.7%</td>
<td align="right">34,722,860</td>
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
<td align="left">Failure</td>
<td align="right">12,960</td>
<td align="right">71.3%</td>
<td align="right">11,960</td>
<td align="right">70.6%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,220</td>
<td align="right">28.7%</td>
<td align="right">4,980</td>
<td align="right">29.4%</td>
<td align="right">-4.6%</td>
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
<td align="right">12,500</td>
<td align="right">96.5%</td>
<td align="right">11,860</td>
<td align="right">99.2%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">1.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">80</td>
<td align="right">0.6%</td>
<td align="right">80</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">long float</td>
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
<td align="right">8,777,680</td>
<td align="right">13.9%</td>
<td align="right">6,896,000</td>
<td align="right">11.3%</td>
<td align="right">-21.4%</td>
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
<td align="right">86.1%</td>
<td align="right">54,348,780</td>
<td align="right">88.7%</td>
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
<td align="right">4,720</td>
<td align="right">97.5%</td>
<td align="right">2,840</td>
<td align="right">95.9%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">120</td>
<td align="right">2.5%</td>
<td align="right">120</td>
<td align="right">4.1%</td>
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
<td align="right">860</td>
<td align="right">18.2%</td>
<td align="right">300</td>
<td align="right">10.6%</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,880</td>
<td align="right">39.8%</td>
<td align="right">920</td>
<td align="right">32.4%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">16.9%</td>
<td align="right">640</td>
<td align="right">22.5%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,180</td>
<td align="right">25.0%</td>
<td align="right">980</td>
<td align="right">34.5%</td>
<td align="right">-16.9%</td>
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
<td align="right">23,614,740</td>
<td align="right">13.2%</td>
<td align="right">10,156,520</td>
<td align="right">5.9%</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">26,155,280</td>
<td align="right">14.6%</td>
<td align="right">19,177,920</td>
<td align="right">11.1%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">129,172,260</td>
<td align="right">72.2%</td>
<td align="right">142,714,740</td>
<td align="right">82.9%</td>
<td align="right">10.5%</td>
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
<td align="right">6,580</td>
<td align="right">1.3%</td>
<td align="right">2,840</td>
<td align="right">0.8%</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">493,480</td>
<td align="right">98.7%</td>
<td align="right">361,840</td>
<td align="right">99.2%</td>
<td align="right">-26.7%</td>
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
<td align="right">580</td>
<td align="right">8.8%</td>
<td align="right">20</td>
<td align="right">0.7%</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">400</td>
<td align="right">6.1%</td>
<td align="right">780</td>
<td align="right">27.5%</td>
<td align="right">95.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">220</td>
<td align="right">3.3%</td>
<td align="right">40</td>
<td align="right">1.4%</td>
<td align="right">-81.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,460</td>
<td align="right">22.2%</td>
<td align="right">460</td>
<td align="right">16.2%</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">560</td>
<td align="right">8.5%</td>
<td align="right">180</td>
<td align="right">6.3%</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,040</td>
<td align="right">15.8%</td>
<td align="right">1,320</td>
<td align="right">46.5%</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,160</td>
<td align="right">32.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right">40</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">100,447,440</td>
<td align="right">10.6%</td>
<td align="right">86,067,520</td>
<td align="right">8.9%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">195,071,480</td>
<td align="right">20.6%</td>
<td align="right">217,146,920</td>
<td align="right">22.5%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">651,780,980</td>
<td align="right">68.8%</td>
<td align="right">661,777,100</td>
<td align="right">68.5%</td>
<td align="right">1.5%</td>
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
<td align="right">20,240</td>
<td align="right">0.6%</td>
<td align="right">17,300</td>
<td align="right">0.4%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,619,480</td>
<td align="right">99.4%</td>
<td align="right">4,035,860</td>
<td align="right">99.6%</td>
<td align="right">11.5%</td>
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
<td align="right">420</td>
<td align="right">2.1%</td>
<td align="right">160</td>
<td align="right">0.9%</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">60</td>
<td align="right">0.3%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">640</td>
<td align="right">3.2%</td>
<td align="right">360</td>
<td align="right">2.1%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,120</td>
<td align="right">25.3%</td>
<td align="right">3,720</td>
<td align="right">21.5%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">9,700</td>
<td align="right">47.9%</td>
<td align="right">9,280</td>
<td align="right">53.6%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2,840</td>
<td align="right">14.0%</td>
<td align="right">2,800</td>
<td align="right">16.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">2.0%</td>
<td align="right">400</td>
<td align="right">2.3%</td>
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
<td align="right">278,306,960</td>
<td align="right">100.0%</td>
<td align="right">313,787,100</td>
<td align="right">100.0%</td>
<td align="right">12.7%</td>
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
<td align="right">1,980</td>
<td align="right">100.0%</td>
<td align="right">1,920</td>
<td align="right">100.0%</td>
<td align="right">-3.0%</td>
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

### LOAD_METHOD

<details>
<summary> specialization stats for LOAD_METHOD family </summary>

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
<td align="right">8,882,580</td>
<td align="right">9.8%</td>
<td align="right">2,928,920</td>
<td align="right">2.9%</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">81,475,280</td>
<td align="right">90.2%</td>
<td align="right">98,188,380</td>
<td align="right">97.1%</td>
<td align="right">20.5%</td>
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
<td align="right">4,640</td>
<td align="right">0.3%</td>
<td align="right">1,900</td>
<td align="right">0.1%</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,539,760</td>
<td align="right">99.7%</td>
<td align="right">1,855,080</td>
<td align="right">99.9%</td>
<td align="right">20.5%</td>
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
<td align="left">kind 18</td>
<td align="right">180</td>
<td align="right">3.9%</td>
<td align="right">60</td>
<td align="right">3.2%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,200</td>
<td align="right">90.5%</td>
<td align="right">1,700</td>
<td align="right">89.5%</td>
<td align="right">-59.5%</td>
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
<td align="right">19,862,460</td>
<td align="right">16.4%</td>
<td align="right">14,780,720</td>
<td align="right">14.0%</td>
<td align="right">-25.6%</td>
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
<td align="right">44.6%</td>
<td align="right">44,317,440</td>
<td align="right">41.8%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,039,540</td>
<td align="right">38.9%</td>
<td align="right">46,816,440</td>
<td align="right">44.2%</td>
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
<td align="left">Failure</td>
<td align="right">12,420</td>
<td align="right">1.2%</td>
<td align="right">5,840</td>
<td align="right">0.7%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,017,800</td>
<td align="right">98.8%</td>
<td align="right">836,820</td>
<td align="right">99.3%</td>
<td align="right">-17.8%</td>
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
<td align="right">2,040</td>
<td align="right">16.4%</td>
<td align="right">720</td>
<td align="right">12.3%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">200</td>
<td align="right">1.6%</td>
<td align="right">80</td>
<td align="right">1.4%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">9,780</td>
<td align="right">78.7%</td>
<td align="right">4,680</td>
<td align="right">80.1%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,000</td>
<td align="right">8.1%</td>
<td align="right">480</td>
<td align="right">8.2%</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">320</td>
<td align="right">2.6%</td>
<td align="right">280</td>
<td align="right">4.8%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.7%</td>
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
<td align="right">267,120</td>
<td align="right">100.0%</td>
<td align="right">120</td>
<td align="right">100.0%</td>
<td align="right">-100.0%</td>
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
<td align="right">3,965,560</td>
<td align="right">8.5%</td>
<td align="right">-13.5%</td>
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
<td align="right">42,553,800</td>
<td align="right">91.5%</td>
<td align="right">-0.0%</td>
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
<td align="left">Failure</td>
<td align="right">3,760</td>
<td align="right">95.9%</td>
<td align="right">2,220</td>
<td align="right">93.3%</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">160</td>
<td align="right">6.7%</td>
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
<td align="right">1,000</td>
<td align="right">45.0%</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">220</td>
<td align="right">5.9%</td>
<td align="right">200</td>
<td align="right">9.0%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">980</td>
<td align="right">44.1%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">1.1%</td>
<td align="right">40</td>
<td align="right">1.8%</td>
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
<td align="right">3,776,840</td>
<td align="right">1.3%</td>
<td align="right">1,783,940</td>
<td align="right">0.6%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,206,200</td>
<td align="right">3.6%</td>
<td align="right">8,863,980</td>
<td align="right">3.2%</td>
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
<td align="right">268,984,480</td>
<td align="right">95.0%</td>
<td align="right">266,958,980</td>
<td align="right">96.1%</td>
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
<td align="right">193,400</td>
<td align="right">53.7%</td>
<td align="right">168,240</td>
<td align="right">50.0%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">167,000</td>
<td align="right">46.3%</td>
<td align="right">168,360</td>
<td align="right">50.0%</td>
<td align="right">0.8%</td>
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
<td align="left">mapping</td>
<td align="right">2,360</td>
<td align="right">1.4%</td>
<td align="right">880</td>
<td align="right">0.5%</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,200</td>
<td align="right">0.7%</td>
<td align="right">640</td>
<td align="right">0.4%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">121,740</td>
<td align="right">72.9%</td>
<td align="right">125,320</td>
<td align="right">74.4%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">41,540</td>
<td align="right">24.9%</td>
<td align="right">41,360</td>
<td align="right">24.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">3,260</td>
<td align="right">0.0%</td>
<td align="right">-11.9%</td>
</tr>
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
<td align="right">47,741,200</td>
<td align="right">100.0%</td>
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
<td align="right">380</td>
<td align="right">100.0%</td>
<td align="right">340</td>
<td align="right">100.0%</td>
<td align="right">-10.5%</td>
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
<td align="right">3,982,096,980</td>
<td align="right">54.8%</td>
<td align="right">2,066,376,020</td>
<td align="right">51.2%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">2,686,301,900</td>
<td align="right">36.9%</td>
<td align="right">1,413,125,520</td>
<td align="right">35.0%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">215,097,600</td>
<td align="right">3.0%</td>
<td align="right">150,855,460</td>
<td align="right">3.7%</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">386,872,800</td>
<td align="right">5.3%</td>
<td align="right">406,011,260</td>
<td align="right">10.1%</td>
<td align="right">4.9%</td>
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
<td align="right">10,787,480</td>
<td align="right">5.0%</td>
<td align="right">2,869,620</td>
<td align="right">1.9%</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD</td>
<td align="right">8,882,580</td>
<td align="right">4.1%</td>
<td align="right">2,928,920</td>
<td align="right">2.0%</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">23,614,740</td>
<td align="right">11.0%</td>
<td align="right">10,156,520</td>
<td align="right">6.8%</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,776,840</td>
<td align="right">1.8%</td>
<td align="right">1,783,940</td>
<td align="right">1.2%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">21,035,920</td>
<td align="right">9.8%</td>
<td align="right">12,477,580</td>
<td align="right">8.3%</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">19,862,460</td>
<td align="right">9.3%</td>
<td align="right">14,780,720</td>
<td align="right">9.8%</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">10,481,660</td>
<td align="right">4.9%</td>
<td align="right">7,823,560</td>
<td align="right">5.2%</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">8,777,680</td>
<td align="right">4.1%</td>
<td align="right">6,896,000</td>
<td align="right">4.6%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">100,447,440</td>
<td align="right">46.9%</td>
<td align="right">86,067,520</td>
<td align="right">57.3%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,583,860</td>
<td align="right">2.1%</td>
<td align="right">3,965,560</td>
<td align="right">2.6%</td>
<td align="right">-13.5%</td>
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
<td align="right">13,077,400</td>
<td align="right">3.4%</td>
<td align="right">9,588,760</td>
<td align="right">2.4%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">13,077,880</td>
<td align="right">3.4%</td>
<td align="right">9,589,160</td>
<td align="right">2.4%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">103,444,440</td>
<td align="right">26.7%</td>
<td align="right">125,977,000</td>
<td align="right">31.0%</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">LOAD_METHOD_WITH_VALUES</td>
<td align="right">81,163,640</td>
<td align="right">21.0%</td>
<td align="right">97,016,680</td>
<td align="right">23.9%</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,568,700</td>
<td align="right">2.5%</td>
<td align="right">11,404,900</td>
<td align="right">2.8%</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,912,180</td>
<td align="right">13.9%</td>
<td align="right">44,317,440</td>
<td align="right">10.9%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,563,540</td>
<td align="right">1.4%</td>
<td align="right">4,797,880</td>
<td align="right">1.2%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">7,565,220</td>
<td align="right">2.0%</td>
<td align="right">7,393,500</td>
<td align="right">1.8%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">31,651,120</td>
<td align="right">8.2%</td>
<td align="right">31,303,760</td>
<td align="right">7.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">50,609,520</td>
<td align="right">13.1%</td>
<td align="right">50,781,500</td>
<td align="right">12.5%</td>
<td align="right">0.3%</td>
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
<td align="right">8,426,280</td>
<td align="right">2.4%</td>
<td align="right">8,257,800</td>
<td align="right">2.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,307,200</td>
<td align="right">11.1%</td>
<td align="right">39,217,960</td>
<td align="right">11.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,310,680</td>
<td align="right">11.1%</td>
<td align="right">39,221,440</td>
<td align="right">11.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,618,540</td>
<td align="right">11.2%</td>
<td align="right">39,529,960</td>
<td align="right">11.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,618,540</td>
<td align="right">11.2%</td>
<td align="right">39,529,960</td>
<td align="right">11.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">307,860</td>
<td align="right">0.1%</td>
<td align="right">308,520</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">13,631,100</td>
<td align="right">3.8%</td>
<td align="right">13,636,160</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">314,774,820</td>
<td align="right">88.8%</td>
<td align="right">314,863,400</td>
<td align="right">88.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,581,180</td>
<td align="right">88.5%</td>
<td align="right">313,507,000</td>
<td align="right">88.5%</td>
<td align="right">-0.0%</td>
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
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,911,413,100</td>
<td align="right">36.0%</td>
<td align="right">1,924,179,260</td>
<td align="right">24.2%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,720,290,769</td>
<td align="right">33.6%</td>
<td align="right">3,564,974,053</td>
<td align="right">44.8%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,094,384,020</td>
<td align="right">12.1%</td>
<td align="right">774,864,400</td>
<td align="right">8.8%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">717,311,040</td>
<td align="right">8.9%</td>
<td align="right">530,772,420</td>
<td align="right">6.7%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,483,699,637</td>
<td align="right">27.6%</td>
<td align="right">2,964,212,711</td>
<td align="right">33.8%</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,738,175,040</td>
<td align="right">41.5%</td>
<td align="right">3,116,356,420</td>
<td align="right">35.6%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">3,298,625</td>
<td align="right"></td>
<td align="right">3,732,492</td>
<td align="right"></td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,692,214,159</td>
<td align="right">18.8%</td>
<td align="right">1,904,689,405</td>
<td align="right">21.7%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,742,320,739</td>
<td align="right">21.5%</td>
<td align="right">1,937,658,841</td>
<td align="right">24.3%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">36,531,946</td>
<td align="right"></td>
<td align="right">39,385,371</td>
<td align="right"></td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">33,994,765</td>
<td align="right"></td>
<td align="right">36,414,124</td>
<td align="right"></td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">500,800</td>
<td align="right">0.1%</td>
<td align="right">489,800</td>
<td align="right">0.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">205,858,295</td>
<td align="right"></td>
<td align="right">202,454,428</td>
<td align="right"></td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">461,219,115</td>
<td align="right"></td>
<td align="right">465,005,996</td>
<td align="right"></td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">344,840</td>
<td align="right">0.1%</td>
<td align="right">346,360</td>
<td align="right">0.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">432,132,260</td>
<td align="right"></td>
<td align="right">432,893,658</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">395,097,320</td>
<td align="right">58.6%</td>
<td align="right">395,480,140</td>
<td align="right">58.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">395,942,960</td>
<td align="right">58.7%</td>
<td align="right">396,316,300</td>
<td align="right">58.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">278,194,240</td>
<td align="right"></td>
<td align="right">278,445,280</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">278,189,700</td>
<td align="right">41.3%</td>
<td align="right">278,427,360</td>
<td align="right">41.3%</td>
<td align="right">0.1%</td>
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
<td align="right">25,960</td>
<td align="right">73,042,920</td>
<td align="right">1,162,078,432</td>
<td align="right">45,247,480</td>
<td align="right">99,795,880</td>
<td align="right">25,840</td>
<td align="right">73,288,900</td>
<td align="right">1,150,880,291</td>
<td align="right">43,554,520</td>
<td align="right">100,140,340</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">4,272,335,380</td>
<td align="right">1,321.9%</td>
<td align="right">12,373,295,440</td>
<td align="right">2,022.5%</td>
<td align="right">189.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">32,560</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">21,300</td>
<td align="right">65.4%</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">200</td>
<td align="right">0.6%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">13,380</td>
<td align="right">41.1%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">11,060</td>
<td align="right">34.0%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">320</td>
<td align="right">1.0%</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">2,340</td>
<td align="right">7.2%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">140</td>
<td align="right">0.4%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">323,197,440</td>
<td align="right"></td>
<td align="right">611,785,260</td>
<td align="right"></td>
<td align="right">89.3%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">21,300</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">16,160</td>
<td align="right">75.9%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">940</td>
<td align="right">4.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1,480</td>
<td align="right">6.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">7,120</td>
<td align="right">33.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">5,140</td>
<td align="right">24.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,940</td>
<td align="right">13.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,380</td>
<td align="right">15.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">280</td>
<td align="right">1.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">20</td>
<td align="right">0.1%</td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">1,980</td>
<td align="right">9.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">3,080</td>
<td align="right">14.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">6,160</td>
<td align="right">28.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">3,580</td>
<td align="right">16.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,140</td>
<td align="right">5.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">140</td>
<td align="right">0.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">60</td>
<td align="right">0.3%</td>
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
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">880</td>
<td align="right">181,388,000</td>
<td align="right">20,612,172.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">880</td>
<td align="right">143,569,700</td>
<td align="right">16,314,638.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">440</td>
<td align="right">24,408,020</td>
<td align="right">5,547,177.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">440</td>
<td align="right">24,394,020</td>
<td align="right">5,543,995.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">440</td>
<td align="right">4,215,360</td>
<td align="right">957,936.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">3,000</td>
<td align="right">7,925,320</td>
<td align="right">264,077.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">480</td>
<td align="right">1,202,640</td>
<td align="right">250,450.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">480</td>
<td align="right">1,202,640</td>
<td align="right">250,450.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,660</td>
<td align="right">6,247,720</td>
<td align="right">234,776.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">440</td>
<td align="right">336,000</td>
<td align="right">76,263.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">16,360</td>
<td align="right">9,989,620</td>
<td align="right">60,961.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">16,880</td>
<td align="right">8,624,720</td>
<td align="right">50,994.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,140</td>
<td align="right">12,345,180</td>
<td align="right">35,031.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,140</td>
<td align="right">12,345,180</td>
<td align="right">35,031.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">39,560</td>
<td align="right">11,135,820</td>
<td align="right">28,049.2%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">50,160</td>
<td align="right">10,972,300</td>
<td align="right">21,774.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">180</td>
<td align="right">26,460</td>
<td align="right">14,600.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">23,880</td>
<td align="right">3,256,480</td>
<td align="right">13,536.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">15,920</td>
<td align="right">1,484,560</td>
<td align="right">9,225.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">14,316,740</td>
<td align="right">1,174,766,060</td>
<td align="right">8,105.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,251,000</td>
<td align="right">178,630,080</td>
<td align="right">7,835.6%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">145,180</td>
<td align="right">7,152,360</td>
<td align="right">4,826.5%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">145,180</td>
<td align="right">7,150,980</td>
<td align="right">4,825.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">255,620</td>
<td align="right">12,147,960</td>
<td align="right">4,652.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">9,745,000</td>
<td align="right">259,764,740</td>
<td align="right">2,565.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,556,960</td>
<td align="right">66,723,920</td>
<td align="right">2,509.5%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">36,740</td>
<td align="right">847,800</td>
<td align="right">2,207.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">16,120</td>
<td align="right">342,000</td>
<td align="right">2,021.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">16,120</td>
<td align="right">342,000</td>
<td align="right">2,021.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">2,001,540</td>
<td align="right">38,477,380</td>
<td align="right">1,822.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">1,473,780</td>
<td align="right">26,049,020</td>
<td align="right">1,667.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">12,642,820</td>
<td align="right">207,678,800</td>
<td align="right">1,542.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">1,366,400</td>
<td align="right">20,308,320</td>
<td align="right">1,386.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,366,400</td>
<td align="right">20,308,260</td>
<td align="right">1,386.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">2,051,560</td>
<td align="right">29,469,640</td>
<td align="right">1,336.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">20,691,960</td>
<td align="right">281,436,860</td>
<td align="right">1,260.1%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">67,860</td>
<td align="right">892,560</td>
<td align="right">1,215.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,611,860</td>
<td align="right">20,865,640</td>
<td align="right">1,194.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">1,129,160</td>
<td align="right">13,521,960</td>
<td align="right">1,097.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,129,160</td>
<td align="right">13,521,960</td>
<td align="right">1,097.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">63,840</td>
<td align="right">698,700</td>
<td align="right">994.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">82,380</td>
<td align="right">834,080</td>
<td align="right">912.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">82,380</td>
<td align="right">797,040</td>
<td align="right">867.5%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">2,145,380</td>
<td align="right">20,018,020</td>
<td align="right">833.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">4,028,220</td>
<td align="right">37,357,500</td>
<td align="right">827.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">2,303,420</td>
<td align="right">20,039,680</td>
<td align="right">770.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">13,420</td>
<td align="right">103,800</td>
<td align="right">673.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">2,229,600</td>
<td align="right">16,951,420</td>
<td align="right">660.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">47,760</td>
<td align="right">354,160</td>
<td align="right">641.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,439,000</td>
<td align="right">10,519,840</td>
<td align="right">631.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">1,311,340</td>
<td align="right">9,229,200</td>
<td align="right">603.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,827,980</td>
<td align="right">12,609,340</td>
<td align="right">589.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">934,520</td>
<td align="right">6,127,020</td>
<td align="right">555.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,208,420</td>
<td align="right">14,247,920</td>
<td align="right">545.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,393,720</td>
<td align="right">8,918,540</td>
<td align="right">539.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,058,720</td>
<td align="right">18,877,240</td>
<td align="right">517.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">2,819,120</td>
<td align="right">17,345,500</td>
<td align="right">515.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">18,041,880</td>
<td align="right">108,948,420</td>
<td align="right">503.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">39,439,820</td>
<td align="right">233,241,500</td>
<td align="right">491.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,667,720</td>
<td align="right">86,573,640</td>
<td align="right">452.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">15,455,920</td>
<td align="right">78,441,740</td>
<td align="right">407.5%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_WITH_VALUES</td>
<td align="right">13,391,500</td>
<td align="right">65,768,480</td>
<td align="right">391.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">16,184,440</td>
<td align="right">73,281,060</td>
<td align="right">352.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,560,240</td>
<td align="right">15,517,740</td>
<td align="right">335.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">41,706,380</td>
<td align="right">181,211,480</td>
<td align="right">334.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">9,147,140</td>
<td align="right">38,971,680</td>
<td align="right">326.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">2,223,220</td>
<td align="right">9,351,360</td>
<td align="right">320.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">1,694,560</td>
<td align="right">7,036,140</td>
<td align="right">315.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,340,860</td>
<td align="right">5,352,220</td>
<td align="right">299.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">32,482,180</td>
<td align="right">126,599,280</td>
<td align="right">289.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">91,900,940</td>
<td align="right">351,038,040</td>
<td align="right">282.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">19,363,600</td>
<td align="right">73,601,620</td>
<td align="right">280.1%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_NO_DICT</td>
<td align="right">24,626,300</td>
<td align="right">90,301,020</td>
<td align="right">266.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,413,260</td>
<td align="right">14,603,760</td>
<td align="right">230.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">3,467,840</td>
<td align="right">11,246,440</td>
<td align="right">224.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">9,803,920</td>
<td align="right">31,461,300</td>
<td align="right">220.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">29,624,120</td>
<td align="right">94,770,680</td>
<td align="right">219.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">1,305,220</td>
<td align="right">4,133,520</td>
<td align="right">216.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">1,304,220</td>
<td align="right">4,128,720</td>
<td align="right">216.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">23,277,400</td>
<td align="right">73,601,620</td>
<td align="right">216.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">42,869,360</td>
<td align="right">124,456,400</td>
<td align="right">190.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">42,869,360</td>
<td align="right">124,413,440</td>
<td align="right">190.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">3,290,700</td>
<td align="right">9,515,680</td>
<td align="right">189.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">29,108,560</td>
<td align="right">83,098,060</td>
<td align="right">185.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,308,560</td>
<td align="right">9,339,460</td>
<td align="right">182.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">411,997,240</td>
<td align="right">1,162,270,240</td>
<td align="right">182.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">3,664,640</td>
<td align="right">8,669,700</td>
<td align="right">136.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">245,078,800</td>
<td align="right">525,029,340</td>
<td align="right">114.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">12,168,160</td>
<td align="right">25,667,240</td>
<td align="right">110.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">461,661,680</td>
<td align="right">965,921,480</td>
<td align="right">109.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,257,260</td>
<td align="right">7,733,260</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">12,969,060</td>
<td align="right">21,199,000</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">9,317,700</td>
<td align="right">3,419,260</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">34,475,700</td>
<td align="right">13,023,460</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">22,186,040</td>
<td align="right">35,223,460</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">3,415,520</td>
<td align="right">5,298,820</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">_LOAD_METHOD</td>
<td align="right">15,843,660</td>
<td align="right">7,127,680</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">12,406,280</td>
<td align="right">17,520,340</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,813,000</td>
<td align="right">8,164,080</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">11,677,860</td>
<td align="right">7,150,000</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">11,194,340</td>
<td align="right">14,441,480</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">14,061,800</td>
<td align="right">17,398,280</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">192,534,540</td>
<td align="right">235,305,340</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">316,713,240</td>
<td align="right">246,899,020</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">32,682,820</td>
<td align="right">26,238,320</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">1,151,360</td>
<td align="right">949,060</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">923,120</td>
<td align="right">1,067,060</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">923,120</td>
<td align="right">1,067,060</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">59,873,700</td>
<td align="right">52,372,240</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">896,220</td>
<td align="right">784,020</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">9,552,780</td>
<td align="right">8,366,780</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">9,552,780</td>
<td align="right">8,366,780</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">61,419,800</td>
<td align="right">55,110,300</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">94,783,120</td>
<td align="right">85,395,420</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">41,003,500</td>
<td align="right">37,845,260</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">33,799,120</td>
<td align="right">31,596,140</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">25,661,840</td>
<td align="right">24,018,860</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">89,612,340</td>
<td align="right">85,395,420</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">360,680,640</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">323,197,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">89,232,720</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">81,006,220</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">60,721,500</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">42,408,840</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">38,008,820</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">37,642,920</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">37,483,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">34,727,260</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">34,568,700</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">33,464,120</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">31,478,700</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">27,932,060</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">22,055,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">21,905,160</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">15,447,000</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">13,752,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">10,254,520</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">10,204,080</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">9,561,820</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">8,878,860</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">6,321,920</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,096,980</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">3,489,780</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,602,980</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,921,280</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,246,660</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">1,096,200</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">648,840</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">364,340</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">262,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">116,700</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">106,640</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">36,300</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">17,720</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">1,600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">2,560,817,780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_JUMP</td>
<td align="right"></td>
<td align="right">140,579,340</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">117,807,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">117,805,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right"></td>
<td align="right">117,773,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">73,559,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">69,954,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">69,929,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right"></td>
<td align="right">37,103,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_FOR</td>
<td align="right"></td>
<td align="right">36,885,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_NONE</td>
<td align="right"></td>
<td align="right">34,758,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right"></td>
<td align="right">23,216,520</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right"></td>
<td align="right">19,133,860</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">5,410,380</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">5,000,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">4,871,800</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">4,171,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">3,654,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">2,225,840</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">1,742,900</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">1,463,900</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">1,340,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">835,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">832,360</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">714,180</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">626,700</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right"></td>
<td align="right">615,720</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">549,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right"></td>
<td align="right">518,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right"></td>
<td align="right">440,120</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">342,960</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">299,700</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right"></td>
<td align="right">267,000</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right"></td>
<td align="right">250,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right"></td>
<td align="right">227,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right"></td>
<td align="right">176,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">171,780</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">166,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">150,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right"></td>
<td align="right">140,160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_METHOD_METHOD</td>
<td align="right"></td>
<td align="right">72,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right"></td>
<td align="right">49,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">36,660</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right"></td>
<td align="right">13,680</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">10,860</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right"></td>
<td align="right">8,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right"></td>
<td align="right">8,440</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">5,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">5,880</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right"></td>
<td align="right">2,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">2,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">2,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right"></td>
<td align="right">2,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">480</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">480</td>
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
<td align="right">960</td>
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
Stats gathered on: 2025-01-27
