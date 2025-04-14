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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,747,993,332</td>
<td align="right">5,196,627</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,724,898</td>
<td align="right">1,232,478</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,369,166</td>
<td align="right">2,279,613</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">6,000,000</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,461,030,851</td>
<td align="right">194,341,831</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,404,089,333</td>
<td align="right">203,647,624</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,586,181,727</td>
<td align="right">234,168,150</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">701,025,358</td>
<td align="right">103,884,526</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,755,351,205</td>
<td align="right">270,881,832</td>
<td align="right">-84.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,275,288,385</td>
<td align="right">201,299,733</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,719,250,315</td>
<td align="right">433,518,049</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,234,817,788</td>
<td align="right">367,152,247</td>
<td align="right">-83.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">566,124,020</td>
<td align="right">95,841,373</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,484,111,072</td>
<td align="right">606,750,847</td>
<td align="right">-82.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,134,999,098</td>
<td align="right">373,576,496</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">511,629,456</td>
<td align="right">93,553,132</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">89,987,521</td>
<td align="right">19,489,212</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,251,953,919</td>
<td align="right">272,994,690</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,817,490</td>
<td align="right">34,636,020</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,865,327</td>
<td align="right">76,831,003</td>
<td align="right">-77.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">666,490,743</td>
<td align="right">156,784,721</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">223,651,897</td>
<td align="right">55,741,185</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,657,375,068</td>
<td align="right">431,886,684</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">194,822,355</td>
<td align="right">53,561,635</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,290,465,636</td>
<td align="right">2,007,435,566</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">630,901,186</td>
<td align="right">175,240,748</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,652,729</td>
<td align="right">146,141,792</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">369,735,548</td>
<td align="right">107,569,832</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">637,159,248</td>
<td align="right">188,494,541</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,453,775</td>
<td align="right">17,254,523</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">379,223,133</td>
<td align="right">118,886,996</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,197,514,667</td>
<td align="right">693,184,711</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,737,317,305</td>
<td align="right">869,096,213</td>
<td align="right">-68.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,161,872</td>
<td align="right">36,587,678</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">538,273,875</td>
<td align="right">171,368,909</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">258,998,413</td>
<td align="right">84,884,902</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,116,152,788</td>
<td align="right">366,475,370</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,627,162</td>
<td align="right">184,041,333</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,533,863,250</td>
<td align="right">857,514,504</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,758,965,298</td>
<td align="right">1,963,451,074</td>
<td align="right">-65.9%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,387,204</td>
<td align="right">54,908,693</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">357,025,864</td>
<td align="right">123,882,989</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">121,931,925</td>
<td align="right">42,589,947</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">61,979,584</td>
<td align="right">21,988,803</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,043,135,954</td>
<td align="right">3,929,991,645</td>
<td align="right">-64.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,533,869,191</td>
<td align="right">909,787,537</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,438,232,217</td>
<td align="right">4,890,430,515</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,955,602</td>
<td align="right">27,290,292</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,078,699,990</td>
<td align="right">393,441,682</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,334,941,989</td>
<td align="right">495,258,574</td>
<td align="right">-62.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,678,080,883</td>
<td align="right">3,968,643,510</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">882,435,470</td>
<td align="right">333,378,158</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">152,579,847</td>
<td align="right">62.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,806,550,341</td>
<td align="right">1,091,984,627</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">436,917,183</td>
<td align="right">170,094,841</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">65,890,711</td>
<td align="right">25,838,098</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">78,104,351</td>
<td align="right">31,041,012</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,079,361,475</td>
<td align="right">843,721,471</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">2,597,140</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">23,453,072</td>
<td align="right">10,054,183</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">100,761,020</td>
<td align="right">43,485,238</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">404,598,794</td>
<td align="right">177,721,273</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">814,397,892</td>
<td align="right">358,185,121</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,436,108</td>
<td align="right">468,522,117</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,839,290</td>
<td align="right">3,565,851</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">786,511,969</td>
<td align="right">363,189,992</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">114,991,846</td>
<td align="right">53,162,415</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">37,225,275,012</td>
<td align="right">17,421,225,033</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,020,999</td>
<td align="right">129,275,918</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,700,210</td>
<td align="right">47,267,989</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">93,450,142</td>
<td align="right">45,158,022</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,229,447,840</td>
<td align="right">3,557,945,311</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,257,459,973</td>
<td align="right">623,182,645</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,207,322,162</td>
<td align="right">620,742,220</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">519,107,847</td>
<td align="right">267,013,164</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">314,939,074</td>
<td align="right">165,111,138</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">263,723,450</td>
<td align="right">138,280,223</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">72,300,403</td>
<td align="right">38,153,165</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">359,380,081</td>
<td align="right">199,749,709</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">201,832,202</td>
<td align="right">112,478,326</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,851,644,272</td>
<td align="right">2,157,140,775</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">291,208,441</td>
<td align="right">163,747,835</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,510,836,959</td>
<td align="right">849,887,696</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,870,645</td>
<td align="right">88,137,679</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,032,968,258</td>
<td align="right">586,436,808</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">59,525,631</td>
<td align="right">34,897,498</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">774,262,587</td>
<td align="right">456,681,026</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,502,723,368</td>
<td align="right">1,483,375,577</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,544,774,654</td>
<td align="right">936,785,372</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,779,248</td>
<td align="right">4,727,191</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,198,538,678</td>
<td align="right">1,946,795,172</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,186</td>
<td align="right">114,765,192</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,380,411,068</td>
<td align="right">841,665,723</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">183,121,803</td>
<td align="right">112,730,082</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,852,184,857</td>
<td align="right">3,178,296,486</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">828,324,748</td>
<td align="right">553,733,681</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">67,639,540</td>
<td align="right">45,692,699</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">388,084,251</td>
<td align="right">264,306,509</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,794,847</td>
<td align="right">119,477,696</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">168,683,862</td>
<td align="right">117,645,331</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">490,688,569</td>
<td align="right">344,049,593</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">331,132,440</td>
<td align="right">246,836,928</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,322,786,953</td>
<td align="right">2,480,878,400</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">225,147,977</td>
<td align="right">171,464,329</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">827,972,423</td>
<td align="right">646,189,344</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">493,879,067</td>
<td align="right">388,317,898</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,820,553</td>
<td align="right">1,431,548</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">356,629,374</td>
<td align="right">281,351,689</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,171,691,178</td>
<td align="right">2,510,732,094</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,275,789,410</td>
<td align="right">4,991,332,470</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">350,320,507</td>
<td align="right">285,128,938</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">68,712,474</td>
<td align="right">57,897,554</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">292,922,018</td>
<td align="right">249,295,962</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">415,728,450</td>
<td align="right">354,044,427</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,746,303</td>
<td align="right">4,070,789</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">72,567,082</td>
<td align="right">62,326,413</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">95,105,697</td>
<td align="right">81,871,128</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">946,775,763</td>
<td align="right">815,727,344</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,393,832,583</td>
<td align="right">4,653,650,012</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,900,672</td>
<td align="right">10,301,717</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">305,934,767</td>
<td align="right">265,298,248</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">568,031,420</td>
<td align="right">499,739,543</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">985,548,549</td>
<td align="right">872,690,659</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">63,469,178</td>
<td align="right">57,066,699</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">63,490,861</td>
<td align="right">57,857,957</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,793,246</td>
<td align="right">3,486,046</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">137,606,008</td>
<td align="right">127,924,309</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">77,223,689</td>
<td align="right">72,183,982</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,164,022</td>
<td align="right">5,803,530</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,981,291</td>
<td align="right">20,026,139</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,312,261</td>
<td align="right">20,357,109</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,312,282</td>
<td align="right">20,357,130</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,175,222</td>
<td align="right">8,826,332</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">83,615,952</td>
<td align="right">81,081,711</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,934,876</td>
<td align="right">68,838,586</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,865</td>
<td align="right">123,859,632</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">73,266,078</td>
<td align="right">71,282,578</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">14,184,270</td>
<td align="right">13,839,810</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,646</td>
<td align="right">2,706</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,113,857</td>
<td align="right">3,048,123</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,777,120</td>
<td align="right">1,748,448</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,120,608</td>
<td align="right">8,979,326</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,209,057</td>
<td align="right">66,375,183</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">15,091,452</td>
<td align="right">14,947,933</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">408,527</td>
<td align="right">410,617</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,357</td>
<td align="right">5,341</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,266,096</td>
<td align="right">155,899,594</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">245,331,222</td>
<td align="right">244,786,400</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">34,251</td>
<td align="right">34,201</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">244,013,530</td>
<td align="right">243,751,177</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">246,070,813</td>
<td align="right">245,807,054</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,622,449,452</td>
<td align="right">1,620,994,817</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,228,370</td>
<td align="right">180,068,242</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,612,252</td>
<td align="right">418,390,997</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,113,764,783</td>
<td align="right">1,113,201,166</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">135,513</td>
<td align="right">135,464</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">121,292</td>
<td align="right">121,328</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">752,989</td>
<td align="right">752,844</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,417,306</td>
<td align="right">131,401,044</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,762,177</td>
<td align="right">14,763,555</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,917,279</td>
<td align="right">100,917,190</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,688</td>
<td align="right">35,549,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,621,564</td>
<td align="right">591,621,576</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,700</td>
<td align="right">302,246,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,161</td>
<td align="right">128,850,161</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,673</td>
<td align="right">41,964,673</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">9,743,070</td>
<td align="right">9,743,070</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,976,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,644,367</td>
<td align="right">1,644,367</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">117,444</td>
<td align="right">117,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,609</td>
<td align="right">98,609</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,496</td>
<td align="right">84,496</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,511</td>
<td align="right">69,511</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,204</td>
<td align="right">57,204</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,548</td>
<td align="right">56,548</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">13,935</td>
<td align="right">13,935</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,265</td>
<td align="right">5,265</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,889</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,613</td>
<td align="right">3,613</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
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
<td align="right">153</td>
<td align="right">153</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">982,843,701</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">849,443,433</td>
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
<td align="right">2,805,607,571</td>
<td align="right">15.0%</td>
<td align="right">1,091,600,138</td>
<td align="right">6.4%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">59,056,812</td>
<td align="right">0.3%</td>
<td align="right">51,913,124</td>
<td align="right">0.3%</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,836,672,160</td>
<td align="right">84.7%</td>
<td align="right">15,818,226,541</td>
<td align="right">93.3%</td>
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
<td align="right">925,709</td>
<td align="right">45.0%</td>
<td align="right">366,432</td>
<td align="right">26.9%</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,131,103</td>
<td align="right">55.0%</td>
<td align="right">997,330</td>
<td align="right">73.1%</td>
<td align="right">-11.8%</td>
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
<td align="left">subscr list slice</td>
<td align="right">115,276</td>
<td align="right">12.5%</td>
<td align="right">6,366</td>
<td align="right">1.7%</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">9.2%</td>
<td align="right">16,343</td>
<td align="right">4.5%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">2,767</td>
<td align="right">0.8%</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,220</td>
<td align="right">8.0%</td>
<td align="right">18,458</td>
<td align="right">5.0%</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">0.9%</td>
<td align="right">2,343</td>
<td align="right">0.6%</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.3%</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,512</td>
<td align="right">2.5%</td>
<td align="right">8,297</td>
<td align="right">2.3%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">350,765</td>
<td align="right">37.9%</td>
<td align="right">131,990</td>
<td align="right">36.0%</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,256</td>
<td align="right">0.1%</td>
<td align="right">488</td>
<td align="right">0.1%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">399</td>
<td align="right">0.0%</td>
<td align="right">189</td>
<td align="right">0.1%</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,857</td>
<td align="right">4.7%</td>
<td align="right">22,154</td>
<td align="right">6.0%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,963</td>
<td align="right">3.7%</td>
<td align="right">19,873</td>
<td align="right">5.4%</td>
<td align="right">-41.5%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">2.1%</td>
<td align="right">11,552</td>
<td align="right">3.2%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,619</td>
<td align="right">4.0%</td>
<td align="right">23,117</td>
<td align="right">6.3%</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,514</td>
<td align="right">0.9%</td>
<td align="right">6,194</td>
<td align="right">1.7%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">7,224</td>
<td align="right">0.8%</td>
<td align="right">5,752</td>
<td align="right">1.6%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">43,427</td>
<td align="right">4.7%</td>
<td align="right">36,635</td>
<td align="right">10.0%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">46,933</td>
<td align="right">5.1%</td>
<td align="right">40,824</td>
<td align="right">11.1%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,036</td>
<td align="right">0.2%</td>
<td align="right">1,996</td>
<td align="right">0.5%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">637</td>
<td align="right">0.1%</td>
<td align="right">631</td>
<td align="right">0.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,154</td>
<td align="right">0.3%</td>
<td align="right">3,174</td>
<td align="right">0.9%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">1,971</td>
<td align="right">0.2%</td>
<td align="right">1,968</td>
<td align="right">0.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,342</td>
<td align="right">0.3%</td>
<td align="right">2,340</td>
<td align="right">0.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.1%</td>
<td align="right">1,384</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">597</td>
<td align="right">0.1%</td>
<td align="right">597</td>
<td align="right">0.2%</td>
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
<tr>
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">545,627,162</td>
<td align="right">100.0%</td>
<td align="right">184,041,333</td>
<td align="right">100.0%</td>
<td align="right">-66.3%</td>
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
<td align="right">178,751,185</td>
<td align="right">1.6%</td>
<td align="right">147,726,050</td>
<td align="right">1.3%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">175,611,183</td>
<td align="right">1.6%</td>
<td align="right">145,171,398</td>
<td align="right">1.3%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,043,166,650</td>
<td align="right">98.4%</td>
<td align="right">11,038,103,020</td>
<td align="right">98.7%</td>
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
<td align="right">3,548,083</td>
<td align="right">100.0%</td>
<td align="right">2,964,823</td>
<td align="right">100.0%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">446</td>
<td align="right">0.0%</td>
<td align="right">446</td>
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
<td align="right">168.6%</td>
<td align="right">752</td>
<td align="right">168.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right">267</td>
<td align="right">59.9%</td>
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
<td align="right">684,522</td>
<td align="right">97.1%</td>
<td align="right">684,522</td>
<td align="right">97.1%</td>
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
<td align="right">583,803</td>
<td align="right">82.8%</td>
<td align="right">583,803</td>
<td align="right">82.8%</td>
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
<td align="right">20,453</td>
<td align="right">99.4%</td>
<td align="right">20,489</td>
<td align="right">99.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">511,398,729</td>
<td align="right">10.2%</td>
<td align="right">93,434,270</td>
<td align="right">2.0%</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,466,367</td>
<td align="right">0.0%</td>
<td align="right">1,154,223</td>
<td align="right">0.0%</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,510,567,851</td>
<td align="right">89.8%</td>
<td align="right">4,495,202,544</td>
<td align="right">97.9%</td>
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
<td align="right">212,527</td>
<td align="right">82.4%</td>
<td align="right">100,404</td>
<td align="right">71.5%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">45,543</td>
<td align="right">17.6%</td>
<td align="right">40,037</td>
<td align="right">28.5%</td>
<td align="right">-12.1%</td>
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
<td align="right">90,864</td>
<td align="right">42.8%</td>
<td align="right">4,547</td>
<td align="right">4.5%</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,830</td>
<td align="right">3.2%</td>
<td align="right">372</td>
<td align="right">0.4%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">10,452</td>
<td align="right">4.9%</td>
<td align="right">5,958</td>
<td align="right">5.9%</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">15,199</td>
<td align="right">7.2%</td>
<td align="right">9,243</td>
<td align="right">9.2%</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,678</td>
<td align="right">21.5%</td>
<td align="right">37,123</td>
<td align="right">37.0%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.2%</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,367</td>
<td align="right">0.6%</td>
<td align="right">1,321</td>
<td align="right">1.3%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,021</td>
<td align="right">1.0%</td>
<td align="right">2,003</td>
<td align="right">2.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,373</td>
<td align="right">11.0%</td>
<td align="right">23,175</td>
<td align="right">23.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,774</td>
<td align="right">3.7%</td>
<td align="right">7,715</td>
<td align="right">7.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">3.6%</td>
<td align="right">7,648</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">965</td>
<td align="right">0.5%</td>
<td align="right">965</td>
<td align="right">1.0%</td>
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
<td align="right">155,809,161</td>
<td align="right">6.6%</td>
<td align="right">88,092,365</td>
<td align="right">3.9%</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,190,872,429</td>
<td align="right">93.3%</td>
<td align="right">2,186,577,247</td>
<td align="right">96.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,395,959</td>
<td align="right">0.1%</td>
<td align="right">1,395,959</td>
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
<td align="right">59,365</td>
<td align="right">67.6%</td>
<td align="right">42,995</td>
<td align="right">60.0%</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,462</td>
<td align="right">32.4%</td>
<td align="right">28,662</td>
<td align="right">40.0%</td>
<td align="right">0.7%</td>
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
<td align="right">21,374</td>
<td align="right">36.0%</td>
<td align="right">9,767</td>
<td align="right">22.7%</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,642</td>
<td align="right">24.7%</td>
<td align="right">12,031</td>
<td align="right">28.0%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,700</td>
<td align="right">19.7%</td>
<td align="right">10,048</td>
<td align="right">23.4%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,649</td>
<td align="right">19.6%</td>
<td align="right">11,149</td>
<td align="right">25.9%</td>
<td align="right">-4.3%</td>
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
<td align="right">1,460,598,766</td>
<td align="right">28.8%</td>
<td align="right">194,225,823</td>
<td align="right">13.1%</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,448,022,644</td>
<td align="right">68.0%</td>
<td align="right">1,222,616,369</td>
<td align="right">82.7%</td>
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
<td align="right">163,998,306</td>
<td align="right">3.2%</td>
<td align="right">61,964,399</td>
<td align="right">4.2%</td>
<td align="right">-62.2%</td>
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
<td align="right">426,901</td>
<td align="right">12.1%</td>
<td align="right">110,846</td>
<td align="right">8.6%</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,099,313</td>
<td align="right">87.9%</td>
<td align="right">1,174,141</td>
<td align="right">91.4%</td>
<td align="right">-62.1%</td>
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
<td align="left">zip</td>
<td align="right">172,123</td>
<td align="right">40.3%</td>
<td align="right">4,500</td>
<td align="right">4.1%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,793</td>
<td align="right">19.6%</td>
<td align="right">11,085</td>
<td align="right">10.0%</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,944</td>
<td align="right">8.2%</td>
<td align="right">6,619</td>
<td align="right">6.0%</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,153</td>
<td align="right">0.7%</td>
<td align="right">1,132</td>
<td align="right">1.0%</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,250</td>
<td align="right">4.3%</td>
<td align="right">7,038</td>
<td align="right">6.3%</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,815</td>
<td align="right">2.5%</td>
<td align="right">4,340</td>
<td align="right">3.9%</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,147</td>
<td align="right">0.7%</td>
<td align="right">1,673</td>
<td align="right">1.5%</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,535</td>
<td align="right">4.6%</td>
<td align="right">12,995</td>
<td align="right">11.7%</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">67,975</td>
<td align="right">15.9%</td>
<td align="right">50,424</td>
<td align="right">45.5%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,583</td>
<td align="right">1.1%</td>
<td align="right">3,813</td>
<td align="right">3.4%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,932</td>
<td align="right">1.6%</td>
<td align="right">6,512</td>
<td align="right">5.9%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">254</td>
<td align="right">0.1%</td>
<td align="right">254</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">826,478,379</td>
<td align="right">6.0%</td>
<td align="right">551,972,928</td>
<td align="right">4.2%</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">865,862,626</td>
<td align="right">6.3%</td>
<td align="right">609,733,785</td>
<td align="right">4.6%</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,061,814,557</td>
<td align="right">87.7%</td>
<td align="right">12,090,458,677</td>
<td align="right">91.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,263,439</td>
<td align="right">0.0%</td>
<td align="right">1,263,439</td>
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
<td align="right">16,422,887</td>
<td align="right">96.7%</td>
<td align="right">11,594,486</td>
<td align="right">96.0%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">561,069</td>
<td align="right">3.3%</td>
<td align="right">489,137</td>
<td align="right">4.0%</td>
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
<td align="left">method</td>
<td align="right">77,415</td>
<td align="right">13.8%</td>
<td align="right">39,366</td>
<td align="right">8.0%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,201</td>
<td align="right">0.2%</td>
<td align="right">841</td>
<td align="right">0.2%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">58,134</td>
<td align="right">10.4%</td>
<td align="right">42,829</td>
<td align="right">8.8%</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,106</td>
<td align="right">1.1%</td>
<td align="right">4,908</td>
<td align="right">1.0%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,737</td>
<td align="right">0.5%</td>
<td align="right">2,377</td>
<td align="right">0.5%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,215</td>
<td align="right">1.6%</td>
<td align="right">8,025</td>
<td align="right">1.6%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">66,530</td>
<td align="right">11.9%</td>
<td align="right">61,767</td>
<td align="right">12.6%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">25,246</td>
<td align="right">4.5%</td>
<td align="right">24,205</td>
<td align="right">4.9%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,684</td>
<td align="right">3.0%</td>
<td align="right">16,291</td>
<td align="right">3.3%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,802</td>
<td align="right">0.3%</td>
<td align="right">1,775</td>
<td align="right">0.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,020</td>
<td align="right">0.9%</td>
<td align="right">5,018</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.1%</td>
<td align="right">6,405</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,493</td>
<td align="right">0.3%</td>
<td align="right">1,493</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.0%</td>
<td align="right">235</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">163</td>
<td align="right">0.0%</td>
<td align="right">163</td>
<td align="right">0.0%</td>
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
<td align="right">9,081,699,011</td>
<td align="right">99.8%</td>
<td align="right">4,565,775,530</td>
<td align="right">99.7%</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,240</td>
<td align="right">0.0%</td>
<td align="right">52,673</td>
<td align="right">0.0%</td>
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
<td align="right">14,623,633</td>
<td align="right">0.2%</td>
<td align="right">14,623,573</td>
<td align="right">0.3%</td>
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
<td align="right">1,502</td>
<td align="right">0.0%</td>
<td align="right">1,502</td>
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
<td align="right">139,322</td>
<td align="right">100.0%</td>
<td align="right">140,760</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
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
<td align="right">66,583,035</td>
<td align="right">100.0%</td>
<td align="right">65,818,390</td>
<td align="right">100.0%</td>
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
<td align="right">252</td>
<td align="right">0.0%</td>
<td align="right">252</td>
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
<td align="right">2,394</td>
<td align="right">100.0%</td>
<td align="right">2,454</td>
<td align="right">100.0%</td>
<td align="right">2.5%</td>
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
<td align="right">591,606,853</td>
<td align="right">82.1%</td>
<td align="right">591,606,865</td>
<td align="right">82.1%</td>
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
<td align="right">128,815,363</td>
<td align="right">17.9%</td>
<td align="right">128,815,363</td>
<td align="right">17.9%</td>
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
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">34,411</td>
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
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">3,260</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">77,130,132</td>
<td align="right">3.8%</td>
<td align="right">72,090,188</td>
<td align="right">3.6%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">113,754,138</td>
<td align="right">5.6%</td>
<td align="right">106,426,163</td>
<td align="right">5.3%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,827,547,015</td>
<td align="right">90.5%</td>
<td align="right">1,823,688,061</td>
<td align="right">91.1%</td>
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
<td align="left">Success</td>
<td align="right">2,186,216</td>
<td align="right">97.6%</td>
<td align="right">2,049,393</td>
<td align="right">97.5%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">52,739</td>
<td align="right">2.4%</td>
<td align="right">51,575</td>
<td align="right">2.5%</td>
<td align="right">-2.2%</td>
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
<td align="right">6,007</td>
<td align="right">11.4%</td>
<td align="right">4,898</td>
<td align="right">9.5%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">271,391</td>
<td align="right">514.6%</td>
<td align="right">262,933</td>
<td align="right">509.8%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">1,619</td>
<td align="right">3.1%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,319</td>
<td align="right">10.1%</td>
<td align="right">5,315</td>
<td align="right">10.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">46.4%</td>
<td align="right">24,476</td>
<td align="right">47.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.5%</td>
<td align="right">7,666</td>
<td align="right">14.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,346</td>
<td align="right">6.3%</td>
<td align="right">3,346</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">814</td>
<td align="right">1.5%</td>
<td align="right">814</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">365</td>
<td align="right">0.7%</td>
<td align="right">365</td>
<td align="right">0.7%</td>
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
<td align="right">112,724,898</td>
<td align="right">100.0%</td>
<td align="right">1,232,478</td>
<td align="right">100.0%</td>
<td align="right">-98.9%</td>
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
<td align="right">700,841,016</td>
<td align="right">43.2%</td>
<td align="right">103,845,775</td>
<td align="right">10.1%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">923,147,664</td>
<td align="right">56.8%</td>
<td align="right">920,391,197</td>
<td align="right">89.9%</td>
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
<td align="right">182,260</td>
<td align="right">98.8%</td>
<td align="right">36,548</td>
<td align="right">94.2%</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,122</td>
<td align="right">1.2%</td>
<td align="right">2,243</td>
<td align="right">5.8%</td>
<td align="right">5.7%</td>
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
<td align="right">86,613</td>
<td align="right">47.5%</td>
<td align="right">341</td>
<td align="right">0.9%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,309</td>
<td align="right">2.9%</td>
<td align="right">176</td>
<td align="right">0.5%</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,343</td>
<td align="right">10.6%</td>
<td align="right">3,483</td>
<td align="right">9.5%</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.8%</td>
<td align="right">10,484</td>
<td align="right">28.7%</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,324</td>
<td align="right">9.5%</td>
<td align="right">17,324</td>
<td align="right">47.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,991</td>
<td align="right">1.6%</td>
<td align="right">2,991</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">0.9%</td>
<td align="right">1,681</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">68</td>
<td align="right">0.2%</td>
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
<td align="right">263,041,241</td>
<td align="right">5.2%</td>
<td align="right">137,722,333</td>
<td align="right">3.0%</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">110,032,189</td>
<td align="right">2.2%</td>
<td align="right">63,558,240</td>
<td align="right">1.4%</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,705,616,991</td>
<td align="right">92.6%</td>
<td align="right">4,366,428,397</td>
<td align="right">95.6%</td>
<td align="right">-7.2%</td>
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
<td align="right">2,125,085</td>
<td align="right">77.1%</td>
<td align="right">1,248,713</td>
<td align="right">71.1%</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">631,547</td>
<td align="right">22.9%</td>
<td align="right">506,736</td>
<td align="right">28.9%</td>
<td align="right">-19.8%</td>
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
<td align="right">18,878</td>
<td align="right">3.0%</td>
<td align="right">4,677</td>
<td align="right">0.9%</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">132,984</td>
<td align="right">21.1%</td>
<td align="right">33,960</td>
<td align="right">6.7%</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">20,485</td>
<td align="right">3.2%</td>
<td align="right">15,223</td>
<td align="right">3.0%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">10,016</td>
<td align="right">1.6%</td>
<td align="right">9,086</td>
<td align="right">1.8%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">77,650</td>
<td align="right">12.3%</td>
<td align="right">73,686</td>
<td align="right">14.5%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">97,681</td>
<td align="right">15.5%</td>
<td align="right">96,091</td>
<td align="right">19.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,644</td>
<td align="right">41.0%</td>
<td align="right">258,808</td>
<td align="right">51.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,323</td>
<td align="right">2.1%</td>
<td align="right">13,319</td>
<td align="right">2.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
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
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">84</td>
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
<td align="right">1,809,544</td>
<td align="right">0.1%</td>
<td align="right">1,420,647</td>
<td align="right">0.1%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,241,226,847</td>
<td align="right">99.9%</td>
<td align="right">1,240,202,066</td>
<td align="right">99.9%</td>
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
<td align="right">996</td>
<td align="right">9.0%</td>
<td align="right">868</td>
<td align="right">7.9%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,093</td>
<td align="right">91.0%</td>
<td align="right">10,113</td>
<td align="right">92.1%</td>
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
<td align="left">sequence</td>
<td align="right">762</td>
<td align="right">76.5%</td>
<td align="right">634</td>
<td align="right">73.0%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">13.7%</td>
<td align="right">136</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">9.8%</td>
<td align="right">98</td>
<td align="right">11.3%</td>
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
<td align="right">7,609,695,954</td>
<td align="right">3.6%</td>
<td align="right">2,666,953,407</td>
<td align="right">2.7%</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">86,661,798,011</td>
<td align="right">41.1%</td>
<td align="right">39,254,052,666</td>
<td align="right">40.2%</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">115,052,312,363</td>
<td align="right">54.6%</td>
<td align="right">54,575,641,812</td>
<td align="right">56.0%</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,495,101,532</td>
<td align="right">0.7%</td>
<td align="right">1,044,658,591</td>
<td align="right">1.1%</td>
<td align="right">-30.1%</td>
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
<td align="right">1,460,598,766</td>
<td align="right">18.8%</td>
<td align="right">194,225,823</td>
<td align="right">6.9%</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,841,016</td>
<td align="right">9.0%</td>
<td align="right">103,845,775</td>
<td align="right">3.7%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">511,398,729</td>
<td align="right">6.6%</td>
<td align="right">93,434,270</td>
<td align="right">3.3%</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,627,162</td>
<td align="right">7.0%</td>
<td align="right">184,041,333</td>
<td align="right">6.6%</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,805,607,571</td>
<td align="right">36.1%</td>
<td align="right">1,091,600,138</td>
<td align="right">38.9%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">263,041,241</td>
<td align="right">3.4%</td>
<td align="right">137,722,333</td>
<td align="right">4.9%</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,809,161</td>
<td align="right">2.0%</td>
<td align="right">88,092,365</td>
<td align="right">3.1%</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">826,478,379</td>
<td align="right">10.6%</td>
<td align="right">551,972,928</td>
<td align="right">19.7%</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">175,611,183</td>
<td align="right">2.3%</td>
<td align="right">145,171,398</td>
<td align="right">5.2%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,363</td>
<td align="right">1.7%</td>
<td align="right">128,815,363</td>
<td align="right">4.6%</td>
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
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,009,822</td>
<td align="right">5.5%</td>
<td align="right">30,957,018</td>
<td align="right">3.0%</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,911,089</td>
<td align="right">5.5%</td>
<td align="right">30,929,986</td>
<td align="right">3.0%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">48,567,381</td>
<td align="right">3.2%</td>
<td align="right">26,695,011</td>
<td align="right">2.6%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,399,981</td>
<td align="right">3.6%</td>
<td align="right">29,929,921</td>
<td align="right">2.9%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">368,035,000</td>
<td align="right">24.6%</td>
<td align="right">214,265,327</td>
<td align="right">20.5%</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">266,127,312</td>
<td align="right">17.8%</td>
<td align="right">175,384,349</td>
<td align="right">16.8%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,922,842</td>
<td align="right">5.5%</td>
<td align="right">54,017,960</td>
<td align="right">5.2%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,246,425</td>
<td align="right">6.3%</td>
<td align="right">87,379,559</td>
<td align="right">8.4%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">87,402,584</td>
<td align="right">5.8%</td>
<td align="right">82,734,563</td>
<td align="right">7.9%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">85,607,267</td>
<td align="right">5.7%</td>
<td align="right">82,152,584</td>
<td align="right">7.9%</td>
<td align="right">-4.0%</td>
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
<td align="right">71,196,145</td>
<td align="right">1.1%</td>
<td align="right">70,335,314</td>
<td align="right">1.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,093,913,274</td>
<td align="right">75.8%</td>
<td align="right">5,073,104,529</td>
<td align="right">75.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,450,959,744</td>
<td align="right">81.1%</td>
<td align="right">5,428,998,796</td>
<td align="right">81.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">945,675,675</td>
<td align="right">14.1%</td>
<td align="right">944,241,015</td>
<td align="right">14.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">949,953,006</td>
<td align="right">14.1%</td>
<td align="right">948,518,346</td>
<td align="right">14.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">276,250,033</td>
<td align="right">4.1%</td>
<td align="right">275,979,671</td>
<td align="right">4.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,626,941,632</td>
<td align="right">24.2%</td>
<td align="right">1,625,486,997</td>
<td align="right">24.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,626,941,632</td>
<td align="right">24.2%</td>
<td align="right">1,625,486,997</td>
<td align="right">24.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">260,794,620</td>
<td align="right">3.9%</td>
<td align="right">260,786,746</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">676,988,626</td>
<td align="right">10.1%</td>
<td align="right">676,968,651</td>
<td align="right">10.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,892,842</td>
<td align="right">0.4%</td>
<td align="right">24,892,501</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,402</td>
<td align="right">2.0%</td>
<td align="right">132,513,402</td>
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
<td align="left">Mortal increfs</td>
<td align="right">25,144,290,064</td>
<td align="right">19.0%</td>
<td align="right">66,358,617,559</td>
<td align="right">48.7%</td>
<td align="right">163.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">32,825,817,174</td>
<td align="right">22.2%</td>
<td align="right">73,501,499,500</td>
<td align="right">48.0%</td>
<td align="right">123.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">78,883,834,353</td>
<td align="right">59.7%</td>
<td align="right">42,170,769,523</td>
<td align="right">30.9%</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">88,590,762,479</td>
<td align="right">59.8%</td>
<td align="right">52,380,398,721</td>
<td align="right">34.2%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,658,621,780</td>
<td align="right">3.5%</td>
<td align="right">3,002,077,024</td>
<td align="right">2.2%</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,894,461,978</td>
<td align="right">1.3%</td>
<td align="right">1,235,039,239</td>
<td align="right">0.8%</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">5,335,856</td>
<td align="right"></td>
<td align="right">6,158,036</td>
<td align="right"></td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">475,311</td>
<td align="right">0.3%</td>
<td align="right">434,351</td>
<td align="right">0.2%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,251,936,285</td>
<td align="right"></td>
<td align="right">2,061,280,714</td>
<td align="right"></td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">23,385,352,442</td>
<td align="right">17.7%</td>
<td align="right">24,733,254,840</td>
<td align="right">18.2%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,744,874,130</td>
<td align="right">16.7%</td>
<td align="right">26,047,439,313</td>
<td align="right">17.0%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">64,638,408</td>
<td align="right"></td>
<td align="right">66,034,244</td>
<td align="right"></td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">60,106,002</td>
<td align="right"></td>
<td align="right">60,678,710</td>
<td align="right"></td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,227,205</td>
<td align="right"></td>
<td align="right">178,368,104</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,980,076,602</td>
<td align="right">31.7%</td>
<td align="right">5,962,471,422</td>
<td align="right">31.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,651,594,163</td>
<td align="right"></td>
<td align="right">6,632,066,554</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,058,056,010</td>
<td align="right">32.2%</td>
<td align="right">6,040,293,306</td>
<td align="right">32.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,881,531,397</td>
<td align="right"></td>
<td align="right">2,873,097,903</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,558,467</td>
<td align="right">0.4%</td>
<td align="right">71,401,784</td>
<td align="right">0.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,778,434,723</td>
<td align="right"></td>
<td align="right">12,755,095,648</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,778,324,597</td>
<td align="right">67.8%</td>
<td align="right">12,754,995,759</td>
<td align="right">67.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,420,941</td>
<td align="right">0.0%</td>
<td align="right">6,420,100</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,443,445</td>
<td align="right">2.5%</td>
<td align="right">4,443,445</td>
<td align="right">2.5%</td>
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
<td align="right">364,984</td>
<td align="right">102,285,972</td>
<td align="right">9,592,063,940</td>
<td align="right">764,228,669</td>
<td align="right">765,768,882</td>
<td align="right">364,149</td>
<td align="right">100,769,215</td>
<td align="right">9,606,867,207</td>
<td align="right">767,041,572</td>
<td align="right">765,235,527</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,627,071,138</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,627,331,298</td>
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
<td align="right">30</td>
<td align="right">30</td>
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
<td align="right">37</td>
<td align="right">37</td>
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
<td align="right">100</td>
<td align="right">100 / 0 !!</td>
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
<td align="right">100</td>
<td align="right">100 / 0 !!</td>
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
<td align="right">2,479</td>
<td align="right">2,479</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-03-28
