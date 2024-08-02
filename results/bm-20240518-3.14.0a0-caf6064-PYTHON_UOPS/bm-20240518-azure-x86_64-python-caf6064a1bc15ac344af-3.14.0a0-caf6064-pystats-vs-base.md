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
<td align="right">4,918,210,502</td>
<td align="right">1,716,254</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">80,934,935</td>
<td align="right">211,830</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">8,123,940</td>
<td align="right">161,920</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">162,427,160</td>
<td align="right">7,254,180</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">832,088,245</td>
<td align="right">47,426,934</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">133,515,680</td>
<td align="right">8,000,960</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">233,231,273</td>
<td align="right">18,673,600</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,783,349,625</td>
<td align="right">169,518,869</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">76,975,583</td>
<td align="right">7,498,299</td>
<td align="right">-90.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">665,647,651</td>
<td align="right">67,887,609</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">15,058,629</td>
<td align="right">1,571,798</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">189,311,744</td>
<td align="right">22,329,447</td>
<td align="right">-88.2%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">12,200,025</td>
<td align="right">1,470,189</td>
<td align="right">-87.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">589,494,006</td>
<td align="right">78,170,947</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,797,519</td>
<td align="right">244,702</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,382,308,235</td>
<td align="right">190,037,448</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,933,562,434</td>
<td align="right">275,392,877</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">232,769,421</td>
<td align="right">33,291,807</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">448,579,130</td>
<td align="right">64,931,202</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">650,362,962</td>
<td align="right">94,708,381</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">506,727,981</td>
<td align="right">74,001,755</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">457,475,929</td>
<td align="right">72,694,786</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">212,903,041</td>
<td align="right">39,478,532</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,680,794,100</td>
<td align="right">330,344,288</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,628,693,600</td>
<td align="right">324,968,537</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">515,619,781</td>
<td align="right">108,604,067</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,323,572,970</td>
<td align="right">290,127,858</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,506,286,797</td>
<td align="right">361,781,305</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">195,351,500</td>
<td align="right">48,010,469</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,573,273,520</td>
<td align="right">891,647,565</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">43,290,669</td>
<td align="right">10,875,607</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,623,145,856</td>
<td align="right">414,723,627</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">113,464,581</td>
<td align="right">29,852,021</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">284,550,316</td>
<td align="right">83,959,432</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">468,153,924</td>
<td align="right">142,942,601</td>
<td align="right">-69.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">211,756,585</td>
<td align="right">65,832,348</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">469,958,523</td>
<td align="right">147,332,791</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">151,198,871</td>
<td align="right">49,173,364</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">981,942,082</td>
<td align="right">321,382,508</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,083,195,083</td>
<td align="right">686,921,984</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,788,411,283</td>
<td align="right">945,797,338</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,477,247,973</td>
<td align="right">513,573,444</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,265,224,322</td>
<td align="right">451,231,844</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,291,750,443</td>
<td align="right">829,153,484</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">320,387,167</td>
<td align="right">116,488,229</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">279,546,363</td>
<td align="right">105,032,286</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,045,488,543</td>
<td align="right">4,605,966,623</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">152,393,373</td>
<td align="right">58,414,807</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">127,689,436</td>
<td align="right">49,009,215</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">15,881,893,516</td>
<td align="right">6,163,573,476</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">839,534,610</td>
<td align="right">326,550,988</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">15,807,230,136</td>
<td align="right">6,197,242,523</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,217,496</td>
<td align="right">32,546,618</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">417,828,865</td>
<td align="right">166,890,770</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,059,311,756</td>
<td align="right">428,375,958</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">176,569,957</td>
<td align="right">72,217,742</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">979,722,058</td>
<td align="right">402,422,464</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">8,204,680</td>
<td align="right">3,464,680</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">434,338,381</td>
<td align="right">188,135,650</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">853,396,932</td>
<td align="right">374,905,413</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">14,669,336,971</td>
<td align="right">6,503,401,900</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">891,771,637</td>
<td align="right">402,244,339</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">155,853,290</td>
<td align="right">70,460,447</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">68,777,471</td>
<td align="right">31,595,866</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,181,660</td>
<td align="right">546,220</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,981,056,916</td>
<td align="right">1,386,597,206</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">360,262,690</td>
<td align="right">168,997,028</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,939,194,778</td>
<td align="right">3,290,500,229</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">187,737,922</td>
<td align="right">89,262,128</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">660,381,394</td>
<td align="right">315,548,012</td>
<td align="right">-52.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,462,727,102</td>
<td align="right">1,208,721,294</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">840,053,425</td>
<td align="right">414,206,397</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">394,410,522</td>
<td align="right">195,333,298</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,181,688,784</td>
<td align="right">586,826,609</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">12,299,520</td>
<td align="right">6,167,569</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">115,177,241</td>
<td align="right">58,107,471</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">544,386,328</td>
<td align="right">276,951,454</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">50,075,574,998</td>
<td align="right">25,724,945,846</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">242,408,085</td>
<td align="right">126,399,035</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">18,058,241</td>
<td align="right">9,580,222</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">2,054,975,150</td>
<td align="right">1,110,245,700</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,270,240</td>
<td align="right">1,781,582</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,038,778,491</td>
<td align="right">1,132,668,649</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,842,899,742</td>
<td align="right">1,587,360,247</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">253,893,090</td>
<td align="right">142,209,048</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">14,132,500</td>
<td align="right">8,087,720</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">437,668,371</td>
<td align="right">250,972,814</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,591,065,324</td>
<td align="right">2,662,217,599</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">83,960</td>
<td align="right">49,180</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">357,442,014</td>
<td align="right">209,395,733</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,283,269,991</td>
<td align="right">3,725,251,559</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">199,269,801</td>
<td align="right">118,421,941</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">249,500,050</td>
<td align="right">148,276,749</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">709,539,800</td>
<td align="right">424,509,973</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">384,902,924</td>
<td align="right">233,855,514</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,259,711,286</td>
<td align="right">766,366,522</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">65,856,854</td>
<td align="right">40,066,768</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">354,411,568</td>
<td align="right">215,902,818</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,785,771,713</td>
<td align="right">1,697,570,491</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">86,958,388</td>
<td align="right">53,096,781</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">679,629,446</td>
<td align="right">416,399,324</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,244,584</td>
<td align="right">13,028,301</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,244,724</td>
<td align="right">13,036,061</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">689,112,584</td>
<td align="right">428,442,130</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">519,275,877</td>
<td align="right">324,101,945</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,683,162,479</td>
<td align="right">4,800,087,958</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,773,764</td>
<td align="right">13,040,388</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">275,583,815</td>
<td align="right">175,140,560</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">481,704,296</td>
<td align="right">321,160,258</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">155,631,080</td>
<td align="right">105,984,240</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">177,060,196</td>
<td align="right">122,051,234</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">1,041,440</td>
<td align="right">719,420</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">885,541,179</td>
<td align="right">618,776,298</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">74,755,121</td>
<td align="right">52,501,661</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">139,685,160</td>
<td align="right">98,881,660</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,428,192,390</td>
<td align="right">1,016,096,910</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">148,346,402</td>
<td align="right">105,667,962</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">499,540,859</td>
<td align="right">356,422,710</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">558,292,837</td>
<td align="right">398,712,768</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">661,054,995</td>
<td align="right">475,961,479</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">5,615,555,109</td>
<td align="right">4,061,092,894</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">8,969,654,179</td>
<td align="right">6,593,324,643</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,974,996</td>
<td align="right">4,407,098</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,542,751,990</td>
<td align="right">1,144,482,447</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">626,464,347</td>
<td align="right">467,757,397</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">389,840,137</td>
<td align="right">297,847,708</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">196,453,166</td>
<td align="right">150,687,214</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,417,397,980</td>
<td align="right">3,409,759,726</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">4,878,846,952</td>
<td align="right">3,796,924,825</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">28,740</td>
<td align="right">22,800</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">418,530,517</td>
<td align="right">335,464,545</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">64,954,158</td>
<td align="right">52,179,020</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,156,119,149</td>
<td align="right">932,976,957</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,770,092,780</td>
<td align="right">4,787,222,927</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">2,117,331,540</td>
<td align="right">1,774,753,913</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">225,577,542</td>
<td align="right">190,270,311</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">369,174,772</td>
<td align="right">312,556,368</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,040</td>
<td align="right">900</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,863,278</td>
<td align="right">9,474,855</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">119,293,520</td>
<td align="right">104,674,809</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">2,162,071,144</td>
<td align="right">1,925,267,898</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,240</td>
<td align="right">2,000</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,260</td>
<td align="right">2,020</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">88,176,449</td>
<td align="right">83,084,560</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">306,403,408</td>
<td align="right">290,425,768</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,180</td>
<td align="right">25,780</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">6,981,424</td>
<td align="right">6,665,757</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,395,992,103</td>
<td align="right">1,338,063,210</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,480,980</td>
<td align="right">90,669,540</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">94,738,323</td>
<td align="right">91,106,465</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,811,540,046</td>
<td align="right">2,899,598,307</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">273,866,684</td>
<td align="right">266,298,443</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,823,558</td>
<td align="right">1,788,424</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">507,140</td>
<td align="right">497,860</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">47,436,284</td>
<td align="right">46,613,180</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,198,480</td>
<td align="right">90,664,420</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,892,827</td>
<td align="right">80,976,809</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">16,184</td>
<td align="right">16,007</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">117,125,601</td>
<td align="right">116,115,426</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,241,893</td>
<td align="right">9,213,258</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,371,134</td>
<td align="right">20,308,838</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">147,220</td>
<td align="right">146,780</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">229,269,611</td>
<td align="right">228,622,190</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,665,749</td>
<td align="right">9,649,060</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,874,289</td>
<td align="right">1,873,256</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">94,200</td>
<td align="right">94,160</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,917,586</td>
<td align="right">555,700,744</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,345,149</td>
<td align="right">233,313,195</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">692,698</td>
<td align="right">692,629</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,225,749</td>
<td align="right">786,216,135</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,026,591</td>
<td align="right">402,024,625</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,894</td>
<td align="right">173,318,630</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,460</td>
<td align="right">38,846,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,760</td>
<td align="right">38,845,760</td>
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
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">2,995,200</td>
<td align="right">2,995,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">150,560</td>
<td align="right">150,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">90,000</td>
<td align="right">90,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">2,318,820,868</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,846,241,863</td>
<td align="right">83.7%</td>
<td align="right">2,260,612,468</td>
<td align="right">80.6%</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,524,877,544</td>
<td align="right">16.3%</td>
<td align="right">541,360,250</td>
<td align="right">19.3%</td>
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
<td align="right">50,340,300</td>
<td align="right">0.5%</td>
<td align="right">29,500,920</td>
<td align="right">1.1%</td>
<td align="right">-41.4%</td>
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
<td align="right">992,589</td>
<td align="right">36.6%</td>
<td align="right">592,378</td>
<td align="right">34.6%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,718,140</td>
<td align="right">63.4%</td>
<td align="right">1,121,736</td>
<td align="right">65.4%</td>
<td align="right">-34.7%</td>
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
<td align="left">lshift</td>
<td align="right">28,765</td>
<td align="right">1.7%</td>
<td align="right">5,030</td>
<td align="right">0.4%</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">216,760</td>
<td align="right">12.6%</td>
<td align="right">38,056</td>
<td align="right">3.4%</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">36,944</td>
<td align="right">2.2%</td>
<td align="right">8,609</td>
<td align="right">0.8%</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">66,728</td>
<td align="right">3.9%</td>
<td align="right">15,919</td>
<td align="right">1.4%</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">17,763</td>
<td align="right">1.0%</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">-73.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">256,567</td>
<td align="right">14.9%</td>
<td align="right">90,965</td>
<td align="right">8.1%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">29,443</td>
<td align="right">1.7%</td>
<td align="right">10,464</td>
<td align="right">0.9%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">33,603</td>
<td align="right">2.0%</td>
<td align="right">12,944</td>
<td align="right">1.2%</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">68,959</td>
<td align="right">4.0%</td>
<td align="right">29,082</td>
<td align="right">2.6%</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">52,672</td>
<td align="right">3.1%</td>
<td align="right">32,096</td>
<td align="right">2.9%</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66,521</td>
<td align="right">3.9%</td>
<td align="right">43,856</td>
<td align="right">3.9%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">23,481</td>
<td align="right">1.4%</td>
<td align="right">15,508</td>
<td align="right">1.4%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">15,260</td>
<td align="right">0.9%</td>
<td align="right">10,620</td>
<td align="right">0.9%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">16,126</td>
<td align="right">0.9%</td>
<td align="right">12,092</td>
<td align="right">1.1%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">5,500</td>
<td align="right">0.3%</td>
<td align="right">5,220</td>
<td align="right">0.5%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,760</td>
<td align="right">0.2%</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">777,954</td>
<td align="right">45.3%</td>
<td align="right">781,612</td>
<td align="right">69.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,894</td>
<td align="right">0.1%</td>
<td align="right">1,899</td>
<td align="right">0.2%</td>
<td align="right">0.3%</td>
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
<td align="right">1,627,536,287</td>
<td align="right">26.0%</td>
<td align="right">416,215,669</td>
<td align="right">24.1%</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,629,421,372</td>
<td align="right">74.0%</td>
<td align="right">1,309,623,569</td>
<td align="right">75.9%</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,045,352</td>
<td align="right">0.1%</td>
<td align="right">1,753,860</td>
<td align="right">0.1%</td>
<td align="right">-65.2%</td>
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
<td align="right">468,385</td>
<td align="right">71.5%</td>
<td align="right">148,575</td>
<td align="right">56.7%</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">186,536</td>
<td align="right">28.5%</td>
<td align="right">113,243</td>
<td align="right">43.3%</td>
<td align="right">-39.3%</td>
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
<td align="right">35,080</td>
<td align="right">7.5%</td>
<td align="right">1,080</td>
<td align="right">0.7%</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">157,600</td>
<td align="right">33.6%</td>
<td align="right">16,200</td>
<td align="right">10.9%</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">117,662</td>
<td align="right">25.1%</td>
<td align="right">30,991</td>
<td align="right">20.9%</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">57,380</td>
<td align="right">12.3%</td>
<td align="right">30,220</td>
<td align="right">20.3%</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">74,080</td>
<td align="right">15.8%</td>
<td align="right">44,000</td>
<td align="right">29.6%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">980</td>
<td align="right">0.2%</td>
<td align="right">780</td>
<td align="right">0.5%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,620</td>
<td align="right">1.2%</td>
<td align="right">5,320</td>
<td align="right">3.6%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">123</td>
<td align="right">0.0%</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,760</td>
<td align="right">4.2%</td>
<td align="right">19,760</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,086,951,349</td>
<td align="right">97.3%</td>
<td align="right">6,884,821,441</td>
<td align="right">95.6%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">41,300</td>
<td align="right">0.0%</td>
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">248,411,694</td>
<td align="right">1.8%</td>
<td align="right">203,410,049</td>
<td align="right">2.8%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">360,232,848</td>
<td align="right">2.7%</td>
<td align="right">315,130,700</td>
<td align="right">4.4%</td>
<td align="right">-12.5%</td>
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
<td align="right">5,226,081</td>
<td align="right">98.5%</td>
<td align="right">4,318,655</td>
<td align="right">98.3%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">78,366</td>
<td align="right">1.5%</td>
<td align="right">76,120</td>
<td align="right">1.7%</td>
<td align="right">-2.9%</td>
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
<td align="right">700</td>
<td align="right">0.9%</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">1,960</td>
<td align="right">2.5%</td>
<td align="right">580</td>
<td align="right">0.8%</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">9,520</td>
<td align="right">12.1%</td>
<td align="right">8,340</td>
<td align="right">11.0%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">68,366</td>
<td align="right">87.2%</td>
<td align="right">67,300</td>
<td align="right">88.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,100</td>
<td align="right">4.0%</td>
<td align="right">3,100</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">480</td>
<td align="right">0.6%</td>
<td align="right">480</td>
<td align="right">0.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,822,305,715</td>
<td align="right">96.0%</td>
<td align="right">2,790,903,083</td>
<td align="right">95.6%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">243,499,499</td>
<td align="right">4.0%</td>
<td align="right">126,935,564</td>
<td align="right">4.4%</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,377,331</td>
<td align="right">0.0%</td>
<td align="right">741,495</td>
<td align="right">0.0%</td>
<td align="right">-46.2%</td>
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
<td align="right">201,544</td>
<td align="right">70.5%</td>
<td align="right">138,361</td>
<td align="right">67.5%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">84,373</td>
<td align="right">29.5%</td>
<td align="right">66,605</td>
<td align="right">32.5%</td>
<td align="right">-21.1%</td>
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
<td align="right">9,880</td>
<td align="right">4.9%</td>
<td align="right">1,740</td>
<td align="right">1.3%</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">3,452</td>
<td align="right">1.7%</td>
<td align="right">1,546</td>
<td align="right">1.1%</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">52,131</td>
<td align="right">25.9%</td>
<td align="right">26,036</td>
<td align="right">18.8%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">27,480</td>
<td align="right">13.6%</td>
<td align="right">18,720</td>
<td align="right">13.5%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,300</td>
<td align="right">1.1%</td>
<td align="right">1,640</td>
<td align="right">1.2%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">19,100</td>
<td align="right">9.5%</td>
<td align="right">14,322</td>
<td align="right">10.4%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">34,472</td>
<td align="right">17.1%</td>
<td align="right">26,467</td>
<td align="right">19.1%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,200</td>
<td align="right">0.6%</td>
<td align="right">960</td>
<td align="right">0.7%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">500</td>
<td align="right">0.4%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">23,809</td>
<td align="right">11.8%</td>
<td align="right">20,540</td>
<td align="right">14.8%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,780</td>
<td align="right">6.3%</td>
<td align="right">11,730</td>
<td align="right">8.5%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">14,360</td>
<td align="right">7.1%</td>
<td align="right">14,160</td>
<td align="right">10.2%</td>
<td align="right">-1.4%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,446,635,975</td>
<td align="right">86.3%</td>
<td align="right">381,479,684</td>
<td align="right">61.7%</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">387,222,230</td>
<td align="right">13.7%</td>
<td align="right">236,203,418</td>
<td align="right">38.2%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,546,240</td>
<td align="right">0.1%</td>
<td align="right">2,517,260</td>
<td align="right">0.4%</td>
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
<td align="left">Failure</td>
<td align="right">165,615</td>
<td align="right">73.0%</td>
<td align="right">110,338</td>
<td align="right">65.2%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,319</td>
<td align="right">27.0%</td>
<td align="right">59,018</td>
<td align="right">34.8%</td>
<td align="right">-3.8%</td>
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
<td align="right">35,880</td>
<td align="right">21.7%</td>
<td align="right">16,660</td>
<td align="right">15.1%</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">22,014</td>
<td align="right">13.3%</td>
<td align="right">13,518</td>
<td align="right">12.3%</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">31,341</td>
<td align="right">18.9%</td>
<td align="right">23,020</td>
<td align="right">20.9%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">76,380</td>
<td align="right">46.1%</td>
<td align="right">57,140</td>
<td align="right">51.8%</td>
<td align="right">-25.2%</td>
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
<td align="right">173,295,389</td>
<td align="right">4.3%</td>
<td align="right">174,702</td>
<td align="right">0.0%</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,325,274,864</td>
<td align="right">83.0%</td>
<td align="right">344,771,289</td>
<td align="right">82.3%</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">676,416,569</td>
<td align="right">16.9%</td>
<td align="right">74,034,801</td>
<td align="right">17.7%</td>
<td align="right">-89.1%</td>
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
<td align="right">3,318,726</td>
<td align="right">92.0%</td>
<td align="right">47,867</td>
<td align="right">33.8%</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">288,075</td>
<td align="right">8.0%</td>
<td align="right">93,789</td>
<td align="right">66.2%</td>
<td align="right">-67.4%</td>
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
<td align="right">29,280</td>
<td align="right">10.2%</td>
<td align="right">1,540</td>
<td align="right">1.6%</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">41,833</td>
<td align="right">14.5%</td>
<td align="right">9,568</td>
<td align="right">10.2%</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">5,800</td>
<td align="right">2.0%</td>
<td align="right">1,380</td>
<td align="right">1.5%</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">2,280</td>
<td align="right">0.8%</td>
<td align="right">560</td>
<td align="right">0.6%</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">21,980</td>
<td align="right">7.6%</td>
<td align="right">6,840</td>
<td align="right">7.3%</td>
<td align="right">-68.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">12,240</td>
<td align="right">4.2%</td>
<td align="right">3,840</td>
<td align="right">4.1%</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">107,888</td>
<td align="right">37.5%</td>
<td align="right">36,541</td>
<td align="right">39.0%</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">28,154</td>
<td align="right">9.8%</td>
<td align="right">10,160</td>
<td align="right">10.8%</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">660</td>
<td align="right">0.2%</td>
<td align="right">320</td>
<td align="right">0.3%</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">5,980</td>
<td align="right">2.1%</td>
<td align="right">3,220</td>
<td align="right">3.4%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">14,020</td>
<td align="right">4.9%</td>
<td align="right">7,720</td>
<td align="right">8.2%</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">9,760</td>
<td align="right">3.4%</td>
<td align="right">6,460</td>
<td align="right">6.9%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">7,920</td>
<td align="right">2.7%</td>
<td align="right">5,420</td>
<td align="right">5.8%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">220</td>
<td align="right">0.2%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">959,589,174</td>
<td align="right">4.4%</td>
<td align="right">246,698,378</td>
<td align="right">1.8%</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,977,134,683</td>
<td align="right">13.5%</td>
<td align="right">1,373,341,032</td>
<td align="right">10.2%</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">19,035,835,893</td>
<td align="right">86.4%</td>
<td align="right">12,140,059,939</td>
<td align="right">89.8%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">321,100</td>
<td align="right">0.0%</td>
<td align="right">320,700</td>
<td align="right">0.0%</td>
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
<td align="right">18,734,008</td>
<td align="right">88.2%</td>
<td align="right">5,198,036</td>
<td align="right">86.3%</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,498,974</td>
<td align="right">11.8%</td>
<td align="right">827,959</td>
<td align="right">13.7%</td>
<td align="right">-66.9%</td>
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
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-95.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">715,921</td>
<td align="right">28.6%</td>
<td align="right">45,267</td>
<td align="right">5.5%</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">997,185</td>
<td align="right">39.9%</td>
<td align="right">266,481</td>
<td align="right">32.2%</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">115,026</td>
<td align="right">4.6%</td>
<td align="right">54,238</td>
<td align="right">6.6%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">152,745</td>
<td align="right">6.1%</td>
<td align="right">85,728</td>
<td align="right">10.4%</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">294,382</td>
<td align="right">11.8%</td>
<td align="right">179,430</td>
<td align="right">21.7%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">20,620</td>
<td align="right">0.8%</td>
<td align="right">14,379</td>
<td align="right">1.7%</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,910</td>
<td align="right">0.7%</td>
<td align="right">13,318</td>
<td align="right">1.6%</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">3,460</td>
<td align="right">0.1%</td>
<td align="right">2,860</td>
<td align="right">0.3%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">22,300</td>
<td align="right">0.9%</td>
<td align="right">19,820</td>
<td align="right">2.4%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">81,353</td>
<td align="right">3.3%</td>
<td align="right">72,998</td>
<td align="right">8.8%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,132</td>
<td align="right">0.2%</td>
<td align="right">5,660</td>
<td align="right">0.7%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">28,720</td>
<td align="right">1.1%</td>
<td align="right">26,700</td>
<td align="right">3.2%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">11,980</td>
<td align="right">0.5%</td>
<td align="right">11,360</td>
<td align="right">1.4%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">16,620</td>
<td align="right">0.7%</td>
<td align="right">15,760</td>
<td align="right">1.9%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,460</td>
<td align="right">0.5%</td>
<td align="right">12,200</td>
<td align="right">1.5%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
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
<td align="right">12,554,267,378</td>
<td align="right">99.8%</td>
<td align="right">7,351,142,151</td>
<td align="right">99.7%</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,320</td>
<td align="right">0.0%</td>
<td align="right">11,300</td>
<td align="right">0.0%</td>
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
<td align="right">482,509</td>
<td align="right">0.0%</td>
<td align="right">450,972</td>
<td align="right">0.0%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,375,394</td>
<td align="right">0.2%</td>
<td align="right">20,312,856</td>
<td align="right">0.3%</td>
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
<td align="left">Success</td>
<td align="right">478,249</td>
<td align="right">100.0%</td>
<td align="right">446,954</td>
<td align="right">100.0%</td>
<td align="right">-6.5%</td>
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
<td align="right">8,224</td>
<td align="right">0.0%</td>
<td align="right">8,127</td>
<td align="right">0.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,716,385</td>
<td align="right">100.0%</td>
<td align="right">82,765,233</td>
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
<td align="right">7,960</td>
<td align="right">100.0%</td>
<td align="right">7,880</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">786,195,089</td>
<td align="right">81.9%</td>
<td align="right">786,185,475</td>
<td align="right">81.9%</td>
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
<td align="right">173,284,454</td>
<td align="right">18.1%</td>
<td align="right">173,284,270</td>
<td align="right">18.1%</td>
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
<td align="right">30,660</td>
<td align="right">0.0%</td>
<td align="right">30,660</td>
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
<td align="right">5,480</td>
<td align="right">8.4%</td>
<td align="right">5,420</td>
<td align="right">8.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,620</td>
<td align="right">91.6%</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
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
<td align="left">list</td>
<td align="right">9,980</td>
<td align="right">16.7%</td>
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">55.7%</td>
<td align="right">33,180</td>
<td align="right">55.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,240</td>
<td align="right">23.9%</td>
<td align="right">14,240</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,220</td>
<td align="right">3.7%</td>
<td align="right">2,220</td>
<td align="right">3.7%</td>
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
<td align="right">150,721,516</td>
<td align="right">3.9%</td>
<td align="right">68,517,053</td>
<td align="right">2.2%</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">216,447,864</td>
<td align="right">5.6%</td>
<td align="right">98,657,960</td>
<td align="right">3.1%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,619,055,776</td>
<td align="right">94.3%</td>
<td align="right">3,053,412,312</td>
<td align="right">96.8%</td>
<td align="right">-15.6%</td>
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
<td align="right">2,944,337</td>
<td align="right">96.5%</td>
<td align="right">1,383,791</td>
<td align="right">95.1%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">106,786</td>
<td align="right">3.5%</td>
<td align="right">71,168</td>
<td align="right">4.9%</td>
<td align="right">-33.4%</td>
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
<td align="right">34,800</td>
<td align="right">32.6%</td>
<td align="right">10,220</td>
<td align="right">14.4%</td>
<td align="right">-70.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,900</td>
<td align="right">7.4%</td>
<td align="right">4,360</td>
<td align="right">6.1%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,900</td>
<td align="right">6.5%</td>
<td align="right">3,940</td>
<td align="right">5.5%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,680</td>
<td align="right">3.4%</td>
<td align="right">2,840</td>
<td align="right">4.0%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">10,700</td>
<td align="right">10.0%</td>
<td align="right">8,580</td>
<td align="right">12.1%</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">840</td>
<td align="right">0.8%</td>
<td align="right">760</td>
<td align="right">1.1%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,720</td>
<td align="right">13.8%</td>
<td align="right">13,760</td>
<td align="right">19.3%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,340</td>
<td align="right">5.0%</td>
<td align="right">5,020</td>
<td align="right">7.1%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">5,060</td>
<td align="right">4.7%</td>
<td align="right">4,840</td>
<td align="right">6.8%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">16,726</td>
<td align="right">15.7%</td>
<td align="right">16,728</td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">448,410,049</td>
<td align="right">33.0%</td>
<td align="right">64,867,394</td>
<td align="right">25.0%</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">909,878,273</td>
<td align="right">67.0%</td>
<td align="right">194,659,176</td>
<td align="right">75.0%</td>
<td align="right">-78.6%</td>
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
<td align="right"></td>
<td align="right"></td>
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
<td align="left">Failure</td>
<td align="right">158,720</td>
<td align="right">92.3%</td>
<td align="right">52,764</td>
<td align="right">82.7%</td>
<td align="right">-66.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,261</td>
<td align="right">7.7%</td>
<td align="right">11,044</td>
<td align="right">17.3%</td>
<td align="right">-16.7%</td>
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
<td align="right">66,240</td>
<td align="right">41.7%</td>
<td align="right">6,480</td>
<td align="right">12.3%</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">9,640</td>
<td align="right">6.1%</td>
<td align="right">1,040</td>
<td align="right">2.0%</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,200</td>
<td align="right">2.0%</td>
<td align="right">780</td>
<td align="right">1.5%</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">34,300</td>
<td align="right">21.6%</td>
<td align="right">10,164</td>
<td align="right">19.3%</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">43,960</td>
<td align="right">27.7%</td>
<td align="right">33,160</td>
<td align="right">62.8%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,360</td>
<td align="right">0.9%</td>
<td align="right">1,120</td>
<td align="right">2.1%</td>
<td align="right">-17.6%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">142,071,995</td>
<td align="right">1.7%</td>
<td align="right">49,195,675</td>
<td align="right">1.0%</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,574,838,144</td>
<td align="right">90.4%</td>
<td align="right">4,383,377,104</td>
<td align="right">89.3%</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">799,524,803</td>
<td align="right">9.5%</td>
<td align="right">523,805,455</td>
<td align="right">10.7%</td>
<td align="right">-34.5%</td>
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
<td align="right">721,679</td>
<td align="right">20.0%</td>
<td align="right">239,179</td>
<td align="right">17.7%</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,880,508</td>
<td align="right">80.0%</td>
<td align="right">1,112,520</td>
<td align="right">82.3%</td>
<td align="right">-61.4%</td>
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
<td align="right">174,026</td>
<td align="right">24.1%</td>
<td align="right">4,587</td>
<td align="right">1.9%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">98,549</td>
<td align="right">13.7%</td>
<td align="right">27,090</td>
<td align="right">11.3%</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">229,031</td>
<td align="right">31.7%</td>
<td align="right">68,581</td>
<td align="right">28.7%</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">27,520</td>
<td align="right">3.8%</td>
<td align="right">13,360</td>
<td align="right">5.6%</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">97,708</td>
<td align="right">13.5%</td>
<td align="right">48,000</td>
<td align="right">20.1%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">28,794</td>
<td align="right">4.0%</td>
<td align="right">14,684</td>
<td align="right">6.1%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">16,560</td>
<td align="right">2.3%</td>
<td align="right">13,720</td>
<td align="right">5.7%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,740</td>
<td align="right">0.2%</td>
<td align="right">1,460</td>
<td align="right">0.6%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">46,291</td>
<td align="right">6.4%</td>
<td align="right">46,237</td>
<td align="right">19.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.1%</td>
<td align="right">1,040</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">420</td>
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
<td align="right">1,768,037</td>
<td align="right">0.1%</td>
<td align="right">215,479</td>
<td align="right">0.0%</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,607,259,105</td>
<td align="right">99.9%</td>
<td align="right">598,545,792</td>
<td align="right">100.0%</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,240</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">Failure</td>
<td align="right">2,874</td>
<td align="right">8.5%</td>
<td align="right">2,079</td>
<td align="right">7.1%</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,848</td>
<td align="right">91.5%</td>
<td align="right">27,144</td>
<td align="right">92.9%</td>
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
<td align="left">sequence</td>
<td align="right">2,234</td>
<td align="right">77.7%</td>
<td align="right">1,439</td>
<td align="right">69.2%</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">13.2%</td>
<td align="right">380</td>
<td align="right">18.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">9.0%</td>
<td align="right">260</td>
<td align="right">12.5%</td>
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
<td align="right">1,811,802,840</td>
<td align="right">0.7%</td>
<td align="right">680,865,890</td>
<td align="right">0.5%</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">27,240,192,141</td>
<td align="right">10.5%</td>
<td align="right">12,702,615,300</td>
<td align="right">9.5%</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">136,644,949,776</td>
<td align="right">52.6%</td>
<td align="right">69,799,344,091</td>
<td align="right">52.3%</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">93,858,668,971</td>
<td align="right">36.2%</td>
<td align="right">50,274,923,393</td>
<td align="right">37.7%</td>
<td align="right">-46.4%</td>
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
<td align="right">676,416,569</td>
<td align="right">7.2%</td>
<td align="right">74,034,801</td>
<td align="right">1.9%</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,627,536,287</td>
<td align="right">17.2%</td>
<td align="right">416,215,669</td>
<td align="right">10.5%</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,524,877,544</td>
<td align="right">16.1%</td>
<td align="right">541,360,250</td>
<td align="right">13.7%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">216,447,864</td>
<td align="right">2.3%</td>
<td align="right">98,657,960</td>
<td align="right">2.5%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,977,134,683</td>
<td align="right">31.5%</td>
<td align="right">1,373,341,032</td>
<td align="right">34.6%</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">243,499,499</td>
<td align="right">2.6%</td>
<td align="right">126,935,564</td>
<td align="right">3.2%</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">387,222,230</td>
<td align="right">4.1%</td>
<td align="right">236,203,418</td>
<td align="right">6.0%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">799,524,803</td>
<td align="right">8.5%</td>
<td align="right">523,805,455</td>
<td align="right">13.2%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">360,232,848</td>
<td align="right">3.8%</td>
<td align="right">315,130,700</td>
<td align="right">7.9%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">448,410,049</td>
<td align="right">4.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">173,284,270</td>
<td align="right">4.4%</td>
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
<td align="right">377,640,821</td>
<td align="right">20.0%</td>
<td align="right">73,011,232</td>
<td align="right">9.6%</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">348,608,675</td>
<td align="right">18.4%</td>
<td align="right">100,617,268</td>
<td align="right">13.3%</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">120,130,223</td>
<td align="right">6.4%</td>
<td align="right">43,295,960</td>
<td align="right">5.7%</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">109,974,964</td>
<td align="right">5.8%</td>
<td align="right">40,955,651</td>
<td align="right">5.4%</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">123,407,303</td>
<td align="right">6.5%</td>
<td align="right">98,419,065</td>
<td align="right">13.0%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,883,540</td>
<td align="right">4.1%</td>
<td align="right">77,874,866</td>
<td align="right">10.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,883,540</td>
<td align="right">4.1%</td>
<td align="right">77,874,866</td>
<td align="right">10.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">86,719,479</td>
<td align="right">4.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">86,445,850</td>
<td align="right">4.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">67,024,314</td>
<td align="right">3.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">39,166,936</td>
<td align="right">5.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">27,511,614</td>
<td align="right">3.6%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">25,201,793</td>
<td align="right">3.3%</td>
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
<td align="right">5,297,460</td>
<td align="right">0.1%</td>
<td align="right">2,651,460</td>
<td align="right">0.0%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">473,140,429</td>
<td align="right">4.9%</td>
<td align="right">590,975,839</td>
<td align="right">6.4%</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">28,740</td>
<td align="right">0.0%</td>
<td align="right">22,800</td>
<td align="right">0.0%</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">83,830,767</td>
<td align="right">0.9%</td>
<td align="right">71,655,823</td>
<td align="right">0.8%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,926,720,291</td>
<td align="right">71.1%</td>
<td align="right">6,267,349,144</td>
<td align="right">68.4%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,042,218</td>
<td align="right">0.3%</td>
<td align="right">28,601,908</td>
<td align="right">0.3%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">7,958,057,598</td>
<td align="right">81.7%</td>
<td align="right">7,491,400,605</td>
<td align="right">81.7%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,952,733,477</td>
<td align="right">20.0%</td>
<td align="right">2,047,522,845</td>
<td align="right">22.3%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,958,059,677</td>
<td align="right">20.1%</td>
<td align="right">2,050,197,105</td>
<td align="right">22.4%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,814,994,476</td>
<td align="right">28.9%</td>
<td align="right">2,902,048,923</td>
<td align="right">31.6%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,814,994,476</td>
<td align="right">28.9%</td>
<td align="right">2,902,048,923</td>
<td align="right">31.6%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">856,934,799</td>
<td align="right">8.8%</td>
<td align="right">851,851,818</td>
<td align="right">9.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">472,740,152</td>
<td align="right">4.9%</td>
<td align="right">474,942,988</td>
<td align="right">5.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,381,027</td>
<td align="right">2.2%</td>
<td align="right">211,381,047</td>
<td align="right">2.3%</td>
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
<td align="left">Method cache misses</td>
<td align="right">63,465,454</td>
<td align="right"></td>
<td align="right">21,284,570</td>
<td align="right"></td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">70,135,736</td>
<td align="right"></td>
<td align="right">27,805,055</td>
<td align="right"></td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">114,120</td>
<td align="right">0.1%</td>
<td align="right">63,880</td>
<td align="right">0.0%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,309,663,733</td>
<td align="right"></td>
<td align="right">2,645,147,329</td>
<td align="right"></td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,675,932</td>
<td align="right"></td>
<td align="right">6,702,639</td>
<td align="right"></td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">27,620,680,509</td>
<td align="right">21.6%</td>
<td align="right">25,101,207,917</td>
<td align="right">20.1%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,245,936</td>
<td align="right"></td>
<td align="right">149,681,086</td>
<td align="right"></td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">12,609,729,931</td>
<td align="right"></td>
<td align="right">11,674,855,499</td>
<td align="right"></td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,090,215,549</td>
<td align="right">62.2%</td>
<td align="right">11,202,706,531</td>
<td align="right">61.6%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">30,769,896,144</td>
<td align="right">21.0%</td>
<td align="right">28,521,684,350</td>
<td align="right">20.0%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,213,608,844</td>
<td align="right">62.8%</td>
<td align="right">11,326,158,590</td>
<td align="right">62.3%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">7,229,048,292</td>
<td align="right">37.2%</td>
<td align="right">6,846,107,965</td>
<td align="right">37.7%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">7,230,918,750</td>
<td align="right"></td>
<td align="right">6,847,882,193</td>
<td align="right"></td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,370,949,362</td>
<td align="right"></td>
<td align="right">4,210,979,155</td>
<td align="right"></td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,211,231</td>
<td align="right">0.1%</td>
<td align="right">19,745,483</td>
<td align="right">0.1%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">115,660,396,092</td>
<td align="right">79.0%</td>
<td align="right">114,063,672,485</td>
<td align="right">80.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,306,500</td>
<td align="right">2.0%</td>
<td align="right">3,271,100</td>
<td align="right">2.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,182,064</td>
<td align="right">0.5%</td>
<td align="right">103,706,576</td>
<td align="right">0.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">100,169,862,914</td>
<td align="right">78.4%</td>
<td align="right">99,828,899,222</td>
<td align="right">79.9%</td>
<td align="right">-0.3%</td>
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
<td align="right">115,425,780</td>
<td align="right">16,439,062,459</td>
<td align="right">0</td>
<td align="right">18,591,228</td>
<td align="right">14,424,921,478</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,753,920</td>
<td align="right">7,039,236,456</td>
<td align="right">0</td>
<td align="right">10,753,920</td>
<td align="right">7,059,096,892</td>
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
<td align="right">360</td>
<td align="right">360</td>
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
<td align="right">0</td>
<td align="right">1,081</td>
<td align="right">1,081 / 0 !!</td>
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
<td align="right">1,081</td>
<td align="right">1,081 / 0 !!</td>
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
<td align="right">1,920</td>
<td align="right">1,900</td>
<td align="right">-1.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-05-19
