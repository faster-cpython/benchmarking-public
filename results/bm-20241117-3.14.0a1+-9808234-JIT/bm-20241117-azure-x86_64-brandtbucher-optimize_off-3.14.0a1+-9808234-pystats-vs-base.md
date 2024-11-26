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
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">215,166,959</td>
<td align="right">182,895,367</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">91,284,179</td>
<td align="right">78,193,366</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">106,432,131</td>
<td align="right">91,821,888</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">73,485,867</td>
<td align="right">63,606,710</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,871,232</td>
<td align="right">1,635,280</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">517,940,353</td>
<td align="right">459,595,533</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">59,757,395</td>
<td align="right">65,066,120</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">415,406,812</td>
<td align="right">380,822,988</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">103,188,368</td>
<td align="right">109,727,932</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">175,123,516</td>
<td align="right">184,457,561</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">36,761,679</td>
<td align="right">34,827,627</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,488,943</td>
<td align="right">3,314,291</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">77,758,378</td>
<td align="right">74,091,059</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">86,238,218</td>
<td align="right">82,216,448</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">260,401,645</td>
<td align="right">248,293,265</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">82,575,823</td>
<td align="right">86,261,167</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">37,989,781</td>
<td align="right">36,319,858</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">603,288,286</td>
<td align="right">577,317,664</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">183,665,793</td>
<td align="right">191,246,213</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">27,097,314</td>
<td align="right">25,990,704</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">321,925,793</td>
<td align="right">308,877,926</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,979,410</td>
<td align="right">51,938,886</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">43,745,247</td>
<td align="right">45,377,923</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,112,306</td>
<td align="right">12,640,484</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">197,373,901</td>
<td align="right">190,588,144</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">348,795,711</td>
<td align="right">336,827,673</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">733,091</td>
<td align="right">758,015</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,425,618</td>
<td align="right">43,995,018</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">648,487,913</td>
<td align="right">629,736,566</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">294,752,880</td>
<td align="right">303,030,878</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,298,554,714</td>
<td align="right">1,263,923,384</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">46,578,364</td>
<td align="right">45,353,510</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">151,082,249</td>
<td align="right">147,192,943</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">35,271,672</td>
<td align="right">36,172,621</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">51,957,410</td>
<td align="right">53,234,214</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">337,874</td>
<td align="right">345,950</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">35,377,586</td>
<td align="right">36,221,004</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">133,329,833</td>
<td align="right">130,176,129</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">104,745,351</td>
<td align="right">102,369,406</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">580,599,036</td>
<td align="right">568,420,848</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">78,540,460</td>
<td align="right">80,134,042</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">274,030,826</td>
<td align="right">279,355,262</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">43,395,075</td>
<td align="right">44,235,945</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,912,808</td>
<td align="right">7,773,944</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">109,663,600</td>
<td align="right">111,565,401</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">588,247,948</td>
<td align="right">598,401,877</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,547,275,268</td>
<td align="right">1,520,643,128</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,029,214</td>
<td align="right">7,891,087</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">453,179,304</td>
<td align="right">445,909,551</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,710,833</td>
<td align="right">3,652,461</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">52,291,762</td>
<td align="right">51,490,034</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">5,797,472</td>
<td align="right">5,712,332</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">202,245</td>
<td align="right">199,302</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,979,384,865</td>
<td align="right">11,813,052,377</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,506,058,186</td>
<td align="right">2,472,764,596</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">156,099,792</td>
<td align="right">154,036,852</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,407,647,961</td>
<td align="right">3,365,483,179</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">35,301,584</td>
<td align="right">35,734,204</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">271,751,485</td>
<td align="right">275,000,018</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">123,610,631</td>
<td align="right">125,070,878</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">221,854,787</td>
<td align="right">219,305,259</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,822,249,413</td>
<td align="right">2,790,330,715</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">54,741,477</td>
<td align="right">55,350,710</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,642,453</td>
<td align="right">1,624,942</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">223,209,531</td>
<td align="right">220,914,318</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">20,065,459</td>
<td align="right">19,865,493</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">26,730,075</td>
<td align="right">26,994,965</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">80,940,632</td>
<td align="right">80,139,075</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">416,126,224</td>
<td align="right">412,085,027</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">516,472,328</td>
<td align="right">521,203,726</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">107,304,803</td>
<td align="right">108,253,854</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">602,087,842</td>
<td align="right">596,782,358</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,027,798,848</td>
<td align="right">2,011,508,218</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,512,757,358</td>
<td align="right">1,524,767,008</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">29,719,414</td>
<td align="right">29,494,662</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,235,174,887</td>
<td align="right">2,218,757,689</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">794,995,701</td>
<td align="right">789,422,165</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,362,380</td>
<td align="right">17,244,985</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,509,845,583</td>
<td align="right">1,500,304,260</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,967,127,267</td>
<td align="right">1,954,761,822</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,570,556,886</td>
<td align="right">3,548,893,413</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">98,709,585</td>
<td align="right">98,119,855</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">24,826,902</td>
<td align="right">24,970,020</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">260,785,683</td>
<td align="right">259,348,684</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">256,639,266</td>
<td align="right">257,902,965</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">187,380,043</td>
<td align="right">186,523,099</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">43,076,737</td>
<td align="right">42,881,233</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">130,247,800</td>
<td align="right">129,681,804</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">182,770,838</td>
<td align="right">182,020,519</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,028,645,729</td>
<td align="right">2,020,347,789</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">357,536,913</td>
<td align="right">356,266,473</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">162,896,910</td>
<td align="right">162,359,137</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">32,655,932</td>
<td align="right">32,760,866</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">26,746,393</td>
<td align="right">26,830,574</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">150,833,391</td>
<td align="right">151,284,985</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,054,739,780</td>
<td align="right">1,057,669,219</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">470,028,724</td>
<td align="right">468,728,608</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,779,985,837</td>
<td align="right">2,787,627,377</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">490,474,759</td>
<td align="right">491,803,798</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">145,420,201</td>
<td align="right">145,084,523</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">215,694</td>
<td align="right">215,212</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">366,809,497</td>
<td align="right">366,063,381</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,549,170</td>
<td align="right">7,563,747</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">105,844,084</td>
<td align="right">105,650,952</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">95,256,887</td>
<td align="right">95,430,136</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">40,171,877</td>
<td align="right">40,243,098</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">86,434,102</td>
<td align="right">86,314,364</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">239,830,147</td>
<td align="right">239,506,304</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">40,560,261</td>
<td align="right">40,613,699</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">63,850,849</td>
<td align="right">63,933,531</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">170,727,417</td>
<td align="right">170,523,564</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">217,263,936</td>
<td align="right">217,496,554</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,785,896,803</td>
<td align="right">1,784,050,202</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">123,769,028</td>
<td align="right">123,888,094</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">159,695,256</td>
<td align="right">159,543,302</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,345,339,974</td>
<td align="right">4,341,869,796</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,710</td>
<td align="right">2,708</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,693</td>
<td align="right">33,671</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">14,004,375</td>
<td align="right">13,996,277</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">153,026,092</td>
<td align="right">153,108,990</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">46,378,814</td>
<td align="right">46,354,288</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">45,734,748</td>
<td align="right">45,715,129</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">27,866,157</td>
<td align="right">27,875,924</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">405,838</td>
<td align="right">405,710</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">179,106,713</td>
<td align="right">179,055,756</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">48,502,781</td>
<td align="right">48,492,272</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">342,030,685</td>
<td align="right">342,102,350</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">4,042,502</td>
<td align="right">4,043,291</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">113,391,963</td>
<td align="right">113,412,781</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,919,407</td>
<td align="right">8,917,853</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">58,842,948</td>
<td align="right">58,852,730</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,909,845</td>
<td align="right">1,071,774,517</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">55,853,124</td>
<td align="right">55,859,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">254,013,098</td>
<td align="right">254,040,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,022,445</td>
<td align="right">10,023,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">66,937,801</td>
<td align="right">66,931,368</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">33,326,024</td>
<td align="right">33,328,804</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,370,468</td>
<td align="right">11,371,412</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,879</td>
<td align="right">120,870</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">75,163,082</td>
<td align="right">75,168,130</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">591,993</td>
<td align="right">591,959</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,327,986</td>
<td align="right">2,328,106</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,442,576</td>
<td align="right">25,443,818</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">428,651,322</td>
<td align="right">428,665,537</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">791,958,183</td>
<td align="right">791,932,919</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">145,895,928</td>
<td align="right">145,891,555</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">31,871,036</td>
<td align="right">31,870,276</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">94,794,214</td>
<td align="right">94,792,623</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,279</td>
<td align="right">14,760,086</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,068,901</td>
<td align="right">20,069,155</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">203,060,415</td>
<td align="right">203,058,597</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">111,140,633</td>
<td align="right">111,141,433</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">19,739,403</td>
<td align="right">19,739,461</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,070,024</td>
<td align="right">20,070,082</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,644,030</td>
<td align="right">1,644,033</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">23,342,306</td>
<td align="right">23,342,286</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">113,796,627</td>
<td align="right">113,796,692</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,816,176</td>
<td align="right">100,816,124</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,793</td>
<td align="right">5,803,795</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,048,540</td>
<td align="right">3,048,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,376</td>
<td align="right">302,607,376</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">168,156,024</td>
<td align="right">168,156,024</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,588</td>
<td align="right">128,850,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">38,329,162</td>
<td align="right">38,329,162</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">4,851,787</td>
<td align="right">4,851,787</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,140</td>
<td align="right">2,597,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">219,420</td>
<td align="right">219,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,720</td>
<td align="right">98,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,553</td>
<td align="right">84,553</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,672</td>
<td align="right">56,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">52,821</td>
<td align="right">52,821</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">42,350</td>
<td align="right">42,350</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,546</td>
<td align="right">17,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,321</td>
<td align="right">5,321</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,643</td>
<td align="right">3,643</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,435</td>
<td align="right">3,435</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">335</td>
<td align="right">335</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">150</td>
<td align="right">150</td>
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
<td align="right">38</td>
<td align="right">38</td>
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
<td align="right">294,000,490</td>
<td align="right">3.8%</td>
<td align="right">302,282,989</td>
<td align="right">3.9%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21,323,520</td>
<td align="right">0.3%</td>
<td align="right">21,438,460</td>
<td align="right">0.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,375,326,089</td>
<td align="right">95.9%</td>
<td align="right">7,373,171,026</td>
<td align="right">95.8%</td>
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
<td align="right">745,270</td>
<td align="right">100.0%</td>
<td align="right">740,810</td>
<td align="right">100.0%</td>
<td align="right">-0.6%</td>
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
<td align="left">xor</td>
<td align="right">2,749</td>
<td align="right">0.4%</td>
<td align="right">3,048</td>
<td align="right">0.4%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">10,015</td>
<td align="right">1.3%</td>
<td align="right">10,919</td>
<td align="right">1.5%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">7,813</td>
<td align="right">1.0%</td>
<td align="right">8,202</td>
<td align="right">1.1%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,019</td>
<td align="right">2.6%</td>
<td align="right">19,616</td>
<td align="right">2.6%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">5,890</td>
<td align="right">0.8%</td>
<td align="right">5,764</td>
<td align="right">0.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">736</td>
<td align="right">0.1%</td>
<td align="right">745</td>
<td align="right">0.1%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">583,287</td>
<td align="right">78.3%</td>
<td align="right">577,007</td>
<td align="right">77.9%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">491</td>
<td align="right">0.1%</td>
<td align="right">496</td>
<td align="right">0.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">4,576</td>
<td align="right">0.6%</td>
<td align="right">4,555</td>
<td align="right">0.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">34,917</td>
<td align="right">4.7%</td>
<td align="right">34,772</td>
<td align="right">4.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,330</td>
<td align="right">0.3%</td>
<td align="right">2,323</td>
<td align="right">0.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">36,115</td>
<td align="right">4.8%</td>
<td align="right">36,027</td>
<td align="right">4.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">2,831</td>
<td align="right">0.4%</td>
<td align="right">2,826</td>
<td align="right">0.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1,122</td>
<td align="right">0.2%</td>
<td align="right">1,121</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">4,185</td>
<td align="right">0.6%</td>
<td align="right">4,182</td>
<td align="right">0.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">22,275</td>
<td align="right">3.0%</td>
<td align="right">22,288</td>
<td align="right">3.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">5,787</td>
<td align="right">0.8%</td>
<td align="right">5,787</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,049</td>
<td align="right">0.1%</td>
<td align="right">1,049</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="right">86,434,102</td>
<td align="right">100.0%</td>
<td align="right">86,314,364</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">5,757,086</td>
<td align="right">0.1%</td>
<td align="right">5,760,151</td>
<td align="right">0.1%</td>
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
<td align="right">428,506,409</td>
<td align="right">7.3%</td>
<td align="right">428,521,040</td>
<td align="right">7.3%</td>
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
<td align="right">5,467,100,307</td>
<td align="right">92.6%</td>
<td align="right">5,466,965,629</td>
<td align="right">92.6%</td>
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
<td align="right">135,634</td>
<td align="right">53.5%</td>
<td align="right">135,224</td>
<td align="right">53.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">117,703</td>
<td align="right">46.5%</td>
<td align="right">117,755</td>
<td align="right">46.5%</td>
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
<td align="left">out of range</td>
<td align="right">36,185</td>
<td align="right">26.7%</td>
<td align="right">35,804</td>
<td align="right">26.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">6,276</td>
<td align="right">4.6%</td>
<td align="right">6,256</td>
<td align="right">4.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">9,797</td>
<td align="right">7.2%</td>
<td align="right">9,793</td>
<td align="right">7.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,455</td>
<td align="right">2.5%</td>
<td align="right">3,456</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">45,727</td>
<td align="right">33.7%</td>
<td align="right">45,722</td>
<td align="right">33.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,362</td>
<td align="right">9.1%</td>
<td align="right">12,361</td>
<td align="right">9.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">18,032</td>
<td align="right">13.3%</td>
<td align="right">18,032</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
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
<td align="left">buffer slice</td>
<td align="right">766</td>
<td align="right">0.6%</td>
<td align="right">766</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">72</td>
<td align="right">0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">119,244,735</td>
<td align="right">1.1%</td>
<td align="right">127,610,142</td>
<td align="right">1.2%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">19,585</td>
<td align="right">0.0%</td>
<td align="right">19,489</td>
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
<td align="right">10,883,970,742</td>
<td align="right">98.9%</td>
<td align="right">10,864,092,759</td>
<td align="right">98.8%</td>
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
<td align="right">230,115</td>
<td align="right">0.0%</td>
<td align="right">230,058</td>
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
<td align="right">2,442,532</td>
<td align="right">100.0%</td>
<td align="right">2,600,366</td>
<td align="right">100.0%</td>
<td align="right">6.5%</td>
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
<td align="left">init not simple</td>
<td align="right">752</td>
<td align="right">132.2%</td>
<td align="right">752</td>
<td align="right">132.2%</td>
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
<tr>
<td align="left">init not inline values</td>
<td align="right">385</td>
<td align="right">67.7%</td>
<td align="right">385</td>
<td align="right">67.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">287</td>
<td align="right">50.4%</td>
<td align="right">287</td>
<td align="right">50.4%</td>
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
<td align="right">500,942</td>
<td align="right">80.6%</td>
<td align="right">500,886</td>
<td align="right">80.6%</td>
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
<td align="right">111,570</td>
<td align="right">17.9%</td>
<td align="right">111,568</td>
<td align="right">17.9%</td>
<td align="right">-0.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">887,215</td>
<td align="right">0.0%</td>
<td align="right">803,822</td>
<td align="right">0.0%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">78,437,630</td>
<td align="right">1.7%</td>
<td align="right">80,034,295</td>
<td align="right">1.7%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,514,941,707</td>
<td align="right">98.3%</td>
<td align="right">4,514,188,599</td>
<td align="right">98.2%</td>
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
<td align="right">34,791</td>
<td align="right">29.2%</td>
<td align="right">33,199</td>
<td align="right">29.0%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">84,531</td>
<td align="right">70.8%</td>
<td align="right">81,469</td>
<td align="right">71.0%</td>
<td align="right">-3.6%</td>
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
<td align="right">27,813</td>
<td align="right">32.9%</td>
<td align="right">24,341</td>
<td align="right">29.9%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,337</td>
<td align="right">9.9%</td>
<td align="right">8,778</td>
<td align="right">10.8%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">337</td>
<td align="right">0.4%</td>
<td align="right">333</td>
<td align="right">0.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">677</td>
<td align="right">0.8%</td>
<td align="right">684</td>
<td align="right">0.8%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,453</td>
<td align="right">7.6%</td>
<td align="right">6,411</td>
<td align="right">7.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,969</td>
<td align="right">4.7%</td>
<td align="right">3,960</td>
<td align="right">4.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">20,933</td>
<td align="right">24.8%</td>
<td align="right">20,952</td>
<td align="right">25.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,192</td>
<td align="right">7.3%</td>
<td align="right">6,190</td>
<td align="right">7.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,554</td>
<td align="right">8.9%</td>
<td align="right">7,554</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">974</td>
<td align="right">1.2%</td>
<td align="right">974</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">958</td>
<td align="right">1.1%</td>
<td align="right">958</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
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
<td align="right">35,239,693</td>
<td align="right">1.6%</td>
<td align="right">36,140,346</td>
<td align="right">1.6%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,182,117,822</td>
<td align="right">98.3%</td>
<td align="right">2,181,705,257</td>
<td align="right">98.3%</td>
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
<td align="right">1,916,370</td>
<td align="right">0.1%</td>
<td align="right">1,916,370</td>
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
<td align="right">29,721</td>
<td align="right">100.0%</td>
<td align="right">30,017</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
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
<td align="left">list</td>
<td align="right">4,969</td>
<td align="right">16.7%</td>
<td align="right">5,209</td>
<td align="right">17.4%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">7,197</td>
<td align="right">24.2%</td>
<td align="right">7,217</td>
<td align="right">24.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,143</td>
<td align="right">24.0%</td>
<td align="right">7,158</td>
<td align="right">23.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,412</td>
<td align="right">35.0%</td>
<td align="right">10,433</td>
<td align="right">34.8%</td>
<td align="right">0.2%</td>
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
<td align="right">73,439,152</td>
<td align="right">12.3%</td>
<td align="right">63,562,364</td>
<td align="right">10.7%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,361,031</td>
<td align="right">4.1%</td>
<td align="right">27,624,147</td>
<td align="right">4.6%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">500,186,968</td>
<td align="right">83.6%</td>
<td align="right">504,725,381</td>
<td align="right">84.7%</td>
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
<td align="right">464,555</td>
<td align="right">91.8%</td>
<td align="right">526,106</td>
<td align="right">93.1%</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">41,640</td>
<td align="right">8.2%</td>
<td align="right">39,280</td>
<td align="right">6.9%</td>
<td align="right">-5.7%</td>
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
<td align="left">dict values</td>
<td align="right">4,154</td>
<td align="right">10.0%</td>
<td align="right">1,833</td>
<td align="right">4.7%</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,604</td>
<td align="right">8.7%</td>
<td align="right">3,350</td>
<td align="right">8.5%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,463</td>
<td align="right">15.5%</td>
<td align="right">6,676</td>
<td align="right">17.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">883</td>
<td align="right">2.1%</td>
<td align="right">863</td>
<td align="right">2.2%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,996</td>
<td align="right">4.8%</td>
<td align="right">1,956</td>
<td align="right">5.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,799</td>
<td align="right">4.3%</td>
<td align="right">1,824</td>
<td align="right">4.6%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">3,462</td>
<td align="right">8.3%</td>
<td align="right">3,481</td>
<td align="right">8.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">13,512</td>
<td align="right">32.4%</td>
<td align="right">13,530</td>
<td align="right">34.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,231</td>
<td align="right">3.0%</td>
<td align="right">1,230</td>
<td align="right">3.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,477</td>
<td align="right">5.9%</td>
<td align="right">2,478</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,761</td>
<td align="right">4.2%</td>
<td align="right">1,761</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">130</td>
<td align="right">0.3%</td>
<td align="right">130</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">113</td>
<td align="right">0.3%</td>
<td align="right">113</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">55</td>
<td align="right">0.1%</td>
<td align="right">55</td>
<td align="right">0.1%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">598,241</td>
<td align="right">0.0%</td>
<td align="right">298,081</td>
<td align="right">0.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">401,606,059</td>
<td align="right">3.1%</td>
<td align="right">347,463,992</td>
<td align="right">2.7%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">414,062,680</td>
<td align="right">3.2%</td>
<td align="right">379,898,837</td>
<td align="right">2.9%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,148,879,215</td>
<td align="right">93.7%</td>
<td align="right">12,292,733,673</td>
<td align="right">94.4%</td>
<td align="right">1.2%</td>
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
<td align="right">8,707,680</td>
<td align="right">97.7%</td>
<td align="right">7,269,271</td>
<td align="right">97.3%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">203,813</td>
<td align="right">2.3%</td>
<td align="right">200,674</td>
<td align="right">2.7%</td>
<td align="right">-1.5%</td>
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
<td align="right">0.2%</td>
<td align="right">180</td>
<td align="right">0.1%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">131</td>
<td align="right">0.1%</td>
<td align="right">147</td>
<td align="right">0.1%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">18,560</td>
<td align="right">9.1%</td>
<td align="right">16,771</td>
<td align="right">8.4%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">857</td>
<td align="right">0.4%</td>
<td align="right">837</td>
<td align="right">0.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40,103</td>
<td align="right">19.7%</td>
<td align="right">39,547</td>
<td align="right">19.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">13,911</td>
<td align="right">6.8%</td>
<td align="right">13,804</td>
<td align="right">6.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">35,868</td>
<td align="right">17.6%</td>
<td align="right">35,655</td>
<td align="right">17.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,688</td>
<td align="right">2.3%</td>
<td align="right">4,666</td>
<td align="right">2.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">56,531</td>
<td align="right">27.7%</td>
<td align="right">56,293</td>
<td align="right">28.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,541</td>
<td align="right">3.7%</td>
<td align="right">7,542</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,146</td>
<td align="right">4.0%</td>
<td align="right">8,147</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,405</td>
<td align="right">1.2%</td>
<td align="right">2,405</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,584</td>
<td align="right">0.8%</td>
<td align="right">1,584</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,439</td>
<td align="right">0.7%</td>
<td align="right">1,439</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,263</td>
<td align="right">0.6%</td>
<td align="right">1,263</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,106</td>
<td align="right">0.5%</td>
<td align="right">1,106</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
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
<td align="right">3,408,570,699</td>
<td align="right">99.6%</td>
<td align="right">3,361,631,718</td>
<td align="right">99.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,680</td>
<td align="right">0.4%</td>
<td align="right">14,622,599</td>
<td align="right">0.4%</td>
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
<td align="right">1,637</td>
<td align="right">0.0%</td>
<td align="right">1,637</td>
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
<td align="right">52,982</td>
<td align="right">0.0%</td>
<td align="right">52,982</td>
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
<td align="right">138,387</td>
<td align="right">100.0%</td>
<td align="right">138,275</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">63,989,914</td>
<td align="right">100.0%</td>
<td align="right">63,341,127</td>
<td align="right">100.0%</td>
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
<td align="right">255</td>
<td align="right">0.0%</td>
<td align="right">253</td>
<td align="right">0.0%</td>
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
<td align="right">2,455</td>
<td align="right">100.0%</td>
<td align="right">2,455</td>
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
<td align="right">128,815,796</td>
<td align="right">17.8%</td>
<td align="right">128,815,796</td>
<td align="right">17.8%</td>
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
<td align="right">593,288,799</td>
<td align="right">82.2%</td>
<td align="right">593,288,799</td>
<td align="right">82.2%</td>
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
<td align="right">105,277,321</td>
<td align="right">5.2%</td>
<td align="right">60,913,195</td>
<td align="right">3.1%</td>
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
<td align="right">53,892,461</td>
<td align="right">2.7%</td>
<td align="right">51,852,374</td>
<td align="right">2.6%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,855,046,540</td>
<td align="right">92.1%</td>
<td align="right">1,859,007,133</td>
<td align="right">94.3%</td>
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
<td align="right">2,028,127</td>
<td align="right">97.9%</td>
<td align="right">1,191,113</td>
<td align="right">96.4%</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">44,396</td>
<td align="right">2.1%</td>
<td align="right">43,956</td>
<td align="right">3.6%</td>
<td align="right">-1.0%</td>
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
<td align="right">22,622</td>
<td align="right">51.0%</td>
<td align="right">22,173</td>
<td align="right">50.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,623</td>
<td align="right">10.4%</td>
<td align="right">4,639</td>
<td align="right">10.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,757</td>
<td align="right">4.0%</td>
<td align="right">1,752</td>
<td align="right">4.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,352</td>
<td align="right">7.6%</td>
<td align="right">3,350</td>
<td align="right">7.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,506</td>
<td align="right">16.9%</td>
<td align="right">7,506</td>
<td align="right">17.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.6%</td>
<td align="right">1,619</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">913</td>
<td align="right">2.1%</td>
<td align="right">913</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.6%</td>
<td align="right">730</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.6%</td>
<td align="right">699</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">365</td>
<td align="right">0.8%</td>
<td align="right">365</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">100</td>
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
<td align="right">215,694</td>
<td align="right">100.0%</td>
<td align="right">215,212</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
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
<td align="right">86,203,680</td>
<td align="right">8.6%</td>
<td align="right">82,182,897</td>
<td align="right">8.2%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">918,915,812</td>
<td align="right">91.4%</td>
<td align="right">918,502,764</td>
<td align="right">91.8%</td>
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
<td align="right">32,378</td>
<td align="right">93.6%</td>
<td align="right">31,390</td>
<td align="right">93.4%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,200</td>
<td align="right">6.4%</td>
<td align="right">2,201</td>
<td align="right">6.6%</td>
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
<td align="right">3,028</td>
<td align="right">9.4%</td>
<td align="right">2,039</td>
<td align="right">6.5%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">3,058</td>
<td align="right">9.4%</td>
<td align="right">3,059</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,723</td>
<td align="right">51.6%</td>
<td align="right">16,723</td>
<td align="right">53.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">8,633</td>
<td align="right">26.7%</td>
<td align="right">8,633</td>
<td align="right">27.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">500</td>
<td align="right">1.5%</td>
<td align="right">500</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">208</td>
<td align="right">0.6%</td>
<td align="right">208</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">204</td>
<td align="right">0.6%</td>
<td align="right">204</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">24</td>
<td align="right">0.1%</td>
<td align="right">24</td>
<td align="right">0.1%</td>
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
<td align="right">22,501,751</td>
<td align="right">0.5%</td>
<td align="right">20,802,079</td>
<td align="right">0.4%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,556,140,598</td>
<td align="right">96.9%</td>
<td align="right">4,745,319,179</td>
<td align="right">97.0%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">123,471,131</td>
<td align="right">2.6%</td>
<td align="right">123,625,517</td>
<td align="right">2.5%</td>
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
<td align="left">Failure</td>
<td align="right">247,643</td>
<td align="right">34.3%</td>
<td align="right">212,331</td>
<td align="right">32.5%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">473,426</td>
<td align="right">65.7%</td>
<td align="right">441,293</td>
<td align="right">67.5%</td>
<td align="right">-6.8%</td>
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
<td align="right">73,951</td>
<td align="right">29.9%</td>
<td align="right">49,473</td>
<td align="right">23.3%</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">111,748</td>
<td align="right">45.1%</td>
<td align="right">100,990</td>
<td align="right">47.6%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">12,989</td>
<td align="right">5.2%</td>
<td align="right">12,948</td>
<td align="right">6.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">5,373</td>
<td align="right">2.2%</td>
<td align="right">5,357</td>
<td align="right">2.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,278</td>
<td align="right">3.7%</td>
<td align="right">9,261</td>
<td align="right">4.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,025</td>
<td align="right">3.2%</td>
<td align="right">8,024</td>
<td align="right">3.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,839</td>
<td align="right">4.8%</td>
<td align="right">11,838</td>
<td align="right">5.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">12,798</td>
<td align="right">5.2%</td>
<td align="right">12,798</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.6%</td>
<td align="right">1,420</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">182</td>
<td align="right">0.1%</td>
<td align="right">182</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,232,941,425</td>
<td align="right">100.0%</td>
<td align="right">1,232,725,883</td>
<td align="right">100.0%</td>
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
<td align="right">579,756</td>
<td align="right">0.0%</td>
<td align="right">579,750</td>
<td align="right">0.0%</td>
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
<td align="right">663</td>
<td align="right">5.4%</td>
<td align="right">647</td>
<td align="right">5.3%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,654</td>
<td align="right">94.6%</td>
<td align="right">11,642</td>
<td align="right">94.7%</td>
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
<td align="left">sequence</td>
<td align="right">436</td>
<td align="right">65.8%</td>
<td align="right">420</td>
<td align="right">64.9%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">20.5%</td>
<td align="right">136</td>
<td align="right">21.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">13.7%</td>
<td align="right">91</td>
<td align="right">14.1%</td>
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
<td align="right">703,617,012</td>
<td align="right">1.0%</td>
<td align="right">615,075,238</td>
<td align="right">0.9%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">1,821,477,752</td>
<td align="right">2.6%</td>
<td align="right">1,781,737,701</td>
<td align="right">2.6%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">41,687,985,423</td>
<td align="right">59.3%</td>
<td align="right">41,342,917,214</td>
<td align="right">59.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">26,056,868,370</td>
<td align="right">37.1%</td>
<td align="right">25,876,694,771</td>
<td align="right">37.2%</td>
<td align="right">-0.7%</td>
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
<td align="right">73,439,152</td>
<td align="right">4.0%</td>
<td align="right">63,562,364</td>
<td align="right">3.6%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">414,062,680</td>
<td align="right">22.8%</td>
<td align="right">379,898,837</td>
<td align="right">21.4%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">86,203,680</td>
<td align="right">4.7%</td>
<td align="right">82,182,897</td>
<td align="right">4.6%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,892,461</td>
<td align="right">3.0%</td>
<td align="right">51,852,374</td>
<td align="right">2.9%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">294,000,490</td>
<td align="right">16.2%</td>
<td align="right">302,282,989</td>
<td align="right">17.0%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">78,437,630</td>
<td align="right">4.3%</td>
<td align="right">80,034,295</td>
<td align="right">4.5%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">86,434,102</td>
<td align="right">4.8%</td>
<td align="right">86,314,364</td>
<td align="right">4.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">123,471,131</td>
<td align="right">6.8%</td>
<td align="right">123,625,517</td>
<td align="right">6.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">428,506,409</td>
<td align="right">23.6%</td>
<td align="right">428,521,040</td>
<td align="right">24.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,796</td>
<td align="right">7.1%</td>
<td align="right">128,815,796</td>
<td align="right">7.2%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">88,225,820</td>
<td align="right">12.5%</td>
<td align="right">43,865,409</td>
<td align="right">7.1%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">57,832,354</td>
<td align="right">8.2%</td>
<td align="right">44,557,781</td>
<td align="right">7.2%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">44,339,899</td>
<td align="right">6.3%</td>
<td align="right">36,556,596</td>
<td align="right">5.9%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">159,010,207</td>
<td align="right">22.6%</td>
<td align="right">132,979,424</td>
<td align="right">21.6%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">101,524,042</td>
<td align="right">14.4%</td>
<td align="right">95,596,172</td>
<td align="right">15.5%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">63,020,573</td>
<td align="right">9.0%</td>
<td align="right">65,128,644</td>
<td align="right">10.6%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,361,976</td>
<td align="right">2.3%</td>
<td align="right">16,832,044</td>
<td align="right">2.7%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">17,029,642</td>
<td align="right">2.4%</td>
<td align="right">17,029,395</td>
<td align="right">2.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,872,804</td>
<td align="right">3.0%</td>
<td align="right">20,872,801</td>
<td align="right">3.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">15,424,646</td>
<td align="right">2.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">18,018,351</td>
<td align="right">2.9%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,252,453</td>
<td align="right">4.2%</td>
<td align="right">278,431,159</td>
<td align="right">4.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,117,886,156</td>
<td align="right">16.7%</td>
<td align="right">1,116,175,031</td>
<td align="right">16.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,120,018,301</td>
<td align="right">16.8%</td>
<td align="right">1,118,307,176</td>
<td align="right">16.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,284,403,061</td>
<td align="right">79.1%</td>
<td align="right">5,278,902,482</td>
<td align="right">79.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,790,944,143</td>
<td align="right">26.8%</td>
<td align="right">1,789,098,326</td>
<td align="right">26.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,790,944,143</td>
<td align="right">26.8%</td>
<td align="right">1,789,098,326</td>
<td align="right">26.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,891,798,061</td>
<td align="right">73.2%</td>
<td align="right">4,888,003,570</td>
<td align="right">73.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,925,842</td>
<td align="right">10.0%</td>
<td align="right">670,791,150</td>
<td align="right">10.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,527,041</td>
<td align="right">1.1%</td>
<td align="right">71,527,181</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,275</td>
<td align="right">0.4%</td>
<td align="right">24,922,284</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,406,131</td>
<td align="right">3.9%</td>
<td align="right">261,406,062</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,248</td>
<td align="right">0.0%</td>
<td align="right">2,128,248</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,897</td>
<td align="right">0.0%</td>
<td align="right">3,897</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,139</td>
<td align="right">2.0%</td>
<td align="right">132,513,139</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">6,726,475</td>
<td align="right"></td>
<td align="right">6,191,551</td>
<td align="right"></td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">65,296,451</td>
<td align="right"></td>
<td align="right">63,080,502</td>
<td align="right"></td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">59,374,467</td>
<td align="right"></td>
<td align="right">57,694,677</td>
<td align="right"></td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">1,988,328,123</td>
<td align="right"></td>
<td align="right">1,965,851,041</td>
<td align="right"></td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">87,162,847,239</td>
<td align="right">43.0%</td>
<td align="right">87,793,902,071</td>
<td align="right">43.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">7,849,416,979</td>
<td align="right">4.7%</td>
<td align="right">7,793,090,438</td>
<td align="right">4.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">81,880,771,186</td>
<td align="right">49.4%</td>
<td align="right">82,435,080,005</td>
<td align="right">49.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">44,375,371,308</td>
<td align="right">21.9%</td>
<td align="right">44,081,441,609</td>
<td align="right">21.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">32,472,418,735</td>
<td align="right">19.6%</td>
<td align="right">32,261,186,729</td>
<td align="right">19.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">15,185,633,585</td>
<td align="right">7.5%</td>
<td align="right">15,114,060,037</td>
<td align="right">7.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">56,138,961,899</td>
<td align="right">27.7%</td>
<td align="right">55,958,274,030</td>
<td align="right">27.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,068,904</td>
<td align="right"></td>
<td align="right">178,597,091</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,072,134,636</td>
<td align="right"></td>
<td align="right">3,066,174,969</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">43,514,548,910</td>
<td align="right">26.3%</td>
<td align="right">43,591,061,041</td>
<td align="right">26.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,972,756</td>
<td align="right">0.4%</td>
<td align="right">72,068,631</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,431,099</td>
<td align="right">0.0%</td>
<td align="right">6,437,059</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,432,363,494</td>
<td align="right"></td>
<td align="right">8,428,786,788</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,432,188,678</td>
<td align="right">44.9%</td>
<td align="right">8,428,626,659</td>
<td align="right">44.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,929,382,024</td>
<td align="right"></td>
<td align="right">10,926,308,688</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,264,213,654</td>
<td align="right">54.7%</td>
<td align="right">10,261,545,741</td>
<td align="right">54.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,342,617,509</td>
<td align="right">55.1%</td>
<td align="right">10,340,051,431</td>
<td align="right">55.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,139</td>
<td align="right">2.5%</td>
<td align="right">4,444,139</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">434,414</td>
<td align="right">0.2%</td>
<td align="right">434,414</td>
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
<td align="right">363,438</td>
<td align="right">103,146,435</td>
<td align="right">19,002,128,765</td>
<td align="right">363,428</td>
<td align="right">103,023,653</td>
<td align="right">19,001,126,044</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,246,203,240</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,246,203,240</td>
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
<td align="right">3,692</td>
<td align="right">0.5%</td>
<td align="right">2,664</td>
<td align="right">0.3%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,669</td>
<td align="right">0.1%</td>
<td align="right">1,470</td>
<td align="right">0.1%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">761,576</td>
<td align="right">50.2%</td>
<td align="right">838,602</td>
<td align="right">51.8%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">5,038</td>
<td align="right">0.3%</td>
<td align="right">4,598</td>
<td align="right">0.3%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,515,815</td>
<td align="right"></td>
<td align="right">1,618,882</td>
<td align="right"></td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">774,170</td>
<td align="right">51.1%</td>
<td align="right">820,589</td>
<td align="right">50.7%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">7,284</td>
<td align="right">0.5%</td>
<td align="right">6,906</td>
<td align="right">0.4%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">257,638,664,250</td>
<td align="right">3,335.2%</td>
<td align="right">269,186,840,322</td>
<td align="right">3,361.6%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">15,334</td>
<td align="right">1.0%</td>
<td align="right">14,689</td>
<td align="right">0.9%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,724,810,070</td>
<td align="right"></td>
<td align="right">8,007,635,906</td>
<td align="right"></td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">752,570</td>
<td align="right">49.6%</td>
<td align="right">778,810</td>
<td align="right">48.1%</td>
<td align="right">3.5%</td>
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
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">460</td>
<td align="right">0.1%</td>
<td align="right">582</td>
<td align="right">0.1%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">730,844</td>
<td align="right">96.0%</td>
<td align="right">838,020</td>
<td align="right">99.9%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">761,576</td>
<td align="right"></td>
<td align="right">838,602</td>
<td align="right"></td>
<td align="right">10.1%</td>
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
<td align="right">53,232</td>
<td align="right">7.0%</td>
<td align="right">55,962</td>
<td align="right">6.7%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">138,710</td>
<td align="right">18.2%</td>
<td align="right">146,217</td>
<td align="right">17.4%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">263,427</td>
<td align="right">34.6%</td>
<td align="right">299,126</td>
<td align="right">35.7%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">199,395</td>
<td align="right">26.2%</td>
<td align="right">225,501</td>
<td align="right">26.9%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">80,430</td>
<td align="right">10.6%</td>
<td align="right">85,031</td>
<td align="right">10.1%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">22,753</td>
<td align="right">3.0%</td>
<td align="right">23,386</td>
<td align="right">2.8%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">3,349</td>
<td align="right">0.4%</td>
<td align="right">3,099</td>
<td align="right">0.4%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">10,771</td>
<td align="right">1.4%</td>
<td align="right">11,461</td>
<td align="right">1.4%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">123,656</td>
<td align="right">16.2%</td>
<td align="right">71,275</td>
<td align="right">8.5%</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">142,598</td>
<td align="right">18.7%</td>
<td align="right">193,196</td>
<td align="right">23.0%</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">290,653</td>
<td align="right">38.2%</td>
<td align="right">343,471</td>
<td align="right">41.0%</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">121,929</td>
<td align="right">16.0%</td>
<td align="right">159,471</td>
<td align="right">19.0%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">33,258</td>
<td align="right">4.4%</td>
<td align="right">46,144</td>
<td align="right">5.5%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">7,087</td>
<td align="right">0.9%</td>
<td align="right">11,709</td>
<td align="right">1.4%</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">892</td>
<td align="right">0.1%</td>
<td align="right">1,293</td>
<td align="right">0.2%</td>
<td align="right">45.0%</td>
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
<td align="left">_LOAD_CONST</td>
<td align="right">3,872,691</td>
<td align="right">1,356,884,367</td>
<td align="right">34,937.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">34,182,480</td>
<td align="right">3,948,095,169</td>
<td align="right">11,450.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">22,765,103</td>
<td align="right">2,605,337,824</td>
<td align="right">11,344.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">723,471,700</td>
<td align="right">6,793,126,039</td>
<td align="right">839.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">28,686,482</td>
<td align="right">163,123,940</td>
<td align="right">468.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">28,686,482</td>
<td align="right">163,123,940</td>
<td align="right">468.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">340,017,023</td>
<td align="right">1,751,442,899</td>
<td align="right">415.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">952,603</td>
<td align="right">3,445,233</td>
<td align="right">261.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">18,712,660</td>
<td align="right">59,139,240</td>
<td align="right">216.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">610,908,521</td>
<td align="right">1,598,111,181</td>
<td align="right">161.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">739,739,587</td>
<td align="right">1,410,295,164</td>
<td align="right">90.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,906,095,493</td>
<td align="right">1,054,796,202</td>
<td align="right">-78.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,095,266,644</td>
<td align="right">769,155,129</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">40,539</td>
<td align="right">15,619</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">220,997</td>
<td align="right">335,633</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,107,703,983</td>
<td align="right">8,905,399,988</td>
<td align="right">45.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">117,300,031</td>
<td align="right">68,304,387</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">18,532,628</td>
<td align="right">13,509,898</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">18,825,684</td>
<td align="right">14,136,021</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">8,983,964</td>
<td align="right">7,058,372</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">81,814,636</td>
<td align="right">65,986,122</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">1,102</td>
<td align="right">907</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">144,620,095</td>
<td align="right">165,542,165</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">27,185,838</td>
<td align="right">30,635,624</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,319,767</td>
<td align="right">2,597,185</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,768,598,839</td>
<td align="right">1,975,439,631</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">618,466,785</td>
<td align="right">685,311,599</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,126,205,284</td>
<td align="right">2,344,017,165</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,597,001,382</td>
<td align="right">1,751,442,899</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,984,154,372</td>
<td align="right">1,795,090,459</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">169,957,666</td>
<td align="right">158,600,158</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">61,807,139</td>
<td align="right">65,254,040</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">84,419,435</td>
<td align="right">88,708,425</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">123,096,620</td>
<td align="right">129,072,306</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">21,078,250</td>
<td align="right">22,054,731</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,337,409,017</td>
<td align="right">5,583,965,564</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,794,122,302</td>
<td align="right">7,095,439,355</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">300,511,030</td>
<td align="right">313,159,344</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">464,084,551</td>
<td align="right">482,025,536</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">467,788,353</td>
<td align="right">485,737,178</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">841,773,820</td>
<td align="right">873,868,689</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,724,810,070</td>
<td align="right">8,007,635,906</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">296,762,480</td>
<td align="right">306,808,790</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">9,427,902</td>
<td align="right">9,133,041</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">203,145,229</td>
<td align="right">196,805,674</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">11,637,694</td>
<td align="right">11,964,896</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">10,119,000,763</td>
<td align="right">10,389,195,330</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">57,226</td>
<td align="right">58,716</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">437,491,318</td>
<td align="right">448,866,280</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">297,614,167</td>
<td align="right">290,756,373</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">3,599,106</td>
<td align="right">3,516,499</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">907,289,755</td>
<td align="right">887,544,639</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,018,566</td>
<td align="right">87,108,242</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,494,106,632</td>
<td align="right">1,525,952,030</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">990,276</td>
<td align="right">1,009,990</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,344,033,493</td>
<td align="right">6,459,179,098</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">29,924,691</td>
<td align="right">30,421,570</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">159,337,079</td>
<td align="right">161,902,436</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">517,394,177</td>
<td align="right">509,096,089</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">779,136,434</td>
<td align="right">790,807,079</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">808,056,932</td>
<td align="right">820,147,805</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">124,024,776</td>
<td align="right">125,801,639</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">270,210,582</td>
<td align="right">266,369,682</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">817,036,194</td>
<td align="right">828,538,759</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,171,584,930</td>
<td align="right">1,155,760,994</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">276,815,238</td>
<td align="right">280,507,445</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">1,540,117</td>
<td align="right">1,560,653</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,021,213,193</td>
<td align="right">3,060,115,776</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">193,789,505</td>
<td align="right">191,397,526</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,665,926,024</td>
<td align="right">3,709,565,607</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">857,301,675</td>
<td align="right">847,829,375</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">810,580,916</td>
<td align="right">801,683,513</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,034,578,226</td>
<td align="right">2,012,342,534</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">525,701,900</td>
<td align="right">531,422,992</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">526,587,748</td>
<td align="right">532,309,029</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,884,438,187</td>
<td align="right">2,914,990,406</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,004,928,569</td>
<td align="right">2,025,503,738</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,395,001,651</td>
<td align="right">1,408,548,822</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,397,180,443</td>
<td align="right">1,410,709,659</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">642,946,372</td>
<td align="right">649,143,234</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">55,825,099</td>
<td align="right">56,362,372</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">861,715</td>
<td align="right">853,639</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">102,000,081</td>
<td align="right">101,053,064</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">17,678,410,853</td>
<td align="right">17,836,474,401</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">181,602,868</td>
<td align="right">179,996,455</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,599,329</td>
<td align="right">9,515,131</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,710,314,941</td>
<td align="right">2,687,086,605</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,748,026,795</td>
<td align="right">2,724,906,752</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">739,348,407</td>
<td align="right">745,554,610</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,243,108,947</td>
<td align="right">1,253,532,676</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,397,896,984</td>
<td align="right">1,409,250,848</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">7,421,512</td>
<td align="right">7,362,554</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,024,586,373</td>
<td align="right">1,016,635,414</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,487,441,996</td>
<td align="right">1,498,788,951</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">21,242,326,033</td>
<td align="right">21,402,190,443</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,188,340,391</td>
<td align="right">6,233,609,733</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">739,321,328</td>
<td align="right">734,014,155</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,310,032,431</td>
<td align="right">1,319,327,159</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">118,872,214</td>
<td align="right">118,076,147</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,960,650,154</td>
<td align="right">2,980,265,844</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">614,622,474</td>
<td align="right">618,643,435</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">573,418,552</td>
<td align="right">569,840,477</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">43,206,619</td>
<td align="right">42,941,729</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">79,476,516</td>
<td align="right">79,043,896</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,008,431,536</td>
<td align="right">1,997,718,014</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,394,190,693</td>
<td align="right">2,381,559,424</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">228,336,466</td>
<td align="right">227,171,600</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,158,640,808</td>
<td align="right">2,147,844,348</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">532,708,822</td>
<td align="right">535,355,785</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">395,437,281</td>
<td align="right">393,546,221</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">41,994,889</td>
<td align="right">42,194,855</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">926,771,347</td>
<td align="right">931,070,250</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,663,820,499</td>
<td align="right">8,702,711,816</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,337,414</td>
<td align="right">2,347,399</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,214,306,685</td>
<td align="right">4,231,391,824</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">26,364,257</td>
<td align="right">26,465,767</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">438,884,562</td>
<td align="right">437,202,837</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">226,563,432</td>
<td align="right">225,725,715</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">652,348</td>
<td align="right">650,064</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">68,396,138</td>
<td align="right">68,631,604</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">427,503,855</td>
<td align="right">428,897,951</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,922,720,122</td>
<td align="right">1,928,781,372</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,754,382,885</td>
<td align="right">1,749,385,597</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">315,150,911</td>
<td align="right">316,035,567</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">53,847,338</td>
<td align="right">53,708,717</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">210,484,368</td>
<td align="right">209,945,476</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">179,800,823</td>
<td align="right">179,348,682</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">365,148,420</td>
<td align="right">366,035,504</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">804,941,660</td>
<td align="right">806,853,957</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">887,122,388</td>
<td align="right">885,030,439</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,388,921,478</td>
<td align="right">1,385,672,210</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,416,210,808</td>
<td align="right">3,424,193,891</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">882,296,114</td>
<td align="right">880,263,338</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,946,124,954</td>
<td align="right">1,950,488,148</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,805,575,929</td>
<td align="right">9,827,292,914</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">260,145,620</td>
<td align="right">260,693,560</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,486,172,860</td>
<td align="right">2,491,276,501</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,706,990,697</td>
<td align="right">4,716,458,670</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">118,835,531</td>
<td align="right">119,066,875</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">36,430,890</td>
<td align="right">36,364,932</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,146,389</td>
<td align="right">8,131,822</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">303,964,641</td>
<td align="right">304,505,356</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">594,881,233</td>
<td align="right">593,860,290</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">595,899,793</td>
<td align="right">594,878,850</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">560,148,582</td>
<td align="right">559,189,229</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">343,354,957</td>
<td align="right">342,768,616</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">796,140,157</td>
<td align="right">797,461,921</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">522,378,015</td>
<td align="right">521,536,050</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">35,752,733</td>
<td align="right">35,697,660</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">37,454,760</td>
<td align="right">37,401,533</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,075,008,149</td>
<td align="right">3,079,048,284</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">94,419,975</td>
<td align="right">94,539,713</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">35,397,285</td>
<td align="right">35,357,175</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">35,397,285</td>
<td align="right">35,357,175</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">5,955,405</td>
<td align="right">5,961,853</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">592,915,339</td>
<td align="right">593,557,114</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">98,761,592</td>
<td align="right">98,656,660</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">2,886,259</td>
<td align="right">2,883,400</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">74,591,061</td>
<td align="right">74,521,633</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">107,544,415</td>
<td align="right">107,642,319</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">107,544,415</td>
<td align="right">107,642,319</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">247,300,858</td>
<td align="right">247,082,037</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">81,922,800</td>
<td align="right">81,851,579</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">529,990,683</td>
<td align="right">529,541,799</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,107,731,898</td>
<td align="right">1,106,841,734</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,566,995,670</td>
<td align="right">2,568,873,558</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">159,099,657</td>
<td align="right">159,215,328</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">75,120,086</td>
<td align="right">75,068,888</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,918,400,480</td>
<td align="right">1,919,646,752</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">37,894,110</td>
<td align="right">37,918,635</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">37,894,110</td>
<td align="right">37,918,635</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,219,148,021</td>
<td align="right">1,219,839,183</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">51,989,210</td>
<td align="right">52,015,352</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">42,640,644</td>
<td align="right">42,619,768</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">42,638,963</td>
<td align="right">42,618,147</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">681,195,165</td>
<td align="right">681,526,649</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,061,365,085</td>
<td align="right">1,061,879,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,328,371,332</td>
<td align="right">4,326,361,390</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">28,573,937</td>
<td align="right">28,584,366</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,413,128,534</td>
<td align="right">4,414,730,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,308,133,367</td>
<td align="right">3,309,273,005</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,363,167,796</td>
<td align="right">1,362,741,208</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">98,527,085</td>
<td align="right">98,496,995</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,652,290</td>
<td align="right">60,669,804</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">81,834,048</td>
<td align="right">81,853,708</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,976,034,397</td>
<td align="right">2,975,401,568</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">30,365,189</td>
<td align="right">30,370,602</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">63,129,800</td>
<td align="right">63,139,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">66,660,803</td>
<td align="right">66,650,670</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">177,364,141</td>
<td align="right">177,389,771</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">192,745,814</td>
<td align="right">192,773,154</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,103,721,988</td>
<td align="right">1,103,866,716</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,540,016</td>
<td align="right">24,539,072</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">126,082,646</td>
<td align="right">126,086,913</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,566,341,225</td>
<td align="right">1,566,392,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">4,017,009</td>
<td align="right">4,016,883</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">41,855,684</td>
<td align="right">41,854,492</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,398,220</td>
<td align="right">4,398,100</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,003,965,489</td>
<td align="right">1,003,938,193</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,927,009,820</td>
<td align="right">1,927,055,332</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">63,251,165</td>
<td align="right">63,250,627</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">72,549,534</td>
<td align="right">72,548,989</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">501,459,956</td>
<td align="right">501,456,219</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">4,018,086</td>
<td align="right">4,018,057</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">124,936,800</td>
<td align="right">124,937,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">390,244,435</td>
<td align="right">390,246,121</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">112,470,800</td>
<td align="right">112,471,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">74,738,554</td>
<td align="right">74,738,478</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,236,544</td>
<td align="right">1,236,545</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,284,032</td>
<td align="right">47,284,052</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">174,530,405</td>
<td align="right">174,530,365</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">72,535,170</td>
<td align="right">72,535,171</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,858,689,540</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">827,209,490</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">468,875,893</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">311,282,897</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">165,769,397</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">58,355,163</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,115</td>
<td align="right">36,620,115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,115</td>
<td align="right">36,620,115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,527,364</td>
<td align="right">4,527,364</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right">3,555,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,336,533</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">840,692</td>
<td align="right">840,692</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">768,354</td>
<td align="right">768,354</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">768,270</td>
<td align="right">768,270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">561,600</td>
<td align="right">561,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">17,198</td>
<td align="right">17,198</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">15,117</td>
<td align="right">15,117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">4,363</td>
<td align="right">4,363</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_WITH_SPEC</td>
<td align="right">2,417</td>
<td align="right">2,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">1,905</td>
<td align="right">1,905</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">462</td>
<td align="right">462</td>
<td align="right">0.0%</td>
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
<td align="right">2,153</td>
<td align="right">1,721</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">53,994</td>
<td align="right">56,137</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,274</td>
<td align="right">23,729</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">29,758</td>
<td align="right">29,936</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">106</td>
<td align="right">106</td>
<td align="right">0.0%</td>
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
<td align="right">250</td>
<td align="right">239</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">250</td>
<td align="right">239</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,629</td>
<td align="right">22,629</td>
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
<td align="right">31</td>
<td align="right">31</td>
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
<td align="right">38</td>
<td align="right">38</td>
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
<td align="right">2,476</td>
<td align="right">2,476</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-18
