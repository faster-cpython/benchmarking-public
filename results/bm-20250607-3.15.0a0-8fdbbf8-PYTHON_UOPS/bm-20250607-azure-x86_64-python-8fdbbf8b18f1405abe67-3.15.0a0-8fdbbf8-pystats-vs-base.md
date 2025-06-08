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
<td align="right">5,792,182,330</td>
<td align="right">5,092,068</td>
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
<td align="right">459,026,593</td>
<td align="right">12,943,448</td>
<td align="right">-97.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,358,415</td>
<td align="right">2,268,279</td>
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
<td align="right">1,504,734,620</td>
<td align="right">199,992,327</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,585,081,810</td>
<td align="right">232,732,849</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,789,219</td>
<td align="right">103,530,114</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,403,492,042</td>
<td align="right">212,959,619</td>
<td align="right">-84.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,754,455,817</td>
<td align="right">268,431,702</td>
<td align="right">-84.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,718,912,631</td>
<td align="right">436,461,904</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,275,546,200</td>
<td align="right">205,598,436</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,621,127</td>
<td align="right">85,851,985</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">565,952,963</td>
<td align="right">95,811,572</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,124,111,422</td>
<td align="right">359,684,847</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,482,959,781</td>
<td align="right">603,162,313</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,265,394,786</td>
<td align="right">436,755,997</td>
<td align="right">-80.7%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">88,979,222</td>
<td align="right">18,516,040</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,252,080,277</td>
<td align="right">271,669,529</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">690,694,629</td>
<td align="right">152,135,345</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,277,797</td>
<td align="right">76,368,392</td>
<td align="right">-77.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,809,451</td>
<td align="right">34,936,816</td>
<td align="right">-77.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">671,907,486</td>
<td align="right">160,487,704</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,657,281,589</td>
<td align="right">429,935,903</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">187,994,216</td>
<td align="right">49,114,387</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,284,138,790</td>
<td align="right">1,976,203,408</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">626,939,612</td>
<td align="right">171,083,039</td>
<td align="right">-72.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">940,055,965</td>
<td align="right">260,808,080</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,493,160</td>
<td align="right">104,488,672</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,436,387</td>
<td align="right">145,966,113</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,140,421,096</td>
<td align="right">638,264,140</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">377,665,382</td>
<td align="right">118,482,057</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">3,434,142,035</td>
<td align="right">1,092,777,393</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,733,495,726</td>
<td align="right">873,368,191</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">56,905,472</td>
<td align="right">18,189,637</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">534,903,332</td>
<td align="right">172,574,970</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">253,095,160</td>
<td align="right">82,073,896</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">77,896,786</td>
<td align="right">25,335,102</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,531,628,151</td>
<td align="right">835,535,447</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,731,803</td>
<td align="right">183,468,459</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,839,541,158</td>
<td align="right">1,973,230,290</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">352,583,518</td>
<td align="right">120,709,665</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,387,231</td>
<td align="right">54,908,720</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,489,992,418</td>
<td align="right">872,320,306</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,243,769,005</td>
<td align="right">437,937,779</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,673,283,345</td>
<td align="right">3,858,304,477</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,389,212,175</td>
<td align="right">4,853,760,896</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,786,196</td>
<td align="right">27,120,971</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,111,717,017</td>
<td align="right">3,678,238,720</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,040,119,521</td>
<td align="right">380,543,299</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">153,224,408</td>
<td align="right">62.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">433,502,887</td>
<td align="right">163,777,522</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,358,303</td>
<td align="right">25,718,414</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,842,507</td>
<td align="right">3,121,726</td>
<td align="right">-60.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">99,732,529</td>
<td align="right">39,893,486</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">261,849,218</td>
<td align="right">105,753,539</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">22,616,447</td>
<td align="right">9,150,069</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">90,430,236</td>
<td align="right">36,710,083</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">861,439,048</td>
<td align="right">359,000,612</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">2,597,140</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,105,484,936</td>
<td align="right">899,736,428</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">795,188,542</td>
<td align="right">342,000,036</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">536,610,413</td>
<td align="right">238,436,921</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,366,470</td>
<td align="right">468,452,801</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">780,703,698</td>
<td align="right">353,061,980</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,344,782,438</td>
<td align="right">1,076,777,422</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">401,289,719</td>
<td align="right">187,873,586</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">8,531,661,185</td>
<td align="right">4,046,506,257</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">33,493,351,016</td>
<td align="right">15,973,298,113</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,022,191</td>
<td align="right">129,271,097</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,095,737,761</td>
<td align="right">535,520,122</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">256,569,729</td>
<td align="right">125,977,194</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,633</td>
<td align="right">4,866,853</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">233,988</td>
<td align="right">117,444</td>
<td align="right">-49.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">316,780,722</td>
<td align="right">160,993,658</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">201,394,525</td>
<td align="right">103,494,112</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">72,974,869</td>
<td align="right">37,751,540</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,435,919</td>
<td align="right">51,312,005</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">14,816</td>
<td align="right">7,744</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,214,780,114</td>
<td align="right">643,823,985</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,749,759</td>
<td align="right">940,509</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">355,943,029</td>
<td align="right">193,755,432</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,831,654</td>
<td align="right">86,043,533</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">283,088,088</td>
<td align="right">159,338,442</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,888,558,746</td>
<td align="right">2,198,659,268</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,542,377,233</td>
<td align="right">877,225,146</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">59,159,179</td>
<td align="right">33,677,562</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,056,461,078</td>
<td align="right">602,940,451</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,537,337,079</td>
<td align="right">880,694,951</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">116,387,114</td>
<td align="right">66,936,075</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,420,208,096</td>
<td align="right">1,413,080,044</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,343,180</td>
<td align="right">4,326,164</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">773,983,661</td>
<td align="right">456,706,681</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,164,837,288</td>
<td align="right">1,895,740,472</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,358,282,350</td>
<td align="right">820,009,353</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,143</td>
<td align="right">114,765,163</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">190,498,002</td>
<td align="right">119,444,548</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">801,850,548</td>
<td align="right">519,298,812</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,128,392</td>
<td align="right">74,930,496</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,367,659</td>
<td align="right">40,671,145</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,694,619</td>
<td align="right">80,230,603</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,297,536</td>
<td align="right">114,727,916</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">66,578,805</td>
<td align="right">43,940,842</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,750,041,495</td>
<td align="right">3,147,150,538</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">385,173,546</td>
<td align="right">259,691,688</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">485,183,030</td>
<td align="right">334,242,321</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">164,039,977</td>
<td align="right">113,102,341</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,382,717,454</td>
<td align="right">2,402,100,523</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">678,254,524</td>
<td align="right">486,795,361</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">325,847,620</td>
<td align="right">238,384,127</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">68,559,865</td>
<td align="right">52,119,267</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">840,952,846</td>
<td align="right">639,537,124</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,657,135</td>
<td align="right">1,262,432</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">233,830,288</td>
<td align="right">181,227,956</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">290,125,147</td>
<td align="right">225,531,609</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,241,061,012</td>
<td align="right">4,891,951,836</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">355,503,220</td>
<td align="right">281,004,407</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,215,655,075</td>
<td align="right">2,550,784,247</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">468,044,535</td>
<td align="right">381,141,654</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,122,133</td>
<td align="right">2,550,465</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">346,674,152</td>
<td align="right">285,137,917</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">80,980,805</td>
<td align="right">67,191,531</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">943,020,678</td>
<td align="right">798,534,288</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,359,081,257</td>
<td align="right">4,614,344,270</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">72,576,742</td>
<td align="right">62,511,414</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">267,733,339</td>
<td align="right">234,988,821</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,316,955</td>
<td align="right">366,827,475</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">975,005,572</td>
<td align="right">863,012,612</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">335,120,069</td>
<td align="right">298,927,859</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">147,886,771</td>
<td align="right">132,496,284</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">76,781</td>
<td align="right">69,551</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">61,064,676</td>
<td align="right">55,569,629</td>
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
<td align="right">75,216,102</td>
<td align="right">69,154,674</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">66,481,426</td>
<td align="right">61,279,427</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">70,521,660</td>
<td align="right">65,525,953</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,165,349</td>
<td align="right">5,799,295</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,098,361</td>
<td align="right">9,507,088</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,844,471</td>
<td align="right">19,815,285</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,171,221</td>
<td align="right">20,142,035</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,171,240</td>
<td align="right">20,142,054</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">463,959</td>
<td align="right">441,455</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,097,849</td>
<td align="right">9,680,340</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,112,304,323</td>
<td align="right">1,066,435,532</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">12,705,510</td>
<td align="right">12,202,287</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">75,636,607</td>
<td align="right">73,160,692</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,631</td>
<td align="right">13,034</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,706</td>
<td align="right">123,859,844</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">65,686,370</td>
<td align="right">63,788,864</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">72,271,460</td>
<td align="right">70,197,302</td>
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
<td align="right">3,090,888</td>
<td align="right">3,024,264</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,555,373</td>
<td align="right">27,974,934</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">243,222</td>
<td align="right">248,091</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,431,152</td>
<td align="right">5,347,696</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,961,113</td>
<td align="right">35,546,989</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,587,182,744</td>
<td align="right">1,569,045,241</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">115,333,020</td>
<td align="right">114,403,157</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">190,447,282</td>
<td align="right">189,431,797</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,966,351</td>
<td align="right">418,214,503</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,519,648</td>
<td align="right">241,671,608</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,569,811</td>
<td align="right">243,720,365</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,544,189</td>
<td align="right">591,602,865</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,097,007</td>
<td align="right">155,716,430</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,658,183</td>
<td align="right">302,244,071</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,628</td>
<td align="right">72,564</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,357</td>
<td align="right">5,360</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,756,328</td>
<td align="right">14,760,221</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,301,989</td>
<td align="right">131,286,177</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,694</td>
<td align="right">33,691</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">214,357</td>
<td align="right">214,356</td>
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
<td align="right">128,851,743</td>
<td align="right">128,851,743</td>
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
<td align="right">10,549,278</td>
<td align="right">10,549,278</td>
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
<td align="right">56,995</td>
<td align="right">56,995</td>
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
<td align="right">966,720,117</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">901,765,291</td>
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
<td align="right">16,240,029,263</td>
<td align="right">87.1%</td>
<td align="right">3,936,393,112</td>
<td align="right">77.7%</td>
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
<td align="right">2,343,852,155</td>
<td align="right">12.6%</td>
<td align="right">1,076,296,190</td>
<td align="right">21.2%</td>
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
<td align="right">62,403,706</td>
<td align="right">0.3%</td>
<td align="right">55,486,560</td>
<td align="right">1.1%</td>
<td align="right">-11.1%</td>
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
<td align="right">913,023</td>
<td align="right">43.3%</td>
<td align="right">462,812</td>
<td align="right">30.3%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,194,435</td>
<td align="right">56.7%</td>
<td align="right">1,065,124</td>
<td align="right">69.7%</td>
<td align="right">-10.8%</td>
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
<td align="right">74,223</td>
<td align="right">8.1%</td>
<td align="right">18,451</td>
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
<td align="right">1,096</td>
<td align="right">0.1%</td>
<td align="right">334</td>
<td align="right">0.1%</td>
<td align="right">-69.5%</td>
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
<td align="right">23,514</td>
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
<td align="right">43,458</td>
<td align="right">4.8%</td>
<td align="right">21,784</td>
<td align="right">4.7%</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,984</td>
<td align="right">3.7%</td>
<td align="right">19,848</td>
<td align="right">4.3%</td>
<td align="right">-41.6%</td>
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
<td align="right">35,905</td>
<td align="right">3.9%</td>
<td align="right">22,400</td>
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
<td align="right">78,858</td>
<td align="right">8.6%</td>
<td align="right">63,018</td>
<td align="right">13.6%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">8,166</td>
<td align="right">0.9%</td>
<td align="right">6,693</td>
<td align="right">1.4%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">42,915</td>
<td align="right">4.7%</td>
<td align="right">36,124</td>
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
<td align="left">true divide different types</td>
<td align="right">2,035</td>
<td align="right">0.2%</td>
<td align="right">1,996</td>
<td align="right">0.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">7,087</td>
<td align="right">0.8%</td>
<td align="right">6,958</td>
<td align="right">1.5%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">636</td>
<td align="right">0.1%</td>
<td align="right">629</td>
<td align="right">0.1%</td>
<td align="right">-1.1%</td>
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
<td align="left">subscr string slice</td>
<td align="right">2,336</td>
<td align="right">0.3%</td>
<td align="right">2,334</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">107,941</td>
<td align="right">11.8%</td>
<td align="right">107,938</td>
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
<td align="right">545,731,803</td>
<td align="right">100.0%</td>
<td align="right">183,468,459</td>
<td align="right">100.0%</td>
<td align="right">-66.4%</td>
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
<td align="right">11,105,364,683</td>
<td align="right">98.4%</td>
<td align="right">5,036,163,292</td>
<td align="right">97.1%</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">182,106,050</td>
<td align="right">1.6%</td>
<td align="right">149,683,961</td>
<td align="right">2.9%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">178,744,301</td>
<td align="right">1.6%</td>
<td align="right">146,934,007</td>
<td align="right">2.8%</td>
<td align="right">-17.8%</td>
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
<td align="right">3,604,825</td>
<td align="right">100.0%</td>
<td align="right">2,997,899</td>
<td align="right">100.0%</td>
<td align="right">-16.8%</td>
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
<td align="right">19,927</td>
<td align="right">100.0%</td>
<td align="right">20,330</td>
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
<td align="right">510,395,884</td>
<td align="right">10.2%</td>
<td align="right">85,736,809</td>
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
<td align="right">4,505,841,770</td>
<td align="right">89.8%</td>
<td align="right">1,219,729,390</td>
<td align="right">93.3%</td>
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
<td align="right">1,270,909</td>
<td align="right">0.0%</td>
<td align="right">1,136,813</td>
<td align="right">0.1%</td>
<td align="right">-10.6%</td>
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
<td align="right">207,513</td>
<td align="right">83.4%</td>
<td align="right">96,997</td>
<td align="right">71.1%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">41,399</td>
<td align="right">16.6%</td>
<td align="right">39,436</td>
<td align="right">28.9%</td>
<td align="right">-4.7%</td>
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
<td align="right">90,412</td>
<td align="right">43.6%</td>
<td align="right">4,118</td>
<td align="right">4.2%</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,831</td>
<td align="right">3.3%</td>
<td align="right">372</td>
<td align="right">0.4%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">10,441</td>
<td align="right">5.0%</td>
<td align="right">4,519</td>
<td align="right">4.7%</td>
<td align="right">-56.7%</td>
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
<td align="right">45,432</td>
<td align="right">21.9%</td>
<td align="right">36,529</td>
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
<td align="left">bool</td>
<td align="right">1,884</td>
<td align="right">0.9%</td>
<td align="right">1,920</td>
<td align="right">2.0%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,295</td>
<td align="right">11.2%</td>
<td align="right">23,073</td>
<td align="right">23.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,744</td>
<td align="right">3.7%</td>
<td align="right">7,719</td>
<td align="right">8.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,649</td>
<td align="right">3.7%</td>
<td align="right">7,648</td>
<td align="right">7.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">998</td>
<td align="right">0.5%</td>
<td align="right">998</td>
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
<td align="right">2,186,555,117</td>
<td align="right">93.4%</td>
<td align="right">431,480,705</td>
<td align="right">83.3%</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,403,587</td>
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
<td align="right">153,771,477</td>
<td align="right">6.6%</td>
<td align="right">85,999,561</td>
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
<td align="right">28,589</td>
<td align="right">33.0%</td>
<td align="right">16,053</td>
<td align="right">27.8%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">58,067</td>
<td align="right">67.0%</td>
<td align="right">41,662</td>
<td align="right">72.2%</td>
<td align="right">-28.3%</td>
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
<td align="right">21,455</td>
<td align="right">36.9%</td>
<td align="right">9,860</td>
<td align="right">23.7%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,604</td>
<td align="right">25.2%</td>
<td align="right">11,984</td>
<td align="right">28.8%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,995</td>
<td align="right">18.9%</td>
<td align="right">9,315</td>
<td align="right">22.4%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,013</td>
<td align="right">19.0%</td>
<td align="right">10,503</td>
<td align="right">25.2%</td>
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
<td align="right">1,504,293,656</td>
<td align="right">29.3%</td>
<td align="right">199,879,058</td>
<td align="right">13.5%</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,977,365</td>
<td align="right">3.2%</td>
<td align="right">55,723,559</td>
<td align="right">3.8%</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,473,406,744</td>
<td align="right">67.5%</td>
<td align="right">1,225,126,449</td>
<td align="right">82.7%</td>
<td align="right">-64.7%</td>
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
<td align="right">435,572</td>
<td align="right">12.3%</td>
<td align="right">107,872</td>
<td align="right">9.3%</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,099,123</td>
<td align="right">87.7%</td>
<td align="right">1,056,611</td>
<td align="right">90.7%</td>
<td align="right">-65.9%</td>
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
<td align="right">4,178</td>
<td align="right">3.9%</td>
<td align="right">-97.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,676</td>
<td align="right">19.2%</td>
<td align="right">10,875</td>
<td align="right">10.1%</td>
<td align="right">-87.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,707</td>
<td align="right">8.0%</td>
<td align="right">6,499</td>
<td align="right">6.0%</td>
<td align="right">-81.3%</td>
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
<td align="right">10,543</td>
<td align="right">2.4%</td>
<td align="right">3,376</td>
<td align="right">3.1%</td>
<td align="right">-68.0%</td>
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
<td align="left">seq iter</td>
<td align="right">18,283</td>
<td align="right">4.2%</td>
<td align="right">5,891</td>
<td align="right">5.5%</td>
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
<td align="right">3,138</td>
<td align="right">0.7%</td>
<td align="right">1,126</td>
<td align="right">1.0%</td>
<td align="right">-64.1%</td>
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
<td align="right">1,638</td>
<td align="right">1.5%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">180</td>
<td align="right">0.2%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">69,536</td>
<td align="right">16.0%</td>
<td align="right">48,717</td>
<td align="right">45.2%</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">18,030</td>
<td align="right">4.1%</td>
<td align="right">12,917</td>
<td align="right">12.0%</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,284</td>
<td align="right">1.0%</td>
<td align="right">3,293</td>
<td align="right">3.1%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,083</td>
<td align="right">1.4%</td>
<td align="right">5,197</td>
<td align="right">4.8%</td>
<td align="right">-14.6%</td>
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
<td align="right">2,710,702</td>
<td align="right">2,710,702 / 0 !!</td>
<td align="right">1,674,734</td>
<td align="right">1,674,734 / 0 !!</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">119,408,527</td>
<td align="right">119,408,527 / 0 !!</td>
<td align="right">111,963,101</td>
<td align="right">111,963,101 / 0 !!</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">304,489,198</td>
<td align="right">304,489,198 / 0 !!</td>
<td align="right">298,553,436</td>
<td align="right">298,553,436 / 0 !!</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,509,055</td>
<td align="right">5,509,055 / 0 !!</td>
<td align="right">5,422,274</td>
<td align="right">5,422,274 / 0 !!</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,933,003</td>
<td align="right">34,933,003 / 0 !!</td>
<td align="right">34,420,285</td>
<td align="right">34,420,285 / 0 !!</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">101,924,833</td>
<td align="right">101,924,833 / 0 !!</td>
<td align="right">101,415,656</td>
<td align="right">101,415,656 / 0 !!</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,112,023</td>
<td align="right">12,112,023 / 0 !!</td>
<td align="right">12,166,399</td>
<td align="right">12,166,399 / 0 !!</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">171,864,188</td>
<td align="right">171,864,188 / 0 !!</td>
<td align="right">171,393,505</td>
<td align="right">171,393,505 / 0 !!</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">341,959,101</td>
<td align="right">341,959,101 / 0 !!</td>
<td align="right">341,396,859</td>
<td align="right">341,396,859 / 0 !!</td>
<td align="right">-0.2%</td>
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
<td align="right">11,985,566,326</td>
<td align="right">87.8%</td>
<td align="right">6,671,432,540</td>
<td align="right">85.5%</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">800,077,846</td>
<td align="right">5.9%</td>
<td align="right">517,609,150</td>
<td align="right">6.6%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,438,767</td>
<td align="right">0.0%</td>
<td align="right">1,005,161</td>
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
<td align="right">860,613,588</td>
<td align="right">6.3%</td>
<td align="right">615,194,931</td>
<td align="right">7.9%</td>
<td align="right">-28.5%</td>
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
<td align="right">16,316,673</td>
<td align="right">97.0%</td>
<td align="right">11,693,309</td>
<td align="right">96.4%</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">505,672</td>
<td align="right">3.0%</td>
<td align="right">431,826</td>
<td align="right">3.6%</td>
<td align="right">-14.6%</td>
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
<td align="right">73,630</td>
<td align="right">14.6%</td>
<td align="right">35,566</td>
<td align="right">8.2%</td>
<td align="right">-51.7%</td>
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
<td align="right">39,655</td>
<td align="right">9.2%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,324</td>
<td align="right">1.1%</td>
<td align="right">4,086</td>
<td align="right">0.9%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,156</td>
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
<td align="right">0.6%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,813</td>
<td align="right">3.1%</td>
<td align="right">13,846</td>
<td align="right">3.2%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">53,206</td>
<td align="right">10.5%</td>
<td align="right">47,295</td>
<td align="right">11.0%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,720</td>
<td align="right">0.3%</td>
<td align="right">1,693</td>
<td align="right">0.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">24,469</td>
<td align="right">4.8%</td>
<td align="right">24,156</td>
<td align="right">5.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,841</td>
<td align="right">0.4%</td>
<td align="right">1,839</td>
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
<td align="right">9,222,210,228</td>
<td align="right">99.8%</td>
<td align="right">4,375,283,025</td>
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
<td align="right">48,384</td>
<td align="right">0.0%</td>
<td align="right">47,788</td>
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
<td align="right">14,622,455</td>
<td align="right">0.2%</td>
<td align="right">14,622,453</td>
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
<td align="right">134,578</td>
<td align="right">100.0%</td>
<td align="right">138,473</td>
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
<td align="right">64,155,564</td>
<td align="right">100.0%</td>
<td align="right">58,593,893</td>
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
<td align="right">593,529,478</td>
<td align="right">82.2%</td>
<td align="right">591,588,154</td>
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
<td align="right">128,816,945</td>
<td align="right">17.8%</td>
<td align="right">128,816,945</td>
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
<td align="right">1,812,783,037</td>
<td align="right">90.9%</td>
<td align="right">1,566,339,576</td>
<td align="right">90.4%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">114,220,009</td>
<td align="right">5.7%</td>
<td align="right">104,184,120</td>
<td align="right">6.0%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">66,396,838</td>
<td align="right">3.3%</td>
<td align="right">61,194,451</td>
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
<td align="right">2,194,017</td>
<td align="right">98.0%</td>
<td align="right">2,006,575</td>
<td align="right">97.9%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">44,923</td>
<td align="right">2.0%</td>
<td align="right">43,671</td>
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
<td align="left">other</td>
<td align="right">248,236</td>
<td align="right">552.6%</td>
<td align="right">239,551</td>
<td align="right">548.5%</td>
<td align="right">-3.5%</td>
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
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,340</td>
<td align="right">7.4%</td>
<td align="right">3,344</td>
<td align="right">7.7%</td>
<td align="right">0.1%</td>
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
<td align="right">16.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">753</td>
<td align="right">1.7%</td>
<td align="right">753</td>
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
<td align="right">700,605,317</td>
<td align="right">43.3%</td>
<td align="right">103,491,806</td>
<td align="right">32.3%</td>
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
<td align="right">918,534,261</td>
<td align="right">56.7%</td>
<td align="right">216,519,017</td>
<td align="right">67.7%</td>
<td align="right">-76.4%</td>
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
<td align="right">255,922,635</td>
<td align="right">5.0%</td>
<td align="right">125,492,135</td>
<td align="right">4.4%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,728,934,916</td>
<td align="right">92.8%</td>
<td align="right">2,653,789,428</td>
<td align="right">93.4%</td>
<td align="right">-43.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">110,683,167</td>
<td align="right">2.2%</td>
<td align="right">62,452,205</td>
<td align="right">2.2%</td>
<td align="right">-43.6%</td>
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
<td align="right">2,136,855</td>
<td align="right">78.2%</td>
<td align="right">1,227,999</td>
<td align="right">73.9%</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">596,948</td>
<td align="right">21.8%</td>
<td align="right">433,873</td>
<td align="right">26.1%</td>
<td align="right">-27.3%</td>
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
<td align="right">126,705</td>
<td align="right">21.2%</td>
<td align="right">27,675</td>
<td align="right">6.4%</td>
<td align="right">-78.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,856</td>
<td align="right">3.2%</td>
<td align="right">4,655</td>
<td align="right">1.1%</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">72,063</td>
<td align="right">12.1%</td>
<td align="right">38,958</td>
<td align="right">9.0%</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">16,308</td>
<td align="right">2.7%</td>
<td align="right">9,741</td>
<td align="right">2.2%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">83,562</td>
<td align="right">14.0%</td>
<td align="right">74,370</td>
<td align="right">17.1%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,724</td>
<td align="right">1.6%</td>
<td align="right">8,710</td>
<td align="right">2.0%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,049</td>
<td align="right">1.7%</td>
<td align="right">10,080</td>
<td align="right">2.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">257,839</td>
<td align="right">43.2%</td>
<td align="right">257,842</td>
<td align="right">59.4%</td>
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
<td align="right">1,237,628,095</td>
<td align="right">99.9%</td>
<td align="right">646,844,846</td>
<td align="right">99.8%</td>
<td align="right">-47.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,646,406</td>
<td align="right">0.1%</td>
<td align="right">1,251,703</td>
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
<td align="right">920</td>
<td align="right">8.5%</td>
<td align="right">800</td>
<td align="right">7.4%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">9,889</td>
<td align="right">91.5%</td>
<td align="right">10,009</td>
<td align="right">92.6%</td>
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
<td align="right">685</td>
<td align="right">74.5%</td>
<td align="right">566</td>
<td align="right">70.8%</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">99</td>
<td align="right">10.8%</td>
<td align="right">98</td>
<td align="right">12.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">14.8%</td>
<td align="right">136</td>
<td align="right">17.0%</td>
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
<td align="right">8,239,378,799</td>
<td align="right">3.9%</td>
<td align="right">3,124,109,967</td>
<td align="right">3.2%</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">78,580,060,006</td>
<td align="right">37.3%</td>
<td align="right">34,703,466,485</td>
<td align="right">35.9%</td>
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
<td align="right">122,128,888,736</td>
<td align="right">58.0%</td>
<td align="right">57,688,346,809</td>
<td align="right">59.7%</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,497,486,329</td>
<td align="right">0.7%</td>
<td align="right">1,045,401,688</td>
<td align="right">1.1%</td>
<td align="right">-30.2%</td>
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
<td align="right">1,504,293,656</td>
<td align="right">20.6%</td>
<td align="right">199,879,058</td>
<td align="right">7.3%</td>
<td align="right">-86.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,605,317</td>
<td align="right">9.6%</td>
<td align="right">103,491,806</td>
<td align="right">3.8%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,395,884</td>
<td align="right">7.0%</td>
<td align="right">85,736,809</td>
<td align="right">3.1%</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,731,803</td>
<td align="right">7.5%</td>
<td align="right">183,468,459</td>
<td align="right">6.7%</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,343,852,155</td>
<td align="right">32.0%</td>
<td align="right">1,076,296,190</td>
<td align="right">39.4%</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">255,922,635</td>
<td align="right">3.5%</td>
<td align="right">125,492,135</td>
<td align="right">4.6%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">153,771,477</td>
<td align="right">2.1%</td>
<td align="right">85,999,561</td>
<td align="right">3.1%</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">800,077,846</td>
<td align="right">10.9%</td>
<td align="right">517,609,150</td>
<td align="right">18.9%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">178,744,301</td>
<td align="right">2.4%</td>
<td align="right">146,934,007</td>
<td align="right">5.4%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,945</td>
<td align="right">1.8%</td>
<td align="right">128,816,945</td>
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
<td align="right">82,000,546</td>
<td align="right">5.5%</td>
<td align="right">27,819,086</td>
<td align="right">2.7%</td>
<td align="right">-66.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,899,424</td>
<td align="right">5.5%</td>
<td align="right">27,827,925</td>
<td align="right">2.7%</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,376,042</td>
<td align="right">3.3%</td>
<td align="right">26,804,525</td>
<td align="right">2.6%</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,476,507</td>
<td align="right">3.6%</td>
<td align="right">29,926,052</td>
<td align="right">2.9%</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">365,459,314</td>
<td align="right">24.4%</td>
<td align="right">220,414,576</td>
<td align="right">21.1%</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">81,670,466</td>
<td align="right">5.5%</td>
<td align="right">53,112,400</td>
<td align="right">5.1%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">264,671,267</td>
<td align="right">17.7%</td>
<td align="right">175,564,671</td>
<td align="right">16.8%</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">89,935,833</td>
<td align="right">6.0%</td>
<td align="right">83,880,175</td>
<td align="right">8.0%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">93,987,984</td>
<td align="right">6.3%</td>
<td align="right">87,790,732</td>
<td align="right">8.4%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">82,835,868</td>
<td align="right">5.5%</td>
<td align="right">80,681,057</td>
<td align="right">7.7%</td>
<td align="right">-2.6%</td>
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
<td align="right">5,095,043,803</td>
<td align="right">76.2%</td>
<td align="right">4,980,541,459</td>
<td align="right">76.0%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,471,636</td>
<td align="right">8.7%</td>
<td align="right">575,151,368</td>
<td align="right">8.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,416,130,644</td>
<td align="right">81.0%</td>
<td align="right">5,330,095,704</td>
<td align="right">81.3%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">275,686,944</td>
<td align="right">4.1%</td>
<td align="right">271,436,415</td>
<td align="right">4.1%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,037,686</td>
<td align="right">1.1%</td>
<td align="right">70,104,057</td>
<td align="right">1.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,591,670,361</td>
<td align="right">23.8%</td>
<td align="right">1,573,532,850</td>
<td align="right">24.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,591,670,361</td>
<td align="right">23.8%</td>
<td align="right">1,573,532,850</td>
<td align="right">24.0%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,007,198,725</td>
<td align="right">15.1%</td>
<td align="right">998,381,482</td>
<td align="right">15.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,002,921,404</td>
<td align="right">15.0%</td>
<td align="right">996,249,356</td>
<td align="right">15.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">259,483,469</td>
<td align="right">3.9%</td>
<td align="right">258,591,611</td>
<td align="right">3.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">23,591,225</td>
<td align="right">0.4%</td>
<td align="right">23,551,272</td>
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
<td align="right">26,292,859</td>
<td align="right"></td>
<td align="right">5,478,938</td>
<td align="right"></td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">80,063,300</td>
<td align="right"></td>
<td align="right">56,722,171</td>
<td align="right"></td>
<td align="right">-29.2%</td>
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
<td align="left">Method cache hits</td>
<td align="right">2,365,497,833</td>
<td align="right"></td>
<td align="right">2,145,563,336</td>
<td align="right"></td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">54,574,230</td>
<td align="right"></td>
<td align="right">52,048,071</td>
<td align="right"></td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">22,990,254,539</td>
<td align="right">25.1%</td>
<td align="right">22,478,987,716</td>
<td align="right">24.8%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,860,391,467</td>
<td align="right">1.7%</td>
<td align="right">1,820,984,914</td>
<td align="right">1.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">24,957,971,961</td>
<td align="right">27.2%</td>
<td align="right">24,446,842,268</td>
<td align="right">27.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,573,444,367</td>
<td align="right"></td>
<td align="right">13,331,931,077</td>
<td align="right"></td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,573,299,212</td>
<td align="right">70.9%</td>
<td align="right">13,331,825,072</td>
<td align="right">70.8%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,940,864,509</td>
<td align="right">22.9%</td>
<td align="right">24,535,709,598</td>
<td align="right">22.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">31,766,204,028</td>
<td align="right">29.2%</td>
<td align="right">31,269,063,356</td>
<td align="right">29.1%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,484,794,555</td>
<td align="right">28.7%</td>
<td align="right">5,425,527,269</td>
<td align="right">28.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,562,426,078</td>
<td align="right">29.1%</td>
<td align="right">5,502,966,597</td>
<td align="right">29.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,159,734,459</td>
<td align="right"></td>
<td align="right">6,095,771,814</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,643,319,023</td>
<td align="right">5.1%</td>
<td align="right">4,596,478,440</td>
<td align="right">5.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,427,955,330</td>
<td align="right"></td>
<td align="right">2,407,463,104</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">50,151,373,037</td>
<td align="right">46.1%</td>
<td align="right">49,754,949,193</td>
<td align="right">46.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">174,612,630</td>
<td align="right"></td>
<td align="right">173,355,645</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,266,245</td>
<td align="right">0.4%</td>
<td align="right">71,075,115</td>
<td align="right">0.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">39,077,247,220</td>
<td align="right">42.6%</td>
<td align="right">38,972,913,516</td>
<td align="right">43.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,365,278</td>
<td align="right">0.0%</td>
<td align="right">6,364,213</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,404,481</td>
<td align="right">1.9%</td>
<td align="right">3,404,481</td>
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
<td align="right">364,827</td>
<td align="right">101,642,387</td>
<td align="right">9,559,256,557</td>
<td align="right">761,545,581</td>
<td align="right">765,755,693</td>
<td align="right">362,976</td>
<td align="right">99,331,545</td>
<td align="right">9,471,629,635</td>
<td align="right">750,634,817</td>
<td align="right">761,100,065</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,678,076,580</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,500</td>
<td align="right">5,678,335,336</td>
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
Stats gathered on: 2025-06-08
