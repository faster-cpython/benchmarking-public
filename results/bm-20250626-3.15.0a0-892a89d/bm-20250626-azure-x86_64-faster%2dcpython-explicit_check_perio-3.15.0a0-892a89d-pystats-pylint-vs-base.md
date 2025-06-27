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
<td align="right">975</td>
<td align="right">20,475</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">191</td>
<td align="right">4,011</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">59</td>
<td align="right">1,239</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">29</td>
<td align="right">609</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">15</td>
<td align="right">315</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">10</td>
<td align="right">210</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,957</td>
<td align="right">60,816</td>
<td align="right">1,956.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,687</td>
<td align="right">110,460</td>
<td align="right">1,842.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">783</td>
<td align="right">13,881</td>
<td align="right">1,672.8%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">11,450</td>
<td align="right">195,615</td>
<td align="right">1,608.4%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,729</td>
<td align="right">80,094</td>
<td align="right">1,593.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,011</td>
<td align="right">28,140</td>
<td align="right">1,299.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,121</td>
<td align="right">14,049</td>
<td align="right">1,153.3%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">922</td>
<td align="right">10,395</td>
<td align="right">1,027.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">24,007</td>
<td align="right">254,352</td>
<td align="right">959.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">26,293</td>
<td align="right">241,731</td>
<td align="right">819.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">22,736</td>
<td align="right">203,574</td>
<td align="right">795.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,396</td>
<td align="right">21,294</td>
<td align="right">788.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">522</td>
<td align="right">4,242</td>
<td align="right">712.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">167,374</td>
<td align="right">1,280,790</td>
<td align="right">665.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">942</td>
<td align="right">6,972</td>
<td align="right">640.1%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">261</td>
<td align="right">1,638</td>
<td align="right">527.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">543,485</td>
<td align="right">3,366,023</td>
<td align="right">519.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">136,210</td>
<td align="right">735,838</td>
<td align="right">440.2%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,055</td>
<td align="right">5,502</td>
<td align="right">421.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">714</td>
<td align="right">3,465</td>
<td align="right">385.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,823,051</td>
<td align="right">32,927,394</td>
<td align="right">382.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,034,649</td>
<td align="right">4,873,331</td>
<td align="right">371.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">289,767</td>
<td align="right">1,325,394</td>
<td align="right">357.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">5,604,777</td>
<td align="right">22,310,912</td>
<td align="right">298.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">83,959</td>
<td align="right">333,543</td>
<td align="right">297.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,903,000</td>
<td align="right">27,380,135</td>
<td align="right">246.5%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">960,428</td>
<td align="right">3,323,628</td>
<td align="right">246.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,166,522</td>
<td align="right">3,944,598</td>
<td align="right">238.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,837,376</td>
<td align="right">12,914,790</td>
<td align="right">236.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">7,704,785</td>
<td align="right">25,289,517</td>
<td align="right">228.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">9,779,703</td>
<td align="right">32,034,770</td>
<td align="right">227.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">50,150</td>
<td align="right">164,040</td>
<td align="right">227.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">10,667,555</td>
<td align="right">34,688,176</td>
<td align="right">225.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,995,928</td>
<td align="right">25,268,733</td>
<td align="right">216.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">8,880,726</td>
<td align="right">27,984,222</td>
<td align="right">215.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,780,369</td>
<td align="right">8,480,911</td>
<td align="right">205.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">9,097,362</td>
<td align="right">26,660,355</td>
<td align="right">193.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,049,207</td>
<td align="right">8,846,586</td>
<td align="right">190.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,351,488</td>
<td align="right">3,861,667</td>
<td align="right">185.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">86,671</td>
<td align="right">243,789</td>
<td align="right">181.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">10,377,474</td>
<td align="right">29,081,934</td>
<td align="right">180.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">25,234,108</td>
<td align="right">70,086,676</td>
<td align="right">177.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,385,394</td>
<td align="right">3,687,180</td>
<td align="right">166.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">15,866,183</td>
<td align="right">40,642,680</td>
<td align="right">156.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">341,180</td>
<td align="right">860,559</td>
<td align="right">152.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">35,252,193</td>
<td align="right">86,985,229</td>
<td align="right">146.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">963,841</td>
<td align="right">2,288,665</td>
<td align="right">137.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,364,809</td>
<td align="right">5,548,158</td>
<td align="right">134.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">232,083</td>
<td align="right">532,434</td>
<td align="right">129.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">55,974</td>
<td align="right">127,596</td>
<td align="right">128.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">14,355,886</td>
<td align="right">32,644,962</td>
<td align="right">127.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">786,300</td>
<td align="right">1,787,586</td>
<td align="right">127.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">182,671,739</td>
<td align="right">414,501,747</td>
<td align="right">126.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,808,235</td>
<td align="right">6,334,163</td>
<td align="right">125.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">29,178,096</td>
<td align="right">65,776,416</td>
<td align="right">125.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">197,540</td>
<td align="right">444,969</td>
<td align="right">125.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">311,409</td>
<td align="right">700,791</td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,554,944</td>
<td align="right">5,622,288</td>
<td align="right">120.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">15,564,107</td>
<td align="right">34,240,331</td>
<td align="right">120.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">22,915,488</td>
<td align="right">49,915,522</td>
<td align="right">117.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,343,466</td>
<td align="right">2,924,565</td>
<td align="right">117.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,652,709</td>
<td align="right">10,066,620</td>
<td align="right">116.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,243,648</td>
<td align="right">4,841,584</td>
<td align="right">115.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">14,002</td>
<td align="right">30,156</td>
<td align="right">115.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">3,384,861</td>
<td align="right">7,289,447</td>
<td align="right">115.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">46,314,548</td>
<td align="right">98,932,657</td>
<td align="right">113.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,933,278</td>
<td align="right">4,110,874</td>
<td align="right">112.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">1,063,090</td>
<td align="right">2,213,421</td>
<td align="right">108.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">32,351,611</td>
<td align="right">67,286,995</td>
<td align="right">108.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">48,744,077</td>
<td align="right">100,850,518</td>
<td align="right">106.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">122,296</td>
<td align="right">245,763</td>
<td align="right">101.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">35,576,785</td>
<td align="right">70,738,700</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,552,807</td>
<td align="right">13,004,895</td>
<td align="right">98.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">254,952</td>
<td align="right">504,126</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">3,030</td>
<td align="right">5,985</td>
<td align="right">97.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,829,302</td>
<td align="right">9,522,954</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">614,126</td>
<td align="right">1,195,194</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">614,126</td>
<td align="right">1,195,194</td>
<td align="right">94.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">57,398,106</td>
<td align="right">111,399,284</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">29,015,728</td>
<td align="right">56,202,338</td>
<td align="right">93.7%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">688,601</td>
<td align="right">1,320,606</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">669,232</td>
<td align="right">1,273,755</td>
<td align="right">90.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">26,638,571</td>
<td align="right">50,554,764</td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">42,163</td>
<td align="right">79,674</td>
<td align="right">89.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">16,943,696</td>
<td align="right">31,560,688</td>
<td align="right">86.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">4,240,187</td>
<td align="right">7,779,889</td>
<td align="right">83.5%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">85,285</td>
<td align="right">154,350</td>
<td align="right">81.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">14,887,416</td>
<td align="right">26,909,580</td>
<td align="right">80.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">260,331</td>
<td align="right">465,927</td>
<td align="right">79.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">49,022,713</td>
<td align="right">87,252,584</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,779,932</td>
<td align="right">6,727,390</td>
<td align="right">78.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">57,506,349</td>
<td align="right">101,810,142</td>
<td align="right">77.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">8,581,619</td>
<td align="right">15,120,160</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">4,301,851</td>
<td align="right">7,541,035</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">163,891</td>
<td align="right">285,327</td>
<td align="right">74.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">930,406</td>
<td align="right">1,612,779</td>
<td align="right">73.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">81,525</td>
<td align="right">138,957</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">531,405</td>
<td align="right">902,538</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,737,425</td>
<td align="right">4,613,509</td>
<td align="right">68.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,223,620</td>
<td align="right">5,425,495</td>
<td align="right">68.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,313,358</td>
<td align="right">20,564,393</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">12,265,555</td>
<td align="right">20,405,990</td>
<td align="right">66.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">196,787</td>
<td align="right">326,676</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,666,461</td>
<td align="right">4,414,534</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">25,464,495</td>
<td align="right">42,157,872</td>
<td align="right">65.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">819,855</td>
<td align="right">1,347,927</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,836,698</td>
<td align="right">4,663,155</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">257,149</td>
<td align="right">422,163</td>
<td align="right">64.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">10,081,892</td>
<td align="right">16,426,687</td>
<td align="right">62.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,496,871</td>
<td align="right">2,433,417</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">281,060</td>
<td align="right">455,448</td>
<td align="right">62.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">280,940</td>
<td align="right">452,928</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,617,130</td>
<td align="right">2,564,982</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">622,298</td>
<td align="right">983,457</td>
<td align="right">58.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,586,442</td>
<td align="right">15,091,789</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,930,690</td>
<td align="right">9,181,934</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,197,534</td>
<td align="right">3,391,395</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,766,915</td>
<td align="right">7,354,053</td>
<td align="right">54.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,516,865</td>
<td align="right">6,846,126</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,625,053</td>
<td align="right">8,512,224</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">822,943</td>
<td align="right">1,236,438</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">820,138</td>
<td align="right">1,231,820</td>
<td align="right">50.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,108,709</td>
<td align="right">3,090,213</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,887,083</td>
<td align="right">4,203,255</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">984,602</td>
<td align="right">1,427,055</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">37,326,398</td>
<td align="right">53,746,764</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,030,194</td>
<td align="right">1,480,101</td>
<td align="right">43.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">2,018,058</td>
<td align="right">2,837,310</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,407,659</td>
<td align="right">4,736,712</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,420,183</td>
<td align="right">6,087,231</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,970</td>
<td align="right">74,319</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,955,567</td>
<td align="right">2,623,236</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">11,857,179</td>
<td align="right">15,884,181</td>
<td align="right">34.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,743,700</td>
<td align="right">2,327,892</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">84</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">63</td>
<td align="right">42</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">42,789</td>
<td align="right">56,952</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,788,559</td>
<td align="right">2,324,838</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,546,184</td>
<td align="right">1,993,593</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">165,054</td>
<td align="right">212,394</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">353,412</td>
<td align="right">451,731</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">614,516</td>
<td align="right">771,204</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,375,010</td>
<td align="right">1,693,671</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,081</td>
<td align="right">120,267</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">437,896</td>
<td align="right">536,256</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">20,383,717</td>
<td align="right">24,898,221</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,874,655</td>
<td align="right">3,509,289</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">1,795,405</td>
<td align="right">2,158,317</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">795,570</td>
<td align="right">941,703</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">108,646</td>
<td align="right">128,205</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,814,327</td>
<td align="right">6,786,297</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">76,123</td>
<td align="right">87,234</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">11,715,926</td>
<td align="right">13,413,813</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">1,292,815</td>
<td align="right">1,470,189</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">5,370,242</td>
<td align="right">6,083,058</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">47,641</td>
<td align="right">53,802</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,219,331</td>
<td align="right">12,650,463</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">14,616,001</td>
<td align="right">16,452,870</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">5,420,872</td>
<td align="right">6,065,283</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">8,150,099</td>
<td align="right">9,075,216</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">1,086,743</td>
<td align="right">1,195,761</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">3,689,757</td>
<td align="right">4,036,200</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">2,355,148</td>
<td align="right">2,535,078</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">19,652</td>
<td align="right">20,706</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,494,864</td>
<td align="right">6,825,525</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">468,526</td>
<td align="right">490,308</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,257,421</td>
<td align="right">8,626,968</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">63,725</td>
<td align="right">66,528</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,151,847</td>
<td align="right">8,496,663</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">18,923</td>
<td align="right">18,207</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">5,331,831</td>
<td align="right">5,476,359</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">192</td>
<td align="right">189</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,238,816</td>
<td align="right">1,227,975</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,426</td>
<td align="right">72,135</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CHECK_PERIODIC</td>
<td align="right"></td>
<td align="right">64,097,743</td>
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
<td align="right">3,213,464</td>
<td align="right">12.1%</td>
<td align="right">5,390,593</td>
<td align="right">15.1%</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,162,625</td>
<td align="right">87.2%</td>
<td align="right">30,142,812</td>
<td align="right">84.3%</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,741</td>
<td align="right">0.6%</td>
<td align="right">191,146</td>
<td align="right">0.5%</td>
<td align="right">16.7%</td>
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
<td align="right">5,029</td>
<td align="right">38.0%</td>
<td align="right">16,821</td>
<td align="right">43.8%</td>
<td align="right">234.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,221</td>
<td align="right">62.0%</td>
<td align="right">21,567</td>
<td align="right">56.2%</td>
<td align="right">162.3%</td>
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
<td align="left">lshift</td>
<td align="right">10</td>
<td align="right">0.1%</td>
<td align="right">210</td>
<td align="right">1.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">9</td>
<td align="right">0.1%</td>
<td align="right">189</td>
<td align="right">0.9%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">147</td>
<td align="right">0.7%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">4</td>
<td align="right">0.0%</td>
<td align="right">84</td>
<td align="right">0.4%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">subscr range</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">36</td>
<td align="right">0.4%</td>
<td align="right">336</td>
<td align="right">1.6%</td>
<td align="right">833.3%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.3%</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">384.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">200</td>
<td align="right">2.4%</td>
<td align="right">777</td>
<td align="right">3.6%</td>
<td align="right">288.5%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">808</td>
<td align="right">9.8%</td>
<td align="right">2,961</td>
<td align="right">13.7%</td>
<td align="right">266.5%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">986</td>
<td align="right">12.0%</td>
<td align="right">3,381</td>
<td align="right">15.7%</td>
<td align="right">242.9%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">715</td>
<td align="right">8.7%</td>
<td align="right">2,310</td>
<td align="right">10.7%</td>
<td align="right">223.1%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">743</td>
<td align="right">9.0%</td>
<td align="right">2,310</td>
<td align="right">10.7%</td>
<td align="right">210.9%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">117</td>
<td align="right">1.4%</td>
<td align="right">336</td>
<td align="right">1.6%</td>
<td align="right">187.2%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">23</td>
<td align="right">0.3%</td>
<td align="right">63</td>
<td align="right">0.3%</td>
<td align="right">173.9%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">326</td>
<td align="right">4.0%</td>
<td align="right">882</td>
<td align="right">4.1%</td>
<td align="right">170.6%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">47</td>
<td align="right">0.6%</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">168.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">232</td>
<td align="right">2.8%</td>
<td align="right">588</td>
<td align="right">2.7%</td>
<td align="right">153.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,655</td>
<td align="right">44.5%</td>
<td align="right">6,027</td>
<td align="right">27.9%</td>
<td align="right">64.9%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.8%</td>
<td align="right">105</td>
<td align="right">0.5%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">152</td>
<td align="right">1.8%</td>
<td align="right">210</td>
<td align="right">1.0%</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
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
<td align="right">614,516</td>
<td align="right">100.0%</td>
<td align="right">771,204</td>
<td align="right">100.0%</td>
<td align="right">25.5%</td>
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
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">14,445,707</td>
<td align="right">11.3%</td>
<td align="right">169,590.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">58,500,680</td>
<td align="right">87.8%</td>
<td align="right">113,500,817</td>
<td align="right">88.5%</td>
<td align="right">94.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,933,259</td>
<td align="right">11.9%</td>
<td align="right">14,314,644</td>
<td align="right">11.2%</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,078,729</td>
<td align="right">12.1%</td>
<td align="right">14,445,707</td>
<td align="right">11.3%</td>
<td align="right">78.8%</td>
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
<td align="right">171,763</td>
<td align="right">100.0%</td>
<td align="right">372,794</td>
<td align="right">100.0%</td>
<td align="right">117.0%</td>
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
<td align="left">init not simple</td>
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
<td align="right">483</td>
<td align="right">483 / 0 !!</td>
<td align="right">666.7%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">568,395</td>
<td align="right">97.8%</td>
<td align="right">636,615</td>
<td align="right">96.7%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">578,755</td>
<td align="right">99.6%</td>
<td align="right">637,287</td>
<td align="right">96.8%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">637,287</td>
<td align="right">96.8%</td>
<td align="right"></td>
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
<td align="right">12,756</td>
<td align="right">100.0%</td>
<td align="right">21,966</td>
<td align="right">100.0%</td>
<td align="right">72.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,320</td>
<td align="right">0.0%</td>
<td align="right">29,484</td>
<td align="right">0.1%</td>
<td align="right">788.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,030,664</td>
<td align="right">5.7%</td>
<td align="right">4,850,544</td>
<td align="right">11.6%</td>
<td align="right">370.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,028,447</td>
<td align="right">94.3%</td>
<td align="right">37,036,926</td>
<td align="right">88.3%</td>
<td align="right">117.5%</td>
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
<td align="right">1,506</td>
<td align="right">37.2%</td>
<td align="right">12,285</td>
<td align="right">52.7%</td>
<td align="right">715.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,546</td>
<td align="right">62.8%</td>
<td align="right">11,048</td>
<td align="right">47.3%</td>
<td align="right">333.9%</td>
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
<td align="right">20</td>
<td align="right">0.8%</td>
<td align="right">420</td>
<td align="right">3.8%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.2%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">670</td>
<td align="right">26.3%</td>
<td align="right">4,326</td>
<td align="right">39.2%</td>
<td align="right">545.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">143</td>
<td align="right">5.6%</td>
<td align="right">882</td>
<td align="right">8.0%</td>
<td align="right">516.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">182</td>
<td align="right">7.1%</td>
<td align="right">882</td>
<td align="right">8.0%</td>
<td align="right">384.6%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">51</td>
<td align="right">2.0%</td>
<td align="right">210</td>
<td align="right">1.9%</td>
<td align="right">311.8%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">168</td>
<td align="right">1.5%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,103</td>
<td align="right">43.3%</td>
<td align="right">3,591</td>
<td align="right">32.5%</td>
<td align="right">225.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">90</td>
<td align="right">3.5%</td>
<td align="right">168</td>
<td align="right">1.5%</td>
<td align="right">86.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">237</td>
<td align="right">9.3%</td>
<td align="right">359</td>
<td align="right">3.2%</td>
<td align="right">51.5%</td>
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
<td align="right">4,104,251</td>
<td align="right">54.4%</td>
<td align="right">7,475,830</td>
<td align="right">61.1%</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,400,443</td>
<td align="right">45.1%</td>
<td align="right">4,713,770</td>
<td align="right">38.5%</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">26,561</td>
<td align="right">0.4%</td>
<td align="right">26,439</td>
<td align="right">0.2%</td>
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
<td align="left">Success</td>
<td align="right">1,219</td>
<td align="right">15.8%</td>
<td align="right">4,851</td>
<td align="right">20.7%</td>
<td align="right">297.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,508</td>
<td align="right">84.2%</td>
<td align="right">18,574</td>
<td align="right">79.3%</td>
<td align="right">185.4%</td>
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
<td align="right">638</td>
<td align="right">9.8%</td>
<td align="right">2,373</td>
<td align="right">12.8%</td>
<td align="right">271.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,185</td>
<td align="right">18.2%</td>
<td align="right">3,759</td>
<td align="right">20.2%</td>
<td align="right">217.2%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,356</td>
<td align="right">20.8%</td>
<td align="right">4,221</td>
<td align="right">22.7%</td>
<td align="right">211.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,329</td>
<td align="right">51.2%</td>
<td align="right">8,221</td>
<td align="right">44.3%</td>
<td align="right">147.0%</td>
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
<td align="right">33,297,319</td>
<td align="right">84.6%</td>
<td align="right">65,811,304</td>
<td align="right">90.4%</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,804,049</td>
<td align="right">14.8%</td>
<td align="right">6,748,749</td>
<td align="right">9.3%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">225,565</td>
<td align="right">0.6%</td>
<td align="right">231,084</td>
<td align="right">0.3%</td>
<td align="right">2.4%</td>
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
<td align="right">5,494</td>
<td align="right">37.8%</td>
<td align="right">19,488</td>
<td align="right">46.5%</td>
<td align="right">254.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">9,036</td>
<td align="right">62.2%</td>
<td align="right">22,386</td>
<td align="right">53.5%</td>
<td align="right">147.7%</td>
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
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">231</td>
<td align="right">1.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">9</td>
<td align="right">0.1%</td>
<td align="right">189</td>
<td align="right">0.8%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">256</td>
<td align="right">2.8%</td>
<td align="right">1,155</td>
<td align="right">5.2%</td>
<td align="right">351.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">171</td>
<td align="right">1.9%</td>
<td align="right">630</td>
<td align="right">2.8%</td>
<td align="right">268.4%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">146</td>
<td align="right">1.6%</td>
<td align="right">525</td>
<td align="right">2.3%</td>
<td align="right">259.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">578</td>
<td align="right">6.4%</td>
<td align="right">1,953</td>
<td align="right">8.7%</td>
<td align="right">237.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,468</td>
<td align="right">16.2%</td>
<td align="right">4,935</td>
<td align="right">22.0%</td>
<td align="right">236.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1,556</td>
<td align="right">17.2%</td>
<td align="right">4,893</td>
<td align="right">21.9%</td>
<td align="right">214.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">306</td>
<td align="right">3.4%</td>
<td align="right">924</td>
<td align="right">4.1%</td>
<td align="right">202.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">46</td>
<td align="right">0.5%</td>
<td align="right">126</td>
<td align="right">0.6%</td>
<td align="right">173.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">251</td>
<td align="right">2.8%</td>
<td align="right">630</td>
<td align="right">2.8%</td>
<td align="right">151.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">4,237</td>
<td align="right">46.9%</td>
<td align="right">6,174</td>
<td align="right">27.6%</td>
<td align="right">45.7%</td>
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
<td align="left">bytes</td>
<td align="right">3</td>
<td align="right">3 / 0 !!</td>
<td align="right">63</td>
<td align="right">63 / 0 !!</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">629</td>
<td align="right">629 / 0 !!</td>
<td align="right">6,804</td>
<td align="right">6,804 / 0 !!</td>
<td align="right">981.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,228,641</td>
<td align="right">1,228,641 / 0 !!</td>
<td align="right">3,654,292</td>
<td align="right">3,654,292 / 0 !!</td>
<td align="right">197.4%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">4,412,967</td>
<td align="right">4,412,967 / 0 !!</td>
<td align="right">9,144,742</td>
<td align="right">9,144,742 / 0 !!</td>
<td align="right">107.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">7,668</td>
<td align="right">7,668 / 0 !!</td>
<td align="right">13,713</td>
<td align="right">13,713 / 0 !!</td>
<td align="right">78.8%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">161,360</td>
<td align="right">161,360 / 0 !!</td>
<td align="right">243,705</td>
<td align="right">243,705 / 0 !!</td>
<td align="right">51.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">609,320</td>
<td align="right">609,320 / 0 !!</td>
<td align="right">858,081</td>
<td align="right">858,081 / 0 !!</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">552,640</td>
<td align="right">552,640 / 0 !!</td>
<td align="right">728,469</td>
<td align="right">728,469 / 0 !!</td>
<td align="right">31.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">285,344</td>
<td align="right">285,344 / 0 !!</td>
<td align="right">363,510</td>
<td align="right">363,510 / 0 !!</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">5,054,786</td>
<td align="right">5,054,786 / 0 !!</td>
<td align="right">5,551,014</td>
<td align="right">5,551,014 / 0 !!</td>
<td align="right">9.8%</td>
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
<td align="right">14,217,051</td>
<td align="right">11.1%</td>
<td align="right">32,146,380</td>
<td align="right">13.1%</td>
<td align="right">126.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">80,054,169</td>
<td align="right">62.4%</td>
<td align="right">164,428,093</td>
<td align="right">67.0%</td>
<td align="right">105.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">198,684</td>
<td align="right">0.2%</td>
<td align="right">341,082</td>
<td align="right">0.1%</td>
<td align="right">71.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">33,812,786</td>
<td align="right">26.4%</td>
<td align="right">48,355,354</td>
<td align="right">19.7%</td>
<td align="right">43.0%</td>
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
<td align="right">78,110</td>
<td align="right">10.6%</td>
<td align="right">193,557</td>
<td align="right">15.8%</td>
<td align="right">147.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">656,170</td>
<td align="right">89.4%</td>
<td align="right">1,030,512</td>
<td align="right">84.2%</td>
<td align="right">57.0%</td>
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
<td align="left">expected error</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">105</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,580</td>
<td align="right">2.0%</td>
<td align="right">21,063</td>
<td align="right">10.9%</td>
<td align="right">1,233.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">66</td>
<td align="right">0.1%</td>
<td align="right">546</td>
<td align="right">0.3%</td>
<td align="right">727.3%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">117</td>
<td align="right">0.1%</td>
<td align="right">756</td>
<td align="right">0.4%</td>
<td align="right">546.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">905</td>
<td align="right">1.2%</td>
<td align="right">4,536</td>
<td align="right">2.3%</td>
<td align="right">401.2%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3,986</td>
<td align="right">5.1%</td>
<td align="right">18,942</td>
<td align="right">9.8%</td>
<td align="right">375.2%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,624</td>
<td align="right">4.6%</td>
<td align="right">15,624</td>
<td align="right">8.1%</td>
<td align="right">331.1%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">255</td>
<td align="right">0.3%</td>
<td align="right">1,092</td>
<td align="right">0.6%</td>
<td align="right">328.2%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">203</td>
<td align="right">0.3%</td>
<td align="right">840</td>
<td align="right">0.4%</td>
<td align="right">313.8%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">450</td>
<td align="right">0.6%</td>
<td align="right">1,806</td>
<td align="right">0.9%</td>
<td align="right">301.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">193</td>
<td align="right">0.2%</td>
<td align="right">609</td>
<td align="right">0.3%</td>
<td align="right">215.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,565</td>
<td align="right">2.0%</td>
<td align="right">3,591</td>
<td align="right">1.9%</td>
<td align="right">129.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">836</td>
<td align="right">1.1%</td>
<td align="right">1,869</td>
<td align="right">1.0%</td>
<td align="right">123.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">42</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,950</td>
<td align="right">0.0%</td>
<td align="right">103,509</td>
<td align="right">0.1%</td>
<td align="right">1,991.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,348</td>
<td align="right">0.0%</td>
<td align="right">41,160</td>
<td align="right">0.0%</td>
<td align="right">846.6%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">435</td>
<td align="right">0.0%</td>
<td align="right">1,134</td>
<td align="right">0.0%</td>
<td align="right">160.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">61,525,359</td>
<td align="right">100.0%</td>
<td align="right">133,022,251</td>
<td align="right">99.8%</td>
<td align="right">116.2%</td>
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
<td align="right">17,854</td>
<td align="right">100.0%</td>
<td align="right">100,611</td>
<td align="right">100.0%</td>
<td align="right">463.5%</td>
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
<td align="right">101</td>
<td align="right">0.0%</td>
<td align="right">2,121</td>
<td align="right">0.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">708,539</td>
<td align="right">99.9%</td>
<td align="right">3,578,417</td>
<td align="right">99.9%</td>
<td align="right">405.0%</td>
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
<td align="right">421</td>
<td align="right">100.0%</td>
<td align="right">2,121</td>
<td align="right">100.0%</td>
<td align="right">403.8%</td>
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
<td align="right">6,491,901</td>
<td align="right">54.9%</td>
<td align="right">6,815,697</td>
<td align="right">55.4%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,331,831</td>
<td align="right">45.1%</td>
<td align="right">5,476,359</td>
<td align="right">44.5%</td>
<td align="right">2.7%</td>
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
<td align="right">103</td>
<td align="right">3.5%</td>
<td align="right">903</td>
<td align="right">9.2%</td>
<td align="right">776.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,860</td>
<td align="right">96.5%</td>
<td align="right">8,925</td>
<td align="right">90.8%</td>
<td align="right">212.1%</td>
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
<td align="right">51</td>
<td align="right">1.8%</td>
<td align="right">210</td>
<td align="right">2.4%</td>
<td align="right">311.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,057</td>
<td align="right">71.9%</td>
<td align="right">6,594</td>
<td align="right">73.9%</td>
<td align="right">220.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">26.3%</td>
<td align="right">2,121</td>
<td align="right">23.8%</td>
<td align="right">182.0%</td>
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
<td align="right">1,728,748</td>
<td align="right">12.5%</td>
<td align="right">13,712,937</td>
<td align="right">30.4%</td>
<td align="right">693.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,378,083</td>
<td align="right">9.9%</td>
<td align="right">3,657,780</td>
<td align="right">8.1%</td>
<td align="right">165.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,738,279</td>
<td align="right">77.5%</td>
<td align="right">27,744,888</td>
<td align="right">61.5%</td>
<td align="right">158.4%</td>
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
<td align="right">36,745</td>
<td align="right">92.3%</td>
<td align="right">271,299</td>
<td align="right">94.3%</td>
<td align="right">638.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,073</td>
<td align="right">7.7%</td>
<td align="right">16,422</td>
<td align="right">5.7%</td>
<td align="right">434.4%</td>
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
<td align="right">52</td>
<td align="right">1.7%</td>
<td align="right">1,092</td>
<td align="right">6.6%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">10</td>
<td align="right">0.3%</td>
<td align="right">210</td>
<td align="right">1.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">8</td>
<td align="right">0.3%</td>
<td align="right">168</td>
<td align="right">1.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">0.3%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">49</td>
<td align="right">1.6%</td>
<td align="right">609</td>
<td align="right">3.7%</td>
<td align="right">1,142.9%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">280</td>
<td align="right">9.1%</td>
<td align="right">3,360</td>
<td align="right">20.5%</td>
<td align="right">1,100.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,385</td>
<td align="right">45.1%</td>
<td align="right">7,539</td>
<td align="right">45.9%</td>
<td align="right">444.3%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">572</td>
<td align="right">18.6%</td>
<td align="right">1,869</td>
<td align="right">11.4%</td>
<td align="right">226.7%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">230</td>
<td align="right">7.5%</td>
<td align="right">630</td>
<td align="right">3.8%</td>
<td align="right">173.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">63,111</td>
<td align="right">2,053.7%</td>
<td align="right">118,251</td>
<td align="right">720.1%</td>
<td align="right">87.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">401</td>
<td align="right">13.0%</td>
<td align="right">441</td>
<td align="right">2.7%</td>
<td align="right">10.0%</td>
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
<td align="right">29</td>
<td align="right">100.0%</td>
<td align="right">609</td>
<td align="right">100.0%</td>
<td align="right">2,000.0%</td>
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
<td align="right">85,898</td>
<td align="right">3.2%</td>
<td align="right">239,757</td>
<td align="right">6.2%</td>
<td align="right">179.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,583,614</td>
<td align="right">96.8%</td>
<td align="right">3,629,178</td>
<td align="right">93.7%</td>
<td align="right">40.5%</td>
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
<td align="right">341</td>
<td align="right">44.1%</td>
<td align="right">2,121</td>
<td align="right">52.6%</td>
<td align="right">522.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">432</td>
<td align="right">55.9%</td>
<td align="right">1,911</td>
<td align="right">47.4%</td>
<td align="right">342.4%</td>
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
<td align="left">bytearray int</td>
<td align="right">21</td>
<td align="right">4.9%</td>
<td align="right">441</td>
<td align="right">23.1%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">6</td>
<td align="right">1.4%</td>
<td align="right">126</td>
<td align="right">6.6%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">25</td>
<td align="right">5.8%</td>
<td align="right">105</td>
<td align="right">5.5%</td>
<td align="right">320.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">48</td>
<td align="right">11.1%</td>
<td align="right">168</td>
<td align="right">8.8%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">240</td>
<td align="right">55.6%</td>
<td align="right">819</td>
<td align="right">42.9%</td>
<td align="right">241.2%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">92</td>
<td align="right">21.3%</td>
<td align="right">252</td>
<td align="right">13.2%</td>
<td align="right">173.9%</td>
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
<td align="right">40,991,329</td>
<td align="right">90.0%</td>
<td align="right">97,311,467</td>
<td align="right">91.1%</td>
<td align="right">137.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,954,393</td>
<td align="right">8.7%</td>
<td align="right">8,539,020</td>
<td align="right">8.0%</td>
<td align="right">115.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">608,231</td>
<td align="right">1.3%</td>
<td align="right">917,454</td>
<td align="right">0.9%</td>
<td align="right">50.8%</td>
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
<td align="right">81,779</td>
<td align="right">92.5%</td>
<td align="right">209,013</td>
<td align="right">92.6%</td>
<td align="right">155.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">6,623</td>
<td align="right">7.5%</td>
<td align="right">16,758</td>
<td align="right">7.4%</td>
<td align="right">153.0%</td>
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
<td align="right">134</td>
<td align="right">2.0%</td>
<td align="right">1,113</td>
<td align="right">6.6%</td>
<td align="right">730.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">27</td>
<td align="right">0.4%</td>
<td align="right">147</td>
<td align="right">0.9%</td>
<td align="right">444.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">50</td>
<td align="right">0.8%</td>
<td align="right">210</td>
<td align="right">1.3%</td>
<td align="right">320.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">325</td>
<td align="right">4.9%</td>
<td align="right">1,239</td>
<td align="right">7.4%</td>
<td align="right">281.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">3,973</td>
<td align="right">60.0%</td>
<td align="right">10,626</td>
<td align="right">63.4%</td>
<td align="right">167.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">888</td>
<td align="right">13.4%</td>
<td align="right">1,617</td>
<td align="right">9.6%</td>
<td align="right">82.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">664</td>
<td align="right">10.0%</td>
<td align="right">1,050</td>
<td align="right">6.3%</td>
<td align="right">58.1%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">562</td>
<td align="right">8.5%</td>
<td align="right">756</td>
<td align="right">4.5%</td>
<td align="right">34.5%</td>
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
<td align="right">7,816,461</td>
<td align="right">86.3%</td>
<td align="right">25,423,707</td>
<td align="right">95.4%</td>
<td align="right">225.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,237,654</td>
<td align="right">13.7%</td>
<td align="right">1,222,599</td>
<td align="right">4.6%</td>
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
<td align="left">Success</td>
<td align="right">790</td>
<td align="right">68.0%</td>
<td align="right">4,410</td>
<td align="right">82.0%</td>
<td align="right">458.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">372</td>
<td align="right">32.0%</td>
<td align="right">966</td>
<td align="right">18.0%</td>
<td align="right">159.7%</td>
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
<td align="left">iterator</td>
<td align="right">24</td>
<td align="right">6.5%</td>
<td align="right">84</td>
<td align="right">8.7%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">348</td>
<td align="right">93.5%</td>
<td align="right">882</td>
<td align="right">91.3%</td>
<td align="right">153.4%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">696,247,960</td>
<td align="right">56.4%</td>
<td align="right">1,473,322,552</td>
<td align="right">57.6%</td>
<td align="right">111.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">439,008,268</td>
<td align="right">35.6%</td>
<td align="right">910,750,133</td>
<td align="right">35.6%</td>
<td align="right">107.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">48,577,256</td>
<td align="right">3.9%</td>
<td align="right">86,213,085</td>
<td align="right">3.4%</td>
<td align="right">77.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">50,644,034</td>
<td align="right">4.1%</td>
<td align="right">89,241,770</td>
<td align="right">3.5%</td>
<td align="right">76.2%</td>
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
<td align="right">1,030,664</td>
<td align="right">2.2%</td>
<td align="right">4,850,544</td>
<td align="right">5.9%</td>
<td align="right">370.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,378,083</td>
<td align="right">3.0%</td>
<td align="right">3,657,780</td>
<td align="right">4.4%</td>
<td align="right">165.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">14,217,051</td>
<td align="right">30.5%</td>
<td align="right">32,146,380</td>
<td align="right">39.0%</td>
<td align="right">126.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">7,933,259</td>
<td align="right">17.0%</td>
<td align="right">14,314,644</td>
<td align="right">17.3%</td>
<td align="right">80.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">3,213,464</td>
<td align="right">6.9%</td>
<td align="right">5,390,593</td>
<td align="right">6.5%</td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,400,443</td>
<td align="right">7.3%</td>
<td align="right">4,713,770</td>
<td align="right">5.7%</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">5,804,049</td>
<td align="right">12.5%</td>
<td align="right">6,748,749</td>
<td align="right">8.2%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,491,901</td>
<td align="right">13.9%</td>
<td align="right">6,815,697</td>
<td align="right">8.3%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,237,654</td>
<td align="right">2.7%</td>
<td align="right">1,222,599</td>
<td align="right">1.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">614,516</td>
<td align="right">1.3%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">917,454</td>
<td align="right">1.1%</td>
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
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,728,685</td>
<td align="right">3.6%</td>
<td align="right">13,712,895</td>
<td align="right">15.9%</td>
<td align="right">693.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,003,396</td>
<td align="right">2.1%</td>
<td align="right">3,664,899</td>
<td align="right">4.3%</td>
<td align="right">265.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,347,676</td>
<td align="right">6.9%</td>
<td align="right">7,107,261</td>
<td align="right">8.2%</td>
<td align="right">112.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,607,247</td>
<td align="right">11.5%</td>
<td align="right">10,576,500</td>
<td align="right">12.3%</td>
<td align="right">88.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,216,524</td>
<td align="right">6.6%</td>
<td align="right">5,268,291</td>
<td align="right">6.1%</td>
<td align="right">63.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,341,890</td>
<td align="right">11.0%</td>
<td align="right">8,635,179</td>
<td align="right">10.0%</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,632,404</td>
<td align="right">3.4%</td>
<td align="right">2,341,015</td>
<td align="right">2.7%</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">7,833,776</td>
<td align="right">16.1%</td>
<td align="right">10,387,881</td>
<td align="right">12.0%</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">16,088,964</td>
<td align="right">33.1%</td>
<td align="right">18,348,120</td>
<td align="right">21.3%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">538,208</td>
<td align="right">1.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">2,328,438</td>
<td align="right">2.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">69</td>
<td align="right">0.0%</td>
<td align="right">1,449</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">236</td>
<td align="right">0.0%</td>
<td align="right">3,675</td>
<td align="right">0.0%</td>
<td align="right">1,457.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">922</td>
<td align="right">0.0%</td>
<td align="right">10,395</td>
<td align="right">0.0%</td>
<td align="right">1,027.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,127,300</td>
<td align="right">8.9%</td>
<td align="right">24,772,838</td>
<td align="right">19.9%</td>
<td align="right">304.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,126,142</td>
<td align="right">8.9%</td>
<td align="right">24,758,768</td>
<td align="right">19.9%</td>
<td align="right">304.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,127,437</td>
<td align="right">1.6%</td>
<td align="right">4,325,471</td>
<td align="right">3.5%</td>
<td align="right">283.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">8,123,850</td>
<td align="right">11.8%</td>
<td align="right">27,746,291</td>
<td align="right">22.3%</td>
<td align="right">241.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">8,123,850</td>
<td align="right">11.8%</td>
<td align="right">27,746,291</td>
<td align="right">22.3%</td>
<td align="right">241.5%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">47,694,610</td>
<td align="right">69.3%</td>
<td align="right">100,759,321</td>
<td align="right">81.0%</td>
<td align="right">111.3%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">870,816</td>
<td align="right">1.3%</td>
<td align="right">1,677,753</td>
<td align="right">1.3%</td>
<td align="right">92.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">60,670,767</td>
<td align="right">88.2%</td>
<td align="right">96,655,206</td>
<td align="right">77.7%</td>
<td align="right">59.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">451,945</td>
<td align="right">0.7%</td>
<td align="right">682,689</td>
<td align="right">0.5%</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">373,487</td>
<td align="right">0.5%</td>
<td align="right">561,595</td>
<td align="right">0.5%</td>
<td align="right">50.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">1,996,550</td>
<td align="right">2.9%</td>
<td align="right">2,973,453</td>
<td align="right">2.4%</td>
<td align="right">48.9%</td>
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
<td align="left">Materialize dict (new key)</td>
<td align="right">4,842</td>
<td align="right">0.4%</td>
<td align="right">37,632</td>
<td align="right">0.9%</td>
<td align="right">677.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">38,139</td>
<td align="right">0.0%</td>
<td align="right">227,094</td>
<td align="right">0.1%</td>
<td align="right">495.4%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">95,819</td>
<td align="right">8.7%</td>
<td align="right">366,114</td>
<td align="right">9.2%</td>
<td align="right">282.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,098,574</td>
<td align="right"></td>
<td align="right">3,978,070</td>
<td align="right"></td>
<td align="right">262.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">143,551,933</td>
<td align="right">18.3%</td>
<td align="right">348,968,541</td>
<td align="right">22.5%</td>
<td align="right">143.1%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">176,036,320</td>
<td align="right">23.3%</td>
<td align="right">419,598,367</td>
<td align="right">27.3%</td>
<td align="right">138.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">214,840</td>
<td align="right"></td>
<td align="right">483,059</td>
<td align="right"></td>
<td align="right">124.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">274,593,005</td>
<td align="right">36.3%</td>
<td align="right">594,506,457</td>
<td align="right">38.6%</td>
<td align="right">116.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">46,872,423</td>
<td align="right">52.7%</td>
<td align="right">98,404,471</td>
<td align="right">56.5%</td>
<td align="right">109.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">47,222,547</td>
<td align="right">53.1%</td>
<td align="right">99,120,235</td>
<td align="right">56.9%</td>
<td align="right">109.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">54,636,427</td>
<td align="right"></td>
<td align="right">113,147,449</td>
<td align="right"></td>
<td align="right">107.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,786,824</td>
<td align="right"></td>
<td align="right">3,600,786</td>
<td align="right"></td>
<td align="right">101.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,573,919</td>
<td align="right"></td>
<td align="right">3,145,838</td>
<td align="right"></td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">371,295,728</td>
<td align="right">47.3%</td>
<td align="right">738,155,062</td>
<td align="right">47.5%</td>
<td align="right">98.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">45,831,811</td>
<td align="right"></td>
<td align="right">86,978,870</td>
<td align="right"></td>
<td align="right">89.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">29,052,519</td>
<td align="right"></td>
<td align="right">55,044,776</td>
<td align="right"></td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">41,642,573</td>
<td align="right">46.9%</td>
<td align="right">75,003,988</td>
<td align="right">43.1%</td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">41,667,142</td>
<td align="right"></td>
<td align="right">75,044,478</td>
<td align="right"></td>
<td align="right">80.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">243,417,493</td>
<td align="right">31.0%</td>
<td align="right">429,696,963</td>
<td align="right">27.7%</td>
<td align="right">76.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">40,138,539</td>
<td align="right">5.3%</td>
<td align="right">70,252,773</td>
<td align="right">4.6%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">265,305,914</td>
<td align="right">35.1%</td>
<td align="right">455,233,539</td>
<td align="right">29.6%</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">311,985</td>
<td align="right">0.4%</td>
<td align="right">488,670</td>
<td align="right">0.3%</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">27,270,184</td>
<td align="right">3.5%</td>
<td align="right">36,267,949</td>
<td align="right">2.3%</td>
<td align="right">33.0%</td>
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
<td align="right">1,309</td>
<td align="right">26,808</td>
<td align="right">69,801,832</td>
<td align="right">10,194,626</td>
<td align="right">2,224,915</td>
<td align="right">4,872</td>
<td align="right">65,289</td>
<td align="right">154,164,293</td>
<td align="right">19,090,583</td>
<td align="right">7,313,265</td>
</tr>
<tr>
<td align="right">2</td>
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
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">12</td>
<td align="right">252</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">12</td>
<td align="right">252</td>
<td align="right">2,000.0%</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-06-27
