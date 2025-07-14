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
<td align="right">5,784,426,932</td>
<td align="right">6,254,917</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,726,146</td>
<td align="right">1,349,822</td>
<td align="right">-98.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">454,419,508</td>
<td align="right">13,990,506</td>
<td align="right">-96.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,353,996</td>
<td align="right">2,731,887</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">6,245,700</td>
<td align="right">-93.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,481,931,097</td>
<td align="right">211,364,722</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">699,151,985</td>
<td align="right">105,501,073</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,748,640,214</td>
<td align="right">275,086,334</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,260,300,317</td>
<td align="right">205,151,440</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,701,184,589</td>
<td align="right">458,629,915</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">564,541,626</td>
<td align="right">96,300,347</td>
<td align="right">-82.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,140,172,486</td>
<td align="right">405,450,321</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,258,177,324</td>
<td align="right">280,770,396</td>
<td align="right">-77.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">530,636,071</td>
<td align="right">118,811,767</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">337,891,673</td>
<td align="right">77,861,022</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,648,002</td>
<td align="right">35,973,423</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,747,060,650</td>
<td align="right">903,935,742</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,546,154,282</td>
<td align="right">375,253,299</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,848,547,538</td>
<td align="right">498,122,834</td>
<td align="right">-73.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">942,167,217</td>
<td align="right">254,315,572</td>
<td align="right">-73.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,475,135,404</td>
<td align="right">685,683,738</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">698,689,252</td>
<td align="right">200,916,840</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">635,256,062</td>
<td align="right">187,148,559</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">190,607,927</td>
<td align="right">56,175,996</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">501,632,612</td>
<td align="right">148,534,854</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">367,293,091</td>
<td align="right">108,859,214</td>
<td align="right">-70.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,711,759,377</td>
<td align="right">2,475,523,294</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,146,688,065</td>
<td align="right">698,186,157</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,464,860</td>
<td align="right">51,781,126</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,468,108,593</td>
<td align="right">1,153,541,719</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">536,773,391</td>
<td align="right">178,680,814</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,108,467,764</td>
<td align="right">372,040,359</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">555,842,658</td>
<td align="right">195,531,735</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">740,117,342</td>
<td align="right">275,437,573</td>
<td align="right">-62.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">56,814,359</td>
<td align="right">21,523,753</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,953,184,703</td>
<td align="right">742,394,961</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">112,839,761</td>
<td align="right">43,196,727</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">373,933,613</td>
<td align="right">143,940,216</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,636,323,073</td>
<td align="right">1,016,667,139</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,473,096,176</td>
<td align="right">4,150,575,670</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">433,850,863</td>
<td align="right">172,552,383</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,741,642,982</td>
<td align="right">1,091,267,964</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">65,308,513</td>
<td align="right">25,999,897</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,102,841,308</td>
<td align="right">448,830,501</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,190,300,382</td>
<td align="right">5,878,329,260</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">148,763,608</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">264,682,435</td>
<td align="right">111,532,773</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">22,595,120</td>
<td align="right">9,550,843</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,160,927,255</td>
<td align="right">1,343,232,059</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">859,385,516</td>
<td align="right">370,121,977</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,637,439</td>
<td align="right">32,284,128</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6,560,272</td>
<td align="right">2,854,596</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">91,190,312</td>
<td align="right">39,954,492</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">11,807,347,617</td>
<td align="right">5,186,693,349</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,049,376,789</td>
<td align="right">472,408,269</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,758,423,956</td>
<td align="right">3,059,530,400</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,154,000</td>
<td align="right">2,840,180</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">467,537,602</td>
<td align="right">216,130,024</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">312,948,142</td>
<td align="right">147,127,864</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">818,025,638</td>
<td align="right">387,490,701</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">395,736,944</td>
<td align="right">190,576,908</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,385,958,485</td>
<td align="right">1,172,825,803</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">577,648,424</td>
<td align="right">289,875,058</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,090,707,176</td>
<td align="right">552,179,257</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">9,075,444,779</td>
<td align="right">4,661,647,501</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">314,003,186</td>
<td align="right">165,578,768</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">12,021,858</td>
<td align="right">6,363,650</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,877,719</td>
<td align="right">52,448,562</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,564,871,033</td>
<td align="right">1,392,867,422</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">987,919,066</td>
<td align="right">536,908,295</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,228,210,663</td>
<td align="right">669,783,411</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">297,014,386</td>
<td align="right">162,179,853</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">38,388,090,296</td>
<td align="right">21,414,381,260</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">204,697,979</td>
<td align="right">118,135,001</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">140,554,019</td>
<td align="right">81,966,060</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,050,846,203</td>
<td align="right">615,673,959</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">116,623,025</td>
<td align="right">68,708,553</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,640,328,826</td>
<td align="right">981,553,386</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">84,639,364</td>
<td align="right">50,783,228</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">812,928,560</td>
<td align="right">492,261,157</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,344,839</td>
<td align="right">4,481,107</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,356,162,716</td>
<td align="right">828,812,675</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">294,668,308</td>
<td align="right">180,136,098</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,626,823</td>
<td align="right">115,592,492</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,601,740,037</td>
<td align="right">1,644,970,489</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">144,097,391</td>
<td align="right">91,963,986</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">417,331,175</td>
<td align="right">270,846,253</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">184,591,301</td>
<td align="right">120,657,325</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">113,987,469</td>
<td align="right">74,745,505</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">2,332,424</td>
<td align="right">1,535,624</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,521,117,939</td>
<td align="right">2,329,683,186</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,683,959,909</td>
<td align="right">3,105,805,411</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">121,628,901</td>
<td align="right">81,071,793</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">61,875,703</td>
<td align="right">41,252,537</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">213,894,647</td>
<td align="right">144,276,189</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">836,583,116</td>
<td align="right">565,591,957</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">177,339,515</td>
<td align="right">119,966,211</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">61,260,458</td>
<td align="right">41,944,782</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">498,595,139</td>
<td align="right">354,587,299</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">442,970,039</td>
<td align="right">315,612,348</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,330,155,501</td>
<td align="right">3,805,033,715</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">66,958,345</td>
<td align="right">48,068,515</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">419,857,742</td>
<td align="right">301,735,070</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">344,908,170</td>
<td align="right">250,001,751</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">23,354</td>
<td align="right">17,210</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">218,010,776</td>
<td align="right">164,367,901</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,698,163</td>
<td align="right">1,315,441</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,928,397,217</td>
<td align="right">3,060,875,151</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">289,867,237</td>
<td align="right">226,101,790</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">353,781,411</td>
<td align="right">281,405,882</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">79,762,867</td>
<td align="right">64,531,933</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,444,079,352</td>
<td align="right">2,798,174,935</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,553,919</td>
<td align="right">1,265,519</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,448,794,482</td>
<td align="right">2,819,963,872</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,104,606,182</td>
<td align="right">5,816,355,299</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">347,938,076</td>
<td align="right">289,768,138</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,463,585</td>
<td align="right">2,901,350</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,165,730,081</td>
<td align="right">986,882,594</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">612,013,536</td>
<td align="right">520,101,742</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">336,727,455</td>
<td align="right">288,706,371</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">570,607,088</td>
<td align="right">500,452,877</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,013,566</td>
<td align="right">368,303,524</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">6,297,051,243</td>
<td align="right">5,586,476,337</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">117,480,362</td>
<td align="right">104,427,274</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">390,314,597</td>
<td align="right">347,703,238</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,002,368,395</td>
<td align="right">893,437,150</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">332,404,813</td>
<td align="right">299,816,133</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">140,583,051</td>
<td align="right">127,323,049</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">148,578,793</td>
<td align="right">134,601,377</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,599,446,741</td>
<td align="right">1,461,582,305</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">75,536,045</td>
<td align="right">69,667,527</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">117,946,633</td>
<td align="right">108,866,328</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">4,131,223</td>
<td align="right">3,824,023</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">66,064,613</td>
<td align="right">61,184,333</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,279,043</td>
<td align="right">5,918,615</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">64,103,596</td>
<td align="right">60,657,474</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,734,244</td>
<td align="right">67,183,462</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,169,929</td>
<td align="right">20,346,356</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,445,450</td>
<td align="right">20,621,877</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,445,471</td>
<td align="right">20,621,898</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,108,062,741</td>
<td align="right">1,067,059,301</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">13,523,839</td>
<td align="right">13,028,564</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,781,029</td>
<td align="right">10,387,898</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">80,107,004</td>
<td align="right">77,424,373</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,887,601</td>
<td align="right">9,622,664</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">72,491,206</td>
<td align="right">70,670,298</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">130,185,212</td>
<td align="right">126,964,862</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,100,432</td>
<td align="right">3,034,786</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">68,953,988</td>
<td align="right">67,779,992</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">80,217</td>
<td align="right">78,915</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,866,538,503</td>
<td align="right">1,850,929,272</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,572,241</td>
<td align="right">5,545,316</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">214,591,064</td>
<td align="right">213,694,053</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">312,620,677</td>
<td align="right">311,795,699</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">314,670,791</td>
<td align="right">313,844,449</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">155,083,922</td>
<td align="right">154,709,343</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,690,305</td>
<td align="right">114,491,228</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,454,736</td>
<td align="right">28,433,125</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,720,203</td>
<td align="right">418,484,627</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,580,580</td>
<td align="right">1,580,346</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">560,102</td>
<td align="right">560,157</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,928,332</td>
<td align="right">35,926,296</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">92,030</td>
<td align="right">92,026</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">324,555</td>
<td align="right">324,566</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,478,727</td>
<td align="right">591,462,355</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,554,438</td>
<td align="right">302,552,390</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">333,538</td>
<td align="right">333,537</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">15,623,105</td>
<td align="right">15,623,106</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,636,886</td>
<td align="right">172,636,886</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,310,881</td>
<td align="right">129,310,881</td>
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
<td align="right">41,858,572</td>
<td align="right">41,858,572</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,660</td>
<td align="right">29,134,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">29,134,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">11,838,546</td>
<td align="right">11,838,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,951,274</td>
<td align="right">8,951,274</td>
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
<td align="left">CLEANUP_THROW</td>
<td align="right">120,759</td>
<td align="right">120,759</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">115,623</td>
<td align="right">115,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">106,354</td>
<td align="right">106,354</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">74,697</td>
<td align="right">74,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">73,792</td>
<td align="right">73,792</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">50,376</td>
<td align="right">50,376</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">23,410</td>
<td align="right">23,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,157</td>
<td align="right">14,157</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,959</td>
<td align="right">5,959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">3,696</td>
<td align="right">3,696</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,709</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,776</td>
<td align="right">1,776</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">725</td>
<td align="right">725</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">1,056,095,190</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">848,562,204</td>
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
<td align="right">16,890,370,345</td>
<td align="right">87.3%</td>
<td align="right">4,769,704,657</td>
<td align="right">79.4%</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,384,712,644</td>
<td align="right">12.3%</td>
<td align="right">1,171,992,564</td>
<td align="right">19.5%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">71,992,654</td>
<td align="right">0.4%</td>
<td align="right">65,507,678</td>
<td align="right">1.1%</td>
<td align="right">-9.0%</td>
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
<td align="right">1,087,493</td>
<td align="right">41.8%</td>
<td align="right">674,918</td>
<td align="right">32.6%</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,514,724</td>
<td align="right">58.2%</td>
<td align="right">1,392,359</td>
<td align="right">67.4%</td>
<td align="right">-8.1%</td>
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
<td align="left">subscr bytes</td>
<td align="right">25,632</td>
<td align="right">2.4%</td>
<td align="right">5,170</td>
<td align="right">0.8%</td>
<td align="right">-79.8%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">114,008</td>
<td align="right">10.5%</td>
<td align="right">29,084</td>
<td align="right">4.3%</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">126,579</td>
<td align="right">11.6%</td>
<td align="right">33,181</td>
<td align="right">4.9%</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">88,203</td>
<td align="right">8.1%</td>
<td align="right">25,123</td>
<td align="right">3.7%</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">14,049</td>
<td align="right">1.3%</td>
<td align="right">5,350</td>
<td align="right">0.8%</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">71,160</td>
<td align="right">6.5%</td>
<td align="right">29,721</td>
<td align="right">4.4%</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">29,806</td>
<td align="right">2.7%</td>
<td align="right">15,185</td>
<td align="right">2.2%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,759</td>
<td align="right">0.2%</td>
<td align="right">1,041</td>
<td align="right">0.2%</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">900</td>
<td align="right">0.1%</td>
<td align="right">560</td>
<td align="right">0.1%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">22,724</td>
<td align="right">2.1%</td>
<td align="right">15,137</td>
<td align="right">2.2%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">41,971</td>
<td align="right">3.9%</td>
<td align="right">28,131</td>
<td align="right">4.2%</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">18,714</td>
<td align="right">1.7%</td>
<td align="right">12,881</td>
<td align="right">1.9%</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">56,714</td>
<td align="right">5.2%</td>
<td align="right">39,634</td>
<td align="right">5.9%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">754</td>
<td align="right">0.1%</td>
<td align="right">567</td>
<td align="right">0.1%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">87,210</td>
<td align="right">8.0%</td>
<td align="right">71,298</td>
<td align="right">10.6%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">13,113</td>
<td align="right">1.2%</td>
<td align="right">10,953</td>
<td align="right">1.6%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">62,111</td>
<td align="right">5.7%</td>
<td align="right">53,271</td>
<td align="right">7.9%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">63,123</td>
<td align="right">5.8%</td>
<td align="right">56,525</td>
<td align="right">8.4%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">64,472</td>
<td align="right">5.9%</td>
<td align="right">58,435</td>
<td align="right">8.7%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">1,227</td>
<td align="right">0.1%</td>
<td align="right">1,164</td>
<td align="right">0.2%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">4,915</td>
<td align="right">0.5%</td>
<td align="right">4,813</td>
<td align="right">0.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">15,486</td>
<td align="right">1.4%</td>
<td align="right">15,270</td>
<td align="right">2.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">25,262</td>
<td align="right">2.3%</td>
<td align="right">24,950</td>
<td align="right">3.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">8,485</td>
<td align="right">0.8%</td>
<td align="right">8,422</td>
<td align="right">1.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">4,257</td>
<td align="right">0.4%</td>
<td align="right">4,237</td>
<td align="right">0.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">5,634</td>
<td align="right">0.5%</td>
<td align="right">5,613</td>
<td align="right">0.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,414</td>
<td align="right">0.1%</td>
<td align="right">1,412</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">109,862</td>
<td align="right">10.1%</td>
<td align="right">109,841</td>
<td align="right">16.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,785</td>
<td align="right">0.3%</td>
<td align="right">3,785</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,756</td>
<td align="right">0.3%</td>
<td align="right">2,756</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">363</td>
<td align="right">0.0%</td>
<td align="right">363</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr structtime</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">81</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
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
<td align="right">555,842,658</td>
<td align="right">100.0%</td>
<td align="right">195,531,735</td>
<td align="right">100.0%</td>
<td align="right">-64.8%</td>
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
<td align="right">12,175,874,279</td>
<td align="right">98.4%</td>
<td align="right">6,361,972,419</td>
<td align="right">97.4%</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">194,550,527</td>
<td align="right">1.6%</td>
<td align="right">165,664,292</td>
<td align="right">2.5%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">191,862,295</td>
<td align="right">1.6%</td>
<td align="right">163,521,168</td>
<td align="right">2.5%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,720</td>
<td align="right">0.0%</td>
<td align="right">6,720</td>
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
<td align="right">4,268,646</td>
<td align="right">100.0%</td>
<td align="right">3,723,304</td>
<td align="right">100.0%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">166</td>
<td align="right">0.0%</td>
<td align="right">166</td>
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
<td align="right">3,414</td>
<td align="right">2,056.6%</td>
<td align="right">3,414</td>
<td align="right">2,056.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">947</td>
<td align="right">570.5%</td>
<td align="right">947</td>
<td align="right">570.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">166</td>
<td align="right">100.0%</td>
<td align="right">166</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">685,116</td>
<td align="right">91.8%</td>
<td align="right">685,118</td>
<td align="right">91.8%</td>
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
<td align="right">640,338</td>
<td align="right">85.8%</td>
<td align="right">640,338</td>
<td align="right">85.8%</td>
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
<td align="right">61,576</td>
<td align="right">100.0%</td>
<td align="right">61,574</td>
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
<td align="right">530,294,136</td>
<td align="right">9.3%</td>
<td align="right">118,580,814</td>
<td align="right">5.7%</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,196,782,805</td>
<td align="right">90.7%</td>
<td align="right">1,955,818,840</td>
<td align="right">94.2%</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,318,811</td>
<td align="right">0.0%</td>
<td align="right">1,128,545</td>
<td align="right">0.1%</td>
<td align="right">-14.4%</td>
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
<td align="right">275,950</td>
<td align="right">75.3%</td>
<td align="right">164,969</td>
<td align="right">65.5%</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">90,461</td>
<td align="right">24.7%</td>
<td align="right">86,771</td>
<td align="right">34.5%</td>
<td align="right">-4.1%</td>
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
<td align="right">97,272</td>
<td align="right">35.2%</td>
<td align="right">12,324</td>
<td align="right">7.5%</td>
<td align="right">-87.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">7,625</td>
<td align="right">2.8%</td>
<td align="right">1,243</td>
<td align="right">0.8%</td>
<td align="right">-83.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">20,705</td>
<td align="right">7.5%</td>
<td align="right">14,862</td>
<td align="right">9.0%</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">64,866</td>
<td align="right">23.5%</td>
<td align="right">53,889</td>
<td align="right">32.7%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,692</td>
<td align="right">5.3%</td>
<td align="right">12,209</td>
<td align="right">7.4%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">514</td>
<td align="right">0.2%</td>
<td align="right">473</td>
<td align="right">0.3%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">2,842</td>
<td align="right">1.0%</td>
<td align="right">2,738</td>
<td align="right">1.7%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,598</td>
<td align="right">10.0%</td>
<td align="right">27,415</td>
<td align="right">16.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,839</td>
<td align="right">1.0%</td>
<td align="right">2,821</td>
<td align="right">1.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">22,221</td>
<td align="right">8.1%</td>
<td align="right">22,219</td>
<td align="right">13.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">11,543</td>
<td align="right">4.2%</td>
<td align="right">11,543</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,233</td>
<td align="right">1.2%</td>
<td align="right">3,233</td>
<td align="right">2.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,181,121,644</td>
<td align="right">92.1%</td>
<td align="right">446,920,548</td>
<td align="right">78.6%</td>
<td align="right">-79.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,369,433</td>
<td align="right">0.1%</td>
<td align="right">718,169</td>
<td align="right">0.1%</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">184,448,820</td>
<td align="right">7.8%</td>
<td align="right">120,530,846</td>
<td align="right">21.2%</td>
<td align="right">-34.7%</td>
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
<td align="right">41,395</td>
<td align="right">24.6%</td>
<td align="right">29,107</td>
<td align="right">20.8%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">126,811</td>
<td align="right">75.4%</td>
<td align="right">110,809</td>
<td align="right">79.2%</td>
<td align="right">-12.6%</td>
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
<td align="right">43,529</td>
<td align="right">34.3%</td>
<td align="right">32,490</td>
<td align="right">29.3%</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">19,730</td>
<td align="right">15.6%</td>
<td align="right">17,973</td>
<td align="right">16.2%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">32,252</td>
<td align="right">25.4%</td>
<td align="right">29,742</td>
<td align="right">26.8%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">31,300</td>
<td align="right">24.7%</td>
<td align="right">30,604</td>
<td align="right">27.6%</td>
<td align="right">-2.2%</td>
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
<td align="right">1,481,351,818</td>
<td align="right">28.9%</td>
<td align="right">211,105,057</td>
<td align="right">13.4%</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,489,057,312</td>
<td align="right">68.0%</td>
<td align="right">1,301,268,805</td>
<td align="right">82.6%</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">162,065,019</td>
<td align="right">3.2%</td>
<td align="right">62,562,858</td>
<td align="right">4.0%</td>
<td align="right">-61.4%</td>
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
<td align="right">519,605</td>
<td align="right">14.3%</td>
<td align="right">199,999</td>
<td align="right">13.9%</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,117,071</td>
<td align="right">85.7%</td>
<td align="right">1,239,666</td>
<td align="right">86.1%</td>
<td align="right">-60.2%</td>
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
<td align="right">175,073</td>
<td align="right">33.7%</td>
<td align="right">10,312</td>
<td align="right">5.2%</td>
<td align="right">-94.1%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">89,103</td>
<td align="right">17.1%</td>
<td align="right">17,503</td>
<td align="right">8.8%</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">46,750</td>
<td align="right">9.0%</td>
<td align="right">18,715</td>
<td align="right">9.4%</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">12,435</td>
<td align="right">2.4%</td>
<td align="right">5,609</td>
<td align="right">2.8%</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">22,380</td>
<td align="right">4.3%</td>
<td align="right">10,570</td>
<td align="right">5.3%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">2,065</td>
<td align="right">0.4%</td>
<td align="right">1,183</td>
<td align="right">0.6%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,148</td>
<td align="right">3.3%</td>
<td align="right">10,360</td>
<td align="right">5.2%</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">5,499</td>
<td align="right">1.1%</td>
<td align="right">3,497</td>
<td align="right">1.7%</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">5,583</td>
<td align="right">1.1%</td>
<td align="right">4,254</td>
<td align="right">2.1%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">23,559</td>
<td align="right">4.5%</td>
<td align="right">18,593</td>
<td align="right">9.3%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">96,041</td>
<td align="right">18.5%</td>
<td align="right">77,595</td>
<td align="right">38.8%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,124</td>
<td align="right">0.4%</td>
<td align="right">1,785</td>
<td align="right">0.9%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">8,625</td>
<td align="right">1.7%</td>
<td align="right">7,734</td>
<td align="right">3.9%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">11,801</td>
<td align="right">2.3%</td>
<td align="right">10,890</td>
<td align="right">5.4%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">1,159</td>
<td align="right">0.2%</td>
<td align="right">1,159</td>
<td align="right">0.6%</td>
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
<td align="left">string</td>
<td align="right">2,799,014</td>
<td align="right">2,799,014 / 0 !!</td>
<td align="right">1,742,246</td>
<td align="right">1,742,246 / 0 !!</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">117,057,114</td>
<td align="right">117,057,114 / 0 !!</td>
<td align="right">112,137,545</td>
<td align="right">112,137,545 / 0 !!</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,399,958</td>
<td align="right">34,399,958 / 0 !!</td>
<td align="right">33,902,248</td>
<td align="right">33,902,248 / 0 !!</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,653,840</td>
<td align="right">5,653,840 / 0 !!</td>
<td align="right">5,578,094</td>
<td align="right">5,578,094 / 0 !!</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">305,705,773</td>
<td align="right">305,705,773 / 0 !!</td>
<td align="right">302,070,803</td>
<td align="right">302,070,803 / 0 !!</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,678,494</td>
<td align="right">101,678,494 / 0 !!</td>
<td align="right">101,287,372</td>
<td align="right">101,287,372 / 0 !!</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,386,582</td>
<td align="right">12,386,582 / 0 !!</td>
<td align="right">12,354,599</td>
<td align="right">12,354,599 / 0 !!</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">336,990,185</td>
<td align="right">336,990,185 / 0 !!</td>
<td align="right">336,452,159</td>
<td align="right">336,452,159 / 0 !!</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">173,221,887</td>
<td align="right">173,221,887 / 0 !!</td>
<td align="right">172,964,356</td>
<td align="right">172,964,356 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">814,329</td>
<td align="right">814,329 / 0 !!</td>
<td align="right">814,329</td>
<td align="right">814,329 / 0 !!</td>
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
<td align="right">14,832,285,892</td>
<td align="right">89.7%</td>
<td align="right">9,829,284,836</td>
<td align="right">89.1%</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">833,775,423</td>
<td align="right">5.0%</td>
<td align="right">562,877,498</td>
<td align="right">5.1%</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">869,398,817</td>
<td align="right">5.3%</td>
<td align="right">642,162,505</td>
<td align="right">5.8%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,386,949</td>
<td align="right">0.0%</td>
<td align="right">1,133,675</td>
<td align="right">0.0%</td>
<td align="right">-18.3%</td>
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
<td align="right">17,014,370</td>
<td align="right">95.3%</td>
<td align="right">12,727,397</td>
<td align="right">94.3%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">841,770</td>
<td align="right">4.7%</td>
<td align="right">764,853</td>
<td align="right">5.7%</td>
<td align="right">-9.1%</td>
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
<td align="right">118,562</td>
<td align="right">14.1%</td>
<td align="right">79,788</td>
<td align="right">10.4%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">91,783</td>
<td align="right">10.9%</td>
<td align="right">78,013</td>
<td align="right">10.2%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">3,068</td>
<td align="right">0.4%</td>
<td align="right">2,753</td>
<td align="right">0.4%</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">13,506</td>
<td align="right">1.6%</td>
<td align="right">12,304</td>
<td align="right">1.6%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">5,081</td>
<td align="right">0.6%</td>
<td align="right">4,745</td>
<td align="right">0.6%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">30,981</td>
<td align="right">3.7%</td>
<td align="right">29,039</td>
<td align="right">3.8%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">145,378</td>
<td align="right">17.3%</td>
<td align="right">136,853</td>
<td align="right">17.9%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">4,306</td>
<td align="right">0.5%</td>
<td align="right">4,139</td>
<td align="right">0.5%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">42,671</td>
<td align="right">5.1%</td>
<td align="right">41,169</td>
<td align="right">5.4%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">9,020</td>
<td align="right">1.1%</td>
<td align="right">8,978</td>
<td align="right">1.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">14,879</td>
<td align="right">1.8%</td>
<td align="right">14,843</td>
<td align="right">1.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">21,865</td>
<td align="right">2.6%</td>
<td align="right">21,864</td>
<td align="right">2.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,673</td>
<td align="right">0.2%</td>
<td align="right">1,673</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,092</td>
<td align="right">0.1%</td>
<td align="right">1,092</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">1,021</td>
<td align="right">0.1%</td>
<td align="right">1,021</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">106</td>
<td align="right">0.0%</td>
<td align="right">106</td>
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
<td align="right">10,686,508,066</td>
<td align="right">99.9%</td>
<td align="right">6,120,093,031</td>
<td align="right">99.7%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">313,107</td>
<td align="right">0.0%</td>
<td align="right">312,520</td>
<td align="right">0.0%</td>
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
<td align="right">15,100,883</td>
<td align="right">0.1%</td>
<td align="right">15,100,917</td>
<td align="right">0.2%</td>
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
<td align="right">5,094</td>
<td align="right">0.0%</td>
<td align="right">5,094</td>
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
<td align="right">527,345</td>
<td align="right">100.0%</td>
<td align="right">527,312</td>
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
<td align="right">67,204,028</td>
<td align="right">100.0%</td>
<td align="right">63,692,260</td>
<td align="right">100.0%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,987</td>
<td align="right">0.0%</td>
<td align="right">6,987</td>
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
<td align="right">7,170</td>
<td align="right">100.0%</td>
<td align="right">7,170</td>
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
<td align="right">591,451,306</td>
<td align="right">82.1%</td>
<td align="right">591,434,934</td>
<td align="right">82.1%</td>
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
<td align="right">129,260,906</td>
<td align="right">17.9%</td>
<td align="right">129,260,906</td>
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
<td align="right">27,421</td>
<td align="right">0.0%</td>
<td align="right">27,421</td>
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
<td align="right">4,554</td>
<td align="right">9.0%</td>
<td align="right">4,554</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,927</td>
<td align="right">91.0%</td>
<td align="right">45,927</td>
<td align="right">91.0%</td>
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
<td align="right">25,040</td>
<td align="right">54.5%</td>
<td align="right">25,040</td>
<td align="right">54.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,693</td>
<td align="right">21.1%</td>
<td align="right">9,693</td>
<td align="right">21.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,073</td>
<td align="right">19.8%</td>
<td align="right">9,073</td>
<td align="right">19.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,121</td>
<td align="right">4.6%</td>
<td align="right">2,121</td>
<td align="right">4.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,485,224,899</td>
<td align="right">92.8%</td>
<td align="right">2,245,202,435</td>
<td align="right">92.6%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">65,851,026</td>
<td align="right">2.5%</td>
<td align="right">60,972,203</td>
<td align="right">2.5%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">125,541,511</td>
<td align="right">4.7%</td>
<td align="right">118,768,294</td>
<td align="right">4.9%</td>
<td align="right">-5.4%</td>
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
<td align="right">2,475,416</td>
<td align="right">96.0%</td>
<td align="right">2,347,669</td>
<td align="right">95.9%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">102,722</td>
<td align="right">4.0%</td>
<td align="right">101,265</td>
<td align="right">4.1%</td>
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
<td align="left">method</td>
<td align="right">603</td>
<td align="right">0.6%</td>
<td align="right">519</td>
<td align="right">0.5%</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">9,321</td>
<td align="right">9.1%</td>
<td align="right">8,188</td>
<td align="right">8.1%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,088</td>
<td align="right">3.0%</td>
<td align="right">2,942</td>
<td align="right">2.9%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">631</td>
<td align="right">0.6%</td>
<td align="right">610</td>
<td align="right">0.6%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">319,652</td>
<td align="right">311.2%</td>
<td align="right">310,196</td>
<td align="right">306.3%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">7,974</td>
<td align="right">7.8%</td>
<td align="right">7,891</td>
<td align="right">7.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">11,033</td>
<td align="right">10.7%</td>
<td align="right">11,043</td>
<td align="right">10.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">43,626</td>
<td align="right">42.5%</td>
<td align="right">43,626</td>
<td align="right">43.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">14,124</td>
<td align="right">13.7%</td>
<td align="right">14,124</td>
<td align="right">13.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">7,044</td>
<td align="right">6.9%</td>
<td align="right">7,044</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,823</td>
<td align="right">1.8%</td>
<td align="right">1,823</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">273</td>
<td align="right">0.3%</td>
<td align="right">273</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">251</td>
<td align="right">0.2%</td>
<td align="right">251</td>
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
<td align="right">112,726,146</td>
<td align="right">100.0%</td>
<td align="right">1,349,822</td>
<td align="right">100.0%</td>
<td align="right">-98.8%</td>
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
<td align="right">698,912,170</td>
<td align="right">42.7%</td>
<td align="right">105,406,186</td>
<td align="right">30.5%</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">938,473,079</td>
<td align="right">57.3%</td>
<td align="right">240,238,403</td>
<td align="right">69.5%</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,160</td>
<td align="right">0.0%</td>
<td align="right">2,160</td>
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
<td align="right">224,647</td>
<td align="right">93.7%</td>
<td align="right">79,721</td>
<td align="right">84.0%</td>
<td align="right">-64.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">15,208</td>
<td align="right">6.3%</td>
<td align="right">15,206</td>
<td align="right">16.0%</td>
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
<td align="left">other</td>
<td align="right">85,774</td>
<td align="right">38.2%</td>
<td align="right">850</td>
<td align="right">1.1%</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">8,795</td>
<td align="right">3.9%</td>
<td align="right">2,202</td>
<td align="right">2.8%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">53,621</td>
<td align="right">23.9%</td>
<td align="right">16,173</td>
<td align="right">20.3%</td>
<td align="right">-69.8%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">23,849</td>
<td align="right">10.6%</td>
<td align="right">7,909</td>
<td align="right">9.9%</td>
<td align="right">-66.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,485</td>
<td align="right">2.0%</td>
<td align="right">4,464</td>
<td align="right">5.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">45,016</td>
<td align="right">20.0%</td>
<td align="right">45,016</td>
<td align="right">56.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">2,939</td>
<td align="right">1.3%</td>
<td align="right">2,939</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">168</td>
<td align="right">0.1%</td>
<td align="right">168</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">113,857,091</td>
<td align="right">1.8%</td>
<td align="right">69,700,704</td>
<td align="right">1.7%</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,609,683,712</td>
<td align="right">91.0%</td>
<td align="right">3,659,967,651</td>
<td align="right">90.5%</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">442,058,664</td>
<td align="right">7.2%</td>
<td align="right">314,841,366</td>
<td align="right">7.8%</td>
<td align="right">-28.8%</td>
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
<td align="right">2,367,168</td>
<td align="right">77.5%</td>
<td align="right">1,533,983</td>
<td align="right">73.7%</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">686,648</td>
<td align="right">22.5%</td>
<td align="right">546,251</td>
<td align="right">26.3%</td>
<td align="right">-20.4%</td>
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
<td align="right">20,936</td>
<td align="right">3.0%</td>
<td align="right">6,774</td>
<td align="right">1.2%</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">133,152</td>
<td align="right">19.4%</td>
<td align="right">55,899</td>
<td align="right">10.2%</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">81,319</td>
<td align="right">11.8%</td>
<td align="right">48,705</td>
<td align="right">8.9%</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">23,634</td>
<td align="right">3.4%</td>
<td align="right">17,269</td>
<td align="right">3.2%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">94,755</td>
<td align="right">13.8%</td>
<td align="right">85,650</td>
<td align="right">15.7%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">11,872</td>
<td align="right">1.7%</td>
<td align="right">10,961</td>
<td align="right">2.0%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,017</td>
<td align="right">1.9%</td>
<td align="right">13,021</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">305,901</td>
<td align="right">44.5%</td>
<td align="right">305,910</td>
<td align="right">56.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">622</td>
<td align="right">0.1%</td>
<td align="right">622</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
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
<td align="right">1,271,016,840</td>
<td align="right">99.9%</td>
<td align="right">685,567,292</td>
<td align="right">99.8%</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,658,437</td>
<td align="right">0.1%</td>
<td align="right">1,275,773</td>
<td align="right">0.2%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">2,660</td>
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
<td align="right">2,537</td>
<td align="right">6.4%</td>
<td align="right">2,475</td>
<td align="right">6.2%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">37,229</td>
<td align="right">93.6%</td>
<td align="right">37,233</td>
<td align="right">93.8%</td>
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
<td align="right">1,843</td>
<td align="right">72.6%</td>
<td align="right">1,782</td>
<td align="right">72.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">316</td>
<td align="right">12.5%</td>
<td align="right">315</td>
<td align="right">12.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">378</td>
<td align="right">14.9%</td>
<td align="right">378</td>
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
<td align="right">8,535,495,927</td>
<td align="right">3.7%</td>
<td align="right">3,568,560,427</td>
<td align="right">3.0%</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">88,143,730,785</td>
<td align="right">38.1%</td>
<td align="right">45,695,943,311</td>
<td align="right">37.9%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">133,233,292,102</td>
<td align="right">57.6%</td>
<td align="right">70,300,718,390</td>
<td align="right">58.2%</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,541,233,820</td>
<td align="right">0.7%</td>
<td align="right">1,127,355,188</td>
<td align="right">0.9%</td>
<td align="right">-26.9%</td>
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
<td align="right">1,481,351,818</td>
<td align="right">19.4%</td>
<td align="right">211,105,057</td>
<td align="right">6.7%</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">698,912,170</td>
<td align="right">9.2%</td>
<td align="right">105,406,186</td>
<td align="right">3.3%</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">530,294,136</td>
<td align="right">7.0%</td>
<td align="right">118,580,814</td>
<td align="right">3.7%</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">555,842,658</td>
<td align="right">7.3%</td>
<td align="right">195,531,735</td>
<td align="right">6.2%</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,384,712,644</td>
<td align="right">31.3%</td>
<td align="right">1,171,992,564</td>
<td align="right">36.9%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">184,448,820</td>
<td align="right">2.4%</td>
<td align="right">120,530,846</td>
<td align="right">3.8%</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">833,775,423</td>
<td align="right">10.9%</td>
<td align="right">562,877,498</td>
<td align="right">17.7%</td>
<td align="right">-32.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">442,058,664</td>
<td align="right">5.8%</td>
<td align="right">314,841,366</td>
<td align="right">9.9%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">191,862,295</td>
<td align="right">2.5%</td>
<td align="right">163,521,168</td>
<td align="right">5.2%</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">129,260,906</td>
<td align="right">1.7%</td>
<td align="right">129,260,906</td>
<td align="right">4.1%</td>
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
<td align="right">81,047,405</td>
<td align="right">5.3%</td>
<td align="right">31,246,440</td>
<td align="right">2.8%</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">80,935,366</td>
<td align="right">5.3%</td>
<td align="right">31,235,063</td>
<td align="right">2.8%</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,808,421</td>
<td align="right">3.6%</td>
<td align="right">32,428,664</td>
<td align="right">2.9%</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">52,207,937</td>
<td align="right">3.4%</td>
<td align="right">31,410,061</td>
<td align="right">2.8%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">369,437,540</td>
<td align="right">24.0%</td>
<td align="right">235,971,273</td>
<td align="right">20.9%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">265,863,089</td>
<td align="right">17.2%</td>
<td align="right">188,473,558</td>
<td align="right">16.7%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">90,579,647</td>
<td align="right">5.9%</td>
<td align="right">66,321,187</td>
<td align="right">5.9%</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">89,371,143</td>
<td align="right">5.8%</td>
<td align="right">81,762,397</td>
<td align="right">7.3%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">84,214,487</td>
<td align="right">5.5%</td>
<td align="right">78,555,055</td>
<td align="right">7.0%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">105,769,620</td>
<td align="right">6.9%</td>
<td align="right">101,927,449</td>
<td align="right">9.0%</td>
<td align="right">-3.6%</td>
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
<td align="right">4,223,902</td>
<td align="right">0.1%</td>
<td align="right">2,111,710</td>
<td align="right">0.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,679,142,023</td>
<td align="right">75.2%</td>
<td align="right">5,583,451,714</td>
<td align="right">75.1%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,423,026</td>
<td align="right">7.7%</td>
<td align="right">575,730,244</td>
<td align="right">7.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,354,723,993</td>
<td align="right">84.2%</td>
<td align="right">6,283,896,411</td>
<td align="right">84.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,570,743</td>
<td align="right">0.9%</td>
<td align="right">70,841,275</td>
<td align="right">1.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,871,223,949</td>
<td align="right">24.8%</td>
<td align="right">1,855,614,713</td>
<td align="right">24.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,871,223,949</td>
<td align="right">24.8%</td>
<td align="right">1,855,614,713</td>
<td align="right">24.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">460,252,122</td>
<td align="right">6.1%</td>
<td align="right">457,325,093</td>
<td align="right">6.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,286,800,923</td>
<td align="right">17.0%</td>
<td align="right">1,279,884,469</td>
<td align="right">17.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,282,526,645</td>
<td align="right">17.0%</td>
<td align="right">1,277,722,383</td>
<td align="right">17.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">307,736,962</td>
<td align="right">4.1%</td>
<td align="right">307,279,594</td>
<td align="right">4.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,815,099</td>
<td align="right">0.3%</td>
<td align="right">23,808,740</td>
<td align="right">0.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">50,376</td>
<td align="right">0.0%</td>
<td align="right">50,376</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">131,916,029</td>
<td align="right">1.7%</td>
<td align="right">131,916,029</td>
<td align="right">1.8%</td>
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
<td align="right">23,023,362</td>
<td align="right"></td>
<td align="right">6,338,491</td>
<td align="right"></td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">83,988,196</td>
<td align="right"></td>
<td align="right">63,520,088</td>
<td align="right"></td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">336,853</td>
<td align="right">0.2%</td>
<td align="right">295,893</td>
<td align="right">0.2%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,280,486,060</td>
<td align="right"></td>
<td align="right">2,078,710,558</td>
<td align="right"></td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">61,664,262</td>
<td align="right"></td>
<td align="right">57,881,670</td>
<td align="right"></td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,950,661,959</td>
<td align="right">1.7%</td>
<td align="right">1,913,444,107</td>
<td align="right">1.7%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">23,493,784,229</td>
<td align="right">24.0%</td>
<td align="right">23,067,974,319</td>
<td align="right">23.8%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">25,814,968,721</td>
<td align="right">26.4%</td>
<td align="right">25,389,633,296</td>
<td align="right">26.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,130,091,141</td>
<td align="right">70.6%</td>
<td align="right">13,916,111,835</td>
<td align="right">70.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,131,758,525</td>
<td align="right"></td>
<td align="right">13,917,786,129</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">23,134,991,207</td>
<td align="right">20.5%</td>
<td align="right">22,820,582,185</td>
<td align="right">20.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">32,637,668,792</td>
<td align="right">28.9%</td>
<td align="right">32,242,526,686</td>
<td align="right">28.8%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">5,388,097,602</td>
<td align="right">5.5%</td>
<td align="right">5,346,534,822</td>
<td align="right">5.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,817,706,084</td>
<td align="right">29.1%</td>
<td align="right">5,773,770,842</td>
<td align="right">29.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,896,000,757</td>
<td align="right">29.4%</td>
<td align="right">5,851,901,264</td>
<td align="right">29.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,469,687,015</td>
<td align="right"></td>
<td align="right">6,422,289,821</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">177,721,562</td>
<td align="right"></td>
<td align="right">176,543,827</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">55,030,039,519</td>
<td align="right">48.8%</td>
<td align="right">54,820,023,486</td>
<td align="right">49.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,695,036</td>
<td align="right">0.4%</td>
<td align="right">71,530,060</td>
<td align="right">0.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,881,762,413</td>
<td align="right"></td>
<td align="right">2,877,129,410</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">43,179,128,960</td>
<td align="right">44.1%</td>
<td align="right">43,238,265,247</td>
<td align="right">44.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,599,637</td>
<td align="right">0.0%</td>
<td align="right">6,600,362</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,639,764</td>
<td align="right">2.0%</td>
<td align="right">3,639,764</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,383</td>
<td align="right">0.0%</td>
<td align="right">4,383</td>
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
<td align="right">367,291</td>
<td align="right">94,885,657</td>
<td align="right">9,781,430,878</td>
<td align="right">809,644,258</td>
<td align="right">758,154,852</td>
<td align="right">365,427</td>
<td align="right">92,801,609</td>
<td align="right">9,735,418,060</td>
<td align="right">806,922,679</td>
<td align="right">754,784,753</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,934</td>
<td align="right">4,304,865</td>
<td align="right">5,704,434,606</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,934</td>
<td align="right">4,304,865</td>
<td align="right">5,704,692,198</td>
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
<td align="right">22,239</td>
<td align="right">22,239</td>
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
<td align="right">714</td>
<td align="right">714</td>
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
<td align="right">901</td>
<td align="right">901</td>
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
<td align="right">401</td>
<td align="right">401 / 0 !!</td>
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
<td align="right">401</td>
<td align="right">401 / 0 !!</td>
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
<td align="right">2,337</td>
<td align="right">2,337</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-07-14
