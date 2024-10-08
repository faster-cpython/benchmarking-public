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
<td align="left">END_FOR</td>
<td align="right">82,461,963</td>
<td align="right">805,391</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">338,864,978</td>
<td align="right">8,086,961</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,641</td>
<td align="right">2,581</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">43,448,680</td>
<td align="right">1,398,601</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,521,763</td>
<td align="right">295,323</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">44,067,851</td>
<td align="right">1,743,001</td>
<td align="right">-96.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">62,053,943</td>
<td align="right">2,907,749</td>
<td align="right">-95.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">5,560</td>
<td align="right">-93.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">304,922,595</td>
<td align="right">18,877,104</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,210,011</td>
<td align="right">833,415</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">275,147,318</td>
<td align="right">35,415,313</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">27,949,499</td>
<td align="right">4,698,176</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,477,730</td>
<td align="right">754,714</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">120,124,718</td>
<td align="right">20,539,653</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">298,283,270</td>
<td align="right">58,772,193</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">90,973,084</td>
<td align="right">18,205,775</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">93,417,344</td>
<td align="right">20,389,822</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">43,628,260</td>
<td align="right">10,181,662</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">735,481,162</td>
<td align="right">186,522,909</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">56,050,360</td>
<td align="right">14,868,561</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">53,177,386</td>
<td align="right">15,155,280</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,479,810</td>
<td align="right">40,604,348</td>
<td align="right">-71.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">220,106,779</td>
<td align="right">63,972,630</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,082,879</td>
<td align="right">53,001,202</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">56,641,245</td>
<td align="right">16,864,676</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,016,371</td>
<td align="right">38,722,677</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">430,189,182</td>
<td align="right">136,201,011</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">50,028,630</td>
<td align="right">16,204,666</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">197,308,884</td>
<td align="right">66,164,365</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">108,046,843</td>
<td align="right">38,174,791</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">107,218,522</td>
<td align="right">38,114,103</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,142,793</td>
<td align="right">29,717,908</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">332,686,658</td>
<td align="right">119,782,390</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,445,404</td>
<td align="right">17,118,788</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">238,807,069</td>
<td align="right">87,025,725</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">103,158,635</td>
<td align="right">38,023,303</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">100,288,460</td>
<td align="right">38,764,312</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">158,450,808</td>
<td align="right">61,985,194</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">27,478,592</td>
<td align="right">11,797,100</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">392,395,523</td>
<td align="right">172,361,147</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,893,250</td>
<td align="right">1,273,370</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">36,478,010</td>
<td align="right">16,128,211</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">251,207,037</td>
<td align="right">111,921,717</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,419,552</td>
<td align="right">635,149</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">178,551,511</td>
<td align="right">80,085,122</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">182,862,020</td>
<td align="right">85,966,227</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,323,663</td>
<td align="right">48,680,700</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">733,649,077</td>
<td align="right">347,068,672</td>
<td align="right">-52.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">224,007</td>
<td align="right">108,239</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">525,480,978</td>
<td align="right">258,566,247</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">226,426,021</td>
<td align="right">111,748,885</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">474,369,545</td>
<td align="right">234,464,906</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">255,207,852</td>
<td align="right">131,075,599</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,643,979,302</td>
<td align="right">1,895,272,487</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,629,760,470</td>
<td align="right">2,433,932,830</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">187,856,852</td>
<td align="right">99,877,947</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">203,724,397</td>
<td align="right">108,701,312</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">340,692,953</td>
<td align="right">184,997,488</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,777,894,577</td>
<td align="right">2,103,603,631</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,558,824</td>
<td align="right">32,230,907</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">52,704,415</td>
<td align="right">29,940,978</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,614,254,290</td>
<td align="right">1,496,652,022</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,706,676,774</td>
<td align="right">2,131,583,547</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,372,096,510</td>
<td align="right">797,682,533</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">78,591,655</td>
<td align="right">45,908,606</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">135,281,115</td>
<td align="right">80,103,673</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">88,069,983</td>
<td align="right">52,251,428</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">85,127,967</td>
<td align="right">50,622,787</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,334,424,505</td>
<td align="right">2,578,947,462</td>
<td align="right">-40.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,251,014</td>
<td align="right">22,481,752</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,034,244</td>
<td align="right">21,275,430</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,411,926,233</td>
<td align="right">1,480,852,715</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">15,592,928,677</td>
<td align="right">9,593,415,313</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,636,240,538</td>
<td align="right">1,006,917,697</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,826,826,040</td>
<td align="right">1,135,941,652</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">562,528,781</td>
<td align="right">355,580,845</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">370,559,846</td>
<td align="right">235,265,049</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">154,270,242</td>
<td align="right">98,134,992</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,973,118,292</td>
<td align="right">1,270,095,089</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">65,676,271</td>
<td align="right">42,356,192</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">190,830,471</td>
<td align="right">123,796,411</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">528,859,441</td>
<td align="right">345,293,295</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">348,929,787</td>
<td align="right">229,751,868</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">137,085,052</td>
<td align="right">91,520,267</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,470</td>
<td align="right">115,870</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">99,173,424</td>
<td align="right">67,213,106</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,088,467</td>
<td align="right">15,099,910</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">170,740,817</td>
<td align="right">117,349,059</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">74,062,926</td>
<td align="right">51,043,817</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">153,076,055</td>
<td align="right">107,258,438</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">58,873,294</td>
<td align="right">41,725,410</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">33,173,255</td>
<td align="right">23,570,622</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,744,106</td>
<td align="right">2,663,215</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">33,835,153</td>
<td align="right">24,174,697</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">91,866,985</td>
<td align="right">66,240,652</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">951,446,591</td>
<td align="right">687,316,161</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">197,213,586</td>
<td align="right">143,264,366</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,215,258,838</td>
<td align="right">1,609,342,048</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">822,173,045</td>
<td align="right">602,610,609</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">457,084,498</td>
<td align="right">335,463,095</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">207,686,382</td>
<td align="right">152,698,309</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">36,668,601</td>
<td align="right">26,965,363</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">8,530,886</td>
<td align="right">6,277,619</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">134,320,418</td>
<td align="right">98,899,925</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,430,073,494</td>
<td align="right">1,799,696,728</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">141,987,269</td>
<td align="right">105,499,056</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,348,190,925</td>
<td align="right">1,006,264,265</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">53,710,832</td>
<td align="right">40,324,087</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,489,413</td>
<td align="right">53,855,758</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">806,281,916</td>
<td align="right">609,539,867</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,995,982</td>
<td align="right">8,354,990</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">525,287</td>
<td align="right">400,226</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">52,159,512</td>
<td align="right">40,062,397</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,859,343,325</td>
<td align="right">2,202,406,453</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">58,580</td>
<td align="right">45,182</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">551,620</td>
<td align="right">428,120</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">556,842,266</td>
<td align="right">436,801,219</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,031,285,831</td>
<td align="right">814,453,991</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">260,960,041</td>
<td align="right">206,312,157</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">93,340,658</td>
<td align="right">74,167,493</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">189,687,578</td>
<td align="right">151,295,698</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">618,272,599</td>
<td align="right">493,581,222</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">522,935,351</td>
<td align="right">418,855,500</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,596,128,128</td>
<td align="right">3,708,837,762</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">355,320,855</td>
<td align="right">287,531,259</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">276,932,946</td>
<td align="right">224,481,169</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">365,127,701</td>
<td align="right">299,242,855</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">60,308,098</td>
<td align="right">49,445,197</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,732,605</td>
<td align="right">7,260,003</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">720,751</td>
<td align="right">609,527</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">410,179,948</td>
<td align="right">348,031,073</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">331,693,283</td>
<td align="right">292,150,404</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">44,848,991</td>
<td align="right">39,719,879</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,340,743</td>
<td align="right">9,194,443</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,104,162</td>
<td align="right">357,896,122</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,564,525</td>
<td align="right">361,239,607</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,603,414</td>
<td align="right">3,256,173</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,768,286</td>
<td align="right">16,960,839</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">150,193,462</td>
<td align="right">137,472,956</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,422,676</td>
<td align="right">9,730,447</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">120,698,504</td>
<td align="right">112,726,118</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,258,213</td>
<td align="right">10,566,551</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">14,953,270</td>
<td align="right">14,043,022</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">147,000,844</td>
<td align="right">140,024,509</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">64,986,063</td>
<td align="right">62,814,988</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,945,743</td>
<td align="right">2,857,968</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,387,074</td>
<td align="right">20,755,069</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,053,113,336</td>
<td align="right">1,030,382,993</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,037,959</td>
<td align="right">8,843,273</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">221,400,401</td>
<td align="right">218,239,094</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">763,776</td>
<td align="right">754,576</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">71,261,716</td>
<td align="right">70,680,538</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">16,246,056</td>
<td align="right">16,140,776</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,288</td>
<td align="right">3,451,828</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,166,081</td>
<td align="right">267,846,253</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,259,182,194</td>
<td align="right">2,258,328,145</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,586,959</td>
<td align="right">3,586,397</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,167</td>
<td align="right">15,168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">66,760</td>
<td align="right">66,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">268,685</td>
<td align="right">268,691</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">102,115,621</td>
<td align="right">102,117,015</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,259,182</td>
<td align="right">1,259,196</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">70,944,737</td>
<td align="right">70,944,281</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,395,415</td>
<td align="right">21,395,328</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,407,121</td>
<td align="right">198,407,616</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,081,104</td>
<td align="right">21,081,066</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,353,558</td>
<td align="right">20,353,543</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,399,214</td>
<td align="right">173,399,214</td>
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
<td align="right">8,000,960</td>
<td align="right">8,000,960</td>
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
<td align="left">RAISE_VARARGS</td>
<td align="right">5,830,247</td>
<td align="right">5,830,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">651,872</td>
<td align="right">651,872</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">157,711</td>
<td align="right">157,711</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">29,709</td>
<td align="right">29,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,806</td>
<td align="right">27,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,856</td>
<td align="right">21,856</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16,120</td>
<td align="right">16,120</td>
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
<td align="right">1,062</td>
<td align="right">1,062</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">423</td>
<td align="right">423</td>
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
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">140</td>
<td align="right">140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">369,401,569</td>
<td align="right">3.8%</td>
<td align="right">234,249,392</td>
<td align="right">2.4%</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,480,870</td>
<td align="right">0.3%</td>
<td align="right">20,104,990</td>
<td align="right">0.2%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,403,446,726</td>
<td align="right">95.9%</td>
<td align="right">9,357,321,728</td>
<td align="right">97.3%</td>
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
<td align="right">598,065</td>
<td align="right">34.9%</td>
<td align="right">421,193</td>
<td align="right">30.2%</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,116,292</td>
<td align="right">65.1%</td>
<td align="right">973,684</td>
<td align="right">69.8%</td>
<td align="right">-12.8%</td>
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
<td align="right">49,299</td>
<td align="right">4.4%</td>
<td align="right">21,484</td>
<td align="right">2.2%</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">47,061</td>
<td align="right">4.2%</td>
<td align="right">28,034</td>
<td align="right">2.9%</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,923</td>
<td align="right">7.3%</td>
<td align="right">53,861</td>
<td align="right">5.5%</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,830</td>
<td align="right">0.3%</td>
<td align="right">1,870</td>
<td align="right">0.2%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,620</td>
<td align="right">0.5%</td>
<td align="right">3,776</td>
<td align="right">0.4%</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">8,249</td>
<td align="right">0.7%</td>
<td align="right">5,631</td>
<td align="right">0.6%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,742</td>
<td align="right">0.9%</td>
<td align="right">6,812</td>
<td align="right">0.7%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">401</td>
<td align="right">0.0%</td>
<td align="right">301</td>
<td align="right">0.0%</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,395</td>
<td align="right">1.3%</td>
<td align="right">10,851</td>
<td align="right">1.1%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">6,805</td>
<td align="right">0.6%</td>
<td align="right">5,565</td>
<td align="right">0.6%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,963</td>
<td align="right">0.3%</td>
<td align="right">2,583</td>
<td align="right">0.3%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,272</td>
<td align="right">2.8%</td>
<td align="right">27,705</td>
<td align="right">2.8%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,471</td>
<td align="right">0.8%</td>
<td align="right">7,649</td>
<td align="right">0.8%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,805</td>
<td align="right">1.0%</td>
<td align="right">10,069</td>
<td align="right">1.0%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,608</td>
<td align="right">70.0%</td>
<td align="right">733,891</td>
<td align="right">75.4%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,580</td>
<td align="right">0.2%</td>
<td align="right">2,439</td>
<td align="right">0.3%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">20,124</td>
<td align="right">1.8%</td>
<td align="right">19,339</td>
<td align="right">2.0%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">31,310</td>
<td align="right">2.8%</td>
<td align="right">30,990</td>
<td align="right">3.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">834</td>
<td align="right">0.1%</td>
<td align="right">834</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


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
<td align="right">474,099,725</td>
<td align="right">7.1%</td>
<td align="right">234,258,888</td>
<td align="right">3.6%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,792,351</td>
<td align="right">0.1%</td>
<td align="right">4,789,909</td>
<td align="right">0.1%</td>
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
<td align="right">6,201,993,890</td>
<td align="right">92.8%</td>
<td align="right">6,201,779,301</td>
<td align="right">96.3%</td>
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
<td align="right">178,219</td>
<td align="right">49.5%</td>
<td align="right">114,477</td>
<td align="right">38.7%</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,562</td>
<td align="right">50.5%</td>
<td align="right">181,476</td>
<td align="right">61.3%</td>
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
<td align="right">26,640</td>
<td align="right">14.9%</td>
<td align="right">3,580</td>
<td align="right">3.1%</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,330</td>
<td align="right">12.0%</td>
<td align="right">10,309</td>
<td align="right">9.0%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">58,326</td>
<td align="right">32.7%</td>
<td align="right">30,506</td>
<td align="right">26.6%</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">320</td>
<td align="right">0.2%</td>
<td align="right">220</td>
<td align="right">0.2%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">700</td>
<td align="right">0.6%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">65,338</td>
<td align="right">36.7%</td>
<td align="right">63,717</td>
<td align="right">55.7%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">940</td>
<td align="right">0.5%</td>
<td align="right">920</td>
<td align="right">0.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">2.4%</td>
<td align="right">4,300</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">125</td>
<td align="right">0.1%</td>
<td align="right">125</td>
<td align="right">0.1%</td>
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
<td align="right">150,934,445</td>
<td align="right">1.1%</td>
<td align="right">121,655,824</td>
<td align="right">0.9%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,060</td>
<td align="right">0.0%</td>
<td align="right">30,680</td>
<td align="right">0.0%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,498,584,766</td>
<td align="right">98.9%</td>
<td align="right">13,533,340,441</td>
<td align="right">99.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">716,679</td>
<td align="right">0.0%</td>
<td align="right">716,684</td>
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
<td align="right">3,422,578</td>
<td align="right">100.0%</td>
<td align="right">2,868,079</td>
<td align="right">100.0%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">363</td>
<td align="right">0.0%</td>
<td align="right">363</td>
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
<td align="right">779.3%</td>
<td align="right">2,829</td>
<td align="right">779.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,003</td>
<td align="right">551.8%</td>
<td align="right">2,003</td>
<td align="right">551.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">921</td>
<td align="right">253.7%</td>
<td align="right">921</td>
<td align="right">253.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">363</td>
<td align="right">100.0%</td>
<td align="right">363</td>
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
<td align="right">435,240</td>
<td align="right">86.7%</td>
<td align="right">304,880</td>
<td align="right">82.0%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,415</td>
<td align="right">7.3%</td>
<td align="right">36,415</td>
<td align="right">9.8%</td>
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
<td align="right">103,107,638</td>
<td align="right">1.8%</td>
<td align="right">48,511,195</td>
<td align="right">0.8%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,249,139</td>
<td align="right">0.0%</td>
<td align="right">610,645</td>
<td align="right">0.0%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,722,094,276</td>
<td align="right">98.2%</td>
<td align="right">5,720,361,731</td>
<td align="right">99.1%</td>
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
<td align="right">160,993</td>
<td align="right">67.3%</td>
<td align="right">114,659</td>
<td align="right">63.4%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">78,249</td>
<td align="right">32.7%</td>
<td align="right">66,080</td>
<td align="right">36.6%</td>
<td align="right">-15.6%</td>
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
<td align="right">6.6%</td>
<td align="right">1,480</td>
<td align="right">1.3%</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">29,783</td>
<td align="right">18.5%</td>
<td align="right">10,787</td>
<td align="right">9.4%</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,060</td>
<td align="right">1.9%</td>
<td align="right">1,700</td>
<td align="right">1.5%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,524</td>
<td align="right">9.0%</td>
<td align="right">9,201</td>
<td align="right">8.0%</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,720</td>
<td align="right">1.7%</td>
<td align="right">1,920</td>
<td align="right">1.7%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,189</td>
<td align="right">11.9%</td>
<td align="right">15,089</td>
<td align="right">13.2%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,439</td>
<td align="right">10.8%</td>
<td align="right">15,092</td>
<td align="right">13.2%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,086</td>
<td align="right">7.5%</td>
<td align="right">10,867</td>
<td align="right">9.5%</td>
<td align="right">-10.1%</td>
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
<td align="left">different types</td>
<td align="right">48,512</td>
<td align="right">30.1%</td>
<td align="right">45,603</td>
<td align="right">39.8%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,550</td>
<td align="right">1.0%</td>
<td align="right">1,510</td>
<td align="right">1.3%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">960</td>
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
<td align="right">2,546,180</td>
<td align="right">0.1%</td>
<td align="right">1,368,680</td>
<td align="right">0.1%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">36,584,086</td>
<td align="right">1.4%</td>
<td align="right">26,889,413</td>
<td align="right">1.1%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,486,718,666</td>
<td align="right">98.4%</td>
<td align="right">2,486,941,232</td>
<td align="right">98.9%</td>
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
<td align="right">61,139</td>
<td align="right">46.2%</td>
<td align="right">38,939</td>
<td align="right">38.3%</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">71,336</td>
<td align="right">53.8%</td>
<td align="right">62,771</td>
<td align="right">61.7%</td>
<td align="right">-12.0%</td>
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
<td align="right">14,470</td>
<td align="right">20.3%</td>
<td align="right">12,004</td>
<td align="right">19.1%</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,578</td>
<td align="right">38.7%</td>
<td align="right">23,596</td>
<td align="right">37.6%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,306</td>
<td align="right">21.5%</td>
<td align="right">13,809</td>
<td align="right">22.0%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">13,982</td>
<td align="right">19.6%</td>
<td align="right">13,362</td>
<td align="right">21.3%</td>
<td align="right">-4.4%</td>
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
<td align="right">6,746,723</td>
<td align="right">1.1%</td>
<td align="right">4,618,665</td>
<td align="right">1.1%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">73,913,641</td>
<td align="right">12.0%</td>
<td align="right">50,903,346</td>
<td align="right">11.6%</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">534,037,689</td>
<td align="right">86.9%</td>
<td align="right">382,580,228</td>
<td align="right">87.3%</td>
<td align="right">-28.4%</td>
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
<td align="right">175,722</td>
<td align="right">63.6%</td>
<td align="right">135,513</td>
<td align="right">59.6%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">100,558</td>
<td align="right">36.4%</td>
<td align="right">91,851</td>
<td align="right">40.4%</td>
<td align="right">-8.7%</td>
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
<td align="right">2,467</td>
<td align="right">2.5%</td>
<td align="right">1,527</td>
<td align="right">1.7%</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,602</td>
<td align="right">7.6%</td>
<td align="right">5,122</td>
<td align="right">5.6%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">2,724</td>
<td align="right">2.7%</td>
<td align="right">2,484</td>
<td align="right">2.7%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,071</td>
<td align="right">11.0%</td>
<td align="right">10,101</td>
<td align="right">11.0%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,775</td>
<td align="right">36.6%</td>
<td align="right">33,642</td>
<td align="right">36.6%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">10,798</td>
<td align="right">10.7%</td>
<td align="right">10,295</td>
<td align="right">11.2%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,565</td>
<td align="right">6.5%</td>
<td align="right">6,345</td>
<td align="right">6.9%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,222</td>
<td align="right">5.2%</td>
<td align="right">5,122</td>
<td align="right">5.6%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,956</td>
<td align="right">4.9%</td>
<td align="right">4,876</td>
<td align="right">5.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,737</td>
<td align="right">6.7%</td>
<td align="right">6,697</td>
<td align="right">7.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,981</td>
<td align="right">4.0%</td>
<td align="right">3,980</td>
<td align="right">4.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">740</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">620</td>
<td align="right">0.6%</td>
<td align="right">620</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.3%</td>
<td align="right">280</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
<td align="right">558,709,619</td>
<td align="right">3.4%</td>
<td align="right">352,075,669</td>
<td align="right">2.2%</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">341,162,049</td>
<td align="right">2.1%</td>
<td align="right">262,465,390</td>
<td align="right">1.6%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,288,800</td>
<td align="right">0.0%</td>
<td align="right">1,189,100</td>
<td align="right">0.0%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,374,610,351</td>
<td align="right">94.4%</td>
<td align="right">15,305,688,598</td>
<td align="right">96.1%</td>
<td align="right">-0.4%</td>
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
<td align="right">9,748,220</td>
<td align="right">95.4%</td>
<td align="right">8,015,711</td>
<td align="right">95.2%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">473,308</td>
<td align="right">4.6%</td>
<td align="right">408,460</td>
<td align="right">4.8%</td>
<td align="right">-13.7%</td>
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
<td align="right">88,006</td>
<td align="right">18.6%</td>
<td align="right">62,407</td>
<td align="right">15.3%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,992</td>
<td align="right">3.8%</td>
<td align="right">13,878</td>
<td align="right">3.4%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">32,253</td>
<td align="right">6.8%</td>
<td align="right">26,918</td>
<td align="right">6.6%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,964</td>
<td align="right">0.6%</td>
<td align="right">2,484</td>
<td align="right">0.6%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">11,000</td>
<td align="right">2.3%</td>
<td align="right">9,300</td>
<td align="right">2.3%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">31,279</td>
<td align="right">6.6%</td>
<td align="right">26,933</td>
<td align="right">6.6%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">84,351</td>
<td align="right">17.8%</td>
<td align="right">73,940</td>
<td align="right">18.1%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">15,331</td>
<td align="right">3.2%</td>
<td align="right">13,975</td>
<td align="right">3.4%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.2%</td>
<td align="right">1,040</td>
<td align="right">0.3%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">5,300</td>
<td align="right">1.1%</td>
<td align="right">4,860</td>
<td align="right">1.2%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">20,880</td>
<td align="right">4.4%</td>
<td align="right">19,440</td>
<td align="right">4.8%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">138,634</td>
<td align="right">29.3%</td>
<td align="right">129,372</td>
<td align="right">31.7%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">2,755</td>
<td align="right">0.6%</td>
<td align="right">2,675</td>
<td align="right">0.7%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,425</td>
<td align="right">1.1%</td>
<td align="right">5,385</td>
<td align="right">1.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2,543</td>
<td align="right">0.5%</td>
<td align="right">2,543</td>
<td align="right">0.6%</td>
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
<tr>
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">4,492,950,151</td>
<td align="right">99.5%</td>
<td align="right">2,773,297,000</td>
<td align="right">99.3%</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">394,374</td>
<td align="right">0.0%</td>
<td align="right">394,135</td>
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
<td align="right">19,893,761</td>
<td align="right">0.4%</td>
<td align="right">19,893,753</td>
<td align="right">0.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,236</td>
<td align="right">0.0%</td>
<td align="right">9,236</td>
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
<td align="right">465,604</td>
<td align="right">100.0%</td>
<td align="right">465,614</td>
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
<td align="right">86,169,022</td>
<td align="right">100.0%</td>
<td align="right">86,124,371</td>
<td align="right">100.0%</td>
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
<td align="right">7,626</td>
<td align="right">0.0%</td>
<td align="right">7,627</td>
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
<td align="right">7,541</td>
<td align="right">100.0%</td>
<td align="right">7,541</td>
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

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NONE family </summary>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NOT_NONE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


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
<td align="right">786,232,550</td>
<td align="right">81.9%</td>
<td align="right">786,232,582</td>
<td align="right">81.9%</td>
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
<td align="right">173,334,483</td>
<td align="right">18.1%</td>
<td align="right">173,334,483</td>
<td align="right">18.1%</td>
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
<td align="right">30,643</td>
<td align="right">0.0%</td>
<td align="right">30,643</td>
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
<td align="right">59,734</td>
<td align="right">91.5%</td>
<td align="right">59,734</td>
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
<td align="right">55.5%</td>
<td align="right">33,180</td>
<td align="right">55.5%</td>
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
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">2,260</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">44,667,152</td>
<td align="right">1.7%</td>
<td align="right">39,543,340</td>
<td align="right">1.5%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">111,394,440</td>
<td align="right">4.3%</td>
<td align="right">101,116,558</td>
<td align="right">3.9%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,463,383,025</td>
<td align="right">94.0%</td>
<td align="right">2,468,919,136</td>
<td align="right">94.6%</td>
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
<td align="right">2,204,796</td>
<td align="right">96.7%</td>
<td align="right">2,010,932</td>
<td align="right">96.6%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">76,051</td>
<td align="right">3.3%</td>
<td align="right">70,751</td>
<td align="right">3.4%</td>
<td align="right">-7.0%</td>
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
<td align="right">3,185</td>
<td align="right">4.2%</td>
<td align="right">2,765</td>
<td align="right">3.9%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">31,884</td>
<td align="right">41.9%</td>
<td align="right">27,724</td>
<td align="right">39.2%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,383</td>
<td align="right">11.0%</td>
<td align="right">7,723</td>
<td align="right">10.9%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,439</td>
<td align="right">8.5%</td>
<td align="right">6,379</td>
<td align="right">9.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,776</td>
<td align="right">12.9%</td>
<td align="right">9,776</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,505</td>
<td align="right">9.9%</td>
<td align="right">7,505</td>
<td align="right">10.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,075</td>
<td align="right">6.7%</td>
<td align="right">5,075</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">2,160</td>
<td align="right">2.8%</td>
<td align="right">2,160</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">804</td>
<td align="right">1.1%</td>
<td align="right">804</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">780</td>
<td align="right">1.0%</td>
<td align="right">780</td>
<td align="right">1.1%</td>
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
<td align="right">93,337,109</td>
<td align="right">9.6%</td>
<td align="right">20,335,716</td>
<td align="right">2.3%</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">875,265,881</td>
<td align="right">90.4%</td>
<td align="right">875,181,845</td>
<td align="right">97.7%</td>
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
<td align="right">66,905</td>
<td align="right">83.3%</td>
<td align="right">40,774</td>
<td align="right">75.3%</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,370</td>
<td align="right">16.7%</td>
<td align="right">13,372</td>
<td align="right">24.7%</td>
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
<td align="left">array int</td>
<td align="right">14,280</td>
<td align="right">21.3%</td>
<td align="right">6,100</td>
<td align="right">15.0%</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">42,263</td>
<td align="right">63.2%</td>
<td align="right">25,023</td>
<td align="right">61.4%</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">640</td>
<td align="right">1.0%</td>
<td align="right">560</td>
<td align="right">1.4%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,520</td>
<td align="right">2.3%</td>
<td align="right">1,400</td>
<td align="right">3.4%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">6,722</td>
<td align="right">10.0%</td>
<td align="right">6,251</td>
<td align="right">15.3%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,480</td>
<td align="right">2.2%</td>
<td align="right">1,440</td>
<td align="right">3.5%</td>
<td align="right">-2.7%</td>
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
<td align="right">158,042,552</td>
<td align="right">2.7%</td>
<td align="right">61,638,923</td>
<td align="right">1.1%</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,569,146</td>
<td align="right">0.4%</td>
<td align="right">17,119,596</td>
<td align="right">0.3%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,761,506,622</td>
<td align="right">96.9%</td>
<td align="right">5,568,034,456</td>
<td align="right">98.6%</td>
<td align="right">-3.4%</td>
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
<td align="right">210,520</td>
<td align="right">24.3%</td>
<td align="right">148,711</td>
<td align="right">22.4%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">656,479</td>
<td align="right">75.7%</td>
<td align="right">516,340</td>
<td align="right">77.6%</td>
<td align="right">-21.3%</td>
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
<td align="right">37,227</td>
<td align="right">17.7%</td>
<td align="right">7,248</td>
<td align="right">4.9%</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">19,076</td>
<td align="right">9.1%</td>
<td align="right">6,882</td>
<td align="right">4.6%</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,145</td>
<td align="right">7.7%</td>
<td align="right">10,305</td>
<td align="right">6.9%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,749</td>
<td align="right">0.8%</td>
<td align="right">1,207</td>
<td align="right">0.8%</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,009</td>
<td align="right">2.9%</td>
<td align="right">4,900</td>
<td align="right">3.3%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">14,911</td>
<td align="right">7.1%</td>
<td align="right">12,710</td>
<td align="right">8.5%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">7,332</td>
<td align="right">3.5%</td>
<td align="right">6,340</td>
<td align="right">4.3%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">82,867</td>
<td align="right">39.4%</td>
<td align="right">74,406</td>
<td align="right">50.0%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">683</td>
<td align="right">0.3%</td>
<td align="right">668</td>
<td align="right">0.4%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">24,181</td>
<td align="right">11.5%</td>
<td align="right">23,705</td>
<td align="right">15.9%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
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
<td align="right">191,651</td>
<td align="right">0.0%</td>
<td align="right">75,999</td>
<td align="right">0.0%</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,529,565,662</td>
<td align="right">100.0%</td>
<td align="right">1,354,987,647</td>
<td align="right">100.0%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">3,080</td>
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
<td align="right">1,861</td>
<td align="right">5.7%</td>
<td align="right">1,743</td>
<td align="right">5.4%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,535</td>
<td align="right">94.3%</td>
<td align="right">30,537</td>
<td align="right">94.6%</td>
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
<td align="right">20.4%</td>
<td align="right">260</td>
<td align="right">14.9%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,214</td>
<td align="right">65.2%</td>
<td align="right">1,216</td>
<td align="right">69.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">267</td>
<td align="right">14.3%</td>
<td align="right">267</td>
<td align="right">15.3%</td>
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
<td align="right">7,550,697,959</td>
<td align="right">8.5%</td>
<td align="right">4,520,015,307</td>
<td align="right">7.9%</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">50,587,976,422</td>
<td align="right">56.7%</td>
<td align="right">31,881,792,186</td>
<td align="right">56.0%</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">30,485,411,275</td>
<td align="right">34.1%</td>
<td align="right">20,003,347,626</td>
<td align="right">35.1%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">673,946,986</td>
<td align="right">0.8%</td>
<td align="right">534,790,830</td>
<td align="right">0.9%</td>
<td align="right">-20.6%</td>
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
<td align="right">93,337,109</td>
<td align="right">4.4%</td>
<td align="right">20,335,716</td>
<td align="right">1.6%</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">158,042,552</td>
<td align="right">7.5%</td>
<td align="right">61,638,923</td>
<td align="right">4.9%</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,107,638</td>
<td align="right">4.9%</td>
<td align="right">48,511,195</td>
<td align="right">3.8%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">474,099,725</td>
<td align="right">22.5%</td>
<td align="right">234,258,888</td>
<td align="right">18.6%</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">558,709,619</td>
<td align="right">26.5%</td>
<td align="right">352,075,669</td>
<td align="right">27.9%</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">369,401,569</td>
<td align="right">17.5%</td>
<td align="right">234,249,392</td>
<td align="right">18.6%</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">73,913,641</td>
<td align="right">3.5%</td>
<td align="right">50,903,346</td>
<td align="right">4.0%</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">36,584,086</td>
<td align="right">1.7%</td>
<td align="right">26,889,413</td>
<td align="right">2.1%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">44,667,152</td>
<td align="right">2.1%</td>
<td align="right">39,543,340</td>
<td align="right">3.1%</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,334,483</td>
<td align="right">8.2%</td>
<td align="right">173,334,483</td>
<td align="right">13.7%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">38,012,121</td>
<td align="right">5.6%</td>
<td align="right">18,933,036</td>
<td align="right">3.5%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,508,653</td>
<td align="right">6.0%</td>
<td align="right">27,362,546</td>
<td align="right">5.1%</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">80,483,460</td>
<td align="right">11.9%</td>
<td align="right">58,827,941</td>
<td align="right">11.0%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">89,298,741</td>
<td align="right">13.2%</td>
<td align="right">70,315,424</td>
<td align="right">13.1%</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">23,851,898</td>
<td align="right">3.5%</td>
<td align="right">18,813,246</td>
<td align="right">3.5%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">134,218,764</td>
<td align="right">19.9%</td>
<td align="right">115,174,344</td>
<td align="right">21.5%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,177,240</td>
<td align="right">3.0%</td>
<td align="right">18,121,080</td>
<td align="right">3.4%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">87,518,876</td>
<td align="right">13.0%</td>
<td align="right">82,284,310</td>
<td align="right">15.4%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,105,372</td>
<td align="right">2.7%</td>
<td align="right">17,727,675</td>
<td align="right">3.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,497,345</td>
<td align="right">4.1%</td>
<td align="right">27,497,457</td>
<td align="right">5.1%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">333,949,713</td>
<td align="right">4.0%</td>
<td align="right">333,388,720</td>
<td align="right">4.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">851,984,507</td>
<td align="right">10.1%</td>
<td align="right">851,611,818</td>
<td align="right">10.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,644,565</td>
<td align="right">3.9%</td>
<td align="right">331,782,123</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,262,999,398</td>
<td align="right">26.8%</td>
<td align="right">2,262,144,789</td>
<td align="right">26.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,262,999,398</td>
<td align="right">26.8%</td>
<td align="right">2,262,144,789</td>
<td align="right">26.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,406,566,490</td>
<td align="right">16.7%</td>
<td align="right">1,406,084,570</td>
<td align="right">16.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,411,014,891</td>
<td align="right">16.7%</td>
<td align="right">1,410,532,971</td>
<td align="right">16.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,680,527,455</td>
<td align="right">79.2%</td>
<td align="right">6,680,063,905</td>
<td align="right">79.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,755,923</td>
<td align="right">1.0%</td>
<td align="right">84,754,595</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,168,181,787</td>
<td align="right">73.2%</td>
<td align="right">6,168,200,722</td>
<td align="right">73.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,097,811</td>
<td align="right">0.4%</td>
<td align="right">31,097,881</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,501</td>
<td align="right">2.1%</td>
<td align="right">175,480,527</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,418,272</td>
<td align="right">0.1%</td>
<td align="right">4,418,272</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">30,129</td>
<td align="right">0.0%</td>
<td align="right">30,129</td>
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
<td align="left">Interpreter increfs</td>
<td align="right">41,210,052,013</td>
<td align="right">29.9%</td>
<td align="right">27,769,851,432</td>
<td align="right">19.9%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">56,365,676,905</td>
<td align="right">35.2%</td>
<td align="right">46,089,541,695</td>
<td align="right">28.4%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">96,509,508,823</td>
<td align="right">70.1%</td>
<td align="right">111,606,996,511</td>
<td align="right">80.1%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">103,859,174,619</td>
<td align="right">64.8%</td>
<td align="right">115,997,931,439</td>
<td align="right">71.6%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,600,348</td>
<td align="right"></td>
<td align="right">7,286,125</td>
<td align="right"></td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,543,478,346</td>
<td align="right"></td>
<td align="right">2,494,512,786</td>
<td align="right"></td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">68,609,788</td>
<td align="right"></td>
<td align="right">67,609,561</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,773,781,686</td>
<td align="right">52.1%</td>
<td align="right">12,947,814,364</td>
<td align="right">52.4%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,882,111,556</td>
<td align="right">52.5%</td>
<td align="right">13,056,209,865</td>
<td align="right">52.8%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,582,829,430</td>
<td align="right"></td>
<td align="right">13,757,734,019</td>
<td align="right"></td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">62,000,011</td>
<td align="right"></td>
<td align="right">61,317,590</td>
<td align="right"></td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,635,338,910</td>
<td align="right"></td>
<td align="right">11,665,158,301</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,633,462,021</td>
<td align="right">47.5%</td>
<td align="right">11,663,249,752</td>
<td align="right">47.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,711,387,511</td>
<td align="right"></td>
<td align="right">3,704,961,204</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">92,968,938</td>
<td align="right">0.4%</td>
<td align="right">93,028,709</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">15,360,932</td>
<td align="right">0.1%</td>
<td align="right">15,366,792</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">235,988,948</td>
<td align="right"></td>
<td align="right">235,963,377</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,300</td>
<td align="right">1.4%</td>
<td align="right">3,382,300</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">240,283</td>
<td align="right">0.1%</td>
<td align="right">240,283</td>
<td align="right">0.1%</td>
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
<td align="right">112,267,788</td>
<td align="right">19,369,638,285</td>
<td align="right">0</td>
<td align="right">112,778,123</td>
<td align="right">19,357,910,842</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,644,844</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,700,792</td>
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
<td align="right">1,899</td>
<td align="right">0.2%</td>
<td align="right">4,725</td>
<td align="right">0.8%</td>
<td align="right">148.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">649,917</td>
<td align="right">72.6%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
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
<td align="right">177,313</td>
<td align="right">19.8%</td>
<td align="right">285,807</td>
<td align="right">47.1%</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">8,280</td>
<td align="right">4.7%</td>
<td align="right">13,021</td>
<td align="right">4.6%</td>
<td align="right">57.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">715,606</td>
<td align="right">80.0%</td>
<td align="right">316,453</td>
<td align="right">52.1%</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">894,818</td>
<td align="right"></td>
<td align="right">606,985</td>
<td align="right"></td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">12,084</td>
<td align="right">1.4%</td>
<td align="right">15,713</td>
<td align="right">2.6%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">9,432,209,759</td>
<td align="right"></td>
<td align="right">11,692,155,853</td>
<td align="right"></td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">301,300,380,982</td>
<td align="right">3,194.4%</td>
<td align="right">359,072,417,278</td>
<td align="right">3,071.1%</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,002</td>
<td align="right">0.1%</td>
<td align="right">1,149</td>
<td align="right">0.2%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,581</td>
<td align="right">0.4%</td>
<td align="right">4,062</td>
<td align="right">0.7%</td>
<td align="right">13.4%</td>
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
<td align="right">165,554</td>
<td align="right">93.4%</td>
<td align="right">273,125</td>
<td align="right">95.6%</td>
<td align="right">65.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">177,313</td>
<td align="right"></td>
<td align="right">285,807</td>
<td align="right"></td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,600</td>
<td align="right">1.5%</td>
<td align="right">3,066</td>
<td align="right">1.1%</td>
<td align="right">17.9%</td>
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
<td align="right">3,694</td>
<td align="right">2.1%</td>
<td align="right">7,300</td>
<td align="right">2.6%</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">22,781</td>
<td align="right">12.8%</td>
<td align="right">32,738</td>
<td align="right">11.5%</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20,875</td>
<td align="right">11.8%</td>
<td align="right">42,032</td>
<td align="right">14.7%</td>
<td align="right">101.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">47,871</td>
<td align="right">27.0%</td>
<td align="right">76,641</td>
<td align="right">26.8%</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">40,521</td>
<td align="right">22.9%</td>
<td align="right">61,839</td>
<td align="right">21.6%</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">23,867</td>
<td align="right">13.5%</td>
<td align="right">37,171</td>
<td align="right">13.0%</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">14,544</td>
<td align="right">8.2%</td>
<td align="right">22,753</td>
<td align="right">8.0%</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,800</td>
<td align="right">1.6%</td>
<td align="right">4,793</td>
<td align="right">1.7%</td>
<td align="right">71.2%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">360</td>
<td align="right">0.2%</td>
<td align="right">540</td>
<td align="right">0.2%</td>
<td align="right">50.0%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">20,030</td>
<td align="right">11.3%</td>
<td align="right">13,831</td>
<td align="right">4.8%</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,551</td>
<td align="right">9.3%</td>
<td align="right">44,055</td>
<td align="right">15.4%</td>
<td align="right">166.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">30,531</td>
<td align="right">17.2%</td>
<td align="right">57,652</td>
<td align="right">20.2%</td>
<td align="right">88.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">50,136</td>
<td align="right">28.3%</td>
<td align="right">76,525</td>
<td align="right">26.8%</td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">29,412</td>
<td align="right">16.6%</td>
<td align="right">47,348</td>
<td align="right">16.6%</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,514</td>
<td align="right">7.6%</td>
<td align="right">21,621</td>
<td align="right">7.6%</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,660</td>
<td align="right">2.6%</td>
<td align="right">11,042</td>
<td align="right">3.9%</td>
<td align="right">137.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">700</td>
<td align="right">0.4%</td>
<td align="right">1,031</td>
<td align="right">0.4%</td>
<td align="right">47.3%</td>
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
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,885</td>
<td align="right">175,808,514</td>
<td align="right">11,287.4%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">640,118</td>
<td align="right">7,706.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">10,164</td>
<td align="right">121,400</td>
<td align="right">1,094.4%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,468,651</td>
<td align="right">59,893,813</td>
<td align="right">825.9%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">4,785,180</td>
<td align="right">40,205,673</td>
<td align="right">740.2%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">5,709,160</td>
<td align="right">42,197,373</td>
<td align="right">639.1%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,942,620</td>
<td align="right">20,576,275</td>
<td align="right">599.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">6,776,827</td>
<td align="right">42,595,424</td>
<td align="right">528.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,084,240</td>
<td align="right">12,944,325</td>
<td align="right">521.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">60,921,091</td>
<td align="right">283,836,087</td>
<td align="right">365.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">936,365,537</td>
<td align="right">3,760,509,638</td>
<td align="right">301.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,431,296</td>
<td align="right">37,445,396</td>
<td align="right">297.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">937,895</td>
<td align="right">3,184,776</td>
<td align="right">239.6%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,076,388,923</td>
<td align="right">3,341,923,012</td>
<td align="right">210.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,994,660</td>
<td align="right">6,070,999</td>
<td align="right">204.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">370,525</td>
<td align="right">1,063,695</td>
<td align="right">187.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,275,764</td>
<td align="right">155,045,878</td>
<td align="right">185.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,280,004</td>
<td align="right">155,057,298</td>
<td align="right">185.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,241,400</td>
<td align="right">5,962,737</td>
<td align="right">166.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,640,211</td>
<td align="right">6,550,728</td>
<td align="right">148.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">12,712,504</td>
<td align="right">29,530,530</td>
<td align="right">132.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">204,905,296</td>
<td align="right">470,016,566</td>
<td align="right">129.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">49,870,456</td>
<td align="right">104,713,145</td>
<td align="right">110.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">51,304,796</td>
<td align="right">106,311,186</td>
<td align="right">107.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">49,699,380</td>
<td align="right">100,463,473</td>
<td align="right">102.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">32,293,752</td>
<td align="right">64,241,670</td>
<td align="right">98.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,154,420</td>
<td align="right">19,757,254</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,905,604</td>
<td align="right">17,282,237</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">209,960,769</td>
<td align="right">406,169,562</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">785,055</td>
<td align="right">1,478,486</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">181,469,202</td>
<td align="right">333,042,293</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">40,300,048</td>
<td align="right">73,603,671</td>
<td align="right">82.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">40,985,468</td>
<td align="right">73,669,331</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,894,060</td>
<td align="right">82,717,988</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,894,060</td>
<td align="right">82,717,988</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">39,076,060</td>
<td align="right">65,920,079</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">92,412,707</td>
<td align="right">153,900,891</td>
<td align="right">66.5%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,587,500</td>
<td align="right">9,271,129</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">891,713,662</td>
<td align="right">1,479,080,882</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">452,354,489</td>
<td align="right">738,320,654</td>
<td align="right">63.2%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,842,060</td>
<td align="right">2,988,360</td>
<td align="right">62.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">115,238,934</td>
<td align="right">179,420,732</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">110,269,454</td>
<td align="right">171,346,232</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">107,936,249</td>
<td align="right">167,082,617</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">24,662</td>
<td align="right">38,060</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">48,047,215</td>
<td align="right">73,894,953</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,951,640</td>
<td align="right">10,635,269</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">162,208,144</td>
<td align="right">247,416,018</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">45,570,023</td>
<td align="right">68,890,263</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">45,570,023</td>
<td align="right">68,890,263</td>
<td align="right">51.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">200,142,092</td>
<td align="right">298,856,620</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">139,676,556</td>
<td align="right">206,815,208</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,713,031,331</td>
<td align="right">2,521,459,226</td>
<td align="right">47.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">278,686,103</td>
<td align="right">406,903,732</td>
<td align="right">46.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,427,900</td>
<td align="right">138,732,969</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,287,646,922</td>
<td align="right">3,211,993,865</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,462,298,225</td>
<td align="right">3,455,811,854</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">7,869,568</td>
<td align="right">11,030,875</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">84,053,160</td>
<td align="right">117,479,809</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">57,016,988</td>
<td align="right">79,542,791</td>
<td align="right">39.5%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">353,753,017</td>
<td align="right">492,669,099</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">160,127,395</td>
<td align="right">222,356,582</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">475,047,261</td>
<td align="right">658,584,630</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">99,691,960</td>
<td align="right">137,694,111</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,398,739,180</td>
<td align="right">3,304,276,915</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">388,236,039</td>
<td align="right">528,037,469</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,111,754,393</td>
<td align="right">2,869,595,833</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">27,150,708</td>
<td align="right">36,760,842</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,145,062,479</td>
<td align="right">2,902,433,537</td>
<td align="right">35.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">114,754,074</td>
<td align="right">154,233,167</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">125,369,780</td>
<td align="right">167,694,629</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,133,029,652</td>
<td align="right">4,167,459,654</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">36,583,000</td>
<td align="right">48,661,100</td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">305,989,398</td>
<td align="right">406,300,055</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">166,049,961</td>
<td align="right">220,000,421</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">153,210,727</td>
<td align="right">201,665,105</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,122,658,448</td>
<td align="right">1,473,007,271</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,649,463,161</td>
<td align="right">4,742,352,553</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">985,071,238</td>
<td align="right">1,278,993,909</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">5,472,895</td>
<td align="right">7,092,775</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">622,669,738</td>
<td align="right">803,913,772</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,826,179,766</td>
<td align="right">4,933,490,075</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">707,669,498</td>
<td align="right">907,121,749</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,183,355,126</td>
<td align="right">10,443,176,206</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">917,546,025</td>
<td align="right">1,166,084,019</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,413,790,191</td>
<td align="right">4,332,895,486</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">74,216,157</td>
<td align="right">94,141,609</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,936,694,929</td>
<td align="right">10,000,650,372</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">847,863,072</td>
<td align="right">1,067,829,387</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">3,362,936,711</td>
<td align="right">4,230,893,473</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,810,249,921</td>
<td align="right">4,782,778,130</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">924,918,454</td>
<td align="right">1,160,385,065</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">489,820</td>
<td align="right">613,320</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">219,954,795</td>
<td align="right">275,286,707</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">394,254,521</td>
<td align="right">493,331,156</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">167,924,929</td>
<td align="right">209,975,009</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">991,343,737</td>
<td align="right">1,237,644,359</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,332,317,854</td>
<td align="right">1,663,110,374</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">898,300,429</td>
<td align="right">1,117,833,984</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">9,432,209,759</td>
<td align="right">11,692,155,853</td>
<td align="right">24.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">57,765,800</td>
<td align="right">71,539,474</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">247,072,356</td>
<td align="right">305,844,362</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">68,863,002</td>
<td align="right">85,147,783</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,619,349,265</td>
<td align="right">2,000,112,041</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">121,101,396</td>
<td align="right">148,914,241</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,776,769,171</td>
<td align="right">2,182,675,245</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,947,788,445</td>
<td align="right">2,386,420,775</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,561,764,436</td>
<td align="right">4,344,396,997</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,756,619,371</td>
<td align="right">2,142,062,610</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,618,713,155</td>
<td align="right">1,973,135,726</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">8,218,999,035</td>
<td align="right">9,955,858,864</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">122,707,543</td>
<td align="right">148,379,063</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">341,961,176</td>
<td align="right">408,098,269</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">25,336,425,548</td>
<td align="right">30,195,587,617</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,232,020</td>
<td align="right">417,290,328</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,413,619,239</td>
<td align="right">1,682,361,672</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,739,351</td>
<td align="right">243,548,814</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">576,272,661</td>
<td align="right">685,176,965</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,065,198,609</td>
<td align="right">1,266,238,914</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">290,692,085</td>
<td align="right">345,374,967</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">67,610,140</td>
<td align="right">79,962,940</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">130,183,353</td>
<td align="right">153,942,898</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,420,036,091</td>
<td align="right">2,847,979,521</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,082,746,573</td>
<td align="right">1,273,029,866</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,156,491,394</td>
<td align="right">1,356,530,276</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,018,699</td>
<td align="right">100,788,679</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">703,070,472</td>
<td align="right">822,987,681</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,731,396,602</td>
<td align="right">4,365,750,304</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">709,493,219</td>
<td align="right">829,412,521</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,365,961,034</td>
<td align="right">7,439,239,770</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">2,104,763</td>
<td align="right">2,452,282</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,405,542,033</td>
<td align="right">5,112,992,511</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,364,112,300</td>
<td align="right">2,737,691,194</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">879,797,758</td>
<td align="right">1,017,670,863</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,744,938,250</td>
<td align="right">17,045,857,212</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">376,020</td>
<td align="right">433,620</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,617,520,810</td>
<td align="right">1,857,532,182</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">21,070,493,105</td>
<td align="right">24,183,323,100</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">697,977,658</td>
<td align="right">799,829,682</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">702,781,818</td>
<td align="right">804,638,471</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">25,246,820</td>
<td align="right">28,854,367</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,699,893,829</td>
<td align="right">1,939,562,690</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,309,832</td>
<td align="right">103,031,826</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">797,202,387</td>
<td align="right">904,892,594</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">961,404,862</td>
<td align="right">1,090,486,486</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,821,109,334</td>
<td align="right">2,060,402,047</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">281,309,822</td>
<td align="right">318,092,670</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">530,143,303</td>
<td align="right">599,356,875</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,670,451,879</td>
<td align="right">6,405,535,183</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">351,212,423</td>
<td align="right">396,081,233</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">359,288,787</td>
<td align="right">404,848,112</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">44,058,042</td>
<td align="right">49,598,390</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">44,061,602</td>
<td align="right">49,601,950</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,247,637,332</td>
<td align="right">11,509,059,175</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,344,480,866</td>
<td align="right">1,500,529,099</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,071,491,684</td>
<td align="right">1,195,765,517</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,439,954</td>
<td align="right">671,446,436</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">242,849,697</td>
<td align="right">270,121,416</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,183,374,371</td>
<td align="right">1,312,009,571</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">952,135,942</td>
<td align="right">1,055,019,572</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">658,816,803</td>
<td align="right">727,934,604</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">556,437,781</td>
<td align="right">613,329,336</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,351,087</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,143,984,920</td>
<td align="right">1,258,756,129</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">782,483,423</td>
<td align="right">855,540,467</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,254,344,736</td>
<td align="right">5,741,326,348</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,730,972,596</td>
<td align="right">5,167,656,489</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,265,959,537</td>
<td align="right">1,376,125,083</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">566,894,220</td>
<td align="right">615,980,418</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">760,095,394</td>
<td align="right">825,016,143</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">238,358,782</td>
<td align="right">258,579,063</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">676,913,769</td>
<td align="right">733,010,897</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,436,926</td>
<td align="right">35,077,941</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,478,801,318</td>
<td align="right">1,593,471,821</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">532,993,906</td>
<td align="right">574,177,489</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,557,249,657</td>
<td align="right">2,751,946,304</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,241,889</td>
<td align="right">104,217,801</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,289,989</td>
<td align="right">104,265,901</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">166,996,855</td>
<td align="right">178,806,564</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">8,445,156,796</td>
<td align="right">7,851,200,534</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">155,220,170</td>
<td align="right">165,809,092</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,939,009,314</td>
<td align="right">4,194,750,598</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,884,415,707</td>
<td align="right">5,188,654,289</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,303,714</td>
<td align="right">1,383,704</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,625,840,004</td>
<td align="right">3,841,368,331</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">236,468,671</td>
<td align="right">249,836,338</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,224,686,354</td>
<td align="right">2,348,731,318</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">39,233,233</td>
<td align="right">41,404,286</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">10,339,855,502</td>
<td align="right">10,909,096,508</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">41,253,593</td>
<td align="right">43,434,846</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">366,309,287</td>
<td align="right">385,482,646</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,049,856,630</td>
<td align="right">1,104,477,408</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,313,759,885</td>
<td align="right">2,432,849,083</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">394,814,562</td>
<td align="right">413,921,814</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">11,163,200</td>
<td align="right">11,699,705</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,905,400</td>
<td align="right">162,131,840</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,713,956,979</td>
<td align="right">1,781,747,472</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">721,026,612</td>
<td align="right">749,237,594</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,484,235</td>
<td align="right">809,792,727</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">780,841,995</td>
<td align="right">811,150,487</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">112,666,344</td>
<td align="right">116,178,518</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,035,326,593</td>
<td align="right">3,123,739,411</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">228,516,684</td>
<td align="right">234,986,794</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,567,700</td>
<td align="right">33,477,980</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">11,445,900</td>
<td align="right">11,748,430</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,391,402,480</td>
<td align="right">2,450,955,272</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,377,462,304</td>
<td align="right">2,431,122,421</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,331,739</td>
<td align="right">69,798,052</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,081,911,595</td>
<td align="right">2,123,200,748</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,316,575,890</td>
<td align="right">1,339,428,624</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,006,381</td>
<td align="right">81,752,361</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">210,378,782</td>
<td align="right">211,861,329</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,043,323</td>
<td align="right">738,044,982</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">580,643,900</td>
<td align="right">582,470,778</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,752,980</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,626,064</td>
<td align="right">46,679,258</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,102,252</td>
<td align="right">518,422,112</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,871,063,615</td>
<td align="right">2,870,849,761</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">962,920</td>
<td align="right">962,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">962,920</td>
<td align="right">962,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">597,220</td>
<td align="right">597,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">574,043,588</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">44,208,040</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">1,080,913</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">89,060</td>
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
<td align="left">RAISE_VARARGS</td>
<td align="right">1,020</td>
<td align="right">2,720</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">19,115</td>
<td align="right">45,589</td>
<td align="right">138.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">60</td>
<td align="right">100</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,115</td>
<td align="right">57,121</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">36,000</td>
<td align="right">38,160</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right"></td>
<td align="right">380</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right"></td>
<td align="right">40</td>
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
<td align="right">1,151</td>
<td align="right">1,170</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,151</td>
<td align="right">1,170</td>
<td align="right">1.7%</td>
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
<td align="right">300</td>
<td align="right">300</td>
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
<td align="right">460</td>
<td align="right">460</td>
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
<td align="right">1,801</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-08-27
