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
<td align="right">3,874,397</td>
<td align="right">3,654,022,340</td>
<td align="right">94,212.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">485,800</td>
<td align="right">8,111,820</td>
<td align="right">1,569.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">54,270,955</td>
<td align="right">195,241,047</td>
<td align="right">259.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">219,468</td>
<td align="right">662,271</td>
<td align="right">201.8%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,420</td>
<td align="right">478,280</td>
<td align="right">175.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,376,440</td>
<td align="right">6,338,243</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">8,000,960</td>
<td align="right">960</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">8,000,000</td>
<td align="right">1,800</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,451,690</td>
<td align="right">64,501</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">481,492,919</td>
<td align="right">788,530</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,580,110</td>
<td align="right">671,181</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,024,162</td>
<td align="right">3,830,180</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">195,651,646</td>
<td align="right">2,083,742</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,101,108</td>
<td align="right">1,187,400</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,961,863</td>
<td align="right">348,822</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">68,002,425</td>
<td align="right">130,343,991</td>
<td align="right">91.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">146,912,060</td>
<td align="right">18,319,892</td>
<td align="right">-87.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">23,966,865</td>
<td align="right">44,904,981</td>
<td align="right">87.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,612,192</td>
<td align="right">11,482,412</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">135,755,200</td>
<td align="right">35,745,760</td>
<td align="right">-73.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,358,831</td>
<td align="right">14,316,313</td>
<td align="right">71.3%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">142,537,682</td>
<td align="right">43,931,982</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,714,481</td>
<td align="right">23,427,361</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">4,628,872</td>
<td align="right">7,663,898</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">909,566,726</td>
<td align="right">1,480,572,030</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">295,222,464</td>
<td align="right">124,175,061</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">232,167,863</td>
<td align="right">100,508,619</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">118,777,231</td>
<td align="right">52,262,048</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">76,350,505</td>
<td align="right">116,254,707</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,806,492</td>
<td align="right">109,974,394</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">378,234,226</td>
<td align="right">570,592,916</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">773,918,108</td>
<td align="right">381,450,400</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">42,433,744</td>
<td align="right">63,403,217</td>
<td align="right">49.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">276,486,064</td>
<td align="right">405,233,621</td>
<td align="right">46.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">137,986,057</td>
<td align="right">73,875,174</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">666,613,584</td>
<td align="right">371,090,432</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">20,333,898</td>
<td align="right">11,400,248</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,379,981,938</td>
<td align="right">6,194,511,836</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,815,465</td>
<td align="right">57,715,784</td>
<td align="right">41.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">298,257,057</td>
<td align="right">196,820,114</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,525,894,943</td>
<td align="right">2,418,242,684</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">901,623,105</td>
<td align="right">634,787,141</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">679,740,125</td>
<td align="right">878,880,179</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">328,729,288</td>
<td align="right">235,478,280</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">639,895,780</td>
<td align="right">469,838,689</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,131,545,491</td>
<td align="right">832,301,888</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">739,557,058</td>
<td align="right">557,527,078</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">108,591,623</td>
<td align="right">134,564,338</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,641,548</td>
<td align="right">174,427,570</td>
<td align="right">-22.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">56,521,715</td>
<td align="right">44,256,297</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,994,682,805</td>
<td align="right">4,720,806,205</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">211,271,082</td>
<td align="right">254,848,324</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,388,590</td>
<td align="right">8,420,264</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">677,179,245</td>
<td align="right">557,077,097</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,399,952,069</td>
<td align="right">1,993,850,213</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,297,198,388</td>
<td align="right">2,749,569,225</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,553,696</td>
<td align="right">39,665,784</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">386,366,035</td>
<td align="right">324,114,828</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">386,026,172</td>
<td align="right">325,469,590</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">486,461,360</td>
<td align="right">410,208,991</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,664,658,668</td>
<td align="right">4,784,990,341</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">35,531,143</td>
<td align="right">30,125,833</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">162,539,697</td>
<td align="right">139,220,847</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,370</td>
<td align="right">216,041,098</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">6,221,206,810</td>
<td align="right">5,378,376,112</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,850,391</td>
<td align="right">61,079,619</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,866,838</td>
<td align="right">349,970,415</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">202,175,486</td>
<td align="right">228,410,946</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">318,041,043</td>
<td align="right">279,889,533</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">100,343,428</td>
<td align="right">88,951,381</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">409,215,349</td>
<td align="right">454,966,967</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,641,404</td>
<td align="right">3,242,720</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">31,808,501</td>
<td align="right">35,012,441</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">366,806,199</td>
<td align="right">403,725,913</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,819,086,892</td>
<td align="right">2,540,969,225</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,297,524</td>
<td align="right">236,600,016</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">62,247,604</td>
<td align="right">56,631,480</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">404,538,568</td>
<td align="right">439,215,382</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">21,175,493</td>
<td align="right">19,402,256</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">215,047,513</td>
<td align="right">197,180,232</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,413,070</td>
<td align="right">4,048,842</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,099,631,443</td>
<td align="right">3,766,667,305</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">942,147,494</td>
<td align="right">866,383,108</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,016,823,533</td>
<td align="right">1,098,426,431</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">199,228,081</td>
<td align="right">183,503,952</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,569,390</td>
<td align="right">170,306,794</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,255,226,069</td>
<td align="right">1,347,370,692</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">332,019,365</td>
<td align="right">355,927,332</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">385,034,485</td>
<td align="right">358,572,307</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">791,279,079</td>
<td align="right">844,037,625</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,489,307,295</td>
<td align="right">5,128,825,145</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,644,661,655</td>
<td align="right">2,477,074,111</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,284,882</td>
<td align="right">86,439,205</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">46,620</td>
<td align="right">49,520</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">205,889,302</td>
<td align="right">218,145,532</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,913,460</td>
<td align="right">141,047,993</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">557,041,358</td>
<td align="right">527,424,730</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">198,605,843</td>
<td align="right">188,124,721</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,450,734,258</td>
<td align="right">2,322,055,986</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">283,353,267</td>
<td align="right">269,095,289</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">146,465,249</td>
<td align="right">139,472,160</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">59,137,415</td>
<td align="right">56,329,887</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">194,483,450</td>
<td align="right">203,521,974</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,411,795,175</td>
<td align="right">1,347,491,872</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,563,364,277</td>
<td align="right">1,634,140,442</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">66,763,224</td>
<td align="right">63,819,174</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,591,861</td>
<td align="right">119,332,656</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">49,209,196</td>
<td align="right">47,215,745</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,175,821</td>
<td align="right">86,521,296</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">79,279,731</td>
<td align="right">76,109,073</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">804,949,290</td>
<td align="right">772,847,751</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">66,953,717</td>
<td align="right">64,335,656</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">231,221,819</td>
<td align="right">222,726,699</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">108,507,080</td>
<td align="right">104,619,340</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">173,188,542</td>
<td align="right">166,990,341</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,882,803</td>
<td align="right">78,955,613</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">828,544,752</td>
<td align="right">801,748,591</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,607</td>
<td align="right">1,815,306</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,473,436</td>
<td align="right">16,946,592</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">431,589,715</td>
<td align="right">418,684,340</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,290,129,139</td>
<td align="right">1,323,316,262</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,221,949,971</td>
<td align="right">4,312,526,275</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">140,536,584</td>
<td align="right">137,708,649</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">222,836</td>
<td align="right">218,813</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">657,740</td>
<td align="right">646,520</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">453,756,955</td>
<td align="right">447,407,687</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,105,988,808</td>
<td align="right">4,065,045,333</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,240</td>
<td align="right">3,432,760</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,461,660</td>
<td align="right">7,526,420</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">166,866,129</td>
<td align="right">168,225,859</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,110,576,413</td>
<td align="right">1,101,853,985</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,366,385</td>
<td align="right">1,055,345,956</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">714,120</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">349,280,434</td>
<td align="right">351,818,422</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">114,868,113</td>
<td align="right">114,177,602</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,877,652</td>
<td align="right">9,823,360</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">81,682,686</td>
<td align="right">82,102,159</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">87,803,224</td>
<td align="right">87,423,241</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">30,785,345</td>
<td align="right">30,910,923</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">21,580,514,118</td>
<td align="right">21,654,119,556</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,142,187</td>
<td align="right">90,842,982</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">421,589,954</td>
<td align="right">420,311,657</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,165,100</td>
<td align="right">91,941,340</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,446,940</td>
<td align="right">94,223,180</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">59,677,580</td>
<td align="right">59,608,358</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">228,048,203</td>
<td align="right">227,801,449</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,371,141,239</td>
<td align="right">1,370,148,132</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,603,447,253</td>
<td align="right">1,602,319,659</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">485,135,654</td>
<td align="right">484,912,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,872,175,209</td>
<td align="right">1,871,664,830</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">14,885</td>
<td align="right">14,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,739</td>
<td align="right">687,850</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">272,719,008</td>
<td align="right">272,676,163</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,152,899</td>
<td align="right">21,150,768</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,694,461</td>
<td align="right">20,696,337</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,160,659</td>
<td align="right">21,162,288</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,808,204</td>
<td align="right">1,808,114</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">12,102,480</td>
<td align="right">12,102,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,658,065</td>
<td align="right">9,658,243</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,236,148</td>
<td align="right">9,236,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,344,783</td>
<td align="right">20,344,635</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,950,730</td>
<td align="right">5,950,766</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,301,355</td>
<td align="right">274,302,967</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,907,353</td>
<td align="right">555,908,643</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,338,342</td>
<td align="right">233,338,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,319,328</td>
<td align="right">173,319,334</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,220,562</td>
<td align="right">786,220,577</td>
<td align="right">0.0%</td>
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
<td align="left">CLEANUP_THROW</td>
<td align="right">150,560</td>
<td align="right">150,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">142,240</td>
<td align="right">142,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,640</td>
<td align="right">91,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">89,960</td>
<td align="right">89,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">28,760</td>
<td align="right">28,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,180</td>
<td align="right">27,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,340</td>
<td align="right">21,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">1,120</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,040</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">720</td>
<td align="right">720</td>
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
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">OPTIMIZE</td>
<td align="right"></td>
<td align="right">1,587,517,761</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,500,920</td>
<td align="right">0.3%</td>
<td align="right">47,777,940</td>
<td align="right">0.5%</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">436,996,138</td>
<td align="right">4.4%</td>
<td align="right">500,421,949</td>
<td align="right">5.0%</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,428,336,550</td>
<td align="right">95.6%</td>
<td align="right">9,452,860,123</td>
<td align="right">95.0%</td>
<td align="right">0.3%</td>
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
<td align="right">597,624</td>
<td align="right">34.7%</td>
<td align="right">942,554</td>
<td align="right">40.6%</td>
<td align="right">57.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,122,507</td>
<td align="right">65.3%</td>
<td align="right">1,380,404</td>
<td align="right">59.4%</td>
<td align="right">23.0%</td>
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
<td align="right">48,680</td>
<td align="right">4.3%</td>
<td align="right">154,110</td>
<td align="right">11.2%</td>
<td align="right">216.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,407</td>
<td align="right">7.3%</td>
<td align="right">248,092</td>
<td align="right">18.0%</td>
<td align="right">201.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,026</td>
<td align="right">0.4%</td>
<td align="right">9,831</td>
<td align="right">0.7%</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,610</td>
<td align="right">0.8%</td>
<td align="right">10,687</td>
<td align="right">0.8%</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,504</td>
<td align="right">0.9%</td>
<td align="right">8,713</td>
<td align="right">0.6%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,240</td>
<td align="right">0.2%</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">0.9%</td>
<td align="right">9,620</td>
<td align="right">0.7%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,884</td>
<td align="right">0.8%</td>
<td align="right">8,167</td>
<td align="right">0.6%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">13,626</td>
<td align="right">1.2%</td>
<td align="right">12,570</td>
<td align="right">0.9%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">4,427</td>
<td align="right">0.3%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,385</td>
<td align="right">2.9%</td>
<td align="right">31,203</td>
<td align="right">2.3%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,760</td>
<td align="right">0.2%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,606</td>
<td align="right">69.6%</td>
<td align="right">767,449</td>
<td align="right">55.6%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,266</td>
<td align="right">2.8%</td>
<td align="right">31,769</td>
<td align="right">2.3%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,548</td>
<td align="right">0.5%</td>
<td align="right">5,469</td>
<td align="right">0.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">22,628</td>
<td align="right">2.0%</td>
<td align="right">22,452</td>
<td align="right">1.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,318</td>
<td align="right">4.3%</td>
<td align="right">48,526</td>
<td align="right">3.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,915</td>
<td align="right">0.2%</td>
<td align="right">1,919</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
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
<td align="right">743,945,445</td>
<td align="right">10.8%</td>
<td align="right">561,973,903</td>
<td align="right">8.2%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,149,810,038</td>
<td align="right">89.2%</td>
<td align="right">6,276,814,585</td>
<td align="right">91.8%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,810,117</td>
<td align="right">0.1%</td>
<td align="right">4,818,429</td>
<td align="right">0.1%</td>
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
<td align="left">Failure</td>
<td align="right">240,169</td>
<td align="right">56.9%</td>
<td align="right">190,027</td>
<td align="right">51.1%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,561</td>
<td align="right">43.1%</td>
<td align="right">181,577</td>
<td align="right">48.9%</td>
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
<td align="right">16,200</td>
<td align="right">6.7%</td>
<td align="right">36,920</td>
<td align="right">19.4%</td>
<td align="right">127.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">110,406</td>
<td align="right">46.0%</td>
<td align="right">51,420</td>
<td align="right">27.1%</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">880</td>
<td align="right">0.4%</td>
<td align="right">700</td>
<td align="right">0.4%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">55,960</td>
<td align="right">23.3%</td>
<td align="right">46,420</td>
<td align="right">24.4%</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,160</td>
<td align="right">0.5%</td>
<td align="right">1,020</td>
<td align="right">0.5%</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,499</td>
<td align="right">12.7%</td>
<td align="right">28,600</td>
<td align="right">15.1%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">127</td>
<td align="right">0.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.2%</td>
<td align="right">5,220</td>
<td align="right">2.7%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,500</td>
<td align="right">8.1%</td>
<td align="right">19,500</td>
<td align="right">10.3%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">19,400</td>
<td align="right">0.0%</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">181,480,777</td>
<td align="right">1.3%</td>
<td align="right">164,013,813</td>
<td align="right">1.1%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">662,503,918</td>
<td align="right">4.6%</td>
<td align="right">645,143,677</td>
<td align="right">4.5%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,665,827,683</td>
<td align="right">95.3%</td>
<td align="right">13,657,229,470</td>
<td align="right">95.5%</td>
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
<td align="right">3,947,091</td>
<td align="right">96.0%</td>
<td align="right">3,617,702</td>
<td align="right">95.6%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">165,422</td>
<td align="right">4.0%</td>
<td align="right">165,322</td>
<td align="right">4.4%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">155,922</td>
<td align="right">94.3%</td>
<td align="right">155,822</td>
<td align="right">94.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">9,160</td>
<td align="right">5.5%</td>
<td align="right">9,160</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,920</td>
<td align="right">1.8%</td>
<td align="right">2,920</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">1,940</td>
<td align="right">1.2%</td>
<td align="right">1,940</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">940</td>
<td align="right">0.6%</td>
<td align="right">940</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
<td align="right">0.2%</td>
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
<td align="right">1,069,647</td>
<td align="right">0.0%</td>
<td align="right">906,210</td>
<td align="right">0.0%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">101,187,315</td>
<td align="right">1.6%</td>
<td align="right">89,651,148</td>
<td align="right">1.4%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,122,641,512</td>
<td align="right">98.4%</td>
<td align="right">6,105,129,402</td>
<td align="right">98.5%</td>
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
<td align="right">149,613</td>
<td align="right">66.3%</td>
<td align="right">133,390</td>
<td align="right">64.6%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">76,147</td>
<td align="right">33.7%</td>
<td align="right">73,053</td>
<td align="right">35.4%</td>
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
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.1%</td>
<td align="right">1,140</td>
<td align="right">0.9%</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,620</td>
<td align="right">1.1%</td>
<td align="right">880</td>
<td align="right">0.7%</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">560</td>
<td align="right">0.4%</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,375</td>
<td align="right">9.6%</td>
<td align="right">11,344</td>
<td align="right">8.5%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,060</td>
<td align="right">18.1%</td>
<td align="right">22,400</td>
<td align="right">16.8%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,000</td>
<td align="right">12.7%</td>
<td align="right">16,760</td>
<td align="right">12.6%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,424</td>
<td align="right">1.0%</td>
<td align="right">1,285</td>
<td align="right">1.0%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,703</td>
<td align="right">11.2%</td>
<td align="right">18,193</td>
<td align="right">13.6%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">42,443</td>
<td align="right">28.4%</td>
<td align="right">45,868</td>
<td align="right">34.4%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.4%</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,188</td>
<td align="right">8.1%</td>
<td align="right">11,840</td>
<td align="right">8.9%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,580</td>
<td align="right">1.7%</td>
<td align="right">2,580</td>
<td align="right">1.9%</td>
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
<td align="right">208,260,694</td>
<td align="right">7.7%</td>
<td align="right">220,487,659</td>
<td align="right">8.3%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,489,651,066</td>
<td align="right">92.3%</td>
<td align="right">2,433,294,000</td>
<td align="right">91.7%</td>
<td align="right">-2.3%</td>
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
<td align="right">2,513,020</td>
<td align="right">0.1%</td>
<td align="right">-1.3%</td>
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
<td align="right">113,728</td>
<td align="right">65.0%</td>
<td align="right">110,453</td>
<td align="right">64.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,120</td>
<td align="right">35.0%</td>
<td align="right">60,440</td>
<td align="right">35.4%</td>
<td align="right">-1.1%</td>
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
<td align="right">13,940</td>
<td align="right">12.3%</td>
<td align="right">12,420</td>
<td align="right">11.2%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,518</td>
<td align="right">24.2%</td>
<td align="right">25,040</td>
<td align="right">22.7%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,730</td>
<td align="right">13.8%</td>
<td align="right">14,713</td>
<td align="right">13.3%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">56,540</td>
<td align="right">49.7%</td>
<td align="right">58,280</td>
<td align="right">52.8%</td>
<td align="right">3.1%</td>
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
<td align="right">483,787,769</td>
<td align="right">46.9%</td>
<td align="right">734,056</td>
<td align="right">0.3%</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,588,403</td>
<td align="right">0.3%</td>
<td align="right">38,060</td>
<td align="right">0.0%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">547,133,422</td>
<td align="right">53.1%</td>
<td align="right">216,588,385</td>
<td align="right">99.6%</td>
<td align="right">-60.4%</td>
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
<td align="right">196,985</td>
<td align="right">67.1%</td>
<td align="right">43,960</td>
<td align="right">47.5%</td>
<td align="right">-77.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">96,568</td>
<td align="right">32.9%</td>
<td align="right">48,574</td>
<td align="right">52.5%</td>
<td align="right">-49.7%</td>
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
<td align="right">104,960</td>
<td align="right">53.3%</td>
<td align="right">2,980</td>
<td align="right">6.8%</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">4,060</td>
<td align="right">2.1%</td>
<td align="right">1,260</td>
<td align="right">2.9%</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3,840</td>
<td align="right">1.9%</td>
<td align="right">1,440</td>
<td align="right">3.3%</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,252</td>
<td align="right">5.2%</td>
<td align="right">3,940</td>
<td align="right">9.0%</td>
<td align="right">-61.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,480</td>
<td align="right">3.3%</td>
<td align="right">2,660</td>
<td align="right">6.1%</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">37,173</td>
<td align="right">18.9%</td>
<td align="right">15,920</td>
<td align="right">36.2%</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,300</td>
<td align="right">3.2%</td>
<td align="right">2,820</td>
<td align="right">6.4%</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,100</td>
<td align="right">2.6%</td>
<td align="right">2,460</td>
<td align="right">5.6%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,720</td>
<td align="right">0.9%</td>
<td align="right">840</td>
<td align="right">1.9%</td>
<td align="right">-51.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,285</td>
<td align="right">5.7%</td>
<td align="right">6,020</td>
<td align="right">13.7%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">120</td>
<td align="right">0.3%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,220</td>
<td align="right">2.1%</td>
<td align="right">2,400</td>
<td align="right">5.5%</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">580</td>
<td align="right">1.3%</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">615</td>
<td align="right">0.3%</td>
<td align="right">520</td>
<td align="right">1.2%</td>
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
<td align="right">420,250,038</td>
<td align="right">2.4%</td>
<td align="right">531,517,861</td>
<td align="right">3.0%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,521,315,006</td>
<td align="right">8.6%</td>
<td align="right">1,621,893,051</td>
<td align="right">9.0%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">16,088,194,391</td>
<td align="right">91.3%</td>
<td align="right">16,317,368,900</td>
<td align="right">90.9%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">263,380</td>
<td align="right">0.0%</td>
<td align="right">261,280</td>
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
<td align="right">8,539,421</td>
<td align="right">89.8%</td>
<td align="right">10,639,467</td>
<td align="right">92.7%</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">972,024</td>
<td align="right">10.2%</td>
<td align="right">839,328</td>
<td align="right">7.3%</td>
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
<td align="left">class attr simple</td>
<td align="right">156,280</td>
<td align="right">16.1%</td>
<td align="right">49,372</td>
<td align="right">5.9%</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,840</td>
<td align="right">0.3%</td>
<td align="right">2,141</td>
<td align="right">0.3%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,360</td>
<td align="right">1.5%</td>
<td align="right">17,640</td>
<td align="right">2.1%</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,638</td>
<td align="right">9.0%</td>
<td align="right">80,527</td>
<td align="right">9.6%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,570</td>
<td align="right">0.6%</td>
<td align="right">5,190</td>
<td align="right">0.6%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">263,066</td>
<td align="right">27.1%</td>
<td align="right">246,948</td>
<td align="right">29.4%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">340</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,880</td>
<td align="right">2.8%</td>
<td align="right">25,520</td>
<td align="right">3.0%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,340</td>
<td align="right">2.1%</td>
<td align="right">19,560</td>
<td align="right">2.3%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,400</td>
<td align="right">0.6%</td>
<td align="right">5,600</td>
<td align="right">0.7%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">102,064</td>
<td align="right">10.5%</td>
<td align="right">100,843</td>
<td align="right">12.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">164,774</td>
<td align="right">17.0%</td>
<td align="right">163,236</td>
<td align="right">19.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,749</td>
<td align="right">1.8%</td>
<td align="right">17,900</td>
<td align="right">2.1%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,300</td>
<td align="right">1.6%</td>
<td align="right">15,420</td>
<td align="right">1.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.3%</td>
<td align="right">12,160</td>
<td align="right">1.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">75,343</td>
<td align="right">7.8%</td>
<td align="right">75,091</td>
<td align="right">8.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
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
<td align="right">5,849,260,284</td>
<td align="right">99.6%</td>
<td align="right">5,181,023,290</td>
<td align="right">99.6%</td>
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
<td align="right">439,085</td>
<td align="right">0.0%</td>
<td align="right">438,121</td>
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
<td align="right">20,321,197</td>
<td align="right">0.3%</td>
<td align="right">20,320,234</td>
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
<td align="right">11,640</td>
<td align="right">0.0%</td>
<td align="right">11,640</td>
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
<td align="right">462,671</td>
<td align="right">100.0%</td>
<td align="right">462,522</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,465</td>
<td align="right">0.0%</td>
<td align="right">7,469</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,720,927</td>
<td align="right">100.0%</td>
<td align="right">83,735,494</td>
<td align="right">100.0%</td>
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
<td align="right">7,420</td>
<td align="right">100.0%</td>
<td align="right">7,420</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,284,908</td>
<td align="right">18.1%</td>
<td align="right">173,284,914</td>
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
<td align="right">786,189,902</td>
<td align="right">81.9%</td>
<td align="right">786,189,917</td>
<td align="right">81.9%</td>
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
<td align="right">5,460</td>
<td align="right">8.4%</td>
<td align="right">5,460</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,620</td>
<td align="right">91.6%</td>
<td align="right">59,620</td>
<td align="right">91.6%</td>
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
<td align="left">list</td>
<td align="right">9,980</td>
<td align="right">16.7%</td>
<td align="right">9,980</td>
<td align="right">16.7%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">190,480,747</td>
<td align="right">6.5%</td>
<td align="right">198,680,319</td>
<td align="right">6.8%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">139,449,178</td>
<td align="right">4.8%</td>
<td align="right">140,438,970</td>
<td align="right">4.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,724,885,653</td>
<td align="right">93.4%</td>
<td align="right">2,728,670,725</td>
<td align="right">93.1%</td>
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
<td align="right">92,028</td>
<td align="right">3.3%</td>
<td align="right">92,854</td>
<td align="right">3.3%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,726,794</td>
<td align="right">96.7%</td>
<td align="right">2,745,416</td>
<td align="right">96.7%</td>
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
<td align="left">property</td>
<td align="right">2,860</td>
<td align="right">3.1%</td>
<td align="right">3,180</td>
<td align="right">3.4%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,760</td>
<td align="right">9.5%</td>
<td align="right">8,240</td>
<td align="right">8.9%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">32,280</td>
<td align="right">35.1%</td>
<td align="right">33,560</td>
<td align="right">36.1%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,480</td>
<td align="right">8.1%</td>
<td align="right">7,380</td>
<td align="right">7.9%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,780</td>
<td align="right">5.2%</td>
<td align="right">4,740</td>
<td align="right">5.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,960</td>
<td align="right">15.2%</td>
<td align="right">13,860</td>
<td align="right">14.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,940</td>
<td align="right">5.4%</td>
<td align="right">4,920</td>
<td align="right">5.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,728</td>
<td align="right">10.6%</td>
<td align="right">9,734</td>
<td align="right">10.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,320</td>
<td align="right">6.9%</td>
<td align="right">6,320</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">800</td>
<td align="right">0.9%</td>
<td align="right">800</td>
<td align="right">0.9%</td>
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
<td align="right">0.0%</td>
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
<td align="right">232,057,895</td>
<td align="right">20.9%</td>
<td align="right">100,432,792</td>
<td align="right">10.3%</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">877,148,872</td>
<td align="right">79.1%</td>
<td align="right">875,240,879</td>
<td align="right">89.7%</td>
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
<td align="right">99,966</td>
<td align="right">88.6%</td>
<td align="right">65,863</td>
<td align="right">83.7%</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,902</td>
<td align="right">11.4%</td>
<td align="right">12,864</td>
<td align="right">16.3%</td>
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
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">6.5%</td>
<td align="right">14,560</td>
<td align="right">22.1%</td>
<td align="right">124.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,420</td>
<td align="right">43.4%</td>
<td align="right">440</td>
<td align="right">0.7%</td>
<td align="right">-99.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,340</td>
<td align="right">1.3%</td>
<td align="right">920</td>
<td align="right">1.4%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,526</td>
<td align="right">7.5%</td>
<td align="right">6,983</td>
<td align="right">10.6%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,480</td>
<td align="right">1.5%</td>
<td align="right">1,380</td>
<td align="right">2.1%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">39,720</td>
<td align="right">39.7%</td>
<td align="right">41,580</td>
<td align="right">63.1%</td>
<td align="right">4.7%</td>
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
<td align="right">55,396,243</td>
<td align="right">0.9%</td>
<td align="right">34,503,692</td>
<td align="right">0.5%</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">248,285,288</td>
<td align="right">3.9%</td>
<td align="right">236,667,733</td>
<td align="right">3.7%</td>
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
<td align="right">6,101,764,761</td>
<td align="right">96.1%</td>
<td align="right">6,169,436,618</td>
<td align="right">96.3%</td>
<td align="right">1.1%</td>
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
<td align="right">356,093</td>
<td align="right">22.3%</td>
<td align="right">513,464</td>
<td align="right">37.8%</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,238,312</td>
<td align="right">77.7%</td>
<td align="right">844,469</td>
<td align="right">62.2%</td>
<td align="right">-31.8%</td>
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
<td align="right">5,145</td>
<td align="right">1.4%</td>
<td align="right">135,844</td>
<td align="right">26.5%</td>
<td align="right">2,540.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12,779</td>
<td align="right">3.6%</td>
<td align="right">7,413</td>
<td align="right">1.4%</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,237</td>
<td align="right">3.7%</td>
<td align="right">18,492</td>
<td align="right">3.6%</td>
<td align="right">39.7%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.3%</td>
<td align="right">640</td>
<td align="right">0.1%</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">135,496</td>
<td align="right">38.1%</td>
<td align="right">164,983</td>
<td align="right">32.1%</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,020</td>
<td align="right">4.2%</td>
<td align="right">17,540</td>
<td align="right">3.4%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">35,068</td>
<td align="right">9.8%</td>
<td align="right">31,238</td>
<td align="right">6.1%</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">55,260</td>
<td align="right">15.5%</td>
<td align="right">54,038</td>
<td align="right">10.5%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,168</td>
<td align="right">22.8%</td>
<td align="right">81,396</td>
<td align="right">15.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.4%</td>
<td align="right">1,460</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">420</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">1,060</td>
<td align="right">0.0%</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">194,005</td>
<td align="right">0.0%</td>
<td align="right">188,369</td>
<td align="right">0.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,558,785,707</td>
<td align="right">100.0%</td>
<td align="right">1,557,774,624</td>
<td align="right">100.0%</td>
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
<td align="right">1,855</td>
<td align="right">5.8%</td>
<td align="right">1,640</td>
<td align="right">5.2%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,056</td>
<td align="right">94.2%</td>
<td align="right">29,864</td>
<td align="right">94.8%</td>
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
<td align="left">sequence</td>
<td align="right">1,215</td>
<td align="right">65.5%</td>
<td align="right">1,000</td>
<td align="right">61.0%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">20.5%</td>
<td align="right">380</td>
<td align="right">23.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.0%</td>
<td align="right">260</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">915,465,077</td>
<td align="right">0.7%</td>
<td align="right">1,004,897,993</td>
<td align="right">0.8%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">66,989,118,843</td>
<td align="right">54.8%</td>
<td align="right">61,043,206,102</td>
<td align="right">50.7%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">42,687,434,008</td>
<td align="right">34.9%</td>
<td align="right">46,022,692,315</td>
<td align="right">38.2%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,721,029,980</td>
<td align="right">9.6%</td>
<td align="right">12,288,965,252</td>
<td align="right">10.2%</td>
<td align="right">4.8%</td>
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
<td align="right">232,057,895</td>
<td align="right">4.6%</td>
<td align="right">100,432,792</td>
<td align="right">2.3%</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">743,945,445</td>
<td align="right">14.8%</td>
<td align="right">561,973,903</td>
<td align="right">12.9%</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">436,996,138</td>
<td align="right">8.7%</td>
<td align="right">500,421,949</td>
<td align="right">11.5%</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,521,315,006</td>
<td align="right">30.3%</td>
<td align="right">1,621,893,051</td>
<td align="right">37.1%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">208,260,694</td>
<td align="right">4.1%</td>
<td align="right">220,487,659</td>
<td align="right">5.0%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">248,285,288</td>
<td align="right">4.9%</td>
<td align="right">236,667,733</td>
<td align="right">5.4%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">190,480,747</td>
<td align="right">3.8%</td>
<td align="right">198,680,319</td>
<td align="right">4.5%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">662,503,918</td>
<td align="right">13.2%</td>
<td align="right">645,143,677</td>
<td align="right">14.8%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,908</td>
<td align="right">3.5%</td>
<td align="right">173,284,914</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">483,787,769</td>
<td align="right">9.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">89,651,148</td>
<td align="right">2.1%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,549,216</td>
<td align="right">3.6%</td>
<td align="right">61,228,596</td>
<td align="right">5.7%</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">58,791,367</td>
<td align="right">5.9%</td>
<td align="right">90,417,391</td>
<td align="right">8.4%</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">172,481,741</td>
<td align="right">17.4%</td>
<td align="right">211,571,602</td>
<td align="right">19.5%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">98,362,398</td>
<td align="right">9.9%</td>
<td align="right">85,938,081</td>
<td align="right">7.9%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">125,829,008</td>
<td align="right">12.7%</td>
<td align="right">129,655,007</td>
<td align="right">12.0%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">114,234,100</td>
<td align="right">11.5%</td>
<td align="right">114,147,683</td>
<td align="right">10.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,508</td>
<td align="right">2.8%</td>
<td align="right">27,496,816</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,897,789</td>
<td align="right">7.8%</td>
<td align="right">77,897,257</td>
<td align="right">7.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,897,789</td>
<td align="right">7.8%</td>
<td align="right">77,897,257</td>
<td align="right">7.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,365,670</td>
<td align="right">2.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">26,267,867</td>
<td align="right">2.4%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">550,011,420</td>
<td align="right">6.3%</td>
<td align="right">409,034,904</td>
<td align="right">4.7%</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,783,963,981</td>
<td align="right">20.5%</td>
<td align="right">1,625,215,644</td>
<td align="right">18.7%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,788,410,421</td>
<td align="right">20.5%</td>
<td align="right">1,629,662,084</td>
<td align="right">18.7%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,648,977,964</td>
<td align="right">30.4%</td>
<td align="right">2,480,522,141</td>
<td align="right">28.5%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,648,977,964</td>
<td align="right">30.4%</td>
<td align="right">2,480,522,141</td>
<td align="right">28.5%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">348,464,228</td>
<td align="right">4.0%</td>
<td align="right">330,689,595</td>
<td align="right">3.8%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,064,292,819</td>
<td align="right">69.6%</td>
<td align="right">6,217,076,372</td>
<td align="right">71.5%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,567,543</td>
<td align="right">9.9%</td>
<td align="right">850,860,057</td>
<td align="right">9.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,401,244</td>
<td align="right">1.0%</td>
<td align="right">83,726,033</td>
<td align="right">1.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,954,292,757</td>
<td align="right">79.8%</td>
<td align="right">6,939,788,977</td>
<td align="right">79.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,271</td>
<td align="right">2.0%</td>
<td align="right">175,480,597</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,015,253</td>
<td align="right">0.4%</td>
<td align="right">31,015,302</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,417,680</td>
<td align="right">0.1%</td>
<td align="right">4,417,680</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">28,760</td>
<td align="right">0.0%</td>
<td align="right">28,760</td>
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
<td align="left">Method cache hits</td>
<td align="right">3,237,638,376</td>
<td align="right"></td>
<td align="right">2,858,916,000</td>
<td align="right"></td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">90,338,233,069</td>
<td align="right">62.8%</td>
<td align="right">100,487,339,492</td>
<td align="right">65.2%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">94,431,359,712</td>
<td align="right">56.7%</td>
<td align="right">104,959,076,907</td>
<td align="right">59.3%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">10,918,390</td>
<td align="right"></td>
<td align="right">10,017,095</td>
<td align="right"></td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,569,681,461</td>
<td align="right"></td>
<td align="right">4,413,560,546</td>
<td align="right"></td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">61,812,756</td>
<td align="right"></td>
<td align="right">59,909,715</td>
<td align="right"></td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">54,207,586</td>
<td align="right"></td>
<td align="right">53,204,024</td>
<td align="right"></td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">94,091,431</td>
<td align="right">0.4%</td>
<td align="right">93,427,377</td>
<td align="right">0.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">14,848,228</td>
<td align="right">0.1%</td>
<td align="right">14,772,572</td>
<td align="right">0.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">53,429,990,693</td>
<td align="right">37.2%</td>
<td align="right">53,627,903,314</td>
<td align="right">34.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">72,153,947,970</td>
<td align="right">43.3%</td>
<td align="right">71,947,892,764</td>
<td align="right">40.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,823,546,309</td>
<td align="right">55.7%</td>
<td align="right">12,802,947,747</td>
<td align="right">55.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,714,606,650</td>
<td align="right">55.2%</td>
<td align="right">12,694,747,798</td>
<td align="right">55.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,527,829,810</td>
<td align="right"></td>
<td align="right">13,507,097,634</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,131,266</td>
<td align="right"></td>
<td align="right">161,907,492</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,206,533,082</td>
<td align="right">44.3%</td>
<td align="right">10,198,422,869</td>
<td align="right">44.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,208,402,135</td>
<td align="right"></td>
<td align="right">10,200,304,549</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,305,720</td>
<td align="right">2.0%</td>
<td align="right">3,305,720</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">114,680</td>
<td align="right">0.1%</td>
<td align="right">114,680</td>
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
<td align="right">115,238,760</td>
<td align="right">19,145,187,803</td>
<td align="right">0</td>
<td align="right">114,868,080</td>
<td align="right">19,193,355,591</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,365,028</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,970,613,548</td>
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
<td align="right">125,516</td>
<td align="right">10.2%</td>
<td align="right">1,580,691</td>
<td align="right">44.9%</td>
<td align="right">1,159.4%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">50,467</td>
<td align="right">4.1%</td>
<td align="right">613,885</td>
<td align="right">17.4%</td>
<td align="right">1,116.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,224,837</td>
<td align="right"></td>
<td align="right">3,523,419</td>
<td align="right"></td>
<td align="right">187.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">496,328</td>
<td align="right">40.5%</td>
<td align="right">1,278,354</td>
<td align="right">36.3%</td>
<td align="right">157.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,663,392,854</td>
<td align="right"></td>
<td align="right">16,954,894,761</td>
<td align="right"></td>
<td align="right">121.2%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,720</td>
<td align="right">0.1%</td>
<td align="right">3,380</td>
<td align="right">0.1%</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,099,321</td>
<td align="right">89.8%</td>
<td align="right">1,942,728</td>
<td align="right">55.1%</td>
<td align="right">76.7%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,339</td>
<td align="right">0.1%</td>
<td align="right">683</td>
<td align="right">0.0%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">160</td>
<td align="right">0.0%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">249,966,105,973</td>
<td align="right">3,261.8%</td>
<td align="right">284,855,958,997</td>
<td align="right">1,680.1%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,359</td>
<td align="right">5.1%</td>
<td align="right">7,093</td>
<td align="right">0.4%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">12,581</td>
<td align="right">1.0%</td>
<td align="right">13,484</td>
<td align="right">0.4%</td>
<td align="right">7.2%</td>
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
<td align="right">110,723</td>
<td align="right">88.2%</td>
<td align="right">1,559,103</td>
<td align="right">98.6%</td>
<td align="right">1,308.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">125,516</td>
<td align="right"></td>
<td align="right">1,580,691</td>
<td align="right"></td>
<td align="right">1,159.4%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,447</td>
<td align="right">1.9%</td>
<td align="right">1,192</td>
<td align="right">0.1%</td>
<td align="right">-51.3%</td>
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
<td align="right">5,310</td>
<td align="right">4.2%</td>
<td align="right">92,293</td>
<td align="right">5.8%</td>
<td align="right">1,638.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,492</td>
<td align="right">17.1%</td>
<td align="right">363,755</td>
<td align="right">23.0%</td>
<td align="right">1,592.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,069</td>
<td align="right">27.9%</td>
<td align="right">499,524</td>
<td align="right">31.6%</td>
<td align="right">1,324.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">30,950</td>
<td align="right">24.7%</td>
<td align="right">546,710</td>
<td align="right">34.6%</td>
<td align="right">1,666.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21,164</td>
<td align="right">16.9%</td>
<td align="right">61,919</td>
<td align="right">3.9%</td>
<td align="right">192.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,671</td>
<td align="right">7.7%</td>
<td align="right">14,433</td>
<td align="right">0.9%</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,700</td>
<td align="right">1.4%</td>
<td align="right">1,857</td>
<td align="right">0.1%</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
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
<td align="right">4,130</td>
<td align="right">3.3%</td>
<td align="right">85,073</td>
<td align="right">5.4%</td>
<td align="right">1,959.9%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">14,824</td>
<td align="right">11.8%</td>
<td align="right">393,619</td>
<td align="right">24.9%</td>
<td align="right">2,555.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">25,109</td>
<td align="right">20.0%</td>
<td align="right">256,275</td>
<td align="right">16.2%</td>
<td align="right">920.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">36,455</td>
<td align="right">29.0%</td>
<td align="right">684,137</td>
<td align="right">43.3%</td>
<td align="right">1,776.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">18,459</td>
<td align="right">14.7%</td>
<td align="right">101,628</td>
<td align="right">6.4%</td>
<td align="right">450.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,726</td>
<td align="right">7.0%</td>
<td align="right">34,931</td>
<td align="right">2.2%</td>
<td align="right">300.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,640</td>
<td align="right">2.1%</td>
<td align="right">3,080</td>
<td align="right">0.2%</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">380</td>
<td align="right">0.3%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">-5.3%</td>
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
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">39,840</td>
<td align="right">8,634,141</td>
<td align="right">21,572.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">2,971,767</td>
<td align="right">9,832.4%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,720</td>
<td align="right">35,951,500</td>
<td align="right">4,275.2%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,917,600</td>
<td align="right">103,481,280</td>
<td align="right">2,541.4%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">5,782,740</td>
<td align="right">103,942,680</td>
<td align="right">1,697.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">3,025,020</td>
<td align="right">51,089,260</td>
<td align="right">1,588.9%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">3,628,054</td>
<td align="right">54,842,041</td>
<td align="right">1,411.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">904,464,441</td>
<td align="right">3,783,838,641</td>
<td align="right">318.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">462,537</td>
<td align="right">1,739,126</td>
<td align="right">276.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,657,411</td>
<td align="right">224,648,319</td>
<td align="right">134.8%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,229,751</td>
<td align="right">225,424,196</td>
<td align="right">131.8%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,831,680</td>
<td align="right">142,414,760</td>
<td align="right">130.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">7,009,955,553</td>
<td align="right">15,945,679,210</td>
<td align="right">127.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,663,392,854</td>
<td align="right">16,954,894,761</td>
<td align="right">121.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,420,400,153</td>
<td align="right">2,843,557,860</td>
<td align="right">100.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,568,217,073</td>
<td align="right">1,920</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">239,745,240</td>
<td align="right">41,734</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">310,680</td>
<td align="right">5,820</td>
<td align="right">-98.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,688,754,561</td>
<td align="right">3,205,012,781</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,648,680</td>
<td align="right">655,000</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">67,775,580</td>
<td align="right">121,919,098</td>
<td align="right">79.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">214,048,243</td>
<td align="right">383,985,874</td>
<td align="right">79.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">121,960,451</td>
<td align="right">212,665,441</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">387,391,356</td>
<td align="right">673,488,363</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">30,596,970</td>
<td align="right">9,363,180</td>
<td align="right">-69.4%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,921,150</td>
<td align="right">1,577,066</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">274,617,103</td>
<td align="right">450,158,934</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,120,367,853</td>
<td align="right">10,014,872,644</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">11,627,700</td>
<td align="right">18,715,194</td>
<td align="right">61.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">2,792,220</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,401,617</td>
<td align="right">149,295,423</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">338,030,129</td>
<td align="right">162,670,861</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">11,380</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">436,044,792</td>
<td align="right">644,975,581</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">514,886,812</td>
<td align="right">749,139,501</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">59,644,340</td>
<td align="right">36,509,940</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,866,101</td>
<td align="right">44,137,879</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">317,176,897</td>
<td align="right">436,301,961</td>
<td align="right">37.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,324,919,691</td>
<td align="right">842,372,607</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,682,027</td>
<td align="right">14,569,328</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">266,225,788</td>
<td align="right">362,583,099</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">269,595,648</td>
<td align="right">175,332,330</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">270,822,908</td>
<td align="right">176,683,430</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">25,717,580</td>
<td align="right">17,201,220</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,402,306</td>
<td align="right">43,015,232</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,966,880</td>
<td align="right">3,926,660</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,025,145,254</td>
<td align="right">2,679,451,455</td>
<td align="right">32.3%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,697,060</td>
<td align="right">8,749,975</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">860,839,545</td>
<td align="right">1,127,066,226</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">140,275,385</td>
<td align="right">179,494,039</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">126,563,832</td>
<td align="right">161,944,552</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">263,534,500</td>
<td align="right">333,676,249</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,329,328,006</td>
<td align="right">1,758,396,836</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,085,626,855</td>
<td align="right">2,582,647,408</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,328,418</td>
<td align="right">2,864,804</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,098,637,956</td>
<td align="right">1,349,353,290</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,790,372,963</td>
<td align="right">2,188,969,257</td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">947,162,370</td>
<td align="right">1,157,377,170</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,718,673</td>
<td align="right">111,782,500</td>
<td align="right">21.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">394,178,764</td>
<td align="right">479,622,429</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">113,127,721</td>
<td align="right">137,387,260</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,883,903,750</td>
<td align="right">2,274,243,067</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,963,689,584</td>
<td align="right">2,370,027,787</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">643,762,866</td>
<td align="right">775,427,659</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,322,509,992</td>
<td align="right">1,588,430,423</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,301,791,792</td>
<td align="right">1,562,245,732</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">321,336,639</td>
<td align="right">385,448,175</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,189,408,152</td>
<td align="right">1,423,875,045</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,027,078,726</td>
<td align="right">826,086,664</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">658,563,732</td>
<td align="right">784,870,226</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,511,445</td>
<td align="right">2,050,939</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,576,454,735</td>
<td align="right">1,864,586,464</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">47,971,803</td>
<td align="right">56,614,640</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,746,465,696</td>
<td align="right">3,241,255,405</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,013,560</td>
<td align="right">628,665,800</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">64,522,836</td>
<td align="right">53,009,180</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,092,173</td>
<td align="right">41,290,492</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">10,050,940</td>
<td align="right">8,359,093</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,228,648</td>
<td align="right">11,901,752</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,816,457,228</td>
<td align="right">2,109,803,901</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">651,580,315</td>
<td align="right">752,007,131</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">25,197,736</td>
<td align="right">29,072,980</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">702,316,836</td>
<td align="right">807,393,083</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">48,440,938</td>
<td align="right">41,217,400</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">800,681,643</td>
<td align="right">919,598,789</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,591,762</td>
<td align="right">13,280,974</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,591,762</td>
<td align="right">13,280,974</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,672,988</td>
<td align="right">102,368,031</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,020,261,031</td>
<td align="right">2,303,407,510</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">970,230,774</td>
<td align="right">1,103,645,975</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,258,985,067</td>
<td align="right">2,563,055,405</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">216,537,799</td>
<td align="right">245,405,232</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,165,636,393</td>
<td align="right">2,454,052,746</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">219,066,585</td>
<td align="right">247,748,652</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,997,812,905</td>
<td align="right">2,252,838,723</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,110</td>
<td align="right">117,438,605</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,194,110</td>
<td align="right">117,438,605</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,319,487,543</td>
<td align="right">2,607,975,681</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,862,100</td>
<td align="right">6,016,379</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">562,750,411</td>
<td align="right">627,652,386</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">457,489,248</td>
<td align="right">509,724,824</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">395,091,069</td>
<td align="right">350,149,533</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,619,543,737</td>
<td align="right">4,009,171,986</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,700,779</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,682,494,153</td>
<td align="right">1,849,735,079</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,824,369,759</td>
<td align="right">7,495,889,378</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,713,899</td>
<td align="right">99,581,974</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,638,101</td>
<td align="right">347,129,700</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,131,181,328</td>
<td align="right">1,240,573,667</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">164,118,930</td>
<td align="right">179,842,957</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">533,019,891</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">834,115,357</td>
<td align="right">909,457,345</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,825,999,714</td>
<td align="right">1,989,615,432</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,695,607,728</td>
<td align="right">8,831,936,427</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,508,808,218</td>
<td align="right">2,731,565,065</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,059,559,797</td>
<td align="right">965,555,420</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">893,944,320</td>
<td align="right">973,211,360</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,372,398,263</td>
<td align="right">3,668,170,106</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,682,753</td>
<td align="right">62,726,972</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">31,880</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">104,757,000</td>
<td align="right">96,193,667</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,671,620</td>
<td align="right">3,971,100</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,165,678,517</td>
<td align="right">3,421,245,153</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,491,231,004</td>
<td align="right">1,371,087,090</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">101,766,723</td>
<td align="right">109,836,200</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">81,660,980</td>
<td align="right">88,073,598</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,990,831,757</td>
<td align="right">19,401,906,042</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,152,852,636</td>
<td align="right">1,238,620,692</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">193,517,411</td>
<td align="right">180,169,451</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,841,164,960</td>
<td align="right">2,648,449,550</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,345,934,232</td>
<td align="right">1,435,701,500</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">218,973,940</td>
<td align="right">233,133,061</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">133,514,720</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">297,428,675</td>
<td align="right">278,537,165</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">407,485,821</td>
<td align="right">433,156,557</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">81,529,700</td>
<td align="right">86,628,971</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,580,260</td>
<td align="right">91,988,567</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,701,493</td>
<td align="right">827,269,844</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,659,960</td>
<td align="right">6,012,339</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,186,223,262</td>
<td align="right">14,001,271,931</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,418,307,989</td>
<td align="right">4,690,195,745</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">778,164,173</td>
<td align="right">825,090,004</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,275,911,478</td>
<td align="right">4,527,186,269</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">244,676,060</td>
<td align="right">258,932,759</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,282,317,776</td>
<td align="right">7,691,759,768</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,819,431,072</td>
<td align="right">4,552,629,293</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">67,154,944</td>
<td align="right">70,741,761</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">60,988,920</td>
<td align="right">57,784,980</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,199</td>
<td align="right">614,077,344</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">28,421,214</td>
<td align="right">27,061,160</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">149,619,268</td>
<td align="right">142,494,347</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,431,918,856</td>
<td align="right">3,591,756,173</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">173,365,468</td>
<td align="right">181,103,930</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,853,908,949</td>
<td align="right">1,771,822,642</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">395,735,798</td>
<td align="right">412,962,812</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,280,056,779</td>
<td align="right">1,227,035,856</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">235,348,136</td>
<td align="right">244,795,492</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,253,443,403</td>
<td align="right">1,302,859,400</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">992,083,936</td>
<td align="right">1,029,923,268</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">777,673,568</td>
<td align="right">804,864,105</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,046,287,225</td>
<td align="right">1,010,515,914</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,258,253,734</td>
<td align="right">6,467,857,984</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,685,040</td>
<td align="right">211,461,561</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">972,671,738</td>
<td align="right">1,004,794,268</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">664,423,779</td>
<td align="right">685,898,058</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,406,979</td>
<td align="right">96,212,258</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">905,547,040</td>
<td align="right">932,498,927</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">198,419,844</td>
<td align="right">204,272,344</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,602,987</td>
<td align="right">753,099,939</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">102,572,237</td>
<td align="right">105,190,300</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,449,512</td>
<td align="right">80,440,397</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,036,914,590</td>
<td align="right">3,111,962,625</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">15,659,836,248</td>
<td align="right">16,027,896,809</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">163,092,480</td>
<td align="right">166,922,010</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,611,854,806</td>
<td align="right">1,649,344,108</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">545,860</td>
<td align="right">557,120</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">554,024,588</td>
<td align="right">564,899,866</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">890,109,062</td>
<td align="right">872,662,625</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">923,984,301</td>
<td align="right">941,081,486</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,187,091</td>
<td align="right">99,965,296</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,990,580</td>
<td align="right">147,554,080</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,383,531,333</td>
<td align="right">1,359,400,359</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">327,320</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">137,740,395</td>
<td align="right">135,743,061</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">2,752,040</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,622,893,039</td>
<td align="right">3,668,336,989</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,404,439,011</td>
<td align="right">2,433,119,848</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">53,221,560</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">45,856,940</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,688,458,980</td>
<td align="right">4,639,722,134</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,430,657,611</td>
<td align="right">2,453,117,267</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">246,294,674</td>
<td align="right">248,380,718</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">95,413,551</td>
<td align="right">94,728,759</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,772,000</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,177,300</td>
<td align="right">8,231,460</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,705,220</td>
<td align="right">80,260,280</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">510,187,700</td>
<td align="right">512,880,040</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,754,409</td>
<td align="right">228,700,319</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,141,183,560</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,490,447</td>
<td align="right">160,939,722</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,550,540</td>
<td align="right">187,276,880</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,739,971,633</td>
<td align="right">3,735,268,208</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">75,938,681</td>
<td align="right">75,903,155</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,965,460</td>
<td align="right">154,900,700</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">398,193,991</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_AITER</td>
<td align="right"></td>
<td align="right">7,998,200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">59,033</td>
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
<td align="left">SEND_GEN</td>
<td align="right">320</td>
<td align="right">218,880</td>
<td align="right">68,300.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">6,140</td>
<td align="right">217,842</td>
<td align="right">3,447.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,622</td>
<td align="right">82,263</td>
<td align="right">1,142.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3,540</td>
<td align="right">40,840</td>
<td align="right">1,053.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,200</td>
<td align="right">12,400</td>
<td align="right">933.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">30,500</td>
<td align="right">242,880</td>
<td align="right">696.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,457</td>
<td align="right">14,819</td>
<td align="right">503.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">600</td>
<td align="right">2,300</td>
<td align="right">283.3%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">640</td>
<td align="right">1,720</td>
<td align="right">168.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">33,340</td>
<td align="right">78,943</td>
<td align="right">136.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">486,303</td>
<td align="right">118,322</td>
<td align="right">-75.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">44,661</td>
<td align="right">52,344</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">400</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,680</td>
<td align="right">1,560</td>
<td align="right">-7.1%</td>
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
<td align="right">1,109</td>
<td align="right">1,091</td>
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
<td align="right">1,109</td>
<td align="right">1,091</td>
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
<td align="right">420</td>
<td align="right">420</td>
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
<td align="right">1,780</td>
<td align="right">1,780</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-07-11
