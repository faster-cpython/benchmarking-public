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
<td align="left">RERAISE</td>
<td align="right">2,080</td>
<td align="right">41,393</td>
<td align="right">1,890.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">159,728,265</td>
<td align="right">434,192</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">3,428,882</td>
<td align="right">189,424</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,302,220</td>
<td align="right">76,340</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">22,329,562</td>
<td align="right">1,919,097</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">12,133,376</td>
<td align="right">1,340,231</td>
<td align="right">-89.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">29,478,226</td>
<td align="right">3,445,072</td>
<td align="right">-88.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,082,060</td>
<td align="right">244,881</td>
<td align="right">-88.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">23,690,098</td>
<td align="right">3,506,198</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">20,173,574</td>
<td align="right">3,312,372</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">62,897,185</td>
<td align="right">10,542,298</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">13,016,037</td>
<td align="right">2,450,564</td>
<td align="right">-81.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">519,600</td>
<td align="right">101,060</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">563,260</td>
<td align="right">117,080</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">891,160</td>
<td align="right">232,459</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">103,749,802</td>
<td align="right">27,184,486</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">10,415,023</td>
<td align="right">2,841,351</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">14,289,746</td>
<td align="right">4,081,669</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">34,836,820</td>
<td align="right">10,023,333</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">12,317,433</td>
<td align="right">3,638,829</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">6,188,737</td>
<td align="right">1,870,070</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">5,346,183</td>
<td align="right">1,679,030</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">14,340,707</td>
<td align="right">4,842,138</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">21,440,254</td>
<td align="right">7,414,530</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">60,705,494</td>
<td align="right">23,930,337</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">9,060,000</td>
<td align="right">3,615,267</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">103,696,682</td>
<td align="right">41,797,017</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">178,820</td>
<td align="right">72,160</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">4,939,358</td>
<td align="right">2,030,186</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">105,649,616</td>
<td align="right">44,715,980</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">39,866,757</td>
<td align="right">17,002,255</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">2,160</td>
<td align="right">940</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">29,602,994</td>
<td align="right">13,209,634</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">3,349,007</td>
<td align="right">1,515,229</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">46,967,944</td>
<td align="right">21,656,000</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,757,507</td>
<td align="right">840,826</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">191,533</td>
<td align="right">93,880</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">4,647,755</td>
<td align="right">2,352,364</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">100,229,547</td>
<td align="right">51,050,971</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">30,939,103</td>
<td align="right">16,321,531</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">6,680</td>
<td align="right">3,600</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">96,252,909</td>
<td align="right">51,945,467</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">43,493,174</td>
<td align="right">23,538,717</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,655,057</td>
<td align="right">1,450,186</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">359,824,567</td>
<td align="right">197,146,116</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">253,670,527</td>
<td align="right">140,707,881</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">47,745,470</td>
<td align="right">26,826,091</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">31,787,758</td>
<td align="right">18,576,503</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">38,568,686</td>
<td align="right">22,668,152</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">23,624,654</td>
<td align="right">13,978,371</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">56,988,268</td>
<td align="right">33,833,218</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">19,280</td>
<td align="right">11,480</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">91,893,210</td>
<td align="right">54,931,583</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">7,897,741</td>
<td align="right">4,746,266</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">1,277,818</td>
<td align="right">769,294</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">68,112,101</td>
<td align="right">41,094,425</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">978,091,295</td>
<td align="right">591,742,367</td>
<td align="right">-39.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,486,136</td>
<td align="right">1,518,450</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">68,465,940</td>
<td align="right">42,260,652</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">272,500,424</td>
<td align="right">168,592,845</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">23,272,362</td>
<td align="right">14,540,828</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">6,079,788</td>
<td align="right">3,850,216</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">146,061,544</td>
<td align="right">92,651,842</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">16,713,434</td>
<td align="right">10,624,375</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">192,011,843</td>
<td align="right">122,242,773</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">51,441,589</td>
<td align="right">32,967,521</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">99,466,002</td>
<td align="right">64,757,706</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">60,104,713</td>
<td align="right">39,215,106</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">30,204,807</td>
<td align="right">19,733,641</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">45,518,502</td>
<td align="right">30,656,797</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">33,956,464</td>
<td align="right">22,983,493</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">209,735</td>
<td align="right">142,511</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">258,126,615</td>
<td align="right">180,122,793</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">172,937,436</td>
<td align="right">121,615,029</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">234,426,746</td>
<td align="right">170,560,678</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">34,034,444</td>
<td align="right">24,831,045</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,875,298</td>
<td align="right">43,045,582</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">16,849,533</td>
<td align="right">12,328,564</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">19,820,271</td>
<td align="right">14,521,946</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">67,687,953</td>
<td align="right">49,711,115</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">22,497,414</td>
<td align="right">16,564,066</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">21,626,658</td>
<td align="right">16,054,772</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">159,264</td>
<td align="right">119,244</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">175,840</td>
<td align="right">139,180</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">5,980</td>
<td align="right">4,760</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">28,040,193</td>
<td align="right">22,355,193</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">35,502,191</td>
<td align="right">29,311,706</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">8,698,009</td>
<td align="right">7,231,045</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">24,015,849</td>
<td align="right">20,030,614</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,995,949</td>
<td align="right">5,045,967</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">74,840</td>
<td align="right">63,800</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,882,122</td>
<td align="right">5,027,429</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">613,454</td>
<td align="right">530,706</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,537,477</td>
<td align="right">3,095,562</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">6,046,102</td>
<td align="right">5,333,882</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">28,283,144</td>
<td align="right">25,266,570</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">9,151,141</td>
<td align="right">8,206,807</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">14,676,053</td>
<td align="right">13,187,815</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,996,384</td>
<td align="right">8,135,739</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">61,441,972</td>
<td align="right">55,892,422</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">5,307,694</td>
<td align="right">4,847,012</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">180,088</td>
<td align="right">165,203</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,283,382</td>
<td align="right">2,098,305</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">22,970,488</td>
<td align="right">21,352,869</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,771,453</td>
<td align="right">2,582,390</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">20,344,619</td>
<td align="right">19,021,273</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">569,074</td>
<td align="right">532,765</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,372,377</td>
<td align="right">8,958,396</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">57,272,144</td>
<td align="right">54,922,680</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,955,062</td>
<td align="right">8,607,991</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">9,769,336</td>
<td align="right">9,430,479</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,759,790</td>
<td align="right">7,491,122</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,349,330</td>
<td align="right">1,388,295</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,630,623</td>
<td align="right">1,592,093</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">888,204</td>
<td align="right">867,370</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,690,462</td>
<td align="right">2,628,009</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">419,101</td>
<td align="right">411,790</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,814,130</td>
<td align="right">1,784,196</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">540,400</td>
<td align="right">532,240</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">19,500</td>
<td align="right">19,260</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">50,525</td>
<td align="right">49,997</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">5,766,707</td>
<td align="right">5,719,510</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">141,900</td>
<td align="right">140,940</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">284,480</td>
<td align="right">282,560</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">284,520</td>
<td align="right">282,600</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,585,510</td>
<td align="right">12,656,052</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">39,854</td>
<td align="right">39,676</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">126,610,557</td>
<td align="right">126,130,288</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,578,351</td>
<td align="right">1,572,567</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">228,350</td>
<td align="right">227,611</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">22,568</td>
<td align="right">22,510</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,121,362</td>
<td align="right">1,118,638</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,932,128</td>
<td align="right">22,980,074</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">178,414,290</td>
<td align="right">178,043,952</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,029,820</td>
<td align="right">1,028,520</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">1,203</td>
<td align="right">1,204</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">907,076</td>
<td align="right">906,533</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">907,076</td>
<td align="right">906,533</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">907,076</td>
<td align="right">906,533</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">119,126</td>
<td align="right">119,058</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">4,006</td>
<td align="right">4,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">47,561</td>
<td align="right">47,548</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,349,370</td>
<td align="right">1,349,022</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">181,880</td>
<td align="right">181,848</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,766</td>
<td align="right">12,768</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">887,868</td>
<td align="right">887,770</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,182,033</td>
<td align="right">1,181,915</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">210,360</td>
<td align="right">210,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">262,603</td>
<td align="right">262,586</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">543,683</td>
<td align="right">543,653</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">28,013,501</td>
<td align="right">28,012,216</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">519,360</td>
<td align="right">519,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">442,840</td>
<td align="right">442,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">233,080</td>
<td align="right">233,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">3,100</td>
<td align="right">3,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">2,660</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,540</td>
<td align="right">2,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,040</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,840</td>
<td align="right">1,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">117,210,149</td>
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
<td align="right">35,444,323</td>
<td align="right">65.2%</td>
<td align="right">29,256,771</td>
<td align="right">60.8%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,839,646</td>
<td align="right">34.7%</td>
<td align="right">18,838,107</td>
<td align="right">39.1%</td>
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
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">120</td>
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
<td align="right">51,146</td>
<td align="right">88.4%</td>
<td align="right">48,231</td>
<td align="right">87.8%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,722</td>
<td align="right">11.6%</td>
<td align="right">6,704</td>
<td align="right">12.2%</td>
<td align="right">-0.3%</td>
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
<td align="left">true divide float</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,820</td>
<td align="right">13.3%</td>
<td align="right">5,840</td>
<td align="right">12.1%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">1,272</td>
<td align="right">2.5%</td>
<td align="right">1,108</td>
<td align="right">2.3%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,360</td>
<td align="right">4.6%</td>
<td align="right">2,120</td>
<td align="right">4.4%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">2,273</td>
<td align="right">4.4%</td>
<td align="right">2,051</td>
<td align="right">4.3%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">7,463</td>
<td align="right">14.6%</td>
<td align="right">6,742</td>
<td align="right">14.0%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,958</td>
<td align="right">3.8%</td>
<td align="right">1,817</td>
<td align="right">3.8%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,448</td>
<td align="right">18.5%</td>
<td align="right">9,144</td>
<td align="right">19.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,965</td>
<td align="right">7.8%</td>
<td align="right">3,841</td>
<td align="right">8.0%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">223</td>
<td align="right">0.4%</td>
<td align="right">226</td>
<td align="right">0.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,194</td>
<td align="right">2.3%</td>
<td align="right">1,183</td>
<td align="right">2.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,861</td>
<td align="right">5.6%</td>
<td align="right">2,854</td>
<td align="right">5.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">583</td>
<td align="right">1.1%</td>
<td align="right">582</td>
<td align="right">1.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,522</td>
<td align="right">4.9%</td>
<td align="right">2,521</td>
<td align="right">5.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,825</td>
<td align="right">7.5%</td>
<td align="right">3,824</td>
<td align="right">7.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,700</td>
<td align="right">7.2%</td>
<td align="right">3,700</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">376</td>
<td align="right">0.7%</td>
<td align="right">376</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">300</td>
<td align="right">0.6%</td>
<td align="right">300</td>
<td align="right">0.6%</td>
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
<td align="right">569,074</td>
<td align="right">100.0%</td>
<td align="right">532,765</td>
<td align="right">100.0%</td>
<td align="right">-6.4%</td>
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
<td align="right">23,665,026</td>
<td align="right">35.6%</td>
<td align="right">3,488,392</td>
<td align="right">7.5%</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">45,573</td>
<td align="right">0.1%</td>
<td align="right">14,927</td>
<td align="right">0.0%</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">42,683,389</td>
<td align="right">64.3%</td>
<td align="right">42,687,035</td>
<td align="right">92.4%</td>
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
<td align="right">17,517</td>
<td align="right">67.7%</td>
<td align="right">10,334</td>
<td align="right">57.3%</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">8,355</td>
<td align="right">32.3%</td>
<td align="right">7,712</td>
<td align="right">42.7%</td>
<td align="right">-7.7%</td>
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
<td align="right">3,640</td>
<td align="right">20.8%</td>
<td align="right">1,960</td>
<td align="right">19.0%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,094</td>
<td align="right">69.0%</td>
<td align="right">7,152</td>
<td align="right">69.2%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">1,760</td>
<td align="right">10.0%</td>
<td align="right">1,200</td>
<td align="right">11.6%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">20</td>
<td align="right">0.1%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">31,040</td>
<td align="right">0.0%</td>
<td align="right">21,800</td>
<td align="right">0.0%</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">31,453,573</td>
<td align="right">7.6%</td>
<td align="right">29,752,479</td>
<td align="right">7.2%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">383,236,211</td>
<td align="right">92.4%</td>
<td align="right">385,078,464</td>
<td align="right">92.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">167,549</td>
<td align="right">0.0%</td>
<td align="right">167,508</td>
<td align="right">0.0%</td>
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
<td align="right">691,947</td>
<td align="right">100.0%</td>
<td align="right">659,957</td>
<td align="right">100.0%</td>
<td align="right">-4.6%</td>
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
<td align="left">init not inline values</td>
<td align="right">260</td>
<td align="right">260 / 0 !!</td>
<td align="right">260</td>
<td align="right">260 / 0 !!</td>
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
<td align="right">7,986</td>
<td align="right">48.9%</td>
<td align="right">7,984</td>
<td align="right">48.8%</td>
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
<td align="right">3,580</td>
<td align="right">21.9%</td>
<td align="right">3,580</td>
<td align="right">21.9%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">38,488,372</td>
<td align="right">36.6%</td>
<td align="right">22,595,428</td>
<td align="right">25.3%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">553,430</td>
<td align="right">0.5%</td>
<td align="right">465,611</td>
<td align="right">0.5%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">66,107,895</td>
<td align="right">62.8%</td>
<td align="right">66,066,997</td>
<td align="right">74.1%</td>
<td align="right">-0.1%</td>
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
<td align="right">70,671</td>
<td align="right">78.1%</td>
<td align="right">63,096</td>
<td align="right">77.6%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">19,863</td>
<td align="right">21.9%</td>
<td align="right">18,208</td>
<td align="right">22.4%</td>
<td align="right">-8.3%</td>
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
<td align="left">bool</td>
<td align="right">2,074</td>
<td align="right">2.9%</td>
<td align="right">417</td>
<td align="right">0.7%</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">19,491</td>
<td align="right">27.6%</td>
<td align="right">16,225</td>
<td align="right">25.7%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,302</td>
<td align="right">21.7%</td>
<td align="right">12,862</td>
<td align="right">20.4%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,042</td>
<td align="right">14.2%</td>
<td align="right">9,920</td>
<td align="right">15.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">12,242</td>
<td align="right">17.3%</td>
<td align="right">12,152</td>
<td align="right">19.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,320</td>
<td align="right">14.6%</td>
<td align="right">10,320</td>
<td align="right">16.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">220</td>
<td align="right">0.3%</td>
<td align="right">220</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
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
<td align="right">22,313,103</td>
<td align="right">42.9%</td>
<td align="right">1,907,965</td>
<td align="right">6.0%</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,686,761</td>
<td align="right">57.1%</td>
<td align="right">29,686,108</td>
<td align="right">93.9%</td>
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
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">1,200</td>
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
<td align="right">15,219</td>
<td align="right">92.5%</td>
<td align="right">9,892</td>
<td align="right">88.9%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,240</td>
<td align="right">7.5%</td>
<td align="right">1,240</td>
<td align="right">11.1%</td>
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
<td align="right">8,161</td>
<td align="right">53.6%</td>
<td align="right">3,556</td>
<td align="right">35.9%</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,180</td>
<td align="right">7.8%</td>
<td align="right">940</td>
<td align="right">9.5%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">5,578</td>
<td align="right">36.7%</td>
<td align="right">5,116</td>
<td align="right">51.7%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">300</td>
<td align="right">2.0%</td>
<td align="right">280</td>
<td align="right">2.8%</td>
<td align="right">-6.7%</td>
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
<td align="right">1,566,433</td>
<td align="right">0.7%</td>
<td align="right">113,433</td>
<td align="right">0.2%</td>
<td align="right">-92.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">108,492,481</td>
<td align="right">50.7%</td>
<td align="right">21,983,757</td>
<td align="right">44.6%</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">103,640,398</td>
<td align="right">48.5%</td>
<td align="right">27,137,773</td>
<td align="right">55.1%</td>
<td align="right">-73.8%</td>
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
<td align="right">41,428</td>
<td align="right">29.8%</td>
<td align="right">14,019</td>
<td align="right">28.8%</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97,383</td>
<td align="right">70.2%</td>
<td align="right">34,705</td>
<td align="right">71.2%</td>
<td align="right">-64.4%</td>
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
<td align="left">dict items</td>
<td align="right">69,272</td>
<td align="right">71.1%</td>
<td align="right">16,378</td>
<td align="right">47.2%</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">8,958</td>
<td align="right">9.2%</td>
<td align="right">4,005</td>
<td align="right">11.5%</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,600</td>
<td align="right">7.8%</td>
<td align="right">4,720</td>
<td align="right">13.6%</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,720</td>
<td align="right">2.8%</td>
<td align="right">1,960</td>
<td align="right">5.6%</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,233</td>
<td align="right">4.3%</td>
<td align="right">3,462</td>
<td align="right">10.0%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,640</td>
<td align="right">1.7%</td>
<td align="right">1,400</td>
<td align="right">4.0%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">860</td>
<td align="right">0.9%</td>
<td align="right">780</td>
<td align="right">2.2%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,940</td>
<td align="right">2.0%</td>
<td align="right">1,840</td>
<td align="right">5.3%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
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
<td align="right">67,650,332</td>
<td align="right">15.4%</td>
<td align="right">33,216,584</td>
<td align="right">8.6%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">99,238,311</td>
<td align="right">22.5%</td>
<td align="right">64,542,646</td>
<td align="right">16.8%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">273,015,557</td>
<td align="right">62.0%</td>
<td align="right">286,581,839</td>
<td align="right">74.5%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,500</td>
<td align="right">0.0%</td>
<td align="right">22,500</td>
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
<td align="right">1,361,082</td>
<td align="right">91.1%</td>
<td align="right">710,878</td>
<td align="right">85.4%</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">133,574</td>
<td align="right">8.9%</td>
<td align="right">121,886</td>
<td align="right">14.6%</td>
<td align="right">-8.8%</td>
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
<td align="left">module attr not found</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">560</td>
<td align="right">0.4%</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,340</td>
<td align="right">1.0%</td>
<td align="right">880</td>
<td align="right">0.7%</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">10,462</td>
<td align="right">7.8%</td>
<td align="right">7,743</td>
<td align="right">6.4%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">11,116</td>
<td align="right">8.3%</td>
<td align="right">9,262</td>
<td align="right">7.6%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">16,520</td>
<td align="right">12.4%</td>
<td align="right">14,880</td>
<td align="right">12.2%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">5,260</td>
<td align="right">3.9%</td>
<td align="right">4,800</td>
<td align="right">3.9%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">12,529</td>
<td align="right">9.4%</td>
<td align="right">11,714</td>
<td align="right">9.6%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">62,733</td>
<td align="right">47.0%</td>
<td align="right">59,460</td>
<td align="right">48.8%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,034</td>
<td align="right">6.8%</td>
<td align="right">8,907</td>
<td align="right">7.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">120</td>
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
<td align="right">380,467,910</td>
<td align="right">99.9%</td>
<td align="right">265,086,714</td>
<td align="right">99.9%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">90,077</td>
<td align="right">0.0%</td>
<td align="right">90,019</td>
<td align="right">0.0%</td>
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
<td align="right">20,380</td>
<td align="right">0.0%</td>
<td align="right">20,380</td>
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
<td align="right">91,963</td>
<td align="right">100.0%</td>
<td align="right">91,989</td>
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
<td align="right">603</td>
<td align="right">0.0%</td>
<td align="right">604</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,996,163</td>
<td align="right">100.0%</td>
<td align="right">2,996,031</td>
<td align="right">100.0%</td>
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
<td align="right">600</td>
<td align="right">100.0%</td>
<td align="right">600</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">30,660</td>
<td align="right">2.1%</td>
<td align="right">30,640</td>
<td align="right">2.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">439,720</td>
<td align="right">29.9%</td>
<td align="right">439,720</td>
<td align="right">29.9%</td>
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
<td align="right">999,160</td>
<td align="right">67.8%</td>
<td align="right">999,160</td>
<td align="right">67.8%</td>
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
<td align="right">3,080</td>
<td align="right">83.2%</td>
<td align="right">3,060</td>
<td align="right">83.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">620</td>
<td align="right">16.8%</td>
<td align="right">620</td>
<td align="right">16.8%</td>
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
<td align="right">3,080</td>
<td align="right">100.0%</td>
<td align="right">3,060</td>
<td align="right">100.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">2,216,189</td>
<td align="right">17.0%</td>
<td align="right">426,066</td>
<td align="right">3.5%</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,381,288</td>
<td align="right">79.8%</td>
<td align="right">11,175,418</td>
<td align="right">93.0%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">410,295</td>
<td align="right">3.2%</td>
<td align="right">402,986</td>
<td align="right">3.4%</td>
<td align="right">-1.8%</td>
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
<td align="right">46,772</td>
<td align="right">92.7%</td>
<td align="right">12,972</td>
<td align="right">77.8%</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,706</td>
<td align="right">7.3%</td>
<td align="right">3,704</td>
<td align="right">22.2%</td>
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
<td align="left">not managed dict</td>
<td align="right">1,446</td>
<td align="right">39.0%</td>
<td align="right">1,444</td>
<td align="right">39.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,960</td>
<td align="right">52.9%</td>
<td align="right">1,960</td>
<td align="right">52.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">240</td>
<td align="right">6.5%</td>
<td align="right">240</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">60</td>
<td align="right">1.6%</td>
<td align="right">60</td>
<td align="right">1.6%</td>
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
<td align="right">2,160</td>
<td align="right">100.0%</td>
<td align="right">940</td>
<td align="right">100.0%</td>
<td align="right">-56.5%</td>
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
<td align="right">3,422,522</td>
<td align="right">13.1%</td>
<td align="right">183,867</td>
<td align="right">0.8%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">22,628,001</td>
<td align="right">86.8%</td>
<td align="right">22,622,056</td>
<td align="right">99.2%</td>
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
<td align="right">3,640</td>
<td align="right">57.2%</td>
<td align="right">2,833</td>
<td align="right">51.0%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,720</td>
<td align="right">42.8%</td>
<td align="right">2,724</td>
<td align="right">49.0%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">3,640</td>
<td align="right">100.0%</td>
<td align="right">2,833</td>
<td align="right">100.0%</td>
<td align="right">-22.2%</td>
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
<td align="right">792,593</td>
<td align="right">0.4%</td>
<td align="right">440,011</td>
<td align="right">0.2%</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">197,912,991</td>
<td align="right">93.7%</td>
<td align="right">196,679,803</td>
<td align="right">93.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,503,618</td>
<td align="right">5.9%</td>
<td align="right">12,580,670</td>
<td align="right">6.0%</td>
<td align="right">0.6%</td>
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
<td align="right">29,261</td>
<td align="right">30.6%</td>
<td align="right">22,756</td>
<td align="right">27.6%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">66,363</td>
<td align="right">69.4%</td>
<td align="right">59,738</td>
<td align="right">72.4%</td>
<td align="right">-10.0%</td>
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
<td align="right">3,731</td>
<td align="right">12.8%</td>
<td align="right">1,634</td>
<td align="right">7.2%</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">14,948</td>
<td align="right">51.1%</td>
<td align="right">10,793</td>
<td align="right">47.4%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,340</td>
<td align="right">8.0%</td>
<td align="right">2,080</td>
<td align="right">9.1%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,434</td>
<td align="right">4.9%</td>
<td align="right">1,440</td>
<td align="right">6.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">3,508</td>
<td align="right">12.0%</td>
<td align="right">3,509</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">3,260</td>
<td align="right">11.1%</td>
<td align="right">3,260</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.2%</td>
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
<td align="right">27,694</td>
<td align="right">0.0%</td>
<td align="right">27,516</td>
<td align="right">0.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">105,507,393</td>
<td align="right">100.0%</td>
<td align="right">105,735,096</td>
<td align="right">100.0%</td>
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
<td align="right">11,384</td>
<td align="right">93.6%</td>
<td align="right">11,384</td>
<td align="right">93.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">776</td>
<td align="right">6.4%</td>
<td align="right">776</td>
<td align="right">6.4%</td>
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
<td align="right">716</td>
<td align="right">92.3%</td>
<td align="right">716</td>
<td align="right">92.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">60</td>
<td align="right">7.7%</td>
<td align="right">60</td>
<td align="right">7.7%</td>
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
<td align="right">341,252,214</td>
<td align="right">5.7%</td>
<td align="right">164,079,238</td>
<td align="right">4.4%</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">104,334,063</td>
<td align="right">1.8%</td>
<td align="right">64,485,031</td>
<td align="right">1.7%</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,916,933,964</td>
<td align="right">32.2%</td>
<td align="right">1,194,492,695</td>
<td align="right">32.0%</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">3,597,748,963</td>
<td align="right">60.4%</td>
<td align="right">2,311,199,631</td>
<td align="right">61.9%</td>
<td align="right">-35.8%</td>
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
<td align="right">22,313,103</td>
<td align="right">6.6%</td>
<td align="right">1,907,965</td>
<td align="right">1.2%</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">23,665,026</td>
<td align="right">7.0%</td>
<td align="right">3,488,392</td>
<td align="right">2.1%</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">103,640,398</td>
<td align="right">30.4%</td>
<td align="right">27,137,773</td>
<td align="right">16.6%</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">38,488,372</td>
<td align="right">11.3%</td>
<td align="right">22,595,428</td>
<td align="right">13.8%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">99,238,311</td>
<td align="right">29.2%</td>
<td align="right">64,542,646</td>
<td align="right">39.5%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">35,444,323</td>
<td align="right">10.4%</td>
<td align="right">29,256,771</td>
<td align="right">17.9%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">569,074</td>
<td align="right">0.2%</td>
<td align="right">532,765</td>
<td align="right">0.3%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,503,618</td>
<td align="right">3.7%</td>
<td align="right">12,580,670</td>
<td align="right">7.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">3,422,522</td>
<td align="right">1.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">439,720</td>
<td align="right">0.1%</td>
<td align="right">439,720</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">402,986</td>
<td align="right">0.2%</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,215,209</td>
<td align="right">2.1%</td>
<td align="right">425,086</td>
<td align="right">0.7%</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">36,662,046</td>
<td align="right">35.1%</td>
<td align="right">14,012,773</td>
<td align="right">21.7%</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">17,010,580</td>
<td align="right">16.3%</td>
<td align="right">9,548,850</td>
<td align="right">14.8%</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,237,306</td>
<td align="right">8.9%</td>
<td align="right">5,407,697</td>
<td align="right">8.4%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">7,802,621</td>
<td align="right">7.5%</td>
<td align="right">6,162,961</td>
<td align="right">9.6%</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">4,127,213</td>
<td align="right">4.0%</td>
<td align="right">3,669,067</td>
<td align="right">5.7%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">14,297,952</td>
<td align="right">13.7%</td>
<td align="right">14,347,924</td>
<td align="right">22.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,661,192</td>
<td align="right">2.6%</td>
<td align="right">2,661,158</td>
<td align="right">4.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">6,512,255</td>
<td align="right">6.2%</td>
<td align="right">6,512,226</td>
<td align="right">10.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">794,321</td>
<td align="right">0.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">464,011</td>
<td align="right">0.7%</td>
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
<td align="left">Frame objects created</td>
<td align="right">1,287,652</td>
<td align="right">0.5%</td>
<td align="right">1,365,894</td>
<td align="right">0.5%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">53,332,186</td>
<td align="right">19.6%</td>
<td align="right">52,805,850</td>
<td align="right">19.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">97,778,297</td>
<td align="right">35.9%</td>
<td align="right">97,250,340</td>
<td align="right">35.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">97,785,597</td>
<td align="right">35.9%</td>
<td align="right">97,257,640</td>
<td align="right">35.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">145,700,736</td>
<td align="right">53.5%</td>
<td align="right">146,406,320</td>
<td align="right">53.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">126,814,147</td>
<td align="right">46.5%</td>
<td align="right">126,373,185</td>
<td align="right">46.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">126,814,147</td>
<td align="right">46.5%</td>
<td align="right">126,373,185</td>
<td align="right">46.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">29,028,550</td>
<td align="right">10.7%</td>
<td align="right">29,115,545</td>
<td align="right">10.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">243,169,868</td>
<td align="right">89.2%</td>
<td align="right">243,347,602</td>
<td align="right">89.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">23,783,785</td>
<td align="right">8.7%</td>
<td align="right">23,782,907</td>
<td align="right">8.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">11,825,054</td>
<td align="right">4.3%</td>
<td align="right">11,824,676</td>
<td align="right">4.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">6,960</td>
<td align="right">0.0%</td>
<td align="right">6,960</td>
<td align="right">0.0%</td>
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
<td align="left">Increfs</td>
<td align="right">1,417,000,129</td>
<td align="right">35.6%</td>
<td align="right">2,666,038,816</td>
<td align="right">59.8%</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">4,386,941</td>
<td align="right"></td>
<td align="right">1,105,296</td>
<td align="right"></td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">1,587,480,208</td>
<td align="right">34.8%</td>
<td align="right">2,755,887,217</td>
<td align="right">54.8%</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">11,084,012</td>
<td align="right"></td>
<td align="right">4,916,194</td>
<td align="right"></td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">6,700,726</td>
<td align="right"></td>
<td align="right">3,814,872</td>
<td align="right"></td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">2,564,448,033</td>
<td align="right">64.4%</td>
<td align="right">1,790,531,295</td>
<td align="right">40.2%</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">2,968,282,189</td>
<td align="right">65.2%</td>
<td align="right">2,275,196,533</td>
<td align="right">45.2%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">200,935,505</td>
<td align="right"></td>
<td align="right">193,514,842</td>
<td align="right"></td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,035,245</td>
<td align="right">0.2%</td>
<td align="right">1,065,497</td>
<td align="right">0.2%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">339,008,762</td>
<td align="right"></td>
<td align="right">337,716,714</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">292,769,235</td>
<td align="right">44.5%</td>
<td align="right">292,972,230</td>
<td align="right">44.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">291,709,530</td>
<td align="right">44.4%</td>
<td align="right">291,882,273</td>
<td align="right">44.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">306,720,426</td>
<td align="right"></td>
<td align="right">306,897,550</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,393,080</td>
<td align="right"></td>
<td align="right">1,392,810</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">364,506,701</td>
<td align="right">55.5%</td>
<td align="right">364,539,796</td>
<td align="right">55.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">364,745,776</td>
<td align="right"></td>
<td align="right">364,778,873</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">24,460</td>
<td align="right">0.0%</td>
<td align="right">24,460</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
<td align="right">80</td>
<td align="right">80 / 0 !!</td>
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
<td align="right">80</td>
<td align="right">80 / 0 !!</td>
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
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-09-22
