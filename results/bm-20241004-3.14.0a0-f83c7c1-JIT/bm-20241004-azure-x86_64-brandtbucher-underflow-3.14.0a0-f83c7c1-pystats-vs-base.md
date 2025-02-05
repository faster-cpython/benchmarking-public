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
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">339,879,307</td>
<td align="right">9,233,048</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">43,587,006</td>
<td align="right">1,772,674</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">44,137,572</td>
<td align="right">2,245,047</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">60,910,078</td>
<td align="right">3,946,828</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">311,379,156</td>
<td align="right">29,876,682</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,327,546</td>
<td align="right">1,045,746</td>
<td align="right">-88.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">275,514,451</td>
<td align="right">38,524,344</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,590,497</td>
<td align="right">723,234</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">123,634,745</td>
<td align="right">22,522,551</td>
<td align="right">-81.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,546,413</td>
<td align="right">18,652,720</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">303,913,683</td>
<td align="right">66,568,683</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">90,742,950</td>
<td align="right">22,878,279</td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">43,741,382</td>
<td align="right">11,160,290</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">56,295,333</td>
<td align="right">15,558,519</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">62,350,154</td>
<td align="right">18,467,033</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">53,307,448</td>
<td align="right">16,379,042</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">747,626,944</td>
<td align="right">231,345,059</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">184,889,905</td>
<td align="right">60,646,915</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,596,738</td>
<td align="right">46,511,375</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">439,223,347</td>
<td align="right">152,853,392</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">221,078,450</td>
<td align="right">77,144,370</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">126,367,789</td>
<td align="right">45,121,140</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">198,193,887</td>
<td align="right">71,382,155</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,383,522</td>
<td align="right">29,758,955</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">82,436,604</td>
<td align="right">30,808,076</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,363,378</td>
<td align="right">17,907,887</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">108,218,350</td>
<td align="right">41,322,697</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">49,919,211</td>
<td align="right">19,685,674</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">100,382,731</td>
<td align="right">39,740,181</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">150,314,300</td>
<td align="right">59,581,566</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">12,297,643</td>
<td align="right">4,923,503</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">240,970,305</td>
<td align="right">97,688,541</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">104,183,851</td>
<td align="right">45,325,660</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,942,262</td>
<td align="right">1,281,645</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">257,510,335</td>
<td align="right">121,276,770</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">186,114,597</td>
<td align="right">88,707,470</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">125,514,214</td>
<td align="right">60,962,196</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,517,374</td>
<td align="right">11,059,549</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">31,693,577</td>
<td align="right">15,767,555</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">537,308,876</td>
<td align="right">268,484,491</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">275,677,858</td>
<td align="right">138,674,411</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">475,035,583</td>
<td align="right">240,813,942</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">190,889,780</td>
<td align="right">97,387,118</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">102,005,980</td>
<td align="right">52,890,817</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,677,742,515</td>
<td align="right">1,951,928,938</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">234,600,416</td>
<td align="right">126,725,000</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">772,839,830</td>
<td align="right">421,192,546</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,683,167,292</td>
<td align="right">2,562,257,978</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,335,943</td>
<td align="right">5,668,523</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">53,669,742</td>
<td align="right">29,508,243</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">433,945,804</td>
<td align="right">239,394,939</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">62,328,675</td>
<td align="right">34,621,789</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">200,061,818</td>
<td align="right">112,471,246</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,772,728,950</td>
<td align="right">2,128,677,597</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,629,211,053</td>
<td align="right">1,513,124,514</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,732,242,762</td>
<td align="right">2,148,297,682</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">239,398</td>
<td align="right">137,957</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">77,534,467</td>
<td align="right">44,887,237</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,371,275,632</td>
<td align="right">798,756,902</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">29,436,793</td>
<td align="right">17,214,318</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">204,114,228</td>
<td align="right">121,726,030</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">87,690,412</td>
<td align="right">52,550,906</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,043,806</td>
<td align="right">21,364,175</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">42,562,886</td>
<td align="right">59,123,972</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,434,984,571</td>
<td align="right">2,717,677,239</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">348,913,662</td>
<td align="right">216,821,115</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,254,402</td>
<td align="right">37,411,091</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,692,740,812</td>
<td align="right">1,087,253,574</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,975,811,426</td>
<td align="right">10,294,330,236</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,771,413</td>
<td align="right">2,445,299</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,641,371,220</td>
<td align="right">1,728,739,359</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">365,915,427</td>
<td align="right">240,173,654</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,996,337,344</td>
<td align="right">1,314,256,957</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,579,836</td>
<td align="right">25,046,223</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,832,402,116</td>
<td align="right">1,225,373,728</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">548,511,254</td>
<td align="right">370,615,312</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">487,327,685</td>
<td align="right">330,458,285</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">385,069,104</td>
<td align="right">263,652,270</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">139,853,967</td>
<td align="right">96,505,552</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,535,845</td>
<td align="right">6,608,792</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">198,953,040</td>
<td align="right">138,687,240</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">93,490,876</td>
<td align="right">65,342,363</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">100,204,594</td>
<td align="right">70,422,745</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">138,732,062</td>
<td align="right">99,340,634</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">162,652,553</td>
<td align="right">116,526,965</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">29,521,503</td>
<td align="right">21,208,802</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,387,000,256</td>
<td align="right">1,720,798,890</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">768,328,600</td>
<td align="right">555,878,803</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,693,851</td>
<td align="right">2,678,067</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,250,338,596</td>
<td align="right">1,646,872,829</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">159,508,586</td>
<td align="right">116,970,565</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">458,340,905</td>
<td align="right">336,977,978</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">967,949,947</td>
<td align="right">717,936,067</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">552,420</td>
<td align="right">410,720</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">826,895,963</td>
<td align="right">618,366,818</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">199,534,928</td>
<td align="right">150,195,730</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">11,000,608</td>
<td align="right">8,421,196</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">96,260</td>
<td align="right">73,971</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">33,275,624</td>
<td align="right">25,594,373</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,364,606,842</td>
<td align="right">1,051,524,686</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">92,233,942</td>
<td align="right">71,838,686</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">580,652,625</td>
<td align="right">454,730,627</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">355,805,073</td>
<td align="right">278,650,509</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,454,202</td>
<td align="right">27,876,268</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">53,413,457</td>
<td align="right">42,133,615</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">58,070,285</td>
<td align="right">45,900,715</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">268,617,374</td>
<td align="right">212,844,146</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">588,341,780</td>
<td align="right">466,996,320</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">620,653,015</td>
<td align="right">496,584,426</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,890,132,456</td>
<td align="right">2,321,928,583</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">101,022,119</td>
<td align="right">82,350,015</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,622,452,160</td>
<td align="right">3,774,346,569</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">281,553,856</td>
<td align="right">230,561,432</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,026,069,899</td>
<td align="right">841,438,912</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,758,230</td>
<td align="right">44,193,042</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">193,319,109</td>
<td align="right">159,358,629</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">94,664,964</td>
<td align="right">78,918,622</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">363,377,987</td>
<td align="right">311,072,555</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,558,656</td>
<td align="right">32,219,775</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">411,110,611</td>
<td align="right">358,029,840</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">429,733</td>
<td align="right">377,128</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,657,020,036</td>
<td align="right">1,454,286,393</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">333,729,513</td>
<td align="right">293,798,262</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">18,378,066</td>
<td align="right">16,224,730</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">9,406,542</td>
<td align="right">8,312,677</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,442,434</td>
<td align="right">9,259,740</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">215,415,057</td>
<td align="right">191,152,571</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,070,965</td>
<td align="right">358,737,370</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,738,915</td>
<td align="right">362,119,499</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,271,095</td>
<td align="right">10,142,709</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">142,661,289</td>
<td align="right">131,280,443</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,561,513</td>
<td align="right">66,086,401</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,975,855</td>
<td align="right">136,010,691</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">135,428,398</td>
<td align="right">125,791,745</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">694,383</td>
<td align="right">647,284</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">119,964,974</td>
<td align="right">111,937,396</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">150,283,412</td>
<td align="right">140,795,127</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">80,560,460</td>
<td align="right">75,685,733</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,862,208</td>
<td align="right">17,770,185</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">96,676,738</td>
<td align="right">102,063,210</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">45,815,752</td>
<td align="right">43,970,707</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">73,375,666</td>
<td align="right">70,785,912</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">691,031</td>
<td align="right">667,800</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,018,159</td>
<td align="right">218,315,608</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">65,329,240</td>
<td align="right">63,849,735</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">58,419</td>
<td align="right">57,259</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,055,814,623</td>
<td align="right">1,036,861,192</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">14,822,869</td>
<td align="right">14,589,867</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,010,429</td>
<td align="right">8,871,019</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,320,470</td>
<td align="right">21,042,934</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">10,868,299</td>
<td align="right">10,742,991</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">773,856</td>
<td align="right">766,189</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">11,380</td>
<td align="right">11,300</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,267,342,123</td>
<td align="right">2,255,766,081</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,464,188</td>
<td align="right">3,450,688</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,464,353</td>
<td align="right">3,453,108</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">262,532,638</td>
<td align="right">261,771,160</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,189,405</td>
<td align="right">197,964,906</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">71,248,485</td>
<td align="right">71,316,095</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,329,264</td>
<td align="right">268,377,493</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">270,650</td>
<td align="right">270,662</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,321,991</td>
<td align="right">21,321,147</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,989,397</td>
<td align="right">20,988,650</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,270,065</td>
<td align="right">1,270,032</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,829,245</td>
<td align="right">5,829,203</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,363,858</td>
<td align="right">20,363,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,339,536</td>
<td align="right">173,339,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">77,693,920</td>
<td align="right">77,693,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,240</td>
<td align="right">38,846,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,680</td>
<td align="right">38,845,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">8,000,900</td>
<td align="right">8,000,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">651,392</td>
<td align="right">651,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">150,551</td>
<td align="right">150,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,641</td>
<td align="right">91,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">67,116</td>
<td align="right">67,116</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">29,669</td>
<td align="right">29,669</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,526</td>
<td align="right">27,526</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,996</td>
<td align="right">21,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,205</td>
<td align="right">15,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,122</td>
<td align="right">1,122</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">241</td>
<td align="right">241</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">3</td>
<td align="right">3</td>
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
<td align="right">383,905,095</td>
<td align="right">3.9%</td>
<td align="right">262,615,621</td>
<td align="right">2.7%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,478,670</td>
<td align="right">0.3%</td>
<td align="right">20,249,490</td>
<td align="right">0.2%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,415,491,700</td>
<td align="right">95.8%</td>
<td align="right">9,369,797,848</td>
<td align="right">97.1%</td>
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
<td align="left">Success</td>
<td align="right">598,456</td>
<td align="right">34.8%</td>
<td align="right">424,323</td>
<td align="right">29.9%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,121,593</td>
<td align="right">65.2%</td>
<td align="right">994,266</td>
<td align="right">70.1%</td>
<td align="right">-11.4%</td>
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
<td align="left">add different types</td>
<td align="right">48,095</td>
<td align="right">4.3%</td>
<td align="right">25,688</td>
<td align="right">2.6%</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">47,661</td>
<td align="right">4.2%</td>
<td align="right">30,997</td>
<td align="right">3.1%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">83,544</td>
<td align="right">7.4%</td>
<td align="right">57,511</td>
<td align="right">5.8%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">8,727</td>
<td align="right">0.8%</td>
<td align="right">6,186</td>
<td align="right">0.6%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,042</td>
<td align="right">0.9%</td>
<td align="right">7,408</td>
<td align="right">0.7%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">6,803</td>
<td align="right">0.6%</td>
<td align="right">5,044</td>
<td align="right">0.5%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,996</td>
<td align="right">1.3%</td>
<td align="right">11,330</td>
<td align="right">1.1%</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">401</td>
<td align="right">0.0%</td>
<td align="right">321</td>
<td align="right">0.0%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">32,490</td>
<td align="right">2.9%</td>
<td align="right">29,236</td>
<td align="right">2.9%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,723</td>
<td align="right">0.2%</td>
<td align="right">2,542</td>
<td align="right">0.3%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,604</td>
<td align="right">69.7%</td>
<td align="right">734,027</td>
<td align="right">73.8%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,547</td>
<td align="right">0.8%</td>
<td align="right">8,166</td>
<td align="right">0.8%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,888</td>
<td align="right">0.3%</td>
<td align="right">2,769</td>
<td align="right">0.3%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,557</td>
<td align="right">0.2%</td>
<td align="right">2,468</td>
<td align="right">0.2%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">21,593</td>
<td align="right">1.9%</td>
<td align="right">22,318</td>
<td align="right">2.2%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,563</td>
<td align="right">0.9%</td>
<td align="right">10,284</td>
<td align="right">1.0%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,606</td>
<td align="right">0.5%</td>
<td align="right">5,541</td>
<td align="right">0.6%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">31,917</td>
<td align="right">2.8%</td>
<td align="right">31,594</td>
<td align="right">3.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">836</td>
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
<td align="right">184,889,905</td>
<td align="right">100.0%</td>
<td align="right">60,646,915</td>
<td align="right">100.0%</td>
<td align="right">-67.2%</td>
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
<td align="right">474,766,558</td>
<td align="right">7.1%</td>
<td align="right">240,604,923</td>
<td align="right">3.7%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,200,406,873</td>
<td align="right">92.8%</td>
<td align="right">6,182,195,466</td>
<td align="right">96.2%</td>
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
<td align="right">4,803,579</td>
<td align="right">0.1%</td>
<td align="right">4,796,613</td>
<td align="right">0.1%</td>
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
<td align="right">177,314</td>
<td align="right">49.4%</td>
<td align="right">117,324</td>
<td align="right">39.2%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,772</td>
<td align="right">50.6%</td>
<td align="right">181,647</td>
<td align="right">60.8%</td>
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
<td align="left">array int</td>
<td align="right">26,640</td>
<td align="right">15.0%</td>
<td align="right">3,660</td>
<td align="right">3.1%</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,357</td>
<td align="right">12.0%</td>
<td align="right">11,457</td>
<td align="right">9.8%</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">57,005</td>
<td align="right">32.1%</td>
<td align="right">30,685</td>
<td align="right">26.2%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">840</td>
<td align="right">0.5%</td>
<td align="right">740</td>
<td align="right">0.6%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,000</td>
<td align="right">0.6%</td>
<td align="right">1,020</td>
<td align="right">0.9%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">65,609</td>
<td align="right">37.0%</td>
<td align="right">64,898</td>
<td align="right">55.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">123</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">2.4%</td>
<td align="right">4,300</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
<td align="right">155,132,894</td>
<td align="right">1.1%</td>
<td align="right">131,900,457</td>
<td align="right">1.0%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,538,151,562</td>
<td align="right">98.9%</td>
<td align="right">13,520,998,974</td>
<td align="right">99.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,460</td>
<td align="right">0.0%</td>
<td align="right">32,485</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">722,100</td>
<td align="right">0.0%</td>
<td align="right">722,126</td>
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
<td align="right">3,514,556</td>
<td align="right">100.0%</td>
<td align="right">3,075,385</td>
<td align="right">100.0%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">343</td>
<td align="right">0.0%</td>
<td align="right">343</td>
<td align="right">0.0%</td>
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
<td align="left">init not inline values</td>
<td align="right">2,829</td>
<td align="right">824.8%</td>
<td align="right">2,829</td>
<td align="right">824.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,003</td>
<td align="right">584.0%</td>
<td align="right">2,003</td>
<td align="right">584.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">921</td>
<td align="right">268.5%</td>
<td align="right">921</td>
<td align="right">268.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">343</td>
<td align="right">100.0%</td>
<td align="right">343</td>
<td align="right">100.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">804,860</td>
<td align="right">92.3%</td>
<td align="right">748,401</td>
<td align="right">91.8%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,651</td>
<td align="right">4.2%</td>
<td align="right">36,653</td>
<td align="right">4.5%</td>
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
<td align="right">101,796,558</td>
<td align="right">1.7%</td>
<td align="right">52,711,658</td>
<td align="right">0.9%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,074,066</td>
<td align="right">0.0%</td>
<td align="right">686,852</td>
<td align="right">0.0%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,735,476,829</td>
<td align="right">98.2%</td>
<td align="right">5,731,184,867</td>
<td align="right">99.1%</td>
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
<td align="right">153,760</td>
<td align="right">67.0%</td>
<td align="right">123,539</td>
<td align="right">64.4%</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">75,581</td>
<td align="right">33.0%</td>
<td align="right">68,270</td>
<td align="right">35.6%</td>
<td align="right">-9.7%</td>
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
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">6.9%</td>
<td align="right">1,682</td>
<td align="right">1.4%</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,520</td>
<td align="right">2.3%</td>
<td align="right">2,040</td>
<td align="right">1.7%</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,582</td>
<td align="right">9.5%</td>
<td align="right">9,902</td>
<td align="right">8.0%</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">31,724</td>
<td align="right">20.6%</td>
<td align="right">23,362</td>
<td align="right">18.9%</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,600</td>
<td align="right">1.7%</td>
<td align="right">2,160</td>
<td align="right">1.7%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">18,018</td>
<td align="right">11.7%</td>
<td align="right">15,442</td>
<td align="right">12.5%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,150</td>
<td align="right">11.8%</td>
<td align="right">15,828</td>
<td align="right">12.8%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,272</td>
<td align="right">8.0%</td>
<td align="right">11,153</td>
<td align="right">9.0%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">490</td>
<td align="right">0.3%</td>
<td align="right">450</td>
<td align="right">0.4%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,573</td>
<td align="right">1.0%</td>
<td align="right">1,550</td>
<td align="right">1.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">39,151</td>
<td align="right">25.5%</td>
<td align="right">38,970</td>
<td align="right">31.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,000</td>
<td align="right">0.7%</td>
<td align="right">1,000</td>
<td align="right">0.8%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,545,460</td>
<td align="right">0.1%</td>
<td align="right">747,745</td>
<td align="right">0.0%</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">37,472,304</td>
<td align="right">1.5%</td>
<td align="right">32,136,326</td>
<td align="right">1.3%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,488,148,132</td>
<td align="right">98.4%</td>
<td align="right">2,485,374,286</td>
<td align="right">98.7%</td>
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
<td align="left">Success</td>
<td align="right">61,099</td>
<td align="right">45.5%</td>
<td align="right">27,214</td>
<td align="right">27.9%</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">73,193</td>
<td align="right">54.5%</td>
<td align="right">70,290</td>
<td align="right">72.1%</td>
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
<td align="left">tuple</td>
<td align="right">28,092</td>
<td align="right">38.4%</td>
<td align="right">26,689</td>
<td align="right">38.0%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,289</td>
<td align="right">20.9%</td>
<td align="right">14,732</td>
<td align="right">21.0%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,670</td>
<td align="right">20.0%</td>
<td align="right">14,167</td>
<td align="right">20.2%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">15,142</td>
<td align="right">20.7%</td>
<td align="right">14,702</td>
<td align="right">20.9%</td>
<td align="right">-2.9%</td>
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
<td align="right">576,044,474</td>
<td align="right">83.0%</td>
<td align="right">430,991,901</td>
<td align="right">80.6%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">26,028,348</td>
<td align="right">3.7%</td>
<td align="right">31,920,909</td>
<td align="right">6.0%</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">92,075,951</td>
<td align="right">13.3%</td>
<td align="right">71,688,051</td>
<td align="right">13.4%</td>
<td align="right">-22.1%</td>
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
<td align="right">539,801</td>
<td align="right">83.2%</td>
<td align="right">650,982</td>
<td align="right">86.5%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">108,899</td>
<td align="right">16.8%</td>
<td align="right">101,557</td>
<td align="right">13.5%</td>
<td align="right">-6.7%</td>
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
<td align="right">2,567</td>
<td align="right">2.4%</td>
<td align="right">1,767</td>
<td align="right">1.7%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,662</td>
<td align="right">7.0%</td>
<td align="right">5,323</td>
<td align="right">5.2%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4,981</td>
<td align="right">4.6%</td>
<td align="right">3,960</td>
<td align="right">3.9%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,607</td>
<td align="right">6.1%</td>
<td align="right">6,005</td>
<td align="right">5.9%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">260</td>
<td align="right">0.2%</td>
<td align="right">240</td>
<td align="right">0.2%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,463</td>
<td align="right">3.2%</td>
<td align="right">3,222</td>
<td align="right">3.2%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,839</td>
<td align="right">10.9%</td>
<td align="right">11,362</td>
<td align="right">11.2%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,973</td>
<td align="right">11.0%</td>
<td align="right">11,548</td>
<td align="right">11.4%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">38,353</td>
<td align="right">35.2%</td>
<td align="right">37,076</td>
<td align="right">36.5%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">7,916</td>
<td align="right">7.3%</td>
<td align="right">7,836</td>
<td align="right">7.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,222</td>
<td align="right">4.8%</td>
<td align="right">5,182</td>
<td align="right">5.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,697</td>
<td align="right">6.1%</td>
<td align="right">6,677</td>
<td align="right">6.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">619</td>
<td align="right">0.6%</td>
<td align="right">619</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">485,129,438</td>
<td align="right">2.9%</td>
<td align="right">328,358,481</td>
<td align="right">2.0%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,052,740</td>
<td align="right">0.0%</td>
<td align="right">940,502</td>
<td align="right">0.0%</td>
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
<td align="right">401,769,232</td>
<td align="right">2.4%</td>
<td align="right">387,903,925</td>
<td align="right">2.4%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,590,536,537</td>
<td align="right">94.6%</td>
<td align="right">15,454,264,094</td>
<td align="right">95.6%</td>
<td align="right">-0.9%</td>
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
<td align="right">466,185</td>
<td align="right">4.8%</td>
<td align="right">418,945</td>
<td align="right">4.5%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,277,450</td>
<td align="right">95.2%</td>
<td align="right">8,965,333</td>
<td align="right">95.5%</td>
<td align="right">-3.4%</td>
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
<td align="right">89,195</td>
<td align="right">19.1%</td>
<td align="right">64,862</td>
<td align="right">15.5%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">32,368</td>
<td align="right">6.9%</td>
<td align="right">28,026</td>
<td align="right">6.7%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">84,076</td>
<td align="right">18.0%</td>
<td align="right">76,024</td>
<td align="right">18.1%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">15,486</td>
<td align="right">3.3%</td>
<td align="right">14,164</td>
<td align="right">3.4%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">15,289</td>
<td align="right">3.3%</td>
<td align="right">13,989</td>
<td align="right">3.3%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,924</td>
<td align="right">0.6%</td>
<td align="right">2,690</td>
<td align="right">0.6%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3,464</td>
<td align="right">0.7%</td>
<td align="right">3,303</td>
<td align="right">0.8%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">139,326</td>
<td align="right">29.9%</td>
<td align="right">132,871</td>
<td align="right">31.7%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">5,300</td>
<td align="right">1.1%</td>
<td align="right">5,086</td>
<td align="right">1.2%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">680</td>
<td align="right">0.1%</td>
<td align="right">700</td>
<td align="right">0.2%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">2,674</td>
<td align="right">0.6%</td>
<td align="right">2,634</td>
<td align="right">0.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,425</td>
<td align="right">1.2%</td>
<td align="right">5,365</td>
<td align="right">1.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">21,520</td>
<td align="right">4.6%</td>
<td align="right">21,318</td>
<td align="right">5.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">33,279</td>
<td align="right">7.1%</td>
<td align="right">33,143</td>
<td align="right">7.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,120</td>
<td align="right">0.2%</td>
<td align="right">1,119</td>
<td align="right">0.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">360</td>
<td align="right">0.1%</td>
<td align="right">360</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">122</td>
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
<td align="right">4,567,692,770</td>
<td align="right">99.5%</td>
<td align="right">2,890,663,519</td>
<td align="right">99.3%</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">415,168</td>
<td align="right">0.0%</td>
<td align="right">414,848</td>
<td align="right">0.0%</td>
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
<td align="right">19,899,939</td>
<td align="right">0.4%</td>
<td align="right">19,899,981</td>
<td align="right">0.7%</td>
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
<td align="right">9,934</td>
<td align="right">0.0%</td>
<td align="right">9,934</td>
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
<td align="right">469,644</td>
<td align="right">100.0%</td>
<td align="right">469,603</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">89,006,336</td>
<td align="right">100.0%</td>
<td align="right">86,200,704</td>
<td align="right">100.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,644</td>
<td align="right">0.0%</td>
<td align="right">7,644</td>
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
<td align="right">7,561</td>
<td align="right">100.0%</td>
<td align="right">7,561</td>
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
<td align="right">173,274,845</td>
<td align="right">18.1%</td>
<td align="right">173,274,852</td>
<td align="right">18.1%</td>
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
<td align="right">786,227,611</td>
<td align="right">81.9%</td>
<td align="right">786,227,582</td>
<td align="right">81.9%</td>
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
<td align="right">30,663</td>
<td align="right">0.0%</td>
<td align="right">30,663</td>
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
<td align="right">5,557</td>
<td align="right">8.5%</td>
<td align="right">5,557</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,714</td>
<td align="right">91.5%</td>
<td align="right">59,714</td>
<td align="right">91.5%</td>
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
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">55.6%</td>
<td align="right">33,180</td>
<td align="right">55.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,268</td>
<td align="right">23.9%</td>
<td align="right">14,268</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,020</td>
<td align="right">16.8%</td>
<td align="right">10,020</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,240</td>
<td align="right">3.8%</td>
<td align="right">2,240</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
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
<td align="right">125,076,462</td>
<td align="right">4.8%</td>
<td align="right">107,012,983</td>
<td align="right">4.1%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">45,629,380</td>
<td align="right">1.7%</td>
<td align="right">43,787,210</td>
<td align="right">1.7%</td>
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
<td align="right">2,449,619,197</td>
<td align="right">93.5%</td>
<td align="right">2,466,863,901</td>
<td align="right">94.2%</td>
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
<td align="left">Success</td>
<td align="right">2,460,874</td>
<td align="right">96.8%</td>
<td align="right">2,120,184</td>
<td align="right">96.4%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">82,568</td>
<td align="right">3.2%</td>
<td align="right">79,691</td>
<td align="right">3.6%</td>
<td align="right">-3.5%</td>
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
<td align="right">2,985</td>
<td align="right">3.6%</td>
<td align="right">2,745</td>
<td align="right">3.4%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,423</td>
<td align="right">10.2%</td>
<td align="right">7,803</td>
<td align="right">9.8%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">32,084</td>
<td align="right">38.9%</td>
<td align="right">30,285</td>
<td align="right">38.0%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">804</td>
<td align="right">1.0%</td>
<td align="right">764</td>
<td align="right">1.0%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">15,445</td>
<td align="right">18.7%</td>
<td align="right">15,285</td>
<td align="right">19.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,075</td>
<td align="right">6.1%</td>
<td align="right">5,055</td>
<td align="right">6.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,831</td>
<td align="right">11.9%</td>
<td align="right">9,833</td>
<td align="right">12.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">4,981</td>
<td align="right">6.0%</td>
<td align="right">4,981</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">2,100</td>
<td align="right">2.5%</td>
<td align="right">2,100</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">780</td>
<td align="right">0.9%</td>
<td align="right">780</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">60</td>
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
<td align="right">12,297,643</td>
<td align="right">100.0%</td>
<td align="right">4,923,503</td>
<td align="right">100.0%</td>
<td align="right">-60.0%</td>
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
<td align="right">93,465,933</td>
<td align="right">9.6%</td>
<td align="right">18,593,661</td>
<td align="right">2.1%</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">876,953,227</td>
<td align="right">90.4%</td>
<td align="right">873,350,070</td>
<td align="right">97.9%</td>
<td align="right">-0.4%</td>
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
<td align="right">67,150</td>
<td align="right">83.4%</td>
<td align="right">45,731</td>
<td align="right">77.4%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,370</td>
<td align="right">16.6%</td>
<td align="right">13,368</td>
<td align="right">22.6%</td>
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
<td align="left">array int</td>
<td align="right">14,240</td>
<td align="right">21.2%</td>
<td align="right">6,100</td>
<td align="right">13.3%</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">42,203</td>
<td align="right">62.8%</td>
<td align="right">29,283</td>
<td align="right">64.0%</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">6,887</td>
<td align="right">10.3%</td>
<td align="right">6,568</td>
<td align="right">14.4%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">600</td>
<td align="right">0.9%</td>
<td align="right">580</td>
<td align="right">1.3%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,600</td>
<td align="right">2.4%</td>
<td align="right">1,580</td>
<td align="right">3.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,600</td>
<td align="right">2.4%</td>
<td align="right">1,600</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">149,896,112</td>
<td align="right">2.5%</td>
<td align="right">59,123,293</td>
<td align="right">1.0%</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">26,297,068</td>
<td align="right">0.4%</td>
<td align="right">22,620,646</td>
<td align="right">0.4%</td>
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
<td align="right">5,758,790,024</td>
<td align="right">97.0%</td>
<td align="right">5,558,904,367</td>
<td align="right">98.5%</td>
<td align="right">-3.5%</td>
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
<td align="right">220,043</td>
<td align="right">24.2%</td>
<td align="right">260,190</td>
<td align="right">29.6%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">689,286</td>
<td align="right">75.8%</td>
<td align="right">620,203</td>
<td align="right">70.4%</td>
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
<td align="left">number</td>
<td align="right">44,741</td>
<td align="right">20.3%</td>
<td align="right">110,172</td>
<td align="right">42.3%</td>
<td align="right">146.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">19,251</td>
<td align="right">8.7%</td>
<td align="right">7,895</td>
<td align="right">3.0%</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,526</td>
<td align="right">7.5%</td>
<td align="right">12,218</td>
<td align="right">4.7%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,469</td>
<td align="right">0.7%</td>
<td align="right">1,250</td>
<td align="right">0.5%</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">6,922</td>
<td align="right">3.1%</td>
<td align="right">5,957</td>
<td align="right">2.3%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">84,128</td>
<td align="right">38.2%</td>
<td align="right">76,867</td>
<td align="right">29.5%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">14,910</td>
<td align="right">6.8%</td>
<td align="right">14,050</td>
<td align="right">5.4%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,122</td>
<td align="right">2.8%</td>
<td align="right">5,832</td>
<td align="right">2.2%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">24,951</td>
<td align="right">11.3%</td>
<td align="right">24,926</td>
<td align="right">9.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">683</td>
<td align="right">0.3%</td>
<td align="right">683</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
<td align="right">0.1%</td>
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
<td align="right">198,816</td>
<td align="right">0.0%</td>
<td align="right">97,451</td>
<td align="right">0.0%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,057,841,701</td>
<td align="right">100.0%</td>
<td align="right">1,887,685,793</td>
<td align="right">100.0%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">434,440</td>
<td align="right">0.0%</td>
<td align="right">434,440</td>
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
<td align="right">1,763</td>
<td align="right">3.6%</td>
<td align="right">1,683</td>
<td align="right">3.5%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">46,879</td>
<td align="right">96.4%</td>
<td align="right">46,883</td>
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
<td align="left">other</td>
<td align="right">380</td>
<td align="right">21.6%</td>
<td align="right">320</td>
<td align="right">19.0%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,116</td>
<td align="right">63.3%</td>
<td align="right">1,096</td>
<td align="right">65.1%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">267</td>
<td align="right">15.1%</td>
<td align="right">267</td>
<td align="right">15.9%</td>
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
<td align="right">2,261,390,141</td>
<td align="right">2.5%</td>
<td align="right">1,374,842,898</td>
<td align="right">2.2%</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">57,950,087,468</td>
<td align="right">62.9%</td>
<td align="right">38,022,441,647</td>
<td align="right">62.1%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">31,173,870,340</td>
<td align="right">33.8%</td>
<td align="right">21,073,702,443</td>
<td align="right">34.4%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">774,143,902</td>
<td align="right">0.8%</td>
<td align="right">709,764,624</td>
<td align="right">1.2%</td>
<td align="right">-8.3%</td>
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
<td align="right">184,889,905</td>
<td align="right">8.2%</td>
<td align="right">60,646,915</td>
<td align="right">4.4%</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">149,896,112</td>
<td align="right">6.6%</td>
<td align="right">59,123,293</td>
<td align="right">4.3%</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">474,766,558</td>
<td align="right">21.0%</td>
<td align="right">240,604,923</td>
<td align="right">17.6%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">101,796,558</td>
<td align="right">4.5%</td>
<td align="right">52,711,658</td>
<td align="right">3.8%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">485,129,438</td>
<td align="right">21.5%</td>
<td align="right">328,358,481</td>
<td align="right">24.0%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">383,905,095</td>
<td align="right">17.0%</td>
<td align="right">262,615,621</td>
<td align="right">19.2%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">92,075,951</td>
<td align="right">4.1%</td>
<td align="right">71,688,051</td>
<td align="right">5.2%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">45,629,380</td>
<td align="right">2.0%</td>
<td align="right">43,787,210</td>
<td align="right">3.2%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,274,845</td>
<td align="right">7.7%</td>
<td align="right">173,274,852</td>
<td align="right">12.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,465,933</td>
<td align="right">4.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">32,136,326</td>
<td align="right">2.3%</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">83,583,750</td>
<td align="right">10.8%</td>
<td align="right">64,395,876</td>
<td align="right">9.1%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">23,908,292</td>
<td align="right">3.1%</td>
<td align="right">19,368,988</td>
<td align="right">2.7%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">101,163,564</td>
<td align="right">13.1%</td>
<td align="right">87,642,570</td>
<td align="right">12.3%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">43,173,612</td>
<td align="right">5.6%</td>
<td align="right">37,686,046</td>
<td align="right">5.3%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,177,240</td>
<td align="right">2.6%</td>
<td align="right">18,124,260</td>
<td align="right">2.6%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">49,372,034</td>
<td align="right">6.4%</td>
<td align="right">48,695,231</td>
<td align="right">6.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">111,113,912</td>
<td align="right">14.3%</td>
<td align="right">110,013,452</td>
<td align="right">15.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">155,869,247</td>
<td align="right">20.1%</td>
<td align="right">155,431,114</td>
<td align="right">21.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,211,092</td>
<td align="right">2.4%</td>
<td align="right">18,195,765</td>
<td align="right">2.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,497,989</td>
<td align="right">3.6%</td>
<td align="right">27,497,574</td>
<td align="right">3.9%</td>
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
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,418,292</td>
<td align="right">0.1%</td>
<td align="right">2,658,132</td>
<td align="right">0.0%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,174,603,886</td>
<td align="right">73.1%</td>
<td align="right">6,131,610,350</td>
<td align="right">73.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">851,740,343</td>
<td align="right">10.1%</td>
<td align="right">846,580,217</td>
<td align="right">10.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,271,084,876</td>
<td align="right">26.9%</td>
<td align="right">2,259,498,016</td>
<td align="right">26.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,271,084,876</td>
<td align="right">26.9%</td>
<td align="right">2,259,498,016</td>
<td align="right">26.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,419,344,533</td>
<td align="right">16.8%</td>
<td align="right">1,412,917,799</td>
<td align="right">16.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,690,631,888</td>
<td align="right">79.2%</td>
<td align="right">6,667,481,233</td>
<td align="right">79.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,414,896,132</td>
<td align="right">16.8%</td>
<td align="right">1,410,229,558</td>
<td align="right">16.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">334,223,051</td>
<td align="right">4.0%</td>
<td align="right">333,561,500</td>
<td align="right">4.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,613,149</td>
<td align="right">1.0%</td>
<td align="right">84,595,014</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,055,788</td>
<td align="right">0.4%</td>
<td align="right">31,054,929</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,590,198</td>
<td align="right">3.9%</td>
<td align="right">331,586,003</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,645</td>
<td align="right">2.1%</td>
<td align="right">175,480,635</td>
<td align="right">2.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">30,109</td>
<td align="right">0.0%</td>
<td align="right">30,109</td>
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
<td align="left">Interpreter mortal increfs</td>
<td align="right">41,833,738,829</td>
<td align="right">19.2%</td>
<td align="right">28,987,209,106</td>
<td align="right">13.4%</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">19,523,859,282</td>
<td align="right">9.0%</td>
<td align="right">14,446,708,105</td>
<td align="right">6.7%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">22,340,264,772</td>
<td align="right">8.5%</td>
<td align="right">18,043,296,658</td>
<td align="right">6.9%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">57,114,985,764</td>
<td align="right">21.8%</td>
<td align="right">47,175,901,951</td>
<td align="right">18.0%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">97,456,639,944</td>
<td align="right">44.7%</td>
<td align="right">111,197,043,176</td>
<td align="right">51.3%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">105,056,068,248</td>
<td align="right">40.2%</td>
<td align="right">116,035,554,898</td>
<td align="right">44.3%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">61,963,116</td>
<td align="right"></td>
<td align="right">58,450,650</td>
<td align="right"></td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">67,594,451</td>
<td align="right"></td>
<td align="right">64,115,671</td>
<td align="right"></td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">77,146,274,614</td>
<td align="right">29.5%</td>
<td align="right">80,796,348,758</td>
<td align="right">30.8%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">59,223,067,370</td>
<td align="right">27.2%</td>
<td align="right">61,941,620,045</td>
<td align="right">28.6%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">232,836,557</td>
<td align="right"></td>
<td align="right">236,165,716</td>
<td align="right"></td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,380,031,963</td>
<td align="right"></td>
<td align="right">2,346,420,065</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">13,091,158,396</td>
<td align="right">52.4%</td>
<td align="right">13,231,280,952</td>
<td align="right">52.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">13,216,164,781</td>
<td align="right">52.9%</td>
<td align="right">13,356,459,256</td>
<td align="right">53.1%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,985,367,063</td>
<td align="right"></td>
<td align="right">14,123,700,358</td>
<td align="right"></td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,628,983</td>
<td align="right"></td>
<td align="right">6,661,217</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,731,446,283</td>
<td align="right"></td>
<td align="right">3,713,370,079</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">104,007,706</td>
<td align="right">0.4%</td>
<td align="right">104,188,185</td>
<td align="right">0.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,998,679</td>
<td align="right">0.1%</td>
<td align="right">20,990,119</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,180</td>
<td align="right">1.5%</td>
<td align="right">3,381,380</td>
<td align="right">1.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,784,852,160</td>
<td align="right">47.1%</td>
<td align="right">11,782,322,117</td>
<td align="right">46.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,786,698,503</td>
<td align="right"></td>
<td align="right">11,784,172,768</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">198,300</td>
<td align="right">0.1%</td>
<td align="right">198,300</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">16,243</td>
<td align="right">0.0%</td>
<td align="right">16,243</td>
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
<td align="right">451,319</td>
<td align="right">112,166,117</td>
<td align="right">19,191,346,335</td>
<td align="right">453,934</td>
<td align="right">112,071,937</td>
<td align="right">19,257,739,195</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">10,240</td>
<td align="right">5,379,840</td>
<td align="right">6,332,019,160</td>
<td align="right">15,360</td>
<td align="right">10,755,840</td>
<td align="right">6,958,374,400</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">2,548</td>
<td align="right">0.1%</td>
<td align="right">5,425</td>
<td align="right">0.4%</td>
<td align="right">112.9%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">893,958</td>
<td align="right">51.7%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">10,008</td>
<td align="right">1.2%</td>
<td align="right">15,941</td>
<td align="right">1.4%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">896,790</td>
<td align="right">51.9%</td>
<td align="right">395,976</td>
<td align="right">25.6%</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">828,375</td>
<td align="right">47.9%</td>
<td align="right">1,143,061</td>
<td align="right">74.0%</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">600</td>
<td align="right">0.0%</td>
<td align="right">800</td>
<td align="right">0.1%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">5,879</td>
<td align="right">0.3%</td>
<td align="right">7,564</td>
<td align="right">0.5%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">30,503</td>
<td align="right">1.8%</td>
<td align="right">38,039</td>
<td align="right">2.5%</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">9,228,484,433</td>
<td align="right"></td>
<td align="right">11,189,979,814</td>
<td align="right"></td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">15,618</td>
<td align="right">0.9%</td>
<td align="right">18,585</td>
<td align="right">1.2%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">315,229,904,334</td>
<td align="right">3,415.8%</td>
<td align="right">370,218,647,789</td>
<td align="right">3,308.5%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,727,713</td>
<td align="right"></td>
<td align="right">1,544,462</td>
<td align="right"></td>
<td align="right">-10.6%</td>
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
<td align="right">802,754</td>
<td align="right">96.9%</td>
<td align="right">1,113,925</td>
<td align="right">97.5%</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">828,375</td>
<td align="right"></td>
<td align="right">1,143,061</td>
<td align="right"></td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,943</td>
<td align="right">0.4%</td>
<td align="right">3,213</td>
<td align="right">0.3%</td>
<td align="right">9.2%</td>
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
<td align="right">59,745</td>
<td align="right">7.2%</td>
<td align="right">76,346</td>
<td align="right">6.7%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">121,036</td>
<td align="right">14.6%</td>
<td align="right">187,904</td>
<td align="right">16.4%</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">276,824</td>
<td align="right">33.4%</td>
<td align="right">368,530</td>
<td align="right">32.2%</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">236,135</td>
<td align="right">28.5%</td>
<td align="right">306,920</td>
<td align="right">26.9%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">94,138</td>
<td align="right">11.4%</td>
<td align="right">139,745</td>
<td align="right">12.2%</td>
<td align="right">48.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">34,419</td>
<td align="right">4.2%</td>
<td align="right">53,393</td>
<td align="right">4.7%</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">5,438</td>
<td align="right">0.7%</td>
<td align="right">9,283</td>
<td align="right">0.8%</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">640</td>
<td align="right">0.1%</td>
<td align="right">940</td>
<td align="right">0.1%</td>
<td align="right">46.9%</td>
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
<td align="right">36,901</td>
<td align="right">4.5%</td>
<td align="right">19,258</td>
<td align="right">1.7%</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">93,242</td>
<td align="right">11.3%</td>
<td align="right">153,323</td>
<td align="right">13.4%</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">142,218</td>
<td align="right">17.2%</td>
<td align="right">219,524</td>
<td align="right">19.2%</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">312,519</td>
<td align="right">37.7%</td>
<td align="right">405,766</td>
<td align="right">35.5%</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">152,111</td>
<td align="right">18.4%</td>
<td align="right">214,870</td>
<td align="right">18.8%</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">51,381</td>
<td align="right">6.2%</td>
<td align="right">74,828</td>
<td align="right">6.5%</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">13,026</td>
<td align="right">1.6%</td>
<td align="right">24,582</td>
<td align="right">2.2%</td>
<td align="right">88.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,356</td>
<td align="right">0.2%</td>
<td align="right">1,774</td>
<td align="right">0.2%</td>
<td align="right">30.8%</td>
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
<td align="left">_POP_EXCEPT</td>
<td align="right">1,380</td>
<td align="right">278,072</td>
<td align="right">20,050.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">2,849,902</td>
<td align="right">167,295,894</td>
<td align="right">5,770.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">7,168,847</td>
<td align="right">58,796,234</td>
<td align="right">720.2%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">3,623</td>
<td align="right">26,981</td>
<td align="right">644.7%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">7,132,917</td>
<td align="right">42,271,321</td>
<td align="right">492.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">60,407,979</td>
<td align="right">279,896,456</td>
<td align="right">363.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,669,060</td>
<td align="right">6,576,363</td>
<td align="right">294.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">905,595,755</td>
<td align="right">3,566,927,373</td>
<td align="right">293.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,578,771</td>
<td align="right">36,903,955</td>
<td align="right">285.3%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,671,040</td>
<td align="right">13,306,733</td>
<td align="right">262.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">844,401</td>
<td align="right">3,000,828</td>
<td align="right">255.4%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,889,100</td>
<td align="right">16,268,746</td>
<td align="right">232.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,055,426,255</td>
<td align="right">3,223,266,989</td>
<td align="right">205.4%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,796,220</td>
<td align="right">8,270,612</td>
<td align="right">195.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,157,548</td>
<td align="right">149,242,935</td>
<td align="right">175.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,161,328</td>
<td align="right">149,248,575</td>
<td align="right">175.6%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,251,933</td>
<td align="right">10,954,496</td>
<td align="right">157.6%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">38,100</td>
<td align="right">89,505</td>
<td align="right">134.9%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,756,105</td>
<td align="right">6,219,951</td>
<td align="right">125.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,907,512</td>
<td align="right">4,227,612</td>
<td align="right">121.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">207,918,017</td>
<td align="right">438,065,276</td>
<td align="right">110.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">202,602,319</td>
<td align="right">399,197,671</td>
<td align="right">97.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,725,457</td>
<td align="right">16,998,940</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">20,429,937</td>
<td align="right">39,125,898</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">172,804,839</td>
<td align="right">317,980,773</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">50,129,989</td>
<td align="right">91,746,887</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">13,833,890</td>
<td align="right">25,051,442</td>
<td align="right">81.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">41,152,522</td>
<td align="right">73,633,175</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">32,192,673</td>
<td align="right">57,097,547</td>
<td align="right">77.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">42,115,522</td>
<td align="right">74,514,116</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,987,560</td>
<td align="right">17,506,761</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,608,920</td>
<td align="right">9,232,988</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">89,342,754</td>
<td align="right">146,775,715</td>
<td align="right">64.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">881,325,005</td>
<td align="right">1,445,825,889</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,606,880</td>
<td align="right">9,186,301</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">445,596,557</td>
<td align="right">725,266,734</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,754,620</td>
<td align="right">78,946,350</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,754,620</td>
<td align="right">78,946,350</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">116,490,798</td>
<td align="right">185,690,117</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">38,894,320</td>
<td align="right">61,062,422</td>
<td align="right">57.0%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">48,894,224</td>
<td align="right">76,598,356</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">48,894,224</td>
<td align="right">76,598,356</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">1,159,386</td>
<td align="right">1,777,659</td>
<td align="right">53.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">109,080,210</td>
<td align="right">166,043,565</td>
<td align="right">52.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">161,551,639</td>
<td align="right">239,194,358</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">131,217,186</td>
<td align="right">191,463,583</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">1,567,968</td>
<td align="right">2,240,370</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,718,132,801</td>
<td align="right">2,443,091,934</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,036,879</td>
<td align="right">137,478,514</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">158,195,514</td>
<td align="right">221,905,092</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">202,659,429</td>
<td align="right">283,278,919</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">83,904,803</td>
<td align="right">116,468,395</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">105,682,262</td>
<td align="right">146,104,696</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">457,066,664</td>
<td align="right">629,984,624</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">99,516,758</td>
<td align="right">136,427,193</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">286,631,849</td>
<td align="right">390,941,175</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,441,742,158</td>
<td align="right">3,327,091,078</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,847,480</td>
<td align="right">2,514,260</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,384,767,921</td>
<td align="right">3,213,227,598</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,104,209,955</td>
<td align="right">2,816,368,866</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">125,274,400</td>
<td align="right">167,165,649</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,126,294,519</td>
<td align="right">2,830,540,028</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,259,113,010</td>
<td align="right">2,986,133,807</td>
<td align="right">32.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">371,941,117</td>
<td align="right">491,445,219</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">5,422,603</td>
<td align="right">7,082,980</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">115,484,146</td>
<td align="right">150,834,205</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,110,612,630</td>
<td align="right">4,048,221,477</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">347,376,151</td>
<td align="right">451,690,535</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,103,043,927</td>
<td align="right">1,433,807,868</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">297,026,335</td>
<td align="right">385,251,479</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">489,020</td>
<td align="right">630,720</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">977,606,404</td>
<td align="right">1,256,614,151</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,690,232,533</td>
<td align="right">4,697,841,794</td>
<td align="right">27.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,841,273,769</td>
<td align="right">4,886,738,043</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">146,990,890</td>
<td align="right">186,480,821</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">213,033,780</td>
<td align="right">269,327,910</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,136,017,601</td>
<td align="right">10,215,773,232</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,541,401,055</td>
<td align="right">4,441,071,690</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">167,786,680</td>
<td align="right">209,601,016</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">133,273,234</td>
<td align="right">166,465,936</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">392,348,241</td>
<td align="right">490,018,525</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,331,243,429</td>
<td align="right">1,661,880,596</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">35,507,468</td>
<td align="right">44,272,546</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">914,487,628</td>
<td align="right">1,140,144,339</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">3,490,938,727</td>
<td align="right">4,348,560,303</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">8,118,101,342</td>
<td align="right">10,102,170,041</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,807,081,185</td>
<td align="right">4,714,451,854</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">689,870,498</td>
<td align="right">853,683,326</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">702,837,666</td>
<td align="right">867,321,505</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">984,502,796</td>
<td align="right">1,213,845,266</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">808,542,806</td>
<td align="right">996,323,731</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,920,968,758</td>
<td align="right">2,356,330,272</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,625,490,993</td>
<td align="right">1,984,264,786</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">31,222,472</td>
<td align="right">38,037,218</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">915,526,225</td>
<td align="right">1,110,255,085</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">9,228,484,433</td>
<td align="right">11,189,979,814</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,529,093,569</td>
<td align="right">4,273,615,321</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">163,734,497</td>
<td align="right">197,391,326</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">33,468,854</td>
<td align="right">40,322,399</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">247,660,485</td>
<td align="right">297,273,714</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,654,804,076</td>
<td align="right">1,974,850,617</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">333,727,015</td>
<td align="right">398,198,731</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,055,352,719</td>
<td align="right">9,610,431,644</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,777,311,272</td>
<td align="right">2,119,845,078</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">35,514,412</td>
<td align="right">42,358,404</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,769,899,680</td>
<td align="right">2,106,969,731</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">66,252,040</td>
<td align="right">78,830,212</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">889,399,513</td>
<td align="right">1,057,738,424</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">745,059,431</td>
<td align="right">884,420,458</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,666,486</td>
<td align="right">242,286,892</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,215,040</td>
<td align="right">414,314,300</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">246,156,073</td>
<td align="right">290,700,279</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,379,516,003</td>
<td align="right">2,807,415,884</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,414,449,749</td>
<td align="right">1,667,461,183</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">684,811,838</td>
<td align="right">807,299,966</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">25,387,230,932</td>
<td align="right">29,849,893,853</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">691,531,820</td>
<td align="right">809,530,485</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">570,216,542</td>
<td align="right">667,199,326</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">687,194,269</td>
<td align="right">802,819,222</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,079,263,825</td>
<td align="right">1,255,347,174</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">72,489,699</td>
<td align="right">84,296,418</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">12,053,061,254</td>
<td align="right">13,999,960,141</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,347,680,047</td>
<td align="right">7,362,566,875</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">21,995,098</td>
<td align="right">25,462,394</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">882,402,106</td>
<td align="right">1,019,016,968</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">22,731,918</td>
<td align="right">26,205,362</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,080,696,567</td>
<td align="right">1,245,258,348</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,416,073,874</td>
<td align="right">5,086,752,878</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">113,868,464</td>
<td align="right">130,984,219</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,653,511,821</td>
<td align="right">16,820,411,371</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,681,938,201</td>
<td align="right">4,224,633,601</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,617,978,198</td>
<td align="right">1,852,278,370</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,336,974,206</td>
<td align="right">2,670,828,604</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">55,443,824</td>
<td align="right">63,182,665</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,699,229,615</td>
<td align="right">1,936,194,751</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">21,152,460,737</td>
<td align="right">24,006,231,917</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,815,225,631</td>
<td align="right">2,052,253,825</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">958,541,089</td>
<td align="right">1,082,623,513</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">507,570,930</td>
<td align="right">572,032,880</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,423,758,758</td>
<td align="right">1,602,883,528</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,676,681,964</td>
<td align="right">6,380,330,864</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">835,333,080</td>
<td align="right">937,977,502</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">71,675,620</td>
<td align="right">80,449,120</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">282,771,220</td>
<td align="right">315,795,134</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,239,286,406</td>
<td align="right">11,426,954,165</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">94,294,371</td>
<td align="right">105,046,766</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,071,791,933</td>
<td align="right">1,193,071,890</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">350,254,019</td>
<td align="right">389,849,751</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,195,128</td>
<td align="right">108,149,412</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,223,308</td>
<td align="right">108,172,934</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">355,606,466</td>
<td align="right">395,205,889</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">62,980,880</td>
<td align="right">69,951,674</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,343,459,877</td>
<td align="right">1,487,385,261</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,389,687</td>
<td align="right">667,117,620</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">112,882,839</td>
<td align="right">124,234,343</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">1,292,732</td>
<td align="right">1,163,243</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">302,468,005</td>
<td align="right">332,448,357</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">100,238,453</td>
<td align="right">109,970,411</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,143,717,400</td>
<td align="right">1,253,928,031</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">782,351,898</td>
<td align="right">857,284,997</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">24,991,116</td>
<td align="right">27,378,249</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">626,215,401</td>
<td align="right">685,886,782</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">954,224,086</td>
<td align="right">1,044,324,981</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">44,216,237</td>
<td align="right">48,249,678</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">44,216,237</td>
<td align="right">48,247,078</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">561,204,432</td>
<td align="right">611,063,033</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">8,288,910,101</td>
<td align="right">7,578,795,272</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,267,828,424</td>
<td align="right">5,715,707,323</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">159,370,481</td>
<td align="right">172,675,783</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">565,350,280</td>
<td align="right">610,898,954</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,598,618,397</td>
<td align="right">2,806,537,149</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,432,750</td>
<td align="right">35,011,848</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">532,741,366</td>
<td align="right">573,478,953</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,475,893,204</td>
<td align="right">1,583,476,310</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">234,859,119</td>
<td align="right">251,854,473</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">13,362,391</td>
<td align="right">12,400,577</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,524,239,989</td>
<td align="right">1,630,697,695</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,179,411,765</td>
<td align="right">1,260,985,284</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">769,416,189</td>
<td align="right">822,604,732</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,886,792,241</td>
<td align="right">5,215,115,407</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,939,170,598</td>
<td align="right">4,196,884,066</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">676,363,200</td>
<td align="right">719,911,299</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,290,976</td>
<td align="right">1,371,080</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">120,295,057</td>
<td align="right">127,598,146</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">6,546,724,477</td>
<td align="right">6,933,887,518</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,225,365,068</td>
<td align="right">2,354,856,510</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,624,977,427</td>
<td align="right">3,819,895,031</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,041,916,139</td>
<td align="right">1,096,247,587</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,316,738,982</td>
<td align="right">2,437,348,777</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">150,129,520</td>
<td align="right">157,503,660</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">394,053,731</td>
<td align="right">413,112,116</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,050,388</td>
<td align="right">1,100,065</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">10,288,504,034</td>
<td align="right">10,762,342,698</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">25,303</td>
<td align="right">26,463</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,713,694,685</td>
<td align="right">1,790,822,169</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">237,243,062</td>
<td align="right">247,666,771</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">781,523,968</td>
<td align="right">815,853,743</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">782,881,748</td>
<td align="right">817,211,523</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">154,164,815</td>
<td align="right">160,163,308</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">364,965,233</td>
<td align="right">378,914,647</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">719,440,051</td>
<td align="right">741,850,765</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,030,733,337</td>
<td align="right">3,123,629,977</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">229,258,065</td>
<td align="right">235,788,199</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">11,936,819</td>
<td align="right">11,729,832</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">67,839,699</td>
<td align="right">68,679,375</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">735,163,256</td>
<td align="right">744,192,012</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,310,326,736</td>
<td align="right">1,326,113,697</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,973,508</td>
<td align="right">81,718,333</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,051,397,021</td>
<td align="right">2,067,023,641</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,657,797</td>
<td align="right">32,890,751</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,335,717,533</td>
<td align="right">2,347,974,944</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,824,576,821</td>
<td align="right">2,809,980,327</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">475,465,963</td>
<td align="right">477,190,182</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,740,660</td>
<td align="right">4,754,160</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,353,742,783</td>
<td align="right">2,360,241,685</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">580,516,320</td>
<td align="right">579,864,777</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,832,619</td>
<td align="right">46,847,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">963,080</td>
<td align="right">963,191</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">517,932,770</td>
<td align="right">517,884,512</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,780</td>
<td align="right">125,514,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">963,000</td>
<td align="right">963,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">598,440</td>
<td align="right">598,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">440</td>
<td align="right">440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">546,646,310</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">43,333,607</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">1,006,893</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">121,942</td>
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
<td align="right">33,982</td>
<td align="right">75,706</td>
<td align="right">122.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">2,823</td>
<td align="right">5,856</td>
<td align="right">107.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120</td>
<td align="right">240</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">70,702</td>
<td align="right">98,328</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">41,940</td>
<td align="right">49,367</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right"></td>
<td align="right">2,240</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right"></td>
<td align="right">431</td>
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
<td align="right">240</td>
<td align="right">240</td>
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
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,260</td>
<td align="right">1,260</td>
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
<td align="right">1,260</td>
<td align="right">1,260</td>
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
<td align="right">1,941</td>
<td align="right">1,941</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
