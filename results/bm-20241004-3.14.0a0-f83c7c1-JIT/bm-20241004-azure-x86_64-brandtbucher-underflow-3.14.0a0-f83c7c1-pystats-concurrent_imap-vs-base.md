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
<td align="left">YIELD_VALUE</td>
<td align="right">6,337,380</td>
<td align="right">19,064</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">1,212,805</td>
<td align="right">7,341</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,464,219</td>
<td align="right">36,563</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,277,771</td>
<td align="right">32,048</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,279,011</td>
<td align="right">56,235</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">625,605</td>
<td align="right">90,633</td>
<td align="right">-85.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">486,093</td>
<td align="right">86,358</td>
<td align="right">-82.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,557,759</td>
<td align="right">566,212</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,241,926</td>
<td align="right">282,742</td>
<td align="right">-77.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">3,829,466</td>
<td align="right">875,565</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">79,200</td>
<td align="right">20,115</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">14,029,294</td>
<td align="right">3,665,821</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,567,026</td>
<td align="right">724,994</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,606,682</td>
<td align="right">763,185</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,758,732</td>
<td align="right">545,137</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">9,002,013</td>
<td align="right">2,817,221</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">4,952,735</td>
<td align="right">1,657,086</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">13,004,810</td>
<td align="right">4,540,557</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">4,326,331</td>
<td align="right">1,516,813</td>
<td align="right">-64.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,966,930</td>
<td align="right">725,346</td>
<td align="right">-63.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">29,799,261</td>
<td align="right">11,182,796</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,454,531</td>
<td align="right">923,668</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">19,971,911</td>
<td align="right">7,584,431</td>
<td align="right">-62.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">8,216,900</td>
<td align="right">3,132,664</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">822,782</td>
<td align="right">314,458</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">3,296,910</td>
<td align="right">1,262,386</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">10,808,276</td>
<td align="right">4,179,399</td>
<td align="right">-61.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,493,050</td>
<td align="right">966,900</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,699,839</td>
<td align="right">3,766,146</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">22,952,898</td>
<td align="right">8,917,548</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">3,342,770</td>
<td align="right">1,299,206</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,669,125</td>
<td align="right">651,343</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">5,028,286</td>
<td align="right">1,979,905</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">3,391,370</td>
<td align="right">1,347,406</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">849,894</td>
<td align="right">339,226</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,545,431</td>
<td align="right">1,016,170</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,694,233</td>
<td align="right">677,183</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">851,354</td>
<td align="right">340,686</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">24,906,559</td>
<td align="right">10,000,003</td>
<td align="right">-59.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,151,430</td>
<td align="right">866,699</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,594,979</td>
<td align="right">1,050,569</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">16,248,532</td>
<td align="right">6,615,019</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">8,971,611</td>
<td align="right">3,660,213</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">434,758</td>
<td align="right">177,925</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,397,627</td>
<td align="right">4,670,733</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">464,398</td>
<td align="right">193,275</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">13,379,194</td>
<td align="right">5,620,543</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,760,425</td>
<td align="right">741,203</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">17,461,640</td>
<td align="right">7,431,968</td>
<td align="right">-57.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">446,911</td>
<td align="right">190,629</td>
<td align="right">-57.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">220</td>
<td align="right">95</td>
<td align="right">-56.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">16,963,086</td>
<td align="right">7,416,011</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">111,224,121</td>
<td align="right">48,689,813</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,918,039</td>
<td align="right">1,299,929</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">9,603,831</td>
<td align="right">4,381,057</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">31,704,594</td>
<td align="right">14,574,994</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">854,345</td>
<td align="right">394,407</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,915,076</td>
<td align="right">2,757,836</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,678,321</td>
<td align="right">2,288,041</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">20,408,897</td>
<td align="right">9,991,274</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">10,560</td>
<td align="right">5,200</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,578,824</td>
<td align="right">2,764,200</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">6,784,932</td>
<td align="right">3,419,924</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">36,476,233</td>
<td align="right">18,884,434</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,431,887</td>
<td align="right">756,949</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">340</td>
<td align="right">180</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,123,687</td>
<td align="right">595,054</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">4,033,884</td>
<td align="right">2,248,109</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">4,789,064</td>
<td align="right">2,672,132</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,007,077</td>
<td align="right">576,680</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">47,005</td>
<td align="right">28,973</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">11,103,078</td>
<td align="right">6,964,055</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,380</td>
<td align="right">1,540</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">3,600</td>
<td align="right">2,440</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">13,541,180</td>
<td align="right">9,182,953</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">144,776</td>
<td align="right">102,862</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">64,469</td>
<td align="right">48,238</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">38,400</td>
<td align="right">29,440</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">45,700</td>
<td align="right">35,860</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">2,090,237</td>
<td align="right">1,644,160</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">84,980</td>
<td align="right">66,925</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">136,342</td>
<td align="right">107,575</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">50,860</td>
<td align="right">40,180</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">218,698</td>
<td align="right">173,606</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">55,448</td>
<td align="right">46,348</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">1,040</td>
<td align="right">880</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">19,280</td>
<td align="right">16,485</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">8,084</td>
<td align="right">7,104</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">80,489</td>
<td align="right">70,978</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">124,531</td>
<td align="right">111,800</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">59,680</td>
<td align="right">54,520</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">250,382</td>
<td align="right">228,822</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">18,930</td>
<td align="right">17,865</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">197,504</td>
<td align="right">187,548</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">24,210</td>
<td align="right">23,065</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">24,210</td>
<td align="right">23,065</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">34,740</td>
<td align="right">33,140</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">22,400</td>
<td align="right">21,440</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">393,173</td>
<td align="right">376,731</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">11,780</td>
<td align="right">11,300</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">11,780</td>
<td align="right">11,300</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">29,462</td>
<td align="right">28,364</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">6,580</td>
<td align="right">6,340</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">37,506</td>
<td align="right">36,388</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">97,960</td>
<td align="right">95,160</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,160</td>
<td align="right">16,700</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">33,400</td>
<td align="right">32,520</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">71,620</td>
<td align="right">69,780</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">51,720</td>
<td align="right">50,440</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">49,000</td>
<td align="right">47,800</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">16,980</td>
<td align="right">16,580</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">40,560</td>
<td align="right">39,607</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">71,580</td>
<td align="right">69,900</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">548,136</td>
<td align="right">536,082</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">28,000</td>
<td align="right">27,400</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">88,480</td>
<td align="right">86,740</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">71,247</td>
<td align="right">69,865</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">37,480</td>
<td align="right">36,760</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">65,800</td>
<td align="right">64,600</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">108,980</td>
<td align="right">107,220</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">62,080</td>
<td align="right">61,120</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">44,460</td>
<td align="right">43,774</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,280</td>
<td align="right">5,200</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">15,900</td>
<td align="right">15,660</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,400</td>
<td align="right">5,320</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">17,180</td>
<td align="right">16,941</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">11,540</td>
<td align="right">11,380</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">11,680</td>
<td align="right">11,520</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,268,287</td>
<td align="right">2,241,036</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">26,100</td>
<td align="right">25,860</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">131,360</td>
<td align="right">130,160</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">132,060</td>
<td align="right">130,860</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">38,900</td>
<td align="right">38,660</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">25,652</td>
<td align="right">25,579</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">35,206</td>
<td align="right">35,117</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">8,320</td>
<td align="right">8,314</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">25,479</td>
<td align="right">25,493</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">18,640</td>
<td align="right">18,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,860</td>
<td align="right">4,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,540</td>
<td align="right">1,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,220</td>
<td align="right">1,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">560</td>
<td align="right">560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">460</td>
<td align="right">460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">400</td>
<td align="right">400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">320</td>
<td align="right">320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
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
<td align="right">10,800,551</td>
<td align="right">80.7%</td>
<td align="right">4,173,491</td>
<td align="right">70.1%</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,573,806</td>
<td align="right">19.2%</td>
<td align="right">1,770,749</td>
<td align="right">29.8%</td>
<td align="right">-31.2%</td>
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
<td align="right">7,065</td>
<td align="right">91.5%</td>
<td align="right">5,248</td>
<td align="right">88.8%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">660</td>
<td align="right">8.5%</td>
<td align="right">660</td>
<td align="right">11.2%</td>
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
<td align="left">or</td>
<td align="right">1,998</td>
<td align="right">28.3%</td>
<td align="right">1,378</td>
<td align="right">26.3%</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">200</td>
<td align="right">2.8%</td>
<td align="right">140</td>
<td align="right">2.7%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,555</td>
<td align="right">50.3%</td>
<td align="right">2,521</td>
<td align="right">48.0%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">640</td>
<td align="right">9.1%</td>
<td align="right">589</td>
<td align="right">11.2%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">672</td>
<td align="right">9.5%</td>
<td align="right">620</td>
<td align="right">11.8%</td>
<td align="right">-7.7%</td>
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
<td align="right">19,280</td>
<td align="right">100.0%</td>
<td align="right">16,485</td>
<td align="right">100.0%</td>
<td align="right">-14.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,091,702</td>
<td align="right">95.2%</td>
<td align="right">575,218</td>
<td align="right">92.5%</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">54,564</td>
<td align="right">4.8%</td>
<td align="right">45,504</td>
<td align="right">7.3%</td>
<td align="right">-16.6%</td>
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
<td align="right">584</td>
<td align="right">66.1%</td>
<td align="right">544</td>
<td align="right">64.5%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">300</td>
<td align="right">33.9%</td>
<td align="right">300</td>
<td align="right">35.5%</td>
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
<td align="right">584</td>
<td align="right">100.0%</td>
<td align="right">544</td>
<td align="right">100.0%</td>
<td align="right">-6.8%</td>
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
<td align="right">45,909,744</td>
<td align="right">99.9%</td>
<td align="right">22,189,385</td>
<td align="right">99.8%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,840</td>
<td align="right">0.0%</td>
<td align="right">4,360</td>
<td align="right">0.0%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">19,298</td>
<td align="right">0.0%</td>
<td align="right">19,272</td>
<td align="right">0.1%</td>
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
<td align="right">16,788</td>
<td align="right">100.0%</td>
<td align="right">16,725</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">53.2%</td>
<td align="right">820</td>
<td align="right">53.2%</td>
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
<td align="right">1,275,843</td>
<td align="right">14.4%</td>
<td align="right">53,582</td>
<td align="right">1.2%</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,568,195</td>
<td align="right">85.5%</td>
<td align="right">4,398,376</td>
<td align="right">98.6%</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6,400</td>
<td align="right">0.1%</td>
<td align="right">6,320</td>
<td align="right">0.1%</td>
<td align="right">-1.2%</td>
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
<td align="right">1,414</td>
<td align="right">43.3%</td>
<td align="right">909</td>
<td align="right">33.0%</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,854</td>
<td align="right">56.7%</td>
<td align="right">1,844</td>
<td align="right">67.0%</td>
<td align="right">-0.5%</td>
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
<td align="left">float long</td>
<td align="right">922</td>
<td align="right">65.2%</td>
<td align="right">500</td>
<td align="right">55.0%</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">172</td>
<td align="right">12.2%</td>
<td align="right">140</td>
<td align="right">15.4%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">320</td>
<td align="right">22.6%</td>
<td align="right">269</td>
<td align="right">29.6%</td>
<td align="right">-15.9%</td>
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
<td align="right">3,373,984</td>
<td align="right">100.0%</td>
<td align="right">1,586,842</td>
<td align="right">100.0%</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">180</td>
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
<td align="right">140</td>
<td align="right">100.0%</td>
<td align="right">140</td>
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
<td align="right">8,432,128</td>
<td align="right">99.6%</td>
<td align="right">6,500,378</td>
<td align="right">99.5%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">31,640</td>
<td align="right">0.4%</td>
<td align="right">30,820</td>
<td align="right">0.5%</td>
<td align="right">-2.6%</td>
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
<td align="right">1,040</td>
<td align="right">59.1%</td>
<td align="right">1,000</td>
<td align="right">58.8%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">720</td>
<td align="right">40.9%</td>
<td align="right">700</td>
<td align="right">41.2%</td>
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
<td align="left">callable</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">180</td>
<td align="right">18.0%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">260</td>
<td align="right">25.0%</td>
<td align="right">240</td>
<td align="right">24.0%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">200</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">200</td>
<td align="right">19.2%</td>
<td align="right">200</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">140</td>
<td align="right">13.5%</td>
<td align="right">140</td>
<td align="right">14.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">40</td>
<td align="right">3.8%</td>
<td align="right">40</td>
<td align="right">4.0%</td>
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
<td align="right">11,362,866</td>
<td align="right">13.0%</td>
<td align="right">4,638,727</td>
<td align="right">10.5%</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">75,319,032</td>
<td align="right">86.4%</td>
<td align="right">38,928,986</td>
<td align="right">88.4%</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">435,976</td>
<td align="right">0.5%</td>
<td align="right">417,642</td>
<td align="right">0.9%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
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
<td align="right">14,853</td>
<td align="right">35.0%</td>
<td align="right">12,174</td>
<td align="right">30.9%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">27,637</td>
<td align="right">65.0%</td>
<td align="right">27,243</td>
<td align="right">69.1%</td>
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
<td align="left">not managed dict</td>
<td align="right">120</td>
<td align="right">0.8%</td>
<td align="right">80</td>
<td align="right">0.7%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,358</td>
<td align="right">29.3%</td>
<td align="right">2,949</td>
<td align="right">24.2%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">80</td>
<td align="right">0.5%</td>
<td align="right">60</td>
<td align="right">0.5%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">2,294</td>
<td align="right">15.4%</td>
<td align="right">1,922</td>
<td align="right">15.8%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">580</td>
<td align="right">3.9%</td>
<td align="right">489</td>
<td align="right">4.0%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,360</td>
<td align="right">9.2%</td>
<td align="right">1,200</td>
<td align="right">9.9%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">240</td>
<td align="right">1.6%</td>
<td align="right">220</td>
<td align="right">1.8%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">3,840</td>
<td align="right">25.9%</td>
<td align="right">3,659</td>
<td align="right">30.1%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">60</td>
<td align="right">0.4%</td>
<td align="right">60</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">40</td>
<td align="right">0.3%</td>
<td align="right">40</td>
<td align="right">0.3%</td>
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
<td align="right">34,481,510</td>
<td align="right">99.8%</td>
<td align="right">14,352,500</td>
<td align="right">99.6%</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,880</td>
<td align="right">0.1%</td>
<td align="right">28,560</td>
<td align="right">0.2%</td>
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
<td align="right">13,624</td>
<td align="right">0.0%</td>
<td align="right">13,599</td>
<td align="right">0.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">800</td>
<td align="right">0.0%</td>
<td align="right">800</td>
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
<td align="right">12,088</td>
<td align="right">100.0%</td>
<td align="right">12,040</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">4,537,149</td>
<td align="right">100.0%</td>
<td align="right">1,731,425</td>
<td align="right">100.0%</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
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
<td align="right">300</td>
<td align="right">100.0%</td>
<td align="right">300</td>
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
<td align="right">9,782,985</td>
<td align="right">97.4%</td>
<td align="right">4,656,715</td>
<td align="right">94.7%</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">82,300</td>
<td align="right">0.8%</td>
<td align="right">80,700</td>
<td align="right">1.6%</td>
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
<td align="right">172,120</td>
<td align="right">1.7%</td>
<td align="right">171,800</td>
<td align="right">3.5%</td>
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
<td align="right">1,760</td>
<td align="right">19.0%</td>
<td align="right">1,620</td>
<td align="right">17.8%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,500</td>
<td align="right">81.0%</td>
<td align="right">7,500</td>
<td align="right">82.2%</td>
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
<td align="left">overridden</td>
<td align="right">100</td>
<td align="right">5.7%</td>
<td align="right">80</td>
<td align="right">4.9%</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">980</td>
<td align="right">55.7%</td>
<td align="right">880</td>
<td align="right">54.3%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">480</td>
<td align="right">27.3%</td>
<td align="right">460</td>
<td align="right">28.4%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">200</td>
<td align="right">11.4%</td>
<td align="right">200</td>
<td align="right">12.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,447,504</td>
<td align="right">99.2%</td>
<td align="right">1,664,163</td>
<td align="right">98.4%</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,120</td>
<td align="right">0.8%</td>
<td align="right">26,560</td>
<td align="right">1.6%</td>
<td align="right">-2.1%</td>
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
<td align="right">580</td>
<td align="right">65.9%</td>
<td align="right">540</td>
<td align="right">64.3%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">300</td>
<td align="right">34.1%</td>
<td align="right">300</td>
<td align="right">35.7%</td>
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
<td align="right">180</td>
<td align="right">31.0%</td>
<td align="right">160</td>
<td align="right">29.6%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">400</td>
<td align="right">69.0%</td>
<td align="right">380</td>
<td align="right">70.4%</td>
<td align="right">-5.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">24,166,717</td>
<td align="right">99.5%</td>
<td align="right">9,689,958</td>
<td align="right">98.9%</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">119,359</td>
<td align="right">0.5%</td>
<td align="right">106,843</td>
<td align="right">1.1%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">880</td>
<td align="right">0.0%</td>
<td align="right">880</td>
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
<td align="right">2,112</td>
<td align="right">40.8%</td>
<td align="right">1,900</td>
<td align="right">38.3%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,060</td>
<td align="right">59.2%</td>
<td align="right">3,057</td>
<td align="right">61.7%</td>
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
<td align="right">80</td>
<td align="right">3.8%</td>
<td align="right">60</td>
<td align="right">3.2%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">180</td>
<td align="right">8.5%</td>
<td align="right">140</td>
<td align="right">7.4%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">380</td>
<td align="right">18.0%</td>
<td align="right">340</td>
<td align="right">17.9%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">332</td>
<td align="right">15.7%</td>
<td align="right">300</td>
<td align="right">15.8%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">740</td>
<td align="right">35.0%</td>
<td align="right">680</td>
<td align="right">35.8%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">400</td>
<td align="right">18.9%</td>
<td align="right">380</td>
<td align="right">20.0%</td>
<td align="right">-5.0%</td>
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
<td align="right">3,003,009</td>
<td align="right">100.0%</td>
<td align="right">2,460,792</td>
<td align="right">100.0%</td>
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
<td align="right">680</td>
<td align="right">0.0%</td>
<td align="right">680</td>
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
<td align="right">540</td>
<td align="right">100.0%</td>
<td align="right">540</td>
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
<td align="right">23,898,551</td>
<td align="right">4.0%</td>
<td align="right">9,291,996</td>
<td align="right">3.6%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">376,749,418</td>
<td align="right">62.3%</td>
<td align="right">159,695,152</td>
<td align="right">61.9%</td>
<td align="right">-57.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">203,203,695</td>
<td align="right">33.6%</td>
<td align="right">88,205,544</td>
<td align="right">34.2%</td>
<td align="right">-56.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">649,188</td>
<td align="right">0.1%</td>
<td align="right">629,661</td>
<td align="right">0.2%</td>
<td align="right">-3.0%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">1,275,843</td>
<td align="right">5.4%</td>
<td align="right">53,582</td>
<td align="right">0.6%</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">10,800,551</td>
<td align="right">45.4%</td>
<td align="right">4,173,491</td>
<td align="right">45.3%</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">11,362,866</td>
<td align="right">47.7%</td>
<td align="right">4,638,727</td>
<td align="right">50.4%</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">54,564</td>
<td align="right">0.2%</td>
<td align="right">45,504</td>
<td align="right">0.5%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">19,280</td>
<td align="right">0.1%</td>
<td align="right">16,485</td>
<td align="right">0.2%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">119,359</td>
<td align="right">0.5%</td>
<td align="right">106,843</td>
<td align="right">1.2%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">31,640</td>
<td align="right">0.1%</td>
<td align="right">30,820</td>
<td align="right">0.3%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">27,120</td>
<td align="right">0.1%</td>
<td align="right">26,560</td>
<td align="right">0.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">82,300</td>
<td align="right">0.3%</td>
<td align="right">80,700</td>
<td align="right">0.9%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">19,298</td>
<td align="right">0.1%</td>
<td align="right">19,272</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">62,215</td>
<td align="right">9.6%</td>
<td align="right">54,080</td>
<td align="right">8.6%</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">10,700</td>
<td align="right">1.6%</td>
<td align="right">10,380</td>
<td align="right">1.6%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">356,041</td>
<td align="right">54.8%</td>
<td align="right">345,842</td>
<td align="right">54.9%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,340</td>
<td align="right">1.0%</td>
<td align="right">6,260</td>
<td align="right">1.0%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">172,120</td>
<td align="right">26.5%</td>
<td align="right">171,800</td>
<td align="right">27.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">18,180</td>
<td align="right">2.8%</td>
<td align="right">18,180</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">12,380</td>
<td align="right">1.9%</td>
<td align="right">12,380</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">5,100</td>
<td align="right">0.8%</td>
<td align="right">5,100</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,380</td>
<td align="right">0.2%</td>
<td align="right">1,380</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,060</td>
<td align="right">0.2%</td>
<td align="right">1,060</td>
<td align="right">0.2%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">986,126</td>
<td align="right">1.7%</td>
<td align="right">473,085</td>
<td align="right">1.5%</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">50,579,143</td>
<td align="right">89.0%</td>
<td align="right">25,951,597</td>
<td align="right">80.7%</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">43,315,523</td>
<td align="right">76.2%</td>
<td align="right">22,951,404</td>
<td align="right">71.4%</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">13,009,080</td>
<td align="right">22.9%</td>
<td align="right">8,659,173</td>
<td align="right">26.9%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">13,010,520</td>
<td align="right">22.9%</td>
<td align="right">8,660,613</td>
<td align="right">26.9%</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">13,546,520</td>
<td align="right">23.8%</td>
<td align="right">9,188,213</td>
<td align="right">28.6%</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">13,546,520</td>
<td align="right">23.8%</td>
<td align="right">9,188,213</td>
<td align="right">28.6%</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">24,570</td>
<td align="right">0.0%</td>
<td align="right">23,425</td>
<td align="right">0.1%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">571,260</td>
<td align="right">1.0%</td>
<td align="right">562,140</td>
<td align="right">1.7%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">536,000</td>
<td align="right">0.9%</td>
<td align="right">527,600</td>
<td align="right">1.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">544,820</td>
<td align="right">1.0%</td>
<td align="right">544,020</td>
<td align="right">1.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">460</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">980</td>
<td align="right">0.0%</td>
<td align="right">980</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">98,313</td>
<td align="right"></td>
<td align="right">15,374</td>
<td align="right"></td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">220,803</td>
<td align="right"></td>
<td align="right">51,656</td>
<td align="right"></td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">128,025</td>
<td align="right"></td>
<td align="right">42,013</td>
<td align="right"></td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,473,170</td>
<td align="right"></td>
<td align="right">1,426,566</td>
<td align="right"></td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">138,561,768</td>
<td align="right">15.6%</td>
<td align="right">58,247,355</td>
<td align="right">12.4%</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">20,127,437</td>
<td align="right"></td>
<td align="right">8,619,069</td>
<td align="right"></td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">132,188,744</td>
<td align="right">17.1%</td>
<td align="right">58,336,972</td>
<td align="right">14.3%</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">333,486,699</td>
<td align="right">37.5%</td>
<td align="right">153,552,964</td>
<td align="right">32.6%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">246,010,066</td>
<td align="right">31.9%</td>
<td align="right">113,753,502</td>
<td align="right">27.8%</td>
<td align="right">-53.8%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">1,600</td>
<td align="right">0.0%</td>
<td align="right">800</td>
<td align="right">0.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">36,092,823</td>
<td align="right">52.9%</td>
<td align="right">18,297,964</td>
<td align="right">49.0%</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">36,103,680</td>
<td align="right"></td>
<td align="right">18,308,454</td>
<td align="right"></td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">129,423,994</td>
<td align="right">16.8%</td>
<td align="right">69,738,298</td>
<td align="right">17.0%</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">179,935,125</td>
<td align="right">20.2%</td>
<td align="right">97,748,712</td>
<td align="right">20.7%</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">21,749,703</td>
<td align="right"></td>
<td align="right">11,988,584</td>
<td align="right"></td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">34,997,837</td>
<td align="right"></td>
<td align="right">20,162,096</td>
<td align="right"></td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">31,932,214</td>
<td align="right">46.8%</td>
<td align="right">18,929,489</td>
<td align="right">50.7%</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">32,092,746</td>
<td align="right">47.1%</td>
<td align="right">19,062,666</td>
<td align="right">51.0%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">264,416,447</td>
<td align="right">34.2%</td>
<td align="right">167,321,264</td>
<td align="right">40.9%</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">238,361,765</td>
<td align="right">26.8%</td>
<td align="right">161,536,121</td>
<td align="right">34.3%</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">72,361</td>
<td align="right">0.1%</td>
<td align="right">54,467</td>
<td align="right">0.1%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">88,171</td>
<td align="right">0.1%</td>
<td align="right">78,710</td>
<td align="right">0.2%</td>
<td align="right">-10.7%</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">6,185</td>
<td align="right">71.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">5,886</td>
<td align="right">67.7%</td>
<td align="right">1,356</td>
<td align="right">28.9%</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">41</td>
<td align="right">0.5%</td>
<td align="right">60</td>
<td align="right">1.3%</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">8,698</td>
<td align="right"></td>
<td align="right">4,685</td>
<td align="right"></td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">608</td>
<td align="right">7.0%</td>
<td align="right">805</td>
<td align="right">17.2%</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">783,549,743</td>
<td align="right">2,298.5%</td>
<td align="right">571,650,198</td>
<td align="right">1,707.9%</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,204</td>
<td align="right">25.3%</td>
<td align="right">2,524</td>
<td align="right">53.9%</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">320</td>
<td align="right">14.5%</td>
<td align="right">360</td>
<td align="right">14.3%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.4%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">34,088,937</td>
<td align="right"></td>
<td align="right">33,470,195</td>
<td align="right"></td>
<td align="right">-1.8%</td>
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
<td align="right">2,084</td>
<td align="right">94.6%</td>
<td align="right">2,404</td>
<td align="right">95.2%</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,204</td>
<td align="right"></td>
<td align="right">2,524</td>
<td align="right"></td>
<td align="right">14.5%</td>
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
<td align="right">120</td>
<td align="right">5.4%</td>
<td align="right">120</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
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
<td align="right">419</td>
<td align="right">19.0%</td>
<td align="right">372</td>
<td align="right">14.7%</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">230</td>
<td align="right">10.4%</td>
<td align="right">451</td>
<td align="right">17.9%</td>
<td align="right">96.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">391</td>
<td align="right">17.7%</td>
<td align="right">396</td>
<td align="right">15.7%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">640</td>
<td align="right">29.0%</td>
<td align="right">622</td>
<td align="right">24.6%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">322</td>
<td align="right">14.6%</td>
<td align="right">441</td>
<td align="right">17.5%</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">182</td>
<td align="right">8.3%</td>
<td align="right">190</td>
<td align="right">7.5%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">0.9%</td>
<td align="right">52</td>
<td align="right">2.1%</td>
<td align="right">160.0%</td>
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
<td align="right">166</td>
<td align="right">7.5%</td>
<td align="right">134</td>
<td align="right">5.3%</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">426</td>
<td align="right">19.3%</td>
<td align="right">535</td>
<td align="right">21.2%</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">57</td>
<td align="right">2.6%</td>
<td align="right">154</td>
<td align="right">6.1%</td>
<td align="right">170.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">667</td>
<td align="right">30.3%</td>
<td align="right">660</td>
<td align="right">26.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">425</td>
<td align="right">19.3%</td>
<td align="right">460</td>
<td align="right">18.2%</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">282</td>
<td align="right">12.8%</td>
<td align="right">367</td>
<td align="right">14.5%</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">61</td>
<td align="right">2.8%</td>
<td align="right">74</td>
<td align="right">2.9%</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">0.8%</td>
<td align="right"></td>
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
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">240</td>
<td align="right">443,195</td>
<td align="right">184,564.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">760</td>
<td align="right">483,135</td>
<td align="right">63,470.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">40</td>
<td align="right">2,640</td>
<td align="right">6,500.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">40</td>
<td align="right">1,040</td>
<td align="right">2,500.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">40</td>
<td align="right">880</td>
<td align="right">2,100.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">24,420</td>
<td align="right">526,840</td>
<td align="right">2,057.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">78,300</td>
<td align="right">517,895</td>
<td align="right">561.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">82,440</td>
<td align="right">275,231</td>
<td align="right">233.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">7,023,795</td>
<td align="right">15,857,699</td>
<td align="right">125.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">3,949</td>
<td align="right">6,479</td>
<td align="right">64.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">399,380</td>
<td align="right">145,140</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,199,685</td>
<td align="right">436,967</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">2,000,911</td>
<td align="right">730,033</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">4,004,216</td>
<td align="right">1,462,938</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,201,839</td>
<td align="right">439,599</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,201,959</td>
<td align="right">439,719</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,201,959</td>
<td align="right">439,719</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,202,039</td>
<td align="right">439,799</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">6,413,084</td>
<td align="right">2,353,468</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,202,559</td>
<td align="right">442,919</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">405,111</td>
<td align="right">151,269</td>
<td align="right">-62.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">4,652,803</td>
<td align="right">7,561,386</td>
<td align="right">62.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">815,642</td>
<td align="right">307,557</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">830,302</td>
<td align="right">322,217</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,250,933</td>
<td align="right">488,745</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,250,933</td>
<td align="right">488,745</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">4,410,177</td>
<td align="right">1,782,787</td>
<td align="right">-59.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">4,464,475</td>
<td align="right">1,835,260</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">425,009</td>
<td align="right">177,579</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">3,316,706</td>
<td align="right">1,442,924</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">1,500</td>
<td align="right">2,340</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">4,170,423</td>
<td align="right">1,891,391</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">9,433,423</td>
<td align="right">4,321,778</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">9,433,423</td>
<td align="right">4,321,778</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">4,944,019</td>
<td align="right">2,317,263</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">1,610,179</td>
<td align="right">758,987</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">8,233,738</td>
<td align="right">3,884,811</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">4,029,327</td>
<td align="right">1,951,739</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">4,064,865</td>
<td align="right">1,989,982</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">1,216,135</td>
<td align="right">596,621</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">10,734,530</td>
<td align="right">5,271,330</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,513,659</td>
<td align="right">1,241,086</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,579,094</td>
<td align="right">1,291,469</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">7,688,568</td>
<td align="right">3,871,548</td>
<td align="right">-49.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">399,561</td>
<td align="right">596,237</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">4,512,403</td>
<td align="right">2,302,286</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">14,163,502</td>
<td align="right">7,517,095</td>
<td align="right">-46.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">12,943,047</td>
<td align="right">6,907,204</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">12,946,387</td>
<td align="right">6,919,494</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">11,177,574</td>
<td align="right">6,148,107</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">20,971,458</td>
<td align="right">11,748,693</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">441,226</td>
<td align="right">634,711</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,210,063</td>
<td align="right">2,387,575</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">6,861,772</td>
<td align="right">3,906,244</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,552,162</td>
<td align="right">2,597,111</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">829,772</td>
<td align="right">475,919</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,104,562</td>
<td align="right">1,825,760</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">27,870,071</td>
<td align="right">16,643,535</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">22,782,339</td>
<td align="right">13,612,873</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">2,137,588</td>
<td align="right">1,280,846</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">4,638,442</td>
<td align="right">2,796,116</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,275,074</td>
<td align="right">3,247,295</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,427,425</td>
<td align="right">3,358,469</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">2,531,550</td>
<td align="right">1,568,366</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,639,238</td>
<td align="right">1,645,148</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,736,494</td>
<td align="right">1,706,299</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">18,900,238</td>
<td align="right">12,017,904</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">18,361,185</td>
<td align="right">11,861,274</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">27,061,104</td>
<td align="right">17,608,515</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,600,642</td>
<td align="right">1,048,310</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">19,970,302</td>
<td align="right">13,236,055</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">49,161,929</td>
<td align="right">33,470,885</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">17,294,615</td>
<td align="right">11,921,104</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">17,298,564</td>
<td align="right">11,927,583</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,388,109</td>
<td align="right">3,055,800</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">11,896,761</td>
<td align="right">8,311,462</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">11,896,761</td>
<td align="right">8,311,462</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">14,425,695</td>
<td align="right">10,292,024</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">927,389</td>
<td align="right">1,190,214</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">925,889</td>
<td align="right">1,187,874</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">902,073</td>
<td align="right">647,993</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">917,033</td>
<td align="right">660,754</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,345,936</td>
<td align="right">995,881</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">1,346,456</td>
<td align="right">996,401</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">910,827</td>
<td align="right">675,370</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,207,877</td>
<td align="right">1,643,344</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,802,371</td>
<td align="right">5,063,598</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,810,523</td>
<td align="right">1,353,016</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,244,120</td>
<td align="right">1,718,586</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">5,404,886</td>
<td align="right">4,141,504</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">66,948,694</td>
<td align="right">51,308,612</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">1,803,435</td>
<td align="right">2,193,546</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">937,794</td>
<td align="right">1,132,442</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">937,794</td>
<td align="right">1,132,442</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">30,503,585</td>
<td align="right">24,415,475</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">966,885</td>
<td align="right">1,149,483</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">35,658</td>
<td align="right">42,255</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">35,658</td>
<td align="right">42,255</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">8,199,405</td>
<td align="right">6,766,077</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">4,960</td>
<td align="right">5,800</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">4,960</td>
<td align="right">5,800</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">3,219,674</td>
<td align="right">3,761,731</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">16,858,281</td>
<td align="right">14,068,198</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,456,093</td>
<td align="right">1,215,189</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5,864,159</td>
<td align="right">6,830,546</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">7,414,089</td>
<td align="right">6,310,773</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">7,296,630</td>
<td align="right">6,261,645</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,970,940</td>
<td align="right">1,692,940</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">17,536</td>
<td align="right">19,992</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,760,308</td>
<td align="right">3,257,458</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,760,308</td>
<td align="right">3,257,458</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">43,796</td>
<td align="right">48,986</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">923,423</td>
<td align="right">827,834</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">15,700</td>
<td align="right">16,945</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,537,960</td>
<td align="right">3,791,872</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,860,056</td>
<td align="right">1,942,320</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,014,520</td>
<td align="right">1,058,186</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">78,260</td>
<td align="right">74,900</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">78,260</td>
<td align="right">74,900</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">78,500</td>
<td align="right">75,140</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">4,460</td>
<td align="right">4,300</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">16,100</td>
<td align="right">15,760</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">16,100</td>
<td align="right">15,760</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">34,088,937</td>
<td align="right">33,470,195</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">531,404</td>
<td align="right">521,823</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">34,701,259</td>
<td align="right">34,077,967</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,149,780</td>
<td align="right">1,129,940</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">16,580</td>
<td align="right">16,832</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">16,580</td>
<td align="right">16,832</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">527,400</td>
<td align="right">519,400</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">5,806,800</td>
<td align="right">5,718,800</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">4,038</td>
<td align="right">3,981</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,427,134</td>
<td align="right">4,370,730</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">1,028,780</td>
<td align="right">1,020,860</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">612,322</td>
<td align="right">607,772</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">15,700</td>
<td align="right">15,810</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">15,700</td>
<td align="right">15,810</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">514,104</td>
<td align="right">517,518</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">506,620</td>
<td align="right">506,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,008,040</td>
<td align="right">1,008,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">506,660</td>
<td align="right">506,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">506,580</td>
<td align="right">506,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">12,240</td>
<td align="right">12,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">4,960</td>
<td align="right">4,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">4,740</td>
<td align="right">4,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">4,220</td>
<td align="right">4,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">6,222,156</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">612,199</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right"></td>
<td align="right">442,955</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right"></td>
<td align="right">57,885</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right"></td>
<td align="right">16,775</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right"></td>
<td align="right">8,110</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right"></td>
<td align="right">8,110</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">2,395</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">160</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">160</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">576</td>
<td align="right">586</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
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
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">40</td>
<td align="right">40</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
