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
<td align="left">NOT_TAKEN</td>
<td align="right">108,721</td>
<td align="right">225,968</td>
<td align="right">107.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">849,890</td>
<td align="right">26,196</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">657,649</td>
<td align="right">259,235</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,147,858</td>
<td align="right">461,486</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,421,197</td>
<td align="right">572,432</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">514,619</td>
<td align="right">223,450</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">69,682</td>
<td align="right">32,133</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">723,271</td>
<td align="right">335,848</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,478,762</td>
<td align="right">1,264,145</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,690,189</td>
<td align="right">887,339</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,753,394</td>
<td align="right">2,499,093</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">278,137</td>
<td align="right">161,375</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">666,777</td>
<td align="right">389,115</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,956,939</td>
<td align="right">4,192,943</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,183,811</td>
<td align="right">2,551,501</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,749,617</td>
<td align="right">2,361,163</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">554,393</td>
<td align="right">358,842</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">260,331</td>
<td align="right">172,678</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,011</td>
<td align="right">1,375</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,689,882</td>
<td align="right">3,210,449</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">9,859,011</td>
<td align="right">7,002,485</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">9,034,084</td>
<td align="right">6,483,391</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">15,218,824</td>
<td align="right">11,193,970</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">147,233</td>
<td align="right">110,101</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">3,513,947</td>
<td align="right">2,632,508</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">985,900</td>
<td align="right">743,080</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,686,723</td>
<td align="right">2,027,689</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">20,099,504</td>
<td align="right">15,321,945</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,056,391</td>
<td align="right">1,655,042</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,972,881</td>
<td align="right">1,612,724</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,198,788</td>
<td align="right">982,729</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,235,241</td>
<td align="right">1,022,000</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">30,014,057</td>
<td align="right">25,319,011</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">232,083</td>
<td align="right">196,345</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">311,409</td>
<td align="right">265,862</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">18,789,671</td>
<td align="right">16,074,384</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">753,406</td>
<td align="right">645,878</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">3,761,985</td>
<td align="right">4,283,677</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,583,072</td>
<td align="right">2,226,525</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">44,482,074</td>
<td align="right">38,356,487</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">43,797,377</td>
<td align="right">37,886,386</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">448,618</td>
<td align="right">390,535</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">8,054,979</td>
<td align="right">7,027,067</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">30,517,086</td>
<td align="right">26,939,386</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,378,395</td>
<td align="right">2,104,887</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,421,555</td>
<td align="right">4,802,595</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">67,864</td>
<td align="right">74,759</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">3,042,615</td>
<td align="right">2,746,871</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">24,007</td>
<td align="right">21,717</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,610,293</td>
<td align="right">4,181,752</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">961,126</td>
<td align="right">878,594</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">3,673,657</td>
<td align="right">3,365,172</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,352,219</td>
<td align="right">8,596,138</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,003,453</td>
<td align="right">928,277</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">26,909,589</td>
<td align="right">24,911,540</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">86,671</td>
<td align="right">80,267</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">31,615,889</td>
<td align="right">29,380,845</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">14,884,385</td>
<td align="right">13,897,224</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,903,145</td>
<td align="right">1,777,704</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,160,432</td>
<td align="right">1,085,797</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">164,870,069</td>
<td align="right">154,519,148</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">14,614,364</td>
<td align="right">13,711,800</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">24,573,328</td>
<td align="right">23,182,276</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,501,720</td>
<td align="right">6,165,169</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,331,916</td>
<td align="right">2,219,479</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,022,451</td>
<td align="right">2,882,097</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,825,196</td>
<td align="right">3,696,609</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,961,624</td>
<td align="right">1,898,933</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">14,173,670</td>
<td align="right">13,729,563</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,690,602</td>
<td align="right">9,395,709</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">12,265,539</td>
<td align="right">11,909,635</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,007,726</td>
<td align="right">1,949,792</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,729</td>
<td align="right">4,593</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">8,510,760</td>
<td align="right">8,271,541</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,788,548</td>
<td align="right">1,738,760</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">9,922,816</td>
<td align="right">9,650,786</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">7,043,840</td>
<td align="right">6,883,760</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,287,045</td>
<td align="right">12,021,481</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">18,685,076</td>
<td align="right">18,296,833</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">669,232</td>
<td align="right">656,415</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">3,030</td>
<td align="right">2,972</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">57,168,370</td>
<td align="right">56,138,445</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,879,921</td>
<td align="right">3,811,277</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,489,749</td>
<td align="right">6,376,416</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,528,627</td>
<td align="right">1,546,181</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">37,154,764</td>
<td align="right">36,738,082</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">47,579</td>
<td align="right">47,047</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,726,142</td>
<td align="right">1,743,695</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">622,298</td>
<td align="right">616,108</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,496,869</td>
<td align="right">1,482,081</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,836,699</td>
<td align="right">2,810,512</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,221,244</td>
<td align="right">2,240,336</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">27,120,261</td>
<td align="right">26,955,592</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">108,646</td>
<td align="right">108,003</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,822,993</td>
<td align="right">6,787,330</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,933,271</td>
<td align="right">1,926,365</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,779,927</td>
<td align="right">3,767,433</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,450</td>
<td align="right">11,416</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,617,130</td>
<td align="right">1,612,490</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">819,855</td>
<td align="right">817,529</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">42,163</td>
<td align="right">42,047</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">57,337,333</td>
<td align="right">57,206,105</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,801,861</td>
<td align="right">2,808,224</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,231,398</td>
<td align="right">4,240,176</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">4,301,844</td>
<td align="right">4,294,094</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,508,307</td>
<td align="right">4,516,311</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">46,284,315</td>
<td align="right">46,206,152</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">81,525</td>
<td align="right">81,395</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">984,602</td>
<td align="right">983,960</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">254,951</td>
<td align="right">254,821</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">25,464,440</td>
<td align="right">25,454,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">257,149</td>
<td align="right">257,065</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,666,459</td>
<td align="right">2,665,740</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">289,765</td>
<td align="right">289,696</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,990,150</td>
<td align="right">7,988,444</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,385,394</td>
<td align="right">1,385,306</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">50,144</td>
<td align="right">50,147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">437,896</td>
<td align="right">437,887</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">196,787</td>
<td align="right">196,785</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">353,412</td>
<td align="right">353,409</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">960,421</td>
<td align="right">960,417</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,625,053</td>
<td align="right">5,625,050</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,902,966</td>
<td align="right">7,902,969</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,219,329</td>
<td align="right">11,219,328</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">14,615,998</td>
<td align="right">14,615,998</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">11,715,923</td>
<td align="right">11,715,923</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,257,421</td>
<td align="right">8,257,421</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,151,847</td>
<td align="right">8,151,847</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,494,864</td>
<td align="right">6,494,864</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">5,420,871</td>
<td align="right">5,420,871</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">5,331,831</td>
<td align="right">5,331,831</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,689,757</td>
<td align="right">3,689,757</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,887,083</td>
<td align="right">2,887,083</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,554,934</td>
<td align="right">2,554,934</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,375,009</td>
<td align="right">1,375,009</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,030,194</td>
<td align="right">1,030,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">822,943</td>
<td align="right">822,943</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">820,138</td>
<td align="right">820,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">688,601</td>
<td align="right">688,601</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">614,126</td>
<td align="right">614,126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">614,126</td>
<td align="right">614,126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">543,475</td>
<td align="right">543,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">531,405</td>
<td align="right">531,405</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">281,060</td>
<td align="right">281,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">280,940</td>
<td align="right">280,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">167,374</td>
<td align="right">167,374</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">165,054</td>
<td align="right">165,054</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">163,891</td>
<td align="right">163,891</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">136,208</td>
<td align="right">136,208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">122,296</td>
<td align="right">122,296</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,081</td>
<td align="right">98,081</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">83,960</td>
<td align="right">83,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,426</td>
<td align="right">72,426</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">63,727</td>
<td align="right">63,727</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">58,703</td>
<td align="right">58,703</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">55,974</td>
<td align="right">55,974</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,970</td>
<td align="right">53,970</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">42,789</td>
<td align="right">42,789</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">26,293</td>
<td align="right">26,293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">22,736</td>
<td align="right">22,736</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">19,652</td>
<td align="right">19,652</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">18,923</td>
<td align="right">18,923</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">14,002</td>
<td align="right">14,002</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,687</td>
<td align="right">5,687</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,957</td>
<td align="right">2,957</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,396</td>
<td align="right">2,396</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,121</td>
<td align="right">1,121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,055</td>
<td align="right">1,055</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">975</td>
<td align="right">975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">942</td>
<td align="right">942</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">922</td>
<td align="right">922</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">782</td>
<td align="right">782</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">714</td>
<td align="right">714</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">522</td>
<td align="right">522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">261</td>
<td align="right">261</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">191</td>
<td align="right">191</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">59</td>
<td align="right">59</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">29</td>
<td align="right">29</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">10</td>
<td align="right">10</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">62,986</td>
<td align="right">0.2%</td>
<td align="right">17,724</td>
<td align="right">0.1%</td>
<td align="right">-71.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,677,652</td>
<td align="right">10.4%</td>
<td align="right">2,020,197</td>
<td align="right">8.7%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,105,059</td>
<td align="right">89.4%</td>
<td align="right">21,066,640</td>
<td align="right">91.2%</td>
<td align="right">-8.8%</td>
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
<td align="right">3,107</td>
<td align="right">30.3%</td>
<td align="right">2,253</td>
<td align="right">28.8%</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,138</td>
<td align="right">69.7%</td>
<td align="right">5,559</td>
<td align="right">71.2%</td>
<td align="right">-22.1%</td>
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
<td align="right">2,721</td>
<td align="right">38.1%</td>
<td align="right">1,189</td>
<td align="right">21.4%</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">4</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">177</td>
<td align="right">2.5%</td>
<td align="right">151</td>
<td align="right">2.7%</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">715</td>
<td align="right">10.0%</td>
<td align="right">705</td>
<td align="right">12.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">232</td>
<td align="right">3.3%</td>
<td align="right">229</td>
<td align="right">4.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">200</td>
<td align="right">2.8%</td>
<td align="right">198</td>
<td align="right">3.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">986</td>
<td align="right">13.8%</td>
<td align="right">983</td>
<td align="right">17.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">808</td>
<td align="right">11.3%</td>
<td align="right">807</td>
<td align="right">14.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">743</td>
<td align="right">10.4%</td>
<td align="right">743</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">152</td>
<td align="right">2.1%</td>
<td align="right">152</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">117</td>
<td align="right">1.6%</td>
<td align="right">117</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.9%</td>
<td align="right">66</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">47</td>
<td align="right">0.7%</td>
<td align="right">47</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">36</td>
<td align="right">0.5%</td>
<td align="right">36</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.4%</td>
<td align="right">26</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">23</td>
<td align="right">0.3%</td>
<td align="right">23</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">10</td>
<td align="right">0.1%</td>
<td align="right">10</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">9</td>
<td align="right">0.1%</td>
<td align="right">9</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">4</td>
<td align="right">0.1%</td>
<td align="right">4</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">554,393</td>
<td align="right">100.0%</td>
<td align="right">358,842</td>
<td align="right">100.0%</td>
<td align="right">-35.3%</td>
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
<td align="right">7,751,206</td>
<td align="right">11.6%</td>
<td align="right">7,674,818</td>
<td align="right">11.5%</td>
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
<td align="right">7,611,898</td>
<td align="right">11.4%</td>
<td align="right">7,536,949</td>
<td align="right">11.3%</td>
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
<td align="right">59,022,652</td>
<td align="right">88.4%</td>
<td align="right">59,093,489</td>
<td align="right">88.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">8,513</td>
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
<td align="right">165,601</td>
<td align="right">100.0%</td>
<td align="right">164,162</td>
<td align="right">100.0%</td>
<td align="right">-0.9%</td>
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
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">568,395</td>
<td align="right">97.8%</td>
<td align="right">568,395</td>
<td align="right">97.8%</td>
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
<td align="right">578,755</td>
<td align="right">99.6%</td>
<td align="right">578,755</td>
<td align="right">99.6%</td>
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
<td align="right">12,756</td>
<td align="right">100.0%</td>
<td align="right">12,756</td>
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
<td align="right">999,468</td>
<td align="right">5.5%</td>
<td align="right">924,378</td>
<td align="right">5.1%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,028,448</td>
<td align="right">94.4%</td>
<td align="right">17,028,448</td>
<td align="right">94.8%</td>
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
<td align="right">3,320</td>
<td align="right">0.0%</td>
<td align="right">3,320</td>
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
<td align="right">2,546</td>
<td align="right">62.8%</td>
<td align="right">2,460</td>
<td align="right">62.0%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,506</td>
<td align="right">37.2%</td>
<td align="right">1,506</td>
<td align="right">38.0%</td>
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
<td align="left">different types</td>
<td align="right">1,103</td>
<td align="right">43.3%</td>
<td align="right">1,041</td>
<td align="right">42.3%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">627</td>
<td align="right">24.6%</td>
<td align="right">602</td>
<td align="right">24.5%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">237</td>
<td align="right">9.3%</td>
<td align="right">238</td>
<td align="right">9.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">207</td>
<td align="right">8.1%</td>
<td align="right">207</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">161</td>
<td align="right">6.3%</td>
<td align="right">161</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">90</td>
<td align="right">3.5%</td>
<td align="right">90</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">51</td>
<td align="right">2.0%</td>
<td align="right">51</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">48</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">20</td>
<td align="right">0.8%</td>
<td align="right">20</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">2,471,802</td>
<td align="right">37.4%</td>
<td align="right">1,257,334</td>
<td align="right">23.3%</td>
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
<td align="right">4,104,246</td>
<td align="right">62.1%</td>
<td align="right">4,104,246</td>
<td align="right">76.1%</td>
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
<td align="right">26,561</td>
<td align="right">0.4%</td>
<td align="right">26,561</td>
<td align="right">0.5%</td>
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
<td align="right">6,252</td>
<td align="right">83.7%</td>
<td align="right">6,103</td>
<td align="right">83.4%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,219</td>
<td align="right">16.3%</td>
<td align="right">1,219</td>
<td align="right">16.6%</td>
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
<td align="right">510</td>
<td align="right">8.2%</td>
<td align="right">487</td>
<td align="right">8.0%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,164</td>
<td align="right">18.6%</td>
<td align="right">1,137</td>
<td align="right">18.6%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,285</td>
<td align="right">52.5%</td>
<td align="right">3,212</td>
<td align="right">52.6%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,293</td>
<td align="right">20.7%</td>
<td align="right">1,267</td>
<td align="right">20.8%</td>
<td align="right">-2.0%</td>
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
<td align="right">225,671</td>
<td align="right">0.7%</td>
<td align="right">151,763</td>
<td align="right">0.6%</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,679,866</td>
<td align="right">14.7%</td>
<td align="right">3,203,755</td>
<td align="right">11.8%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">26,888,064</td>
<td align="right">84.5%</td>
<td align="right">23,744,285</td>
<td align="right">87.6%</td>
<td align="right">-11.7%</td>
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
<td align="right">8,774</td>
<td align="right">61.5%</td>
<td align="right">5,453</td>
<td align="right">57.2%</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,496</td>
<td align="right">38.5%</td>
<td align="right">4,084</td>
<td align="right">42.8%</td>
<td align="right">-25.7%</td>
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
<td align="left">seq iter</td>
<td align="right">15</td>
<td align="right">0.2%</td>
<td align="right">4</td>
<td align="right">0.1%</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">4,237</td>
<td align="right">48.3%</td>
<td align="right">1,257</td>
<td align="right">23.1%</td>
<td align="right">-70.3%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">9</td>
<td align="right">0.1%</td>
<td align="right">6</td>
<td align="right">0.1%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,323</td>
<td align="right">15.1%</td>
<td align="right">1,172</td>
<td align="right">21.5%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,425</td>
<td align="right">16.2%</td>
<td align="right">1,269</td>
<td align="right">23.3%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">578</td>
<td align="right">6.6%</td>
<td align="right">558</td>
<td align="right">10.2%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">306</td>
<td align="right">3.5%</td>
<td align="right">306</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">256</td>
<td align="right">2.9%</td>
<td align="right">256</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">251</td>
<td align="right">2.9%</td>
<td align="right">251</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">171</td>
<td align="right">1.9%</td>
<td align="right">171</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">146</td>
<td align="right">1.7%</td>
<td align="right">146</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">46</td>
<td align="right">0.5%</td>
<td align="right">46</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">11</td>
<td align="right">0.2%</td>
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
<td align="left">generator</td>
<td align="right">5,054,786</td>
<td align="right">5,054,786 / 0 !!</td>
<td align="right">5,054,786</td>
<td align="right">5,054,786 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">4,412,958</td>
<td align="right">4,412,958 / 0 !!</td>
<td align="right">4,412,958</td>
<td align="right">4,412,958 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,228,632</td>
<td align="right">1,228,632 / 0 !!</td>
<td align="right">1,228,632</td>
<td align="right">1,228,632 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">609,320</td>
<td align="right">609,320 / 0 !!</td>
<td align="right">609,320</td>
<td align="right">609,320 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">552,640</td>
<td align="right">552,640 / 0 !!</td>
<td align="right">552,640</td>
<td align="right">552,640 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">285,344</td>
<td align="right">285,344 / 0 !!</td>
<td align="right">285,344</td>
<td align="right">285,344 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">161,360</td>
<td align="right">161,360 / 0 !!</td>
<td align="right">161,360</td>
<td align="right">161,360 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">7,668</td>
<td align="right">7,668 / 0 !!</td>
<td align="right">7,668</td>
<td align="right">7,668 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">629</td>
<td align="right">629 / 0 !!</td>
<td align="right">629</td>
<td align="right">629 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3</td>
<td align="right">3 / 0 !!</td>
<td align="right">3</td>
<td align="right">3 / 0 !!</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">78,348,722</td>
<td align="right">62.8%</td>
<td align="right">73,875,771</td>
<td align="right">62.0%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,040,203</td>
<td align="right">11.3%</td>
<td align="right">13,597,075</td>
<td align="right">11.4%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,184,138</td>
<td align="right">25.8%</td>
<td align="right">31,630,321</td>
<td align="right">26.5%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">198,684</td>
<td align="right">0.2%</td>
<td align="right">198,684</td>
<td align="right">0.2%</td>
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
<td align="right">625,468</td>
<td align="right">89.6%</td>
<td align="right">614,989</td>
<td align="right">89.6%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">72,742</td>
<td align="right">10.4%</td>
<td align="right">71,744</td>
<td align="right">10.4%</td>
<td align="right">-1.4%</td>
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
<td align="right">905</td>
<td align="right">1.2%</td>
<td align="right">946</td>
<td align="right">1.3%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,582</td>
<td align="right">4.9%</td>
<td align="right">3,449</td>
<td align="right">4.8%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">66</td>
<td align="right">0.1%</td>
<td align="right">67</td>
<td align="right">0.1%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,538</td>
<td align="right">2.1%</td>
<td align="right">1,540</td>
<td align="right">2.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,565</td>
<td align="right">2.2%</td>
<td align="right">1,564</td>
<td align="right">2.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3,986</td>
<td align="right">5.5%</td>
<td align="right">3,985</td>
<td align="right">5.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">836</td>
<td align="right">1.1%</td>
<td align="right">836</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">450</td>
<td align="right">0.6%</td>
<td align="right">450</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">255</td>
<td align="right">0.4%</td>
<td align="right">255</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">203</td>
<td align="right">0.3%</td>
<td align="right">203</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">193</td>
<td align="right">0.3%</td>
<td align="right">193</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">117</td>
<td align="right">0.2%</td>
<td align="right">117</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="right">56,937,631</td>
<td align="right">100.0%</td>
<td align="right">50,226,211</td>
<td align="right">99.9%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,950</td>
<td align="right">0.0%</td>
<td align="right">4,950</td>
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
<td align="right">435</td>
<td align="right">0.0%</td>
<td align="right">435</td>
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
<td align="right">4,348</td>
<td align="right">0.0%</td>
<td align="right">4,348</td>
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
<td align="right">17,854</td>
<td align="right">100.0%</td>
<td align="right">17,854</td>
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
<td align="right">101</td>
<td align="right">0.0%</td>
<td align="right">101</td>
<td align="right">0.0%</td>
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
<td align="right">708,529</td>
<td align="right">99.9%</td>
<td align="right">708,529</td>
<td align="right">99.9%</td>
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
<td align="right">421</td>
<td align="right">100.0%</td>
<td align="right">421</td>
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
<td align="right">6,491,901</td>
<td align="right">54.9%</td>
<td align="right">6,491,901</td>
<td align="right">54.9%</td>
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
<td align="right">5,331,831</td>
<td align="right">45.1%</td>
<td align="right">5,331,831</td>
<td align="right">45.1%</td>
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
<td align="right">103</td>
<td align="right">3.5%</td>
<td align="right">103</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,860</td>
<td align="right">96.5%</td>
<td align="right">2,860</td>
<td align="right">96.5%</td>
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
<td align="right">2,057</td>
<td align="right">71.9%</td>
<td align="right">2,057</td>
<td align="right">71.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">51</td>
<td align="right">1.8%</td>
<td align="right">51</td>
<td align="right">1.8%</td>
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
<td align="right">1,378,083</td>
<td align="right">9.9%</td>
<td align="right">1,377,996</td>
<td align="right">9.9%</td>
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
<td align="right">10,738,221</td>
<td align="right">77.5%</td>
<td align="right">10,738,221</td>
<td align="right">77.5%</td>
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
<td align="right">1,728,748</td>
<td align="right">12.5%</td>
<td align="right">1,728,748</td>
<td align="right">12.5%</td>
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
<td align="right">3,073</td>
<td align="right">7.7%</td>
<td align="right">3,072</td>
<td align="right">7.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">36,745</td>
<td align="right">92.3%</td>
<td align="right">36,745</td>
<td align="right">92.3%</td>
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
<td align="right">10</td>
<td align="right">0.3%</td>
<td align="right">9</td>
<td align="right">0.3%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">57,827</td>
<td align="right">1,881.8%</td>
<td align="right">56,920</td>
<td align="right">1,852.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,385</td>
<td align="right">45.1%</td>
<td align="right">1,385</td>
<td align="right">45.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">572</td>
<td align="right">18.6%</td>
<td align="right">572</td>
<td align="right">18.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">401</td>
<td align="right">13.0%</td>
<td align="right">401</td>
<td align="right">13.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">280</td>
<td align="right">9.1%</td>
<td align="right">280</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">230</td>
<td align="right">7.5%</td>
<td align="right">230</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">52</td>
<td align="right">1.7%</td>
<td align="right">52</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">49</td>
<td align="right">1.6%</td>
<td align="right">49</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">8</td>
<td align="right">0.3%</td>
<td align="right">8</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
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
<td align="right">29</td>
<td align="right">100.0%</td>
<td align="right">29</td>
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
<td align="right">85,898</td>
<td align="right">3.2%</td>
<td align="right">79,500</td>
<td align="right">3.0%</td>
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
<td align="right">2,583,612</td>
<td align="right">96.8%</td>
<td align="right">2,583,612</td>
<td align="right">97.0%</td>
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
<td align="right">432</td>
<td align="right">55.9%</td>
<td align="right">426</td>
<td align="right">55.5%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">341</td>
<td align="right">44.1%</td>
<td align="right">341</td>
<td align="right">44.5%</td>
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
<td align="right">21</td>
<td align="right">4.9%</td>
<td align="right">15</td>
<td align="right">3.5%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">240</td>
<td align="right">55.6%</td>
<td align="right">240</td>
<td align="right">56.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">92</td>
<td align="right">21.3%</td>
<td align="right">92</td>
<td align="right">21.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">48</td>
<td align="right">11.1%</td>
<td align="right">48</td>
<td align="right">11.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">25</td>
<td align="right">5.8%</td>
<td align="right">25</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">6</td>
<td align="right">1.4%</td>
<td align="right">6</td>
<td align="right">1.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">40,224,998</td>
<td align="right">91.5%</td>
<td align="right">39,231,971</td>
<td align="right">91.4%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,120,909</td>
<td align="right">7.1%</td>
<td align="right">3,086,159</td>
<td align="right">7.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">608,231</td>
<td align="right">1.4%</td>
<td align="right">602,048</td>
<td align="right">1.4%</td>
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
<td align="right">66,056</td>
<td align="right">90.9%</td>
<td align="right">65,400</td>
<td align="right">90.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,623</td>
<td align="right">9.1%</td>
<td align="right">6,617</td>
<td align="right">9.2%</td>
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
<td align="left">other</td>
<td align="right">134</td>
<td align="right">2.0%</td>
<td align="right">129</td>
<td align="right">1.9%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">325</td>
<td align="right">4.9%</td>
<td align="right">324</td>
<td align="right">4.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">3,973</td>
<td align="right">60.0%</td>
<td align="right">3,973</td>
<td align="right">60.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">888</td>
<td align="right">13.4%</td>
<td align="right">888</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">664</td>
<td align="right">10.0%</td>
<td align="right">664</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">562</td>
<td align="right">8.5%</td>
<td align="right">562</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">50</td>
<td align="right">0.8%</td>
<td align="right">50</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">27</td>
<td align="right">0.4%</td>
<td align="right">27</td>
<td align="right">0.4%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">848,854</td>
<td align="right">9.8%</td>
<td align="right">25,238</td>
<td align="right">0.3%</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,813,889</td>
<td align="right">90.2%</td>
<td align="right">7,816,282</td>
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
<td align="left">Failure</td>
<td align="right">246</td>
<td align="right">23.7%</td>
<td align="right">168</td>
<td align="right">17.5%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">790</td>
<td align="right">76.3%</td>
<td align="right">790</td>
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
<td align="left">sequence</td>
<td align="right">222</td>
<td align="right">90.2%</td>
<td align="right">144</td>
<td align="right">85.7%</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">24</td>
<td align="right">9.8%</td>
<td align="right">24</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
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
<td align="right">47,365,021</td>
<td align="right">4.2%</td>
<td align="right">42,195,163</td>
<td align="right">4.0%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">395,947,597</td>
<td align="right">34.9%</td>
<td align="right">359,237,808</td>
<td align="right">34.2%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">645,501,008</td>
<td align="right">56.9%</td>
<td align="right">604,955,712</td>
<td align="right">57.5%</td>
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
<td align="right">45,687,507</td>
<td align="right">4.0%</td>
<td align="right">44,902,966</td>
<td align="right">4.3%</td>
<td align="right">-1.7%</td>
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
<td align="left">CONTAINS_OP</td>
<td align="right">2,471,802</td>
<td align="right">5.7%</td>
<td align="right">1,257,334</td>
<td align="right">3.3%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,679,866</td>
<td align="right">10.9%</td>
<td align="right">3,203,755</td>
<td align="right">8.4%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,677,652</td>
<td align="right">6.2%</td>
<td align="right">2,020,197</td>
<td align="right">5.3%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">999,468</td>
<td align="right">2.3%</td>
<td align="right">924,378</td>
<td align="right">2.4%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">14,040,203</td>
<td align="right">32.6%</td>
<td align="right">13,597,075</td>
<td align="right">35.7%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">608,231</td>
<td align="right">1.4%</td>
<td align="right">602,048</td>
<td align="right">1.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">7,611,898</td>
<td align="right">17.7%</td>
<td align="right">7,536,949</td>
<td align="right">19.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,378,083</td>
<td align="right">3.2%</td>
<td align="right">1,377,996</td>
<td align="right">3.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,491,901</td>
<td align="right">15.1%</td>
<td align="right">6,491,901</td>
<td align="right">17.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">848,854</td>
<td align="right">2.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">568,395</td>
<td align="right">1.5%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,317,205</td>
<td align="right">11.6%</td>
<td align="right">4,971,383</td>
<td align="right">11.1%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">6,496,056</td>
<td align="right">14.2%</td>
<td align="right">6,303,489</td>
<td align="right">14.0%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,155,650</td>
<td align="right">2.5%</td>
<td align="right">1,180,345</td>
<td align="right">2.6%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,781,235</td>
<td align="right">12.7%</td>
<td align="right">5,676,018</td>
<td align="right">12.6%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,711,617</td>
<td align="right">5.9%</td>
<td align="right">2,687,589</td>
<td align="right">6.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,216,577</td>
<td align="right">7.0%</td>
<td align="right">3,202,566</td>
<td align="right">7.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,003,449</td>
<td align="right">2.2%</td>
<td align="right">1,002,210</td>
<td align="right">2.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">16,088,104</td>
<td align="right">35.2%</td>
<td align="right">16,087,893</td>
<td align="right">35.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,728,685</td>
<td align="right">3.8%</td>
<td align="right">1,728,685</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">538,208</td>
<td align="right">1.2%</td>
<td align="right">538,208</td>
<td align="right">1.2%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">373,481</td>
<td align="right">0.5%</td>
<td align="right">373,484</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,126,110</td>
<td align="right">8.9%</td>
<td align="right">6,126,113</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,127,268</td>
<td align="right">8.9%</td>
<td align="right">6,127,271</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,123,816</td>
<td align="right">11.8%</td>
<td align="right">8,123,819</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,123,816</td>
<td align="right">11.8%</td>
<td align="right">8,123,819</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">47,694,518</td>
<td align="right">69.3%</td>
<td align="right">47,694,524</td>
<td align="right">69.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">60,670,704</td>
<td align="right">88.2%</td>
<td align="right">60,670,707</td>
<td align="right">88.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">1,996,548</td>
<td align="right">2.9%</td>
<td align="right">1,996,548</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">236</td>
<td align="right">0.0%</td>
<td align="right">236</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">922</td>
<td align="right">0.0%</td>
<td align="right">922</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">451,945</td>
<td align="right">0.7%</td>
<td align="right">451,945</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,127,460</td>
<td align="right">1.6%</td>
<td align="right">1,127,460</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">69</td>
<td align="right">0.0%</td>
<td align="right">69</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">870,816</td>
<td align="right">1.3%</td>
<td align="right">870,816</td>
<td align="right">1.3%</td>
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
<td align="right">233,528</td>
<td align="right"></td>
<td align="right">291,205</td>
<td align="right"></td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,709,485</td>
<td align="right"></td>
<td align="right">1,863,564</td>
<td align="right"></td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">265,069,592</td>
<td align="right">33.5%</td>
<td align="right">283,218,377</td>
<td align="right">35.9%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,478,049</td>
<td align="right"></td>
<td align="right">1,574,383</td>
<td align="right"></td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">354,316,693</td>
<td align="right">44.8%</td>
<td align="right">333,070,071</td>
<td align="right">42.2%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">260,518,039</td>
<td align="right">34.3%</td>
<td align="right">245,874,179</td>
<td align="right">32.3%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">284,053,810</td>
<td align="right">37.4%</td>
<td align="right">295,596,545</td>
<td align="right">38.9%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">312,978</td>
<td align="right">0.4%</td>
<td align="right">321,178</td>
<td align="right">0.4%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">176,447,946</td>
<td align="right">23.2%</td>
<td align="right">180,002,169</td>
<td align="right">23.7%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">39,418,641</td>
<td align="right">5.2%</td>
<td align="right">38,657,554</td>
<td align="right">5.1%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">26,666,856</td>
<td align="right">3.4%</td>
<td align="right">26,295,592</td>
<td align="right">3.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">38,302</td>
<td align="right">0.0%</td>
<td align="right">38,824</td>
<td align="right">0.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">144,062,844</td>
<td align="right">18.2%</td>
<td align="right">145,965,526</td>
<td align="right">18.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">54,659,600</td>
<td align="right"></td>
<td align="right">54,876,709</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">29,023,920</td>
<td align="right"></td>
<td align="right">28,976,215</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">47,221,088</td>
<td align="right">53.1%</td>
<td align="right">47,231,745</td>
<td align="right">53.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">45,826,848</td>
<td align="right"></td>
<td align="right">45,833,070</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">46,869,808</td>
<td align="right">52.7%</td>
<td align="right">46,871,743</td>
<td align="right">52.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">41,642,792</td>
<td align="right">46.9%</td>
<td align="right">41,643,888</td>
<td align="right">46.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">41,667,361</td>
<td align="right"></td>
<td align="right">41,668,457</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,098,567</td>
<td align="right"></td>
<td align="right">1,098,567</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">95,818</td>
<td align="right">8.7%</td>
<td align="right">95,818</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">4,842</td>
<td align="right">0.4%</td>
<td align="right">4,842</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="right">1,309</td>
<td align="right">26,808</td>
<td align="right">69,832,291</td>
<td align="right">10,184,603</td>
<td align="right">2,235,114</td>
<td align="right">1,310</td>
<td align="right">26,815</td>
<td align="right">70,564,033</td>
<td align="right">10,296,056</td>
<td align="right">2,227,539</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">43</td>
<td align="right">0.9%</td>
<td align="right">539</td>
<td align="right">1.9%</td>
<td align="right">1,153.5%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">21</td>
<td align="right">0.5%</td>
<td align="right">250</td>
<td align="right">0.9%</td>
<td align="right">1,090.5%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">10</td>
<td align="right">0.1%</td>
<td align="right">900.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">633</td>
<td align="right">13.6%</td>
<td align="right">6,022</td>
<td align="right">20.8%</td>
<td align="right">851.3%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">1,191</td>
<td align="right">25.7%</td>
<td align="right">11,188</td>
<td align="right">38.7%</td>
<td align="right">839.4%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">36</td>
<td align="right">0.8%</td>
<td align="right">285</td>
<td align="right">1.0%</td>
<td align="right">691.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">4,643</td>
<td align="right"></td>
<td align="right">28,893</td>
<td align="right"></td>
<td align="right">522.3%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">2,783</td>
<td align="right">59.9%</td>
<td align="right">11,398</td>
<td align="right">39.4%</td>
<td align="right">309.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">313,744,729</td>
<td align="right">2,466.3%</td>
<td align="right">515,921,242</td>
<td align="right">2,833.7%</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">12,721,180</td>
<td align="right"></td>
<td align="right">18,206,763</td>
<td align="right"></td>
<td align="right">43.1%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2 / 0 !!</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">1,191</td>
<td align="right"></td>
<td align="right">11,188</td>
<td align="right"></td>
<td align="right">839.4%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">1,167</td>
<td align="right">98.0%</td>
<td align="right">10,428</td>
<td align="right">93.2%</td>
<td align="right">793.6%</td>
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
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">86,016</td>
<td align="right">0.6%</td>
<td align="right">17,936,384</td>
<td align="right">17.3%</td>
<td align="right">20,752.4%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">2,723,366</td>
<td align="right">18.3%</td>
<td align="right">24,591,053</td>
<td align="right">23.7%</td>
<td align="right">803.0%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">313,968</td>
<td align="right">2.1%</td>
<td align="right">2,187,608</td>
<td align="right">2.1%</td>
<td align="right">596.8%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">14,921,728</td>
<td align="right"></td>
<td align="right">103,645,184</td>
<td align="right"></td>
<td align="right">594.6%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">11,884,394</td>
<td align="right">79.6%</td>
<td align="right">76,866,523</td>
<td align="right">74.2%</td>
<td align="right">546.8%</td>
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
<td align="left">53</td>
<td align="right">4.5%</td>
<td align="left">1,819</td>
<td align="right">17.4%</td>
<td align="right">3,332.1%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">518</td>
<td align="right">44.4%</td>
<td align="left">5,294</td>
<td align="right">50.8%</td>
<td align="right">922.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">426</td>
<td align="right">36.5%</td>
<td align="left">2,579</td>
<td align="right">24.7%</td>
<td align="right">505.4%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">148</td>
<td align="right">12.7%</td>
<td align="left">712</td>
<td align="right">6.8%</td>
<td align="right">381.1%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">22</td>
<td align="right">1.9%</td>
<td align="left">23</td>
<td align="right">0.2%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">1</td>
<td align="right">0.0%</td>
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
<td align="left"><= 8</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">442</td>
<td align="right">4.0%</td>
<td align="right">44,100.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">4</td>
<td align="right">0.3%</td>
<td align="right">456</td>
<td align="right">4.1%</td>
<td align="right">11,300.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">160</td>
<td align="right">13.4%</td>
<td align="right">2,094</td>
<td align="right">18.7%</td>
<td align="right">1,208.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">514</td>
<td align="right">43.2%</td>
<td align="right">4,887</td>
<td align="right">43.7%</td>
<td align="right">850.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">342</td>
<td align="right">28.7%</td>
<td align="right">2,479</td>
<td align="right">22.2%</td>
<td align="right">624.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">148</td>
<td align="right">12.4%</td>
<td align="right">720</td>
<td align="right">6.4%</td>
<td align="right">386.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">22</td>
<td align="right">1.8%</td>
<td align="right">107</td>
<td align="right">1.0%</td>
<td align="right">386.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">3</td>
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
<td align="left"><= 8</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">286</td>
<td align="right">2.6%</td>
<td align="right">14,200.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8</td>
<td align="right">0.7%</td>
<td align="right">1,251</td>
<td align="right">11.2%</td>
<td align="right">15,537.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">538</td>
<td align="right">45.2%</td>
<td align="right">4,839</td>
<td align="right">43.3%</td>
<td align="right">799.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">385</td>
<td align="right">32.3%</td>
<td align="right">2,795</td>
<td align="right">25.0%</td>
<td align="right">626.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">191</td>
<td align="right">16.0%</td>
<td align="right">890</td>
<td align="right">8.0%</td>
<td align="right">366.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">43</td>
<td align="right">3.6%</td>
<td align="right">109</td>
<td align="right">1.0%</td>
<td align="right">153.5%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">256</td>
<td align="right">2.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2</td>
<td align="right">0.0%</td>
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
<td align="left">_LOAD_FAST_2</td>
<td align="right">4,098</td>
<td align="right">133,841</td>
<td align="right">3,166.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">2,709</td>
<td align="right">85,241</td>
<td align="right">3,046.6%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">2,709</td>
<td align="right">85,011</td>
<td align="right">3,038.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">2,709</td>
<td align="right">84,844</td>
<td align="right">3,031.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,090</td>
<td align="right">159,245</td>
<td align="right">2,514.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,032</td>
<td align="right">92,676</td>
<td align="right">2,198.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">6,090</td>
<td align="right">80,725</td>
<td align="right">1,225.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">12,180</td>
<td align="right">140,767</td>
<td align="right">1,055.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">26,295</td>
<td align="right">291,859</td>
<td align="right">1,009.9%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">62</td>
<td align="right">594</td>
<td align="right">858.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">171,732</td>
<td align="right">1,288,043</td>
<td align="right">650.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">19,536</td>
<td align="right">137,789</td>
<td align="right">605.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">10,332</td>
<td align="right">68,266</td>
<td align="right">560.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">26,754</td>
<td align="right">167,108</td>
<td align="right">524.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">63,162</td>
<td align="right">284,381</td>
<td align="right">350.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">70,833</td>
<td align="right">310,052</td>
<td align="right">337.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">60,123</td>
<td align="right">255,674</td>
<td align="right">325.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">77,190</td>
<td align="right">320,010</td>
<td align="right">314.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">62,937</td>
<td align="right">260,680</td>
<td align="right">314.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">112,686</td>
<td align="right">466,637</td>
<td align="right">314.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">212,121</td>
<td align="right">862,443</td>
<td align="right">306.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">46,056</td>
<td align="right">186,091</td>
<td align="right">304.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">19,908</td>
<td align="right">77,991</td>
<td align="right">291.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">141,145</td>
<td align="right">542,494</td>
<td align="right">284.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">21,756</td>
<td align="right">82,375</td>
<td align="right">278.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">26,148</td>
<td align="right">97,933</td>
<td align="right">274.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">156,618</td>
<td align="right">585,159</td>
<td align="right">273.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right">135,828</td>
<td align="right">496,403</td>
<td align="right">265.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">135,828</td>
<td align="right">496,345</td>
<td align="right">265.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">663,285</td>
<td align="right">2,384,362</td>
<td align="right">259.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">30,141</td>
<td align="right">108,310</td>
<td align="right">259.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right">256,768</td>
<td align="right">889,728</td>
<td align="right">246.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">31,185</td>
<td align="right">106,278</td>
<td align="right">240.8%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">15,603</td>
<td align="right">53,152</td>
<td align="right">240.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">52,422</td>
<td align="right">177,863</td>
<td align="right">239.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,193,152</td>
<td align="right">3,957,148</td>
<td align="right">231.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">374,208</td>
<td align="right">1,222,973</td>
<td align="right">226.8%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">60,678</td>
<td align="right">191,913</td>
<td align="right">216.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">60,678</td>
<td align="right">191,913</td>
<td align="right">216.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">60,678</td>
<td align="right">191,913</td>
<td align="right">216.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">60,678</td>
<td align="right">191,912</td>
<td align="right">216.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">128,793</td>
<td align="right">406,455</td>
<td align="right">215.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">1,212,416</td>
<td align="right">211.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">631,344</td>
<td align="right">1,944,328</td>
<td align="right">208.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">60,678</td>
<td align="right">185,553</td>
<td align="right">205.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">207,135</td>
<td align="right">598,324</td>
<td align="right">188.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">63,042</td>
<td align="right">180,080</td>
<td align="right">185.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">116,233</td>
<td align="right">329,474</td>
<td align="right">183.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">28,167</td>
<td align="right">78,268</td>
<td align="right">177.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">63,042</td>
<td align="right">174,716</td>
<td align="right">177.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">33,075</td>
<td align="right">90,986</td>
<td align="right">175.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">2,058,841</td>
<td align="right">5,542,475</td>
<td align="right">169.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,857,597</td>
<td align="right">4,992,366</td>
<td align="right">168.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">32,886</td>
<td align="right">81,207</td>
<td align="right">146.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">679,742</td>
<td align="right">1,666,906</td>
<td align="right">145.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,125,400</td>
<td align="right">2,678,005</td>
<td align="right">138.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">519,759</td>
<td align="right">1,230,260</td>
<td align="right">136.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,171,400</td>
<td align="right">12,227,625</td>
<td align="right">136.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">615,174</td>
<td align="right">1,426,269</td>
<td align="right">131.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">926,083</td>
<td align="right">2,142,944</td>
<td align="right">131.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,577,348</td>
<td align="right">5,813,173</td>
<td align="right">125.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,058,355</td>
<td align="right">2,382,904</td>
<td align="right">125.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">825,756</td>
<td align="right">1,853,668</td>
<td align="right">124.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">6,363</td>
<td align="right">14,275</td>
<td align="right">124.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,334,498</td>
<td align="right">5,227,366</td>
<td align="right">123.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">858,411</td>
<td align="right">1,911,132</td>
<td align="right">122.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">242,775</td>
<td align="right">539,694</td>
<td align="right">122.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,773,199</td>
<td align="right">3,929,118</td>
<td align="right">121.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">509,124</td>
<td align="right">1,128,084</td>
<td align="right">121.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">1,613,197</td>
<td align="right">3,525,885</td>
<td align="right">118.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">614,733</td>
<td align="right">1,330,780</td>
<td align="right">116.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">702,261</td>
<td align="right">1,505,273</td>
<td align="right">114.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">828,892</td>
<td align="right">1,681,711</td>
<td align="right">102.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,548,760</td>
<td align="right">5,129,807</td>
<td align="right">101.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">17,556</td>
<td align="right">2</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">17,556</td>
<td align="right">3</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">8,631</td>
<td align="right">8</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">8,631</td>
<td align="right">8</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,833,809</td>
<td align="right">11,398,667</td>
<td align="right">95.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">2,686,783</td>
<td align="right">5,227,989</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">2,962,825</td>
<td align="right">5,707,365</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">427,850</td>
<td align="right">802,276</td>
<td align="right">87.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">342,240</td>
<td align="right">637,984</td>
<td align="right">86.4%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">8,259</td>
<td align="right">1,364</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,842,778</td>
<td align="right">3,319,763</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,738,349</td>
<td align="right">3,049,580</td>
<td align="right">75.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">902,292</td>
<td align="right">1,571,867</td>
<td align="right">74.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">50,307</td>
<td align="right">87,439</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_SLICE</td>
<td align="right">50,307</td>
<td align="right">87,439</td>
<td align="right">73.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">47,574,572</td>
<td align="right">81,236,918</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,184,463</td>
<td align="right">1,987,313</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">1,228,449</td>
<td align="right">2,027,838</td>
<td align="right">65.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">635,166</td>
<td align="right">1,033,580</td>
<td align="right">62.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">60,212,675</td>
<td align="right">97,465,572</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,002,412</td>
<td align="right">1,618,073</td>
<td align="right">61.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,477,210</td>
<td align="right">2,365,854</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,145,720</td>
<td align="right">11,385,809</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,207,290</td>
<td align="right">1,893,662</td>
<td align="right">56.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,948,671</td>
<td align="right">7,652,829</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,036,409</td>
<td align="right">487,832</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">320,778</td>
<td align="right">156,173</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">572,124</td>
<td align="right">863,293</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">13,143,385</td>
<td align="right">19,820,420</td>
<td align="right">50.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">401,957</td>
<td align="right">597,928</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,003,366</td>
<td align="right">8,862,574</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,003,366</td>
<td align="right">8,861,920</td>
<td align="right">47.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">17,669,851</td>
<td align="right">25,859,592</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">12,400,402</td>
<td align="right">18,050,344</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">12,721,180</td>
<td align="right">18,206,763</td>
<td align="right">43.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">300,090</td>
<td align="right">426,100</td>
<td align="right">42.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,954,572</td>
<td align="right">4,191,690</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">5,420,649</td>
<td align="right">7,667,739</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">746,517</td>
<td align="right">1,055,002</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">7,728</td>
<td align="right">10,905</td>
<td align="right">41.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">1,906,970</td>
<td align="right">2,635,987</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">3,876,595</td>
<td align="right">5,338,549</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">183,136</td>
<td align="right">249,054</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,271,814</td>
<td align="right">8,525,177</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">3,952,596</td>
<td align="right">5,344,085</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,952,596</td>
<td align="right">5,343,443</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">7,143,152</td>
<td align="right">9,562,099</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">3,530,466</td>
<td align="right">4,627,655</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">5,754</td>
<td align="right">7,460</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,119,875</td>
<td align="right">1,368,018</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">7,176,073</td>
<td align="right">8,674,468</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,436,665</td>
<td align="right">1,990,780</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,939,614</td>
<td align="right">4,634,900</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">2,995,297</td>
<td align="right">3,359,136</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">3,459,606</td>
<td align="right">3,833,807</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">1,726,893</td>
<td align="right">1,543,859</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right">7,728</td>
<td align="right">7,053</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,119,875</td>
<td align="right">1,124,586</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">9,702</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">8,778</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">6,363</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right"></td>
<td align="right">355,904</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right"></td>
<td align="right">87,653</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right"></td>
<td align="right">87,653</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right"></td>
<td align="right">67,896</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">57,267</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">49,791</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right">45,607</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">35,738</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">35,663</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right"></td>
<td align="right">35,663</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">35,663</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right"></td>
<td align="right">29,262</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">26,187</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right"></td>
<td align="right">24,473</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right"></td>
<td align="right">22,328</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right"></td>
<td align="right">18,334</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">14,788</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">12,817</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right"></td>
<td align="right">8,719</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">7,750</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_THIRD_NULL</td>
<td align="right"></td>
<td align="right">7,053</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right"></td>
<td align="right">6,906</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right"></td>
<td align="right">6,494</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right"></td>
<td align="right">6,398</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">4,640</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">2,326</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">2,290</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">2,290</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right"></td>
<td align="right">1,724</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right"></td>
<td align="right">1,435</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right"></td>
<td align="right">643</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right"></td>
<td align="right">642</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right"></td>
<td align="right">636</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">246</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LEN</td>
<td align="right"></td>
<td align="right">225</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right"></td>
<td align="right">136</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">130</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">130</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">116</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">87</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right"></td>
<td align="right">84</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">69</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">58</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right"></td>
<td align="right">34</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">9</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">4</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">2</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right"></td>
<td align="right">1</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right"></td>
<td align="right">1</td>
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
<td align="right">36</td>
<td align="right">370</td>
<td align="right">927.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">22</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right"></td>
<td align="right">13</td>
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
<td align="right">1</td>
<td align="right">7</td>
<td align="right">600.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1</td>
<td align="right">7</td>
<td align="right">600.0%</td>
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
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
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
<td align="right">12</td>
<td align="right">12</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-24
