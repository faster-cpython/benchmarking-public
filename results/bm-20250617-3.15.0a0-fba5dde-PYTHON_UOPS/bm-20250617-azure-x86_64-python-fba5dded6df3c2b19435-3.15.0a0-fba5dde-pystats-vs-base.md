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
<td align="right">5,790,443,702</td>
<td align="right">4,855,640</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,724,902</td>
<td align="right">1,232,478</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">459,026,517</td>
<td align="right">12,959,199</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,358,399</td>
<td align="right">2,267,708</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">6,000,000</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,505,187,443</td>
<td align="right">201,439,358</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,584,852,910</td>
<td align="right">232,752,272</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,789,347</td>
<td align="right">103,530,332</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,403,490,869</td>
<td align="right">212,408,061</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,754,454,187</td>
<td align="right">268,431,693</td>
<td align="right">-84.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,275,533,696</td>
<td align="right">202,536,325</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,718,912,768</td>
<td align="right">436,587,654</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,630,867</td>
<td align="right">85,679,404</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">565,954,140</td>
<td align="right">95,679,087</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,123,986,285</td>
<td align="right">359,471,576</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,483,022,181</td>
<td align="right">605,334,192</td>
<td align="right">-82.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,265,360,906</td>
<td align="right">436,418,866</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">88,978,474</td>
<td align="right">18,515,973</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,252,077,469</td>
<td align="right">271,275,207</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">690,673,305</td>
<td align="right">152,151,059</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,808,606</td>
<td align="right">34,663,171</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,277,796</td>
<td align="right">76,368,392</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">671,938,186</td>
<td align="right">160,432,561</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,657,308,135</td>
<td align="right">429,497,713</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">187,992,183</td>
<td align="right">49,887,034</td>
<td align="right">-73.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">940,058,750</td>
<td align="right">254,429,046</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,284,120,618</td>
<td align="right">1,974,801,371</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">626,712,480</td>
<td align="right">171,021,060</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,454,285</td>
<td align="right">104,494,806</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,436,390</td>
<td align="right">145,966,113</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">377,653,289</td>
<td align="right">118,494,513</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,139,790,659</td>
<td align="right">671,749,264</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">56,899,383</td>
<td align="right">17,977,739</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">533,406,829</td>
<td align="right">168,678,778</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,433,509,843</td>
<td align="right">1,090,293,213</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,733,490,985</td>
<td align="right">873,064,544</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">252,182,938</td>
<td align="right">81,437,962</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">77,896,767</td>
<td align="right">25,335,102</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,531,045,368</td>
<td align="right">830,083,785</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">352,573,871</td>
<td align="right">117,626,725</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,503,600</td>
<td align="right">182,396,635</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,837,919,763</td>
<td align="right">1,964,534,632</td>
<td align="right">-66.3%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,387,232</td>
<td align="right">54,908,721</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,243,760,138</td>
<td align="right">432,103,685</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,489,300,197</td>
<td align="right">865,489,544</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,040,228,687</td>
<td align="right">372,870,644</td>
<td align="right">-64.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,671,860,784</td>
<td align="right">3,852,518,906</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,386,421,995</td>
<td align="right">4,850,147,800</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,786,196</td>
<td align="right">27,120,971</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,108,716,650</td>
<td align="right">3,674,843,918</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">433,613,667</td>
<td align="right">161,918,707</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">6,486,155</td>
<td align="right">2,435,640</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,332,726</td>
<td align="right">25,718,454</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">98,038,660</td>
<td align="right">38,823,735</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">261,760,363</td>
<td align="right">104,718,230</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">22,615,860</td>
<td align="right">9,150,065</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">90,542,472</td>
<td align="right">36,768,488</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">149,721,625</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">861,414,444</td>
<td align="right">358,270,271</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">2,597,140</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,103,323,738</td>
<td align="right">890,631,445</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">795,069,017</td>
<td align="right">339,541,484</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,366,470</td>
<td align="right">468,452,801</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">536,441,138</td>
<td align="right">238,651,464</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">780,507,403</td>
<td align="right">350,841,808</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,344,483,241</td>
<td align="right">1,077,133,912</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">401,271,085</td>
<td align="right">184,870,956</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,531,229,700</td>
<td align="right">4,041,990,892</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">33,485,441,056</td>
<td align="right">15,934,309,324</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">72,287,092</td>
<td align="right">34,988,222</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">256,554,405</td>
<td align="right">125,627,258</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,095,411,127</td>
<td align="right">536,487,059</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,098,554</td>
<td align="right">133,691,120</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,646</td>
<td align="right">4,866,866</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">232,167</td>
<td align="right">117,444</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">317,963,205</td>
<td align="right">161,725,737</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">201,369,791</td>
<td align="right">103,659,463</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,437,953</td>
<td align="right">51,289,059</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">14,803</td>
<td align="right">7,744</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,214,361,620</td>
<td align="right">640,740,391</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,749,762</td>
<td align="right">940,512</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">353,984,335</td>
<td align="right">194,242,526</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,812,598</td>
<td align="right">85,943,382</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,887,040,006</td>
<td align="right">2,191,412,037</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">282,063,730</td>
<td align="right">159,078,097</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,542,250,853</td>
<td align="right">873,998,097</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,056,123,867</td>
<td align="right">602,807,689</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,535,694,993</td>
<td align="right">878,425,117</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">116,378,642</td>
<td align="right">66,912,989</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">59,158,601</td>
<td align="right">34,230,877</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,420,092,824</td>
<td align="right">1,417,389,509</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,343,070</td>
<td align="right">4,325,952</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">773,796,039</td>
<td align="right">457,427,736</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,358,157,534</td>
<td align="right">820,148,283</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,164,221,192</td>
<td align="right">1,916,015,426</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,154</td>
<td align="right">114,765,162</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">190,487,643</td>
<td align="right">119,444,483</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">801,824,073</td>
<td align="right">521,491,824</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,128,392</td>
<td align="right">74,933,716</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,361,229</td>
<td align="right">40,671,148</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,682,683</td>
<td align="right">80,233,826</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">66,513,439</td>
<td align="right">43,828,922</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,750,036,054</td>
<td align="right">3,138,759,659</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,294,894</td>
<td align="right">116,308,217</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">385,165,466</td>
<td align="right">259,048,071</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">485,158,938</td>
<td align="right">331,175,729</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">164,037,838</td>
<td align="right">114,497,008</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,380,222,431</td>
<td align="right">2,402,543,921</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">675,483,619</td>
<td align="right">485,286,858</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">325,969,274</td>
<td align="right">237,725,421</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">840,494,592</td>
<td align="right">636,493,388</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">68,557,906</td>
<td align="right">52,140,415</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">233,805,709</td>
<td align="right">178,067,183</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,656,963</td>
<td align="right">1,262,371</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">290,124,507</td>
<td align="right">225,529,939</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,239,843,367</td>
<td align="right">4,881,285,995</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">468,004,690</td>
<td align="right">366,386,559</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">355,610,359</td>
<td align="right">280,712,582</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,215,117,195</td>
<td align="right">2,551,008,831</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,122,125</td>
<td align="right">2,550,468</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">346,666,986</td>
<td align="right">285,115,086</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">80,977,796</td>
<td align="right">67,036,920</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">267,372,078</td>
<td align="right">221,398,864</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">942,993,687</td>
<td align="right">798,533,111</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,358,038,367</td>
<td align="right">4,612,379,086</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,786,271</td>
<td align="right">61,912,763</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,304,402</td>
<td align="right">366,804,618</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">975,004,935</td>
<td align="right">869,403,172</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">334,962,364</td>
<td align="right">299,238,310</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">147,865,796</td>
<td align="right">132,506,141</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">76,669</td>
<td align="right">69,551</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">61,064,703</td>
<td align="right">55,569,659</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,784,349</td>
<td align="right">3,472,349</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">75,214,752</td>
<td align="right">69,156,319</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">66,481,373</td>
<td align="right">61,279,389</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,497,563</td>
<td align="right">65,525,644</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,165,325</td>
<td align="right">5,799,281</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">463,549</td>
<td align="right">441,433</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,505,268</td>
<td align="right">19,638,951</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,832,016</td>
<td align="right">19,965,699</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,832,037</td>
<td align="right">19,965,720</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,096,557</td>
<td align="right">9,678,845</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,112,129,472</td>
<td align="right">1,066,746,741</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,704,408</td>
<td align="right">12,200,932</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">9,870,921</td>
<td align="right">9,505,456</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">75,632,196</td>
<td align="right">73,082,017</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,630</td>
<td align="right">13,029</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,764</td>
<td align="right">123,859,821</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">65,675,864</td>
<td align="right">63,788,730</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">72,271,101</td>
<td align="right">70,196,777</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,513</td>
<td align="right">2,573</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,090,877</td>
<td align="right">3,024,278</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,553,244</td>
<td align="right">27,951,973</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">243,206</td>
<td align="right">248,067</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,430,282</td>
<td align="right">5,347,783</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,587,146,889</td>
<td align="right">1,569,045,251</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,954,695</td>
<td align="right">35,547,045</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">115,321,074</td>
<td align="right">114,402,479</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,418,034</td>
<td align="right">189,459,136</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,942,701</td>
<td align="right">418,214,491</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,519,519</td>
<td align="right">241,671,682</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,569,682</td>
<td align="right">243,720,439</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,514,133</td>
<td align="right">591,602,918</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,096,990</td>
<td align="right">155,716,415</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,651,748</td>
<td align="right">302,244,074</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,350</td>
<td align="right">5,355</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,627</td>
<td align="right">72,564</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,756,294</td>
<td align="right">14,760,188</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,688</td>
<td align="right">33,683</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,301,986</td>
<td align="right">131,286,174</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">214,351</td>
<td align="right">214,350</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,749</td>
<td align="right">128,851,749</td>
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
<td align="right">41,964,443</td>
<td align="right">41,964,443</td>
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
<td align="left">LOAD_SPECIAL</td>
<td align="right">10,549,274</td>
<td align="right">10,549,274</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,796</td>
<td align="right">8,976,796</td>
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
<td align="right">98,577</td>
<td align="right">98,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">56,999</td>
<td align="right">56,999</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,970</td>
<td align="right">53,970</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,864</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,550</td>
<td align="right">3,550</td>
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
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,072</td>
<td align="right">1,072</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">176</td>
<td align="right">176</td>
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
<td align="right">25</td>
<td align="right">25</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">999,067,503</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">856,559,748</td>
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
<td align="right">16,228,049,415</td>
<td align="right">87.0%</td>
<td align="right">3,924,120,670</td>
<td align="right">77.5%</td>
<td align="right">-75.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,343,553,068</td>
<td align="right">12.6%</td>
<td align="right">1,076,652,565</td>
<td align="right">21.3%</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">71,483,620</td>
<td align="right">0.4%</td>
<td align="right">64,566,214</td>
<td align="right">1.3%</td>
<td align="right">-9.7%</td>
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
<td align="right">912,909</td>
<td align="right">40.1%</td>
<td align="right">462,927</td>
<td align="right">27.2%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,365,757</td>
<td align="right">59.9%</td>
<td align="right">1,236,431</td>
<td align="right">72.8%</td>
<td align="right">-9.5%</td>
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
<td align="right">22,292</td>
<td align="right">2.4%</td>
<td align="right">1,810</td>
<td align="right">0.4%</td>
<td align="right">-91.9%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">80</td>
<td align="right">0.0%</td>
<td align="right">-81.8%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">9.4%</td>
<td align="right">16,343</td>
<td align="right">3.5%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">121,439</td>
<td align="right">13.3%</td>
<td align="right">25,835</td>
<td align="right">5.6%</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">2,767</td>
<td align="right">0.6%</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,219</td>
<td align="right">8.1%</td>
<td align="right">18,446</td>
<td align="right">4.0%</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">114,964</td>
<td align="right">12.6%</td>
<td align="right">28,692</td>
<td align="right">6.2%</td>
<td align="right">-75.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">0.9%</td>
<td align="right">2,343</td>
<td align="right">0.5%</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,092</td>
<td align="right">0.1%</td>
<td align="right">334</td>
<td align="right">0.1%</td>
<td align="right">-69.4%</td>
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
<td align="right">23,521</td>
<td align="right">2.6%</td>
<td align="right">8,297</td>
<td align="right">1.8%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">359</td>
<td align="right">0.0%</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,456</td>
<td align="right">4.8%</td>
<td align="right">21,790</td>
<td align="right">4.7%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,985</td>
<td align="right">3.7%</td>
<td align="right">20,079</td>
<td align="right">4.3%</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">2.1%</td>
<td align="right">11,552</td>
<td align="right">2.5%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">35,895</td>
<td align="right">3.9%</td>
<td align="right">22,389</td>
<td align="right">4.8%</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,515</td>
<td align="right">0.9%</td>
<td align="right">6,194</td>
<td align="right">1.3%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">78,851</td>
<td align="right">8.6%</td>
<td align="right">63,025</td>
<td align="right">13.6%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">8,167</td>
<td align="right">0.9%</td>
<td align="right">6,694</td>
<td align="right">1.4%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">42,834</td>
<td align="right">4.7%</td>
<td align="right">36,084</td>
<td align="right">7.8%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">46,925</td>
<td align="right">5.1%</td>
<td align="right">40,933</td>
<td align="right">8.8%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">348</td>
<td align="right">0.0%</td>
<td align="right">326</td>
<td align="right">0.1%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,078</td>
<td align="right">0.8%</td>
<td align="right">6,883</td>
<td align="right">1.5%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,035</td>
<td align="right">0.2%</td>
<td align="right">1,996</td>
<td align="right">0.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,110</td>
<td align="right">0.3%</td>
<td align="right">3,130</td>
<td align="right">0.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">631</td>
<td align="right">0.1%</td>
<td align="right">629</td>
<td align="right">0.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,336</td>
<td align="right">0.3%</td>
<td align="right">2,334</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">107,940</td>
<td align="right">11.8%</td>
<td align="right">107,939</td>
<td align="right">23.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">3,165</td>
<td align="right">0.3%</td>
<td align="right">3,165</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.2%</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">157</td>
<td align="right">0.0%</td>
<td align="right">157</td>
<td align="right">0.0%</td>
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
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">43</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right">26</td>
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
<tr>
<td align="left">subscr deque</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">545,503,600</td>
<td align="right">100.0%</td>
<td align="right">182,396,635</td>
<td align="right">100.0%</td>
<td align="right">-66.6%</td>
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
<td align="right">11,101,952,348</td>
<td align="right">98.4%</td>
<td align="right">5,046,810,247</td>
<td align="right">97.1%</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">181,986,198</td>
<td align="right">1.6%</td>
<td align="right">150,246,307</td>
<td align="right">2.9%</td>
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
<td align="right">178,626,725</td>
<td align="right">1.6%</td>
<td align="right">147,485,780</td>
<td align="right">2.8%</td>
<td align="right">-17.4%</td>
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
<td align="right">3,602,533</td>
<td align="right">100.0%</td>
<td align="right">3,008,448</td>
<td align="right">100.0%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">146</td>
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
<td align="right">267</td>
<td align="right">182.9%</td>
<td align="right">287</td>
<td align="right">196.6%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">754</td>
<td align="right">516.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">146</td>
<td align="right">100.0%</td>
<td align="right">146</td>
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
<td align="right">574,328</td>
<td align="right">96.6%</td>
<td align="right">574,328</td>
<td align="right">96.6%</td>
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
<td align="right">581,624</td>
<td align="right">97.9%</td>
<td align="right">581,624</td>
<td align="right">97.8%</td>
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
<td align="right">19,926</td>
<td align="right">100.0%</td>
<td align="right">20,325</td>
<td align="right">100.0%</td>
<td align="right">2.0%</td>
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
<td align="right">510,405,649</td>
<td align="right">10.2%</td>
<td align="right">85,564,329</td>
<td align="right">6.6%</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,505,608,160</td>
<td align="right">89.8%</td>
<td align="right">1,219,445,161</td>
<td align="right">93.4%</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,270,889</td>
<td align="right">0.0%</td>
<td align="right">1,136,817</td>
<td align="right">0.1%</td>
<td align="right">-10.5%</td>
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
<td align="right">207,488</td>
<td align="right">83.4%</td>
<td align="right">96,903</td>
<td align="right">71.1%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,399</td>
<td align="right">16.6%</td>
<td align="right">39,429</td>
<td align="right">28.9%</td>
<td align="right">-4.8%</td>
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
<td align="right">90,414</td>
<td align="right">43.6%</td>
<td align="right">4,092</td>
<td align="right">4.2%</td>
<td align="right">-95.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,832</td>
<td align="right">3.3%</td>
<td align="right">373</td>
<td align="right">0.4%</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">10,483</td>
<td align="right">5.1%</td>
<td align="right">4,561</td>
<td align="right">4.7%</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">11,307</td>
<td align="right">5.4%</td>
<td align="right">8,649</td>
<td align="right">8.9%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,409</td>
<td align="right">21.9%</td>
<td align="right">36,507</td>
<td align="right">37.7%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">196</td>
<td align="right">0.1%</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,324</td>
<td align="right">0.6%</td>
<td align="right">1,278</td>
<td align="right">1.3%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,298</td>
<td align="right">11.2%</td>
<td align="right">23,080</td>
<td align="right">23.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,881</td>
<td align="right">0.9%</td>
<td align="right">1,873</td>
<td align="right">1.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,762</td>
<td align="right">3.7%</td>
<td align="right">7,734</td>
<td align="right">8.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">3.7%</td>
<td align="right">7,648</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">934</td>
<td align="right">0.5%</td>
<td align="right">934</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,186,664,479</td>
<td align="right">93.4%</td>
<td align="right">429,621,881</td>
<td align="right">83.2%</td>
<td align="right">-80.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,403,375</td>
<td align="right">0.1%</td>
<td align="right">728,519</td>
<td align="right">0.1%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">153,752,174</td>
<td align="right">6.6%</td>
<td align="right">85,899,137</td>
<td align="right">16.6%</td>
<td align="right">-44.1%</td>
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
<td align="right">28,585</td>
<td align="right">32.9%</td>
<td align="right">16,053</td>
<td align="right">27.7%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">58,314</td>
<td align="right">67.1%</td>
<td align="right">41,935</td>
<td align="right">72.3%</td>
<td align="right">-28.1%</td>
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
<td align="right">21,773</td>
<td align="right">37.3%</td>
<td align="right">10,156</td>
<td align="right">24.2%</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,540</td>
<td align="right">24.9%</td>
<td align="right">12,006</td>
<td align="right">28.6%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,988</td>
<td align="right">18.8%</td>
<td align="right">9,269</td>
<td align="right">22.1%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,013</td>
<td align="right">18.9%</td>
<td align="right">10,504</td>
<td align="right">25.0%</td>
<td align="right">-4.6%</td>
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
<td align="right">1,504,746,807</td>
<td align="right">29.3%</td>
<td align="right">201,324,578</td>
<td align="right">13.3%</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,470,904,072</td>
<td align="right">67.5%</td>
<td align="right">1,248,739,477</td>
<td align="right">82.6%</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,968,260</td>
<td align="right">3.2%</td>
<td align="right">61,947,935</td>
<td align="right">4.1%</td>
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
<td align="right">435,244</td>
<td align="right">12.3%</td>
<td align="right">109,392</td>
<td align="right">8.5%</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,098,948</td>
<td align="right">87.7%</td>
<td align="right">1,174,047</td>
<td align="right">91.5%</td>
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
<td align="right">171,565</td>
<td align="right">39.4%</td>
<td align="right">4,191</td>
<td align="right">3.8%</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,675</td>
<td align="right">19.2%</td>
<td align="right">10,875</td>
<td align="right">9.9%</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,700</td>
<td align="right">8.0%</td>
<td align="right">6,394</td>
<td align="right">5.8%</td>
<td align="right">-81.6%</td>
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
<td align="left">other</td>
<td align="right">10,542</td>
<td align="right">2.4%</td>
<td align="right">3,376</td>
<td align="right">3.1%</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,269</td>
<td align="right">4.2%</td>
<td align="right">5,877</td>
<td align="right">5.4%</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,537</td>
<td align="right">2.4%</td>
<td align="right">3,390</td>
<td align="right">3.1%</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,420</td>
<td align="right">0.8%</td>
<td align="right">1,222</td>
<td align="right">1.1%</td>
<td align="right">-64.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">533</td>
<td align="right">0.1%</td>
<td align="right">248</td>
<td align="right">0.2%</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,114</td>
<td align="right">0.7%</td>
<td align="right">1,978</td>
<td align="right">1.8%</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,008</td>
<td align="right">4.1%</td>
<td align="right">12,936</td>
<td align="right">11.8%</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">68,973</td>
<td align="right">15.8%</td>
<td align="right">49,848</td>
<td align="right">45.6%</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,282</td>
<td align="right">1.0%</td>
<td align="right">3,293</td>
<td align="right">3.0%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,083</td>
<td align="right">1.4%</td>
<td align="right">5,157</td>
<td align="right">4.7%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">260</td>
<td align="right">0.2%</td>
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
<td align="right">2,823,200</td>
<td align="right">2,823,200 / 0 !!</td>
<td align="right">1,733,414</td>
<td align="right">1,733,414 / 0 !!</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">119,369,919</td>
<td align="right">119,369,919 / 0 !!</td>
<td align="right">111,962,873</td>
<td align="right">111,962,873 / 0 !!</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">304,453,466</td>
<td align="right">304,453,466 / 0 !!</td>
<td align="right">298,552,863</td>
<td align="right">298,552,863 / 0 !!</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,508,924</td>
<td align="right">5,508,924 / 0 !!</td>
<td align="right">5,422,312</td>
<td align="right">5,422,312 / 0 !!</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,932,891</td>
<td align="right">34,932,891 / 0 !!</td>
<td align="right">34,420,286</td>
<td align="right">34,420,286 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,923,177</td>
<td align="right">101,923,177 / 0 !!</td>
<td align="right">101,415,710</td>
<td align="right">101,415,710 / 0 !!</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,958,869</td>
<td align="right">341,958,869 / 0 !!</td>
<td align="right">341,396,953</td>
<td align="right">341,396,953 / 0 !!</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">171,490,964</td>
<td align="right">171,490,964 / 0 !!</td>
<td align="right">171,250,427</td>
<td align="right">171,250,427 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,122,586</td>
<td align="right">12,122,586 / 0 !!</td>
<td align="right">12,123,694</td>
<td align="right">12,123,694 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
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
<td align="right">11,981,960,333</td>
<td align="right">87.8%</td>
<td align="right">6,663,321,710</td>
<td align="right">85.5%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">800,051,389</td>
<td align="right">5.9%</td>
<td align="right">519,803,171</td>
<td align="right">6.7%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,436,011</td>
<td align="right">0.0%</td>
<td align="right">1,005,161</td>
<td align="right">0.0%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">860,551,074</td>
<td align="right">6.3%</td>
<td align="right">605,830,976</td>
<td align="right">7.8%</td>
<td align="right">-29.6%</td>
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
<td align="right">16,315,455</td>
<td align="right">97.0%</td>
<td align="right">11,516,636</td>
<td align="right">96.4%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">505,661</td>
<td align="right">3.0%</td>
<td align="right">432,385</td>
<td align="right">3.6%</td>
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
<td align="left">method</td>
<td align="right">73,624</td>
<td align="right">14.6%</td>
<td align="right">35,460</td>
<td align="right">8.2%</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,104</td>
<td align="right">0.2%</td>
<td align="right">743</td>
<td align="right">0.2%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">54,639</td>
<td align="right">10.8%</td>
<td align="right">39,915</td>
<td align="right">9.2%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,312</td>
<td align="right">1.1%</td>
<td align="right">4,069</td>
<td align="right">0.9%</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,158</td>
<td align="right">1.6%</td>
<td align="right">6,976</td>
<td align="right">1.6%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,739</td>
<td align="right">0.5%</td>
<td align="right">2,378</td>
<td align="right">0.5%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,794</td>
<td align="right">3.1%</td>
<td align="right">13,845</td>
<td align="right">3.2%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">53,191</td>
<td align="right">10.5%</td>
<td align="right">47,286</td>
<td align="right">10.9%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,463</td>
<td align="right">4.8%</td>
<td align="right">23,402</td>
<td align="right">5.4%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,721</td>
<td align="right">0.3%</td>
<td align="right">1,694</td>
<td align="right">0.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,885</td>
<td align="right">0.4%</td>
<td align="right">1,883</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,448</td>
<td align="right">0.9%</td>
<td align="right">4,446</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">573</td>
<td align="right">0.1%</td>
<td align="right">573</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">545</td>
<td align="right">0.1%</td>
<td align="right">545</td>
<td align="right">0.1%</td>
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
<td align="right">255</td>
<td align="right">0.1%</td>
<td align="right">255</td>
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
<td align="right">9,218,090,378</td>
<td align="right">99.8%</td>
<td align="right">4,367,027,333</td>
<td align="right">99.7%</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">51,816</td>
<td align="right">0.0%</td>
<td align="right">51,220</td>
<td align="right">0.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,452</td>
<td align="right">0.2%</td>
<td align="right">14,622,447</td>
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
<td align="right">1,376</td>
<td align="right">0.0%</td>
<td align="right">1,376</td>
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
<td align="right">134,593</td>
<td align="right">100.0%</td>
<td align="right">138,492</td>
<td align="right">100.0%</td>
<td align="right">2.9%</td>
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
<td align="right">64,155,580</td>
<td align="right">100.0%</td>
<td align="right">58,593,937</td>
<td align="right">100.0%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">203</td>
<td align="right">0.0%</td>
<td align="right">203</td>
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
<td align="right">2,310</td>
<td align="right">100.0%</td>
<td align="right">2,370</td>
<td align="right">100.0%</td>
<td align="right">2.6%</td>
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
<td align="right">593,499,422</td>
<td align="right">82.2%</td>
<td align="right">591,588,207</td>
<td align="right">82.1%</td>
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
<td align="right">128,816,951</td>
<td align="right">17.8%</td>
<td align="right">128,816,951</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,812,769,404</td>
<td align="right">90.9%</td>
<td align="right">1,572,820,278</td>
<td align="right">90.5%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">114,206,014</td>
<td align="right">5.7%</td>
<td align="right">104,092,801</td>
<td align="right">6.0%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">66,396,798</td>
<td align="right">3.3%</td>
<td align="right">61,194,428</td>
<td align="right">3.5%</td>
<td align="right">-7.8%</td>
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
<td align="right">2,193,749</td>
<td align="right">98.0%</td>
<td align="right">2,004,832</td>
<td align="right">97.9%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">44,910</td>
<td align="right">2.0%</td>
<td align="right">43,656</td>
<td align="right">2.1%</td>
<td align="right">-2.8%</td>
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
<td align="right">5,799</td>
<td align="right">12.9%</td>
<td align="right">4,635</td>
<td align="right">10.6%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">423</td>
<td align="right">0.9%</td>
<td align="right">379</td>
<td align="right">0.9%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,321</td>
<td align="right">2.9%</td>
<td align="right">1,275</td>
<td align="right">2.9%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">248,234</td>
<td align="right">552.7%</td>
<td align="right">240,693</td>
<td align="right">551.3%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,334</td>
<td align="right">7.4%</td>
<td align="right">3,340</td>
<td align="right">7.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">3,741</td>
<td align="right">8.3%</td>
<td align="right">3,737</td>
<td align="right">8.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">19,647</td>
<td align="right">43.7%</td>
<td align="right">19,647</td>
<td align="right">45.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,227</td>
<td align="right">16.1%</td>
<td align="right">7,227</td>
<td align="right">16.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">747</td>
<td align="right">1.7%</td>
<td align="right">747</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">363</td>
<td align="right">0.8%</td>
<td align="right">363</td>
<td align="right">0.8%</td>
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
<tr>
<td align="left">mutable class</td>
<td align="right">91</td>
<td align="right">0.2%</td>
<td align="right">91</td>
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
<td align="right">112,724,902</td>
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
<td align="right">700,605,445</td>
<td align="right">43.3%</td>
<td align="right">103,492,024</td>
<td align="right">32.7%</td>
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
<td align="right">918,525,791</td>
<td align="right">56.7%</td>
<td align="right">213,303,592</td>
<td align="right">67.3%</td>
<td align="right">-76.8%</td>
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
<td align="right">181,878</td>
<td align="right">98.9%</td>
<td align="right">36,144</td>
<td align="right">94.3%</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,064</td>
<td align="right">1.1%</td>
<td align="right">2,204</td>
<td align="right">5.7%</td>
<td align="right">6.8%</td>
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
<td align="right">86,545</td>
<td align="right">47.6%</td>
<td align="right">273</td>
<td align="right">0.8%</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,315</td>
<td align="right">2.9%</td>
<td align="right">162</td>
<td align="right">0.4%</td>
<td align="right">-97.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,183</td>
<td align="right">10.5%</td>
<td align="right">3,323</td>
<td align="right">9.2%</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.9%</td>
<td align="right">10,483</td>
<td align="right">29.0%</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,991</td>
<td align="right">1.6%</td>
<td align="right">2,990</td>
<td align="right">8.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,164</td>
<td align="right">9.4%</td>
<td align="right">17,164</td>
<td align="right">47.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">0.9%</td>
<td align="right">1,681</td>
<td align="right">4.7%</td>
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
<td align="right">255,907,337</td>
<td align="right">5.0%</td>
<td align="right">125,118,052</td>
<td align="right">4.4%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">110,663,053</td>
<td align="right">2.2%</td>
<td align="right">60,773,071</td>
<td align="right">2.1%</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,725,910,613</td>
<td align="right">92.8%</td>
<td align="right">2,640,647,995</td>
<td align="right">93.4%</td>
<td align="right">-44.1%</td>
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
<td align="right">2,136,465</td>
<td align="right">78.2%</td>
<td align="right">1,196,312</td>
<td align="right">72.3%</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">596,929</td>
<td align="right">21.8%</td>
<td align="right">458,031</td>
<td align="right">27.7%</td>
<td align="right">-23.3%</td>
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
<td align="right">18,856</td>
<td align="right">3.2%</td>
<td align="right">4,655</td>
<td align="right">1.0%</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">126,701</td>
<td align="right">21.2%</td>
<td align="right">51,854</td>
<td align="right">11.3%</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">72,063</td>
<td align="right">12.1%</td>
<td align="right">38,938</td>
<td align="right">8.5%</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,304</td>
<td align="right">2.7%</td>
<td align="right">9,741</td>
<td align="right">2.1%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">83,562</td>
<td align="right">14.0%</td>
<td align="right">74,372</td>
<td align="right">16.2%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,721</td>
<td align="right">1.6%</td>
<td align="right">8,710</td>
<td align="right">1.9%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,036</td>
<td align="right">1.7%</td>
<td align="right">10,069</td>
<td align="right">2.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,844</td>
<td align="right">43.2%</td>
<td align="right">257,850</td>
<td align="right">56.3%</td>
<td align="right">0.0%</td>
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
<td align="right">1,237,421,823</td>
<td align="right">99.9%</td>
<td align="right">644,562,700</td>
<td align="right">99.8%</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,646,238</td>
<td align="right">0.1%</td>
<td align="right">1,251,648</td>
<td align="right">0.2%</td>
<td align="right">-24.0%</td>
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
<td align="right">916</td>
<td align="right">8.5%</td>
<td align="right">794</td>
<td align="right">7.3%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,889</td>
<td align="right">91.5%</td>
<td align="right">10,009</td>
<td align="right">92.7%</td>
<td align="right">1.2%</td>
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
<td align="right">681</td>
<td align="right">74.3%</td>
<td align="right">560</td>
<td align="right">70.5%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">99</td>
<td align="right">10.8%</td>
<td align="right">98</td>
<td align="right">12.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">14.8%</td>
<td align="right">136</td>
<td align="right">17.1%</td>
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
<td align="right">8,238,926,331</td>
<td align="right">3.9%</td>
<td align="right">3,127,379,008</td>
<td align="right">3.2%</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">78,547,582,572</td>
<td align="right">37.3%</td>
<td align="right">34,700,196,082</td>
<td align="right">36.0%</td>
<td align="right">-55.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">122,103,471,141</td>
<td align="right">58.0%</td>
<td align="right">57,530,519,613</td>
<td align="right">59.7%</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,506,344,023</td>
<td align="right">0.7%</td>
<td align="right">1,050,136,892</td>
<td align="right">1.1%</td>
<td align="right">-30.3%</td>
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
<td align="right">1,504,746,807</td>
<td align="right">20.6%</td>
<td align="right">201,324,578</td>
<td align="right">7.4%</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,605,445</td>
<td align="right">9.6%</td>
<td align="right">103,492,024</td>
<td align="right">3.8%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,405,649</td>
<td align="right">7.0%</td>
<td align="right">85,564,329</td>
<td align="right">3.1%</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,503,600</td>
<td align="right">7.5%</td>
<td align="right">182,396,635</td>
<td align="right">6.7%</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,343,553,068</td>
<td align="right">32.0%</td>
<td align="right">1,076,652,565</td>
<td align="right">39.4%</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">255,907,337</td>
<td align="right">3.5%</td>
<td align="right">125,118,052</td>
<td align="right">4.6%</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,752,174</td>
<td align="right">2.1%</td>
<td align="right">85,899,137</td>
<td align="right">3.1%</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">800,051,389</td>
<td align="right">10.9%</td>
<td align="right">519,803,171</td>
<td align="right">19.0%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">178,626,725</td>
<td align="right">2.4%</td>
<td align="right">147,485,780</td>
<td align="right">5.4%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,951</td>
<td align="right">1.8%</td>
<td align="right">128,816,951</td>
<td align="right">4.7%</td>
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
<td align="right">82,006,511</td>
<td align="right">5.4%</td>
<td align="right">30,927,753</td>
<td align="right">2.9%</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,884,354</td>
<td align="right">5.4%</td>
<td align="right">30,943,634</td>
<td align="right">2.9%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,362,220</td>
<td align="right">3.3%</td>
<td align="right">25,638,628</td>
<td align="right">2.4%</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,472,333</td>
<td align="right">3.6%</td>
<td align="right">29,441,582</td>
<td align="right">2.8%</td>
<td align="right">-46.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">365,459,315</td>
<td align="right">24.3%</td>
<td align="right">216,916,180</td>
<td align="right">20.7%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,667,089</td>
<td align="right">5.4%</td>
<td align="right">53,316,474</td>
<td align="right">5.1%</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">264,664,340</td>
<td align="right">17.6%</td>
<td align="right">175,669,659</td>
<td align="right">16.7%</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">89,886,903</td>
<td align="right">6.0%</td>
<td align="right">80,759,239</td>
<td align="right">7.7%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,987,666</td>
<td align="right">6.2%</td>
<td align="right">87,700,914</td>
<td align="right">8.4%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,824,527</td>
<td align="right">5.5%</td>
<td align="right">77,873,742</td>
<td align="right">7.4%</td>
<td align="right">-6.0%</td>
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
<td align="right">4,273,457</td>
<td align="right">0.1%</td>
<td align="right">2,128,262</td>
<td align="right">0.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,093,849,450</td>
<td align="right">76.2%</td>
<td align="right">4,980,288,954</td>
<td align="right">76.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,463,790</td>
<td align="right">8.7%</td>
<td align="right">575,151,335</td>
<td align="right">8.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,415,095,918</td>
<td align="right">81.0%</td>
<td align="right">5,329,532,816</td>
<td align="right">81.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">275,667,473</td>
<td align="right">4.1%</td>
<td align="right">271,436,732</td>
<td align="right">4.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,591,634,510</td>
<td align="right">23.8%</td>
<td align="right">1,573,532,864</td>
<td align="right">24.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,591,634,510</td>
<td align="right">23.8%</td>
<td align="right">1,573,532,864</td>
<td align="right">24.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,698,544</td>
<td align="right">1.1%</td>
<td align="right">69,927,759</td>
<td align="right">1.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,007,170,720</td>
<td align="right">15.1%</td>
<td align="right">998,381,529</td>
<td align="right">15.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,002,893,399</td>
<td align="right">15.0%</td>
<td align="right">996,249,403</td>
<td align="right">15.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,476,535</td>
<td align="right">3.9%</td>
<td align="right">258,591,578</td>
<td align="right">3.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,590,571</td>
<td align="right">0.4%</td>
<td align="right">23,551,190</td>
<td align="right">0.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
<td align="right">3,864</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,898</td>
<td align="right">2.0%</td>
<td align="right">132,513,898</td>
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
<td align="right">6,765,316</td>
<td align="right"></td>
<td align="right">5,480,971</td>
<td align="right"></td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">306,771</td>
<td align="right">0.2%</td>
<td align="right">265,171</td>
<td align="right">0.2%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">63,252,304</td>
<td align="right"></td>
<td align="right">57,215,793</td>
<td align="right"></td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,362,695,943</td>
<td align="right"></td>
<td align="right">2,141,096,952</td>
<td align="right"></td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">57,289,116</td>
<td align="right"></td>
<td align="right">52,539,749</td>
<td align="right"></td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,860,375,437</td>
<td align="right">1.7%</td>
<td align="right">1,820,744,600</td>
<td align="right">1.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">22,957,395,691</td>
<td align="right">25.1%</td>
<td align="right">22,471,152,747</td>
<td align="right">24.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">24,947,678,755</td>
<td align="right">27.2%</td>
<td align="right">24,436,686,950</td>
<td align="right">27.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,571,298,820</td>
<td align="right"></td>
<td align="right">13,331,121,596</td>
<td align="right"></td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,571,185,778</td>
<td align="right">70.9%</td>
<td align="right">13,331,019,425</td>
<td align="right">70.8%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,446,854,682</td>
<td align="right"></td>
<td align="right">2,404,010,244</td>
<td align="right"></td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">31,754,509,604</td>
<td align="right">29.2%</td>
<td align="right">31,266,041,743</td>
<td align="right">29.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,909,861,255</td>
<td align="right">22.9%</td>
<td align="right">24,529,583,265</td>
<td align="right">22.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,481,377,973</td>
<td align="right">28.7%</td>
<td align="right">5,423,811,512</td>
<td align="right">28.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,559,008,611</td>
<td align="right">29.1%</td>
<td align="right">5,501,247,147</td>
<td align="right">29.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,643,565,996</td>
<td align="right">5.1%</td>
<td align="right">4,596,693,334</td>
<td align="right">5.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,156,937,031</td>
<td align="right"></td>
<td align="right">6,095,170,532</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">50,140,253,009</td>
<td align="right">46.1%</td>
<td align="right">49,749,169,142</td>
<td align="right">46.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,611,660</td>
<td align="right"></td>
<td align="right">173,355,688</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,265,356</td>
<td align="right">0.4%</td>
<td align="right">71,071,491</td>
<td align="right">0.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">39,069,027,781</td>
<td align="right">42.6%</td>
<td align="right">38,974,961,903</td>
<td align="right">43.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,365,282</td>
<td align="right">0.0%</td>
<td align="right">6,364,144</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,404,482</td>
<td align="right">1.9%</td>
<td align="right">3,404,482</td>
<td align="right">2.0%</td>
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
<td align="right">364,840</td>
<td align="right">102,017,796</td>
<td align="right">9,544,770,040</td>
<td align="right">759,974,420</td>
<td align="right">764,461,528</td>
<td align="right">362,946</td>
<td align="right">100,005,890</td>
<td align="right">9,459,713,126</td>
<td align="right">751,212,381</td>
<td align="right">759,661,925</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,681,053,888</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,681,297,920</td>
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
<td align="right">34</td>
<td align="right">34</td>
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
<td align="right">41</td>
<td align="right">41</td>
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
<td align="right">101</td>
<td align="right">101 / 0 !!</td>
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
<td align="right">101</td>
<td align="right">101 / 0 !!</td>
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
<td align="right">2,397</td>
<td align="right">2,397</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-18
