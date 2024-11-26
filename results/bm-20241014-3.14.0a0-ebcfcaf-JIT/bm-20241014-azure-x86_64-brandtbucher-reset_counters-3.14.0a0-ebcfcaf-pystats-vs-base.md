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
<td align="left">UNARY_INVERT</td>
<td align="right">4,121,849</td>
<td align="right">3,014,531</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,093,568</td>
<td align="right">10,930,070</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">41,450,279</td>
<td align="right">46,639,615</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">64,821,179</td>
<td align="right">59,120,935</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,795,474</td>
<td align="right">8,988,520</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">58,419</td>
<td align="right">62,339</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,943,462</td>
<td align="right">3,118,742</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,674,293</td>
<td align="right">4,405,585</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">207,548,445</td>
<td align="right">196,492,960</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">31,983,048</td>
<td align="right">30,295,649</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">138,363</td>
<td align="right">145,540</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,538,288</td>
<td align="right">10,053,543</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,418,115</td>
<td align="right">10,933,533</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">55,768,471</td>
<td align="right">53,634,730</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">14,056,113</td>
<td align="right">13,528,102</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">130,754,445</td>
<td align="right">134,692,063</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">434,652,490</td>
<td align="right">423,940,395</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">238,458</td>
<td align="right">244,042</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">13,496,454</td>
<td align="right">13,207,654</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">359,839,808</td>
<td align="right">352,149,548</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">54,723,332</td>
<td align="right">53,655,229</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">386,615,222</td>
<td align="right">379,167,826</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">160,284,779</td>
<td align="right">157,413,046</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">280,889,545</td>
<td align="right">275,904,200</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">268,726,020</td>
<td align="right">264,098,751</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">28,206,925</td>
<td align="right">27,727,512</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">184,869,032</td>
<td align="right">181,814,302</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">139,188,785</td>
<td align="right">136,901,313</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">730,306,122</td>
<td align="right">718,330,174</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">109,689,251</td>
<td align="right">107,908,285</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">35,754,371</td>
<td align="right">35,186,206</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">694,446</td>
<td align="right">704,747</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">121,203,605</td>
<td align="right">119,441,203</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">190,137,282</td>
<td align="right">187,522,542</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">88,916,818</td>
<td align="right">87,735,584</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">51,056,732</td>
<td align="right">50,410,548</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">486,574,646</td>
<td align="right">480,771,388</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">123,769,925</td>
<td align="right">122,371,273</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">74,524,147</td>
<td align="right">73,713,965</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,556,910,665</td>
<td align="right">1,540,164,958</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">2,895,502,837</td>
<td align="right">2,865,949,658</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">128,303,674</td>
<td align="right">129,593,466</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">39,295,151</td>
<td align="right">38,906,278</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,075,611,863</td>
<td align="right">2,056,084,618</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,922,173</td>
<td align="right">19,096,852</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">57,431,201</td>
<td align="right">57,940,731</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">217,272,752</td>
<td align="right">215,410,270</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">46,505,762</td>
<td align="right">46,122,769</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">622,911,958</td>
<td align="right">617,808,206</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,323,569</td>
<td align="right">37,623,119</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,087,248,419</td>
<td align="right">2,070,786,296</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">29,422,884</td>
<td align="right">29,194,273</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">105,776,093</td>
<td align="right">104,955,194</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">298,150,425</td>
<td align="right">295,860,706</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">95,581,324</td>
<td align="right">94,849,756</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,271,323,658</td>
<td align="right">12,179,457,712</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">603,237,173</td>
<td align="right">598,750,556</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,822,355,173</td>
<td align="right">3,794,038,700</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">161,567,292</td>
<td align="right">160,376,087</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">108,478,298</td>
<td align="right">107,688,058</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">11,380</td>
<td align="right">11,300</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">41,764,324</td>
<td align="right">42,054,823</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,028,319,471</td>
<td align="right">2,014,249,345</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,174,882,509</td>
<td align="right">2,159,848,052</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,686,637,806</td>
<td align="right">2,668,567,761</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">234,763,289</td>
<td align="right">233,209,614</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">112,203,518</td>
<td align="right">111,467,823</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">216,871,541</td>
<td align="right">215,476,850</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">98,929,158</td>
<td align="right">98,302,141</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">23,501,200</td>
<td align="right">23,354,833</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">679,485,238</td>
<td align="right">675,315,639</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,671,916,007</td>
<td align="right">3,650,535,720</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">752,764,376</td>
<td align="right">748,627,900</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">419,708,853</td>
<td align="right">417,446,063</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,368,676,167</td>
<td align="right">1,361,495,806</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">76,934,966</td>
<td align="right">76,536,981</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">29,445,867</td>
<td align="right">29,596,716</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,844,408</td>
<td align="right">142,548,617</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,448,321,626</td>
<td align="right">1,441,168,354</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">456,564,439</td>
<td align="right">454,439,592</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">44,136,356</td>
<td align="right">44,334,181</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">434,484,889</td>
<td align="right">432,560,507</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">197,284,265</td>
<td align="right">196,416,414</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">111,574,700</td>
<td align="right">111,105,635</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">772,216</td>
<td align="right">768,976</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,801,561,180</td>
<td align="right">2,790,638,834</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,353,999,377</td>
<td align="right">1,348,793,984</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">765,348,913</td>
<td align="right">762,477,202</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">247,812,599</td>
<td align="right">246,899,122</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">110,508,809</td>
<td align="right">110,111,291</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">241,164,847</td>
<td align="right">240,305,454</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">462,436,506</td>
<td align="right">464,058,753</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">93,052,727</td>
<td align="right">92,732,575</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">33,204,017</td>
<td align="right">33,090,574</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">3,500,209,258</td>
<td align="right">3,488,636,044</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">56,589,128</td>
<td align="right">56,415,904</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">171,590,348</td>
<td align="right">171,069,556</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">76,308,270</td>
<td align="right">76,531,722</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,456,468</td>
<td align="right">3,466,228</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,803,232,627</td>
<td align="right">1,798,179,280</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">429,730</td>
<td align="right">428,530</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">92,214,184</td>
<td align="right">92,447,243</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,693,899</td>
<td align="right">3,684,902</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">110,944,189</td>
<td align="right">111,183,811</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">19,130,724</td>
<td align="right">19,168,474</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,309,296</td>
<td align="right">9,327,284</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">256,134,637</td>
<td align="right">256,606,782</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">501,820</td>
<td align="right">502,720</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">56,419,961</td>
<td align="right">56,515,345</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">129,123,213</td>
<td align="right">128,920,831</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">322,621,635</td>
<td align="right">323,088,545</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">201,321,324</td>
<td align="right">201,032,576</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,355,971</td>
<td align="right">67,451,419</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,460,991</td>
<td align="right">3,456,123</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">486,412,934</td>
<td align="right">485,742,323</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">340,058,079</td>
<td align="right">340,520,563</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">91,800,232</td>
<td align="right">91,919,999</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,720,032</td>
<td align="right">105,583,798</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">242,081,019</td>
<td align="right">241,807,824</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,657,137,229</td>
<td align="right">1,655,290,116</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,521,682</td>
<td align="right">58,576,087</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">39,874,831</td>
<td align="right">39,911,536</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">15,345,111</td>
<td align="right">15,358,557</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">199,656,231</td>
<td align="right">199,513,929</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">198,193,884</td>
<td align="right">198,334,436</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">658,110</td>
<td align="right">657,669</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">12,002</td>
<td align="right">12,010</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">438,490,483</td>
<td align="right">438,243,158</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">303,817,949</td>
<td align="right">303,657,260</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">60,891,462</td>
<td align="right">60,921,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">14,822,063</td>
<td align="right">14,829,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,634,295</td>
<td align="right">35,651,797</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">43,057,228</td>
<td align="right">43,077,092</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">9,010,513</td>
<td align="right">9,014,245</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">66,685,218</td>
<td align="right">66,659,207</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">548,084,553</td>
<td align="right">548,282,407</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">255,553</td>
<td align="right">255,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">50,279,141</td>
<td align="right">50,262,790</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">40,750,870</td>
<td align="right">40,762,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,207,012</td>
<td align="right">1,207,362</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">49,905,700</td>
<td align="right">49,892,598</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">65,330</td>
<td align="right">65,346</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,043,956</td>
<td align="right">35,050,432</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">82,146,971</td>
<td align="right">82,161,630</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">11,000,437</td>
<td align="right">11,002,124</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,327,625,096</td>
<td align="right">1,327,436,747</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,318,722</td>
<td align="right">21,316,173</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">341,608,986</td>
<td align="right">341,649,318</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,988,490</td>
<td align="right">20,986,444</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,321,108</td>
<td align="right">21,319,034</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">62,592,691</td>
<td align="right">62,587,901</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">99,067,334</td>
<td align="right">99,073,923</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">339,639,199</td>
<td align="right">339,618,232</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">262,530,169</td>
<td align="right">262,516,372</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">313,039,013</td>
<td align="right">313,054,389</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">27,559,264</td>
<td align="right">27,560,505</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">119,979,041</td>
<td align="right">119,982,670</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,325,961</td>
<td align="right">20,326,467</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">138,338,607</td>
<td align="right">138,335,499</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">185,428,583</td>
<td align="right">185,432,124</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,828,811</td>
<td align="right">5,828,715</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,381,625</td>
<td align="right">82,382,627</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">34,603,484</td>
<td align="right">34,603,070</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">10,868,299</td>
<td align="right">10,868,298</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">156,685,782</td>
<td align="right">156,685,770</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">144,206,700</td>
<td align="right">144,206,694</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">330,764,661</td>
<td align="right">330,764,652</td>
<td align="right">-0.0%</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">10,336,083</td>
<td align="right">10,336,083</td>
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
<td align="right">651,092</td>
<td align="right">651,092</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">149,591</td>
<td align="right">149,591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">94,680</td>
<td align="right">94,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,641</td>
<td align="right">91,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">29,649</td>
<td align="right">29,649</td>
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
<td align="right">385,453,496</td>
<td align="right">4.0%</td>
<td align="right">377,999,707</td>
<td align="right">3.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,478,671</td>
<td align="right">0.3%</td>
<td align="right">29,554,990</td>
<td align="right">0.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,301,888,718</td>
<td align="right">95.7%</td>
<td align="right">9,301,100,121</td>
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
<td align="right">1,120,665</td>
<td align="right">65.2%</td>
<td align="right">1,126,865</td>
<td align="right">65.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">597,101</td>
<td align="right">34.8%</td>
<td align="right">598,734</td>
<td align="right">34.7%</td>
<td align="right">0.3%</td>
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
<td align="left">true divide other</td>
<td align="right">2,442</td>
<td align="right">0.2%</td>
<td align="right">2,682</td>
<td align="right">0.2%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,886</td>
<td align="right">0.3%</td>
<td align="right">3,131</td>
<td align="right">0.3%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">83,459</td>
<td align="right">7.4%</td>
<td align="right">89,509</td>
<td align="right">7.9%</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,898</td>
<td align="right">1.3%</td>
<td align="right">14,229</td>
<td align="right">1.3%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">32,493</td>
<td align="right">2.9%</td>
<td align="right">31,603</td>
<td align="right">2.8%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">6,881</td>
<td align="right">0.6%</td>
<td align="right">7,066</td>
<td align="right">0.6%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">20,912</td>
<td align="right">1.9%</td>
<td align="right">21,330</td>
<td align="right">1.9%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,543</td>
<td align="right">0.8%</td>
<td align="right">8,713</td>
<td align="right">0.8%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">8,723</td>
<td align="right">0.8%</td>
<td align="right">8,854</td>
<td align="right">0.8%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,591</td>
<td align="right">0.5%</td>
<td align="right">5,666</td>
<td align="right">0.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,065</td>
<td align="right">2.9%</td>
<td align="right">32,204</td>
<td align="right">2.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,042</td>
<td align="right">0.9%</td>
<td align="right">10,082</td>
<td align="right">0.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,548</td>
<td align="right">0.2%</td>
<td align="right">2,558</td>
<td align="right">0.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">48,146</td>
<td align="right">4.3%</td>
<td align="right">48,299</td>
<td align="right">4.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">47,633</td>
<td align="right">4.3%</td>
<td align="right">47,526</td>
<td align="right">4.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">835</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,560</td>
<td align="right">0.9%</td>
<td align="right">10,565</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,606</td>
<td align="right">69.7%</td>
<td align="right">781,612</td>
<td align="right">69.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">401</td>
<td align="right">0.0%</td>
<td align="right">401</td>
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
<td align="right">111,574,700</td>
<td align="right">100.0%</td>
<td align="right">111,105,635</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">4,795,979</td>
<td align="right">0.1%</td>
<td align="right">4,802,508</td>
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
<td align="right">547,774,020</td>
<td align="right">8.1%</td>
<td align="right">547,971,056</td>
<td align="right">8.1%</td>
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
<td align="right">6,192,154,925</td>
<td align="right">91.8%</td>
<td align="right">6,191,596,691</td>
<td align="right">91.8%</td>
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
<td align="right">219,033</td>
<td align="right">54.7%</td>
<td align="right">219,823</td>
<td align="right">54.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,502</td>
<td align="right">45.3%</td>
<td align="right">181,649</td>
<td align="right">45.2%</td>
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
<td align="left">list slice</td>
<td align="right">12,733</td>
<td align="right">5.8%</td>
<td align="right">12,871</td>
<td align="right">5.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,338</td>
<td align="right">9.7%</td>
<td align="right">21,519</td>
<td align="right">9.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">2,500</td>
<td align="right">1.1%</td>
<td align="right">2,520</td>
<td align="right">1.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">8,448</td>
<td align="right">3.9%</td>
<td align="right">8,489</td>
<td align="right">3.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">65,614</td>
<td align="right">30.0%</td>
<td align="right">65,925</td>
<td align="right">30.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">26,640</td>
<td align="right">12.2%</td>
<td align="right">26,760</td>
<td align="right">12.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">57,972</td>
<td align="right">26.5%</td>
<td align="right">57,945</td>
<td align="right">26.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">19,128</td>
<td align="right">8.7%</td>
<td align="right">19,134</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">2.0%</td>
<td align="right">4,300</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,271,841,037</td>
<td align="right">98.9%</td>
<td align="right">12,247,055,224</td>
<td align="right">98.9%</td>
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
<td align="right">690,188</td>
<td align="right">0.0%</td>
<td align="right">690,421</td>
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
<td align="right">139,375,950</td>
<td align="right">1.1%</td>
<td align="right">139,354,536</td>
<td align="right">1.1%</td>
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
<td align="right">32,461</td>
<td align="right">0.0%</td>
<td align="right">32,460</td>
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
<td align="right">3,184,266</td>
<td align="right">100.0%</td>
<td align="right">3,184,356</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">2,389</td>
<td align="right">696.5%</td>
<td align="right">2,389</td>
<td align="right">696.5%</td>
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
<td align="right">761</td>
<td align="right">221.9%</td>
<td align="right">761</td>
<td align="right">221.9%</td>
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
<td align="right">750,960</td>
<td align="right">92.0%</td>
<td align="right">769,787</td>
<td align="right">92.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">35,767</td>
<td align="right">4.4%</td>
<td align="right">35,777</td>
<td align="right">4.3%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,089,145</td>
<td align="right">0.0%</td>
<td align="right">1,058,914</td>
<td align="right">0.0%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">98,722,807</td>
<td align="right">1.8%</td>
<td align="right">98,096,823</td>
<td align="right">1.8%</td>
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
<td align="right">5,491,849,940</td>
<td align="right">98.2%</td>
<td align="right">5,488,395,146</td>
<td align="right">98.2%</td>
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
<td align="right">74,114</td>
<td align="right">32.7%</td>
<td align="right">73,537</td>
<td align="right">32.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">152,440</td>
<td align="right">67.3%</td>
<td align="right">151,423</td>
<td align="right">67.3%</td>
<td align="right">-0.7%</td>
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
<td align="right">31,718</td>
<td align="right">20.8%</td>
<td align="right">30,095</td>
<td align="right">19.9%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,520</td>
<td align="right">2.3%</td>
<td align="right">3,580</td>
<td align="right">2.4%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">11,330</td>
<td align="right">7.4%</td>
<td align="right">11,178</td>
<td align="right">7.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">40,195</td>
<td align="right">26.4%</td>
<td align="right">40,729</td>
<td align="right">26.9%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,933</td>
<td align="right">11.8%</td>
<td align="right">18,017</td>
<td align="right">11.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,429</td>
<td align="right">12.7%</td>
<td align="right">19,509</td>
<td align="right">12.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,261</td>
<td align="right">0.8%</td>
<td align="right">1,263</td>
<td align="right">0.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,224</td>
<td align="right">8.0%</td>
<td align="right">12,222</td>
<td align="right">8.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.0%</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,700</td>
<td align="right">1.8%</td>
<td align="right">2,700</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">490</td>
<td align="right">0.3%</td>
<td align="right">490</td>
<td align="right">0.3%</td>
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
<td align="right">37,237,568</td>
<td align="right">1.5%</td>
<td align="right">37,536,638</td>
<td align="right">1.5%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,452,893,870</td>
<td align="right">98.4%</td>
<td align="right">2,451,020,697</td>
<td align="right">98.4%</td>
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
<td align="right">2,545,460</td>
<td align="right">0.1%</td>
<td align="right">2,545,500</td>
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
<td align="right">73,242</td>
<td align="right">54.7%</td>
<td align="right">73,722</td>
<td align="right">54.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">60,699</td>
<td align="right">45.3%</td>
<td align="right">60,699</td>
<td align="right">45.2%</td>
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
<td align="right">15,322</td>
<td align="right">20.9%</td>
<td align="right">15,582</td>
<td align="right">21.1%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">28,014</td>
<td align="right">38.2%</td>
<td align="right">28,134</td>
<td align="right">38.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,257</td>
<td align="right">20.8%</td>
<td align="right">15,316</td>
<td align="right">20.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,649</td>
<td align="right">20.0%</td>
<td align="right">14,690</td>
<td align="right">19.9%</td>
<td align="right">0.3%</td>
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
<td align="right">27,036,224</td>
<td align="right">3.9%</td>
<td align="right">21,981,421</td>
<td align="right">3.2%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">566,803,756</td>
<td align="right">82.6%</td>
<td align="right">564,942,465</td>
<td align="right">83.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">92,057,026</td>
<td align="right">13.4%</td>
<td align="right">92,284,625</td>
<td align="right">13.6%</td>
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
<td align="right">557,854</td>
<td align="right">83.6%</td>
<td align="right">462,481</td>
<td align="right">80.1%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">109,080</td>
<td align="right">16.4%</td>
<td align="right">114,570</td>
<td align="right">19.9%</td>
<td align="right">5.0%</td>
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
<td align="right">5,941</td>
<td align="right">5.4%</td>
<td align="right">7,180</td>
<td align="right">6.3%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">620</td>
<td align="right">0.6%</td>
<td align="right">697</td>
<td align="right">0.6%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.7%</td>
<td align="right">820</td>
<td align="right">0.7%</td>
<td align="right">10.8%</td>
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
<td align="left">enumerate</td>
<td align="right">11,840</td>
<td align="right">10.9%</td>
<td align="right">12,545</td>
<td align="right">10.9%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,606</td>
<td align="right">6.1%</td>
<td align="right">6,923</td>
<td align="right">6.0%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,456</td>
<td align="right">3.2%</td>
<td align="right">3,609</td>
<td align="right">3.2%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">37,568</td>
<td align="right">34.4%</td>
<td align="right">39,193</td>
<td align="right">34.2%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,223</td>
<td align="right">4.8%</td>
<td align="right">5,443</td>
<td align="right">4.8%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,567</td>
<td align="right">2.4%</td>
<td align="right">2,667</td>
<td align="right">2.3%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,696</td>
<td align="right">6.1%</td>
<td align="right">6,955</td>
<td align="right">6.1%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,662</td>
<td align="right">7.0%</td>
<td align="right">7,955</td>
<td align="right">6.9%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,985</td>
<td align="right">11.0%</td>
<td align="right">12,327</td>
<td align="right">10.8%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">7,916</td>
<td align="right">7.3%</td>
<td align="right">8,016</td>
<td align="right">7.0%</td>
<td align="right">1.3%</td>
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
<td align="right">432,518,746</td>
<td align="right">3.3%</td>
<td align="right">421,807,708</td>
<td align="right">3.2%</td>
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
<td align="right">487,020,198</td>
<td align="right">3.7%</td>
<td align="right">481,327,590</td>
<td align="right">3.7%</td>
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
<td align="right">12,232,158,299</td>
<td align="right">93.0%</td>
<td align="right">12,196,979,056</td>
<td align="right">93.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,052,720</td>
<td align="right">0.0%</td>
<td align="right">1,052,720</td>
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
<td align="right">10,843,183</td>
<td align="right">96.1%</td>
<td align="right">10,737,511</td>
<td align="right">96.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">444,634</td>
<td align="right">3.9%</td>
<td align="right">441,837</td>
<td align="right">4.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">360</td>
<td align="right">0.1%</td>
<td align="right">380</td>
<td align="right">0.1%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3,464</td>
<td align="right">0.8%</td>
<td align="right">3,284</td>
<td align="right">0.7%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">15,532</td>
<td align="right">3.5%</td>
<td align="right">15,283</td>
<td align="right">3.5%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">69,693</td>
<td align="right">15.7%</td>
<td align="right">68,602</td>
<td align="right">15.5%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">78,425</td>
<td align="right">17.6%</td>
<td align="right">77,478</td>
<td align="right">17.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">2,675</td>
<td align="right">0.6%</td>
<td align="right">2,654</td>
<td align="right">0.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,444</td>
<td align="right">1.2%</td>
<td align="right">5,404</td>
<td align="right">1.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">21,433</td>
<td align="right">4.8%</td>
<td align="right">21,540</td>
<td align="right">4.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">15,251</td>
<td align="right">3.4%</td>
<td align="right">15,194</td>
<td align="right">3.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">32,386</td>
<td align="right">7.3%</td>
<td align="right">32,339</td>
<td align="right">7.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">37,204</td>
<td align="right">8.4%</td>
<td align="right">37,249</td>
<td align="right">8.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">139,280</td>
<td align="right">31.3%</td>
<td align="right">139,346</td>
<td align="right">31.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">5,300</td>
<td align="right">1.2%</td>
<td align="right">5,300</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,944</td>
<td align="right">0.7%</td>
<td align="right">2,944</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,100</td>
<td align="right">0.2%</td>
<td align="right">1,100</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">680</td>
<td align="right">0.2%</td>
<td align="right">680</td>
<td align="right">0.2%</td>
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
<td align="right">3,803,260,827</td>
<td align="right">99.5%</td>
<td align="right">3,780,930,208</td>
<td align="right">99.5%</td>
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
<td align="right">414,508</td>
<td align="right">0.0%</td>
<td align="right">414,188</td>
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
<td align="right">19,880,703</td>
<td align="right">0.5%</td>
<td align="right">19,881,009</td>
<td align="right">0.5%</td>
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
<td align="right">9,294</td>
<td align="right">0.0%</td>
<td align="right">9,294</td>
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
<td align="right">450,983</td>
<td align="right">100.0%</td>
<td align="right">451,183</td>
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
<td align="right">69,779,833</td>
<td align="right">100.0%</td>
<td align="right">66,834,707</td>
<td align="right">100.0%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,041</td>
<td align="right">0.0%</td>
<td align="right">6,049</td>
<td align="right">0.0%</td>
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
<td align="right">5,961</td>
<td align="right">100.0%</td>
<td align="right">5,961</td>
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
<td align="right">144,152,769</td>
<td align="right">17.1%</td>
<td align="right">144,152,763</td>
<td align="right">17.1%</td>
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
<td align="right">700,352,471</td>
<td align="right">82.9%</td>
<td align="right">700,352,488</td>
<td align="right">82.9%</td>
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
<td align="right">4,637</td>
<td align="right">8.5%</td>
<td align="right">4,637</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">49,874</td>
<td align="right">91.5%</td>
<td align="right">49,874</td>
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
<td align="right">66.5%</td>
<td align="right">33,180</td>
<td align="right">66.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,020</td>
<td align="right">20.1%</td>
<td align="right">10,020</td>
<td align="right">20.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,428</td>
<td align="right">8.9%</td>
<td align="right">4,428</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,240</td>
<td align="right">4.5%</td>
<td align="right">2,240</td>
<td align="right">4.5%</td>
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
<td align="right">28,038,752</td>
<td align="right">1.5%</td>
<td align="right">27,559,413</td>
<td align="right">1.5%</td>
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
<td align="right">1,683,806,813</td>
<td align="right">91.6%</td>
<td align="right">1,678,383,429</td>
<td align="right">91.6%</td>
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
<td align="right">127,182,112</td>
<td align="right">6.9%</td>
<td align="right">127,131,079</td>
<td align="right">6.9%</td>
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
<td align="right">76,628</td>
<td align="right">3.0%</td>
<td align="right">76,555</td>
<td align="right">3.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,488,474</td>
<td align="right">97.0%</td>
<td align="right">2,487,611</td>
<td align="right">97.0%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">3,043</td>
<td align="right">4.0%</td>
<td align="right">3,223</td>
<td align="right">4.2%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">2,985</td>
<td align="right">3.9%</td>
<td align="right">2,885</td>
<td align="right">3.8%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,436</td>
<td align="right">5.8%</td>
<td align="right">4,416</td>
<td align="right">5.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">32,166</td>
<td align="right">42.0%</td>
<td align="right">32,024</td>
<td align="right">41.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,828</td>
<td align="right">12.8%</td>
<td align="right">9,837</td>
<td align="right">12.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">15,445</td>
<td align="right">20.2%</td>
<td align="right">15,445</td>
<td align="right">20.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">4,981</td>
<td align="right">6.5%</td>
<td align="right">4,981</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">2,100</td>
<td align="right">2.7%</td>
<td align="right">2,100</td>
<td align="right">2.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">804</td>
<td align="right">1.0%</td>
<td align="right">804</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">780</td>
<td align="right">1.0%</td>
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
<td align="right">138,363</td>
<td align="right">100.0%</td>
<td align="right">145,540</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">859,619,067</td>
<td align="right">89.0%</td>
<td align="right">857,743,915</td>
<td align="right">89.0%</td>
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
<td align="right">105,635,113</td>
<td align="right">10.9%</td>
<td align="right">105,498,561</td>
<td align="right">11.0%</td>
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
<td align="right">71,911</td>
<td align="right">84.6%</td>
<td align="right">72,224</td>
<td align="right">84.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,048</td>
<td align="right">15.4%</td>
<td align="right">13,053</td>
<td align="right">15.3%</td>
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
<td align="left">array slice</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">120</td>
<td align="right">0.2%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">640</td>
<td align="right">0.9%</td>
<td align="right">660</td>
<td align="right">0.9%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,620</td>
<td align="right">2.3%</td>
<td align="right">1,660</td>
<td align="right">2.3%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">14,240</td>
<td align="right">19.8%</td>
<td align="right">14,440</td>
<td align="right">20.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">6,885</td>
<td align="right">9.6%</td>
<td align="right">6,978</td>
<td align="right">9.7%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,540</td>
<td align="right">2.1%</td>
<td align="right">1,520</td>
<td align="right">2.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,420</td>
<td align="right">6.1%</td>
<td align="right">4,380</td>
<td align="right">6.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">42,483</td>
<td align="right">59.1%</td>
<td align="right">42,463</td>
<td align="right">58.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">26,780,743</td>
<td align="right">0.6%</td>
<td align="right">26,121,872</td>
<td align="right">0.6%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,560,480,693</td>
<td align="right">96.7%</td>
<td align="right">4,545,991,390</td>
<td align="right">96.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,707,644</td>
<td align="right">2.7%</td>
<td align="right">128,513,786</td>
<td align="right">2.7%</td>
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
<td align="right">228,190</td>
<td align="right">24.9%</td>
<td align="right">219,641</td>
<td align="right">24.5%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">687,616</td>
<td align="right">75.1%</td>
<td align="right">675,178</td>
<td align="right">75.5%</td>
<td align="right">-1.8%</td>
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
<td align="right">61,339</td>
<td align="right">26.9%</td>
<td align="right">50,555</td>
<td align="right">23.0%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,444</td>
<td align="right">2.8%</td>
<td align="right">6,628</td>
<td align="right">3.0%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">82,142</td>
<td align="right">36.0%</td>
<td align="right">83,838</td>
<td align="right">38.2%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">14,910</td>
<td align="right">6.5%</td>
<td align="right">15,130</td>
<td align="right">6.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,582</td>
<td align="right">7.3%</td>
<td align="right">16,766</td>
<td align="right">7.6%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">6,484</td>
<td align="right">2.8%</td>
<td align="right">6,459</td>
<td align="right">2.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">19,234</td>
<td align="right">8.4%</td>
<td align="right">19,211</td>
<td align="right">8.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,563</td>
<td align="right">8.1%</td>
<td align="right">18,562</td>
<td align="right">8.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,469</td>
<td align="right">0.6%</td>
<td align="right">1,469</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
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
<td align="right">0.1%</td>
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
<td align="right">198,376</td>
<td align="right">0.0%</td>
<td align="right">203,789</td>
<td align="right">0.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,058,061,293</td>
<td align="right">100.0%</td>
<td align="right">2,057,366,187</td>
<td align="right">100.0%</td>
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
<td align="right">3.7%</td>
<td align="right">1,882</td>
<td align="right">3.9%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">46,379</td>
<td align="right">96.3%</td>
<td align="right">46,431</td>
<td align="right">96.1%</td>
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
<td align="left">sequence</td>
<td align="right">1,116</td>
<td align="right">63.3%</td>
<td align="right">1,235</td>
<td align="right">65.6%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">21.6%</td>
<td align="right">380</td>
<td align="right">20.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">267</td>
<td align="right">15.1%</td>
<td align="right">267</td>
<td align="right">14.2%</td>
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
<td align="right">847,031,964</td>
<td align="right">1.2%</td>
<td align="right">835,624,001</td>
<td align="right">1.2%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,138,637,872</td>
<td align="right">3.0%</td>
<td align="right">2,119,308,368</td>
<td align="right">3.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">45,621,390,625</td>
<td align="right">63.2%</td>
<td align="right">45,344,155,190</td>
<td align="right">63.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">23,528,645,446</td>
<td align="right">32.6%</td>
<td align="right">23,386,163,363</td>
<td align="right">32.6%</td>
<td align="right">-0.6%</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">432,518,746</td>
<td align="right">20.3%</td>
<td align="right">421,807,708</td>
<td align="right">20.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">385,453,496</td>
<td align="right">18.1%</td>
<td align="right">377,999,707</td>
<td align="right">17.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">37,237,568</td>
<td align="right">1.7%</td>
<td align="right">37,536,638</td>
<td align="right">1.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">98,722,807</td>
<td align="right">4.6%</td>
<td align="right">98,096,823</td>
<td align="right">4.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">111,574,700</td>
<td align="right">5.2%</td>
<td align="right">111,105,635</td>
<td align="right">5.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">92,057,026</td>
<td align="right">4.3%</td>
<td align="right">92,284,625</td>
<td align="right">4.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">128,707,644</td>
<td align="right">6.0%</td>
<td align="right">128,513,786</td>
<td align="right">6.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">105,635,113</td>
<td align="right">5.0%</td>
<td align="right">105,498,561</td>
<td align="right">5.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">547,774,020</td>
<td align="right">25.7%</td>
<td align="right">547,971,056</td>
<td align="right">25.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">144,152,769</td>
<td align="right">6.8%</td>
<td align="right">144,152,763</td>
<td align="right">6.8%</td>
<td align="right">-0.0%</td>
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
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">16,698,938</td>
<td align="right">2.0%</td>
<td align="right">17,216,909</td>
<td align="right">2.1%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">136,203,208</td>
<td align="right">16.1%</td>
<td align="right">132,471,395</td>
<td align="right">15.9%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">181,856,755</td>
<td align="right">21.5%</td>
<td align="right">179,252,425</td>
<td align="right">21.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">86,285,239</td>
<td align="right">10.2%</td>
<td align="right">85,796,919</td>
<td align="right">10.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,268,762</td>
<td align="right">2.2%</td>
<td align="right">18,174,647</td>
<td align="right">2.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">57,243,399</td>
<td align="right">6.8%</td>
<td align="right">57,427,892</td>
<td align="right">6.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">70,172,767</td>
<td align="right">8.3%</td>
<td align="right">70,291,037</td>
<td align="right">8.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">117,805,284</td>
<td align="right">13.9%</td>
<td align="right">117,745,293</td>
<td align="right">14.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,177,240</td>
<td align="right">2.4%</td>
<td align="right">20,177,240</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">13,501,091</td>
<td align="right">1.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">13,143,312</td>
<td align="right">1.6%</td>
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
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,001,139,308</td>
<td align="right">13.9%</td>
<td align="right">996,185,560</td>
<td align="right">13.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,005,587,689</td>
<td align="right">14.0%</td>
<td align="right">1,000,633,941</td>
<td align="right">14.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,576,301,112</td>
<td align="right">77.5%</td>
<td align="right">5,550,662,443</td>
<td align="right">77.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,385,755,891</td>
<td align="right">74.9%</td>
<td align="right">5,364,975,392</td>
<td align="right">74.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,806,972,686</td>
<td align="right">25.1%</td>
<td align="right">1,801,915,153</td>
<td align="right">25.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,806,972,686</td>
<td align="right">25.1%</td>
<td align="right">1,801,915,153</td>
<td align="right">25.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">334,370,868</td>
<td align="right">4.6%</td>
<td align="right">333,453,069</td>
<td align="right">4.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">801,384,997</td>
<td align="right">11.1%</td>
<td align="right">801,281,212</td>
<td align="right">11.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,608,141</td>
<td align="right">1.2%</td>
<td align="right">84,598,835</td>
<td align="right">1.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">203,948,782</td>
<td align="right">2.8%</td>
<td align="right">203,938,714</td>
<td align="right">2.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">28,068,171</td>
<td align="right">0.4%</td>
<td align="right">28,067,263</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">38,865,690</td>
<td align="right">0.5%</td>
<td align="right">38,865,790</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,418,292</td>
<td align="right">0.1%</td>
<td align="right">4,418,292</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">30,089</td>
<td align="right">0.0%</td>
<td align="right">30,089</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">8,519,633</td>
<td align="right"></td>
<td align="right">11,330,684</td>
<td align="right"></td>
<td align="right">33.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">61,978,257</td>
<td align="right"></td>
<td align="right">70,607,154</td>
<td align="right"></td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">54,432,007</td>
<td align="right"></td>
<td align="right">60,251,093</td>
<td align="right"></td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">185,507,607</td>
<td align="right"></td>
<td align="right">183,359,556</td>
<td align="right"></td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,056,006,060</td>
<td align="right"></td>
<td align="right">2,035,293,228</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">31,830,543,102</td>
<td align="right">16.2%</td>
<td align="right">31,641,141,093</td>
<td align="right">16.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">45,671,588,350</td>
<td align="right">19.3%</td>
<td align="right">45,438,004,394</td>
<td align="right">19.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">15,715,617,778</td>
<td align="right">8.0%</td>
<td align="right">15,642,957,235</td>
<td align="right">8.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">19,922,107,776</td>
<td align="right">8.4%</td>
<td align="right">19,842,536,562</td>
<td align="right">8.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,506,541,723</td>
<td align="right"></td>
<td align="right">3,494,001,867</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,336,498,099</td>
<td align="right"></td>
<td align="right">10,318,858,351</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,335,446,741</td>
<td align="right">46.4%</td>
<td align="right">10,317,809,107</td>
<td align="right">46.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">72,222,461,563</td>
<td align="right">30.4%</td>
<td align="right">72,117,063,369</td>
<td align="right">30.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">96,669,455</td>
<td align="right">0.4%</td>
<td align="right">96,549,530</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">12,682,408,536</td>
<td align="right"></td>
<td align="right">12,666,808,592</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,920,548,661</td>
<td align="right">53.6%</td>
<td align="right">11,906,861,255</td>
<td align="right">53.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,802,880,409</td>
<td align="right">53.0%</td>
<td align="right">11,789,331,577</td>
<td align="right">53.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">56,498,330,522</td>
<td align="right">28.7%</td>
<td align="right">56,438,994,203</td>
<td align="right">28.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,998,797</td>
<td align="right">0.1%</td>
<td align="right">20,980,148</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">92,882,591,564</td>
<td align="right">47.2%</td>
<td align="right">92,811,633,468</td>
<td align="right">47.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">99,376,590,697</td>
<td align="right">41.9%</td>
<td align="right">99,321,708,230</td>
<td align="right">42.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,378,040</td>
<td align="right">1.8%</td>
<td align="right">3,377,240</td>
<td align="right">1.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">198,600</td>
<td align="right">0.1%</td>
<td align="right">198,600</td>
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
<td align="right">279,700</td>
<td align="right">112,327,804</td>
<td align="right">7,993,490,238</td>
<td align="right">279,678</td>
<td align="right">112,187,913</td>
<td align="right">7,988,834,259</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">15,360</td>
<td align="right">10,759,680</td>
<td align="right">7,008,818,440</td>
<td align="right">15,360</td>
<td align="right">10,759,680</td>
<td align="right">7,008,818,440</td>
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
<td align="right">14,893</td>
<td align="right">0.9%</td>
<td align="right">6,823</td>
<td align="right">0.5%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">801,822</td>
<td align="right">50.2%</td>
<td align="right">676,058</td>
<td align="right">45.7%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">16,528</td>
<td align="right">1.0%</td>
<td align="right">17,956</td>
<td align="right">1.2%</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,597,381</td>
<td align="right"></td>
<td align="right">1,477,824</td>
<td align="right"></td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">10,256</td>
<td align="right">1.3%</td>
<td align="right">9,803</td>
<td align="right">1.5%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">6,955</td>
<td align="right">0.4%</td>
<td align="right">6,734</td>
<td align="right">0.5%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">1,080</td>
<td align="right">0.1%</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">3,560</td>
<td align="right">0.2%</td>
<td align="right">3,514</td>
<td align="right">0.2%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">791,999</td>
<td align="right">49.6%</td>
<td align="right">798,252</td>
<td align="right">54.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">817,133</td>
<td align="right">51.2%</td>
<td align="right">811,420</td>
<td align="right">54.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">8,459,611,299</td>
<td align="right"></td>
<td align="right">8,433,454,962</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">303,569,668,784</td>
<td align="right">3,588.5%</td>
<td align="right">303,497,296,745</td>
<td align="right">3,598.7%</td>
<td align="right">-0.0%</td>
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
<td align="right">760,492</td>
<td align="right">94.8%</td>
<td align="right">633,882</td>
<td align="right">93.8%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">801,822</td>
<td align="right"></td>
<td align="right">676,058</td>
<td align="right"></td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,762</td>
<td align="right">0.3%</td>
<td align="right">2,582</td>
<td align="right">0.4%</td>
<td align="right">-6.5%</td>
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
<td align="right">58,037</td>
<td align="right">7.2%</td>
<td align="right">58,895</td>
<td align="right">8.7%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">118,039</td>
<td align="right">14.7%</td>
<td align="right">103,939</td>
<td align="right">15.4%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">265,461</td>
<td align="right">33.1%</td>
<td align="right">218,714</td>
<td align="right">32.4%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">213,248</td>
<td align="right">26.6%</td>
<td align="right">171,500</td>
<td align="right">25.4%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">102,289</td>
<td align="right">12.8%</td>
<td align="right">81,762</td>
<td align="right">12.1%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">36,187</td>
<td align="right">4.5%</td>
<td align="right">33,570</td>
<td align="right">5.0%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">7,341</td>
<td align="right">0.9%</td>
<td align="right">6,358</td>
<td align="right">0.9%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">1,220</td>
<td align="right">0.2%</td>
<td align="right">1,320</td>
<td align="right">0.2%</td>
<td align="right">8.2%</td>
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
<td align="right">36,396</td>
<td align="right">4.5%</td>
<td align="right">35,626</td>
<td align="right">5.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">91,404</td>
<td align="right">11.4%</td>
<td align="right">80,590</td>
<td align="right">11.9%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">138,316</td>
<td align="right">17.3%</td>
<td align="right">130,319</td>
<td align="right">19.3%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">291,994</td>
<td align="right">36.4%</td>
<td align="right">229,819</td>
<td align="right">34.0%</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">139,969</td>
<td align="right">17.5%</td>
<td align="right">108,123</td>
<td align="right">16.0%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">48,059</td>
<td align="right">6.0%</td>
<td align="right">37,260</td>
<td align="right">5.5%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">11,813</td>
<td align="right">1.5%</td>
<td align="right">9,868</td>
<td align="right">1.5%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,541</td>
<td align="right">0.3%</td>
<td align="right">2,277</td>
<td align="right">0.3%</td>
<td align="right">-10.4%</td>
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
<td align="left">_LOAD_GLOBAL</td>
<td align="right">497,556</td>
<td align="right">332,113</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">3,271,998</td>
<td align="right">2,506,925</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">2,245</td>
<td align="right">2,720</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">25,303</td>
<td align="right">21,383</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">128,661,892</td>
<td align="right">144,395,921</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">13,784,183</td>
<td align="right">12,489,487</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">10,317,463</td>
<td align="right">9,515,075</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">279,809,785</td>
<td align="right">261,883,208</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">14,165,778</td>
<td align="right">13,477,504</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">1,182,968</td>
<td align="right">1,131,826</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">31,132,170</td>
<td align="right">32,191,444</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">5,421,403</td>
<td align="right">5,245,883</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">1,642,171</td>
<td align="right">1,591,079</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">156,124,077</td>
<td align="right">160,926,663</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,663,367</td>
<td align="right">9,398,598</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">117,678,998</td>
<td align="right">114,613,682</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">325,648,352</td>
<td align="right">317,636,190</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">29,334,819</td>
<td align="right">29,906,927</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">496,558,003</td>
<td align="right">487,615,708</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">57,530,758</td>
<td align="right">56,588,038</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">26,049,243</td>
<td align="right">25,669,089</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">7,294,197</td>
<td align="right">7,197,820</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,109,075</td>
<td align="right">53,404,486</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,105,254</td>
<td align="right">53,401,066</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">26,799,446</td>
<td align="right">26,461,547</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">123,480,496</td>
<td align="right">121,999,918</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">8,974,178</td>
<td align="right">8,872,992</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">8,977,758</td>
<td align="right">8,876,572</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,870,680,584</td>
<td align="right">2,902,918,889</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,056,574</td>
<td align="right">10,168,696</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">36,623</td>
<td align="right">37,023</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,052,741</td>
<td align="right">1,042,325</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,898,383</td>
<td align="right">1,879,905</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">89,721,264</td>
<td align="right">88,848,830</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">108,849,902</td>
<td align="right">107,791,904</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">4,186,810</td>
<td align="right">4,148,866</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,241,553,426</td>
<td align="right">1,252,665,067</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,290,312</td>
<td align="right">1,278,886</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">578,552,863</td>
<td align="right">583,481,100</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">282,865,910</td>
<td align="right">280,559,866</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">106,016,373</td>
<td align="right">105,201,703</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,907,457,728</td>
<td align="right">1,919,614,633</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">113,925,275</td>
<td align="right">113,253,458</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,004,622,740</td>
<td align="right">998,907,530</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">183,454,833</td>
<td align="right">182,595,653</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,271,537,135</td>
<td align="right">1,277,242,690</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">431,323,240</td>
<td align="right">429,465,396</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">4,744,034</td>
<td align="right">4,724,000</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">32,266,256</td>
<td align="right">32,402,355</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">370,141,874</td>
<td align="right">371,689,312</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">55,542,403</td>
<td align="right">55,770,694</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">7,540,522,066</td>
<td align="right">7,510,791,108</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">704,156,871</td>
<td align="right">701,384,099</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">379,289,819</td>
<td align="right">380,773,489</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">591,283,572</td>
<td align="right">588,979,248</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">99,804,307</td>
<td align="right">100,192,220</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">651,603,187</td>
<td align="right">654,117,017</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">857,222,406</td>
<td align="right">860,496,912</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">101,022,367</td>
<td align="right">101,404,160</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">125,207,694</td>
<td align="right">125,676,367</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">884,685,065</td>
<td align="right">887,965,485</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,082,751,058</td>
<td align="right">1,078,859,644</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">27,300,859</td>
<td align="right">27,209,625</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">6,529,404</td>
<td align="right">6,508,220</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">379,647,043</td>
<td align="right">378,418,070</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">26,380,779</td>
<td align="right">26,297,480</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">8,459,611,299</td>
<td align="right">8,433,454,962</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,749,811</td>
<td align="right">1,744,412</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,740,918</td>
<td align="right">8,714,710</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,970,276,144</td>
<td align="right">1,964,371,514</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">66,047,720</td>
<td align="right">65,849,820</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">122,644,937</td>
<td align="right">123,011,848</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">50,845,413</td>
<td align="right">50,991,060</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,484,444,686</td>
<td align="right">4,497,225,507</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,376,623,512</td>
<td align="right">2,370,242,363</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">658,387,557</td>
<td align="right">656,628,069</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,061,862,193</td>
<td align="right">2,067,008,930</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">191,630,421</td>
<td align="right">192,086,570</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">2,455,212</td>
<td align="right">2,449,458</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,345,093,689</td>
<td align="right">2,349,961,919</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,748,220</td>
<td align="right">4,738,460</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">837,367</td>
<td align="right">835,646</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,825,559,674</td>
<td align="right">4,835,351,183</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">120,725,535</td>
<td align="right">120,966,835</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">976,052,010</td>
<td align="right">974,106,176</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,164,505,323</td>
<td align="right">6,152,376,644</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">113,081,595</td>
<td align="right">112,861,339</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">2,849,902</td>
<td align="right">2,844,502</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">38,655,497</td>
<td align="right">38,722,159</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,593,560,506</td>
<td align="right">1,590,862,803</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">539,620</td>
<td align="right">538,720</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">656,389,507</td>
<td align="right">655,296,070</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">657,747,287</td>
<td align="right">656,653,850</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,852,878,237</td>
<td align="right">6,864,131,494</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,666,061,417</td>
<td align="right">1,663,332,272</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">125,268,748</td>
<td align="right">125,069,640</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">298,049,718</td>
<td align="right">297,596,130</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,673,749,112</td>
<td align="right">1,671,453,785</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,636,388,398</td>
<td align="right">3,631,427,047</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">61,015,752</td>
<td align="right">61,098,822</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,103,515,138</td>
<td align="right">1,104,983,169</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">1,028,144,977</td>
<td align="right">1,026,820,644</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">10,041,822,889</td>
<td align="right">10,029,038,985</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">194,454,710</td>
<td align="right">194,700,277</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,618,608,339</td>
<td align="right">3,614,100,881</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">615,667,036</td>
<td align="right">614,923,204</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">154,509,672</td>
<td align="right">154,324,051</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,555,985,597</td>
<td align="right">1,554,219,528</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,563,014,544</td>
<td align="right">3,559,067,542</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">434,335,100</td>
<td align="right">433,866,536</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">38,702,704</td>
<td align="right">38,662,032</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">38,702,704</td>
<td align="right">38,662,032</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,578,199,001</td>
<td align="right">3,574,798,398</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">133,437,325</td>
<td align="right">133,316,471</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">133,437,325</td>
<td align="right">133,316,471</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,612,056</td>
<td align="right">5,607,060</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,058,554,660</td>
<td align="right">1,057,613,759</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,197,911,260</td>
<td align="right">2,196,006,427</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,610,040</td>
<td align="right">5,605,220</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">163,612,096</td>
<td align="right">163,751,882</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,475,773,222</td>
<td align="right">1,477,021,424</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,286,513,463</td>
<td align="right">5,290,982,253</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,926,284,347</td>
<td align="right">2,923,906,399</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">864,321,277</td>
<td align="right">865,021,987</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">585,429,570</td>
<td align="right">585,901,203</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,198,319,036</td>
<td align="right">3,200,513,603</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">2,430,231</td>
<td align="right">2,428,618</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">808,983,725</td>
<td align="right">808,457,837</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">398,157,140</td>
<td align="right">398,409,214</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,768,120</td>
<td align="right">48,739,380</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,768,120</td>
<td align="right">48,739,380</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,269,655,122</td>
<td align="right">2,268,342,977</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">669,489,307</td>
<td align="right">669,103,600</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">160,897,056</td>
<td align="right">160,805,806</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">555,634,455</td>
<td align="right">555,321,128</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">158,141,752</td>
<td align="right">158,055,800</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">11,330,291,883</td>
<td align="right">11,336,373,851</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,709,004,564</td>
<td align="right">1,709,920,886</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">610,518,410</td>
<td align="right">610,192,415</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">964,497,447</td>
<td align="right">963,988,476</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">237,223,766</td>
<td align="right">237,346,531</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">50,201,295</td>
<td align="right">50,175,900</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,118,434,827</td>
<td align="right">13,111,868,825</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">47,033,875</td>
<td align="right">47,011,519</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">47,033,875</td>
<td align="right">47,011,519</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">8,064,930,351</td>
<td align="right">8,061,165,245</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,658,868,206</td>
<td align="right">5,656,232,786</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">375,022,984</td>
<td align="right">375,196,038</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">3,147,826,934</td>
<td align="right">3,149,274,156</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,392,302,984</td>
<td align="right">2,391,317,535</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">582,300,844</td>
<td align="right">582,064,866</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,219,278,619</td>
<td align="right">2,218,423,911</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">225,081,272</td>
<td align="right">224,996,271</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">772,466,613</td>
<td align="right">772,179,524</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,586,931,016</td>
<td align="right">2,587,867,989</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,536,673,182</td>
<td align="right">3,535,404,003</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">20,293,122,201</td>
<td align="right">20,285,852,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">24,350,205,565</td>
<td align="right">24,341,655,119</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,331,069,691</td>
<td align="right">1,330,602,348</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">63,834,041</td>
<td align="right">63,855,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">94,159,548</td>
<td align="right">94,127,750</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">83,915,772</td>
<td align="right">83,888,216</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">374,324,563</td>
<td align="right">374,206,391</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,523,966,854</td>
<td align="right">1,523,487,282</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">377,452,022</td>
<td align="right">377,338,026</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,430,013,228</td>
<td align="right">1,430,431,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">869,596,605</td>
<td align="right">869,843,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">109,098,839</td>
<td align="right">109,068,796</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">94,288,343</td>
<td align="right">94,263,102</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">719,464,987</td>
<td align="right">719,645,061</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">6,827,166,949</td>
<td align="right">6,828,807,596</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,771,930,514</td>
<td align="right">10,774,489,177</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,625,682,056</td>
<td align="right">3,624,827,894</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">40,638,083</td>
<td align="right">40,628,638</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,656,783</td>
<td align="right">32,649,534</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">35,519,527</td>
<td align="right">35,511,790</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">672,864,843</td>
<td align="right">672,728,858</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">893,741,996</td>
<td align="right">893,572,330</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">532,615,699</td>
<td align="right">532,517,379</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">1,265,921</td>
<td align="right">1,265,700</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">782,620,210</td>
<td align="right">782,756,141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,358,437,268</td>
<td align="right">2,358,040,580</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,931,833,313</td>
<td align="right">3,932,494,333</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">92,133,912</td>
<td align="right">92,119,561</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,975,992</td>
<td align="right">80,988,401</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,973,124,373</td>
<td align="right">1,972,846,204</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,318,418,367</td>
<td align="right">2,318,094,800</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">444,126,265</td>
<td align="right">444,180,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">186,371,921</td>
<td align="right">186,349,409</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">166,577,547</td>
<td align="right">166,557,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">158,616,477</td>
<td align="right">158,597,665</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">2,451,692,545</td>
<td align="right">2,451,406,308</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,546,962,253</td>
<td align="right">2,547,232,502</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">62,980,880</td>
<td align="right">62,974,280</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">66,279,054</td>
<td align="right">66,285,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,015,981,549</td>
<td align="right">3,016,282,399</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">38,593,243</td>
<td align="right">38,596,414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,384,418,286</td>
<td align="right">1,384,529,614</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">615,491,470</td>
<td align="right">615,444,415</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">628,415,183</td>
<td align="right">628,455,559</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,815,283,162</td>
<td align="right">1,815,167,615</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,232,684,713</td>
<td align="right">7,232,224,688</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">963,080</td>
<td align="right">963,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,432,643</td>
<td align="right">32,430,929</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,851,397</td>
<td align="right">149,844,220</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">982,500,318</td>
<td align="right">982,457,644</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">814,795,586</td>
<td align="right">814,771,130</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,215,040</td>
<td align="right">350,204,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">565,346,860</td>
<td align="right">565,332,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">99,169,800</td>
<td align="right">99,167,600</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,327,719,052</td>
<td align="right">1,327,740,466</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">229,246,545</td>
<td align="right">229,243,205</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,143,717,440</td>
<td align="right">1,143,702,206</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,122,285,994</td>
<td align="right">2,122,314,252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">635,393,826</td>
<td align="right">635,387,857</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">514,958,311</td>
<td align="right">514,954,647</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,682,827,712</td>
<td align="right">1,682,821,386</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">99,562,545</td>
<td align="right">99,562,292</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">1,278,786</td>
<td align="right">1,278,789</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,780</td>
<td align="right">125,514,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,846,880</td>
<td align="right">1,846,880</td>
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
<td align="right">598,320</td>
<td align="right">598,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">38,100</td>
<td align="right">38,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">440</td>
<td align="right">440</td>
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
<td align="left">CALL_KW</td>
<td align="right">120</td>
<td align="right">100</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">2,785</td>
<td align="right">2,380</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">37,006</td>
<td align="right">39,845</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">32,824</td>
<td align="right">31,772</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">41,886</td>
<td align="right">41,990</td>
<td align="right">0.2%</td>
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
<td align="right">1,260</td>
<td align="right">1,240</td>
<td align="right">-1.6%</td>
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
<td align="right">1,240</td>
<td align="right">-1.6%</td>
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
<td align="right">1,781</td>
<td align="right">1,781</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
