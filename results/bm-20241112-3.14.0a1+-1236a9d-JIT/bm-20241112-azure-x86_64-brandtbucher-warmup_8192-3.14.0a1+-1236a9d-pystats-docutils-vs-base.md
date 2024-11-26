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
<td align="left">FOR_ITER_RANGE</td>
<td align="right">320,060</td>
<td align="right">1,207,080</td>
<td align="right">277.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">42,960</td>
<td align="right">104,980</td>
<td align="right">144.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">35,280</td>
<td align="right">61,740</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">840</td>
<td align="right">1,440</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">5,880</td>
<td align="right">8,820</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,213,900</td>
<td align="right">3,189,180</td>
<td align="right">44.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">3,300</td>
<td align="right">4,740</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">513,300</td>
<td align="right">710,560</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">3,988,880</td>
<td align="right">5,436,520</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">611,380</td>
<td align="right">824,260</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">524,660</td>
<td align="right">695,420</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">309,020</td>
<td align="right">406,580</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">4,398,600</td>
<td align="right">5,736,640</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">12,854,100</td>
<td align="right">16,471,080</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">35,253,640</td>
<td align="right">44,812,700</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">25,502,180</td>
<td align="right">31,425,460</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,454,400</td>
<td align="right">1,761,380</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">896,260</td>
<td align="right">1,078,100</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">11,179,400</td>
<td align="right">13,423,040</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">66,048,900</td>
<td align="right">78,944,400</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">20,461,700</td>
<td align="right">24,324,120</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">332,420</td>
<td align="right">394,020</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">29,039,600</td>
<td align="right">34,239,700</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">583,440</td>
<td align="right">686,460</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">448,140</td>
<td align="right">523,440</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">6,360,620</td>
<td align="right">7,294,740</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">17,677,600</td>
<td align="right">20,127,220</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">126,454,220</td>
<td align="right">143,700,940</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">163,180,660</td>
<td align="right">184,881,920</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">4,518,180</td>
<td align="right">5,118,520</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">62,846,480</td>
<td align="right">55,056,560</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">145,987,160</td>
<td align="right">164,076,420</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,607,160</td>
<td align="right">1,790,500</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">16,335,080</td>
<td align="right">18,166,500</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">62,314,780</td>
<td align="right">69,285,240</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,500,960</td>
<td align="right">1,663,820</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,746,600</td>
<td align="right">3,039,200</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">1,044,940</td>
<td align="right">1,154,040</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">399,040</td>
<td align="right">440,340</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,943,140</td>
<td align="right">2,141,080</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">32,919,400</td>
<td align="right">35,944,000</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">19,687,540</td>
<td align="right">17,896,580</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">6,660</td>
<td align="right">7,260</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,743,860</td>
<td align="right">19,335,420</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">7,218,760</td>
<td align="right">7,849,280</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,279,340</td>
<td align="right">2,476,120</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,841,500</td>
<td align="right">17,197,980</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">19,933,800</td>
<td align="right">21,640,660</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">61,086,680</td>
<td align="right">66,117,900</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">28,808,460</td>
<td align="right">30,969,640</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">13,365,000</td>
<td align="right">14,321,200</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">6,127,380</td>
<td align="right">6,548,420</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">201,821,080</td>
<td align="right">215,084,400</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">10,824,340</td>
<td align="right">11,473,440</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">226,907,420</td>
<td align="right">240,206,900</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,831,460</td>
<td align="right">11,162,180</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">56,960</td>
<td align="right">59,900</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">235,003,300</td>
<td align="right">246,657,220</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">44,928,320</td>
<td align="right">42,879,200</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">108,486,600</td>
<td align="right">103,651,020</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">4,031,520</td>
<td align="right">4,189,120</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">55,488,940</td>
<td align="right">57,622,040</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">9,887,700</td>
<td align="right">9,516,980</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">71,080</td>
<td align="right">73,620</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">4,553,620</td>
<td align="right">4,715,280</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">5,892,400</td>
<td align="right">5,687,820</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">18,082,940</td>
<td align="right">17,457,620</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">17,740,040</td>
<td align="right">17,131,140</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">13,065,640</td>
<td align="right">13,503,000</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">235,045,300</td>
<td align="right">227,440,340</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">1,139,105,760</td>
<td align="right">1,175,463,320</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">28,982,920</td>
<td align="right">28,063,420</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">28,984,300</td>
<td align="right">28,064,800</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">6,850,160</td>
<td align="right">7,063,240</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">274,914,560</td>
<td align="right">283,334,940</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">144,646,660</td>
<td align="right">140,218,160</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,412,120</td>
<td align="right">8,655,060</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">37,920,100</td>
<td align="right">38,976,480</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">21,764,660</td>
<td align="right">22,351,800</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">58,548,360</td>
<td align="right">56,983,320</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">36,967,180</td>
<td align="right">36,031,720</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">14,645,340</td>
<td align="right">14,294,120</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">4,430,780</td>
<td align="right">4,518,240</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">299,847,860</td>
<td align="right">305,755,840</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,705,740</td>
<td align="right">9,880,940</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,946,200</td>
<td align="right">4,862,300</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">28,172,440</td>
<td align="right">27,715,940</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">103,899,460</td>
<td align="right">105,456,880</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">7,397,180</td>
<td align="right">7,505,000</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">3,240,020</td>
<td align="right">3,281,700</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,413,020</td>
<td align="right">16,206,800</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">2,398,160</td>
<td align="right">2,427,200</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">31,289,400</td>
<td align="right">30,940,580</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,642,700</td>
<td align="right">38,245,440</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">54,526,040</td>
<td align="right">54,003,460</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">103,755,040</td>
<td align="right">102,762,580</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">42,420,800</td>
<td align="right">42,825,500</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">9,849,080</td>
<td align="right">9,939,800</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">149,620</td>
<td align="right">150,940</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">16,294,580</td>
<td align="right">16,409,040</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,976,300</td>
<td align="right">2,995,740</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">142,480,500</td>
<td align="right">143,288,540</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,243,060</td>
<td align="right">1,249,540</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">6,734,920</td>
<td align="right">6,769,920</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">38,367,000</td>
<td align="right">38,186,240</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">206,619,160</td>
<td align="right">205,708,680</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">157,391,560</td>
<td align="right">157,938,880</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,334,960</td>
<td align="right">9,362,900</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">9,880,080</td>
<td align="right">9,902,760</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">11,249,060</td>
<td align="right">11,274,860</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">91,187,680</td>
<td align="right">91,386,780</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">38,326,680</td>
<td align="right">38,275,880</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,581,860</td>
<td align="right">4,587,720</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">90,617,360</td>
<td align="right">90,715,220</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">7,139,100</td>
<td align="right">7,146,540</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">37,057,020</td>
<td align="right">37,048,700</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">2,727,900</td>
<td align="right">2,728,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">2,730,960</td>
<td align="right">2,731,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">2,719,160</td>
<td align="right">2,719,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">37,113,900</td>
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
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">75,960</td>
<td align="right">75,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">61,740</td>
<td align="right">61,740</td>
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
<td align="right">14,700</td>
<td align="right">14,700</td>
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
<td align="right">11,821,480</td>
<td align="right">19.6%</td>
<td align="right">11,152,400</td>
<td align="right">18.7%</td>
<td align="right">-5.7%</td>
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
<td align="right">80.4%</td>
<td align="right">48,411,720</td>
<td align="right">81.3%</td>
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
<td align="right">9,780</td>
<td align="right">100.0%</td>
<td align="right">9,580</td>
<td align="right">100.0%</td>
<td align="right">-2.0%</td>
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
<td align="right">2,760</td>
<td align="right">28.2%</td>
<td align="right">2,540</td>
<td align="right">26.5%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">3,180</td>
<td align="right">32.5%</td>
<td align="right">3,200</td>
<td align="right">33.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">3,160</td>
<td align="right">32.3%</td>
<td align="right">3,160</td>
<td align="right">33.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">320</td>
<td align="right">3.3%</td>
<td align="right">320</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">180</td>
<td align="right">1.8%</td>
<td align="right">180</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">160</td>
<td align="right">1.6%</td>
<td align="right">160</td>
<td align="right">1.7%</td>
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
<td align="right">6,360,620</td>
<td align="right">100.0%</td>
<td align="right">7,294,740</td>
<td align="right">100.0%</td>
<td align="right">14.7%</td>
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
<td align="right">9,692,700</td>
<td align="right">9.2%</td>
<td align="right">9,868,300</td>
<td align="right">9.3%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,146,520</td>
<td align="right">2.0%</td>
<td align="right">2,149,240</td>
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
<td align="right">93,974,740</td>
<td align="right">88.8%</td>
<td align="right">93,973,260</td>
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
<td align="right">12,420</td>
<td align="right">23.2%</td>
<td align="right">12,020</td>
<td align="right">22.6%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,100</td>
<td align="right">76.8%</td>
<td align="right">41,140</td>
<td align="right">77.4%</td>
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
<td align="left">out of range</td>
<td align="right">9,160</td>
<td align="right">73.8%</td>
<td align="right">8,740</td>
<td align="right">72.7%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,680</td>
<td align="right">13.5%</td>
<td align="right">1,700</td>
<td align="right">14.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">720</td>
<td align="right">5.8%</td>
<td align="right">720</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">680</td>
<td align="right">5.5%</td>
<td align="right">680</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">1.4%</td>
<td align="right">180</td>
<td align="right">1.5%</td>
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
<td align="right">16,647,480</td>
<td align="right">2.9%</td>
<td align="right">16,918,800</td>
<td align="right">3.0%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">554,548,280</td>
<td align="right">97.1%</td>
<td align="right">554,291,240</td>
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
<td align="left">Success</td>
<td align="right">318,120</td>
<td align="right">100.0%</td>
<td align="right">323,280</td>
<td align="right">100.0%</td>
<td align="right">1.6%</td>
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
<td align="right">233,700</td>
<td align="right">0.6%</td>
<td align="right">185,420</td>
<td align="right">0.5%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,489,120</td>
<td align="right">4.1%</td>
<td align="right">1,653,720</td>
<td align="right">4.5%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">34,757,180</td>
<td align="right">95.2%</td>
<td align="right">34,739,940</td>
<td align="right">94.9%</td>
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
<td align="right">4,740</td>
<td align="right">29.2%</td>
<td align="right">3,820</td>
<td align="right">28.1%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">11,480</td>
<td align="right">70.8%</td>
<td align="right">9,780</td>
<td align="right">71.9%</td>
<td align="right">-14.8%</td>
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
<td align="right">11,020</td>
<td align="right">96.0%</td>
<td align="right">9,320</td>
<td align="right">95.3%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">200</td>
<td align="right">1.7%</td>
<td align="right">200</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">80</td>
<td align="right">0.7%</td>
<td align="right">80</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">80</td>
<td align="right">0.7%</td>
<td align="right">80</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="right">4,942,300</td>
<td align="right">8.3%</td>
<td align="right">4,858,400</td>
<td align="right">8.2%</td>
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
<td align="right">54,350,400</td>
<td align="right">91.7%</td>
<td align="right">54,350,400</td>
<td align="right">91.8%</td>
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
<td align="right">3,780</td>
<td align="right">100.0%</td>
<td align="right">3,780</td>
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
<td align="right">820</td>
<td align="right">21.7%</td>
<td align="right">860</td>
<td align="right">22.8%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">680</td>
<td align="right">18.0%</td>
<td align="right">660</td>
<td align="right">17.5%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,480</td>
<td align="right">39.2%</td>
<td align="right">1,460</td>
<td align="right">38.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">800</td>
<td align="right">21.2%</td>
<td align="right">800</td>
<td align="right">21.2%</td>
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
<td align="right">22,698,320</td>
<td align="right">15.2%</td>
<td align="right">19,300,540</td>
<td align="right">12.9%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">15,836,700</td>
<td align="right">10.6%</td>
<td align="right">17,192,920</td>
<td align="right">11.5%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">111,207,640</td>
<td align="right">74.3%</td>
<td align="right">112,902,620</td>
<td align="right">75.6%</td>
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
<td align="left">Success</td>
<td align="right">428,240</td>
<td align="right">98.9%</td>
<td align="right">364,140</td>
<td align="right">98.6%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">4,800</td>
<td align="right">1.1%</td>
<td align="right">5,060</td>
<td align="right">1.4%</td>
<td align="right">5.4%</td>
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
<td align="right">100</td>
<td align="right">2.1%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">360</td>
<td align="right">7.5%</td>
<td align="right">500</td>
<td align="right">9.9%</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">680</td>
<td align="right">14.2%</td>
<td align="right">860</td>
<td align="right">17.0%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">800</td>
<td align="right">16.7%</td>
<td align="right">780</td>
<td align="right">15.4%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">2,480</td>
<td align="right">51.7%</td>
<td align="right">2,480</td>
<td align="right">49.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">180</td>
<td align="right">3.8%</td>
<td align="right">180</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">60</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">40</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">40</td>
<td align="right">0.8%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">222,957,720</td>
<td align="right">23.2%</td>
<td align="right">214,119,480</td>
<td align="right">22.5%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">649,221,920</td>
<td align="right">67.4%</td>
<td align="right">648,205,040</td>
<td align="right">68.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">89,991,860</td>
<td align="right">9.3%</td>
<td align="right">90,089,140</td>
<td align="right">9.5%</td>
<td align="right">0.1%</td>
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
<td align="right">4,813,940</td>
<td align="right">99.6%</td>
<td align="right">4,647,980</td>
<td align="right">99.6%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">17,760</td>
<td align="right">0.4%</td>
<td align="right">17,680</td>
<td align="right">0.4%</td>
<td align="right">-0.5%</td>
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
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">1.9%</td>
<td align="right">400</td>
<td align="right">2.3%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">7,140</td>
<td align="right">40.2%</td>
<td align="right">7,020</td>
<td align="right">39.7%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">5,500</td>
<td align="right">31.0%</td>
<td align="right">5,480</td>
<td align="right">31.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">2,840</td>
<td align="right">16.0%</td>
<td align="right">2,840</td>
<td align="right">16.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">620</td>
<td align="right">3.5%</td>
<td align="right">620</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">420</td>
<td align="right">2.4%</td>
<td align="right">420</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">240</td>
<td align="right">1.4%</td>
<td align="right">240</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">180</td>
<td align="right">1.0%</td>
<td align="right">180</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">120</td>
<td align="right">0.7%</td>
<td align="right">120</td>
<td align="right">0.7%</td>
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
<td align="right">225,493,300</td>
<td align="right">100.0%</td>
<td align="right">254,165,020</td>
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
<td align="right">1,960</td>
<td align="right">100.0%</td>
<td align="right">1,960</td>
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
<td align="right">16,401,020</td>
<td align="right">14.0%</td>
<td align="right">16,194,880</td>
<td align="right">13.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">47,041,180</td>
<td align="right">40.1%</td>
<td align="right">47,051,740</td>
<td align="right">40.2%</td>
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
<td align="right">53,913,660</td>
<td align="right">45.9%</td>
<td align="right">53,902,940</td>
<td align="right">46.0%</td>
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
<td align="right">11,600</td>
<td align="right">1.1%</td>
<td align="right">11,520</td>
<td align="right">1.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,017,740</td>
<td align="right">98.9%</td>
<td align="right">1,017,580</td>
<td align="right">98.9%</td>
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
<td align="left">class attr simple</td>
<td align="right">8,960</td>
<td align="right">77.2%</td>
<td align="right">8,880</td>
<td align="right">77.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,040</td>
<td align="right">17.6%</td>
<td align="right">2,040</td>
<td align="right">17.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">360</td>
<td align="right">3.1%</td>
<td align="right">360</td>
<td align="right">3.1%</td>
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
<td align="right">56,960</td>
<td align="right">100.0%</td>
<td align="right">59,900</td>
<td align="right">100.0%</td>
<td align="right">5.2%</td>
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
<td align="right">4,577,980</td>
<td align="right">9.7%</td>
<td align="right">4,583,860</td>
<td align="right">9.7%</td>
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
<td align="left">Failure</td>
<td align="right">3,760</td>
<td align="right">95.9%</td>
<td align="right">3,740</td>
<td align="right">95.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">160</td>
<td align="right">4.1%</td>
<td align="right">160</td>
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
<td align="left">list slice</td>
<td align="right">1,060</td>
<td align="right">28.2%</td>
<td align="right">1,040</td>
<td align="right">27.8%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,440</td>
<td align="right">64.9%</td>
<td align="right">2,440</td>
<td align="right">65.2%</td>
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
<td align="right">4,547,140</td>
<td align="right">1.7%</td>
<td align="right">5,599,140</td>
<td align="right">2.0%</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,214,140</td>
<td align="right">0.8%</td>
<td align="right">2,415,000</td>
<td align="right">0.9%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">265,328,680</td>
<td align="right">97.5%</td>
<td align="right">268,695,020</td>
<td align="right">97.1%</td>
<td align="right">1.3%</td>
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
<td align="right">86,600</td>
<td align="right">57.4%</td>
<td align="right">106,520</td>
<td align="right">63.9%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">64,340</td>
<td align="right">42.6%</td>
<td align="right">60,220</td>
<td align="right">36.1%</td>
<td align="right">-6.4%</td>
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
<td align="right">19,240</td>
<td align="right">29.9%</td>
<td align="right">14,960</td>
<td align="right">24.8%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,040</td>
<td align="right">1.6%</td>
<td align="right">1,220</td>
<td align="right">2.0%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,360</td>
<td align="right">3.7%</td>
<td align="right">2,340</td>
<td align="right">3.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">41,540</td>
<td align="right">64.6%</td>
<td align="right">41,540</td>
<td align="right">69.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">140</td>
<td align="right">0.2%</td>
<td align="right">140</td>
<td align="right">0.2%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">2,062,420,240</td>
<td align="right">35.4%</td>
<td align="right">2,173,625,100</td>
<td align="right">36.1%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">323,161,480</td>
<td align="right">5.5%</td>
<td align="right">312,192,240</td>
<td align="right">5.2%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,273,835,880</td>
<td align="right">56.2%</td>
<td align="right">3,368,099,300</td>
<td align="right">55.9%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">164,141,540</td>
<td align="right">2.8%</td>
<td align="right">166,114,240</td>
<td align="right">2.8%</td>
<td align="right">1.2%</td>
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
<td align="right">6,360,620</td>
<td align="right">3.9%</td>
<td align="right">7,294,740</td>
<td align="right">4.4%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,489,120</td>
<td align="right">0.9%</td>
<td align="right">1,653,720</td>
<td align="right">1.0%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">2,214,140</td>
<td align="right">1.4%</td>
<td align="right">2,415,000</td>
<td align="right">1.5%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">15,836,700</td>
<td align="right">9.7%</td>
<td align="right">17,192,920</td>
<td align="right">10.4%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">11,821,480</td>
<td align="right">7.2%</td>
<td align="right">11,152,400</td>
<td align="right">6.7%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">9,692,700</td>
<td align="right">5.9%</td>
<td align="right">9,868,300</td>
<td align="right">6.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">4,942,300</td>
<td align="right">3.0%</td>
<td align="right">4,858,400</td>
<td align="right">2.9%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">16,401,020</td>
<td align="right">10.0%</td>
<td align="right">16,194,880</td>
<td align="right">9.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">4,577,980</td>
<td align="right">2.8%</td>
<td align="right">4,583,860</td>
<td align="right">2.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">89,991,860</td>
<td align="right">55.1%</td>
<td align="right">90,089,140</td>
<td align="right">54.5%</td>
<td align="right">0.1%</td>
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
<td align="right">11,349,320</td>
<td align="right">3.5%</td>
<td align="right">9,649,660</td>
<td align="right">3.1%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">11,349,000</td>
<td align="right">3.5%</td>
<td align="right">9,650,880</td>
<td align="right">3.1%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">69,007,260</td>
<td align="right">21.4%</td>
<td align="right">63,037,000</td>
<td align="right">20.2%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,071,260</td>
<td align="right">2.8%</td>
<td align="right">9,325,460</td>
<td align="right">3.0%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,766,340</td>
<td align="right">1.5%</td>
<td align="right">4,660,220</td>
<td align="right">1.5%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">79,451,600</td>
<td align="right">24.6%</td>
<td align="right">77,708,600</td>
<td align="right">24.9%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">43,937,420</td>
<td align="right">13.6%</td>
<td align="right">43,079,360</td>
<td align="right">13.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">23,985,060</td>
<td align="right">7.4%</td>
<td align="right">23,779,620</td>
<td align="right">7.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">4,078,000</td>
<td align="right">1.3%</td>
<td align="right">4,093,240</td>
<td align="right">1.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">53,910,480</td>
<td align="right">16.7%</td>
<td align="right">53,899,760</td>
<td align="right">17.3%</td>
<td align="right">-0.0%</td>
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
<td align="right">8,534,560</td>
<td align="right">2.4%</td>
<td align="right">8,143,780</td>
<td align="right">2.3%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,373,320</td>
<td align="right">11.1%</td>
<td align="right">38,976,060</td>
<td align="right">11.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,376,800</td>
<td align="right">11.1%</td>
<td align="right">38,979,540</td>
<td align="right">11.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">39,684,660</td>
<td align="right">11.2%</td>
<td align="right">39,287,400</td>
<td align="right">11.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">39,684,660</td>
<td align="right">11.2%</td>
<td align="right">39,287,400</td>
<td align="right">11.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">314,711,700</td>
<td align="right">88.8%</td>
<td align="right">315,108,960</td>
<td align="right">88.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">313,624,480</td>
<td align="right">88.5%</td>
<td align="right">313,630,960</td>
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
<td align="left">Allocations to 4 kbytes</td>
<td align="right">688,800</td>
<td align="right">0.1%</td>
<td align="right">561,400</td>
<td align="right">0.1%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">2,302,025</td>
<td align="right"></td>
<td align="right">2,051,233</td>
<td align="right"></td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">557,711,040</td>
<td align="right">6.7%</td>
<td align="right">612,618,360</td>
<td align="right">7.3%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">922,968,460</td>
<td align="right">9.9%</td>
<td align="right">975,917,920</td>
<td align="right">10.5%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">34,154,802</td>
<td align="right"></td>
<td align="right">35,799,103</td>
<td align="right"></td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">35,695,889</td>
<td align="right"></td>
<td align="right">37,089,272</td>
<td align="right"></td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,937,643,125</td>
<td align="right">20.7%</td>
<td align="right">1,878,787,035</td>
<td align="right">20.1%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">2,518,024,560</td>
<td align="right">30.1%</td>
<td align="right">2,582,596,900</td>
<td align="right">30.8%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,931,189,757</td>
<td align="right">23.0%</td>
<td align="right">1,884,939,118</td>
<td align="right">22.5%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">3,372,170,260</td>
<td align="right">40.2%</td>
<td align="right">3,302,499,659</td>
<td align="right">39.4%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">3,099,770,955</td>
<td align="right">33.2%</td>
<td align="right">3,053,120,007</td>
<td align="right">32.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">3,380,624,980</td>
<td align="right">36.2%</td>
<td align="right">3,421,484,840</td>
<td align="right">36.7%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">346,240</td>
<td align="right">0.0%</td>
<td align="right">345,520</td>
<td align="right">0.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">608,258,138</td>
<td align="right"></td>
<td align="right">607,619,204</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">196,389,655</td>
<td align="right"></td>
<td align="right">196,542,407</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">572,056,220</td>
<td align="right">70.7%</td>
<td align="right">571,833,580</td>
<td align="right">70.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">236,690,100</td>
<td align="right">29.3%</td>
<td align="right">236,756,300</td>
<td align="right">29.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">236,663,020</td>
<td align="right"></td>
<td align="right">236,729,160</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">461,237,638</td>
<td align="right"></td>
<td align="right">461,146,957</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">571,021,180</td>
<td align="right">70.6%</td>
<td align="right">570,926,660</td>
<td align="right">70.6%</td>
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
<td align="right">25,980</td>
<td align="right">72,818,960</td>
<td align="right">1,464,592,360</td>
<td align="right">25,940</td>
<td align="right">72,682,260</td>
<td align="right">1,451,247,120</td>
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">7,200</td>
<td align="right">1.9%</td>
<td align="right">2,800</td>
<td align="right">1.2%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">277,620</td>
<td align="right">72.5%</td>
<td align="right">120,900</td>
<td align="right">54.0%</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">382,760</td>
<td align="right"></td>
<td align="right">224,080</td>
<td align="right"></td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,260</td>
<td align="right">0.3%</td>
<td align="right">740</td>
<td align="right">0.3%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,240</td>
<td align="right">0.8%</td>
<td align="right">3,880</td>
<td align="right">1.7%</td>
<td align="right">19.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,680</td>
<td align="right">0.4%</td>
<td align="right">1,400</td>
<td align="right">0.6%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">131,620</td>
<td align="right">34.4%</td>
<td align="right">120,240</td>
<td align="right">53.7%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">7,051,701,540</td>
<td align="right">1,261.9%</td>
<td align="right">6,706,967,560</td>
<td align="right">1,202.3%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">103,880</td>
<td align="right">27.1%</td>
<td align="right">102,440</td>
<td align="right">45.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">558,816,140</td>
<td align="right"></td>
<td align="right">557,830,640</td>
<td align="right"></td>
<td align="right">-0.2%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">260,780</td>
<td align="right">93.9%</td>
<td align="right">110,940</td>
<td align="right">91.8%</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">277,620</td>
<td align="right"></td>
<td align="right">120,900</td>
<td align="right"></td>
<td align="right">-56.5%</td>
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
<td align="right">13,180</td>
<td align="right">4.7%</td>
<td align="right">10,280</td>
<td align="right">8.5%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">39,780</td>
<td align="right">14.3%</td>
<td align="right">21,660</td>
<td align="right">17.9%</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">89,820</td>
<td align="right">32.4%</td>
<td align="right">42,160</td>
<td align="right">34.9%</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">83,140</td>
<td align="right">29.9%</td>
<td align="right">25,960</td>
<td align="right">21.5%</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">39,140</td>
<td align="right">14.1%</td>
<td align="right">15,000</td>
<td align="right">12.4%</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">10,520</td>
<td align="right">3.8%</td>
<td align="right">3,960</td>
<td align="right">3.3%</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,900</td>
<td align="right">0.7%</td>
<td align="right">1,820</td>
<td align="right">1.5%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">-57.1%</td>
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
<td align="right">1,720</td>
<td align="right">0.6%</td>
<td align="right">720</td>
<td align="right">0.6%</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">33,060</td>
<td align="right">11.9%</td>
<td align="right">16,260</td>
<td align="right">13.4%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">51,980</td>
<td align="right">18.7%</td>
<td align="right">37,880</td>
<td align="right">31.3%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">104,020</td>
<td align="right">37.5%</td>
<td align="right">32,900</td>
<td align="right">27.2%</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">49,960</td>
<td align="right">18.0%</td>
<td align="right">15,000</td>
<td align="right">12.4%</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">15,940</td>
<td align="right">5.7%</td>
<td align="right">6,300</td>
<td align="right">5.2%</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,580</td>
<td align="right">1.3%</td>
<td align="right">1,620</td>
<td align="right">1.3%</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">520</td>
<td align="right">0.2%</td>
<td align="right">260</td>
<td align="right">0.2%</td>
<td align="right">-50.0%</td>
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
<td align="right">120</td>
<td align="right">6,360</td>
<td align="right">5,200.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">162,120</td>
<td align="right">4,520</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">27,540</td>
<td align="right">3,160</td>
<td align="right">-88.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">2,012,180</td>
<td align="right">351,840</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,795,780</td>
<td align="right">347,320</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">694,900</td>
<td align="right">150,660</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">454,980</td>
<td align="right">806,200</td>
<td align="right">77.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">699,920</td>
<td align="right">169,260</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,224,980</td>
<td align="right">2,144,480</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,224,980</td>
<td align="right">2,144,480</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,508,320</td>
<td align="right">1,460,560</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">324,740</td>
<td align="right">111,860</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">263,380</td>
<td align="right">92,620</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">309,120</td>
<td align="right">111,860</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">821,500</td>
<td align="right">1,310,580</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">10,163,840</td>
<td align="right">4,262,340</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">124,140</td>
<td align="right">57,000</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,346,500</td>
<td align="right">2,146,720</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">4,430,380</td>
<td align="right">2,265,180</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,292,080</td>
<td align="right">1,917,400</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">1,316,180</td>
<td align="right">682,420</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">3,362,600</td>
<td align="right">1,744,920</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">28,491,600</td>
<td align="right">15,596,100</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">9,184,480</td>
<td align="right">5,322,060</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">237,960</td>
<td align="right">138,000</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">26,403,760</td>
<td align="right">15,804,060</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">257,160</td>
<td align="right">154,140</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">294,640</td>
<td align="right">180,180</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">9,434,180</td>
<td align="right">5,817,200</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">16,020</td>
<td align="right">9,900</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">38,738,400</td>
<td align="right">23,968,520</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">537,800</td>
<td align="right">339,860</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">53,269,480</td>
<td align="right">34,061,160</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,670,480</td>
<td align="right">1,883,000</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">63,981,560</td>
<td align="right">45,594,600</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">16,830,420</td>
<td align="right">21,666,000</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">6,462,160</td>
<td align="right">4,630,740</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">30,582,240</td>
<td align="right">21,935,220</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">3,141,880</td>
<td align="right">2,254,860</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">3,141,880</td>
<td align="right">2,254,860</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,216,120</td>
<td align="right">1,615,760</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">33,477,620</td>
<td align="right">42,233,460</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">8,647,080</td>
<td align="right">6,485,900</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">1,479,400</td>
<td align="right">1,848,680</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">10,038,660</td>
<td align="right">7,560,320</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">39,834,800</td>
<td align="right">30,216,340</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">24,866,980</td>
<td align="right">18,943,700</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,158,840</td>
<td align="right">7,746,760</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">4,125,140</td>
<td align="right">3,183,740</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">24,994,220</td>
<td align="right">19,338,640</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">6,400,220</td>
<td align="right">5,007,380</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,355,860</td>
<td align="right">10,146,820</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">827,620</td>
<td align="right">650,820</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">34,855,600</td>
<td align="right">27,422,080</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">1,910,000</td>
<td align="right">1,507,400</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,047,700</td>
<td align="right">2,434,980</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">38,526,920</td>
<td align="right">30,858,560</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">35,477,640</td>
<td align="right">28,423,580</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">2,802,040</td>
<td align="right">2,250,720</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">12,371,760</td>
<td align="right">9,995,120</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">39,133,380</td>
<td align="right">31,648,740</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">2,237,920</td>
<td align="right">1,816,640</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">2,236,840</td>
<td align="right">1,815,800</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">221,860</td>
<td align="right">180,180</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,584,120</td>
<td align="right">1,288,020</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">887,240</td>
<td align="right">725,580</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">339,640</td>
<td align="right">278,040</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">12,263,300</td>
<td align="right">10,130,200</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">5,738,200</td>
<td align="right">4,804,080</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">14,190,580</td>
<td align="right">16,239,700</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">110,786,160</td>
<td align="right">95,260,700</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">110,795,420</td>
<td align="right">95,270,560</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">102,975,360</td>
<td align="right">89,264,440</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">196,362,460</td>
<td align="right">170,388,400</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">840,980</td>
<td align="right">731,880</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">5,483,840</td>
<td align="right">4,787,800</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">15,516,480</td>
<td align="right">13,580,740</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">32,966,620</td>
<td align="right">29,230,760</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">38,116,460</td>
<td align="right">33,940,660</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">4,095,080</td>
<td align="right">3,657,720</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">18,346,480</td>
<td align="right">16,420,680</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">16,561,040</td>
<td align="right">14,868,580</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">13,666,860</td>
<td align="right">12,291,780</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">16,273,620</td>
<td align="right">14,682,060</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">16,273,620</td>
<td align="right">14,682,060</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">6,360,940</td>
<td align="right">6,969,840</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">50,554,320</td>
<td align="right">55,259,980</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">2,147,880</td>
<td align="right">1,948,620</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">2,147,880</td>
<td align="right">1,948,620</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">117,616,760</td>
<td align="right">127,855,920</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">129,706,860</td>
<td align="right">118,488,100</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">26,548,040</td>
<td align="right">28,744,360</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">244,140</td>
<td align="right">224,700</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">244,140</td>
<td align="right">224,700</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">101,450,000</td>
<td align="right">109,249,260</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">997,980</td>
<td align="right">922,680</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">997,980</td>
<td align="right">922,680</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">32,946,660</td>
<td align="right">30,492,700</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">9,231,320</td>
<td align="right">9,900,400</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">24,584,800</td>
<td align="right">22,814,940</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">86,701,100</td>
<td align="right">80,478,440</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">44,246,500</td>
<td align="right">47,414,900</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">15,324,320</td>
<td align="right">16,310,780</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">456,274,200</td>
<td align="right">427,131,260</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">15,253,440</td>
<td align="right">16,211,980</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">475,840</td>
<td align="right">446,800</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">36,217,800</td>
<td align="right">34,060,180</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">48,258,420</td>
<td align="right">45,431,180</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">71,241,320</td>
<td align="right">75,314,660</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">16,795,320</td>
<td align="right">15,839,120</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">559,444,960</td>
<td align="right">528,959,400</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">115,139,880</td>
<td align="right">108,894,900</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">3,332,820</td>
<td align="right">3,513,580</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">247,732,400</td>
<td align="right">234,658,640</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">107,656,340</td>
<td align="right">113,239,460</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,182,620</td>
<td align="right">1,122,100</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">16,464,540</td>
<td align="right">15,622,180</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">46,426,020</td>
<td align="right">44,151,280</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">11,323,280</td>
<td align="right">10,776,080</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">22,696,520</td>
<td align="right">21,640,140</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">10,065,160</td>
<td align="right">10,510,800</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">27,440</td>
<td align="right">26,280</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">27,440</td>
<td align="right">26,280</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">34,240,620</td>
<td align="right">35,673,460</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">97,111,320</td>
<td align="right">100,750,560</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">48,620</td>
<td align="right">46,800</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">146,600</td>
<td align="right">141,120</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">5,691,040</td>
<td align="right">5,897,180</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">53,251,540</td>
<td align="right">51,380,460</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">119,558,680</td>
<td align="right">115,443,320</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">13,551,380</td>
<td align="right">14,007,880</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">6,889,280</td>
<td align="right">6,668,860</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">35,935,460</td>
<td align="right">34,893,220</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">6,751,440</td>
<td align="right">6,575,940</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">107,855,520</td>
<td align="right">110,346,040</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">43,761,060</td>
<td align="right">44,754,020</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">14,230,880</td>
<td align="right">13,935,880</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">5,367,620</td>
<td align="right">5,256,420</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">10,907,360</td>
<td align="right">11,128,500</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">567,320</td>
<td align="right">578,640</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">5,646,220</td>
<td align="right">5,753,720</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">55,872,560</td>
<td align="right">54,818,280</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">73,004,200</td>
<td align="right">71,663,920</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">437,924,840</td>
<td align="right">430,804,660</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,136,720</td>
<td align="right">3,187,520</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">6,793,900</td>
<td align="right">6,686,080</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">53,503,260</td>
<td align="right">52,661,380</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">210,160</td>
<td align="right">207,220</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">7,250,900</td>
<td align="right">7,334,800</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">18,605,940</td>
<td align="right">18,422,600</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">9,288,580</td>
<td align="right">9,197,860</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">74,507,740</td>
<td align="right">73,913,700</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">298,280</td>
<td align="right">295,980</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">1,645,940</td>
<td align="right">1,635,340</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">4,096,660</td>
<td align="right">4,070,860</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">607,074,560</td>
<td align="right">603,261,820</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">211,640</td>
<td align="right">210,320</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">525,468,040</td>
<td align="right">522,463,540</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">17,172,940</td>
<td align="right">17,075,380</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">110,380</td>
<td align="right">109,800</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">68,827,100</td>
<td align="right">68,474,520</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">45,631,440</td>
<td align="right">45,404,920</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">47,438,500</td>
<td align="right">47,225,420</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">965,140</td>
<td align="right">963,080</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">558,816,140</td>
<td align="right">557,830,640</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">14,287,720</td>
<td align="right">14,299,160</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,012,760</td>
<td align="right">4,010,060</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">242,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">63,400</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">41,300</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">26,460</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">7,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">5,880</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">4,780</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">2,940</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">2,540</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">1,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">600</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">540</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">540</td>
<td align="right"></td>
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
<td align="right">8,880</td>
<td align="right">2,860</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">1,480</td>
<td align="right">720</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,860</td>
<td align="right">3,020</td>
<td align="right">-21.8%</td>
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
Stats gathered on: 2024-11-12
