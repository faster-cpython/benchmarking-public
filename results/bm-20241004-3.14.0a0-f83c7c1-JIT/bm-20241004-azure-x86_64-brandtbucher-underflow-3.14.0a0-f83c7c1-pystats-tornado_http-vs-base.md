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
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">228,620</td>
<td align="right">16,184</td>
<td align="right">-92.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">183,240</td>
<td align="right">35,462</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">72,060</td>
<td align="right">16,184</td>
<td align="right">-77.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">12,027</td>
<td align="right">3,216</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">59,980</td>
<td align="right">18,400</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">14,820</td>
<td align="right">4,819</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">860,275</td>
<td align="right">290,266</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">731,267</td>
<td align="right">256,253</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">346,271</td>
<td align="right">141,858</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">534,672</td>
<td align="right">223,613</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">576,300</td>
<td align="right">270,020</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">120,460</td>
<td align="right">61,889</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,882,522</td>
<td align="right">1,507,847</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">622,263</td>
<td align="right">339,787</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">145,480</td>
<td align="right">79,922</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">859,709</td>
<td align="right">477,641</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">330,221</td>
<td align="right">184,357</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">456,000</td>
<td align="right">254,944</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">60,320</td>
<td align="right">33,887</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">60,320</td>
<td align="right">33,887</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">12,020</td>
<td align="right">6,812</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,315,809</td>
<td align="right">1,354,800</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">373,820</td>
<td align="right">219,184</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">742,083</td>
<td align="right">440,608</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">48,300</td>
<td align="right">29,441</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">24,160</td>
<td align="right">15,349</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,892,618</td>
<td align="right">1,209,769</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">202,697</td>
<td align="right">129,824</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">121,298</td>
<td align="right">78,977</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">215,118</td>
<td align="right">142,491</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">7,555,242</td>
<td align="right">5,026,300</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,091,785</td>
<td align="right">2,091,903</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">747,021</td>
<td align="right">526,089</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">767,722</td>
<td align="right">541,592</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,579,241</td>
<td align="right">4,656,922</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">923,729</td>
<td align="right">654,210</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">9,088,647</td>
<td align="right">6,461,666</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">119,980</td>
<td align="right">86,465</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">23,240,691</td>
<td align="right">17,091,118</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">277,940</td>
<td align="right">205,161</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">305,639</td>
<td align="right">225,883</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,131,815</td>
<td align="right">7,543,167</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">35,260</td>
<td align="right">26,449</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">469,100</td>
<td align="right">354,041</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,942,492</td>
<td align="right">6,830,377</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,321,070</td>
<td align="right">10,958,869</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">677,207</td>
<td align="right">519,146</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">30,670</td>
<td align="right">23,557</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">3,982,032</td>
<td align="right">3,059,592</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,660,674</td>
<td align="right">2,828,792</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">65,822,155</td>
<td align="right">50,952,582</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">7,727,241</td>
<td align="right">6,104,843</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">9,750,868</td>
<td align="right">7,734,264</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,989,416</td>
<td align="right">1,593,694</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">12,601,801</td>
<td align="right">10,124,493</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">839,392</td>
<td align="right">674,447</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">9,966,445</td>
<td align="right">8,077,628</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">11,385,860</td>
<td align="right">9,260,893</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,612,048</td>
<td align="right">5,382,086</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">377,718</td>
<td align="right">307,483</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">794,220</td>
<td align="right">647,306</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">893,955</td>
<td align="right">732,214</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,708,155</td>
<td align="right">2,229,155</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">4,827,501</td>
<td align="right">3,988,644</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">17,387,485</td>
<td align="right">14,386,773</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">259,750</td>
<td align="right">214,926</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">191,580</td>
<td align="right">162,518</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">670,852</td>
<td align="right">570,607</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,208,327</td>
<td align="right">1,030,677</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">84,309</td>
<td align="right">72,184</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">425,219</td>
<td align="right">365,497</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">648,203</td>
<td align="right">559,136</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">287,888</td>
<td align="right">249,567</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">850,209</td>
<td align="right">737,789</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">299,908</td>
<td align="right">261,587</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">57,358</td>
<td align="right">50,244</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">100,520</td>
<td align="right">88,249</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,036,561</td>
<td align="right">2,669,713</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">76,220</td>
<td align="right">67,021</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,133,685</td>
<td align="right">2,757,508</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,072,244</td>
<td align="right">944,259</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,787,060</td>
<td align="right">1,997,957</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,840,656</td>
<td align="right">7,935,999</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">691,915</td>
<td align="right">628,102</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">939,311</td>
<td align="right">854,648</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">155,478</td>
<td align="right">142,167</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">108,960</td>
<td align="right">100,149</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">91,846</td>
<td align="right">84,552</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">397,580</td>
<td align="right">367,282</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,622,628</td>
<td align="right">2,424,167</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,783,115</td>
<td align="right">2,585,917</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,604,164</td>
<td align="right">1,508,573</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">325,060</td>
<td align="right">306,876</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">161,228</td>
<td align="right">153,267</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">12,980</td>
<td align="right">12,382</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">444,000</td>
<td align="right">426,644</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,599,797</td>
<td align="right">3,468,098</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">479,642</td>
<td align="right">463,324</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,965,019</td>
<td align="right">1,899,586</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">169,320</td>
<td align="right">163,792</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">287,800</td>
<td align="right">278,523</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">336,300</td>
<td align="right">326,076</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">675,720</td>
<td align="right">655,767</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">460,270</td>
<td align="right">448,980</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">176,243</td>
<td align="right">172,892</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">348,355</td>
<td align="right">341,761</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">204,772</td>
<td align="right">202,564</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,332,324</td>
<td align="right">1,319,089</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,654,240</td>
<td align="right">1,639,032</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">52,879</td>
<td align="right">53,229</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">565,160</td>
<td align="right">563,393</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">12,080</td>
<td align="right">12,060</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">183,445</td>
<td align="right">183,143</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">252,760</td>
<td align="right">252,440</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">934,710</td>
<td align="right">934,379</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">269,186</td>
<td align="right">269,111</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">40,679</td>
<td align="right">40,668</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">221,059</td>
<td align="right">221,006</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">450,650</td>
<td align="right">450,721</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">368,645</td>
<td align="right">368,598</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">460,390</td>
<td align="right">460,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">5,217,143</td>
<td align="right">5,217,650</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">191,118</td>
<td align="right">191,136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,086,829</td>
<td align="right">1,086,869</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">54,720</td>
<td align="right">54,722</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">28,780</td>
<td align="right">28,781</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">116,680</td>
<td align="right">116,681</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">338,220</td>
<td align="right">338,219</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">540,400</td>
<td align="right">540,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">336,820</td>
<td align="right">336,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">327,000</td>
<td align="right">327,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">204,420</td>
<td align="right">204,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">143,960</td>
<td align="right">143,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">121,520</td>
<td align="right">121,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">92,380</td>
<td align="right">92,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">73,200</td>
<td align="right">73,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">72,020</td>
<td align="right">72,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">61,120</td>
<td align="right">61,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">60,540</td>
<td align="right">60,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">60,180</td>
<td align="right">60,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">24,120</td>
<td align="right">24,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">24,060</td>
<td align="right">24,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">16,321</td>
<td align="right">16,321</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">13,980</td>
<td align="right">13,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">12,140</td>
<td align="right">12,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">9,440</td>
<td align="right">9,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">5,940</td>
<td align="right">5,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">3,460</td>
<td align="right">3,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">1,320</td>
<td align="right">1,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">1,300</td>
<td align="right">1,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,140</td>
<td align="right">1,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">420</td>
<td align="right">420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">280</td>
<td align="right">280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">260</td>
<td align="right">260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">100</td>
<td align="right">100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">20</td>
<td align="right">20</td>
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
<td align="right">915,414</td>
<td align="right">27.4%</td>
<td align="right">646,303</td>
<td align="right">21.1%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,415,663</td>
<td align="right">72.3%</td>
<td align="right">2,415,846</td>
<td align="right">78.7%</td>
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
<td align="right">7,355</td>
<td align="right">88.5%</td>
<td align="right">6,947</td>
<td align="right">87.9%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">960</td>
<td align="right">11.5%</td>
<td align="right">960</td>
<td align="right">12.1%</td>
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
<td align="left">add other</td>
<td align="right">1,120</td>
<td align="right">15.2%</td>
<td align="right">980</td>
<td align="right">14.1%</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">880</td>
<td align="right">12.0%</td>
<td align="right">780</td>
<td align="right">11.2%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">22</td>
<td align="right">0.3%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,403</td>
<td align="right">46.3%</td>
<td align="right">3,260</td>
<td align="right">46.9%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">1,226</td>
<td align="right">16.7%</td>
<td align="right">1,200</td>
<td align="right">17.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">425</td>
<td align="right">5.8%</td>
<td align="right">425</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">180</td>
<td align="right">2.4%</td>
<td align="right">180</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">100</td>
<td align="right">1.4%</td>
<td align="right">100</td>
<td align="right">1.4%</td>
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
<td align="right">346,271</td>
<td align="right">100.0%</td>
<td align="right">141,858</td>
<td align="right">100.0%</td>
<td align="right">-59.0%</td>
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
<td align="right">326,701</td>
<td align="right">15.7%</td>
<td align="right">181,017</td>
<td align="right">9.4%</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,743,900</td>
<td align="right">84.0%</td>
<td align="right">1,744,110</td>
<td align="right">90.4%</td>
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
<td align="right">1,780</td>
<td align="right">0.1%</td>
<td align="right">1,780</td>
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
<td align="right">2,560</td>
<td align="right">72.3%</td>
<td align="right">2,380</td>
<td align="right">70.8%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">980</td>
<td align="right">27.7%</td>
<td align="right">980</td>
<td align="right">29.2%</td>
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
<td align="left">buffer int</td>
<td align="right">2,400</td>
<td align="right">93.8%</td>
<td align="right">2,220</td>
<td align="right">93.3%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">160</td>
<td align="right">6.2%</td>
<td align="right">160</td>
<td align="right">6.7%</td>
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
<td align="right">261,961</td>
<td align="right">1.1%</td>
<td align="right">259,824</td>
<td align="right">1.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,528,638</td>
<td align="right">98.7%</td>
<td align="right">23,530,424</td>
<td align="right">98.7%</td>
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
<td align="right">34,000</td>
<td align="right">0.1%</td>
<td align="right">34,002</td>
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
<td align="left">Success</td>
<td align="right">26,121</td>
<td align="right">99.4%</td>
<td align="right">26,086</td>
<td align="right">99.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">160</td>
<td align="right">0.6%</td>
<td align="right">160</td>
<td align="right">0.6%</td>
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
<td align="left">out of versions</td>
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">80</td>
<td align="right">50.0%</td>
<td align="right">80</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">20</td>
<td align="right">12.5%</td>
<td align="right">20</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">20</td>
<td align="right">12.5%</td>
<td align="right">20</td>
<td align="right">12.5%</td>
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
<td align="right">820</td>
<td align="right">52.6%</td>
<td align="right">820</td>
<td align="right">52.6%</td>
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
<td align="right">172,596</td>
<td align="right">4.0%</td>
<td align="right">169,262</td>
<td align="right">3.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,159,375</td>
<td align="right">95.9%</td>
<td align="right">4,159,894</td>
<td align="right">96.0%</td>
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
<td align="right">207</td>
<td align="right">0.0%</td>
<td align="right">207</td>
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
<td align="right">1,747</td>
<td align="right">47.9%</td>
<td align="right">1,730</td>
<td align="right">47.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,900</td>
<td align="right">52.1%</td>
<td align="right">1,900</td>
<td align="right">52.3%</td>
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
<td align="left">big int</td>
<td align="right">160</td>
<td align="right">9.2%</td>
<td align="right">141</td>
<td align="right">8.2%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">127</td>
<td align="right">7.3%</td>
<td align="right">129</td>
<td align="right">7.5%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">480</td>
<td align="right">27.5%</td>
<td align="right">480</td>
<td align="right">27.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">360</td>
<td align="right">20.6%</td>
<td align="right">360</td>
<td align="right">20.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">340</td>
<td align="right">19.5%</td>
<td align="right">340</td>
<td align="right">19.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">180</td>
<td align="right">10.3%</td>
<td align="right">180</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">60</td>
<td align="right">3.4%</td>
<td align="right">60</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">40</td>
<td align="right">2.3%</td>
<td align="right">40</td>
<td align="right">2.3%</td>
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
<td align="right">393,100</td>
<td align="right">58.1%</td>
<td align="right">362,920</td>
<td align="right">56.2%</td>
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
<td align="right">278,660</td>
<td align="right">41.2%</td>
<td align="right">278,660</td>
<td align="right">43.1%</td>
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
<td align="right">4,080</td>
<td align="right">91.1%</td>
<td align="right">3,962</td>
<td align="right">90.8%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">400</td>
<td align="right">8.9%</td>
<td align="right">400</td>
<td align="right">9.2%</td>
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
<td align="right">2,380</td>
<td align="right">58.3%</td>
<td align="right">2,262</td>
<td align="right">57.1%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,200</td>
<td align="right">29.4%</td>
<td align="right">1,200</td>
<td align="right">30.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">440</td>
<td align="right">10.8%</td>
<td align="right">440</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">60</td>
<td align="right">1.5%</td>
<td align="right">60</td>
<td align="right">1.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">673,369</td>
<td align="right">76.7%</td>
<td align="right">586,500</td>
<td align="right">74.3%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">201,434</td>
<td align="right">22.9%</td>
<td align="right">199,236</td>
<td align="right">25.2%</td>
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
<td align="right">2,338</td>
<td align="right">70.0%</td>
<td align="right">2,328</td>
<td align="right">70.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,000</td>
<td align="right">30.0%</td>
<td align="right">1,000</td>
<td align="right">30.0%</td>
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
<td align="left">set</td>
<td align="right">160</td>
<td align="right">6.8%</td>
<td align="right">150</td>
<td align="right">6.4%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,280</td>
<td align="right">54.7%</td>
<td align="right">1,280</td>
<td align="right">55.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">280</td>
<td align="right">12.0%</td>
<td align="right">280</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">200</td>
<td align="right">8.6%</td>
<td align="right">200</td>
<td align="right">8.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">7.7%</td>
<td align="right">180</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">120</td>
<td align="right">5.1%</td>
<td align="right">120</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">118</td>
<td align="right">5.0%</td>
<td align="right">118</td>
<td align="right">5.1%</td>
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
<td align="right">507,971</td>
<td align="right">0.9%</td>
<td align="right">448,776</td>
<td align="right">0.8%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,720,595</td>
<td align="right">4.9%</td>
<td align="right">2,524,800</td>
<td align="right">4.6%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">52,729,315</td>
<td align="right">94.1%</td>
<td align="right">52,437,108</td>
<td align="right">94.5%</td>
<td align="right">-0.6%</td>
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
<td align="right">52,385</td>
<td align="right">72.9%</td>
<td align="right">50,145</td>
<td align="right">72.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">19,520</td>
<td align="right">27.1%</td>
<td align="right">19,259</td>
<td align="right">27.7%</td>
<td align="right">-1.3%</td>
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
<td align="right">1,280</td>
<td align="right">6.6%</td>
<td align="right">1,240</td>
<td align="right">6.4%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">8,020</td>
<td align="right">41.1%</td>
<td align="right">7,889</td>
<td align="right">41.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">7,280</td>
<td align="right">37.3%</td>
<td align="right">7,200</td>
<td align="right">37.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">1,220</td>
<td align="right">6.2%</td>
<td align="right">1,210</td>
<td align="right">6.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">460</td>
<td align="right">2.4%</td>
<td align="right">460</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">380</td>
<td align="right">1.9%</td>
<td align="right">380</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">180</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">160</td>
<td align="right">0.8%</td>
<td align="right">160</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">160</td>
<td align="right">0.8%</td>
<td align="right">160</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
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
<td align="right">16,575,733</td>
<td align="right">99.8%</td>
<td align="right">13,456,954</td>
<td align="right">99.8%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,760</td>
<td align="right">0.1%</td>
<td align="right">14,761</td>
<td align="right">0.1%</td>
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
<td align="right">760</td>
<td align="right">0.0%</td>
<td align="right">760</td>
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
<td align="right">2,760</td>
<td align="right">0.0%</td>
<td align="right">2,760</td>
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
<td align="right">14,040</td>
<td align="right">100.0%</td>
<td align="right">14,040</td>
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
<td align="right">460</td>
<td align="right">0.1%</td>
<td align="right">460</td>
<td align="right">0.1%</td>
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
<td align="right">311,560</td>
<td align="right">99.7%</td>
<td align="right">311,560</td>
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
<td align="right">287,800</td>
<td align="right">46.0%</td>
<td align="right">287,799</td>
<td align="right">46.0%</td>
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
<td align="right">336,200</td>
<td align="right">53.7%</td>
<td align="right">336,199</td>
<td align="right">53.7%</td>
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
<td align="right">200</td>
<td align="right">9.9%</td>
<td align="right">200</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,820</td>
<td align="right">90.1%</td>
<td align="right">1,820</td>
<td align="right">90.1%</td>
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
<td align="right">1,820</td>
<td align="right">100.0%</td>
<td align="right">1,820</td>
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
<td align="right">709,448</td>
<td align="right">5.8%</td>
<td align="right">647,697</td>
<td align="right">5.3%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,964,297</td>
<td align="right">89.8%</td>
<td align="right">11,024,990</td>
<td align="right">90.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">525,560</td>
<td align="right">4.3%</td>
<td align="right">525,560</td>
<td align="right">4.3%</td>
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
<td align="right">20,905</td>
<td align="right">74.3%</td>
<td align="right">19,776</td>
<td align="right">73.3%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">7,220</td>
<td align="right">25.7%</td>
<td align="right">7,220</td>
<td align="right">26.7%</td>
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
<td align="left">not in dict</td>
<td align="right">4,000</td>
<td align="right">55.4%</td>
<td align="right">4,000</td>
<td align="right">55.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,660</td>
<td align="right">23.0%</td>
<td align="right">1,660</td>
<td align="right">23.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">480</td>
<td align="right">6.6%</td>
<td align="right">480</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">480</td>
<td align="right">6.6%</td>
<td align="right">480</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">260</td>
<td align="right">3.6%</td>
<td align="right">260</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">240</td>
<td align="right">3.3%</td>
<td align="right">240</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">100</td>
<td align="right">1.4%</td>
<td align="right">100</td>
<td align="right">1.4%</td>
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
<td align="right">90,480</td>
<td align="right">13.8%</td>
<td align="right">90,480</td>
<td align="right">13.8%</td>
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
<td align="right">565,400</td>
<td align="right">86.0%</td>
<td align="right">565,400</td>
<td align="right">86.0%</td>
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
<td align="right">20.0%</td>
<td align="right">380</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,520</td>
<td align="right">80.0%</td>
<td align="right">1,520</td>
<td align="right">80.0%</td>
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
<td align="right">1,200</td>
<td align="right">78.9%</td>
<td align="right">1,200</td>
<td align="right">78.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">320</td>
<td align="right">21.1%</td>
<td align="right">320</td>
<td align="right">21.1%</td>
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
<td align="right">882,046</td>
<td align="right">6.5%</td>
<td align="right">720,473</td>
<td align="right">5.4%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,576,782</td>
<td align="right">93.3%</td>
<td align="right">12,480,810</td>
<td align="right">94.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">15,160</td>
<td align="right">0.1%</td>
<td align="right">15,121</td>
<td align="right">0.1%</td>
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
<td align="right">4,629</td>
<td align="right">38.0%</td>
<td align="right">4,461</td>
<td align="right">37.2%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,551</td>
<td align="right">62.0%</td>
<td align="right">7,547</td>
<td align="right">62.8%</td>
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
<td align="left">bytes</td>
<td align="right">623</td>
<td align="right">13.5%</td>
<td align="right">547</td>
<td align="right">12.3%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,206</td>
<td align="right">26.1%</td>
<td align="right">1,133</td>
<td align="right">25.4%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">960</td>
<td align="right">20.7%</td>
<td align="right">941</td>
<td align="right">21.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">620</td>
<td align="right">13.4%</td>
<td align="right">620</td>
<td align="right">13.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">500</td>
<td align="right">10.8%</td>
<td align="right">500</td>
<td align="right">11.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">380</td>
<td align="right">8.2%</td>
<td align="right">380</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">340</td>
<td align="right">7.3%</td>
<td align="right">340</td>
<td align="right">7.6%</td>
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
<td align="right">1,170,508</td>
<td align="right">98.8%</td>
<td align="right">1,035,027</td>
<td align="right">98.7%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,920</td>
<td align="right">1.1%</td>
<td align="right">12,920</td>
<td align="right">1.2%</td>
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
<td align="right">900</td>
<td align="right">84.9%</td>
<td align="right">900</td>
<td align="right">84.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">160</td>
<td align="right">15.1%</td>
<td align="right">160</td>
<td align="right">15.1%</td>
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
<td align="right">160</td>
<td align="right">100.0%</td>
<td align="right">160</td>
<td align="right">100.0%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">130,278,319</td>
<td align="right">40.5%</td>
<td align="right">101,647,144</td>
<td align="right">39.9%</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">182,946,983</td>
<td align="right">56.8%</td>
<td align="right">145,413,471</td>
<td align="right">57.1%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">7,126,746</td>
<td align="right">2.2%</td>
<td align="right">6,112,156</td>
<td align="right">2.4%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,499,369</td>
<td align="right">0.5%</td>
<td align="right">1,376,323</td>
<td align="right">0.5%</td>
<td align="right">-8.2%</td>
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
<td align="right">346,271</td>
<td align="right">5.0%</td>
<td align="right">141,858</td>
<td align="right">2.4%</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">326,701</td>
<td align="right">4.7%</td>
<td align="right">181,017</td>
<td align="right">3.0%</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">915,414</td>
<td align="right">13.1%</td>
<td align="right">646,303</td>
<td align="right">10.8%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">882,046</td>
<td align="right">12.6%</td>
<td align="right">720,473</td>
<td align="right">12.1%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">393,100</td>
<td align="right">5.6%</td>
<td align="right">362,920</td>
<td align="right">6.1%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,720,595</td>
<td align="right">39.0%</td>
<td align="right">2,524,800</td>
<td align="right">42.4%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">172,596</td>
<td align="right">2.5%</td>
<td align="right">169,262</td>
<td align="right">2.8%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">201,434</td>
<td align="right">2.9%</td>
<td align="right">199,236</td>
<td align="right">3.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">336,200</td>
<td align="right">4.8%</td>
<td align="right">336,199</td>
<td align="right">5.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">525,560</td>
<td align="right">7.5%</td>
<td align="right">525,560</td>
<td align="right">8.8%</td>
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
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">36,497</td>
<td align="right">2.4%</td>
<td align="right">17,331</td>
<td align="right">1.3%</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">286,231</td>
<td align="right">19.1%</td>
<td align="right">246,290</td>
<td align="right">17.9%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">709,428</td>
<td align="right">47.3%</td>
<td align="right">647,677</td>
<td align="right">47.1%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">66,672</td>
<td align="right">4.4%</td>
<td align="right">65,521</td>
<td align="right">4.8%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">26,531</td>
<td align="right">1.8%</td>
<td align="right">26,191</td>
<td align="right">1.9%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,227</td>
<td align="right">1.0%</td>
<td align="right">15,183</td>
<td align="right">1.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">125,780</td>
<td align="right">8.4%</td>
<td align="right">125,720</td>
<td align="right">9.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">43,396</td>
<td align="right">2.9%</td>
<td align="right">43,412</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">125,112</td>
<td align="right">8.3%</td>
<td align="right">125,130</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">36,880</td>
<td align="right">2.5%</td>
<td align="right">36,880</td>
<td align="right">2.7%</td>
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
<td align="right">1,090,576</td>
<td align="right">5.4%</td>
<td align="right">1,091,113</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,881,843</td>
<td align="right">24.0%</td>
<td align="right">4,882,351</td>
<td align="right">24.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,882,223</td>
<td align="right">24.0%</td>
<td align="right">4,882,731</td>
<td align="right">24.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">5,230,923</td>
<td align="right">25.7%</td>
<td align="right">5,231,430</td>
<td align="right">25.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">5,230,923</td>
<td align="right">25.7%</td>
<td align="right">5,231,430</td>
<td align="right">25.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">752,064</td>
<td align="right">3.7%</td>
<td align="right">752,116</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">19,803,301</td>
<td align="right">97.2%</td>
<td align="right">19,803,916</td>
<td align="right">97.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">880,099</td>
<td align="right">4.3%</td>
<td align="right">880,085</td>
<td align="right">4.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">15,148,198</td>
<td align="right">74.3%</td>
<td align="right">15,148,304</td>
<td align="right">74.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">348,700</td>
<td align="right">1.7%</td>
<td align="right">348,699</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">280</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">132,540</td>
<td align="right">0.7%</td>
<td align="right">132,540</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">169,480</td>
<td align="right">0.8%</td>
<td align="right">169,480</td>
<td align="right">0.8%</td>
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
<td align="right">25,129</td>
<td align="right"></td>
<td align="right">35,919</td>
<td align="right"></td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">81,028,587</td>
<td align="right">23.9%</td>
<td align="right">114,135,481</td>
<td align="right">33.8%</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">88,915,202</td>
<td align="right">24.7%</td>
<td align="right">114,615,415</td>
<td align="right">31.5%</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">53,038,626</td>
<td align="right">15.6%</td>
<td align="right">41,569,488</td>
<td align="right">12.3%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">45,384,934</td>
<td align="right">12.6%</td>
<td align="right">36,876,757</td>
<td align="right">10.1%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">45,449,218</td>
<td align="right">12.6%</td>
<td align="right">53,941,379</td>
<td align="right">14.8%</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">161,648,657</td>
<td align="right">47.6%</td>
<td align="right">132,927,722</td>
<td align="right">39.3%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">331,780</td>
<td align="right"></td>
<td align="right">274,683</td>
<td align="right"></td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">352,103</td>
<td align="right"></td>
<td align="right">305,813</td>
<td align="right"></td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">44,012,533</td>
<td align="right">13.0%</td>
<td align="right">49,203,177</td>
<td align="right">14.6%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">179,610,916</td>
<td align="right">50.0%</td>
<td align="right">158,433,630</td>
<td align="right">43.5%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">80,357</td>
<td align="right">0.3%</td>
<td align="right">81,903</td>
<td align="right">0.3%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">15,911,547</td>
<td align="right">56.7%</td>
<td align="right">16,048,981</td>
<td align="right">56.9%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">16,225,336</td>
<td align="right">57.8%</td>
<td align="right">16,364,520</td>
<td align="right">58.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">16,477,756</td>
<td align="right"></td>
<td align="right">16,615,043</td>
<td align="right"></td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,802,387</td>
<td align="right"></td>
<td align="right">7,756,534</td>
<td align="right"></td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">6,641,488</td>
<td align="right"></td>
<td align="right">6,609,487</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">233,432</td>
<td align="right">0.8%</td>
<td align="right">233,636</td>
<td align="right">0.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,894,897</td>
<td align="right"></td>
<td align="right">11,894,671</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,841,922</td>
<td align="right">42.2%</td>
<td align="right">11,841,714</td>
<td align="right">42.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,059,040</td>
<td align="right"></td>
<td align="right">1,059,040</td>
<td align="right"></td>
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
<td align="right">12,000</td>
<td align="right">1.1%</td>
<td align="right">12,000</td>
<td align="right">1.1%</td>
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
<td align="right">200</td>
<td align="right">1,920</td>
<td align="right">4,387,792</td>
<td align="right">200</td>
<td align="right">1,920</td>
<td align="right">4,377,202</td>
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
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,197</td>
<td align="right">46.6%</td>
<td align="right">5,287</td>
<td align="right">71.5%</td>
<td align="right">140.6%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">227</td>
<td align="right">4.8%</td>
<td align="right">540</td>
<td align="right">7.3%</td>
<td align="right">137.9%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">4,036,124</td>
<td align="right"></td>
<td align="right">8,638,268</td>
<td align="right"></td>
<td align="right">114.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">131,845,552</td>
<td align="right">3,266.6%</td>
<td align="right">265,553,630</td>
<td align="right">3,074.2%</td>
<td align="right">101.4%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">2,876</td>
<td align="right">61.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">4,714</td>
<td align="right"></td>
<td align="right">7,393</td>
<td align="right"></td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">2,517</td>
<td align="right">53.4%</td>
<td align="right">2,106</td>
<td align="right">28.5%</td>
<td align="right">-16.3%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">20</td>
<td align="right">0.4%</td>
<td align="right">20</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
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
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,197</td>
<td align="right"></td>
<td align="right">5,287</td>
<td align="right"></td>
<td align="right">140.6%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">2,197</td>
<td align="right">100.0%</td>
<td align="right">5,287</td>
<td align="right">100.0%</td>
<td align="right">140.6%</td>
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
<td align="right">401</td>
<td align="right">18.3%</td>
<td align="right">1,003</td>
<td align="right">19.0%</td>
<td align="right">150.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">244</td>
<td align="right">11.1%</td>
<td align="right">902</td>
<td align="right">17.1%</td>
<td align="right">269.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">536</td>
<td align="right">24.4%</td>
<td align="right">1,072</td>
<td align="right">20.3%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">552</td>
<td align="right">25.1%</td>
<td align="right">1,069</td>
<td align="right">20.2%</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">243</td>
<td align="right">11.1%</td>
<td align="right">652</td>
<td align="right">12.3%</td>
<td align="right">168.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">163</td>
<td align="right">7.4%</td>
<td align="right">378</td>
<td align="right">7.1%</td>
<td align="right">131.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">58</td>
<td align="right">2.6%</td>
<td align="right">211</td>
<td align="right">4.0%</td>
<td align="right">263.8%</td>
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
<td align="right">225</td>
<td align="right">10.2%</td>
<td align="right">131</td>
<td align="right">2.5%</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">336</td>
<td align="right">15.3%</td>
<td align="right">1,381</td>
<td align="right">26.1%</td>
<td align="right">311.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">226</td>
<td align="right">10.3%</td>
<td align="right">768</td>
<td align="right">14.5%</td>
<td align="right">239.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">766</td>
<td align="right">34.9%</td>
<td align="right">1,382</td>
<td align="right">26.1%</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">362</td>
<td align="right">16.5%</td>
<td align="right">841</td>
<td align="right">15.9%</td>
<td align="right">132.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">183</td>
<td align="right">8.3%</td>
<td align="right">466</td>
<td align="right">8.8%</td>
<td align="right">154.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">63</td>
<td align="right">2.9%</td>
<td align="right">264</td>
<td align="right">5.0%</td>
<td align="right">319.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">36</td>
<td align="right">1.6%</td>
<td align="right">54</td>
<td align="right">1.0%</td>
<td align="right">50.0%</td>
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
<td align="left">_MAKE_FUNCTION</td>
<td align="right">40</td>
<td align="right">59,709</td>
<td align="right">149,172.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">300</td>
<td align="right">212,736</td>
<td align="right">70,812.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">560</td>
<td align="right">285,775</td>
<td align="right">50,931.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">260</td>
<td align="right">73,039</td>
<td align="right">27,991.9%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">40</td>
<td align="right">10,264</td>
<td align="right">25,560.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">640</td>
<td align="right">20,592</td>
<td align="right">3,117.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">135</td>
<td align="right">3,750</td>
<td align="right">2,677.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">10,399</td>
<td align="right">231,328</td>
<td align="right">2,124.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">10,399</td>
<td align="right">231,328</td>
<td align="right">2,124.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">10,020</td>
<td align="right">164,650</td>
<td align="right">1,543.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">380</td>
<td align="right">5,908</td>
<td align="right">1,454.7%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">10,500</td>
<td align="right">157,414</td>
<td align="right">1,399.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,420</td>
<td align="right">125,479</td>
<td align="right">1,104.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,834</td>
<td align="right">18,192</td>
<td align="right">891.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">535,207</td>
<td align="right">5,189,713</td>
<td align="right">869.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">24,747</td>
<td align="right">229,777</td>
<td align="right">828.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">815,585</td>
<td align="right">4,948,060</td>
<td align="right">506.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">290,393</td>
<td align="right">1,506,540</td>
<td align="right">418.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">10,720</td>
<td align="right">55,573</td>
<td align="right">418.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">170,439</td>
<td align="right">853,553</td>
<td align="right">400.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">134,624</td>
<td align="right">609,809</td>
<td align="right">353.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">396,288</td>
<td align="right">1,431,999</td>
<td align="right">261.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">386,000</td>
<td align="right">1,347,300</td>
<td align="right">249.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">230,763</td>
<td align="right">800,792</td>
<td align="right">247.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">54,161</td>
<td align="right">184,633</td>
<td align="right">240.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">387,541</td>
<td align="right">1,297,203</td>
<td align="right">234.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">119,487</td>
<td align="right">394,152</td>
<td align="right">229.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,672,413</td>
<td align="right">8,503,849</td>
<td align="right">218.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">643,118</td>
<td align="right">2,017,773</td>
<td align="right">213.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">509,984</td>
<td align="right">1,592,451</td>
<td align="right">212.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">543,765</td>
<td align="right">1,683,713</td>
<td align="right">209.6%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">200</td>
<td align="right">600</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">200</td>
<td align="right">600</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,530,790</td>
<td align="right">4,277,555</td>
<td align="right">179.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">82,499</td>
<td align="right">228,183</td>
<td align="right">176.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">177,166</td>
<td align="right">488,237</td>
<td align="right">175.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,364,512</td>
<td align="right">3,730,931</td>
<td align="right">173.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">233,179</td>
<td align="right">629,428</td>
<td align="right">169.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">135,630</td>
<td align="right">361,777</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">42,842</td>
<td align="right">113,077</td>
<td align="right">163.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">42,842</td>
<td align="right">113,077</td>
<td align="right">163.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">464,389</td>
<td align="right">1,204,654</td>
<td align="right">159.4%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">11,760</td>
<td align="right">29,944</td>
<td align="right">154.6%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">11,760</td>
<td align="right">29,944</td>
<td align="right">154.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,328,655</td>
<td align="right">3,359,022</td>
<td align="right">152.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">301,284</td>
<td align="right">760,556</td>
<td align="right">152.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,705,423</td>
<td align="right">4,293,821</td>
<td align="right">151.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,105,587</td>
<td align="right">2,778,873</td>
<td align="right">151.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,819,915</td>
<td align="right">4,538,541</td>
<td align="right">149.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">2,540,589</td>
<td align="right">6,297,436</td>
<td align="right">147.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">471,988</td>
<td align="right">1,164,698</td>
<td align="right">146.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">4,236,829</td>
<td align="right">10,390,663</td>
<td align="right">145.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">4,236,829</td>
<td align="right">10,383,231</td>
<td align="right">145.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">184,096</td>
<td align="right">450,027</td>
<td align="right">144.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,899,715</td>
<td align="right">4,637,540</td>
<td align="right">144.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">277,507</td>
<td align="right">659,590</td>
<td align="right">137.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">1,440,546</td>
<td align="right">3,363,034</td>
<td align="right">133.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,440,546</td>
<td align="right">3,363,034</td>
<td align="right">133.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,169,717</td>
<td align="right">5,005,237</td>
<td align="right">130.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">56,483</td>
<td align="right">129,385</td>
<td align="right">129.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">331,145</td>
<td align="right">752,538</td>
<td align="right">127.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">133,923</td>
<td align="right">298,848</td>
<td align="right">123.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">314,924</td>
<td align="right">694,353</td>
<td align="right">120.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">114,492</td>
<td align="right">251,328</td>
<td align="right">119.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">530,832</td>
<td align="right">1,165,162</td>
<td align="right">119.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,045,607</td>
<td align="right">2,279,455</td>
<td align="right">118.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">894,155</td>
<td align="right">1,930,427</td>
<td align="right">115.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,464,580</td>
<td align="right">3,141,195</td>
<td align="right">114.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,036,124</td>
<td align="right">8,638,268</td>
<td align="right">114.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">8,937,620</td>
<td align="right">19,066,203</td>
<td align="right">113.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">196,757</td>
<td align="right">419,723</td>
<td align="right">113.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">8,160</td>
<td align="right">17,359</td>
<td align="right">112.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">184,069</td>
<td align="right">388,482</td>
<td align="right">111.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">253,075</td>
<td align="right">522,355</td>
<td align="right">106.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">4,416,281</td>
<td align="right">9,017,068</td>
<td align="right">104.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">920,356</td>
<td align="right">1,843,299</td>
<td align="right">100.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">920,356</td>
<td align="right">1,843,299</td>
<td align="right">100.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,298,054</td>
<td align="right">4,564,835</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,298,054</td>
<td align="right">4,564,835</td>
<td align="right">98.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">7,387</td>
<td align="right">14,520</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">7,387</td>
<td align="right">14,520</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">201,241</td>
<td align="right">395,349</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,288,034</td>
<td align="right">4,400,185</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">202,105</td>
<td align="right">379,747</td>
<td align="right">87.9%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">446,856</td>
<td align="right">823,239</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">212,315</td>
<td align="right">380,080</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">115,382</td>
<td align="right">204,526</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">86,855</td>
<td align="right">150,664</td>
<td align="right">73.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,085,150</td>
<td align="right">3,611,249</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,336,050</td>
<td align="right">12,610,753</td>
<td align="right">71.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">10,291,123</td>
<td align="right">17,569,974</td>
<td align="right">70.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">2,467,384</td>
<td align="right">4,183,736</td>
<td align="right">69.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">79,027</td>
<td align="right">130,057</td>
<td align="right">64.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,284,729</td>
<td align="right">2,100,052</td>
<td align="right">63.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">20,100</td>
<td align="right">32,371</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">270,625</td>
<td align="right">428,846</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,080</td>
<td align="right">1,678</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,281,359</td>
<td align="right">1,916,301</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,692,781</td>
<td align="right">2,524,439</td>
<td align="right">49.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">8,119,783</td>
<td align="right">12,084,596</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">256,097</td>
<td align="right">372,851</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">343,905</td>
<td align="right">490,900</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">164,556</td>
<td align="right">229,926</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">465,061</td>
<td align="right">634,833</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">542,429</td>
<td align="right">738,359</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,404,775</td>
<td align="right">3,255,076</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">313,615</td>
<td align="right">421,313</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,017,239</td>
<td align="right">1,362,926</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">89,888</td>
<td align="right">118,621</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">48,720</td>
<td align="right">63,928</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">4,947,450</td>
<td align="right">6,488,310</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">1,347,766</td>
<td align="right">1,759,726</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">388,320</td>
<td align="right">500,772</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">58,439</td>
<td align="right">72,941</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">58,439</td>
<td align="right">72,941</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">211,892</td>
<td align="right">259,209</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">38,370</td>
<td align="right">45,839</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">44,132</td>
<td align="right">52,093</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">50,310</td>
<td align="right">57,617</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">101,679</td>
<td align="right">114,867</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">245,280</td>
<td align="right">275,460</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,701,197</td>
<td align="right">1,900,117</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">709,476</td>
<td align="right">789,168</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">709,516</td>
<td align="right">789,208</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">242,824</td>
<td align="right">268,745</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">378,663</td>
<td align="right">417,004</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">378,663</td>
<td align="right">417,004</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">536,689</td>
<td align="right">588,597</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,169,814</td>
<td align="right">1,282,312</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">105,140</td>
<td align="right">115,141</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">3,195,657</td>
<td align="right">3,456,681</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">482,952</td>
<td align="right">500,030</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">436,293</td>
<td align="right">443,444</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">463,351</td>
<td align="right">470,514</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">463,351</td>
<td align="right">470,514</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">503,436</td>
<td align="right">497,587</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">261,345</td>
<td align="right">263,566</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">23,841</td>
<td align="right">23,642</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">59,700</td>
<td align="right">60,020</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">59,700</td>
<td align="right">60,020</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">380,157</td>
<td align="right">378,800</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">58,473</td>
<td align="right">58,537</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">356,362</td>
<td align="right">356,727</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">64,972</td>
<td align="right">64,986</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">56,121</td>
<td align="right">56,132</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">174,140</td>
<td align="right">174,139</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">215,400</td>
<td align="right">215,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">150,300</td>
<td align="right">150,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">105,400</td>
<td align="right">105,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">62,220</td>
<td align="right">62,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">62,220</td>
<td align="right">62,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">49,400</td>
<td align="right">49,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">306,278</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right"></td>
<td align="right">201,056</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">135,600</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">72,645</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">58,571</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right"></td>
<td align="right">55,876</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right"></td>
<td align="right">54,438</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right"></td>
<td align="right">42,333</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">33,515</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">29,062</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right"></td>
<td align="right">26,433</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right"></td>
<td align="right">26,433</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right"></td>
<td align="right">18,859</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">17,356</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right"></td>
<td align="right">13,331</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right"></td>
<td align="right">13,331</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">12,541</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right"></td>
<td align="right">12,105</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right"></td>
<td align="right">11,344</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right"></td>
<td align="right">10,387</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right"></td>
<td align="right">9,276</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right"></td>
<td align="right">8,858</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right"></td>
<td align="right">8,811</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right"></td>
<td align="right">8,811</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right"></td>
<td align="right">8,811</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right"></td>
<td align="right">8,811</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right"></td>
<td align="right">8,811</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right"></td>
<td align="right">7,432</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">5,208</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">3,314</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">1,767</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right"></td>
<td align="right">20</td>
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
<td align="right">40</td>
<td align="right">274</td>
<td align="right">585.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">280</td>
<td align="right">730</td>
<td align="right">160.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right"></td>
<td align="right">500</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right"></td>
<td align="right">60</td>
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
Stats gathered on: 2024-10-05
