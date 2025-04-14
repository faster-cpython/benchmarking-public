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
<td align="left">STORE_SLICE</td>
<td align="right">1,194,076</td>
<td align="right">104,225,613</td>
<td align="right">8,628.6%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,000,000</td>
<td align="right">48,901,740</td>
<td align="right">715.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">191,850,560</td>
<td align="right">1,196,884,502</td>
<td align="right">523.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">188,275,300</td>
<td align="right">1,045,096,243</td>
<td align="right">455.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">19,483,926</td>
<td align="right">85,978,494</td>
<td align="right">341.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">435,988,420</td>
<td align="right">1,855,555,436</td>
<td align="right">325.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">107,538,996</td>
<td align="right">456,293,390</td>
<td align="right">324.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">34,126,176</td>
<td align="right">142,487,824</td>
<td align="right">317.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">204,549,640</td>
<td align="right">780,843,349</td>
<td align="right">281.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">158,680,486</td>
<td align="right">505,650,721</td>
<td align="right">218.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">430,638,512</td>
<td align="right">1,343,641,975</td>
<td align="right">212.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">350,010,116</td>
<td align="right">1,059,870,646</td>
<td align="right">202.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">624,893,676</td>
<td align="right">1,704,159,296</td>
<td align="right">172.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">149,736,796</td>
<td align="right">395,934,530</td>
<td align="right">164.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">26,819,434</td>
<td align="right">69,775,459</td>
<td align="right">160.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">473,985,573</td>
<td align="right">1,230,346,029</td>
<td align="right">159.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">4,461,911</td>
<td align="right">11,220,095</td>
<td align="right">151.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">349,468,176</td>
<td align="right">853,423,190</td>
<td align="right">144.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">777,757,588</td>
<td align="right">1,878,371,284</td>
<td align="right">141.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">517,214,518</td>
<td align="right">1,194,467,675</td>
<td align="right">130.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">747,242,456</td>
<td align="right">1,690,674,998</td>
<td align="right">126.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">925,816,355</td>
<td align="right">1,958,881,844</td>
<td align="right">111.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">937,925,662</td>
<td align="right">1,927,972,987</td>
<td align="right">105.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">2,174,348,167</td>
<td align="right">4,406,679,029</td>
<td align="right">102.7%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">800</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">53,629,016</td>
<td align="right">104,456,816</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">116,937,431</td>
<td align="right">8,779,154</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,030,910</td>
<td align="right">13,044,491</td>
<td align="right">-91.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">230,065,967</td>
<td align="right">35,871,379</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,712,677</td>
<td align="right">938,434</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,950,689</td>
<td align="right">23,068,718</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">187,715,844</td>
<td align="right">43,205,919</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">91,688,009</td>
<td align="right">160,465,567</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">174,611,238</td>
<td align="right">48,559,625</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">142,051,132</td>
<td align="right">42,690,628</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">353,975,309</td>
<td align="right">596,106,798</td>
<td align="right">68.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">58,128,639</td>
<td align="right">18,585,877</td>
<td align="right">-68.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">261,267,387</td>
<td align="right">91,248,547</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">87,947,980</td>
<td align="right">34,773,225</td>
<td align="right">-60.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">112,765,159</td>
<td align="right">180,106,314</td>
<td align="right">59.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">92,497,853</td>
<td align="right">40,281,908</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">292,346,647</td>
<td align="right">130,212,484</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">325,085,550</td>
<td align="right">504,734,260</td>
<td align="right">55.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">947,267,099</td>
<td align="right">1,458,529,239</td>
<td align="right">54.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,271,955,758</td>
<td align="right">600,448,179</td>
<td align="right">-52.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">99,239,657</td>
<td align="right">148,626,160</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,031,470</td>
<td align="right">2,028,577</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,876,628,764</td>
<td align="right">2,806,669,281</td>
<td align="right">49.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,280,178</td>
<td align="right">1,154,683</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">94,412,609</td>
<td align="right">49,017,100</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,681,682</td>
<td align="right">7,175,486</td>
<td align="right">-47.6%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,558,959</td>
<td align="right">14,162,857</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,748,960</td>
<td align="right">2,020,087</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">47,878,059</td>
<td align="right">26,025,449</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">219,680,243</td>
<td align="right">119,817,767</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">480,679,802</td>
<td align="right">699,029,083</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">172,590,763</td>
<td align="right">248,887,707</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,096,849,957</td>
<td align="right">614,209,461</td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">395,528,531</td>
<td align="right">223,346,290</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">232,485,798</td>
<td align="right">131,462,562</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">917,058,621</td>
<td align="right">549,007,000</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">8,117,433</td>
<td align="right">4,866,913</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">369,496,312</td>
<td align="right">224,440,688</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">45,460,144</td>
<td align="right">27,910,147</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">29,016,747</td>
<td align="right">17,986,169</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">85,989,898</td>
<td align="right">53,704,509</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">318,288,517</td>
<td align="right">199,996,710</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">281,447,963</td>
<td align="right">180,850,019</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">194,345,250</td>
<td align="right">127,983,717</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">320,433,821</td>
<td align="right">211,719,133</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">91,319,052</td>
<td align="right">61,006,222</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">71,347,643</td>
<td align="right">47,981,726</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">122,141,956</td>
<td align="right">82,281,342</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">415,667,900</td>
<td align="right">281,527,525</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">32,307,181</td>
<td align="right">22,148,171</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">650,394,197</td>
<td align="right">852,978,149</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">931,573,556</td>
<td align="right">643,850,510</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,842,831,342</td>
<td align="right">5,016,049,659</td>
<td align="right">30.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">657,752,716</td>
<td align="right">458,875,299</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,344,669,605</td>
<td align="right">1,639,300,916</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">70,509,594</td>
<td align="right">49,337,068</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">115,171,891</td>
<td align="right">148,368,291</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,580</td>
<td align="right">552,401</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">282,795,880</td>
<td align="right">203,712,688</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">54,635,115</td>
<td align="right">40,090,097</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,503,361,138</td>
<td align="right">1,847,664,314</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">120,307,220</td>
<td align="right">89,660,721</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">61,269,011</td>
<td align="right">45,904,885</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">258,216,581</td>
<td align="right">195,907,799</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">161,690,628</td>
<td align="right">200,298,591</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,645,086,453</td>
<td align="right">2,013,862,074</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">120,321,423</td>
<td align="right">92,639,598</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,552</td>
<td align="right">65,652</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">36,036,457</td>
<td align="right">28,914,327</td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">62,541,608</td>
<td align="right">74,883,941</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">36,126,865</td>
<td align="right">29,043,897</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">17,216,952,375</td>
<td align="right">20,493,302,043</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">155,498,018</td>
<td align="right">126,110,665</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,910,948</td>
<td align="right">29,126,881</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">141,138,328</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">123,296,285</td>
<td align="right">102,492,834</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,025,818,846</td>
<td align="right">4,703,600,856</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">32,676,263</td>
<td align="right">27,379,185</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">84,598,684</td>
<td align="right">70,986,549</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">330,788,530</td>
<td align="right">278,197,059</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">865,522,870</td>
<td align="right">728,878,509</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">130,489,609</td>
<td align="right">111,674,130</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">811,519,482</td>
<td align="right">925,676,801</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,466,197,752</td>
<td align="right">5,064,343,777</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">138,358,846</td>
<td align="right">155,949,615</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,644,105,066</td>
<td align="right">1,843,866,981</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">507,471,076</td>
<td align="right">446,152,654</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">246,249,832</td>
<td align="right">217,431,572</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">163,039,078</td>
<td align="right">144,308,657</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">116,559,606</td>
<td align="right">103,390,422</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">22,259,655</td>
<td align="right">19,767,092</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,900</td>
<td align="right">269,134,372</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">36,580,028</td>
<td align="right">32,744,866</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">71,112,839</td>
<td align="right">63,926,609</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">43,128,163</td>
<td align="right">38,786,009</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">865,597,765</td>
<td align="right">782,901,790</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">316,199,936</td>
<td align="right">346,307,970</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">176,416,719</td>
<td align="right">160,070,825</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">421,021,917</td>
<td align="right">383,051,495</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">81,146,412</td>
<td align="right">73,915,949</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,350,648</td>
<td align="right">8,647,618</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">781,020</td>
<td align="right">723,460</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,941,449</td>
<td align="right">8,317,620</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,745,941</td>
<td align="right">53,883,467</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">59,727</td>
<td align="right">56,163</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">304,487,580</td>
<td align="right">287,819,469</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,810,666,615</td>
<td align="right">4,561,027,214</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">193,240,138</td>
<td align="right">202,963,159</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,303,349</td>
<td align="right">565,530,681</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">57,592,989</td>
<td align="right">54,925,009</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">680,445,481</td>
<td align="right">651,975,955</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,176,355</td>
<td align="right">64,558,995</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,094,591</td>
<td align="right">9,723,089</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,068,490</td>
<td align="right">8,792,262</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,622,139,718</td>
<td align="right">1,575,553,852</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,439,800</td>
<td align="right">1,402,732</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">3,410,281,599</td>
<td align="right">3,495,725,862</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">103,023,784</td>
<td align="right">100,448,910</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">3,182,889,218</td>
<td align="right">3,103,490,672</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">567,648,531</td>
<td align="right">581,105,855</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,713,360</td>
<td align="right">410,277,976</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,139,190</td>
<td align="right">61,365,236</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,793</td>
<td align="right">41,178,365</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">244,194,672</td>
<td align="right">240,181,236</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,712</td>
<td align="right">33,366</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">352,464,871</td>
<td align="right">348,876,496</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,254,003,841</td>
<td align="right">5,306,959,688</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,246,855</td>
<td align="right">20,044,245</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">116,602,420</td>
<td align="right">117,556,709</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,770</td>
<td align="right">56,322</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,232,234,050</td>
<td align="right">2,217,255,313</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,158</td>
<td align="right">56,798</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">133,112</td>
<td align="right">132,417</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,141</td>
<td align="right">5,165</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">198,455,547</td>
<td align="right">197,562,868</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">173,813,466</td>
<td align="right">174,357,561</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">207,639</td>
<td align="right">207,079</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,512,066</td>
<td align="right">180,214,671</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,965,774</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">405,635</td>
<td align="right">405,179</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,708</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,217</td>
<td align="right">14,758,864</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">19,916,372</td>
<td align="right">19,916,151</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,246,876</td>
<td align="right">20,246,655</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">5,999,940</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,048,535</td>
<td align="right">3,048,552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,920</td>
<td align="right">1,645,923</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,197,377</td>
<td align="right">5,197,384</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,792</td>
<td align="right">5,803,798</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,678</td>
<td align="right">128,851,678</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
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
<td align="left">NOT_TAKEN</td>
<td align="right">17,132,175</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,488,296</td>
<td align="right">3,488,296</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,859</td>
<td align="right">120,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,734</td>
<td align="right">98,734</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,546</td>
<td align="right">17,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,321</td>
<td align="right">5,321</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,897</td>
<td align="right">3,897</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,621</td>
<td align="right">3,621</td>
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
<td align="right">151</td>
<td align="right">151</td>
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
<td align="right">925,468,709</td>
<td align="right">6.6%</td>
<td align="right">1,958,243,349</td>
<td align="right">13.2%</td>
<td align="right">111.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,648,080</td>
<td align="right">0.4%</td>
<td align="right">57,128,093</td>
<td align="right">0.4%</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,123,215,394</td>
<td align="right">93.1%</td>
<td align="right">12,807,081,673</td>
<td align="right">86.4%</td>
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
<td align="left">Failure</td>
<td align="right">329,812</td>
<td align="right">25.7%</td>
<td align="right">620,938</td>
<td align="right">36.2%</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">954,356</td>
<td align="right">74.3%</td>
<td align="right">1,095,179</td>
<td align="right">63.8%</td>
<td align="right">14.8%</td>
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
<td align="right">7,532</td>
<td align="right">2.3%</td>
<td align="right">190,764</td>
<td align="right">30.7%</td>
<td align="right">2,432.7%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,767</td>
<td align="right">0.8%</td>
<td align="right">11,145</td>
<td align="right">1.8%</td>
<td align="right">302.8%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,463</td>
<td align="right">5.6%</td>
<td align="right">64,799</td>
<td align="right">10.4%</td>
<td align="right">251.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">8,372</td>
<td align="right">2.5%</td>
<td align="right">14,453</td>
<td align="right">2.3%</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">7,440</td>
<td align="right">2.3%</td>
<td align="right">11,959</td>
<td align="right">1.9%</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,174</td>
<td align="right">1.0%</td>
<td align="right">1,279</td>
<td align="right">0.2%</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">100,738</td>
<td align="right">30.5%</td>
<td align="right">160,142</td>
<td align="right">25.8%</td>
<td align="right">59.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">17,893</td>
<td align="right">5.4%</td>
<td align="right">27,862</td>
<td align="right">4.5%</td>
<td align="right">55.7%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">12,446</td>
<td align="right">3.8%</td>
<td align="right">6,564</td>
<td align="right">1.1%</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21,614</td>
<td align="right">6.6%</td>
<td align="right">13,788</td>
<td align="right">2.2%</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">34,751</td>
<td align="right">10.5%</td>
<td align="right">23,565</td>
<td align="right">3.8%</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">17,023</td>
<td align="right">5.2%</td>
<td align="right">22,243</td>
<td align="right">3.6%</td>
<td align="right">30.7%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,752</td>
<td align="right">1.7%</td>
<td align="right">4,930</td>
<td align="right">0.8%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,469</td>
<td align="right">7.1%</td>
<td align="right">20,306</td>
<td align="right">3.3%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.4%</td>
<td align="right">1,219</td>
<td align="right">0.2%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">189</td>
<td align="right">0.1%</td>
<td align="right">168</td>
<td align="right">0.0%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">3,607</td>
<td align="right">1.1%</td>
<td align="right">3,265</td>
<td align="right">0.5%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.3%</td>
<td align="right">771</td>
<td align="right">0.1%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">0.6%</td>
<td align="right">1,935</td>
<td align="right">0.3%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">6,193</td>
<td align="right">1.9%</td>
<td align="right">6,011</td>
<td align="right">1.0%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">627</td>
<td align="right">0.2%</td>
<td align="right">610</td>
<td align="right">0.1%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">29,940</td>
<td align="right">9.1%</td>
<td align="right">29,547</td>
<td align="right">4.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">0.7%</td>
<td align="right">2,350</td>
<td align="right">0.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">597</td>
<td align="right">0.2%</td>
<td align="right">597</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">491</td>
<td align="right">0.1%</td>
<td align="right">491</td>
<td align="right">0.1%</td>
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
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">72</td>
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
<td align="right">120,321,423</td>
<td align="right">100.0%</td>
<td align="right">92,639,598</td>
<td align="right">100.0%</td>
<td align="right">-23.0%</td>
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
<td align="right">135,498,014</td>
<td align="right">1.2%</td>
<td align="right">111,315,412</td>
<td align="right">1.0%</td>
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
<td align="right">133,172,545</td>
<td align="right">1.2%</td>
<td align="right">109,446,251</td>
<td align="right">1.0%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,094,100,104</td>
<td align="right">98.8%</td>
<td align="right">10,787,376,662</td>
<td align="right">99.0%</td>
<td align="right">-2.8%</td>
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
<td align="right">2,730,658</td>
<td align="right">100.0%</td>
<td align="right">2,273,894</td>
<td align="right">100.0%</td>
<td align="right">-16.7%</td>
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
<td align="right">287</td>
<td align="right">64.3%</td>
<td align="right">287</td>
<td align="right">64.3%</td>
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
<td align="right">583,846</td>
<td align="right">82.8%</td>
<td align="right">585,746</td>
<td align="right">82.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">684,422</td>
<td align="right">97.1%</td>
<td align="right">686,284</td>
<td align="right">97.1%</td>
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
<td align="right">20,163</td>
<td align="right">99.4%</td>
<td align="right">20,201</td>
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
<td align="right">107,417,266</td>
<td align="right">2.3%</td>
<td align="right">456,098,002</td>
<td align="right">9.4%</td>
<td align="right">324.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,157,757</td>
<td align="right">0.0%</td>
<td align="right">929,339</td>
<td align="right">0.0%</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,514,683,769</td>
<td align="right">97.6%</td>
<td align="right">4,384,708,981</td>
<td align="right">90.6%</td>
<td align="right">-2.9%</td>
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
<td align="right">103,508</td>
<td align="right">72.2%</td>
<td align="right">177,283</td>
<td align="right">83.3%</td>
<td align="right">71.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39,868</td>
<td align="right">27.8%</td>
<td align="right">35,445</td>
<td align="right">16.7%</td>
<td align="right">-11.1%</td>
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
<td align="right">4,563</td>
<td align="right">4.4%</td>
<td align="right">89,973</td>
<td align="right">50.8%</td>
<td align="right">1,871.8%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.4%</td>
<td align="right">1,887</td>
<td align="right">1.1%</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">799</td>
<td align="right">0.8%</td>
<td align="right">320</td>
<td align="right">0.2%</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,549</td>
<td align="right">6.3%</td>
<td align="right">10,397</td>
<td align="right">5.9%</td>
<td align="right">58.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,321</td>
<td align="right">1.3%</td>
<td align="right">581</td>
<td align="right">0.3%</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,149</td>
<td align="right">22.4%</td>
<td align="right">17,794</td>
<td align="right">10.0%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">984</td>
<td align="right">1.0%</td>
<td align="right">805</td>
<td align="right">0.5%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">11,591</td>
<td align="right">11.2%</td>
<td align="right">9,767</td>
<td align="right">5.5%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,697</td>
<td align="right">7.4%</td>
<td align="right">7,234</td>
<td align="right">4.1%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">36,864</td>
<td align="right">35.6%</td>
<td align="right">36,199</td>
<td align="right">20.4%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">2,018</td>
<td align="right">1.9%</td>
<td align="right">1,992</td>
<td align="right">1.1%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">334</td>
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
<td align="right">62,502,601</td>
<td align="right">2.8%</td>
<td align="right">74,842,532</td>
<td align="right">3.4%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,189,778,058</td>
<td align="right">97.1%</td>
<td align="right">2,153,992,844</td>
<td align="right">96.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
<td align="right">1,916,987</td>
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
<td align="right">36,746</td>
<td align="right">48.9%</td>
<td align="right">39,148</td>
<td align="right">50.5%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,435</td>
<td align="right">51.1%</td>
<td align="right">38,435</td>
<td align="right">49.5%</td>
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
<td align="right">9,827</td>
<td align="right">26.7%</td>
<td align="right">14,846</td>
<td align="right">37.9%</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,092</td>
<td align="right">27.5%</td>
<td align="right">7,676</td>
<td align="right">19.6%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,135</td>
<td align="right">30.3%</td>
<td align="right">10,935</td>
<td align="right">27.9%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,692</td>
<td align="right">15.5%</td>
<td align="right">5,691</td>
<td align="right">14.5%</td>
<td align="right">-0.0%</td>
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
<td align="right">204,430,278</td>
<td align="right">18.6%</td>
<td align="right">780,589,898</td>
<td align="right">36.5%</td>
<td align="right">281.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">838,528,493</td>
<td align="right">76.3%</td>
<td align="right">1,317,771,611</td>
<td align="right">61.6%</td>
<td align="right">57.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">55,647,545</td>
<td align="right">5.1%</td>
<td align="right">40,396,027</td>
<td align="right">1.9%</td>
<td align="right">-27.4%</td>
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
<td align="right">114,310</td>
<td align="right">9.8%</td>
<td align="right">248,269</td>
<td align="right">24.4%</td>
<td align="right">117.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,054,863</td>
<td align="right">90.2%</td>
<td align="right">767,173</td>
<td align="right">75.6%</td>
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
<td align="left">zip</td>
<td align="right">4,537</td>
<td align="right">4.0%</td>
<td align="right">167,965</td>
<td align="right">67.7%</td>
<td align="right">3,602.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">73</td>
<td align="right">0.0%</td>
<td align="right">-77.7%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">8,503</td>
<td align="right">7.4%</td>
<td align="right">2,019</td>
<td align="right">0.8%</td>
<td align="right">-76.3%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">7,086</td>
<td align="right">6.2%</td>
<td align="right">2,679</td>
<td align="right">1.1%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">16,541</td>
<td align="right">14.5%</td>
<td align="right">6,593</td>
<td align="right">2.7%</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">254</td>
<td align="right">0.2%</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,866</td>
<td align="right">4.3%</td>
<td align="right">2,961</td>
<td align="right">1.2%</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">91</td>
<td align="right">0.0%</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,902</td>
<td align="right">10.4%</td>
<td align="right">9,273</td>
<td align="right">3.7%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,440</td>
<td align="right">1.3%</td>
<td align="right">1,207</td>
<td align="right">0.5%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,597</td>
<td align="right">2.3%</td>
<td align="right">2,880</td>
<td align="right">1.2%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">51,854</td>
<td align="right">45.4%</td>
<td align="right">48,268</td>
<td align="right">19.4%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,465</td>
<td align="right">1.3%</td>
<td align="right">1,402</td>
<td align="right">0.6%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,804</td>
<td align="right">2.5%</td>
<td align="right">2,724</td>
<td align="right">1.1%</td>
<td align="right">-2.9%</td>
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
<td align="right">12,059,582,707</td>
<td align="right">89.9%</td>
<td align="right">11,634,735,931</td>
<td align="right">89.6%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">565,889,124</td>
<td align="right">4.2%</td>
<td align="right">579,501,862</td>
<td align="right">4.5%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">786,073,006</td>
<td align="right">5.9%</td>
<td align="right">774,226,356</td>
<td align="right">6.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,378,740</td>
<td align="right">0.0%</td>
<td align="right">1,378,740</td>
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
<td align="right">489,713</td>
<td align="right">3.2%</td>
<td align="right">372,876</td>
<td align="right">2.5%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">14,917,391</td>
<td align="right">96.8%</td>
<td align="right">14,691,895</td>
<td align="right">97.5%</td>
<td align="right">-1.5%</td>
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
<td align="right">44,048</td>
<td align="right">9.0%</td>
<td align="right">56,363</td>
<td align="right">15.1%</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,775</td>
<td align="right">0.4%</td>
<td align="right">1,440</td>
<td align="right">0.4%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">820</td>
<td align="right">0.2%</td>
<td align="right">750</td>
<td align="right">0.2%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,942</td>
<td align="right">1.0%</td>
<td align="right">4,584</td>
<td align="right">1.2%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">42,172</td>
<td align="right">8.6%</td>
<td align="right">39,220</td>
<td align="right">10.5%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">15,638</td>
<td align="right">3.2%</td>
<td align="right">14,645</td>
<td align="right">3.9%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.2%</td>
<td align="right">1,032</td>
<td align="right">0.3%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23,192</td>
<td align="right">4.7%</td>
<td align="right">22,163</td>
<td align="right">5.9%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,938</td>
<td align="right">1.6%</td>
<td align="right">7,632</td>
<td align="right">2.0%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,369</td>
<td align="right">0.5%</td>
<td align="right">2,299</td>
<td align="right">0.6%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,086</td>
<td align="right">1.0%</td>
<td align="right">4,946</td>
<td align="right">1.3%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60,447</td>
<td align="right">12.3%</td>
<td align="right">60,737</td>
<td align="right">16.3%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,583</td>
<td align="right">0.3%</td>
<td align="right">1,582</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.3%</td>
<td align="right">6,405</td>
<td align="right">1.7%</td>
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
<td align="right">0.1%</td>
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
<td align="right">4,606,052,696</td>
<td align="right">99.7%</td>
<td align="right">8,870,763,025</td>
<td align="right">99.8%</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,557</td>
<td align="right">0.0%</td>
<td align="right">48,495</td>
<td align="right">0.0%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,686</td>
<td align="right">0.3%</td>
<td align="right">14,622,768</td>
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
<td align="right">1,508</td>
<td align="right">0.0%</td>
<td align="right">1,508</td>
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
<td align="right">138,298</td>
<td align="right">100.0%</td>
<td align="right">136,803</td>
<td align="right">100.0%</td>
<td align="right">-1.1%</td>
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
<td align="right">63,563,956</td>
<td align="right">100.0%</td>
<td align="right">64,459,008</td>
<td align="right">100.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">253</td>
<td align="right">0.0%</td>
<td align="right">254</td>
<td align="right">0.0%</td>
<td align="right">0.4%</td>
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
<td align="right">2,455</td>
<td align="right">100.0%</td>
<td align="right">2,455</td>
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
<td align="right">593,288,638</td>
<td align="right">82.2%</td>
<td align="right">593,288,662</td>
<td align="right">82.2%</td>
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
<td align="right">128,816,907</td>
<td align="right">17.8%</td>
<td align="right">128,816,907</td>
<td align="right">17.8%</td>
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
<td align="right">651</td>
<td align="right">1.9%</td>
<td align="right">651</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,392</td>
<td align="right">98.1%</td>
<td align="right">34,392</td>
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
<td align="right">71.1%</td>
<td align="right">24,440</td>
<td align="right">71.1%</td>
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
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">732</td>
<td align="right">2.1%</td>
<td align="right">732</td>
<td align="right">2.1%</td>
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
<td align="right">70,416,254</td>
<td align="right">3.5%</td>
<td align="right">49,249,575</td>
<td align="right">2.8%</td>
<td align="right">-30.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,845,405,938</td>
<td align="right">90.9%</td>
<td align="right">1,615,872,592</td>
<td align="right">90.8%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">114,447,998</td>
<td align="right">5.6%</td>
<td align="right">113,587,016</td>
<td align="right">6.4%</td>
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
<td align="left">Failure</td>
<td align="right">51,183</td>
<td align="right">2.3%</td>
<td align="right">45,379</td>
<td align="right">2.0%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,200,863</td>
<td align="right">97.7%</td>
<td align="right">2,184,590</td>
<td align="right">98.0%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">4,913</td>
<td align="right">9.6%</td>
<td align="right">1,810</td>
<td align="right">4.0%</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,318</td>
<td align="right">10.4%</td>
<td align="right">2,658</td>
<td align="right">5.9%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">261,768</td>
<td align="right">511.4%</td>
<td align="right">138,594</td>
<td align="right">305.4%</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">741</td>
<td align="right">1.4%</td>
<td align="right">699</td>
<td align="right">1.5%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">15.0%</td>
<td align="right">7,421</td>
<td align="right">16.4%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,076</td>
<td align="right">47.0%</td>
<td align="right">24,316</td>
<td align="right">53.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,342</td>
<td align="right">6.5%</td>
<td align="right">3,352</td>
<td align="right">7.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.2%</td>
<td align="right">1,617</td>
<td align="right">3.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">810</td>
<td align="right">1.6%</td>
<td align="right">810</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">730</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">361</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.2%</td>
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
<td align="right">1,194,076</td>
<td align="right">100.0%</td>
<td align="right">104,225,613</td>
<td align="right">100.0%</td>
<td align="right">8,628.6%</td>
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
<td align="right">149,686,888</td>
<td align="right">14.0%</td>
<td align="right">395,827,048</td>
<td align="right">30.7%</td>
<td align="right">164.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">920,075,322</td>
<td align="right">86.0%</td>
<td align="right">892,663,263</td>
<td align="right">69.3%</td>
<td align="right">-3.0%</td>
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
<td align="right">47,749</td>
<td align="right">95.6%</td>
<td align="right">105,326</td>
<td align="right">98.0%</td>
<td align="right">120.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,199</td>
<td align="right">4.4%</td>
<td align="right">2,196</td>
<td align="right">2.0%</td>
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
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.7%</td>
<td align="right">86,613</td>
<td align="right">82.2%</td>
<td align="right">25,299.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">15,163</td>
<td align="right">31.8%</td>
<td align="right">3,163</td>
<td align="right">3.0%</td>
<td align="right">-79.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">36.3%</td>
<td align="right">5,951</td>
<td align="right">5.7%</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">11,272</td>
<td align="right">23.6%</td>
<td align="right">5,948</td>
<td align="right">5.6%</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">176</td>
<td align="right">0.4%</td>
<td align="right">175</td>
<td align="right">0.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,905</td>
<td align="right">6.1%</td>
<td align="right">2,907</td>
<td align="right">2.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">501</td>
<td align="right">1.0%</td>
<td align="right">501</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.1%</td>
<td align="right">68</td>
<td align="right">0.1%</td>
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
<td align="right">63,034,533</td>
<td align="right">1.3%</td>
<td align="right">66,402,466</td>
<td align="right">1.4%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,520,828,318</td>
<td align="right">96.2%</td>
<td align="right">4,600,905,319</td>
<td align="right">96.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">116,139,233</td>
<td align="right">2.5%</td>
<td align="right">117,084,272</td>
<td align="right">2.4%</td>
<td align="right">0.8%</td>
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
<td align="right">1,237,972</td>
<td align="right">75.0%</td>
<td align="right">1,301,441</td>
<td align="right">75.5%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">413,084</td>
<td align="right">25.0%</td>
<td align="right">422,478</td>
<td align="right">24.5%</td>
<td align="right">2.3%</td>
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
<td align="right">8,880</td>
<td align="right">2.1%</td>
<td align="right">40,298</td>
<td align="right">9.5%</td>
<td align="right">353.8%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,977</td>
<td align="right">1.2%</td>
<td align="right">13,957</td>
<td align="right">3.3%</td>
<td align="right">180.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">15,610</td>
<td align="right">3.8%</td>
<td align="right">10,306</td>
<td align="right">2.4%</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">95,884</td>
<td align="right">23.2%</td>
<td align="right">73,263</td>
<td align="right">17.3%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,674</td>
<td align="right">2.8%</td>
<td align="right">9,415</td>
<td align="right">2.2%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">5,649</td>
<td align="right">1.4%</td>
<td align="right">4,634</td>
<td align="right">1.1%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,538</td>
<td align="right">3.0%</td>
<td align="right">12,063</td>
<td align="right">2.9%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">255,986</td>
<td align="right">62.0%</td>
<td align="right">256,656</td>
<td align="right">60.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,239,238,875</td>
<td align="right">99.9%</td>
<td align="right">1,191,718,753</td>
<td align="right">99.9%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,427,419</td>
<td align="right">0.1%</td>
<td align="right">1,390,403</td>
<td align="right">0.1%</td>
<td align="right">-2.6%</td>
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
<td align="right">858</td>
<td align="right">6.9%</td>
<td align="right">841</td>
<td align="right">6.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,603</td>
<td align="right">93.1%</td>
<td align="right">11,568</td>
<td align="right">93.2%</td>
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
<td align="left">sequence</td>
<td align="right">631</td>
<td align="right">73.5%</td>
<td align="right">614</td>
<td align="right">73.0%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.9%</td>
<td align="right">136</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">10.6%</td>
<td align="right">91</td>
<td align="right">10.8%</td>
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
<td align="right">2,472,040,336</td>
<td align="right">2.6%</td>
<td align="right">4,757,243,918</td>
<td align="right">4.2%</td>
<td align="right">92.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">38,846,325,263</td>
<td align="right">40.1%</td>
<td align="right">47,173,278,424</td>
<td align="right">41.4%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">54,351,368,814</td>
<td align="right">56.1%</td>
<td align="right">60,723,937,703</td>
<td align="right">53.4%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,208,212,318</td>
<td align="right">1.2%</td>
<td align="right">1,166,721,176</td>
<td align="right">1.0%</td>
<td align="right">-3.4%</td>
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
<td align="right">107,417,266</td>
<td align="right">4.1%</td>
<td align="right">456,098,002</td>
<td align="right">9.4%</td>
<td align="right">324.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">204,430,278</td>
<td align="right">7.9%</td>
<td align="right">780,589,898</td>
<td align="right">16.1%</td>
<td align="right">281.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">149,686,888</td>
<td align="right">5.8%</td>
<td align="right">395,827,048</td>
<td align="right">8.1%</td>
<td align="right">164.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">925,468,709</td>
<td align="right">35.6%</td>
<td align="right">1,958,243,349</td>
<td align="right">40.3%</td>
<td align="right">111.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">120,321,423</td>
<td align="right">4.6%</td>
<td align="right">92,639,598</td>
<td align="right">1.9%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">133,172,545</td>
<td align="right">5.1%</td>
<td align="right">109,446,251</td>
<td align="right">2.3%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">565,889,124</td>
<td align="right">21.7%</td>
<td align="right">579,501,862</td>
<td align="right">11.9%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">116,139,233</td>
<td align="right">4.5%</td>
<td align="right">117,084,272</td>
<td align="right">2.4%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,907</td>
<td align="right">5.0%</td>
<td align="right">128,816,907</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">70,416,254</td>
<td align="right">2.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">104,225,613</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">66,736,237</td>
<td align="right">5.5%</td>
<td align="right">55,077,682</td>
<td align="right">4.7%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">80,613,002</td>
<td align="right">6.7%</td>
<td align="right">68,934,137</td>
<td align="right">5.9%</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">27,018,938</td>
<td align="right">2.2%</td>
<td align="right">29,906,525</td>
<td align="right">2.6%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">29,429,647</td>
<td align="right">2.4%</td>
<td align="right">31,747,273</td>
<td align="right">2.7%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">242,350,249</td>
<td align="right">20.1%</td>
<td align="right">230,338,159</td>
<td align="right">19.7%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">326,667,824</td>
<td align="right">27.0%</td>
<td align="right">341,688,234</td>
<td align="right">29.3%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">81,196,981</td>
<td align="right">6.7%</td>
<td align="right">83,106,040</td>
<td align="right">7.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">92,813,303</td>
<td align="right">7.7%</td>
<td align="right">92,615,433</td>
<td align="right">7.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">27,791,850</td>
<td align="right">2.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">27,777,825</td>
<td align="right">2.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">25,065,368</td>
<td align="right">2.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20,994,348</td>
<td align="right">1.8%</td>
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
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">3,558,377</td>
<td align="right">0.1%</td>
<td align="right">2,127,887</td>
<td align="right">0.0%</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,404,916</td>
<td align="right">3.9%</td>
<td align="right">226,581,692</td>
<td align="right">3.5%</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">951,943,158</td>
<td align="right">14.2%</td>
<td align="right">909,570,038</td>
<td align="right">13.9%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">948,380,884</td>
<td align="right">14.1%</td>
<td align="right">907,438,254</td>
<td align="right">13.9%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,462,751,852</td>
<td align="right">81.3%</td>
<td align="right">5,295,713,700</td>
<td align="right">81.1%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,626,632,102</td>
<td align="right">24.2%</td>
<td align="right">1,580,046,179</td>
<td align="right">24.2%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,626,632,102</td>
<td align="right">24.2%</td>
<td align="right">1,580,046,179</td>
<td align="right">24.2%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,089,950,138</td>
<td align="right">75.8%</td>
<td align="right">4,952,402,111</td>
<td align="right">75.8%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">674,688,944</td>
<td align="right">10.0%</td>
<td align="right">670,476,141</td>
<td align="right">10.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,224,966</td>
<td align="right">4.2%</td>
<td align="right">278,998,674</td>
<td align="right">4.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,325</td>
<td align="right">0.4%</td>
<td align="right">24,922,006</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">70,792,475</td>
<td align="right">1.1%</td>
<td align="right">70,791,859</td>
<td align="right">1.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,897</td>
<td align="right">0.0%</td>
<td align="right">3,897</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,139</td>
<td align="right">2.0%</td>
<td align="right">132,513,139</td>
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
<td align="left">Interpreter immortal decrefs</td>
<td align="right">19,352,739,527</td>
<td align="right">9.8%</td>
<td align="right">26,981,104,129</td>
<td align="right">13.9%</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,443,661</td>
<td align="right">0.4%</td>
<td align="right">44,353,015</td>
<td align="right">0.2%</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">11,507,168,797</td>
<td align="right">7.3%</td>
<td align="right">14,814,744,541</td>
<td align="right">9.6%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">42,386,365,195</td>
<td align="right">26.8%</td>
<td align="right">51,740,539,108</td>
<td align="right">33.4%</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">51,918,339,354</td>
<td align="right">26.2%</td>
<td align="right">62,263,730,768</td>
<td align="right">32.2%</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">178,761,327</td>
<td align="right"></td>
<td align="right">143,398,217</td>
<td align="right"></td>
<td align="right">-19.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">68,181,930,440</td>
<td align="right">43.1%</td>
<td align="right">55,356,451,135</td>
<td align="right">35.7%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">75,688,771,227</td>
<td align="right">38.2%</td>
<td align="right">61,631,113,247</td>
<td align="right">31.9%</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">51,084,464,336</td>
<td align="right">25.8%</td>
<td align="right">42,627,356,182</td>
<td align="right">22.0%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">36,094,440,195</td>
<td align="right">22.8%</td>
<td align="right">33,063,159,036</td>
<td align="right">21.3%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,900,566</td>
<td align="right"></td>
<td align="right">7,459,016</td>
<td align="right"></td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,419,169</td>
<td align="right">0.0%</td>
<td align="right">6,858,199</td>
<td align="right">0.0%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,251,722,664</td>
<td align="right"></td>
<td align="right">2,121,877,848</td>
<td align="right"></td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,900,267,960</td>
<td align="right"></td>
<td align="right">2,814,847,930</td>
<td align="right"></td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,675,724,903</td>
<td align="right"></td>
<td align="right">6,508,740,030</td>
<td align="right"></td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,085,610,714</td>
<td align="right">32.9%</td>
<td align="right">5,945,429,663</td>
<td align="right">32.7%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,007,747,884</td>
<td align="right">32.5%</td>
<td align="right">5,894,218,449</td>
<td align="right">32.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,401,164,891</td>
<td align="right"></td>
<td align="right">12,220,150,538</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,401,081,310</td>
<td align="right">67.1%</td>
<td align="right">12,220,072,442</td>
<td align="right">67.3%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">63,070,400</td>
<td align="right"></td>
<td align="right">62,645,588</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">69,163,238</td>
<td align="right"></td>
<td align="right">69,304,048</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,172</td>
<td align="right">2.5%</td>
<td align="right">4,443,812</td>
<td align="right">3.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">434,416</td>
<td align="right">0.2%</td>
<td align="right">434,416</td>
<td align="right">0.3%</td>
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
<td align="right">364,449</td>
<td align="right">102,479,993</td>
<td align="right">9,526,079,238</td>
<td align="right">750,430,753</td>
<td align="right">763,884,389</td>
<td align="right">357,736</td>
<td align="right">94,417,974</td>
<td align="right">9,340,368,303</td>
<td align="right">744,857,261</td>
<td align="right">744,013,283</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,612,641,916</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,612,641,388</td>
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
<td align="right">40,198</td>
<td align="right">9.1%</td>
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
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">216,987</td>
<td align="right">49.3%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">257,308</td>
<td align="right">58.4%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">879</td>
<td align="right">0.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,258</td>
<td align="right">0.7%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">673</td>
<td align="right">0.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">142,846</td>
<td align="right">32.4%</td>
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
<td align="right">280</td>
<td align="right">0.7%</td>
<td align="right">60</td>
<td align="right">60 / 0 !!</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">4,854,068,652</td>
<td align="right"></td>
<td align="right">3,491,979,354</td>
<td align="right"></td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">440,572</td>
<td align="right"></td>
<td align="right">412,188</td>
<td align="right"></td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">231,677,978,421</td>
<td align="right">4,772.9%</td>
<td align="right">241,585,044,586</td>
<td align="right">6,918.3%</td>
<td align="right">4.3%</td>
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
<td align="right">40,198</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">35,304</td>
<td align="right">87.8%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>

### JIT memory stats

<details>
<summary> JIT memory stats </summary>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Base Size (bytes)</th>
<th align="right">Base Ratio</th>
<th align="right">Head Size (bytes)</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">49,852,864</td>
<td align="right">12.2%</td>
<td align="right">203,012,224</td>
<td align="right">18.6%</td>
<td align="right">307.2%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">317,161,472</td>
<td align="right">77.4%</td>
<td align="right">1,085,374,464</td>
<td align="right">99.4%</td>
<td align="right">242.2%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">285,984,627</td>
<td align="right">69.8%</td>
<td align="right">828,819,371</td>
<td align="right">75.9%</td>
<td align="right">189.8%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">409,583,616</td>
<td align="right"></td>
<td align="right">1,092,247,552</td>
<td align="right"></td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">73,746,125</td>
<td align="right">18.0%</td>
<td align="right">60,415,957</td>
<td align="right">5.5%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">
Trampoline size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the trampolines of the JIT traces
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


</details>

### JIT trace total memory histogram

<details>
<summary> JIT trace total memory histogram </summary>

<table>
<thead>
<tr>
<th align="left">Size (bytes)</th>
<th align="left">Base Count</th>
<th align="right">Base Ratio</th>
<th align="left">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 4,096</td>
<td align="left">9,344</td>
<td align="right">26.5%</td>
<td align="left"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">11,446</td>
<td align="right">32.4%</td>
<td align="left">1,499</td>
<td align="right">5.1%</td>
<td align="right">-86.9%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">10,274</td>
<td align="right">29.1%</td>
<td align="left">8,968</td>
<td align="right">30.4%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">2,802</td>
<td align="right">7.9%</td>
<td align="left">8,533</td>
<td align="right">28.9%</td>
<td align="right">204.5%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,150</td>
<td align="right">3.3%</td>
<td align="left">7,312</td>
<td align="right">24.8%</td>
<td align="right">535.8%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">288</td>
<td align="right">0.8%</td>
<td align="left">2,321</td>
<td align="right">7.9%</td>
<td align="right">705.9%</td>
</tr>
<tr>
<td align="left"><= 262,144</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">746</td>
<td align="right">2.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 524,288</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">61</td>
<td align="right">0.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 1,048,576</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">42</td>
<td align="right">0.1%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

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
<td align="left"><= 8</td>
<td align="right">3,555</td>
<td align="right">8.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">3,372</td>
<td align="right">8.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">11,975</td>
<td align="right">29.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">10,548</td>
<td align="right">26.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">5,990</td>
<td align="right">14.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,015</td>
<td align="right">10.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">661</td>
<td align="right">1.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">82</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left"><= 4</td>
<td align="right">1,559</td>
<td align="right">3.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,907</td>
<td align="right">7.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">5,911</td>
<td align="right">14.7%</td>
<td align="right">39</td>
<td align="right">39 / 0 !!</td>
<td align="right">-99.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">12,392</td>
<td align="right">30.8%</td>
<td align="right">1,354</td>
<td align="right">1,354 / 0 !!</td>
<td align="right">-89.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">8,642</td>
<td align="right">21.5%</td>
<td align="right">14,485</td>
<td align="right">14,485 / 0 !!</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,664</td>
<td align="right">6.6%</td>
<td align="right">11,140</td>
<td align="right">11,140 / 0 !!</td>
<td align="right">318.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">981</td>
<td align="right">2.4%</td>
<td align="right">2,442</td>
<td align="right">2,442 / 0 !!</td>
<td align="right">148.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">248</td>
<td align="right">0.6%</td>
<td align="right">22</td>
<td align="right">22 / 0 !!</td>
<td align="right">-91.1%</td>
</tr>
</tbody>
</table>


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>


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
<td align="left">_CHECK_PEP_523</td>
<td align="right">356,340</td>
<td align="right">1,504,980,011</td>
<td align="right">422,243.8%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">263</td>
<td align="right">1,010,539</td>
<td align="right">384,135.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">1,760</td>
<td align="right">3,945,651</td>
<td align="right">224,084.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">5,450,164</td>
<td align="right">5,558,683,571</td>
<td align="right">101,891.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">11,174,708</td>
<td align="right">2,846,271,851</td>
<td align="right">25,370.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">11,174,708</td>
<td align="right">2,846,271,851</td>
<td align="right">25,370.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">13,877,988</td>
<td align="right">2,846,271,851</td>
<td align="right">20,409.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">566,592</td>
<td align="right">103,392,544</td>
<td align="right">18,148.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">566,592</td>
<td align="right">103,392,544</td>
<td align="right">18,148.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">16,144,809</td>
<td align="right">675,984,841</td>
<td align="right">4,087.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">27,762</td>
<td align="right">893,249</td>
<td align="right">3,117.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">7,980,918</td>
<td align="right">148,958,516</td>
<td align="right">1,766.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">6,957,856</td>
<td align="right">1,689.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">55,062,147</td>
<td align="right">971,182,362</td>
<td align="right">1,663.8%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">73,215,328</td>
<td align="right">1,207,133,114</td>
<td align="right">1,548.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">73,215,328</td>
<td align="right">1,204,008,314</td>
<td align="right">1,544.5%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,545,553</td>
<td align="right">24,911,498</td>
<td align="right">1,511.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">275,320</td>
<td align="right">2,892,387</td>
<td align="right">950.6%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">21,253,261</td>
<td align="right">193,308,627</td>
<td align="right">809.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">6,605,576</td>
<td align="right">57,390,793</td>
<td align="right">768.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,186,608</td>
<td align="right">8,867,742</td>
<td align="right">647.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">1,338,342</td>
<td align="right">8,960,843</td>
<td align="right">569.5%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">10,891,331</td>
<td align="right">64,069,396</td>
<td align="right">488.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">573,701,307</td>
<td align="right">2,680,914,665</td>
<td align="right">367.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,137,792</td>
<td align="right">26,850,316</td>
<td align="right">337.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">23,254,117</td>
<td align="right">101,682,139</td>
<td align="right">337.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">15,894,916</td>
<td align="right">66,863,683</td>
<td align="right">320.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">39,173,597</td>
<td align="right">142,657,113</td>
<td align="right">264.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,150,628</td>
<td align="right">19,287,244</td>
<td align="right">213.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">21,292,955</td>
<td align="right">66,688,056</td>
<td align="right">213.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">508,414,651</td>
<td align="right">1,445,835,314</td>
<td align="right">184.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">11,776,201</td>
<td align="right">29,664,220</td>
<td align="right">151.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">9,869,751</td>
<td align="right">22,706,941</td>
<td align="right">130.1%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">2,976,000</td>
<td align="right">6,844,800</td>
<td align="right">130.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">2,976,000</td>
<td align="right">6,844,800</td>
<td align="right">130.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">10,633,784</td>
<td align="right">23,472,834</td>
<td align="right">120.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">720,874,069</td>
<td align="right">1,493,801,321</td>
<td align="right">107.2%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">103,178,820</td>
<td align="right">1,980</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">70,350,323</td>
<td align="right">3,009,143</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,952,369,467</td>
<td align="right">5,778,420,162</td>
<td align="right">95.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">403,932,812</td>
<td align="right">790,261,023</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">21,694,360</td>
<td align="right">42,427,370</td>
<td align="right">95.6%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">70,350,323</td>
<td align="right">4,018,258</td>
<td align="right">-94.3%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">8,460,881</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">15,704,991</td>
<td align="right">30,194,266</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">6,607,739</td>
<td align="right">581,872</td>
<td align="right">-91.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">165,192,785</td>
<td align="right">14,944,248</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">119,607,213</td>
<td align="right">11,342,173</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,131,360</td>
<td align="right">5,174,450</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">48,131,360</td>
<td align="right">5,174,450</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">376,231</td>
<td align="right">45,220</td>
<td align="right">-88.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">179,939,392</td>
<td align="right">335,894,306</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,086,432,510</td>
<td align="right">159,200,158</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">409,570,121</td>
<td align="right">61,046,993</td>
<td align="right">-85.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,210,031,034</td>
<td align="right">188,465,656</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">44,861,967</td>
<td align="right">82,548,969</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">3,894,244,949</td>
<td align="right">713,195,536</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,231,978,550</td>
<td align="right">288,844,627</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">681,859,312</td>
<td align="right">163,828,468</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">501,708,644</td>
<td align="right">130,867,980</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">507,221,525</td>
<td align="right">154,060,722</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">456,927,461</td>
<td align="right">142,796,151</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,424,200,998</td>
<td align="right">4,086,963,299</td>
<td align="right">68.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">458,023,902</td>
<td align="right">143,914,956</td>
<td align="right">-68.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,284,282,025</td>
<td align="right">751,326,469</td>
<td align="right">-67.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,497,208,690</td>
<td align="right">1,509,229,722</td>
<td align="right">-66.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,304,807,465</td>
<td align="right">2,164,671,309</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,445,932,518</td>
<td align="right">1,551,330,027</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,803,845,638</td>
<td align="right">681,043,728</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,808,625,569</td>
<td align="right">691,619,054</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">164,664,559</td>
<td align="right">64,556,561</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">90,376,846</td>
<td align="right">143,780,410</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">140,365,656</td>
<td align="right">61,555,707</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">221,969,774</td>
<td align="right">343,731,286</td>
<td align="right">54.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">108,641,958</td>
<td align="right">50,983,230</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">108,641,958</td>
<td align="right">50,983,230</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">760,386,308</td>
<td align="right">367,065,632</td>
<td align="right">-51.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,059,696,842</td>
<td align="right">1,965,471,434</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">108,754,470</td>
<td align="right">53,363,142</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">551,139,168</td>
<td align="right">278,227,188</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">76,782,406</td>
<td align="right">38,978,381</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,025,841,610</td>
<td align="right">2,054,889,154</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,246,499,635</td>
<td align="right">1,180,369,276</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,302,045,981</td>
<td align="right">689,556,402</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,685,567</td>
<td align="right">5,414,259</td>
<td align="right">46.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">7,278,269,650</td>
<td align="right">3,941,381,809</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">51,235,020</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">186,732,221</td>
<td align="right">106,856,056</td>
<td align="right">-42.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">5,990,195</td>
<td align="right">8,527,170</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">213,804,205</td>
<td align="right">124,353,102</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,713,222,150</td>
<td align="right">1,603,249,884</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,711,639,431</td>
<td align="right">1,011,867,731</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,792,960,382</td>
<td align="right">1,070,925,095</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,082,640,945</td>
<td align="right">650,879,841</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">46,529,798</td>
<td align="right">64,257,946</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,073,355,874</td>
<td align="right">1,482,120,604</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">1,911,764</td>
<td align="right">2,608,914</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">50,176,340</td>
<td align="right">32,565,178</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,614,641,717</td>
<td align="right">1,049,431,202</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">92,069,943</td>
<td align="right">60,229,201</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">57,474,075</td>
<td align="right">37,630,324</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">57,474,075</td>
<td align="right">37,740,046</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">336,432,699</td>
<td align="right">229,208,724</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">720,635,347</td>
<td align="right">497,488,542</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,738,941</td>
<td align="right">53,135,141</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">28,260,933,413</td>
<td align="right">19,884,697,978</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,823,731,413</td>
<td align="right">1,289,902,989</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,854,068,652</td>
<td align="right">3,491,979,354</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">727,968,309</td>
<td align="right">525,137,974</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,359,000,560</td>
<td align="right">987,309,785</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,359,015,122</td>
<td align="right">987,450,655</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">273,499,419</td>
<td align="right">347,257,833</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">10,631,286</td>
<td align="right">13,497,493</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">813,488,778</td>
<td align="right">606,346,955</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">8,457,671,250</td>
<td align="right">6,336,091,103</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">100,465,459</td>
<td align="right">125,381,963</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,953,146,898</td>
<td align="right">1,474,940,463</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">812,629,862</td>
<td align="right">614,065,118</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">165,674,769</td>
<td align="right">204,459,972</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">3,859,515,400</td>
<td align="right">2,967,608,285</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">168,698,546</td>
<td align="right">129,911,524</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">966,747,608</td>
<td align="right">748,252,576</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,003,458,581</td>
<td align="right">779,510,828</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">860,018,576</td>
<td align="right">670,882,162</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">860,214,656</td>
<td align="right">676,735,118</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">373,148,359</td>
<td align="right">294,970,037</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">163,583,998</td>
<td align="right">197,583,475</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">488,213,082</td>
<td align="right">587,482,524</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">488,213,082</td>
<td align="right">587,482,524</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">195,822,026</td>
<td align="right">235,406,770</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">461,800,577</td>
<td align="right">553,858,410</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">7,712,841,284</td>
<td align="right">6,190,938,748</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,983,480,850</td>
<td align="right">3,231,376,163</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">601,219,071</td>
<td align="right">705,187,953</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">344,154,778</td>
<td align="right">286,515,718</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">293,392,160</td>
<td align="right">244,318,760</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">462,079,688</td>
<td align="right">537,141,474</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">293,608,220</td>
<td align="right">247,157,888</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,532,073,942</td>
<td align="right">1,762,122,179</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">965,457,349</td>
<td align="right">1,110,032,162</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">595,295,373</td>
<td align="right">677,893,080</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">455,101,743</td>
<td align="right">516,588,287</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">288,644,996</td>
<td align="right">327,411,094</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">254,690,388</td>
<td align="right">287,219,672</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">230,913,036</td>
<td align="right">201,802,905</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">165,368,488</td>
<td align="right">144,574,939</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">233,998,284</td>
<td align="right">263,404,445</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">37,790,915</td>
<td align="right">42,252,740</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,071,079</td>
<td align="right">52,610,978</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,490,562,819</td>
<td align="right">1,660,438,017</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">529,645,713</td>
<td align="right">580,287,100</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">3,150,271,485</td>
<td align="right">2,852,195,814</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">85,254,326</td>
<td align="right">92,977,677</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">24,864,963</td>
<td align="right">27,033,437</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">24,864,963</td>
<td align="right">27,033,437</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,851,262,755</td>
<td align="right">3,092,836,057</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">24,144,925,467</td>
<td align="right">26,185,769,842</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">146,348,566</td>
<td align="right">134,573,789</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">8,499,029,127</td>
<td align="right">9,178,068,373</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,431,832,253</td>
<td align="right">1,543,697,739</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">49,176,658</td>
<td align="right">45,449,816</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,348,269,311</td>
<td align="right">1,446,134,322</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,054,406,168</td>
<td align="right">1,129,296,345</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">700,405,708</td>
<td align="right">748,926,231</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">41,301,515</td>
<td align="right">44,056,499</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,073,355,874</td>
<td align="right">1,144,807,880</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">39,798,841</td>
<td align="right">42,258,464</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">309,518,630</td>
<td align="right">292,549,305</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">341,542,274</td>
<td align="right">360,197,461</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">78,965,858</td>
<td align="right">83,242,132</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">794,870,255</td>
<td align="right">752,126,885</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">78,198,074</td>
<td align="right">81,967,356</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,009,475,920</td>
<td align="right">1,056,201,237</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">139,366,607</td>
<td align="right">145,266,069</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,308,595,126</td>
<td align="right">2,212,191,513</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,628,879</td>
<td align="right">6,903,178</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">4,700,296,266</td>
<td align="right">4,830,742,776</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">746,405,208</td>
<td align="right">765,616,338</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">60,653,623</td>
<td align="right">62,144,890</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">98,961,397</td>
<td align="right">96,589,784</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,825,193,579</td>
<td align="right">2,882,004,181</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,013,180</td>
<td align="right">61,138,675</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">579,020,387</td>
<td align="right">589,425,208</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">474,452,986</td>
<td align="right">478,594,095</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">266,097,286</td>
<td align="right">267,130,165</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">973,857,421</td>
<td align="right">971,182,362</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">764,033</td>
<td align="right">765,893</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">764,033</td>
<td align="right">765,893</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,837,923,580</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,801,312,135</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">4,123,827,998</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,633,305,254</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,337,994,013</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">528,980,645</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">412,777,290</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">101,999,930</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">62,155,046</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">57,771,648</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">49,691,072</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">40,775,190</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">13,003,580</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">2,703,280</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,421,211</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">41,872,460,957</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right"></td>
<td align="right">3,100,462,135</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right"></td>
<td align="right">490,306,129</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">461,661,663</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_NONE</td>
<td align="right"></td>
<td align="right">198,570,226</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right"></td>
<td align="right">177,295,673</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_CHECK_FUNC</td>
<td align="right"></td>
<td align="right">107,440,654</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_INIT_CALL</td>
<td align="right"></td>
<td align="right">107,440,654</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_FOR</td>
<td align="right"></td>
<td align="right">77,752,885</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">33,473,528</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right"></td>
<td align="right">31,545,060</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right"></td>
<td align="right">27,772,692</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right"></td>
<td align="right">24,805,353</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right"></td>
<td align="right">24,804,644</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right"></td>
<td align="right">13,716,579</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">7,501,118</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right"></td>
<td align="right">7,156,778</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">6,784,091</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right"></td>
<td align="right">6,150,980</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right"></td>
<td align="right">2,233,128</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">908,614</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right"></td>
<td align="right">786,768</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">786,428</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right"></td>
<td align="right">221,197</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right"></td>
<td align="right">202,389</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right"></td>
<td align="right">57,560</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_UPDATE</td>
<td align="right"></td>
<td align="right">18,900</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right"></td>
<td align="right">11,046</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right"></td>
<td align="right">3,564</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_AITER</td>
<td align="right"></td>
<td align="right">60</td>
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
<td align="right">24,089</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,001</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,486</td>
<td align="right"></td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">120</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">120</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
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
<td align="right">2,476</td>
<td align="right">2,456</td>
<td align="right">-0.8%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-12
