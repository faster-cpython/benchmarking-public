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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">37,469</td>
<td align="right">169,378</td>
<td align="right">352.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">36,934</td>
<td align="right">130,111</td>
<td align="right">252.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">116,564</td>
<td align="right">212,524</td>
<td align="right">82.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">330,308</td>
<td align="right">527,731</td>
<td align="right">59.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">716,765</td>
<td align="right">310,287</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,454,535</td>
<td align="right">641,567</td>
<td align="right">-55.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,466,744</td>
<td align="right">651,391</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">488,782</td>
<td align="right">217,762</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,978,565</td>
<td align="right">887,427</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,006,814</td>
<td align="right">915,676</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,014,186</td>
<td align="right">465,048</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">2,044,635</td>
<td align="right">953,497</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">767,226</td>
<td align="right">360,672</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">511,614</td>
<td align="right">240,646</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">511,937</td>
<td align="right">240,969</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">759,336</td>
<td align="right">366,347</td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,943,148</td>
<td align="right">2,400,624</td>
<td align="right">-51.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">798,202</td>
<td align="right">391,708</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,085,709</td>
<td align="right">543,709</td>
<td align="right">-49.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">274,653</td>
<td align="right">139,143</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">277,699</td>
<td align="right">142,133</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">280,547</td>
<td align="right">145,029</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,517,534</td>
<td align="right">3,442,567</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">15,567,946</td>
<td align="right">8,482,757</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">5,619,020</td>
<td align="right">3,084,874</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,503,069</td>
<td align="right">6,435,049</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,939,545</td>
<td align="right">1,124,383</td>
<td align="right">-42.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,533,644</td>
<td align="right">904,748</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,516,886</td>
<td align="right">1,516,768</td>
<td align="right">-39.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,343,059</td>
<td align="right">3,870,637</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,709,775</td>
<td align="right">1,653,574</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,628,410</td>
<td align="right">4,661,186</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">7,916,804</td>
<td align="right">4,904,253</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,944,833</td>
<td align="right">3,695,649</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">13,410,155</td>
<td align="right">8,444,163</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">10,452,715</td>
<td align="right">6,584,157</td>
<td align="right">-37.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">29,234,763</td>
<td align="right">18,780,855</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,151,611</td>
<td align="right">745,125</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,677,717</td>
<td align="right">2,381,252</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">427,370</td>
<td align="right">277,274</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,047,552</td>
<td align="right">684,870</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,143,548</td>
<td align="right">2,059,532</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,054,278</td>
<td align="right">2,016,552</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,195,545</td>
<td align="right">1,461,865</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,173,796</td>
<td align="right">789,598</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">2,683,293</td>
<td align="right">1,828,012</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">74,875,828</td>
<td align="right">51,450,193</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,243,024</td>
<td align="right">4,299,743</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,522,064</td>
<td align="right">1,058,350</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">4,021,352</td>
<td align="right">2,796,806</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,549,946</td>
<td align="right">1,088,363</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">16,464,190</td>
<td align="right">11,832,305</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">24,450,292</td>
<td align="right">17,946,607</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,397,719</td>
<td align="right">1,030,087</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,599,460</td>
<td align="right">5,613,157</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">15,410,202</td>
<td align="right">11,513,941</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">9,444,730</td>
<td align="right">7,141,305</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,630,649</td>
<td align="right">2,754,877</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,321,540</td>
<td align="right">1,003,666</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,874,766</td>
<td align="right">1,428,682</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">20,777,607</td>
<td align="right">16,863,671</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">15,310,063</td>
<td align="right">12,643,398</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">9,472,589</td>
<td align="right">7,834,337</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,683,432</td>
<td align="right">2,260,354</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">168,736</td>
<td align="right">191,026</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,110,605</td>
<td align="right">968,521</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,871,547</td>
<td align="right">3,457,736</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">111,280</td>
<td align="right">99,845</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">4,716,894</td>
<td align="right">4,294,816</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,282</td>
<td align="right">4,811</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">177,438</td>
<td align="right">162,805</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">614,276</td>
<td align="right">572,083</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">735,613</td>
<td align="right">693,370</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">161,639</td>
<td align="right">168,813</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">466</td>
<td align="right">484</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,679</td>
<td align="right">13,208</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">112,188</td>
<td align="right">115,810</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,356,287</td>
<td align="right">3,253,293</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,902</td>
<td align="right">17,431</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,902</td>
<td align="right">17,431</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,612,900</td>
<td align="right">1,570,657</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">221,451</td>
<td align="right">216,455</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">41,072</td>
<td align="right">40,588</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,532</td>
<td align="right">4,578</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">561,108</td>
<td align="right">556,152</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">352</td>
<td align="right">349</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,213</td>
<td align="right">3,232</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">201,616</td>
<td align="right">200,642</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,841</td>
<td align="right">102,346</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">776,706</td>
<td align="right">777,300</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,333</td>
<td align="right">97,285</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">46,411</td>
<td align="right">46,399</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,468</td>
<td align="right">21,472</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,052</td>
<td align="right">34,054</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,362</td>
<td align="right">81,366</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">907,807</td>
<td align="right">907,771</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">452,936</td>
<td align="right">452,933</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,684</td>
<td align="right">1,818,676</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,282</td>
<td align="right">5,068,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,142</td>
<td align="right">105,142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,110</td>
<td align="right">105,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">87,032</td>
<td align="right">87,032</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">86,432</td>
<td align="right">86,432</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">84,725</td>
<td align="right">84,725</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,368</td>
<td align="right">77,368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">68,756</td>
<td align="right">68,756</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,589</td>
<td align="right">67,589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">59,119</td>
<td align="right">59,119</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,611</td>
<td align="right">55,611</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,607</td>
<td align="right">55,607</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">51,440</td>
<td align="right">51,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">44,014</td>
<td align="right">44,014</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,906</td>
<td align="right">42,906</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">38,452</td>
<td align="right">38,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">38,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,136</td>
<td align="right">35,136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,563</td>
<td align="right">29,563</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">20,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,858</td>
<td align="right">17,858</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">17,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">14,867</td>
<td align="right">14,867</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">13,887</td>
<td align="right">13,887</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,839</td>
<td align="right">12,839</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,286</td>
<td align="right">10,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">9,870</td>
<td align="right">9,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,491</td>
<td align="right">8,491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">8,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,227</td>
<td align="right">4,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">4,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">953</td>
<td align="right">953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">806</td>
<td align="right">806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">522</td>
<td align="right">522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">415</td>
<td align="right">415</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">322</td>
<td align="right">322</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">267</td>
<td align="right">267</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">183</td>
<td align="right">183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">154</td>
<td align="right">154</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">149</td>
<td align="right">149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">68</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">38</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">29</td>
<td align="right">29</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1</td>
<td align="right">1</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">11,189</td>
<td align="right">0.1%</td>
<td align="right">98,572</td>
<td align="right">2.0%</td>
<td align="right">781.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,513,949</td>
<td align="right">76.2%</td>
<td align="right">3,434,751</td>
<td align="right">68.5%</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,020,921</td>
<td align="right">23.6%</td>
<td align="right">1,475,919</td>
<td align="right">29.4%</td>
<td align="right">-27.0%</td>
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
<td align="right">3,478</td>
<td align="right">100.0%</td>
<td align="right">7,704</td>
<td align="right">100.0%</td>
<td align="right">121.5%</td>
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
<td align="left">add different types</td>
<td align="right">851</td>
<td align="right">24.5%</td>
<td align="right">5,807</td>
<td align="right">75.4%</td>
<td align="right">582.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">827</td>
<td align="right">23.8%</td>
<td align="right">510</td>
<td align="right">6.6%</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">1,424</td>
<td align="right">40.9%</td>
<td align="right">970</td>
<td align="right">12.6%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">253</td>
<td align="right">7.3%</td>
<td align="right">294</td>
<td align="right">3.8%</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">109</td>
<td align="right">3.1%</td>
<td align="right">109</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">14</td>
<td align="right">0.4%</td>
<td align="right">14</td>
<td align="right">0.2%</td>
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
<td align="right">13,887</td>
<td align="right">100.0%</td>
<td align="right">13,887</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">695,476</td>
<td align="right">94.4%</td>
<td align="right">424,456</td>
<td align="right">91.3%</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">40,799</td>
<td align="right">5.5%</td>
<td align="right">40,328</td>
<td align="right">8.7%</td>
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
<td align="right">155</td>
<td align="right">56.8%</td>
<td align="right">142</td>
<td align="right">54.6%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118</td>
<td align="right">43.2%</td>
<td align="right">118</td>
<td align="right">45.4%</td>
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
<td align="right">154</td>
<td align="right">99.4%</td>
<td align="right">141</td>
<td align="right">99.3%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">0.6%</td>
<td align="right">1</td>
<td align="right">0.7%</td>
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
<td align="right">28,746,600</td>
<td align="right">100.0%</td>
<td align="right">16,276,023</td>
<td align="right">100.0%</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,181</td>
<td align="right">0.0%</td>
<td align="right">1,229</td>
<td align="right">0.0%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">795</td>
<td align="right">0.0%</td>
<td align="right">795</td>
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
<td align="right">3,492</td>
<td align="right">100.0%</td>
<td align="right">3,490</td>
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
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
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
<td align="right">43</td>
<td align="right">23.5%</td>
<td align="right">43</td>
<td align="right">23.5%</td>
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
<td align="right">11,085</td>
<td align="right">0.2%</td>
<td align="right">93,611</td>
<td align="right">2.5%</td>
<td align="right">744.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">758,330</td>
<td align="right">13.3%</td>
<td align="right">363,920</td>
<td align="right">9.6%</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,929,584</td>
<td align="right">86.5%</td>
<td align="right">3,347,336</td>
<td align="right">87.9%</td>
<td align="right">-32.1%</td>
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
<td align="right">464</td>
<td align="right">38.4%</td>
<td align="right">2,029</td>
<td align="right">48.6%</td>
<td align="right">337.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">743</td>
<td align="right">61.6%</td>
<td align="right">2,148</td>
<td align="right">51.4%</td>
<td align="right">189.1%</td>
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
<td align="right">496</td>
<td align="right">66.8%</td>
<td align="right">1,902</td>
<td align="right">88.5%</td>
<td align="right">283.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">106</td>
<td align="right">14.3%</td>
<td align="right">105</td>
<td align="right">4.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">96</td>
<td align="right">12.9%</td>
<td align="right">96</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">44</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">2,104,602</td>
<td align="right">100.0%</td>
<td align="right">1,156,144</td>
<td align="right">100.0%</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">270</td>
<td align="right">0.0%</td>
<td align="right">270</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">43</td>
<td align="right">100.0%</td>
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
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">43</td>
<td align="right">100.0%</td>
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
<td align="right">6,723,804</td>
<td align="right">98.4%</td>
<td align="right">6,263,087</td>
<td align="right">98.2%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">111,860</td>
<td align="right">1.6%</td>
<td align="right">115,483</td>
<td align="right">1.8%</td>
<td align="right">3.2%</td>
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
<td align="right">55</td>
<td align="right">16.8%</td>
<td align="right">51</td>
<td align="right">15.6%</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">273</td>
<td align="right">83.2%</td>
<td align="right">276</td>
<td align="right">84.4%</td>
<td align="right">1.1%</td>
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
<td align="right">55</td>
<td align="right">20.1%</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">28.2%</td>
<td align="right">77</td>
<td align="right">27.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">25.6%</td>
<td align="right">70</td>
<td align="right">25.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">58</td>
<td align="right">21.2%</td>
<td align="right">58</td>
<td align="right">21.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">2.6%</td>
<td align="right">7</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">1.1%</td>
<td align="right">3</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">2</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.4%</td>
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
<td align="right">7,617,385</td>
<td align="right">13.6%</td>
<td align="right">4,651,012</td>
<td align="right">13.5%</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">48,104,904</td>
<td align="right">85.8%</td>
<td align="right">29,424,821</td>
<td align="right">85.4%</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">355,257</td>
<td align="right">0.6%</td>
<td align="right">353,559</td>
<td align="right">1.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
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
<td align="right">6,348</td>
<td align="right">36.3%</td>
<td align="right">5,493</td>
<td align="right">33.1%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,123</td>
<td align="right">63.7%</td>
<td align="right">11,093</td>
<td align="right">66.9%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">1,911</td>
<td align="right">30.1%</td>
<td align="right">1,278</td>
<td align="right">23.3%</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">934</td>
<td align="right">14.7%</td>
<td align="right">788</td>
<td align="right">14.3%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,384</td>
<td align="right">21.8%</td>
<td align="right">1,454</td>
<td align="right">26.5%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">682</td>
<td align="right">10.7%</td>
<td align="right">682</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">7.2%</td>
<td align="right">460</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.1%</td>
<td align="right">71</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.1%</td>
<td align="right">68</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">45</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.4%</td>
<td align="right">23</td>
<td align="right">0.4%</td>
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
<td align="right">21,910,696</td>
<td align="right">100.0%</td>
<td align="right">12,353,085</td>
<td align="right">100.0%</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">835</td>
<td align="right">0.0%</td>
<td align="right">855</td>
<td align="right">0.0%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
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
<td align="right">309</td>
<td align="right">0.0%</td>
<td align="right">309</td>
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
<td align="right">2,387</td>
<td align="right">100.0%</td>
<td align="right">2,386</td>
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
<td align="right">2,692,360</td>
<td align="right">100.0%</td>
<td align="right">1,201,902</td>
<td align="right">100.0%</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13</td>
<td align="right">0.0%</td>
<td align="right">13</td>
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
<td align="right">55</td>
<td align="right">100.0%</td>
<td align="right">55</td>
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
<td align="right">6,068,424</td>
<td align="right">96.5%</td>
<td align="right">3,358,422</td>
<td align="right">93.8%</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,683</td>
<td align="right">1.3%</td>
<td align="right">79,685</td>
<td align="right">2.2%</td>
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
<td align="right">140,654</td>
<td align="right">2.2%</td>
<td align="right">140,654</td>
<td align="right">3.9%</td>
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
<td align="right">3,616</td>
<td align="right">83.8%</td>
<td align="right">3,618</td>
<td align="right">83.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">699</td>
<td align="right">16.2%</td>
<td align="right">699</td>
<td align="right">16.2%</td>
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
<td align="left">property</td>
<td align="right">344</td>
<td align="right">49.2%</td>
<td align="right">344</td>
<td align="right">49.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">29.5%</td>
<td align="right">206</td>
<td align="right">29.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">139</td>
<td align="right">19.9%</td>
<td align="right">139</td>
<td align="right">19.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">10</td>
<td align="right">1.4%</td>
<td align="right">10</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,169,542</td>
<td align="right">99.0%</td>
<td align="right">1,221,274</td>
<td align="right">98.3%</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,264</td>
<td align="right">1.0%</td>
<td align="right">21,266</td>
<td align="right">1.7%</td>
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
<td align="right">17</td>
<td align="right">8.3%</td>
<td align="right">19</td>
<td align="right">9.2%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">91.7%</td>
<td align="right">187</td>
<td align="right">90.8%</td>
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
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
<td align="right">68</td>
<td align="right">36.4%</td>
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
<td align="right">115,401</td>
<td align="right">0.8%</td>
<td align="right">211,291</td>
<td align="right">2.9%</td>
<td align="right">83.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,617,784</td>
<td align="right">99.2%</td>
<td align="right">7,185,721</td>
<td align="right">97.1%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">28</td>
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
<td align="right">703</td>
<td align="right">60.4%</td>
<td align="right">777</td>
<td align="right">63.0%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">460</td>
<td align="right">39.6%</td>
<td align="right">456</td>
<td align="right">37.0%</td>
<td align="right">-0.9%</td>
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
<td align="left">mapping</td>
<td align="right">248</td>
<td align="right">35.3%</td>
<td align="right">325</td>
<td align="right">41.8%</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">152</td>
<td align="right">21.6%</td>
<td align="right">149</td>
<td align="right">19.2%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">126</td>
<td align="right">17.9%</td>
<td align="right">126</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">15.8%</td>
<td align="right">111</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">65</td>
<td align="right">9.2%</td>
<td align="right">65</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,230,176</td>
<td align="right">100.0%</td>
<td align="right">1,959,120</td>
<td align="right">100.0%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">38</td>
<td align="right">0.0%</td>
<td align="right">38</td>
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
<td align="right">111</td>
<td align="right">100.0%</td>
<td align="right">111</td>
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
<td align="right">15,300,288</td>
<td align="right">3.7%</td>
<td align="right">8,964,279</td>
<td align="right">3.1%</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">519,382</td>
<td align="right">0.1%</td>
<td align="right">687,586</td>
<td align="right">0.2%</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">151,510,721</td>
<td align="right">36.4%</td>
<td align="right">103,143,905</td>
<td align="right">35.7%</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">248,738,478</td>
<td align="right">59.8%</td>
<td align="right">176,157,487</td>
<td align="right">61.0%</td>
<td align="right">-29.2%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">115,401</td>
<td align="right">0.8%</td>
<td align="right">211,291</td>
<td align="right">2.4%</td>
<td align="right">83.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">758,330</td>
<td align="right">5.0%</td>
<td align="right">363,920</td>
<td align="right">4.1%</td>
<td align="right">-52.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,513,949</td>
<td align="right">42.6%</td>
<td align="right">3,434,751</td>
<td align="right">38.4%</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">7,617,385</td>
<td align="right">49.9%</td>
<td align="right">4,651,012</td>
<td align="right">52.1%</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,181</td>
<td align="right">0.0%</td>
<td align="right">1,229</td>
<td align="right">0.0%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">111,860</td>
<td align="right">0.7%</td>
<td align="right">115,483</td>
<td align="right">1.3%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40,799</td>
<td align="right">0.3%</td>
<td align="right">40,328</td>
<td align="right">0.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,264</td>
<td align="right">0.1%</td>
<td align="right">21,266</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,683</td>
<td align="right">0.5%</td>
<td align="right">79,685</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">13,887</td>
<td align="right">0.1%</td>
<td align="right">13,887</td>
<td align="right">0.2%</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">11,189</td>
<td align="right">2.2%</td>
<td align="right">98,572</td>
<td align="right">14.3%</td>
<td align="right">781.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">11,084</td>
<td align="right">2.1%</td>
<td align="right">93,610</td>
<td align="right">13.6%</td>
<td align="right">744.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">295,710</td>
<td align="right">56.9%</td>
<td align="right">294,005</td>
<td align="right">42.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,487</td>
<td align="right">9.5%</td>
<td align="right">49,494</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">140,654</td>
<td align="right">27.1%</td>
<td align="right">140,654</td>
<td align="right">20.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.9%</td>
<td align="right">9,895</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">398</td>
<td align="right">0.1%</td>
<td align="right">398</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">275</td>
<td align="right">0.1%</td>
<td align="right">275</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">201</td>
<td align="right">0.0%</td>
<td align="right">201</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">153</td>
<td align="right">0.0%</td>
<td align="right">153</td>
<td align="right">0.0%</td>
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
<td align="right">619,152</td>
<td align="right">1.7%</td>
<td align="right">348,185</td>
<td align="right">1.4%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">32,282,531</td>
<td align="right">86.5%</td>
<td align="right">19,272,269</td>
<td align="right">79.3%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">27,858,957</td>
<td align="right">74.7%</td>
<td align="right">17,152,120</td>
<td align="right">70.6%</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">9,021,650</td>
<td align="right">24.2%</td>
<td align="right">6,718,225</td>
<td align="right">27.6%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">9,021,709</td>
<td align="right">24.2%</td>
<td align="right">6,718,284</td>
<td align="right">27.6%</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">9,449,088</td>
<td align="right">25.3%</td>
<td align="right">7,145,663</td>
<td align="right">29.4%</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">9,449,088</td>
<td align="right">25.3%</td>
<td align="right">7,145,663</td>
<td align="right">29.4%</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,917</td>
<td align="right">0.0%</td>
<td align="right">17,446</td>
<td align="right">0.1%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,379</td>
<td align="right">1.1%</td>
<td align="right">427,379</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">17</td>
<td align="right">0.0%</td>
<td align="right">17</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<td align="right">1.2%</td>
<td align="right">456,471</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,509</td>
<td align="right">1.2%</td>
<td align="right">441,509</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="left">Method cache misses</td>
<td align="right">49,119</td>
<td align="right"></td>
<td align="right">12,362</td>
<td align="right"></td>
<td align="right">-74.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">2,090,988</td>
<td align="right"></td>
<td align="right">1,006,988</td>
<td align="right"></td>
<td align="right">-51.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">12,381,101</td>
<td align="right"></td>
<td align="right">6,317,776</td>
<td align="right"></td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">77,982,202</td>
<td align="right">16.3%</td>
<td align="right">42,734,641</td>
<td align="right">14.5%</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">166,308,493</td>
<td align="right">34.8%</td>
<td align="right">94,467,314</td>
<td align="right">32.1%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">112,344,158</td>
<td align="right">19.6%</td>
<td align="right">65,002,802</td>
<td align="right">18.4%</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">22,671,661</td>
<td align="right">51.8%</td>
<td align="right">13,458,888</td>
<td align="right">48.2%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">22,674,375</td>
<td align="right"></td>
<td align="right">13,461,651</td>
<td align="right"></td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">153,520,163</td>
<td align="right">26.8%</td>
<td align="right">92,186,866</td>
<td align="right">26.0%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">90,209,323</td>
<td align="right">15.7%</td>
<td align="right">55,575,743</td>
<td align="right">15.7%</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">68,787,568</td>
<td align="right">14.4%</td>
<td align="right">43,283,270</td>
<td align="right">14.7%</td>
<td align="right">-37.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">13,995,069</td>
<td align="right"></td>
<td align="right">8,883,093</td>
<td align="right"></td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">216,833,514</td>
<td align="right">37.8%</td>
<td align="right">141,463,235</td>
<td align="right">39.9%</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">217,857</td>
<td align="right"></td>
<td align="right">144,190</td>
<td align="right"></td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">22,869,965</td>
<td align="right"></td>
<td align="right">15,279,566</td>
<td align="right"></td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">20,974,239</td>
<td align="right">47.9%</td>
<td align="right">14,332,309</td>
<td align="right">51.3%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">21,095,634</td>
<td align="right">48.2%</td>
<td align="right">14,453,567</td>
<td align="right">51.8%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">164,399,214</td>
<td align="right">34.4%</td>
<td align="right">113,629,817</td>
<td align="right">38.6%</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">169,067</td>
<td align="right"></td>
<td align="right">132,122</td>
<td align="right"></td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,798</td>
<td align="right">0.2%</td>
<td align="right">77,705</td>
<td align="right">0.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,597</td>
<td align="right">0.1%</td>
<td align="right">43,553</td>
<td align="right">0.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">640</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">54</td>
<td align="right">1.5%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">229</td>
<td align="right">6.4%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">2,929</td>
<td align="right">81.7%</td>
<td align="right">303</td>
<td align="right">62.1%</td>
<td align="right">-89.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">3,046</td>
<td align="right">85.0%</td>
<td align="right">317</td>
<td align="right">65.0%</td>
<td align="right">-89.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,585</td>
<td align="right"></td>
<td align="right">488</td>
<td align="right"></td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">427</td>
<td align="right">11.9%</td>
<td align="right">183</td>
<td align="right">37.5%</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">473,061,929</td>
<td align="right">2,015.6%</td>
<td align="right">253,221,473</td>
<td align="right">1,510.2%</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">23,470,557</td>
<td align="right"></td>
<td align="right">16,767,748</td>
<td align="right"></td>
<td align="right">-28.6%</td>
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
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
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
<td align="right">427</td>
<td align="right"></td>
<td align="right">183</td>
<td align="right"></td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">427</td>
<td align="right">100.0%</td>
<td align="right">183</td>
<td align="right">100.0%</td>
<td align="right">-57.1%</td>
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
<td align="right">122</td>
<td align="right">28.6%</td>
<td align="right">46</td>
<td align="right">25.1%</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20</td>
<td align="right">4.7%</td>
<td align="right">4</td>
<td align="right">2.2%</td>
<td align="right">-80.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">76</td>
<td align="right">17.8%</td>
<td align="right">47</td>
<td align="right">25.7%</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">56</td>
<td align="right">13.1%</td>
<td align="right">39</td>
<td align="right">21.3%</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">86</td>
<td align="right">20.1%</td>
<td align="right">25</td>
<td align="right">13.7%</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">29</td>
<td align="right">6.8%</td>
<td align="right">13</td>
<td align="right">7.1%</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">38</td>
<td align="right">8.9%</td>
<td align="right">9</td>
<td align="right">4.9%</td>
<td align="right">-76.3%</td>
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
<td align="right">21</td>
<td align="right">4.9%</td>
<td align="right">21</td>
<td align="right">11.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">120</td>
<td align="right">28.1%</td>
<td align="right">28</td>
<td align="right">15.3%</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">44</td>
<td align="right">10.3%</td>
<td align="right">22</td>
<td align="right">12.0%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">88</td>
<td align="right">20.6%</td>
<td align="right">64</td>
<td align="right">35.0%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">51</td>
<td align="right">11.9%</td>
<td align="right">7</td>
<td align="right">3.8%</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">36</td>
<td align="right">8.4%</td>
<td align="right">23</td>
<td align="right">12.6%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">67</td>
<td align="right">15.7%</td>
<td align="right">18</td>
<td align="right">9.8%</td>
<td align="right">-73.1%</td>
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
<td align="left">_COMPARE_OP</td>
<td align="right">273,662</td>
<td align="right">414</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">229,104</td>
<td align="right">405</td>
<td align="right">-99.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">11,642</td>
<td align="right">56</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">176,860</td>
<td align="right">1,003</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">917,005</td>
<td align="right">23,556</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">2,066,174</td>
<td align="right">230,594</td>
<td align="right">-88.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">688,314</td>
<td align="right">97,708</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,103,507</td>
<td align="right">162,371</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">3,043,535</td>
<td align="right">487,181</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">440,816</td>
<td align="right">76,432</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">814,139</td>
<td align="right">143,163</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,191,064</td>
<td align="right">415,056</td>
<td align="right">-81.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">227,623</td>
<td align="right">45,070</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">683,582</td>
<td align="right">136,021</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,332,089</td>
<td align="right">506,300</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,730,787</td>
<td align="right">378,824</td>
<td align="right">-78.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">5,321,669</td>
<td align="right">1,253,570</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">5,321,669</td>
<td align="right">1,253,570</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">3,658,412</td>
<td align="right">872,657</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,633,355</td>
<td align="right">1,155,862</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">1,148,312</td>
<td align="right">291,492</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">3,455,767</td>
<td align="right">896,389</td>
<td align="right">-74.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,610,594</td>
<td align="right">700,139</td>
<td align="right">-73.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">180,751</td>
<td align="right">50,211</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">6,564,202</td>
<td align="right">1,838,637</td>
<td align="right">-72.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">2,475,493</td>
<td align="right">699,773</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">177,482</td>
<td align="right">50,211</td>
<td align="right">-71.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">12,960,105</td>
<td align="right">3,801,950</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">5,392,750</td>
<td align="right">1,663,970</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">6,262,860</td>
<td align="right">1,955,648</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,315,906</td>
<td align="right">1,048,435</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">7,569,293</td>
<td align="right">2,448,574</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">892,398</td>
<td align="right">291,678</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">385,816</td>
<td align="right">126,231</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">385,816</td>
<td align="right">126,231</td>
<td align="right">-67.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">11,457,176</td>
<td align="right">3,779,987</td>
<td align="right">-67.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">8,169,154</td>
<td align="right">2,700,692</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">2,298,301</td>
<td align="right">775,949</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,550,330</td>
<td align="right">523,776</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">594,150</td>
<td align="right">202,251</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">594,167</td>
<td align="right">202,266</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">594,167</td>
<td align="right">202,266</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">15,242,547</td>
<td align="right">5,319,762</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,736,816</td>
<td align="right">610,770</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">2,404,621</td>
<td align="right">852,267</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">3,232,561</td>
<td align="right">1,163,271</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,885,499</td>
<td align="right">1,104,638</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,887,272</td>
<td align="right">1,110,202</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,462,339</td>
<td align="right">998,256</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">712,283</td>
<td align="right">290,675</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">9,597,115</td>
<td align="right">3,981,223</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">9,585,535</td>
<td align="right">3,981,223</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,964,674</td>
<td align="right">1,647,719</td>
<td align="right">-58.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">6,425,882</td>
<td align="right">2,681,948</td>
<td align="right">-58.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">229,997</td>
<td align="right">96,891</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">689,995</td>
<td align="right">290,675</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">689,995</td>
<td align="right">290,675</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">689,995</td>
<td align="right">290,675</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">689,995</td>
<td align="right">290,675</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">689,995</td>
<td align="right">290,675</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,044,367</td>
<td align="right">459,596</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,323,628</td>
<td align="right">597,155</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">1,225,948</td>
<td align="right">554,968</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,917,033</td>
<td align="right">889,139</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">4,505,606</td>
<td align="right">2,159,746</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">813,759</td>
<td align="right">409,101</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">813,759</td>
<td align="right">409,101</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">10,600,629</td>
<td align="right">5,384,925</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">1,685,276</td>
<td align="right">871,806</td>
<td align="right">-48.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,028,998</td>
<td align="right">1,703,085</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,028,998</td>
<td align="right">1,703,085</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">28,479,796</td>
<td align="right">16,111,806</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">39,735,077</td>
<td align="right">22,843,797</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">12,136,003</td>
<td align="right">7,015,284</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,729,325</td>
<td align="right">1,005,614</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,956,672</td>
<td align="right">1,224,744</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">11,684,866</td>
<td align="right">7,427,641</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">644,287</td>
<td align="right">412,217</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">636,899</td>
<td align="right">408,098</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">640,813</td>
<td align="right">412,208</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">17,887,114</td>
<td align="right">11,591,045</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">3,421,545</td>
<td align="right">2,266,836</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,452,946</td>
<td align="right">963,768</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,582,012</td>
<td align="right">1,776,297</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">580,188</td>
<td align="right">404,332</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">580,188</td>
<td align="right">404,332</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">7,917,181</td>
<td align="right">5,517,711</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">7,917,181</td>
<td align="right">5,517,711</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">3,327,981</td>
<td align="right">2,327,769</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">23,470,557</td>
<td align="right">16,767,748</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,274,582</td>
<td align="right">912,675</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">24,104,764</td>
<td align="right">17,268,850</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,280,308</td>
<td align="right">4,499,272</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">21,048,098</td>
<td align="right">15,586,446</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">592,593</td>
<td align="right">462,041</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">592,593</td>
<td align="right">462,041</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">9,463,465</td>
<td align="right">7,448,622</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">634,207</td>
<td align="right">501,102</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">637,443</td>
<td align="right">504,338</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">5,856,836</td>
<td align="right">4,700,216</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,452,162</td>
<td align="right">1,223,463</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">5,278,229</td>
<td align="right">4,514,207</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">2,659,690</td>
<td align="right">2,430,927</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,571,801</td>
<td align="right">5,176,647</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">828,262</td>
<td align="right">824,639</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">403,328</td>
<td align="right">403,329</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">403,328</td>
<td align="right">403,329</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">403,328</td>
<td align="right">403,329</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,566,710</td>
<td align="right">4,566,710</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">811,253</td>
<td align="right">811,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">411,805</td>
<td align="right">411,805</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">407,686</td>
<td align="right">407,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">403,567</td>
<td align="right">403,567</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">22,288</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">11,580</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">10,752</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">882</td>
<td align="right">882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">882</td>
<td align="right">882</td>
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
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">112</td>
<td align="right">22</td>
<td align="right">-80.4%</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-21
