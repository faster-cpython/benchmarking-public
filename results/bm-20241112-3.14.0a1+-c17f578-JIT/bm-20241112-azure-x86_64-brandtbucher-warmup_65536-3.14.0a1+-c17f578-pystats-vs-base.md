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
<td align="right">37,695,928</td>
<td align="right">392,688,821</td>
<td align="right">941.7%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">335</td>
<td align="right">2,752</td>
<td align="right">721.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">5,751,189</td>
<td align="right">46,536,091</td>
<td align="right">709.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">342,313</td>
<td align="right">1,199,552</td>
<td align="right">250.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">582,883</td>
<td align="right">1,819,775</td>
<td align="right">212.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">170,649</td>
<td align="right">447,010</td>
<td align="right">161.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">74,239,753</td>
<td align="right">181,414,195</td>
<td align="right">144.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">37,963,746</td>
<td align="right">86,906,359</td>
<td align="right">128.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">35,268,284</td>
<td align="right">74,398,458</td>
<td align="right">111.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">35,235,219</td>
<td align="right">72,768,425</td>
<td align="right">106.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">14,939,151</td>
<td align="right">30,703,402</td>
<td align="right">105.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">20,047,075</td>
<td align="right">40,675,536</td>
<td align="right">102.9%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,144</td>
<td align="right">5,240,664</td>
<td align="right">101.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,851,062</td>
<td align="right">9,741,607</td>
<td align="right">100.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">40,137,747</td>
<td align="right">80,422,062</td>
<td align="right">100.4%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">215,938</td>
<td align="right">421,482</td>
<td align="right">95.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">23,721,527</td>
<td align="right">45,999,202</td>
<td align="right">93.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">217,180,721</td>
<td align="right">397,795,652</td>
<td align="right">83.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">33,558,951</td>
<td align="right">58,343,092</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">24,494,389</td>
<td align="right">40,203,550</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">173,332,173</td>
<td align="right">281,737,437</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,518,326</td>
<td align="right">2,458,699</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">162,476,322</td>
<td align="right">260,279,212</td>
<td align="right">60.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">120,093,200</td>
<td align="right">189,240,885</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,618,598</td>
<td align="right">5,636,589</td>
<td align="right">55.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,177,429</td>
<td align="right">1,826,250</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">50,835,778</td>
<td align="right">78,511,647</td>
<td align="right">54.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">43,663,195</td>
<td align="right">66,831,635</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">129,789,627</td>
<td align="right">192,861,631</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">539,100</td>
<td align="right">781,020</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">46,174,066</td>
<td align="right">66,729,356</td>
<td align="right">44.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">153,497,195</td>
<td align="right">220,209,071</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,546,051</td>
<td align="right">10,679,926</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">42,351</td>
<td align="right">59,614</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,431,589</td>
<td align="right">63,479,410</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,270,803</td>
<td align="right">3,121,800</td>
<td align="right">37.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">26,508,860</td>
<td align="right">36,290,363</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">504,359,970</td>
<td align="right">683,926,245</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">261,123,678</td>
<td align="right">352,431,173</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">26,625,687</td>
<td align="right">35,924,658</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">107,698,082</td>
<td align="right">144,114,690</td>
<td align="right">33.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">187,936,950</td>
<td align="right">251,026,161</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,544,621,221</td>
<td align="right">2,058,281,507</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">38,328,278</td>
<td align="right">26,141,812</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">79,898,760</td>
<td align="right">104,077,214</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">644,588,320</td>
<td align="right">836,960,336</td>
<td align="right">29.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">223,767,873</td>
<td align="right">290,208,558</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">91,303,391</td>
<td align="right">118,295,366</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">93,819,981</td>
<td align="right">120,789,187</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">245,406,730</td>
<td align="right">311,542,676</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,287,938,020</td>
<td align="right">1,624,262,904</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">145,880,661</td>
<td align="right">183,653,508</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">221,475,859</td>
<td align="right">278,349,964</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,032,422,342</td>
<td align="right">1,295,610,109</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">314,878,601</td>
<td align="right">391,951,475</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">22,952,767</td>
<td align="right">28,566,607</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,763,358,599</td>
<td align="right">3,434,093,978</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,940,853,635</td>
<td align="right">2,387,671,963</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">351,192,499</td>
<td align="right">430,428,389</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">467,595,251</td>
<td align="right">570,304,642</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">592,200,492</td>
<td align="right">717,495,176</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,306,032</td>
<td align="right">3,988,814</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">797,716,505</td>
<td align="right">958,530,501</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,396,133,715</td>
<td align="right">4,065,843,966</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,770,709,541</td>
<td align="right">14,039,970,681</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,952,221,543</td>
<td align="right">2,324,668,842</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,484,458,177</td>
<td align="right">1,764,304,125</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">106,520,164</td>
<td align="right">126,500,093</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">28,636,347</td>
<td align="right">33,954,496</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">584,340,551</td>
<td align="right">690,512,480</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">362,142,541</td>
<td align="right">426,976,546</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">416,057,446</td>
<td align="right">490,524,430</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">298,756,214</td>
<td align="right">352,041,951</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">43,769,696</td>
<td align="right">51,563,455</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">576,709,411</td>
<td align="right">677,425,537</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">50,720,475</td>
<td align="right">59,536,411</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">130,860,633</td>
<td align="right">153,589,487</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">179,013,803</td>
<td align="right">210,041,518</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">55,664,660</td>
<td align="right">65,198,868</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">43,393,686</td>
<td align="right">50,767,592</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,691,007</td>
<td align="right">2,240,029</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">350,969,302</td>
<td align="right">408,212,800</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">145,481,658</td>
<td align="right">169,146,394</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">199,484,527</td>
<td align="right">231,232,028</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,854,297,288</td>
<td align="right">3,301,988,840</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">76,959,169</td>
<td align="right">88,858,897</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,024,393</td>
<td align="right">11,524,306</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">40,203,810</td>
<td align="right">46,112,332</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,016,260,896</td>
<td align="right">1,727,551,962</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">26,263,848</td>
<td align="right">29,913,005</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">155,046,489</td>
<td align="right">176,311,814</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">413,505,804</td>
<td align="right">469,339,505</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,466</td>
<td align="right">3,929</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,531,820,347</td>
<td align="right">3,999,856,363</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">54,079,501</td>
<td align="right">61,239,895</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">110,318,700</td>
<td align="right">124,598,800</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,491,966,800</td>
<td align="right">2,806,715,993</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">149,053,872</td>
<td align="right">167,741,216</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,444,951</td>
<td align="right">28,581,996</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,410,857</td>
<td align="right">8,323,721</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">274,841,743</td>
<td align="right">308,517,548</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">58,276,517</td>
<td align="right">65,393,001</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">46,087,702</td>
<td align="right">51,252,202</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,501,702,343</td>
<td align="right">1,665,104,041</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">448,729,364</td>
<td align="right">496,079,286</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">10,056,479</td>
<td align="right">11,107,629</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">32,977,174</td>
<td align="right">36,145,582</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">514,783,397</td>
<td align="right">563,461,977</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,856,057</td>
<td align="right">8,594,255</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">608,256,747</td>
<td align="right">664,220,010</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">97,052,421</td>
<td align="right">105,873,719</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,193,819,297</td>
<td align="right">2,390,701,860</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">269,947,969</td>
<td align="right">293,943,874</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">483,787,589</td>
<td align="right">526,664,619</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">59,396,177</td>
<td align="right">64,526,241</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">85,768,521</td>
<td align="right">93,072,348</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">253,689,219</td>
<td align="right">275,250,778</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">168,054,944</td>
<td align="right">181,905,627</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">121,028,260</td>
<td align="right">111,248,541</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">53,367</td>
<td align="right">57,650</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">56,590,757</td>
<td align="right">61,100,551</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">95,479,241</td>
<td align="right">102,856,904</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">149,619,977</td>
<td align="right">160,711,532</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">12,567,832</td>
<td align="right">13,486,716</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">86,206,145</td>
<td align="right">92,506,011</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">253,380,584</td>
<td align="right">271,597,347</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">54,066,043</td>
<td align="right">57,894,011</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">218,478,550</td>
<td align="right">233,184,965</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">111,528,391</td>
<td align="right">118,922,381</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">261,567,277</td>
<td align="right">277,965,183</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">734,217</td>
<td align="right">774,866</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">791,977,471</td>
<td align="right">832,631,758</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">95,959,748</td>
<td align="right">100,254,098</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">86,255,596</td>
<td align="right">90,078,882</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">63,515,179</td>
<td align="right">66,284,785</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,853,383</td>
<td align="right">1,112,636,969</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">203,058,938</td>
<td align="right">210,052,571</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,302,919,026</td>
<td align="right">4,446,468,091</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">46,643,019</td>
<td align="right">48,115,001</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">66,500,281</td>
<td align="right">68,492,673</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">32,652,988</td>
<td align="right">33,578,221</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">428,552,086</td>
<td align="right">416,698,694</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">79,887,102</td>
<td align="right">81,997,428</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">105,002,402</td>
<td align="right">102,378,659</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">180,904,176</td>
<td align="right">184,965,815</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">182,687,993</td>
<td align="right">186,728,870</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">341,236,230</td>
<td align="right">347,329,168</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">113,819,380</td>
<td align="right">115,443,954</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">31,867,816</td>
<td align="right">32,265,416</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,169,278</td>
<td align="right">17,335,036</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">103,382,803</td>
<td align="right">102,480,844</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,919,189</td>
<td align="right">8,976,850</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,782,164,262</td>
<td align="right">1,792,867,234</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">111,091,404</td>
<td align="right">110,772,371</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,818,355</td>
<td align="right">101,011,867</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">168,156,024</td>
<td align="right">168,432,953</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">152,305,133</td>
<td align="right">152,502,386</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,623,213</td>
<td align="right">1,625,119</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">17,613</td>
<td align="right">17,633</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">74,556,288</td>
<td align="right">74,488,977</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">334,299</td>
<td align="right">334,046</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,635</td>
<td align="right">2,634</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">116,577</td>
<td align="right">116,537</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">16,650,950</td>
<td align="right">16,652,451</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">16,321,516</td>
<td align="right">16,322,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">16,651,871</td>
<td align="right">16,652,475</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,684,621</td>
<td align="right">14,684,126</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">2,981,220</td>
<td align="right">2,981,257</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,395,611</td>
<td align="right">4,395,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,606,993</td>
<td align="right">302,606,993</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,971</td>
<td align="right">128,851,971</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right">29,134,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">29,134,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,780</td>
<td align="right">98,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,554</td>
<td align="right">84,554</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,138</td>
<td align="right">56,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,551</td>
<td align="right">17,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,320</td>
<td align="right">5,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,624</td>
<td align="right">3,624</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">169</td>
<td align="right">169</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">30</td>
<td align="right">30</td>
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
<td align="right">297,980,544</td>
<td align="right">3.9%</td>
<td align="right">351,201,250</td>
<td align="right">4.5%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,189,900</td>
<td align="right">0.3%</td>
<td align="right">23,598,697</td>
<td align="right">0.3%</td>
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
<td align="right">7,388,592,354</td>
<td align="right">95.8%</td>
<td align="right">7,385,114,967</td>
<td align="right">95.2%</td>
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
<td align="right">769,650</td>
<td align="right">100.0%</td>
<td align="right">834,680</td>
<td align="right">100.0%</td>
<td align="right">8.4%</td>
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
<td align="left">add different types</td>
<td align="right">45,938</td>
<td align="right">6.0%</td>
<td align="right">94,727</td>
<td align="right">11.3%</td>
<td align="right">106.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">7,191</td>
<td align="right">0.9%</td>
<td align="right">10,026</td>
<td align="right">1.2%</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">2,748</td>
<td align="right">0.4%</td>
<td align="right">3,822</td>
<td align="right">0.5%</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,049</td>
<td align="right">0.1%</td>
<td align="right">1,364</td>
<td align="right">0.2%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">4,182</td>
<td align="right">0.5%</td>
<td align="right">5,182</td>
<td align="right">0.6%</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">738</td>
<td align="right">0.1%</td>
<td align="right">898</td>
<td align="right">0.1%</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">2,827</td>
<td align="right">0.4%</td>
<td align="right">3,427</td>
<td align="right">0.4%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">4,576</td>
<td align="right">0.6%</td>
<td align="right">5,393</td>
<td align="right">0.6%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">5,681</td>
<td align="right">0.7%</td>
<td align="right">6,664</td>
<td align="right">0.8%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">9,620</td>
<td align="right">1.2%</td>
<td align="right">10,977</td>
<td align="right">1.3%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,441</td>
<td align="right">0.3%</td>
<td align="right">2,723</td>
<td align="right">0.3%</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">55,649</td>
<td align="right">7.2%</td>
<td align="right">59,887</td>
<td align="right">7.2%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">5,987</td>
<td align="right">0.8%</td>
<td align="right">6,347</td>
<td align="right">0.8%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">22,108</td>
<td align="right">2.9%</td>
<td align="right">23,355</td>
<td align="right">2.8%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,012</td>
<td align="right">2.5%</td>
<td align="right">19,959</td>
<td align="right">2.4%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">490</td>
<td align="right">0.1%</td>
<td align="right">497</td>
<td align="right">0.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,323</td>
<td align="right">0.3%</td>
<td align="right">2,343</td>
<td align="right">0.3%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">577,007</td>
<td align="right">75.0%</td>
<td align="right">577,006</td>
<td align="right">69.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">83</td>
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
<td align="right">85,768,521</td>
<td align="right">100.0%</td>
<td align="right">93,072,348</td>
<td align="right">100.0%</td>
<td align="right">8.5%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,754,806</td>
<td align="right">0.1%</td>
<td align="right">5,918,550</td>
<td align="right">0.1%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">428,409,727</td>
<td align="right">7.3%</td>
<td align="right">416,557,991</td>
<td align="right">7.1%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,456,991,774</td>
<td align="right">92.6%</td>
<td align="right">5,481,881,932</td>
<td align="right">92.8%</td>
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
<td align="right">116,308</td>
<td align="right">46.4%</td>
<td align="right">119,400</td>
<td align="right">47.3%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">134,435</td>
<td align="right">53.6%</td>
<td align="right">132,793</td>
<td align="right">52.7%</td>
<td align="right">-1.2%</td>
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
<td align="left">buffer int</td>
<td align="right">9,788</td>
<td align="right">7.3%</td>
<td align="right">3,469</td>
<td align="right">2.6%</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">767</td>
<td align="right">0.6%</td>
<td align="right">989</td>
<td align="right">0.7%</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,759</td>
<td align="right">3.5%</td>
<td align="right">5,384</td>
<td align="right">4.1%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">18,032</td>
<td align="right">13.4%</td>
<td align="right">19,183</td>
<td align="right">14.4%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">45,787</td>
<td align="right">34.1%</td>
<td align="right">48,010</td>
<td align="right">36.2%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">73</td>
<td align="right">0.1%</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,442</td>
<td align="right">2.6%</td>
<td align="right">3,484</td>
<td align="right">2.6%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">36,471</td>
<td align="right">27.1%</td>
<td align="right">36,799</td>
<td align="right">27.7%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,354</td>
<td align="right">9.2%</td>
<td align="right">12,441</td>
<td align="right">9.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.2%</td>
<td align="right">2,941</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
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
<td align="right">18,734</td>
<td align="right">0.0%</td>
<td align="right">22,186</td>
<td align="right">0.0%</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">118,745,409</td>
<td align="right">1.1%</td>
<td align="right">127,326,095</td>
<td align="right">1.2%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,834,584,811</td>
<td align="right">98.9%</td>
<td align="right">10,869,974,398</td>
<td align="right">98.8%</td>
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
<td align="right">192,940</td>
<td align="right">0.0%</td>
<td align="right">192,988</td>
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
<td align="right">2,397,195</td>
<td align="right">100.0%</td>
<td align="right">2,560,004</td>
<td align="right">100.0%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">569</td>
<td align="right">0.0%</td>
<td align="right">569</td>
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
<td align="left">init not python</td>
<td align="right">287</td>
<td align="right">50.4%</td>
<td align="right">267</td>
<td align="right">46.9%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">385</td>
<td align="right">67.7%</td>
<td align="right">365</td>
<td align="right">64.1%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">750</td>
<td align="right">131.8%</td>
<td align="right">750</td>
<td align="right">131.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">569</td>
<td align="right">100.0%</td>
<td align="right">569</td>
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
<td align="right">533,897</td>
<td align="right">82.1%</td>
<td align="right">591,711</td>
<td align="right">83.5%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">109,459</td>
<td align="right">16.8%</td>
<td align="right">109,470</td>
<td align="right">15.5%</td>
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
<td align="right">79,808,318</td>
<td align="right">1.7%</td>
<td align="right">103,976,306</td>
<td align="right">2.3%</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">938,666</td>
<td align="right">0.0%</td>
<td align="right">1,073,564</td>
<td align="right">0.0%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,507,577,420</td>
<td align="right">98.2%</td>
<td align="right">4,508,519,725</td>
<td align="right">97.7%</td>
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
<td align="right">82,731</td>
<td align="right">76.6%</td>
<td align="right">93,237</td>
<td align="right">77.0%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">25,304</td>
<td align="right">23.4%</td>
<td align="right">27,825</td>
<td align="right">23.0%</td>
<td align="right">10.0%</td>
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
<td align="right">682</td>
<td align="right">0.8%</td>
<td align="right">1,149</td>
<td align="right">1.2%</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">334</td>
<td align="right">0.4%</td>
<td align="right">523</td>
<td align="right">0.6%</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">974</td>
<td align="right">1.2%</td>
<td align="right">1,277</td>
<td align="right">1.4%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,765</td>
<td align="right">10.6%</td>
<td align="right">11,261</td>
<td align="right">12.1%</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,176</td>
<td align="right">7.5%</td>
<td align="right">7,632</td>
<td align="right">8.2%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,434</td>
<td align="right">7.8%</td>
<td align="right">7,745</td>
<td align="right">8.3%</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">20,995</td>
<td align="right">25.4%</td>
<td align="right">23,355</td>
<td align="right">25.0%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">25,524</td>
<td align="right">30.9%</td>
<td align="right">27,202</td>
<td align="right">29.2%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,960</td>
<td align="right">4.8%</td>
<td align="right">4,101</td>
<td align="right">4.4%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">999</td>
<td align="right">1.2%</td>
<td align="right">1,019</td>
<td align="right">1.1%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,554</td>
<td align="right">9.1%</td>
<td align="right">7,639</td>
<td align="right">8.2%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.4%</td>
<td align="right">334</td>
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
<td align="right">33,528,278</td>
<td align="right">1.5%</td>
<td align="right">58,306,323</td>
<td align="right">2.6%</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,178,581,295</td>
<td align="right">98.4%</td>
<td align="right">2,182,618,405</td>
<td align="right">97.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,916,370</td>
<td align="right">0.1%</td>
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
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
<td align="right">28,433</td>
<td align="right">100.0%</td>
<td align="right">34,523</td>
<td align="right">100.0%</td>
<td align="right">21.4%</td>
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
<td align="left">str</td>
<td align="right">6,278</td>
<td align="right">22.1%</td>
<td align="right">9,320</td>
<td align="right">27.0%</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,172</td>
<td align="right">25.2%</td>
<td align="right">8,771</td>
<td align="right">25.4%</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">4,838</td>
<td align="right">17.0%</td>
<td align="right">5,508</td>
<td align="right">16.0%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,145</td>
<td align="right">35.7%</td>
<td align="right">10,924</td>
<td align="right">31.6%</td>
<td align="right">7.7%</td>
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
<td align="right">74,195,596</td>
<td align="right">12.4%</td>
<td align="right">181,313,823</td>
<td align="right">19.7%</td>
<td align="right">144.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">500,386,743</td>
<td align="right">83.4%</td>
<td align="right">718,937,534</td>
<td align="right">78.0%</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,186,043</td>
<td align="right">4.2%</td>
<td align="right">21,494,329</td>
<td align="right">2.3%</td>
<td align="right">-14.7%</td>
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
<td align="right">40,641</td>
<td align="right">7.8%</td>
<td align="right">96,851</td>
<td align="right">19.1%</td>
<td align="right">138.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">478,567</td>
<td align="right">92.2%</td>
<td align="right">408,950</td>
<td align="right">80.9%</td>
<td align="right">-14.5%</td>
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
<td align="left">bytes</td>
<td align="right">55</td>
<td align="right">0.1%</td>
<td align="right">572</td>
<td align="right">0.6%</td>
<td align="right">940.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">130</td>
<td align="right">0.3%</td>
<td align="right">736</td>
<td align="right">0.8%</td>
<td align="right">466.2%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,339</td>
<td align="right">3.3%</td>
<td align="right">5,606</td>
<td align="right">5.8%</td>
<td align="right">318.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">13,733</td>
<td align="right">33.8%</td>
<td align="right">46,577</td>
<td align="right">48.1%</td>
<td align="right">239.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">871</td>
<td align="right">2.1%</td>
<td align="right">2,272</td>
<td align="right">2.3%</td>
<td align="right">160.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,769</td>
<td align="right">4.4%</td>
<td align="right">4,538</td>
<td align="right">4.7%</td>
<td align="right">156.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,568</td>
<td align="right">8.8%</td>
<td align="right">6,759</td>
<td align="right">7.0%</td>
<td align="right">89.4%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">69</td>
<td align="right">0.2%</td>
<td align="right">130</td>
<td align="right">0.1%</td>
<td align="right">88.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,571</td>
<td align="right">16.2%</td>
<td align="right">11,987</td>
<td align="right">12.4%</td>
<td align="right">82.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">3,368</td>
<td align="right">8.3%</td>
<td align="right">5,499</td>
<td align="right">5.7%</td>
<td align="right">63.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,860</td>
<td align="right">4.6%</td>
<td align="right">2,799</td>
<td align="right">2.9%</td>
<td align="right">50.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,493</td>
<td align="right">6.1%</td>
<td align="right">3,226</td>
<td align="right">3.3%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,593</td>
<td align="right">8.8%</td>
<td align="right">4,634</td>
<td align="right">4.8%</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,222</td>
<td align="right">3.0%</td>
<td align="right">1,516</td>
<td align="right">1.6%</td>
<td align="right">24.1%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">598,199</td>
<td align="right">0.0%</td>
<td align="right">1,404,484</td>
<td align="right">0.0%</td>
<td align="right">134.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">409,707,305</td>
<td align="right">3.2%</td>
<td align="right">652,713,129</td>
<td align="right">5.0%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">414,764,589</td>
<td align="right">3.2%</td>
<td align="right">489,133,989</td>
<td align="right">3.7%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,079,470,077</td>
<td align="right">93.6%</td>
<td align="right">11,986,516,442</td>
<td align="right">91.3%</td>
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
<td align="right">8,812,305</td>
<td align="right">97.8%</td>
<td align="right">13,475,749</td>
<td align="right">98.4%</td>
<td align="right">52.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">201,827</td>
<td align="right">2.2%</td>
<td align="right">221,195</td>
<td align="right">1.6%</td>
<td align="right">9.6%</td>
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
<td align="left">builtin class method</td>
<td align="right">858</td>
<td align="right">0.4%</td>
<td align="right">1,118</td>
<td align="right">0.5%</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">35,618</td>
<td align="right">17.6%</td>
<td align="right">42,437</td>
<td align="right">19.2%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">13,939</td>
<td align="right">6.9%</td>
<td align="right">16,555</td>
<td align="right">7.5%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,215</td>
<td align="right">0.6%</td>
<td align="right">1,426</td>
<td align="right">0.6%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,406</td>
<td align="right">1.2%</td>
<td align="right">2,667</td>
<td align="right">1.2%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">19,730</td>
<td align="right">9.8%</td>
<td align="right">21,658</td>
<td align="right">9.8%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">56,140</td>
<td align="right">27.8%</td>
<td align="right">60,863</td>
<td align="right">27.5%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,627</td>
<td align="right">2.3%</td>
<td align="right">4,968</td>
<td align="right">2.2%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,069</td>
<td align="right">0.5%</td>
<td align="right">997</td>
<td align="right">0.5%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">361</td>
<td align="right">0.2%</td>
<td align="right">381</td>
<td align="right">0.2%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,480</td>
<td align="right">0.7%</td>
<td align="right">1,558</td>
<td align="right">0.7%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">39,830</td>
<td align="right">19.7%</td>
<td align="right">41,722</td>
<td align="right">18.9%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,106</td>
<td align="right">0.5%</td>
<td align="right">1,092</td>
<td align="right">0.5%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,562</td>
<td align="right">3.7%</td>
<td align="right">7,585</td>
<td align="right">3.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,284</td>
<td align="right">4.1%</td>
<td align="right">8,262</td>
<td align="right">3.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">3,383,206,153</td>
<td align="right">99.6%</td>
<td align="right">4,055,319,689</td>
<td align="right">99.6%</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">31,865</td>
<td align="right">0.0%</td>
<td align="right">31,864</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,584,084</td>
<td align="right">0.4%</td>
<td align="right">14,584,105</td>
<td align="right">0.4%</td>
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
<td align="right">1,453</td>
<td align="right">0.0%</td>
<td align="right">1,453</td>
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
<td align="right">101,248</td>
<td align="right">100.0%</td>
<td align="right">100,731</td>
<td align="right">100.0%</td>
<td align="right">-0.5%</td>
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
<td align="right">216</td>
<td align="right">0.0%</td>
<td align="right">215</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">62,503,338</td>
<td align="right">100.0%</td>
<td align="right">62,610,628</td>
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
<td align="right">2,419</td>
<td align="right">100.0%</td>
<td align="right">2,419</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">593,287,078</td>
<td align="right">82.2%</td>
<td align="right">593,287,030</td>
<td align="right">82.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,817,179</td>
<td align="right">17.8%</td>
<td align="right">128,817,179</td>
<td align="right">17.8%</td>
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
<td align="right">14,711</td>
<td align="right">0.0%</td>
<td align="right">14,711</td>
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
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,412</td>
<td align="right">98.1%</td>
<td align="right">34,412</td>
<td align="right">98.1%</td>
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
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right">752</td>
<td align="right">2.2%</td>
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
<td align="right">104,019,120</td>
<td align="right">5.2%</td>
<td align="right">122,434,862</td>
<td align="right">6.1%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">53,995,445</td>
<td align="right">2.7%</td>
<td align="right">57,822,470</td>
<td align="right">2.9%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,840,530,693</td>
<td align="right">92.1%</td>
<td align="right">1,828,322,104</td>
<td align="right">91.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">1,992,491</td>
<td align="right">98.0%</td>
<td align="right">2,339,804</td>
<td align="right">98.3%</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40,124</td>
<td align="right">2.0%</td>
<td align="right">41,243</td>
<td align="right">1.7%</td>
<td align="right">2.8%</td>
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
<td align="right">4,634</td>
<td align="right">11.5%</td>
<td align="right">5,183</td>
<td align="right">12.6%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.7%</td>
<td align="right">743</td>
<td align="right">1.8%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,467</td>
<td align="right">18.6%</td>
<td align="right">7,627</td>
<td align="right">18.5%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">19,881</td>
<td align="right">49.5%</td>
<td align="right">20,253</td>
<td align="right">49.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">4.0%</td>
<td align="right">1,599</td>
<td align="right">3.9%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,905</td>
<td align="right">4.7%</td>
<td align="right">1,917</td>
<td align="right">4.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,759</td>
<td align="right">4.4%</td>
<td align="right">1,761</td>
<td align="right">4.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">860</td>
<td align="right">2.1%</td>
<td align="right">860</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">731</td>
<td align="right">1.8%</td>
<td align="right">731</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">365</td>
<td align="right">0.9%</td>
<td align="right">365</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">94</td>
<td align="right">0.2%</td>
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
<td align="right">215,938</td>
<td align="right">100.0%</td>
<td align="right">421,482</td>
<td align="right">100.0%</td>
<td align="right">95.2%</td>
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
<td align="right">86,171,781</td>
<td align="right">8.6%</td>
<td align="right">92,470,284</td>
<td align="right">9.1%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">916,843,633</td>
<td align="right">91.4%</td>
<td align="right">919,054,040</td>
<td align="right">90.9%</td>
<td align="right">0.2%</td>
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
<td align="right">32,271</td>
<td align="right">93.8%</td>
<td align="right">33,630</td>
<td align="right">94.0%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,133</td>
<td align="right">6.2%</td>
<td align="right">2,137</td>
<td align="right">6.0%</td>
<td align="right">0.2%</td>
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
<td align="left">array slice</td>
<td align="right">24</td>
<td align="right">0.1%</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">183.3%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">185</td>
<td align="right">0.6%</td>
<td align="right">348</td>
<td align="right">1.0%</td>
<td align="right">88.1%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">3,064</td>
<td align="right">9.5%</td>
<td align="right">3,390</td>
<td align="right">10.1%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">209</td>
<td align="right">0.6%</td>
<td align="right">231</td>
<td align="right">0.7%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">8,633</td>
<td align="right">26.8%</td>
<td align="right">9,517</td>
<td align="right">28.3%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,934</td>
<td align="right">9.1%</td>
<td align="right">2,894</td>
<td align="right">8.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,722</td>
<td align="right">51.8%</td>
<td align="right">16,682</td>
<td align="right">49.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">500</td>
<td align="right">1.5%</td>
<td align="right">500</td>
<td align="right">1.5%</td>
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
<td align="right">22,012,597</td>
<td align="right">0.5%</td>
<td align="right">39,845,657</td>
<td align="right">0.8%</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">120,735,715</td>
<td align="right">2.6%</td>
<td align="right">110,899,202</td>
<td align="right">2.3%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,534,552,546</td>
<td align="right">96.9%</td>
<td align="right">4,597,271,374</td>
<td align="right">96.8%</td>
<td align="right">1.4%</td>
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
<td align="right">448,452</td>
<td align="right">63.5%</td>
<td align="right">784,681</td>
<td align="right">71.3%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">258,248</td>
<td align="right">36.5%</td>
<td align="right">315,116</td>
<td align="right">28.7%</td>
<td align="right">22.0%</td>
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
<td align="right">8,024</td>
<td align="right">3.1%</td>
<td align="right">24,045</td>
<td align="right">7.6%</td>
<td align="right">199.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">9,958</td>
<td align="right">3.9%</td>
<td align="right">1,678</td>
<td align="right">0.5%</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">132,770</td>
<td align="right">51.4%</td>
<td align="right">163,815</td>
<td align="right">52.0%</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,133</td>
<td align="right">3.5%</td>
<td align="right">11,193</td>
<td align="right">3.6%</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">3,385</td>
<td align="right">1.3%</td>
<td align="right">4,044</td>
<td align="right">1.3%</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">72,502</td>
<td align="right">28.1%</td>
<td align="right">85,187</td>
<td align="right">27.0%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">11,778</td>
<td align="right">4.6%</td>
<td align="right">13,566</td>
<td align="right">4.3%</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,276</td>
<td align="right">4.0%</td>
<td align="right">11,166</td>
<td align="right">3.5%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">574,999</td>
<td align="right">0.0%</td>
<td align="right">1,811,600</td>
<td align="right">0.1%</td>
<td align="right">215.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,229,992,907</td>
<td align="right">100.0%</td>
<td align="right">1,243,961,753</td>
<td align="right">99.9%</td>
<td align="right">1.1%</td>
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
<td align="left">Failure</td>
<td align="right">644</td>
<td align="right">8.1%</td>
<td align="right">995</td>
<td align="right">12.1%</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,320</td>
<td align="right">91.9%</td>
<td align="right">7,260</td>
<td align="right">87.9%</td>
<td align="right">-0.8%</td>
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
<td align="right">417</td>
<td align="right">64.8%</td>
<td align="right">768</td>
<td align="right">77.2%</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">21.1%</td>
<td align="right">136</td>
<td align="right">13.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">14.1%</td>
<td align="right">91</td>
<td align="right">9.1%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">711,224,062</td>
<td align="right">1.0%</td>
<td align="right">997,127,869</td>
<td align="right">1.2%</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">25,779,008,052</td>
<td align="right">37.0%</td>
<td align="right">30,465,102,260</td>
<td align="right">37.6%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">1,822,921,103</td>
<td align="right">2.6%</td>
<td align="right">2,104,051,058</td>
<td align="right">2.6%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">41,317,287,245</td>
<td align="right">59.3%</td>
<td align="right">47,513,164,172</td>
<td align="right">58.6%</td>
<td align="right">15.0%</td>
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
<td align="right">74,195,596</td>
<td align="right">4.1%</td>
<td align="right">181,313,823</td>
<td align="right">8.6%</td>
<td align="right">144.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">79,808,318</td>
<td align="right">4.4%</td>
<td align="right">103,976,306</td>
<td align="right">4.9%</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">414,764,589</td>
<td align="right">22.8%</td>
<td align="right">489,133,989</td>
<td align="right">23.3%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">297,980,544</td>
<td align="right">16.4%</td>
<td align="right">351,201,250</td>
<td align="right">16.7%</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">85,768,521</td>
<td align="right">4.7%</td>
<td align="right">93,072,348</td>
<td align="right">4.4%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">120,735,715</td>
<td align="right">6.6%</td>
<td align="right">110,899,202</td>
<td align="right">5.3%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">86,171,781</td>
<td align="right">4.7%</td>
<td align="right">92,470,284</td>
<td align="right">4.4%</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">428,409,727</td>
<td align="right">23.5%</td>
<td align="right">416,557,991</td>
<td align="right">19.8%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,817,179</td>
<td align="right">7.1%</td>
<td align="right">128,817,179</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,995,445</td>
<td align="right">3.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">58,306,323</td>
<td align="right">2.8%</td>
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
<td align="right">157,391,851</td>
<td align="right">22.1%</td>
<td align="right">279,802,954</td>
<td align="right">28.1%</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">102,886,195</td>
<td align="right">14.5%</td>
<td align="right">177,119,068</td>
<td align="right">17.8%</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">48,597,505</td>
<td align="right">6.8%</td>
<td align="right">76,370,635</td>
<td align="right">7.7%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">17,049,085</td>
<td align="right">2.4%</td>
<td align="right">22,175,915</td>
<td align="right">2.2%</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">86,949,385</td>
<td align="right">12.2%</td>
<td align="right">100,223,379</td>
<td align="right">10.0%</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">61,571,236</td>
<td align="right">8.7%</td>
<td align="right">69,084,617</td>
<td align="right">6.9%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">61,706,901</td>
<td align="right">8.7%</td>
<td align="right">68,552,233</td>
<td align="right">6.9%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,976,167</td>
<td align="right">2.4%</td>
<td align="right">18,709,686</td>
<td align="right">1.9%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,872,733</td>
<td align="right">2.9%</td>
<td align="right">20,872,663</td>
<td align="right">2.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">15,363,971</td>
<td align="right">2.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">17,013,872</td>
<td align="right">1.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,276</td>
<td align="right">0.0%</td>
<td align="right">4,273,471</td>
<td align="right">0.1%</td>
<td align="right">100.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,860,854</td>
<td align="right">10.1%</td>
<td align="right">678,892,075</td>
<td align="right">10.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,866,469,480</td>
<td align="right">73.1%</td>
<td align="right">4,917,470,717</td>
<td align="right">73.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">69,244,965</td>
<td align="right">1.0%</td>
<td align="right">68,528,289</td>
<td align="right">1.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,787,211,909</td>
<td align="right">26.9%</td>
<td align="right">1,797,464,005</td>
<td align="right">26.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,787,211,909</td>
<td align="right">26.9%</td>
<td align="right">1,797,464,005</td>
<td align="right">26.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,254,796,442</td>
<td align="right">79.0%</td>
<td align="right">5,275,452,471</td>
<td align="right">78.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,116,351,055</td>
<td align="right">16.8%</td>
<td align="right">1,118,571,930</td>
<td align="right">16.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">278,994,603</td>
<td align="right">4.2%</td>
<td align="right">278,657,038</td>
<td align="right">4.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,928</td>
<td align="right">0.0%</td>
<td align="right">3,929</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,114,218,851</td>
<td align="right">16.7%</td>
<td align="right">1,114,294,530</td>
<td align="right">16.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,899,635</td>
<td align="right">0.4%</td>
<td align="right">24,900,062</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,406,805</td>
<td align="right">3.9%</td>
<td align="right">261,407,050</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,137</td>
<td align="right">2.0%</td>
<td align="right">132,513,137</td>
<td align="right">2.0%</td>
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
<td align="left">Interpreter immortal increfs</td>
<td align="right">7,790,641,622</td>
<td align="right">4.7%</td>
<td align="right">9,461,940,640</td>
<td align="right">5.8%</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">32,153,336,048</td>
<td align="right">19.5%</td>
<td align="right">36,176,899,576</td>
<td align="right">22.0%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">15,092,972,015</td>
<td align="right">7.5%</td>
<td align="right">16,593,152,252</td>
<td align="right">8.3%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">1,983,705,759</td>
<td align="right"></td>
<td align="right">2,169,609,309</td>
<td align="right"></td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,016,667</td>
<td align="right"></td>
<td align="right">5,500,090</td>
<td align="right"></td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">44,069,519,978</td>
<td align="right">21.8%</td>
<td align="right">47,325,331,284</td>
<td align="right">23.6%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">81,645,254,772</td>
<td align="right">49.5%</td>
<td align="right">76,276,236,821</td>
<td align="right">46.5%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">53,026,578</td>
<td align="right"></td>
<td align="right">56,156,233</td>
<td align="right"></td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">86,859,091,957</td>
<td align="right">43.0%</td>
<td align="right">82,299,549,236</td>
<td align="right">41.0%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">58,251,983</td>
<td align="right"></td>
<td align="right">60,866,289</td>
<td align="right"></td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">43,367,147,929</td>
<td align="right">26.3%</td>
<td align="right">42,177,563,892</td>
<td align="right">25.7%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">55,978,484,538</td>
<td align="right">27.7%</td>
<td align="right">54,486,428,704</td>
<td align="right">27.1%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,551,988</td>
<td align="right">0.4%</td>
<td align="right">71,143,689</td>
<td align="right">0.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,065,059,658</td>
<td align="right"></td>
<td align="right">3,075,157,077</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,408,565,692</td>
<td align="right"></td>
<td align="right">8,435,873,615</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,408,399,467</td>
<td align="right">44.9%</td>
<td align="right">8,435,702,430</td>
<td align="right">45.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,886,688,083</td>
<td align="right"></td>
<td align="right">10,914,612,704</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,222,965,711</td>
<td align="right">54.6%</td>
<td align="right">10,248,518,012</td>
<td align="right">54.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,300,922,798</td>
<td align="right">55.1%</td>
<td align="right">10,326,063,866</td>
<td align="right">55.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,405,099</td>
<td align="right">0.0%</td>
<td align="right">6,402,165</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">176,922,238</td>
<td align="right"></td>
<td align="right">177,000,960</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,443,538</td>
<td align="right">2.5%</td>
<td align="right">4,443,533</td>
<td align="right">2.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">392,276</td>
<td align="right">0.2%</td>
<td align="right">392,276</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">4,404</td>
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
<td align="right">362,011</td>
<td align="right">101,029,246</td>
<td align="right">19,007,360,987</td>
<td align="right">362,383</td>
<td align="right">100,829,000</td>
<td align="right">18,991,579,002</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,245,997,730</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,246,116,272</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">3,833</td>
<td align="right">0.5%</td>
<td align="right">521</td>
<td align="right">0.3%</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,707</td>
<td align="right">0.1%</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">757,865</td>
<td align="right">50.5%</td>
<td align="right">154,082</td>
<td align="right">22.4%</td>
<td align="right">-79.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">14,683</td>
<td align="right">1.0%</td>
<td align="right">3,250</td>
<td align="right">0.5%</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,499,788</td>
<td align="right"></td>
<td align="right">687,702</td>
<td align="right"></td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">7,155</td>
<td align="right">0.5%</td>
<td align="right">3,714</td>
<td align="right">0.5%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">763,596</td>
<td align="right">50.9%</td>
<td align="right">509,482</td>
<td align="right">74.1%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">740,216</td>
<td align="right">49.4%</td>
<td align="right">533,280</td>
<td align="right">77.5%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,621,576,023</td>
<td align="right"></td>
<td align="right">5,953,884,601</td>
<td align="right"></td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">5,027</td>
<td align="right">0.3%</td>
<td align="right">4,100</td>
<td align="right">0.6%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">257,081,680,802</td>
<td align="right">3,373.1%</td>
<td align="right">233,387,458,161</td>
<td align="right">3,919.9%</td>
<td align="right">-9.2%</td>
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
<td align="right">448</td>
<td align="right">0.1%</td>
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
<td align="right">724,213</td>
<td align="right">95.6%</td>
<td align="right">139,822</td>
<td align="right">90.7%</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">757,865</td>
<td align="right"></td>
<td align="right">154,082</td>
<td align="right"></td>
<td align="right">-79.7%</td>
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
<td align="right">53,672</td>
<td align="right">7.1%</td>
<td align="right">15,602</td>
<td align="right">10.1%</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">137,986</td>
<td align="right">18.2%</td>
<td align="right">33,380</td>
<td align="right">21.7%</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">261,811</td>
<td align="right">34.5%</td>
<td align="right">47,348</td>
<td align="right">30.7%</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">196,578</td>
<td align="right">25.9%</td>
<td align="right">37,416</td>
<td align="right">24.3%</td>
<td align="right">-81.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">81,726</td>
<td align="right">10.8%</td>
<td align="right">13,267</td>
<td align="right">8.6%</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">22,462</td>
<td align="right">3.0%</td>
<td align="right">6,226</td>
<td align="right">4.0%</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">3,350</td>
<td align="right">0.4%</td>
<td align="right">801</td>
<td align="right">0.5%</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">-85.0%</td>
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
<td align="right">10,901</td>
<td align="right">1.4%</td>
<td align="right">1,612</td>
<td align="right">1.0%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">123,619</td>
<td align="right">16.3%</td>
<td align="right">24,265</td>
<td align="right">15.7%</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">142,071</td>
<td align="right">18.7%</td>
<td align="right">45,318</td>
<td align="right">29.4%</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">286,386</td>
<td align="right">37.8%</td>
<td align="right">40,838</td>
<td align="right">26.5%</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">119,625</td>
<td align="right">15.8%</td>
<td align="right">19,217</td>
<td align="right">12.5%</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">33,499</td>
<td align="right">4.4%</td>
<td align="right">6,671</td>
<td align="right">4.3%</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">7,201</td>
<td align="right">1.0%</td>
<td align="right">1,759</td>
<td align="right">1.1%</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">911</td>
<td align="right">0.1%</td>
<td align="right">142</td>
<td align="right">0.1%</td>
<td align="right">-84.4%</td>
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
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">8,801,643</td>
<td align="right">92,960</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">3,051,546</td>
<td align="right">283,685</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">212,381</td>
<td align="right">22,841</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">51,974,351</td>
<td align="right">11,199,182</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">1,160,472</td>
<td align="right">269,094</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right">911,840</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">985,534</td>
<td align="right">269,094</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">2,886,257</td>
<td align="right">950,100</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">768,270</td>
<td align="right">1,276,286</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">768,354</td>
<td align="right">1,276,286</td>
<td align="right">66.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">11,216,753</td>
<td align="right">3,816,110</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,311,207</td>
<td align="right">804,753</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">36,811,552</td>
<td align="right">59,209,050</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">29,924,329</td>
<td align="right">13,086,685</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,334,286</td>
<td align="right">1,055,094</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">18,513,662</td>
<td align="right">9,025,577</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,702,690</td>
<td align="right">20,074,240</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">4,016,906</td>
<td align="right">2,005,800</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">4,015,749</td>
<td align="right">2,005,800</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">80,630,734</td>
<td align="right">40,346,440</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">79,476,594</td>
<td align="right">40,346,440</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">203,603,853</td>
<td align="right">114,878,164</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">52,848,211</td>
<td align="right">31,302,033</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">22,288,265</td>
<td align="right">13,431,121</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">465,532,946</td>
<td align="right">285,434,353</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,143,524</td>
<td align="right">5,009,660</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">461,819,786</td>
<td align="right">285,243,433</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,292,333</td>
<td align="right">5,840,025</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">5,658,746</td>
<td align="right">3,666,954</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">145,648,879</td>
<td align="right">95,416,023</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,095</td>
<td align="right">48,806,620</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,095</td>
<td align="right">48,806,620</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">107,637,275</td>
<td align="right">72,263,795</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">107,637,275</td>
<td align="right">72,263,795</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">169,495,674</td>
<td align="right">113,897,019</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">25,385,330</td>
<td align="right">17,620,977</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">275,310,706</td>
<td align="right">192,564,294</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">25,857,015</td>
<td align="right">18,679,441</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">363,504,440</td>
<td align="right">266,326,189</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">453,197,287</td>
<td align="right">333,136,308</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">117,678,221</td>
<td align="right">86,933,312</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">21,670,875</td>
<td align="right">16,296,041</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,279,211</td>
<td align="right">962,182</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">605,977,982</td>
<td align="right">462,257,677</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,702,499,212</td>
<td align="right">5,128,038,828</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">19,879,894</td>
<td align="right">15,371,541</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">63,449,000</td>
<td align="right">49,136,280</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">28,357,862</td>
<td align="right">22,034,073</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">28,357,862</td>
<td align="right">22,034,073</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">87,737,821</td>
<td align="right">68,457,345</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,621,576,023</td>
<td align="right">5,953,884,601</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">43,052,750</td>
<td align="right">33,753,890</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">177,416,067</td>
<td align="right">139,978,680</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">117,228,898</td>
<td align="right">92,553,142</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,119,078,046</td>
<td align="right">1,680,684,095</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">163,271,935</td>
<td align="right">196,777,579</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,004,755,806</td>
<td align="right">2,390,356,768</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,180,615</td>
<td align="right">3,329,620</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">35,394,006</td>
<td align="right">28,239,812</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">259,693,391</td>
<td align="right">209,781,681</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">36,117,144</td>
<td align="right">29,516,098</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">10,020,664,935</td>
<td align="right">8,239,513,799</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,024,245,989</td>
<td align="right">4,976,185,453</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">804,660,876</td>
<td align="right">664,704,187</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">43,096,156</td>
<td align="right">35,701,028</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">43,094,473</td>
<td align="right">35,700,508</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">53,860,028</td>
<td align="right">44,653,415</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,495,768,332</td>
<td align="right">1,245,166,050</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,764,608,141</td>
<td align="right">2,310,754,054</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,406,761,729</td>
<td align="right">1,177,322,562</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,320,280,619</td>
<td align="right">1,105,338,639</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,404,115,290</td>
<td align="right">1,176,767,918</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,922,897,506</td>
<td align="right">1,613,718,397</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">866,072,656</td>
<td align="right">727,065,667</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,334,097,671</td>
<td align="right">5,319,526,484</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">98,890,180</td>
<td align="right">83,292,292</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">631,490,186</td>
<td align="right">532,764,645</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">730,777,811</td>
<td align="right">617,994,204</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,802,432,717</td>
<td align="right">2,370,589,812</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">302,238,642</td>
<td align="right">256,405,396</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">191,593,045</td>
<td align="right">162,703,500</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">227,251,680</td>
<td align="right">193,002,615</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,757,922,099</td>
<td align="right">1,493,475,829</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">18,374,856</td>
<td align="right">15,615,269</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">527,503,734</td>
<td align="right">448,911,593</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">7,403,784</td>
<td align="right">6,334,337</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">83,322,920</td>
<td align="right">71,426,907</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">18,156,248</td>
<td align="right">15,580,427</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">337,786,279</td>
<td align="right">290,685,745</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,989,358,428</td>
<td align="right">1,712,834,747</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">37,258,694</td>
<td align="right">32,096,295</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">37,258,694</td>
<td align="right">32,096,295</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">896,544,983</td>
<td align="right">773,625,227</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">158,628,492</td>
<td align="right">136,885,328</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">83,129,150</td>
<td align="right">94,384,954</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,005,141,459</td>
<td align="right">1,733,755,475</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">125,787,016</td>
<td align="right">108,946,532</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,179,645,999</td>
<td align="right">1,023,688,562</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,478,901,872</td>
<td align="right">2,163,350,834</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">67,866,694</td>
<td align="right">59,300,096</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">102,791,007</td>
<td align="right">115,312,241</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">66,443,244</td>
<td align="right">58,807,376</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">178,978,160</td>
<td align="right">158,454,537</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,652,769,734</td>
<td align="right">3,250,436,345</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">774,960,187</td>
<td align="right">692,216,660</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">590,785,428</td>
<td align="right">528,467,702</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,095,360,835</td>
<td align="right">1,874,623,323</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">300,514,969</td>
<td align="right">269,689,930</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">674,421,589</td>
<td align="right">606,665,689</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">209,501,006</td>
<td align="right">188,830,664</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,943,174,725</td>
<td align="right">2,661,705,216</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,106,745,281</td>
<td align="right">1,000,959,779</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">272,941,994</td>
<td align="right">247,143,871</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">9,069,133</td>
<td align="right">8,216,480</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">739,194,499</td>
<td align="right">669,891,950</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">894,477,343</td>
<td align="right">811,609,899</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">296,760,244</td>
<td align="right">269,689,930</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,005,730,687</td>
<td align="right">1,825,331,358</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">921,881,683</td>
<td align="right">839,675,409</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">422,744,580</td>
<td align="right">386,479,727</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,890,982,849</td>
<td align="right">4,485,699,890</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">226,563,409</td>
<td align="right">208,217,711</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">807,799,087</td>
<td align="right">742,544,163</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">61,540,751</td>
<td align="right">56,577,912</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">564,784,350</td>
<td align="right">519,500,440</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,285,237,073</td>
<td align="right">3,022,666,327</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,206,588,396</td>
<td align="right">5,712,721,012</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">526,213,781</td>
<td align="right">484,450,699</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">525,336,075</td>
<td align="right">483,780,975</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">314,977,011</td>
<td align="right">290,227,067</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">75,000,067</td>
<td align="right">69,120,537</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">75,353,484</td>
<td align="right">69,484,581</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">93,785,085</td>
<td align="right">86,481,280</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,860,182,527</td>
<td align="right">2,641,158,426</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">41,852,739</td>
<td align="right">38,716,154</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">501,464,695</td>
<td align="right">464,009,361</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">829,466,263</td>
<td align="right">767,609,041</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">341,971,191</td>
<td align="right">317,581,931</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">34,201,780</td>
<td align="right">31,780,700</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,396,341,168</td>
<td align="right">1,300,139,988</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,039,429,692</td>
<td align="right">1,905,213,331</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">22,767,003</td>
<td align="right">24,255,140</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">594,850,355</td>
<td align="right">556,321,353</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">784,620,075</td>
<td align="right">733,937,843</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">21,174,582,735</td>
<td align="right">19,826,720,388</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">179,390,878</td>
<td align="right">168,053,693</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">593,831,795</td>
<td align="right">556,321,353</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,941,907,102</td>
<td align="right">1,821,873,087</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">559,294,625</td>
<td align="right">524,814,317</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">178,124,484</td>
<td align="right">167,146,768</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,630,823,581</td>
<td align="right">8,101,194,693</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,527,364</td>
<td align="right">4,250,435</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">17,593,101,377</td>
<td align="right">16,564,289,945</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,399,603,549</td>
<td align="right">3,201,107,736</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">736,793,537</td>
<td align="right">694,098,844</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,409,296,019</td>
<td align="right">4,155,439,983</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,232,161,891</td>
<td align="right">1,162,520,932</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">436,517,302</td>
<td align="right">413,034,372</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,330,713,256</td>
<td align="right">5,045,746,191</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">193,453,171</td>
<td align="right">183,219,846</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">80,900,663</td>
<td align="right">85,056,914</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,002,488,208</td>
<td align="right">1,899,919,641</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">63,098,400</td>
<td align="right">59,958,512</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,156,668,472</td>
<td align="right">2,051,518,158</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">881,983,157</td>
<td align="right">839,213,456</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,399,088,912</td>
<td align="right">2,285,629,198</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">795,290,375</td>
<td align="right">759,052,833</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">530,206,094</td>
<td align="right">507,577,224</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">118,444,399</td>
<td align="right">113,392,083</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">123,202,141</td>
<td align="right">118,131,408</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">25,853,649</td>
<td align="right">24,802,451</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,060,624,789</td>
<td align="right">1,017,629,919</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,751,128,646</td>
<td align="right">1,680,567,774</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,019,763,330</td>
<td align="right">979,818,286</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,795,104,547</td>
<td align="right">9,429,141,861</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">35,441,180</td>
<td align="right">34,156,012</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">35,441,180</td>
<td align="right">34,156,012</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,204,346,129</td>
<td align="right">4,051,911,197</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,693,511,112</td>
<td align="right">4,525,760,358</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,485,153,368</td>
<td align="right">1,435,349,991</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">736,774,111</td>
<td align="right">715,477,691</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,918,275,434</td>
<td align="right">1,863,762,157</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">42,226,283</td>
<td align="right">43,381,420</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,568,722,227</td>
<td align="right">2,501,070,316</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,975,912,583</td>
<td align="right">2,907,596,856</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">74,715,797</td>
<td align="right">73,091,220</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">503,959,807</td>
<td align="right">514,106,662</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">246,071,155</td>
<td align="right">250,904,030</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,565,718,280</td>
<td align="right">1,536,122,756</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,002,590,800</td>
<td align="right">984,334,786</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">80,925,680</td>
<td align="right">79,453,758</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,076,518,149</td>
<td align="right">3,020,973,354</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">390,244,323</td>
<td align="right">383,249,170</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">801,450,591</td>
<td align="right">787,198,454</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,389,320,417</td>
<td align="right">1,365,325,551</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,328,633,285</td>
<td align="right">4,257,822,690</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">3,870,811</td>
<td align="right">3,809,260</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">619,576,264</td>
<td align="right">610,187,021</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">266,369,682</td>
<td align="right">262,575,675</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">522,378,610</td>
<td align="right">515,005,979</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,103,255,598</td>
<td align="right">1,089,415,962</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,864,526,397</td>
<td align="right">3,817,674,747</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,360,520,048</td>
<td align="right">1,345,842,512</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,652,202</td>
<td align="right">60,002,028</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">614,600,720</td>
<td align="right">608,302,395</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">98,765,162</td>
<td align="right">97,840,138</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">409,752,121</td>
<td align="right">406,636,857</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,926,697,367</td>
<td align="right">1,937,244,198</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">870,731,195</td>
<td align="right">866,723,358</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,283,751</td>
<td align="right">47,130,180</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">124,940,020</td>
<td align="right">124,542,420</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,218,767,319</td>
<td align="right">1,215,496,277</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">72,549,690</td>
<td align="right">72,403,528</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">112,470,560</td>
<td align="right">112,265,020</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">72,535,267</td>
<td align="right">72,403,528</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">468,875,893</td>
<td align="right">468,285,056</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">311,267,532</td>
<td align="right">311,527,996</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,236,513</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">949,358</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">857,239</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">840,872</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">653,477</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">241,920</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">57,330</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">40,539</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">17,263</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">14,752</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">4,267</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_WITH_SPEC</td>
<td align="right">2,417</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">1,905</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">897</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">462</td>
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
<td align="left">CALL</td>
<td align="right">24,885</td>
<td align="right">12,522</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">52,771</td>
<td align="right">27,443</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">30,637</td>
<td align="right">25,899</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">2,057</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">126</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">248</td>
<td align="right">160</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">248</td>
<td align="right">160</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,592</td>
<td align="right">22,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">35</td>
<td align="right">35</td>
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
<td align="right">42</td>
<td align="right">42</td>
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
<td align="right">1,857</td>
<td align="right">1,857</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-13
