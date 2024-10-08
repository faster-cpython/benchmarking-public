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
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">19,061,976</td>
<td align="right">240,902</td>
<td align="right">-98.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">19,842,309</td>
<td align="right">780,997</td>
<td align="right">-96.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,066,728</td>
<td align="right">318,892</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">25,017,094</td>
<td align="right">3,099,962</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">30,058,681</td>
<td align="right">3,844,102</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">20,166,041</td>
<td align="right">2,854,173</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">15,488,927</td>
<td align="right">2,516,442</td>
<td align="right">-83.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,572,610</td>
<td align="right">262,100</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,181,939</td>
<td align="right">208,630</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">5,713,734</td>
<td align="right">1,023,730</td>
<td align="right">-82.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,472,860</td>
<td align="right">363,397</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,349,061</td>
<td align="right">375,858</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,380,465</td>
<td align="right">403,664</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,080,584</td>
<td align="right">1,613,460</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">57,490,457</td>
<td align="right">18,429,065</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">41,988,899</td>
<td align="right">16,209,506</td>
<td align="right">-61.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">44,907,642</td>
<td align="right">17,845,035</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">144,851,048</td>
<td align="right">61,238,013</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">17,410,293</td>
<td align="right">7,811,461</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,349,147</td>
<td align="right">612,964</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,685,698</td>
<td align="right">792,274</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">519,360</td>
<td align="right">253,806</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">178,058,708</td>
<td align="right">91,277,365</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">32,923,034</td>
<td align="right">16,974,346</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,390,429</td>
<td align="right">4,485,344</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33,402,096</td>
<td align="right">17,870,960</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">31,044,869</td>
<td align="right">16,614,896</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,591,691</td>
<td align="right">878,298</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">6,854,950</td>
<td align="right">3,789,508</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">39,394,905</td>
<td align="right">21,968,339</td>
<td align="right">-44.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">24,651,477</td>
<td align="right">13,791,882</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">10,489,439</td>
<td align="right">5,949,923</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">13,512,518</td>
<td align="right">7,701,327</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">533,098</td>
<td align="right">307,148</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">202,315,149</td>
<td align="right">122,711,360</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">175,184,179</td>
<td align="right">108,384,283</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">56,066,147</td>
<td align="right">35,418,116</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">93,677</td>
<td align="right">59,578</td>
<td align="right">-36.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">532,818</td>
<td align="right">340,735</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">40,192,887</td>
<td align="right">25,860,516</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,587,153</td>
<td align="right">2,320,786</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">46,749,264</td>
<td align="right">30,375,399</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">27,591,719</td>
<td align="right">18,117,693</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">49,963,699</td>
<td align="right">32,953,114</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,041,587</td>
<td align="right">1,356,569</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">15,644,561</td>
<td align="right">10,416,007</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">63,800</td>
<td align="right">42,600</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,733,435</td>
<td align="right">14,771,330</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">608,534,198</td>
<td align="right">418,657,005</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">176,733,189</td>
<td align="right">122,235,746</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">124,106,703</td>
<td align="right">86,245,689</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">7,526,878</td>
<td align="right">5,283,995</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">43,772,260</td>
<td align="right">30,845,517</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">23,972,707</td>
<td align="right">17,046,911</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">906,456</td>
<td align="right">645,411</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">14,281,215</td>
<td align="right">10,250,726</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,549,155</td>
<td align="right">1,124,218</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">118,535,335</td>
<td align="right">86,945,426</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">52,060,395</td>
<td align="right">38,356,600</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">119,124</td>
<td align="right">87,813</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">42,275,850</td>
<td align="right">31,433,265</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">859,356</td>
<td align="right">1,074,668</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">56,517,202</td>
<td align="right">42,403,347</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,628,490</td>
<td align="right">2,007,572</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">22,567,336</td>
<td align="right">17,340,113</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">14,402,928</td>
<td align="right">11,211,980</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,483,256</td>
<td align="right">4,277,435</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">23,055,157</td>
<td align="right">18,031,804</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">10,158,364</td>
<td align="right">7,957,957</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">92,265,072</td>
<td align="right">72,872,542</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">795,461</td>
<td align="right">629,827</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">411,864</td>
<td align="right">328,069</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">8,231,140</td>
<td align="right">6,613,602</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,522,389</td>
<td align="right">2,064,734</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">22,506</td>
<td align="right">18,498</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">32,281,184</td>
<td align="right">26,551,740</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,091,981</td>
<td align="right">4,215,709</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">21,563,501</td>
<td align="right">17,876,670</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">209,456</td>
<td align="right">174,774</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">64,321,784</td>
<td align="right">54,468,449</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,124,464</td>
<td align="right">3,508,491</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">166,576</td>
<td align="right">143,444</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">282,560</td>
<td align="right">245,360</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">282,600</td>
<td align="right">245,400</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">917,501</td>
<td align="right">798,270</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">137,906</td>
<td align="right">120,092</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,900,546</td>
<td align="right">4,314,178</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,908,043</td>
<td align="right">3,440,828</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">251,832</td>
<td align="right">280,770</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">140,940</td>
<td align="right">124,860</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">33,524</td>
<td align="right">29,926</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">3,551,291</td>
<td align="right">3,171,909</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">162,018</td>
<td align="right">145,521</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">11,420</td>
<td align="right">10,260</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">136,395,470</td>
<td align="right">122,872,156</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">178,889,442</td>
<td align="right">162,319,443</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,889,609</td>
<td align="right">1,715,706</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,890,301</td>
<td align="right">3,541,361</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,144,455</td>
<td align="right">1,956,960</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">14,028,689</td>
<td align="right">12,862,860</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">6,688,281</td>
<td align="right">6,156,589</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,805,174</td>
<td align="right">7,186,117</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">775,488</td>
<td align="right">714,134</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">24,695,226</td>
<td align="right">22,800,096</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">18,383,566</td>
<td align="right">17,020,876</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,938,383</td>
<td align="right">10,133,582</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">264,443</td>
<td align="right">247,013</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">17,289,622</td>
<td align="right">16,159,606</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">142,394</td>
<td align="right">133,456</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">21,872,147</td>
<td align="right">20,577,026</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,110,459</td>
<td align="right">1,987,561</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,132,557</td>
<td align="right">2,951,172</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,992,868</td>
<td align="right">8,524,082</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">49,978</td>
<td align="right">47,853</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,443,195</td>
<td align="right">2,351,602</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">543,647</td>
<td align="right">523,907</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,570,949</td>
<td align="right">4,413,172</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">39,704</td>
<td align="right">38,862</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,686,652</td>
<td align="right">1,651,290</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">9,434,623</td>
<td align="right">9,248,798</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,312,483</td>
<td align="right">3,259,713</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">227,509</td>
<td align="right">224,267</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,870,416</td>
<td align="right">2,839,274</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">233,080</td>
<td align="right">230,786</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">13,189,474</td>
<td align="right">13,088,869</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,668,770</td>
<td align="right">12,605,146</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">28,783,581</td>
<td align="right">28,677,132</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">12,470,843</td>
<td align="right">12,439,320</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">867,402</td>
<td align="right">865,542</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">126,333,430</td>
<td align="right">126,159,330</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">47,563</td>
<td align="right">47,581</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">210,280</td>
<td align="right">210,350</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,594,414</td>
<td align="right">2,593,555</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">119,064</td>
<td align="right">119,102</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">181,915</td>
<td align="right">181,973</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">906,456</td>
<td align="right">906,694</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">906,456</td>
<td align="right">906,694</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">262,636</td>
<td align="right">262,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">532,224</td>
<td align="right">532,176</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,029,884</td>
<td align="right">1,029,836</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">28,012,360</td>
<td align="right">28,013,128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,121,267</td>
<td align="right">1,121,295</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">4,746,354</td>
<td align="right">4,746,244</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,784,043</td>
<td align="right">1,784,069</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">887,842</td>
<td align="right">887,834</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">442,840</td>
<td align="right">442,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">139,060</td>
<td align="right">139,060</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">71,900</td>
<td align="right">71,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">19,260</td>
<td align="right">19,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,768</td>
<td align="right">12,768</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,740</td>
<td align="right">4,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">4,008</td>
<td align="right">4,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">3,540</td>
<td align="right">3,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">3,100</td>
<td align="right">3,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">2,660</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,540</td>
<td align="right">2,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,040</td>
<td align="right">2,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,840</td>
<td align="right">1,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">1,204</td>
<td align="right">1,204</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">920</td>
<td align="right">920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
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
<td align="right">30,003,277</td>
<td align="right">61.4%</td>
<td align="right">3,796,461</td>
<td align="right">16.7%</td>
<td align="right">-87.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,839,092</td>
<td align="right">38.5%</td>
<td align="right">18,840,371</td>
<td align="right">83.1%</td>
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
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">120</td>
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
<td align="right">48,674</td>
<td align="right">87.9%</td>
<td align="right">40,885</td>
<td align="right">85.8%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,730</td>
<td align="right">12.1%</td>
<td align="right">6,756</td>
<td align="right">14.2%</td>
<td align="right">0.4%</td>
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
<td align="right">3,700</td>
<td align="right">7.6%</td>
<td align="right">1,020</td>
<td align="right">2.5%</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,080</td>
<td align="right">12.5%</td>
<td align="right">3,686</td>
<td align="right">9.0%</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,148</td>
<td align="right">18.8%</td>
<td align="right">7,025</td>
<td align="right">17.2%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,884</td>
<td align="right">8.0%</td>
<td align="right">3,588</td>
<td align="right">8.8%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,826</td>
<td align="right">7.9%</td>
<td align="right">3,605</td>
<td align="right">8.8%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,861</td>
<td align="right">5.9%</td>
<td align="right">2,797</td>
<td align="right">6.8%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,523</td>
<td align="right">5.2%</td>
<td align="right">2,504</td>
<td align="right">6.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,137</td>
<td align="right">4.4%</td>
<td align="right">2,148</td>
<td align="right">5.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">225</td>
<td align="right">0.5%</td>
<td align="right">224</td>
<td align="right">0.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">1,172</td>
<td align="right">2.4%</td>
<td align="right">1,176</td>
<td align="right">2.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,184</td>
<td align="right">2.4%</td>
<td align="right">1,187</td>
<td align="right">2.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,812</td>
<td align="right">3.7%</td>
<td align="right">1,816</td>
<td align="right">4.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,806</td>
<td align="right">14.0%</td>
<td align="right">6,794</td>
<td align="right">16.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">583</td>
<td align="right">1.2%</td>
<td align="right">584</td>
<td align="right">1.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">2,054</td>
<td align="right">4.2%</td>
<td align="right">2,051</td>
<td align="right">5.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">376</td>
<td align="right">0.8%</td>
<td align="right">376</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">300</td>
<td align="right">0.6%</td>
<td align="right">300</td>
<td align="right">0.7%</td>
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
<td align="right">532,818</td>
<td align="right">100.0%</td>
<td align="right">340,735</td>
<td align="right">100.0%</td>
<td align="right">-36.1%</td>
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
<td align="right">3,569,229</td>
<td align="right">7.7%</td>
<td align="right">2,303,588</td>
<td align="right">5.1%</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">14,915</td>
<td align="right">0.0%</td>
<td align="right">13,689</td>
<td align="right">0.0%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">42,685,577</td>
<td align="right">92.2%</td>
<td align="right">42,647,430</td>
<td align="right">94.8%</td>
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
<td align="right">10,448</td>
<td align="right">57.5%</td>
<td align="right">9,738</td>
<td align="right">55.9%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,716</td>
<td align="right">42.5%</td>
<td align="right">7,691</td>
<td align="right">44.1%</td>
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
<td align="left">tuple slice</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,245</td>
<td align="right">69.3%</td>
<td align="right">6,614</td>
<td align="right">67.9%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,960</td>
<td align="right">18.8%</td>
<td align="right">1,880</td>
<td align="right">19.3%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">1,220</td>
<td align="right">11.7%</td>
<td align="right">1,220</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
<td align="right">0.2%</td>
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
<td align="right">29,717,635</td>
<td align="right">7.2%</td>
<td align="right">25,959,398</td>
<td align="right">6.3%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">385,033,382</td>
<td align="right">92.8%</td>
<td align="right">388,719,873</td>
<td align="right">93.7%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,200</td>
<td align="right">0.0%</td>
<td align="right">22,248</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">167,559</td>
<td align="right">0.0%</td>
<td align="right">167,604</td>
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
<td align="right">659,271</td>
<td align="right">100.0%</td>
<td align="right">588,426</td>
<td align="right">100.0%</td>
<td align="right">-10.7%</td>
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
<td align="right">260</td>
<td align="right">260 / 0 !!</td>
<td align="right">260</td>
<td align="right">260 / 0 !!</td>
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
<td align="right">7,986</td>
<td align="right">48.9%</td>
<td align="right">7,988</td>
<td align="right">48.9%</td>
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
<td align="right">3,580</td>
<td align="right">21.9%</td>
<td align="right">3,580</td>
<td align="right">21.9%</td>
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
<td align="right">500,830</td>
<td align="right">0.5%</td>
<td align="right">117,586</td>
<td align="right">0.1%</td>
<td align="right">-76.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">24,576,711</td>
<td align="right">26.9%</td>
<td align="right">13,739,240</td>
<td align="right">17.5%</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">66,079,814</td>
<td align="right">72.4%</td>
<td align="right">64,508,416</td>
<td align="right">82.3%</td>
<td align="right">-2.4%</td>
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
<td align="right">18,887</td>
<td align="right">22.5%</td>
<td align="right">11,648</td>
<td align="right">21.3%</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">65,116</td>
<td align="right">77.5%</td>
<td align="right">43,003</td>
<td align="right">78.7%</td>
<td align="right">-34.0%</td>
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
<td align="right">10,320</td>
<td align="right">15.8%</td>
<td align="right">1,322</td>
<td align="right">3.1%</td>
<td align="right">-87.2%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">17,604</td>
<td align="right">27.0%</td>
<td align="right">7,419</td>
<td align="right">17.3%</td>
<td align="right">-57.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">13,464</td>
<td align="right">20.7%</td>
<td align="right">11,728</td>
<td align="right">27.3%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,930</td>
<td align="right">15.2%</td>
<td align="right">8,891</td>
<td align="right">20.7%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">260</td>
<td align="right">0.6%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">360</td>
<td align="right">0.8%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">12,146</td>
<td align="right">18.7%</td>
<td align="right">11,994</td>
<td align="right">27.9%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">452</td>
<td align="right">0.7%</td>
<td align="right">449</td>
<td align="right">1.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">280</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">220</td>
<td align="right">0.3%</td>
<td align="right">220</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.2%</td>
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
<td align="right">2,030,356</td>
<td align="right">6.4%</td>
<td align="right">1,345,758</td>
<td align="right">4.3%</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,686,307</td>
<td align="right">93.6%</td>
<td align="right">29,686,471</td>
<td align="right">95.6%</td>
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
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">1,200</td>
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
<td align="right">9,991</td>
<td align="right">89.0%</td>
<td align="right">9,571</td>
<td align="right">88.5%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,240</td>
<td align="right">11.0%</td>
<td align="right">1,240</td>
<td align="right">11.5%</td>
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
<td align="right">3,554</td>
<td align="right">35.6%</td>
<td align="right">3,284</td>
<td align="right">34.3%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">5,257</td>
<td align="right">52.6%</td>
<td align="right">5,109</td>
<td align="right">53.4%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">900</td>
<td align="right">9.0%</td>
<td align="right">898</td>
<td align="right">9.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">280</td>
<td align="right">2.8%</td>
<td align="right">280</td>
<td align="right">2.9%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,543,764</td>
<td align="right">55.3%</td>
<td align="right">18,072,517</td>
<td align="right">55.0%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">22,062,844</td>
<td align="right">44.3%</td>
<td align="right">14,595,172</td>
<td align="right">44.5%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">125,423</td>
<td align="right">0.3%</td>
<td align="right">117,119</td>
<td align="right">0.4%</td>
<td align="right">-6.6%</td>
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
<td align="right">35,937</td>
<td align="right">71.6%</td>
<td align="right">33,172</td>
<td align="right">70.2%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">14,267</td>
<td align="right">28.4%</td>
<td align="right">14,105</td>
<td align="right">29.8%</td>
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
<td align="left">zip</td>
<td align="right">4,720</td>
<td align="right">13.1%</td>
<td align="right">2,481</td>
<td align="right">7.5%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">4,108</td>
<td align="right">11.4%</td>
<td align="right">3,797</td>
<td align="right">11.4%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">17,499</td>
<td align="right">48.7%</td>
<td align="right">17,243</td>
<td align="right">52.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,962</td>
<td align="right">5.5%</td>
<td align="right">1,980</td>
<td align="right">6.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,468</td>
<td align="right">9.7%</td>
<td align="right">3,491</td>
<td align="right">10.5%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">1,840</td>
<td align="right">5.1%</td>
<td align="right">1,840</td>
<td align="right">5.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,400</td>
<td align="right">3.9%</td>
<td align="right">1,400</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">780</td>
<td align="right">2.2%</td>
<td align="right">780</td>
<td align="right">2.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">80</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">34,978,715</td>
<td align="right">8.9%</td>
<td align="right">26,924,033</td>
<td align="right">7.0%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">64,105,901</td>
<td align="right">16.3%</td>
<td align="right">54,256,667</td>
<td align="right">14.2%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">294,445,246</td>
<td align="right">74.8%</td>
<td align="right">300,945,152</td>
<td align="right">78.7%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,500</td>
<td align="right">0.0%</td>
<td align="right">22,445</td>
<td align="right">0.0%</td>
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
<td align="right">744,040</td>
<td align="right">85.8%</td>
<td align="right">592,360</td>
<td align="right">83.3%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">122,752</td>
<td align="right">14.2%</td>
<td align="right">118,637</td>
<td align="right">16.7%</td>
<td align="right">-3.4%</td>
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
<td align="left">builtin class method</td>
<td align="right">880</td>
<td align="right">0.7%</td>
<td align="right">666</td>
<td align="right">0.6%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">9,314</td>
<td align="right">7.6%</td>
<td align="right">8,474</td>
<td align="right">7.1%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">11,881</td>
<td align="right">9.7%</td>
<td align="right">11,332</td>
<td align="right">9.6%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4,800</td>
<td align="right">3.9%</td>
<td align="right">4,586</td>
<td align="right">3.9%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">7,806</td>
<td align="right">6.4%</td>
<td align="right">7,549</td>
<td align="right">6.4%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">59,702</td>
<td align="right">48.6%</td>
<td align="right">58,070</td>
<td align="right">48.9%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,927</td>
<td align="right">7.3%</td>
<td align="right">8,689</td>
<td align="right">7.3%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">15,120</td>
<td align="right">12.3%</td>
<td align="right">14,952</td>
<td align="right">12.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">442</td>
<td align="right">0.4%</td>
<td align="right">440</td>
<td align="right">0.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
<td align="right">0.1%</td>
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
<td align="right">269,324,084</td>
<td align="right">99.9%</td>
<td align="right">183,671,103</td>
<td align="right">99.9%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">90,083</td>
<td align="right">0.0%</td>
<td align="right">90,142</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">20,380</td>
<td align="right">0.0%</td>
<td align="right">20,380</td>
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
<td align="right">91,992</td>
<td align="right">100.0%</td>
<td align="right">91,991</td>
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
<td align="right">2,996,062</td>
<td align="right">100.0%</td>
<td align="right">2,996,157</td>
<td align="right">100.0%</td>
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
<td align="right">604</td>
<td align="right">0.0%</td>
<td align="right">604</td>
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
<td align="right">600</td>
<td align="right">100.0%</td>
<td align="right">600</td>
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
<td align="right">999,224</td>
<td align="right">67.8%</td>
<td align="right">999,176</td>
<td align="right">67.8%</td>
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
<td align="right">439,720</td>
<td align="right">29.9%</td>
<td align="right">439,720</td>
<td align="right">29.9%</td>
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
<td align="right">2.1%</td>
<td align="right">30,660</td>
<td align="right">2.1%</td>
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
<td align="right">620</td>
<td align="right">16.8%</td>
<td align="right">620</td>
<td align="right">16.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,080</td>
<td align="right">83.2%</td>
<td align="right">3,080</td>
<td align="right">83.2%</td>
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
<td align="left">list</td>
<td align="right">3,080</td>
<td align="right">100.0%</td>
<td align="right">3,080</td>
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
<td align="right">533,712</td>
<td align="right">4.4%</td>
<td align="right">693,767</td>
<td align="right">5.7%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">403,058</td>
<td align="right">3.4%</td>
<td align="right">319,421</td>
<td align="right">2.6%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,049,119</td>
<td align="right">92.1%</td>
<td align="right">11,051,087</td>
<td align="right">91.5%</td>
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
<td align="right">15,031</td>
<td align="right">80.2%</td>
<td align="right">18,048</td>
<td align="right">83.6%</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,706</td>
<td align="right">19.8%</td>
<td align="right">3,548</td>
<td align="right">16.4%</td>
<td align="right">-4.3%</td>
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
<td align="right">1,960</td>
<td align="right">52.9%</td>
<td align="right">1,800</td>
<td align="right">50.7%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,446</td>
<td align="right">39.0%</td>
<td align="right">1,448</td>
<td align="right">40.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">240</td>
<td align="right">6.5%</td>
<td align="right">240</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">60</td>
<td align="right">1.6%</td>
<td align="right">60</td>
<td align="right">1.7%</td>
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
<td align="right">920</td>
<td align="right">100.0%</td>
<td align="right">920</td>
<td align="right">100.0%</td>
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
<td align="right">203,852</td>
<td align="right">0.9%</td>
<td align="right">169,271</td>
<td align="right">0.7%</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">22,625,169</td>
<td align="right">99.1%</td>
<td align="right">22,626,055</td>
<td align="right">99.2%</td>
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
<td align="right">2,882</td>
<td align="right">51.4%</td>
<td align="right">2,783</td>
<td align="right">50.6%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,722</td>
<td align="right">48.6%</td>
<td align="right">2,720</td>
<td align="right">49.4%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">2,882</td>
<td align="right">100.0%</td>
<td align="right">2,783</td>
<td align="right">100.0%</td>
<td align="right">-3.4%</td>
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
<td align="right">439,992</td>
<td align="right">0.2%</td>
<td align="right">423,309</td>
<td align="right">0.2%</td>
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
<td align="right">197,056,126</td>
<td align="right">93.8%</td>
<td align="right">189,782,687</td>
<td align="right">93.6%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,593,340</td>
<td align="right">6.0%</td>
<td align="right">12,529,835</td>
<td align="right">6.2%</td>
<td align="right">-0.5%</td>
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
<td align="right">22,793</td>
<td align="right">27.6%</td>
<td align="right">22,673</td>
<td align="right">27.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">59,747</td>
<td align="right">72.4%</td>
<td align="right">59,470</td>
<td align="right">72.4%</td>
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
<td align="left">number</td>
<td align="right">3,500</td>
<td align="right">15.4%</td>
<td align="right">3,451</td>
<td align="right">15.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,835</td>
<td align="right">47.5%</td>
<td align="right">10,759</td>
<td align="right">47.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,637</td>
<td align="right">7.2%</td>
<td align="right">1,647</td>
<td align="right">7.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,441</td>
<td align="right">6.3%</td>
<td align="right">1,436</td>
<td align="right">6.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">3,260</td>
<td align="right">14.3%</td>
<td align="right">3,260</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,080</td>
<td align="right">9.1%</td>
<td align="right">2,080</td>
<td align="right">9.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">105,670,133</td>
<td align="right">100.0%</td>
<td align="right">88,068,894</td>
<td align="right">100.0%</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,540</td>
<td align="right">0.0%</td>
<td align="right">26,714</td>
<td align="right">0.0%</td>
<td align="right">-3.0%</td>
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
<td align="right">776</td>
<td align="right">6.4%</td>
<td align="right">756</td>
<td align="right">6.2%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,388</td>
<td align="right">93.6%</td>
<td align="right">11,392</td>
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
<td align="right">716</td>
<td align="right">92.3%</td>
<td align="right">696</td>
<td align="right">92.1%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">60</td>
<td align="right">7.7%</td>
<td align="right">60</td>
<td align="right">7.9%</td>
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
<td align="right">1,206,388,852</td>
<td align="right">31.7%</td>
<td align="right">780,787,171</td>
<td align="right">30.2%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">167,017,296</td>
<td align="right">4.4%</td>
<td align="right">108,289,451</td>
<td align="right">4.2%</td>
<td align="right">-35.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,366,231,867</td>
<td align="right">62.2%</td>
<td align="right">1,640,890,878</td>
<td align="right">63.5%</td>
<td align="right">-30.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">66,368,428</td>
<td align="right">1.7%</td>
<td align="right">54,306,765</td>
<td align="right">2.1%</td>
<td align="right">-18.2%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">30,003,277</td>
<td align="right">18.0%</td>
<td align="right">3,796,461</td>
<td align="right">3.5%</td>
<td align="right">-87.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">24,576,711</td>
<td align="right">14.8%</td>
<td align="right">13,739,240</td>
<td align="right">12.8%</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">532,818</td>
<td align="right">0.3%</td>
<td align="right">340,735</td>
<td align="right">0.3%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,569,229</td>
<td align="right">2.1%</td>
<td align="right">2,303,588</td>
<td align="right">2.1%</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">27,543,764</td>
<td align="right">16.6%</td>
<td align="right">18,072,517</td>
<td align="right">16.8%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,030,356</td>
<td align="right">1.2%</td>
<td align="right">1,345,758</td>
<td align="right">1.3%</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">403,058</td>
<td align="right">0.2%</td>
<td align="right">319,421</td>
<td align="right">0.3%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">64,105,901</td>
<td align="right">38.5%</td>
<td align="right">54,256,667</td>
<td align="right">50.4%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,593,340</td>
<td align="right">7.6%</td>
<td align="right">12,529,835</td>
<td align="right">11.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">439,720</td>
<td align="right">0.3%</td>
<td align="right">439,720</td>
<td align="right">0.4%</td>
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
<td align="right">5,962,807</td>
<td align="right">9.0%</td>
<td align="right">1,695,309</td>
<td align="right">3.1%</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,043,559</td>
<td align="right">9.1%</td>
<td align="right">2,300,028</td>
<td align="right">4.2%</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">532,732</td>
<td align="right">0.8%</td>
<td align="right">692,787</td>
<td align="right">1.3%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">13,946,681</td>
<td align="right">21.0%</td>
<td align="right">11,125,093</td>
<td align="right">20.5%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,801,480</td>
<td align="right">5.7%</td>
<td align="right">3,463,014</td>
<td align="right">6.4%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">10,688,110</td>
<td align="right">16.1%</td>
<td align="right">10,136,103</td>
<td align="right">18.7%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">14,423,953</td>
<td align="right">21.7%</td>
<td align="right">14,408,629</td>
<td align="right">26.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">6,512,354</td>
<td align="right">9.8%</td>
<td align="right">6,512,244</td>
<td align="right">12.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,661,163</td>
<td align="right">4.0%</td>
<td align="right">2,661,185</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">499,230</td>
<td align="right">0.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">251,873</td>
<td align="right">0.5%</td>
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
<td align="left">Frame objects created</td>
<td align="right">1,350,072</td>
<td align="right">0.5%</td>
<td align="right">1,343,021</td>
<td align="right">0.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">52,933,474</td>
<td align="right">19.4%</td>
<td align="right">52,772,247</td>
<td align="right">19.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">97,378,360</td>
<td align="right">35.7%</td>
<td align="right">97,217,999</td>
<td align="right">35.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">97,385,660</td>
<td align="right">35.7%</td>
<td align="right">97,225,299</td>
<td align="right">35.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">126,568,462</td>
<td align="right">46.4%</td>
<td align="right">126,390,764</td>
<td align="right">46.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">126,568,462</td>
<td align="right">46.4%</td>
<td align="right">126,390,764</td>
<td align="right">46.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">146,135,085</td>
<td align="right">53.6%</td>
<td align="right">146,318,316</td>
<td align="right">53.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">29,182,802</td>
<td align="right">10.7%</td>
<td align="right">29,165,465</td>
<td align="right">10.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">243,204,406</td>
<td align="right">89.2%</td>
<td align="right">243,227,186</td>
<td align="right">89.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">23,783,239</td>
<td align="right">8.7%</td>
<td align="right">23,783,642</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">11,824,722</td>
<td align="right">4.3%</td>
<td align="right">11,824,918</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">6,960</td>
<td align="right">0.0%</td>
<td align="right">6,960</td>
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
<td align="left">Interpreter immortal increfs</td>
<td align="right">671,370,808</td>
<td align="right">10.0%</td>
<td align="right">479,056,898</td>
<td align="right">7.1%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,808,617,735</td>
<td align="right">27.0%</td>
<td align="right">1,296,582,780</td>
<td align="right">19.1%</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">813,274,614</td>
<td align="right">10.7%</td>
<td align="right">608,510,925</td>
<td align="right">7.9%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">2,639,322,749</td>
<td align="right">39.4%</td>
<td align="right">3,265,693,458</td>
<td align="right">48.2%</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">2,737,285,416</td>
<td align="right">35.9%</td>
<td align="right">3,314,314,231</td>
<td align="right">42.9%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">2,294,568,417</td>
<td align="right">30.1%</td>
<td align="right">1,849,450,088</td>
<td align="right">24.0%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">1,770,193,655</td>
<td align="right">23.2%</td>
<td align="right">1,946,958,387</td>
<td align="right">25.2%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">1,581,820,402</td>
<td align="right">23.6%</td>
<td align="right">1,729,794,638</td>
<td align="right">25.5%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,457,946</td>
<td align="right"></td>
<td align="right">1,543,944</td>
<td align="right"></td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">301,231,903</td>
<td align="right">45.2%</td>
<td align="right">318,806,955</td>
<td align="right">46.6%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">302,351,654</td>
<td align="right">45.3%</td>
<td align="right">319,957,291</td>
<td align="right">46.7%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">316,319,168</td>
<td align="right"></td>
<td align="right">333,911,142</td>
<td align="right"></td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">5,429,696</td>
<td align="right"></td>
<td align="right">5,593,919</td>
<td align="right"></td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,095,291</td>
<td align="right">0.2%</td>
<td align="right">1,125,874</td>
<td align="right">0.2%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">184,373,825</td>
<td align="right"></td>
<td align="right">179,818,562</td>
<td align="right"></td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">3,975,920</td>
<td align="right"></td>
<td align="right">4,054,010</td>
<td align="right"></td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">338,143,931</td>
<td align="right"></td>
<td align="right">335,912,300</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">24,460</td>
<td align="right">0.0%</td>
<td align="right">24,462</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,392,899</td>
<td align="right"></td>
<td align="right">1,392,982</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">364,509,832</td>
<td align="right">54.7%</td>
<td align="right">364,497,501</td>
<td align="right">53.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">364,746,504</td>
<td align="right"></td>
<td align="right">364,734,179</td>
<td align="right"></td>
<td align="right">-0.0%</td>
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
<td align="right">89,140</td>
<td align="right">50.3%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">348</td>
<td align="right">0.4%</td>
<td align="right">601</td>
<td align="right">0.4%</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">86,534</td>
<td align="right">48.8%</td>
<td align="right">135,102</td>
<td align="right">75.3%</td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">90,678</td>
<td align="right">51.2%</td>
<td align="right">44,432</td>
<td align="right">24.7%</td>
<td align="right">-51.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">5,552,054,556</td>
<td align="right">1,515.7%</td>
<td align="right">8,011,146,965</td>
<td align="right">1,610.7%</td>
<td align="right">44.3%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,269</td>
<td align="right">3.5%</td>
<td align="right">8,695</td>
<td align="right">4.8%</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">366,296,169</td>
<td align="right"></td>
<td align="right">497,371,271</td>
<td align="right"></td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">558</td>
<td align="right">0.3%</td>
<td align="right">543</td>
<td align="right">0.3%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">177,212</td>
<td align="right"></td>
<td align="right">179,534</td>
<td align="right"></td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">1,195</td>
<td align="right">0.7%</td>
<td align="right">1,189</td>
<td align="right">0.7%</td>
<td align="right">-0.5%</td>
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
<td align="right">82,496</td>
<td align="right">95.3%</td>
<td align="right">130,347</td>
<td align="right">96.5%</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">86,534</td>
<td align="right"></td>
<td align="right">135,102</td>
<td align="right"></td>
<td align="right">56.1%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">170</td>
<td align="right">0.1%</td>
<td align="right">6.2%</td>
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
<td align="right">8,421</td>
<td align="right">9.7%</td>
<td align="right">10,571</td>
<td align="right">7.8%</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">12,333</td>
<td align="right">14.3%</td>
<td align="right">23,188</td>
<td align="right">17.2%</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">35,431</td>
<td align="right">40.9%</td>
<td align="right">53,720</td>
<td align="right">39.8%</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22,325</td>
<td align="right">25.8%</td>
<td align="right">35,536</td>
<td align="right">26.3%</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,351</td>
<td align="right">8.5%</td>
<td align="right">10,885</td>
<td align="right">8.1%</td>
<td align="right">48.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">673</td>
<td align="right">0.8%</td>
<td align="right">1,202</td>
<td align="right">0.9%</td>
<td align="right">78.6%</td>
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
<td align="right">5,626</td>
<td align="right">6.5%</td>
<td align="right">1,809</td>
<td align="right">1.3%</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">6,615</td>
<td align="right">7.6%</td>
<td align="right">15,544</td>
<td align="right">11.5%</td>
<td align="right">135.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20,526</td>
<td align="right">23.7%</td>
<td align="right">37,366</td>
<td align="right">27.7%</td>
<td align="right">82.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">31,901</td>
<td align="right">36.9%</td>
<td align="right">47,141</td>
<td align="right">34.9%</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">16,076</td>
<td align="right">18.6%</td>
<td align="right">25,523</td>
<td align="right">18.9%</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1,710</td>
<td align="right">2.0%</td>
<td align="right">2,880</td>
<td align="right">2.1%</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">0.1%</td>
<td align="right">100.0%</td>
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
<td align="right">5,720</td>
<td align="right">1,316,247</td>
<td align="right">22,911.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">320</td>
<td align="right">52,761</td>
<td align="right">16,387.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">53,420</td>
<td align="right">4,743,477</td>
<td align="right">8,779.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,540</td>
<td align="right">173,086</td>
<td align="right">6,714.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,602,929</td>
<td align="right">109,072,944</td>
<td align="right">6,704.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">2,100</td>
<td align="right">88,754</td>
<td align="right">4,126.4%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,920</td>
<td align="right">39,120</td>
<td align="right">1,937.5%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,920</td>
<td align="right">39,120</td>
<td align="right">1,937.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">960</td>
<td align="right">17,040</td>
<td align="right">1,675.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,279,820</td>
<td align="right">20,101,747</td>
<td align="right">1,470.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">557,948</td>
<td align="right">8,095,506</td>
<td align="right">1,350.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">61,800</td>
<td align="right">591,465</td>
<td align="right">857.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">3,265,229</td>
<td align="right">25,182,676</td>
<td align="right">671.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">605,555</td>
<td align="right">4,512,112</td>
<td align="right">645.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">360</td>
<td align="right">2,612</td>
<td align="right">625.6%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">815,392</td>
<td align="right">5,563,151</td>
<td align="right">582.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">36,234</td>
<td align="right">228,304</td>
<td align="right">530.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">5,441,803</td>
<td align="right">31,649,484</td>
<td align="right">481.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,849,835</td>
<td align="right">21,162,801</td>
<td align="right">449.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">39,300</td>
<td align="right">212,460</td>
<td align="right">440.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">31,816,104</td>
<td align="right">167,792,707</td>
<td align="right">427.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">31,596</td>
<td align="right">150,023</td>
<td align="right">374.8%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">980</td>
<td align="right">4,547</td>
<td align="right">364.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">7,567,219</td>
<td align="right">33,712,734</td>
<td align="right">345.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">4,319,168</td>
<td align="right">17,292,593</td>
<td align="right">300.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">80,270</td>
<td align="right">306,325</td>
<td align="right">281.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">527,009</td>
<td align="right">1,567,536</td>
<td align="right">197.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">11,040</td>
<td align="right">32,240</td>
<td align="right">192.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">5,083,976</td>
<td align="right">14,683,302</td>
<td align="right">188.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">10,354,043</td>
<td align="right">29,400,025</td>
<td align="right">183.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">5,231,069</td>
<td align="right">14,829,943</td>
<td align="right">183.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">925,388</td>
<td align="right">2,544,802</td>
<td align="right">175.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">8,189,790</td>
<td align="right">22,481,255</td>
<td align="right">174.5%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,842,802</td>
<td align="right">4,908,349</td>
<td align="right">166.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">23,066,374</td>
<td align="right">58,283,083</td>
<td align="right">152.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">21,255,270</td>
<td align="right">52,857,177</td>
<td align="right">148.7%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">406,983</td>
<td align="right">993,543</td>
<td align="right">144.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">5,126,018</td>
<td align="right">11,879,505</td>
<td align="right">131.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">27,307,792</td>
<td align="right">62,349,031</td>
<td align="right">128.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">378,126</td>
<td align="right">848,299</td>
<td align="right">124.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">378,126</td>
<td align="right">848,299</td>
<td align="right">124.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">17,940,304</td>
<td align="right">38,883,154</td>
<td align="right">116.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">31,962,042</td>
<td align="right">68,560,887</td>
<td align="right">114.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">13,279,380</td>
<td align="right">27,530,914</td>
<td align="right">107.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">6,375,796</td>
<td align="right">13,163,748</td>
<td align="right">106.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">50,830,310</td>
<td align="right">103,451,620</td>
<td align="right">103.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">14,470,910</td>
<td align="right">28,901,908</td>
<td align="right">99.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,799,643</td>
<td align="right">41,119,858</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">17,722,040</td>
<td align="right">34,734,283</td>
<td align="right">96.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">20,400,851</td>
<td align="right">39,899,242</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">14,030,891</td>
<td align="right">26,853,851</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">50,045,139</td>
<td align="right">95,491,467</td>
<td align="right">90.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">50,584,210</td>
<td align="right">93,785,672</td>
<td align="right">85.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">20,703,563</td>
<td align="right">38,114,985</td>
<td align="right">84.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">13,765,810</td>
<td align="right">24,544,693</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">40,120</td>
<td align="right">71,435</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">40,120</td>
<td align="right">71,435</td>
<td align="right">78.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">18,482,527</td>
<td align="right">32,475,031</td>
<td align="right">75.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,932,015</td>
<td align="right">8,564,200</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">172,914</td>
<td align="right">295,845</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">15,368,858</td>
<td align="right">25,919,710</td>
<td align="right">68.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">22,927,545</td>
<td align="right">38,414,484</td>
<td align="right">67.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">4,490,898</td>
<td align="right">7,490,916</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">57,633,204</td>
<td align="right">96,027,241</td>
<td align="right">66.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">23,584,234</td>
<td align="right">39,098,071</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">112,548,139</td>
<td align="right">184,480,993</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">48,289,013</td>
<td align="right">79,024,869</td>
<td align="right">63.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">73,886,611</td>
<td align="right">118,212,494</td>
<td align="right">60.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">456,836</td>
<td align="right">187,708</td>
<td align="right">-58.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">334,394</td>
<td align="right">520,608</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">337,534</td>
<td align="right">523,748</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">7,344,063</td>
<td align="right">11,375,914</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">1,149,258</td>
<td align="right">1,769,351</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">4,319</td>
<td align="right">2,003</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">4,319</td>
<td align="right">2,003</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">2,562,198</td>
<td align="right">3,929,992</td>
<td align="right">53.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,663,074</td>
<td align="right">2,532,868</td>
<td align="right">52.3%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">313,651</td>
<td align="right">474,838</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">1,070,980</td>
<td align="right">1,603,502</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">46,408,426</td>
<td align="right">69,295,709</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">46,566,826</td>
<td align="right">69,521,473</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">100,093,584</td>
<td align="right">148,818,969</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">200,045,489</td>
<td align="right">295,603,933</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">11,388,763</td>
<td align="right">16,616,335</td>
<td align="right">45.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">937,353</td>
<td align="right">1,362,691</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">404,820</td>
<td align="right">586,255</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">404,820</td>
<td align="right">586,255</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">129,723,803</td>
<td align="right">186,624,207</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">43,672,971</td>
<td align="right">62,748,903</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">40,374,206</td>
<td align="right">57,746,490</td>
<td align="right">43.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">26,355,042</td>
<td align="right">37,216,139</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">37,534,608</td>
<td align="right">52,980,393</td>
<td align="right">41.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">522,112,646</td>
<td align="right">732,004,277</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">43,849,354</td>
<td align="right">60,789,904</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">416,249,027</td>
<td align="right">576,586,794</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">42,800,979</td>
<td align="right">58,988,089</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">59,859,742</td>
<td align="right">82,021,134</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">15,586,300</td>
<td align="right">21,301,691</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">8,869,000</td>
<td align="right">12,060,315</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">366,296,169</td>
<td align="right">497,371,271</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">97,760</td>
<td align="right">131,989</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">15,464,677</td>
<td align="right">20,707,571</td>
<td align="right">33.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">404,213,539</td>
<td align="right">539,497,204</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">16,297,190</td>
<td align="right">21,648,395</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">16,297,190</td>
<td align="right">21,648,395</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">35,100,256</td>
<td align="right">46,094,111</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">58,701,101</td>
<td align="right">75,878,386</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,890,894</td>
<td align="right">2,432,655</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,895,213</td>
<td align="right">2,434,658</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">14,880,621</td>
<td align="right">19,045,191</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">79,815,826</td>
<td align="right">102,054,971</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">102,400,909</td>
<td align="right">128,815,248</td>
<td align="right">25.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">45,411,816</td>
<td align="right">56,631,227</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">67,364,608</td>
<td align="right">83,262,485</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">138,006,632</td>
<td align="right">168,908,051</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,164,967</td>
<td align="right">2,632,687</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">24,566,808</td>
<td align="right">29,758,866</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">62,690,456</td>
<td align="right">75,620,981</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">14,224,432</td>
<td align="right">17,026,310</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">23,774,638</td>
<td align="right">28,301,817</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">36,725,590</td>
<td align="right">43,658,229</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">25,990,549</td>
<td align="right">30,841,581</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">9,534,944</td>
<td align="right">11,089,951</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">7,860</td>
<td align="right">9,020</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">61,870,177</td>
<td align="right">70,605,217</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">224,290,181</td>
<td align="right">255,791,664</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">1,222,572</td>
<td align="right">1,051,603</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">5,774,302</td>
<td align="right">6,579,454</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">67,300</td>
<td align="right">76,258</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">832,513</td>
<td align="right">940,824</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">77,311,915</td>
<td align="right">86,811,701</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,622,946</td>
<td align="right">10,789,021</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,622,946</td>
<td align="right">10,789,021</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">37,917,370</td>
<td align="right">42,125,933</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">1,474,387</td>
<td align="right">1,632,625</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">29,876,958</td>
<td align="right">33,042,177</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">13,395,953</td>
<td align="right">14,743,247</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">9,241,667</td>
<td align="right">10,101,347</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">20,640</td>
<td align="right">22,460</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">58,742,939</td>
<td align="right">63,921,537</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">11,920</td>
<td align="right">12,951</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">20,678</td>
<td align="right">22,460</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">989,577</td>
<td align="right">915,303</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">9,954,652</td>
<td align="right">10,681,418</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">73,409</td>
<td align="right">78,433</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">10,782,704</td>
<td align="right">11,519,345</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">10,782,704</td>
<td align="right">11,519,345</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,486,275</td>
<td align="right">1,587,452</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,796,651</td>
<td align="right">2,984,275</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">20,206,002</td>
<td align="right">21,558,141</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,881,517</td>
<td align="right">2,005,788</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">10,158,039</td>
<td align="right">10,757,538</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">396,684</td>
<td align="right">419,816</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">12,037,701</td>
<td align="right">12,736,115</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">381,694</td>
<td align="right">399,508</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">29,078,846</td>
<td align="right">27,767,947</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">10,492,661</td>
<td align="right">10,951,110</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">53,278,365</td>
<td align="right">55,543,811</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">52,228,695</td>
<td align="right">54,430,367</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,204,437</td>
<td align="right">2,296,110</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">4,298,516</td>
<td align="right">4,472,791</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">41,896,097</td>
<td align="right">43,446,863</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">20,325,151</td>
<td align="right">21,041,437</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">626,702</td>
<td align="right">644,158</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">626,702</td>
<td align="right">644,158</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,050,388</td>
<td align="right">1,021,450</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">627,416</td>
<td align="right">611,561</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">334,093,005</td>
<td align="right">329,025,293</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">25,927,002</td>
<td align="right">26,306,528</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">3,218,238</td>
<td align="right">3,253,446</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">18,087,483</td>
<td align="right">17,925,768</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">18,048</td>
<td align="right">17,892</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,740</td>
<td align="right">13,843</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">14,708,061</td>
<td align="right">14,815,821</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">4,378,364</td>
<td align="right">4,409,989</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">177,100</td>
<td align="right">178,043</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">14,538,241</td>
<td align="right">14,501,652</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">7,537,844</td>
<td align="right">7,552,263</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">49,740</td>
<td align="right">49,772</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">16,858,380</td>
<td align="right">16,867,254</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">3,150,856</td>
<td align="right">3,150,652</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">106,920</td>
<td align="right">106,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">36,780</td>
<td align="right">36,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">30,080</td>
<td align="right">30,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">8,240</td>
<td align="right">8,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">3,760</td>
<td align="right">3,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">3,140</td>
<td align="right">3,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">3,140</td>
<td align="right">3,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,240</td>
<td align="right">1,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">1,240</td>
<td align="right">1,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">17,615,993</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">5,008,351</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right"></td>
<td align="right">973,379</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right"></td>
<td align="right">973,379</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_ATTR</td>
<td align="right"></td>
<td align="right">973,378</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">265,554</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right"></td>
<td align="right">261,283</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right"></td>
<td align="right">19,743</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right"></td>
<td align="right">19,583</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right"></td>
<td align="right">2,294</td>
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
<td align="left">CALL_KW</td>
<td align="right">80</td>
<td align="right">160</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">8,982</td>
<td align="right">16,038</td>
<td align="right">78.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">14,872</td>
<td align="right">22,573</td>
<td align="right">51.8%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">643</td>
<td align="right">754</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">340</td>
<td align="right">340</td>
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
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-05
